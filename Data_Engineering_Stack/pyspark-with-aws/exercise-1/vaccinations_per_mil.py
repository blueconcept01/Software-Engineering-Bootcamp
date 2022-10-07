#!/usr/bin/env python
# coding: utf-8

# vaccinations_per_mil.py
#
# Processes the owid-covid-data.csv file using PySpark SQL and produces a
# new CSV file listing the top 10 locations with the highest sums of
# vaccinations per million of the population. The script simply sums the
# number of reported new vaccinations (smoothed) for each date by location.
#
# The script requires two command line arguments passed to it. Each should 
# map to their appropriate folder in the S3 bucket that was created while
# following the tutorial.
#
# Arguments:
#   <input URI>  - The URI path to the input file (owid-covid-data.csv).
#                  e.g.: s3://<bucket-name>/input/owid-covid-data.csv
#   <output URI> - The URI path to the output folder.
#                  e.g.: s3://<bucket-name>/output
#

from pyspark.sql import SparkSession
import sys

def process_data(inp_uri, outp_uri):
    with SparkSession.builder\
                     .appName('Vaccinations Per Million By Location')\
                     .getOrCreate() as spark:
                     
        covid19_df = spark.read.option('header', 'true').csv(inp_uri)
                               
        covid19_df.createOrReplaceTempView('covid19_data')
        
        vacc_query_result = spark.sql(
            """SELECT   location,
                        SUM(new_vaccinations_smoothed_per_million) 
                        AS vaccinations_per_mil
               FROM     covid19_data
               WHERE    new_vaccinations_smoothed_per_million <> ''
               GROUP BY location
               ORDER BY vaccinations_per_mil DESC LIMIT 10
            """)
        
        vacc_query_result.write.option('header', 'true')\
                               .mode('overwrite')\
                               .csv(outp_uri)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        input_uri  = sys.argv[1]
        output_uri = sys.argv[2]
        process_data(input_uri, output_uri)
    else:
        sys.exit(f"USAGE: {sys.argv[0]} <input> <output>\n\n"
                  "  Positional Arguments:\n"
                  "    input  - The URI of the input CSV file.\n"
                  "    output - The URI of the output folder.\n")