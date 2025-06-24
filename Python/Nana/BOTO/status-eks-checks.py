import boto3

eks_client = boto3.client('eks', region_name="eu-central-1")

clusters = eks_client.list_clusters()["clusters"]

for cluster in clusters:
    describe_cluster = eks_client.describe_cluster(name=cluster)["cluster"]
    print(f"Cluster {cluster} status: {describe_cluster["status"]} | Version: {describe_cluster["version"]}")
    print(f"Endpoint: {describe_cluster["endpoint"]}")
