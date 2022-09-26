import boto3

#Creating Session With Boto3.
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>', region_name= 'us-east-1')

## create session with redshift
obj = session.client('redshift')
obj.create_cluster(
    ClusterIdentifier=<cluster-name>,
    NodeType='dc2.large',
    MasterUsername='root',
    MasterUserPassword='passP123',
    DBName='dev',
    ClusterType='single-node',
    Port=5439,
    Encrypted=False)



