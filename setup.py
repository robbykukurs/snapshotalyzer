from setuptools import setup

setup(
    name='AWS EC2 management script',
    version='1',
    author='Robby Kukurs',
    author_email="robbykukurs@gmail.com",
    description="Python script to manage AWS EC2 instances, volumes and snapshots - allows to start and stop instances, list them, list volumes as well as create and list snapshots",
    license="GPLv3+",
    packages=['ec2'],
    url="robbykukurs.com",
    install_requires=['click','boto3'],
    entry_points='''
        [console_scripts]
        awsmanage=ec2.list_ec2:cli
    ''',
)
