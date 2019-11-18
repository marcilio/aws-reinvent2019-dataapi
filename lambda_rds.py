
#================================================================================
# This is the original Lambda code that is being refactored.
#
# 1) The code interacts with an Amazon RDS MySQL database
# 2) The code uses a persistent connection to issue SQL statements against the database
#================================================================================

import json
import random
import boto3
import pymysql

# Database settings (RDS MySQL)
db_endpoint  = 'payrolldbinstance.c0zzsasfu9vl.us-east-1.rds.amazonaws.com'
db_name = 'PayrollDB'
db_port = 3306
db_employee_table = 'Employee'

# Secrets Manager Settings
secret_name = 'ExampleDBCredentials'
secrets_client = boto3.client('secretsmanager')

# Constants
EMP_ID = 'EmpId'
EMP_NAME = 'EmpName'
INSERT_EMPLOYEE_STMT  = f'INSERT INTO {db_employee_table} ({EMP_ID}, {EMP_NAME}) VALUES (%s, %s)'
QUERY_ALL_EMPLOYEE_STMT  = f'SELECT {EMP_ID}, {EMP_NAME} FROM {db_employee_table}'

# Get DB credentials from AWS Secrets Manager
try:
    secret_response = secrets_client.get_secret_value(SecretId=secret_name)
except Exception as e:
    print(f'Could not retrieve the database credentials from AWS Secrets Manager: {e}')
    raise e
else:
    secret_string = json.loads(secret_response['SecretString'])
    db_username = secret_string['user']
    db_password = secret_string['password']

# Initialize the Database Connection
try:
    conn = pymysql.connect(db_endpoint, user=db_username, passwd=password, db=db_name, connect_timeout=5, port=db_port)
except pymysql.MySQLError as e:
    print(f'Could not connect to MySQL instance: {e}')
    raise e

def add_new_employee(conn, emp_id, emp_name):
    '''
    Adds a new employee to the database
    '''
    try:
        with conn.cursor() as cur:
            print(f'Inserting employee {emp_id}')
            cur.execute(INSERT_EMPLOYEE_STMT, (emp_id, emp_name))
    except Exception as e:
        print(f'Oops, something went wrong adding a new employee. Transaction Rollbacked: {e}')
        conn.rollback()
        raise e
    else:
        conn.commit()

def list_all_employees(conn):
    '''
    Returns all employees in the database
    '''
    try:
        with conn.cursor() as cur:
            cur.execute(QUERY_ALL_EMPLOYEE_STMT)
            rows = cur.fetchall()
            return rows
    except Exception as e:
        print(f'Oops, something went wrong adding a new employee: {e}')
        raise e

def validate_input(event):
    '''
    Validates the input event
    '''
    if EMP_ID not in event or EMP_NAME not in event:
        raise Exception(f'Invalid input! Missing "{EMP_ID}" and/or "{EMP_NAME}" attributes.')
    return event[EMP_ID], event[EMP_NAME]

def lambda_handler(event, context):
    '''
    Lambda execution entry point
    '''
    emp_id, emp_name = validate_input(event)
    add_new_employee(conn)
    return list_all_employees(conn)

if __name__ == '__main__':
    '''
    Run the Lambda code locally as a Python script
    '''
    emp_id = str(random.randint(1,100000))
    event = {
        'EmpId': emp_id,
        'EmpName': f'Employee-Name-{emp_id}'
    }
    context = {}
    lambda_handler(event, context)