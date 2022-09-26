import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')

s3 = session.resource('s3')

my_bucket = s3.Bucket('<bucket-name>')

## delete the file
response = my_bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': "filename.txt"   # the_name of_your_file
            }
        ]
    }
)
