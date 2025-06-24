import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

# Define instance id where to restore the volume
instance_id = "i-053b7edcc766fa0d5"

# Get volumes from the instance ID
instance_volume = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        },
    ],
)["Volumes"][0]

# Get snapshots from the volume
snapshots = ec2_client.describe_snapshots(
    OwnerIds=["self"],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume["VolumeId"]]
        }
    ]
    )["Snapshots"]
latest_snapshot = sorted(snapshots, key=itemgetter("StartTime"), reverse=True)[0]

# Create a volume from a snapshot
new_volume = ec2_client.create_volume(
    AvailabilityZone='eu-central-1a',
    SnapshotId=latest_snapshot["SnapshotId"]
)

# Attach new volume to the instance when it becomes available
while True:
    new_volume_state = ec2_resource.Volume(new_volume["VolumeId"])
    if new_volume_state.state == 'available':
        ec2_resource.Instance(instance_id).attach_volume(
            Device='/dev/xvdb',
            VolumeId=new_volume["VolumeId"]
        )
        print("Volume restored")
        break
