import boto3
import schedule
import time
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-central-1")

snapshots = ec2_client.describe_snapshots(OwnerIds=["self"])["Snapshots"]
snapshots_sorted = sorted(snapshots, key=itemgetter("StartTime"), reverse=True)


# delete a snapshot
def delete_snapshot():
    for snapshot in snapshots_sorted[2:]:
        ec2_client.delete_snapshot(
            SnapshotId=snapshot["SnapshotId"]
        )


# Schedule snapshot deletion
schedule.every().day.at("01:00").do(delete_snapshot)

while True:
    schedule.run_pending()
    time.sleep(1)
