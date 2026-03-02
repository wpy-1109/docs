# Python SDK - Quick Start

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python-quick-start

## V1 SDK Quick Start

```python
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Initialize
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', '<your-bucket-name>')

# Upload an object
bucket.put_object('example.txt', 'Hello OSS!')

# Download an object
result = bucket.get_object('example.txt')
print(result.read().decode())

# List objects
for obj in oss2.ObjectIterator(bucket):
    print(obj.key)

# Delete an object
bucket.delete_object('example.txt')
```

## V2 SDK Quick Start

```python
import alibabacloud_oss_v2 as oss

def main():
    region = "cn-hangzhou"
    bucket_name = "your-bucket-name"
    object_name = "your-object-name"

    # Initialize
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = region

    client = oss.Client(cfg)

    # Upload a string
    result = client.put_object(oss.PutObjectRequest(
        bucket=bucket_name,
        key=object_name,
        body=b'Hello OSS V2!',
    ))
    print(f'Upload successful, ETag: {result.etag}')

    # Upload a local file
    with open('/path/to/local/file.txt', 'rb') as f:
        result = client.put_object(oss.PutObjectRequest(
            bucket=bucket_name,
            key=object_name,
            body=f,
        ))
    print(f'File uploaded, ETag: {result.etag}')

if __name__ == "__main__":
    main()
```
