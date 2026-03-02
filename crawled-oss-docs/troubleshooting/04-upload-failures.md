# Troubleshooting Upload Failures

Source: https://help.aliyun.com/zh/oss/

## Overview

Upload failures can occur for various reasons including network issues, permission problems, and configuration errors. This guide covers common upload failure scenarios and their solutions.

## Common Upload Errors

### 1. EntityTooLarge (400)

**Error**: Object size exceeds the maximum allowed.

**Cause**: Using PutObject for files larger than 5 GB.

**Solution**:
- Use **Multipart Upload** for files >5 GB
- Maximum object size with multipart upload: 48.8 TB
- Recommended: Use multipart upload for files >100 MB

### 2. InvalidDigest (400)

**Error**: Content-MD5 header doesn't match the actual content.

**Cause**: Data corruption during transfer, or incorrect MD5 calculation.

**Solution**:
- Recalculate Content-MD5 from the actual request body
- Ensure Base64 encoding of the MD5 digest
- If not intentionally verifying, remove the Content-MD5 header

### 3. RequestTimeout (400)

**Error**: Upload operation timed out.

**Cause**: Slow network, large file size, or server-side processing delay.

**Solution**:
- Increase client timeout settings
- Use multipart upload with smaller part sizes
- Enable transfer acceleration for cross-region uploads
- Check network connectivity and bandwidth

### 4. InvalidPart / InvalidPartOrder (400)

**Error**: Multipart upload completion failed.

**Cause**: Part numbers or ETags don't match uploaded parts.

**Solution**:
- Ensure all parts are uploaded successfully before calling CompleteMultipartUpload
- Verify part numbers are sequential (1, 2, 3, ...)
- Use the ETag returned from each UploadPart response
- Parts must be listed in ascending order by part number

### 5. NoSuchUpload (404)

**Error**: Multipart upload ID not found.

**Cause**: Upload was already completed, aborted, or expired.

**Solution**:
- Reinitiate the multipart upload with InitiateMultipartUpload
- Check if lifecycle rules are aborting incomplete uploads
- Complete uploads in a timely manner

### 6. AccessDenied (403) During Upload

**Common Causes**:
- RAM user lacks `oss:PutObject` permission
- STS token expired during upload
- Bucket Policy denies the upload action
- Object key matches a deny rule

**Solution**:
- Verify RAM permissions include `oss:PutObject` (and `oss:PutObjectAcl` if setting ACL)
- For multipart upload, also need: `oss:InitiateMultipartUpload`, `oss:UploadPart`, `oss:CompleteMultipartUpload`
- Refresh STS token before expiration

## Client-Side Direct Upload Issues

### STS Token Expiration

**Problem**: Upload fails midway because STS token expired.

**Solution**:
- Default STS token validity: 3600 seconds (1 hour)
- For large files, request longer-lived tokens (max 43200 seconds / 12 hours)
- Implement token refresh logic before expiration
- Cache tokens and refresh when <60 seconds remaining

### CORS Errors (Browser Upload)

**Problem**: Browser blocks upload with CORS error.

**Solution**:
Configure CORS rules on the Bucket:
```
Allowed Origins: https://your-domain.com
Allowed Methods: PUT, POST, GET, HEAD
Allowed Headers: *
Expose Headers: x-oss-request-id, ETag
Max Age: 3600
```

### PostObject Signature Errors

**Problem**: PostObject returns 403 with signature mismatch.

**Common Causes**:
- Policy Base64 encoding error
- Signature calculation using wrong key
- Form fields don't match Policy conditions

**Solution**:
- Verify Policy is properly Base64 encoded
- Ensure signature is calculated using the Policy string (not raw JSON)
- All form fields referenced in Policy must be present in the POST request

## Network-Related Upload Failures

### Connection Reset / Timeout

**Causes**:
- Unstable network connection
- Firewall or proxy interference
- DNS resolution issues

**Solutions**:
1. Enable resumable upload (multipart with checkpoint)
2. Use smaller part sizes (1-10 MB recommended)
3. Use internal endpoint for same-region ECS
4. Enable transfer acceleration for cross-region
5. Check firewall rules for OSS endpoint ports (80/443)

### Slow Upload Speed

**Causes**:
- Long distance between client and OSS region
- Single-threaded upload
- Bandwidth limitations

**Solutions**:
1. Enable **Transfer Acceleration**
2. Use **parallel multipart upload** (multiple threads)
3. Choose the closest OSS region
4. Use internal endpoints from ECS in the same region
5. Check single-connection bandwidth throttling settings

## Multipart Upload Troubleshooting

### Best Practices
- Part size: 1-10 MB for most scenarios
- Minimum part size: 100 KB (except last part)
- Maximum parts: 10,000
- Maximum object size: 48.8 TB
- Use resumable upload with checkpoint file for reliability

### Cleanup Incomplete Uploads
Incomplete multipart uploads consume storage and incur fees:
```python
# List incomplete multipart uploads
for upload in oss2.MultipartUploadIterator(bucket):
    print(f"Key: {upload.key}, UploadId: {upload.upload_id}")
    # Abort if needed
    bucket.abort_multipart_upload(upload.key, upload.upload_id)
```

Or configure lifecycle rules:
```json
{
    "Rules": [
        {
            "ID": "cleanup-fragments",
            "Prefix": "",
            "Status": "Enabled",
            "AbortMultipartUpload": {
                "Days": 3
            }
        }
    ]
}
```

## Upload Verification

### Content-MD5 Verification
Include `Content-MD5` header to verify data integrity:
```python
import hashlib, base64

with open('file.txt', 'rb') as f:
    content_md5 = base64.b64encode(
        hashlib.md5(f.read()).digest()
    ).decode('utf-8')
```

### CRC64 Verification
OSS returns `x-oss-hash-crc64ecma` header for CRC64 verification:
```
x-oss-hash-crc64ecma: 318318444838145455
```
Compare with locally calculated CRC64 to verify data integrity.
