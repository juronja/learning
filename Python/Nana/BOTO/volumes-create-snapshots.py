import boto3
import schedule
import time
import botocore.exceptions  # Import for specific exception handling

ec2_client = boto3.client('ec2', region_name="eu-central-1")

volumes = ec2_client.describe_volumes()["Volumes"]


# Create a snapshot
def create_snapshot():
    for volume in volumes:
        try:
            ec2_client.create_snapshot(
                VolumeId=volume["VolumeId"]
            )
        except botocore.exceptions.ClientError as e:
            print(f"Error describing volumes: {e}")
            return


# Schedule snapshot creations
schedule.every().day.at("00:00").do(create_snapshot)

while True:
    schedule.run_pending()
    time.sleep(1)
