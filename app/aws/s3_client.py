import boto3
import json

def upload_to_s3(bucket_name: str, key: str, data: dict):
    s3 = boto3.client("s3")
    body = json.dumps(data, indent=2)
    response = s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=body.encode("utf-8"),
        ContentType="application/json"
    )
    return response
