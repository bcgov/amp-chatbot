"""
    helloworld.main

    Main program for the helloworld Python project
"""
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)