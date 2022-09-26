import boto3

#Creating Session With Boto3.
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>', region_name= 'us-east-1')

## create session with redshift
client = session.client('redshift')

response = client.delete_cluster(
    ClusterIdentifier=<cluster-name>,
    SkipFinalClusterSnapshot=True
)

print(response)
