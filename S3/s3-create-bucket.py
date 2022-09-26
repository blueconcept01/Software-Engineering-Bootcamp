## Script to create a bucket in AWS S3 using boto3

import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')


#Creating S3 Resource From the Session.
s3 = session.resource('s3')

## create simple bucket with the bucket name and the region you want to launch in -
s3.create_bucket(Bucket='<bucketname>', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'})


## create bucket with configurations and other details
#bucket = s3.create_bucket(
#    ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
#    Bucket='string',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'af-south-1'|'ap-east-1'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ca-central-1'|'cn-north-1'|'cn-northwest-1'|'EU'|'eu-central-1'|'eu-north-1'|'eu-south-1'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'me-south-1'|'sa-east-1'|'us-east-2'|'us-gov-east-1'|'us-gov-west-1'|'us-west-1'|'us-west-2'
#    },
#    GrantFullControl='string',
#    GrantRead='string',
#    GrantReadACP='string',
#    GrantWrite='string',
#    GrantWriteACP='string',
#    ObjectLockEnabledForBucket=True|False,
#    ObjectOwnership='BucketOwnerPreferred'|'ObjectWriter'|'BucketOwnerEnforced'
#)

