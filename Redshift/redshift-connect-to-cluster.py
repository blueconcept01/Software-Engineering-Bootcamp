## Script to connect to redshift database; and perform operations

import psycopg2
import boto3

## function to setup connectivity
def db_connection():

    RS_PORT = <redshift-pot>

    RS_USER = <user-name>

    DATABASE = <database>

    CLUSTER_ID = <cluster-name>

    RS_HOST = <endpoint-url>  ## can easily extract from the console; endpoint

    REGION_NAME = <region of cluster>

    client = boto3.client('redshift',region_name=REGION_NAME, aws_access_key_id='<access-key>', aws_secret_access_key='<scret-key>')

    cluster_creds = client.get_cluster_credentials(DbUser=RS_USER,
                                                DbName=DATABASE,
                                                ClusterIdentifier=CLUSTER_ID,
                                                AutoCreate=False)

    conn = psycopg2.connect(
                host=RS_HOST,
                port=RS_PORT,
                user=cluster_creds['DbUser'],
                password=cluster_creds['DbPassword'],
                database=DATABASE)

    return conn

## function to execute sql

def executescript(redshift_cursor):
    query = "SHOW TABLES;"
    cur=redshift_cursor
    cur.execute(query)

## setup connection and call to the database
conn = db_connection()
print(conn)
conn.set_session(autocommit=False)
cursor = conn.cursor()
executescript(cursor)
conn.close()    
