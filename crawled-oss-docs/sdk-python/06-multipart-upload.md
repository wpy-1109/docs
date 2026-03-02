# Python SDK - Multipart Upload

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python-multipart-upload

## V1 SDK - Multipart Upload

### Basic Multipart Upload

```python
import oss2

# Step 1: Initiate multipart upload
upload_id = bucket.init_multipart_upload('large-file.zip').upload_id

# Step 2: Upload parts
parts = []
part_size = 5 * 1024 * 1024  # 5MB per part

with open('/path/to/large-file.zip', 'rb') as f:
    part_number = 1
    while True:
        data = f.read(part_size)
        if not data:
            break
        result = bucket.upload_part('large-file.zip', upload_id,
                                     part_number, data)
        parts.append(oss2.models.PartInfo(part_number, result.etag))
        part_number += 1

# Step 3: Complete multipart upload
bucket.complete_multipart_upload('large-file.zip', upload_id, parts)
```

### Resumable Upload (Recommended for Large Files)

```python
# Automatic multipart upload with resume support
oss2.resumable_upload(
    bucket,
    'large-file.zip',
    '/path/to/large-file.zip',
    store=oss2.ResumableStore(root='/tmp'),
    multipart_threshold=100 * 1024 * 1024,  # Use multipart for files > 100MB
    part_size=10 * 1024 * 1024,              # 10MB per part
    num_threads=4                             # 4 concurrent upload threads
)
```

### Abort Multipart Upload

```python
bucket.abort_multipart_upload('large-file.zip', upload_id)
```

### List Multipart Uploads

```python
# List uploaded parts
for part in oss2.PartIterator(bucket, 'large-file.zip', upload_id):
    print(f"Part: {part.part_number}, Size: {part.size}, ETag: {part.etag}")

# List all ongoing multipart uploads
for upload in oss2.MultipartUploadIterator(bucket):
    print(f"Key: {upload.key}, Upload ID: {upload.upload_id}")
```

## V2 SDK - Multipart Upload

```python
import alibabacloud_oss_v2 as oss

# Step 1: Initiate
result = client.initiate_multipart_upload(oss.InitiateMultipartUploadRequest(
    bucket=bucket_name,
    key=object_name,
))
upload_id = result.upload_id

# Step 2: Upload parts
parts = []
part_size = 5 * 1024 * 1024
part_number = 1

with open('/path/to/file', 'rb') as f:
    while True:
        data = f.read(part_size)
        if not data:
            break
        up_result = client.upload_part(oss.UploadPartRequest(
            bucket=bucket_name,
            key=object_name,
            upload_id=upload_id,
            part_number=part_number,
            body=data,
        ))
        parts.append(oss.UploadPart(part_number=part_number, etag=up_result.etag))
        part_number += 1

# Step 3: Complete
parts.sort(key=lambda p: p.part_number)
client.complete_multipart_upload(oss.CompleteMultipartUploadRequest(
    bucket=bucket_name,
    key=object_name,
    upload_id=upload_id,
    complete_multipart_upload=oss.CompleteMultipartUpload(parts=parts),
))
```

## Presigned URL Multipart Upload

```python
import alibabacloud_oss_v2 as oss
import requests

# Initiate via presigned URL
init_result = client.presign(oss.InitiateMultipartUploadRequest(
    bucket=bucket_name,
    key=object_name,
))

with requests.post(init_result.url, headers=init_result.signed_headers) as resp:
    obj = oss.InitiateMultipartUploadResult()
    oss.serde.deserialize_xml(xml_data=resp.content, obj=obj)
    upload_id = obj.upload_id

# Generate presigned URLs for parts
PART_SIZE = 5 * 1024 * 1024
total_parts = (file_size + PART_SIZE - 1) // PART_SIZE
parts = []

for part_number in range(1, total_parts + 1):
    req = oss.UploadPartRequest(
        bucket=bucket_name,
        key=object_name,
        part_number=part_number,
        upload_id=upload_id,
        expiration_in_seconds=3600,
    )
    presign_result = client.presign(req)
    parts.append({
        "part_number": part_number,
        "url": presign_result.url,
        "method": "PUT"
    })
```
