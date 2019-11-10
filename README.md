# snapshotalyzer
Project based on Cloud Guru course - listing EC2 instances on AWS, taking snaps etc.

# About

This project is Robby Kukurs practicing using python for AWS.
Here we are using boto3 pyton module within pipenv to manage EC2 instances etc

#Configuring

snapshotalyzer is using AWS configuration file to connect to AWS; you have to create a special AWS user, in our case we use "snapshot" 
'aws configure --profile snapshot'

#Installing the list_ec2.py package as a standalone python package

Use your python installation package such as pip3: 
'pip3 install dist/AWS_EC2_management_script-1-py3-none-any.whl'

#Running

To run the script, do:
'pipenv run python ec2/list_ec2.py'

Append below commands to work with EC2 instances, volumes and snapshots:
'pipenv run python ec2/list_ec2.py instances'
'pipenv run python ec2/list_ec2.py volumes'
'pipenv run python ec2/list_ec2.py snapshots'

Append '--help' to see subcommands for each main command
Append '--project <INSTANCE_PROJECT_TAG_NAME>' to work with only specific instances/volumes/snapshots

Alternatively, if you've installed the package with pip3 install, for example, you can substitute 'pipenv run python ec2/list_ec2.py' with awsmanage:

'awsmanage instances list' for example, and so on
