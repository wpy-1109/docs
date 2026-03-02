# Python SDK - Presigned URLs, Lifecycle, Versioning, Access Control, Encryption

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python

## Presigned URLs

### V1 SDK

```python
# Generate signed GET URL (download)
url = bucket.sign_url('GET', 'example.txt', 3600)  # 1 hour expiration
print(f"Download URL: {url}")

# Generate signed PUT URL (upload)
url = bucket.sign_url('PUT', 'example.txt', 3600)
print(f"Upload URL: {url}")

# With custom headers
headers = {'Content-Type': 'application/octet-stream'}
url = bucket.sign_url('PUT', 'example.txt', 3600, headers=headers)
```

### V2 SDK

```python
import datetime
import alibabacloud_oss_v2 as oss

# Generate presigned download URL
pre_result = client.presign(oss.GetObjectRequest(
    bucket="example_bucket",
    key="exampleobject.txt",
), expires=datetime.timedelta(minutes=10))

print(f'URL: {pre_result.url}')

# Generate presigned upload URL
pre_result = client.presign(oss.PutObjectRequest(
    bucket="example_bucket",
    key="exampleobject.txt",
), expires=datetime.timedelta(hours=1))

print(f'URL: {pre_result.url}')
```

## Lifecycle Rules

### Set Lifecycle Rules

```python
from oss2.models import LifecycleRule, LifecycleExpiration, StorageTransition

# Rule: Expire objects after 30 days
rule1 = LifecycleRule('rule1', 'logs/',
    status=LifecycleRule.ENABLED,
    expiration=LifecycleExpiration(days=30))

# Rule: Transition to IA storage after 60 days
rule2 = LifecycleRule('rule2', 'archive/',
    status=LifecycleRule.ENABLED,
    storage_transitions=[
        StorageTransition(days=60, storage_class=oss2.BUCKET_STORAGE_CLASS_IA)
    ])

lifecycle = oss2.models.BucketLifecycle([rule1, rule2])
bucket.put_bucket_lifecycle(lifecycle)
```

### Get Lifecycle Rules

```python
lifecycle = bucket.get_bucket_lifecycle()
for rule in lifecycle.rules:
    print(f"Rule ID: {rule.id}, Prefix: {rule.prefix}, Status: {rule.status}")
```

### Delete Lifecycle Rules

```python
bucket.delete_bucket_lifecycle()
```

## Versioning

### Enable Versioning

```python
from oss2.models import BucketVersioningConfig

config = BucketVersioningConfig(oss2.BUCKET_VERSIONING_ENABLE)
bucket.put_bucket_versioning(config)
```

### Suspend Versioning

```python
config = BucketVersioningConfig(oss2.BUCKET_VERSIONING_SUSPEND)
bucket.put_bucket_versioning(config)
```

### Get Versioning Status

```python
result = bucket.get_bucket_versioning()
print(f"Versioning status: {result.status}")
```

### Download Specific Version

```python
params = {'versionId': 'your-version-id'}
result = bucket.get_object('example.txt', params=params)
```

### List Object Versions

```python
result = bucket.list_object_versions()
for version in result.versions:
    print(f"Key: {version.key}, VersionId: {version.versionid}, "
          f"IsLatest: {version.is_latest}")
for marker in result.delete_marker:
    print(f"Delete Marker: {marker.key}, VersionId: {marker.versionid}")
```

## Access Control

### Set Bucket ACL

```python
bucket.put_bucket_acl(oss2.BUCKET_ACL_PRIVATE)
# Options: BUCKET_ACL_PRIVATE, BUCKET_ACL_PUBLIC_READ, BUCKET_ACL_PUBLIC_READ_WRITE
```

### Set Object ACL

```python
bucket.put_object_acl('example.txt', oss2.OBJECT_ACL_PUBLIC_READ)
# Options: OBJECT_ACL_DEFAULT, OBJECT_ACL_PRIVATE, OBJECT_ACL_PUBLIC_READ,
#          OBJECT_ACL_PUBLIC_READ_WRITE
```

### Get Object ACL

```python
acl = bucket.get_object_acl('example.txt')
print(f"ACL: {acl.acl}")
```

### CORS Configuration

```python
from oss2.models import CorsRule, BucketCors

rule = CorsRule(
    allowed_origins=['https://example.com'],
    allowed_methods=['GET', 'PUT', 'POST'],
    allowed_headers=['*'],
    max_age_seconds=3600
)
bucket.put_bucket_cors(BucketCors([rule]))
```

