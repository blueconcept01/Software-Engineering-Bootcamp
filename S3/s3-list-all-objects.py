import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')

## list all objects from bucket
s3 = session.resource('s3')

## access the particular bucket
my_bucket = s3.Bucket('<bucket-name>')

## list all the objects from the bucket
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
