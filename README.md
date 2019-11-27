### AWS re:Invent 2019 (Dec 2-6, 2019 - Las Vegas, USA)
#### SVS-333- Build serverless APIs supported by Amazon Aurora Serverless & the Data API
##### [Marcilio Mendonca](https://www.linkedin.com/in/marcilio/), Sr.Solutions Developer, AWS

---

#### Welcome to the exciting world of Serverless databases and database SQL APIs!

This project is part of [session SVS-333](https://www.portal.reinvent.awsevents.com/connect/sessionDetail.ww?SESSION_ID=98051&tclass=popup&csrftkn=EP5T-MDKK-9YSA-VZ2O-Y181-V0LU-K0RP-JEL6) (_Build serverless APIs supported by Amazon Aurora Serverless & the Data API_) of the [AWS re:Invent 2019](https://reinvent.awsevents.com/schedule/) conference!

In this session, you will refactor an existig Lambda function to use the new [Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) for Amazon Aurora Serverless. The Data API allows you to use an API, instead of a persistent connection, to issue SQL commands against an Amazon Aurora Serverless database (MySQL and PostgreSQL). This is how modern Serverless applications interact with modern Serverless databases! Welcome to the future!

## Provided Source Files

* `README.md`: This file :)

* `lambda_rds.py`: The Lambda code that interacts with RDS MySQL that is being refactored.

* `lambda_dataapi.py`: A skeleton of the refactored Lambda code that will interact with an Amazon Aurora Serverless MySQL database using the Data API. If you wish you can use this file to simplify your work (more details in the next section).

* `requirements.txt`: The Python dependencies for `lambda_rds.py`.

## Your Task

Your task is to refactor the `lamba_rds.py` code to remove the persistent database connection object and the dependency on Python package `pymysql` and use the Data API instead to interact with the MySQL database. The behavior of the Lambda function will remaind the same for external clients. Both databases, i.e., the Amazon RDS MySQL database used by the original Lambda code and the Amazon Aurora Serverlesss MySQL used by the refactored Lambda, will be provided for you.

Your options to complete this task are as follows:

**Option 1** (__hardest but more learning__): you'll copy and paste file `lambda_rds.py` into file `lambda_dataapi.py` and do the refactoring from the scratch.

**Option 2** (__easiest but less time consuming__): you'll use provided refactored skeleton file `lambda_dataapi.py` as basis for your refactoring and complete the `TODO` parts in the code.

## I'm not a Python developer!

No worries. In this case, you'll have a bit of extra work but a lot of learning too! You'll need to manually convert the skeleton Lambda `lambda_dataapi.py` to your programming language of choice and then complete the exercise.

Feel free to share your solution! The more solutions using a different programming language the better!

## How do you know you're done?

If your `lambda_dataapi.py` refactored Lambda behaves exactly like the `lambda_rds.py` Lambda (but using Amazon Aurora Serverless MySQL and the Data API), then you're done :)

I'm sure there will be different awesome solutions to this task so please feel free to share your solution and let me know (my contact is at the very bottom)!

## Before you begin

You'll need to set up your workstation to be able to work on this session.

Here are the requirements:

1. [The AWS CLI](https://aws.amazon.com/cli/) installed
2. [Python 3.6+](https://www.python.org/downloads/) installed
3. [The Boto3](https://aws.amazon.com/sdk-for-python/) AWS Python SDK (`pip install boto3`)
4. Python [Virtual environment](https://virtualenv.pypa.io/en/stable/installation/) installed
5. Install a Git client and clone (`git clone`) this repo: [https://github.com/marcilio/aws-reinvent2019-dataapi](https://github.com/marcilio/aws-reinvent2019-dataapi)
6. Set up your local AWS credentials by creating environment variables in your bash/DOS shell as shown below. The actual values for `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` will be shared w/ you during the event.

MacOS:

```bash
export AWS_ACCESS_KEY_ID=[to-be-provided]
export AWS_SECRET_ACCESS_KEY=[to-be-provided]
export AWS_DEFAULT_REGION=us-east-1
```

Windows Command Prompt:

```bash
C:\> setx AWS_ACCESS_KEY_ID [to-be-provided]
C:\> setx AWS_SECRET_ACCESS_KEY [to-be-provided]
C:\> setx AWS_DEFAULT_REGION us-east-1
```

## Running locally

To save you time, you won't need to deploy and run the Lambda function in the AWS cloud. Instead you'll run the Lambda code locally as a Python script. For instance, to run the original
Lambda function locally you'll just type: `python lambda_rds.py`. If yours AWS credentials are configured correctly you'll see a list of employees (id, name) as output.

To run the Amazon RDS Lambda function type `python lambda_rds.py`.
To run the Lambda function you're refactoring simply type `python lambda_dataapi.py`.

File `requirements.txt` contains the dependencies for `lambda_rds.py`. You can create a virtual environment called `reinvent2019-data-api` and install the required packages using `pip` like this:

```
pip install virtualenv
virtualenv reinvent2019-data-api
pip install -r requirements.txt
```

## Running on AWS

Deploy your Lambda function to AWS (e.g., via SAM or Cloudformation or using the AWS console), create an IAM role for the function, and run the Lambda function! We'll discuss this procedure in more details during the re:Invent session.

## Resources

Here are some useful resources that might help you complete this session:

* [Amazon Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html) and [the Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) documentation
* [Boto3 Python SDK doc on the Amazon Aurora Serverless Data API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html) documentation
* [Amazon Aurora Serverless Data API blog](https://aws.amazon.com/blogs/database/using-the-data-api-to-interact-with-an-amazon-aurora-serverless-mysql-database/)
* [GitHub repo](https://github.com/aws-samples/aws-aurora-serverless-data-api-sam/blob/master/examples/dataapi_examples.py) with various sample code using the Aurora Serverless Data API

## Stretch your knowledge

Here's a suggestion to stretch your knowledge: modify your refactored Lambda to add batches of 50 employees at a time in the Amazon Aurora Serverless database using the [Data API batching](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html#RDSDataService.Client.batch_execute_statement) capabilities. Continue to use transactions to rollback or commit an entire batch. Check the `Resources` section above and the examples provided in the GitHub repo.

## Solution

We'll post the solution(s) to this session under folder `/solutions` in this GitHub repo after the event.

Please contact Marcilio (marcilio@amazon.com) if you also want to share your solution with others!

## Contact

Contact AWS guru and Data API lover ___Marcilio Mendonca___ (marcilio@amazon.com) if you have any questions regarding this session.

If you like this project please hit the like button, share with your friends, and spread the love for the Amazon Aurora Serverless and the Data API :)

Have fun!
