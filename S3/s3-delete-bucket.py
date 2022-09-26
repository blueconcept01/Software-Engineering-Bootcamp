import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')

s3 = session.resource('s3')

## connect with the bucket
bucket = s3.Bucket('<bucket-name>')

## empty the bucket
bucket.objects.all().delete()

## delete the bucket
response = bucket.delete()

print(response)
