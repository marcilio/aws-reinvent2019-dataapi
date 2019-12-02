
#================================================================================
# AWS re:Invent 2019 - Dec 2-6, 2019 - Las Vegas
# Session: SVS33 - Build serverless APIs supported by Amazon Aurora Serverless & the Data API
# Marcilio Mendonca, Sr.Solutions Developer, AWS
#
# Description:
#   This is the refactored Lambda code skeleton that:
#     1) Interacts with an Amazon Aurora Serverless MySQL database
#     2) Uses the Aurora Serverless Data API instead of a persistent connection
#        to issue SQL statements against the database
#
# Your Task: fill out the TODO spaces below
#================================================================================

import json
import random
import boto3

# Data API client
rds_client = boto3.client('rds-data')

# Database settings (RDS MySQL)
db_cluster_arn = 'arn:aws:rds:us-east-1:665243897136:cluster:reinvent2019-aurora-serverless-cluster'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:665243897136:secret:reinvent2019-aurora-serverless-secrets-KEFCko'
db_name = 'EmployeeDB'
db_employee_table = 'Employee'

# Constants
EMP_ID = 'EmpId'
EMP_NAME = 'EmpName'
INSERT_EMPLOYEE_STMT  = f'INSERT INTO {db_employee_table} ({EMP_ID}, {EMP_NAME}) VALUES (:{EMP_ID}, :{EMP_NAME})'
QUERY_ALL_EMPLOYEE_STMT  = f'SELECT {EMP_ID}, {EMP_NAME} FROM {db_employee_table}'

def execute_statement(rds_client, sql, sql_parameters=[], transaction_id=None):
    '''
    Invokes the Data API to execute a SQL statement (e.g., select, insert, create table)
    '''
    # TODO: invoke the rds_client.execute_statement() using the parameters above
    # Note that transaction_id is optional

    # TODO: return the output of rds_client.execute_statement()
    return response

def add_new_employee(rds_client, emp_id, emp_name):

    '''
    Adds a new employee to the database
    '''
    # TODO: begin transaction
    try:
        print(f'Inserting employee {emp_id}')
        # TODO: Invoke function execute_statement() defined above
        # Don't forget to pass the transaction_id!
        sql_parameters = []
    except Exception as e:
        # TODO: rollback transaction
        print(f'Oops, something went wrong adding a new employee. Transaction Rollbacked: {e}')
        raise e
    else:
        # TODO: commit transaction
        pass

def list_all_employees(rds_client):
    '''
    Returns all employees in the database
    '''
    # Formatting query returned Field
    def format_field(field):
        return list(field.values())[0]
    # Formatting query returned Record
    def format_record(record):
        return [format_field(field) for field in record]
    # Formatting query returned Field
    def format_records(records):
        return [format_record(record) for record in records]

    try:
        response = execute_statement(rds_client, QUERY_ALL_EMPLOYEE_STMT)
        return format_records(response['records'])
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
    add_new_employee(rds_client, emp_id, emp_name)
    return list_all_employees(rds_client)

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
    employees = lambda_handler(event, context)
    print(f'Number of employees: {len(employees)}')
    print(f'List of employees: {employees}')