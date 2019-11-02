# snapshotalyzer
Project based on Cloud Guru course - listing EC2 instances on AWS, taking snaps etc.

# About

This project is Robby Kukurs practicing using python for AWS.
Here we are using boto3 pyton module within pipenv to manage EC2 instances etc

#Configuring

snapshotalyzer is using AWS configuration file to connect to AWS.

'aws configure --profile snapshot'

#Running

To list ec2 instances, run below
'pipenv run "python /snapshotalyzer/ec2/list_ec2.py'
