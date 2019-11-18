
__Welcome to the exciting world of Serverless databases and database SQL APIs!__

Your task will be to refactor a provided Lambda function (Python 3.6) that interacts
with an existing Amazon RDS MySQL database using a persistent connection (traditional way)
so that the refactored code now interacts with an existing Amazon Aurora Serverless MySQL
database using the new Data API for Amazon Aurora Serverless (modern apps)!

## Provided Source Files

* `README.md`: This file :)

* `lambda_rds.py`: The Lambda code that interacts with RDS MySQL that is being refactored.

* `lambda_dataapi.py`: A skeleton of the refactored Lambda code that will interact with an
Amazon Aurora Serverless MySQL database using the Data API. You'll have to edit this file!

* `requirements.txt`: The Python dependencies for `lambda_rds.py`.

## Your Task

Your task is to modify file `lambda_dataapi.py`, which is a provided code skeleton for the refactored Lambda, so that the refactored Lambda behaves exactly as the original Lambda `lambda_rds.py` but...

1) ... using the provided Amazon Aurora Serverless MySQL database, and

2) ... leveraging the Aurora Serverless Data API instead of using a persistent connection

In other words, __you're removing the database connection from the code and using an API to issue SQL commands instead__. Cool, eh?

## I'm not a Python developer!

No worries. In this case, you'll have a bit of extra work but a lot of learning too! You'll need to translate the skeleton Lambda `lambda_dataapi.py` into your programming language of choice and then complete the exercise.

Feel free to share your solution! The more solutions using a different programming language the better!

## How do you know you're done?

If your `lambda_dataapi.py` refactored Lambda behaves exactly like the `lambda_rds.py` Lambda (but using Amazon Aurora Serverless MySQL and the Data API), then you're done :)

I'm sure there will be different awesome solutions to this task so please feel free to share your solution and let me know (my contact is at the very bottom)!

## Before you begin

You'll need:

1) Proper AWS credentials set up in your local workstation
2) [The AWS CLI](https://aws.amazon.com/cli/) installed
3) [Python 3.6+](https://www.python.org/downloads/) installed
4) [The Boto3](https://aws.amazon.com/sdk-for-python/) AWS Python SDK (`pip install boto3`)
5) [Virtual environment](https://virtualenv.pypa.io/en/stable/installation/) installed

## Running locally

You won't need to run the Lambda function in the AWS cloud. Instead, for simplicify, we're
going to run the Lambda code locally as a Python script. For instance to run the original
Lambda function locally just type: `python lambda_rds.py`. If yours AWS credentials are
configured correctly you'll see a list of employees (id, name) as output.

To run the Lambda function you're refactoring simply type `python lambda_dataapi.py`.

The Lambda code requires the packages in `requirements.txt` to be installed. Create a virtual environment and install the dependencies like this:

```
pip install virtualenv
virtualenv reinvent2019-data-api
pip install -r requirements.txt
```

Got it?

## Resources

Some useful resources that might help you on this task include:

* Amazon Aurora Serverless Data API documentation
* Boto3 Amazon Aurora Serverless Data API documentation
* Blog on the Amazon Aurora Serverless Data API
* GitHub repo with various sample code using the Aurora Serverless Data API

## Stretch your knowledge

Here's a suggestion to stretch your knowledge: modify your refactored Lambda to
support inserting a batch of 50 employees at a time. Continue to use transactions
to rollback or commit an entire batch. Use the Data API support for batches. Check
the `Resources` section above and the examples provided in the GitHub repo.

## Contact

Contact AWS guru and Data API lover ___Marcilio Mendonca___ (marcilio@amazon.com) if you have any questions regarding this task.

If you like this project please hit the like button, share with your friends, and spread the love for the Amazon Aurora Serverless Data API :)

Good Luck!
