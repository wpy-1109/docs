# Python SDK - Bucket Operations

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python-manage-buckets

## V1 SDK (oss2)

### Create a Bucket

```python
import oss2

auth = oss2.Auth('<access-key-id>', '<access-key-secret>')
service = oss2.Service(auth, 'https://oss-cn-hangzhou.aliyuncs.com')

# Simple creation
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'my-bucket')
bucket.create_bucket()

# With storage class and ACL
bucket.create_bucket(
    oss2.BUCKET_ACL_PRIVATE,
    oss2.models.BucketCreateConfig(oss2.BUCKET_STORAGE_CLASS_STANDARD))
```

### List Buckets

```python
service = oss2.Service(auth, 'https://oss-cn-hangzhou.aliyuncs.com')
for bucket_info in oss2.BucketIterator(service):
    print(f"Bucket: {bucket_info.name}, Location: {bucket_info.location}")
```

### Check if Bucket Exists

```python
try:
    bucket.get_bucket_info()
    print("Bucket exists")
except oss2.exceptions.NoSuchBucket:
    print("Bucket does not exist")
```

### Get Bucket Info

```python
info = bucket.get_bucket_info()
print(f"Name: {info.name}")
print(f"Location: {info.location}")
print(f"Storage Class: {info.storage_class}")
print(f"Creation Date: {info.creation_date}")
```

### Set Bucket ACL

```python
bucket.put_bucket_acl(oss2.BUCKET_ACL_PRIVATE)
# Options: BUCKET_ACL_PRIVATE, BUCKET_ACL_PUBLIC_READ, BUCKET_ACL_PUBLIC_READ_WRITE
```

### Get Bucket ACL

```python
acl = bucket.get_bucket_acl()
print(f"ACL: {acl.acl}")
```

### Delete a Bucket

```python
bucket.delete_bucket()
```

## V2 SDK

### Create a Bucket

```python
result = client.put_bucket(oss.PutBucketRequest(
    bucket='my-bucket',
))
print(f"Bucket created: {result.status_code}")
```

### List Buckets

```python
result = client.list_buckets(oss.ListBucketsRequest())
for b in result.buckets:
    print(f"Bucket: {b.name}, Location: {b.location}")
```

### Delete a Bucket

```python
result = client.delete_bucket(oss.DeleteBucketRequest(
    bucket='my-bucket',
))
```
