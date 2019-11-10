import boto3
import click

session = boto3.Session(profile_name='snapshot')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []
    if project:
        filters = [{'Name': 'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances

def filter_volumes(project):
    volumes = []
    if project:
        filters = [{'Name': 'tag:Project', 'Values':[project]}]
        volumes = ec2.volumes.filter(Filters=filters)
    else:
        volumes = ec2.volumes.all()
    return volumes

@click.group()
def cli():
    """snapshotalyzer manages snapshots"""

@cli.group('volumes')
def volumes():
    """Commands for volumes"""

@volumes.command('list')
@click.option('--project', default=None, help="Only volumes for project (tag Project:<name>)")

def list_volumes(project):
    "List EC2 volumes"
    instances = filter_instances(project)
    for i in instances:
        for v in i.volumes.all():
            print(', '.join((
            i.id,
            v.id,
            str(v.size) + " GiB",
            v.encrypted and "Encrypted" or "Not encrypted"
            )))
    return


@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""

@snapshots.command('list')
@click.option('--project', default=None, help="Only snapshots for project (tag Project:<name>)")

def list_snapshots(project):
    "List EC2 volume snapshots"
    volumes = filter_volumes(project)
    for v in volumes:
        for s in v.snapshots.all():
            print(', '.join((
            v.id,
            s.id,
            s.state,
            s.progress,
            s.start_time.strftime("%c")
            )))
    return

@snapshots.command('create')
@click.option('--project', default=None, help="Only snapshots for project (tag Project:<name>)")

def create_snapshots(project):
    "Create EC2 volume snapshots"
    instances = filter_instances(project)
    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
        i.wait_until_stopped()
        for v in i.volumes.all():
            print("Creating snapshot for instance {0} volume {1}...".format(i.id, v.id))
            v.create_snapshot(Description="Created by snapshotalyzer script")
        i.start()
        print("Starting the instance {0}...".format(i.id))

    print("Job's done, instances restarted, snaps created!!!")

    return

@cli.group('instances')
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")

def list_instances(project):
    "List EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or []}
        print(', '.join((
            i.id,
            i.instance_type,
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
            )))
    return

@instances.command('stop')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")

def stop_instances(project):
    "Stop EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("Stopping {0} ...".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project', default=None, help="Only instances for project (tag Project:<name>)")

def start_instances(project):
    "Start EC2 instances"
    instances = filter_instances(project)
    for i in instances:
        print("Starting {0} ...".format(i.id))
        i.start()
    return

if __name__ == '__main__':
    cli()
