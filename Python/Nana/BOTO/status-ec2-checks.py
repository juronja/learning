import boto3
import schedule
import time

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")


# EC2 Instance status check
def check_instance_status():
    instances = ec2_client.describe_instance_status()["InstanceStatuses"]

    for instance in instances:
        instance_state = instance["InstanceState"]["Name"]
        instance_status = instance["InstanceStatus"]["Status"]
        system_status = instance["SystemStatus"]["Status"]
        print(f"Instance State, Status and system status of {instance["InstanceId"]} are: {instance_state}, {instance_status}, {system_status}")


# Schedule status checks
schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()
    time.sleep(1)
