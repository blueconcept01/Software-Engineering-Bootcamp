import boto3

#Creating Session With Boto3.
## add credentials to this line
session = boto3.Session(aws_access_key_id='<access-key>', aws_secret_access_key='<secret-key>')


#Creating S3 Resource From the Session.
s3 = session.resource('s3')

## put file to s3; filename.txt
result = s3.meta.client.put_object(Body='Text Contents', Bucket='<bucket-name>', Key='filename.txt')  ##key is the file-name
res = result.get('ResponseMetadata')

## check if the upload is successfull
if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')
