import os
import json
import boto3
from botocore.exceptions import ClientError

current_dir = os.path.dirname(os.path.realpath(__file__))

def CreateBucketFile(account, bucket, policy):
    bucket_path = os.path.join(current_dir + '/bucket-policies-' + account + '/' +  bucket + '.json')
    if not os.path.exists(bucket_path):
        with open(bucket_path, 'w') as jsonFile:
            if policy:
                json.dump(policy, jsonFile, indent=4, ensure_ascii=False,
                sort_keys=False, separators=(',', ':'))

def GetPolicy(bucket):
    try: 
        response_policy = s3_client.get_bucket_policy(Bucket=bucket)
        policy = response_policy['Policy']
        dict_bucket=eval(policy)
        return dict_bucket
    except ClientError as e: 
        if e.response['Error']['Code'] == 'AccessDenied':
            print(bucket, '- error to access bucket - access denied')
            return False
        else:
            print(bucket, '- error to access bucket ')
            return False
    except Exception as e:
        print(e)
        return False

def CreateAccountDir(account):
    account_bucket_path = os.path.join(current_dir + '/bucket-policies-' + account)
    if not os.path.exists(account_bucket_path):
        os.mkdir(account_bucket_path)

def ScanBuckets():    
    reponse_bucket = s3_client.list_buckets()
    list_bucket_name = [bucket['Name'] for bucket in reponse_bucket['Buckets']]
    return list_bucket_name

if __name__ == '__main__':
    account = 'account-name'
    s3_client = boto3.client('s3')
    CreateAccountDir(account)
    buckets=ScanBuckets()
    for bucket in buckets:
        policy=GetPolicy(bucket)
        if not policy: continue
        CreateBucketFile(account, bucket, policy)