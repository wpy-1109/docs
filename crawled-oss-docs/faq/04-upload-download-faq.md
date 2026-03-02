# OSS Upload and Download FAQ

Source: https://help.aliyun.com/zh/oss/faq-overview

## Upload FAQ

### What upload methods does OSS support?
| Method | Max Size | Use Case |
|---|---|---|
| **Simple Upload (PutObject)** | 5 GB | Small files, simple scenarios |
| **Multipart Upload** | 48.8 TB | Large files, resumable uploads |
| **Append Upload** | 5 GB | Log files, streaming data |
| **Form Upload (PostObject)** | 5 GB | Browser-based HTML form upload |
| **Resumable Upload** | 48.8 TB | Unreliable networks, large files |

### How do I upload large files?
Use **multipart upload**:
1. Call `InitiateMultipartUpload` to get an upload ID
2. Split the file into parts and upload each with `UploadPart`
3. Call `CompleteMultipartUpload` to merge all parts
4. Recommended part size: 1-10 MB
5. Maximum 10,000 parts per upload

### How do I upload from the browser?
Three approaches:
1. **STS credentials + OSS JS SDK** (recommended for most cases)
2. **Server-generated signed URL** (simplest, no SDK needed)
3. **PostObject with server-generated signature** (HTML form-based)

### Can I upload to OSS without going through my server?
Yes, use **client-side direct upload**:
1. Client requests STS temporary credentials from your server
2. Client uploads directly to OSS using the credentials
3. This avoids double-transfer through your server

### How do I set Content-Type automatically?
OSS SDKs automatically detect Content-Type based on file extension. You can also set it explicitly:
```python
bucket.put_object('image.jpg', data, headers={'Content-Type': 'image/jpeg'})
```

### How do I handle upload progress?
Most SDKs support progress callbacks:
```python
def progress_callback(consumed, total):
    print(f'{consumed}/{total} bytes uploaded ({consumed/total*100:.1f}%)')

bucket.put_object('file.zip', data, progress_callback=progress_callback)
```

## Download FAQ

### How do I generate a temporary download URL?
Use **signed URLs**:
```python
# Python: Generate a signed URL valid for 1 hour
url = bucket.sign_url('GET', 'private-file.pdf', 3600)
```

Maximum signed URL validity:
- Signature V1: No specific limit (controlled by Expires parameter)
- Signature V4: 604800 seconds (7 days)

### How do I force a file to download instead of opening in the browser?
Set `Content-Disposition` response header:
```python
params = {'response-content-disposition': 'attachment; filename="report.pdf"'}
url = bucket.sign_url('GET', 'report.pdf', 3600, params=params)
```

### How do I download only part of a file?
Use HTTP **Range** header:
```python
headers = {'Range': 'bytes=0-999'}  # First 1000 bytes
result = bucket.get_object('large-file.zip', headers=headers)
```

### Can I download multiple files as a ZIP?
OSS does not natively support this. Options:
1. Use **Function Compute** to create a ZIP on-the-fly
2. Pre-create ZIP files and store them in OSS
3. Download files individually on the client side

### How do I download archive storage objects?
1. First **restore** the object (initiate thaw)
2. Wait for restore to complete (~1 minute for Archive with Direct Read)
3. Then download normally
4. Restored copies are available for 1-7 days

## Data Integrity FAQ

### How does OSS verify data integrity?
- **Content-MD5**: Include in upload request for server-side verification
- **CRC-64**: OSS returns `x-oss-hash-crc64ecma` header for client-side verification
- **ETag**: MD5 of the object for simple uploads; multipart uploads have a different ETag format

### Can I use ETag as MD5 for integrity checking?
- **Simple upload**: ETag equals the MD5 hash of the object (can be used for verification)
- **Multipart upload**: ETag is NOT the MD5 of the entire file; it's a composite hash. Use CRC-64 instead.

## Transfer Optimization FAQ

### How do I speed up cross-region transfers?
1. Enable **Transfer Acceleration** on the Bucket
2. Use the acceleration endpoint: `oss-accelerate.aliyuncs.com`
3. Or use **CDN** for read-heavy workloads

### How do I upload/download concurrently?
```python
# Python: Parallel multipart upload
from oss2 import SizedFileAdapter, determine_part_size
from oss2.models import PartInfo
import concurrent.futures

# Use SDK's built-in resumable upload with multiple threads
oss2.resumable_upload(bucket, 'object-key', '/path/to/file',
    multipart_threshold=100*1024*1024,  # 100 MB
    part_size=10*1024*1024,             # 10 MB parts
    num_threads=4)                       # 4 parallel threads
```

### What is the bandwidth limit per connection?
You can set per-connection bandwidth limits using `x-oss-traffic-limit`:
- Minimum: 819200 bit/s (100 KB/s)
- Maximum: 838860800 bit/s (100 MB/s)
