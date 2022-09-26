import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')

s3 = session.resource('s3')

## print all buckets in the aws account
buckets = [bucket.name for bucket in s3.buckets.all()]
print(buckets)
