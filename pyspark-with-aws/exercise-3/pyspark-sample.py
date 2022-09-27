#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType
from pyspark import SQLContext
from itertools import islice
from pyspark.sql.functions import col

import sys

if __name__ == '__main__':

    # creating the context
    sqlContext = SQLContext(sc)

    # reading the first csv file and store it in an RDD
    rdd1 = sc.textFile('s3://testtt-ashhh/test1.csv'
                       ).map(lambda line: line.split(','))

    # removing the first row as it contains the header
    rdd1 = rdd1.mapPartitionsWithIndex(lambda idx, it: (islice(it, 1,
            None) if idx == 0 else it))

    # converting the RDD into a dataframe
    df1 = rdd1.toDF(['Name','age','Experience','Salary'])

    # dataframe which holds rows after replacing the 0's into null
    targetDf = df1.withColumn('eq_site_limit', when(df1['eq_site_limit'
                              ] == 0, 'null'
                              ).otherwise(df1['eq_site_limit']))

    df1WithoutNullVal = targetDf.filter(targetDf.eq_site_limit != 'null')

    rdd2 = sc.textFile('s3://testtt-ashhh/test2.csv'
                       ).map(lambda line: line.split(','))
    rdd2 = rdd2.mapPartitionsWithIndex(lambda idx, it: (islice(it, 1,
            None) if idx == 0 else it))
    df2 = df2.toDF(['Name','age','Experience','Salary'])

    innerjoineddf = df1WithoutNullVal.alias('a').join(df2.alias('b'),
            col('b.Name') == col('a.Name')).select([col('a.'
            + xx) for xx in a.columns] + [col('b.age'), col('b.Experience'
            ), col('b.Salary')])

    innerjoineddf.write.parquet('s3://testtt-ashhh/test.parquet')