## Server-Side Encryption

### Set Default Encryption (SSE-OSS)

```python
from oss2.models import ServerSideEncryptionRule

rule = ServerSideEncryptionRule()
rule.sse_algorithm = oss2.SERVER_SIDE_ENCRYPTION_AES256
bucket.put_bucket_encryption(rule)
```

### Set Default Encryption (SSE-KMS)

```python
rule = ServerSideEncryptionRule()
rule.sse_algorithm = oss2.SERVER_SIDE_ENCRYPTION_KMS
rule.kms_master_keyid = '<your-cmk-id>'
bucket.put_bucket_encryption(rule)
```

### Upload with Per-Object Encryption

```python
headers = {
    'x-oss-server-side-encryption': 'AES256'
}
bucket.put_object('encrypted.txt', 'secret data', headers=headers)
```

### Get Encryption Configuration

```python
result = bucket.get_bucket_encryption()
print(f"Algorithm: {result.sse_algorithm}")
```

## Client-Side Encryption (V2 SDK)

### Using RSA Encryption

```python
import alibabacloud_oss_v2 as oss

client = oss.Client(cfg)

mc = oss.crypto.MasterRsaCipher(
    mat_desc={"desc": "your master encrypt key material describe information"},
    public_key="yourRsaPublicKey",
    private_key="yourRsaPrivateKey"
)
encryption_client = oss.EncryptionClient(client, mc)

# Upload encrypted data
data = b'example data'
result = encryption_client.put_object(oss.PutObjectRequest(
    bucket="example_bucket",
    key="encrypted-object.txt",
    body=data,
))

# Download and decrypt
result = encryption_client.get_object(oss.GetObjectRequest(
    bucket="example_bucket",
    key="encrypted-object.txt",
))
decrypted = result.body.read()
```

### Encrypted Multipart Upload

```python
import os

part_size = 100 * 1024
data_size = os.path.getsize("/local/dir/example")

result = encryption_client.initiate_multipart_upload(oss.InitiateMultipartUploadRequest(
    bucket="example_bucket",
    key="example_key",
    cse_part_size=part_size,
    cse_data_size=data_size,
))

part_number = 1
upload_parts = []
with open("/local/dir/example", 'rb') as f:
    for start in range(0, data_size, part_size):
        n = min(part_size, data_size - start)
        reader = oss.io_utils.SectionReader(oss.io_utils.ReadAtReader(f), start, n)
        up_result = encryption_client.upload_part(oss.UploadPartRequest(
            bucket="example_bucket",
            key="example_key",
            upload_id=result.upload_id,
            part_number=part_number,
            cse_multipart_context=result.cse_multipart_context,
            body=reader,
        ))
        upload_parts.append(oss.UploadPart(part_number=part_number, etag=up_result.etag))
        part_number += 1

parts = sorted(upload_parts, key=lambda p: p.part_number)
encryption_client.complete_multipart_upload(oss.CompleteMultipartUploadRequest(
    bucket="example_bucket",
    key="example_key",
    upload_id=result.upload_id,
    complete_multipart_upload=oss.CompleteMultipartUpload(parts=parts),
))
```

## Error Handling

```python
import oss2

try:
    bucket.put_object('example.txt', 'content')
except oss2.exceptions.ServerError as e:
    print(f"Server error: {e.status}, Code: {e.code}, "
          f"Message: {e.message}, Request ID: {e.request_id}")
except oss2.exceptions.ClientError as e:
    print(f"Client error: {e}")
except oss2.exceptions.NoSuchBucket as e:
    print(f"Bucket does not exist: {e}")
except oss2.exceptions.NoSuchKey as e:
    print(f"Object does not exist: {e}")
except oss2.exceptions.AccessDenied as e:
    print(f"Access denied: {e}")
```

## Image Processing

```python
# Resize image
params = 'image/resize,m_fixed,w_100,h_100'
result = bucket.get_object('photo.jpg', params={'x-oss-process': params})

# Watermark
params = 'image/watermark,text_SGVsbG8gT1NT'
result = bucket.get_object('photo.jpg', params={'x-oss-process': params})

# Format conversion
params = 'image/format,png'
result = bucket.get_object('photo.jpg', params={'x-oss-process': params})

# Save processed image as new object
process = 'image/resize,w_200|sys/saveas,o_bmV3LmpwZw,b_bXktYnVja2V0'
bucket.process_object('photo.jpg', process)
```
