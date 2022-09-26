import boto3

#Creating Session With Boto3.
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>', region_name= 'us-east-1')

## create session with redshift
client = session.client('redshift')

## get the details
cluster_list = client.describe_clusters()

## get the name of the clusters
for cluster in cluster_list['Clusters']:
    print(cluster['ClusterIdentifier'])

