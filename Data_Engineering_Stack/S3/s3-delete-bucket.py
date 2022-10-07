import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')

## get the connection the S3 resource
s3 = session.resource('s3')

## connect with the bucket; this will setup the connectivity to the particular bucket; after you can perform the operations
bucket = s3.Bucket('<bucket-name>')

## you cannot delete a bucket if there are any objects exists.
## empty the bucket
bucket.objects.all().delete()

## delete the bucket
response = bucket.delete()

print(response)
