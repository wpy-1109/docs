# Troubleshooting Download Failures

Source: https://help.aliyun.com/zh/oss/

## Overview

Download failures from OSS can result from permission issues, network problems, or incorrect request parameters. This guide covers common scenarios and their solutions.

## Common Download Errors

### 1. NoSuchKey (404)

**Error**: The specified object does not exist.

**Diagnosis**:
- Object key is case-sensitive
- Object may have been deleted or never existed
- Check for leading/trailing spaces in the key
- If versioning is enabled, check if a delete marker exists

**Solution**:
```bash
# List objects to verify the key exists
ossutil ls oss://bucket-name/path/to/

# Check if versioning has a delete marker
ossutil ls oss://bucket-name/object-key --all-versions
```

### 2. InvalidRange (416)

**Error**: The requested range is not satisfiable.

**Cause**: Range header specifies bytes beyond the object size.

**Solution**:
- First get the object size with HEAD request
- Ensure Range is within `0` to `Content-Length - 1`
- For Range downloads, handle the case where the object size changed

### 3. Access Denied for Private Objects

**Error**: 403 when downloading from a private Bucket.

**Solutions**:
1. **Generate signed URL** with appropriate expiration:
   ```python
   url = bucket.sign_url('GET', 'object-key', 3600)  # 1 hour
   ```

2. **Use STS temporary credentials** for SDK downloads

3. **Configure Bucket Policy** for authorized access

### 4. Content-Type Issues

**Problem**: Browser downloads file instead of displaying it, or vice versa.

**Cause**: Incorrect Content-Type metadata on the object.

**Solution**:
- Set correct Content-Type when uploading:
  ```python
  bucket.put_object('page.html', content,
      headers={'Content-Type': 'text/html; charset=utf-8'})
  ```
- Override Content-Type in signed URL:
  ```python
  params = {'response-content-type': 'text/html'}
  url = bucket.sign_url('GET', 'page.html', 3600, params=params)
  ```

### 5. Force Download vs. Inline Display

**Problem**: Need to force browser download instead of displaying inline.

**Solution**: Set `Content-Disposition` header:
```python
# When uploading
headers = {'Content-Disposition': 'attachment; filename="report.pdf"'}
bucket.put_object('report.pdf', content, headers=headers)

# Or in signed URL
params = {'response-content-disposition': 'attachment; filename="report.pdf"'}
url = bucket.sign_url('GET', 'report.pdf', 3600, params=params)
```

## Network-Related Download Issues

### Slow Downloads

**Causes and Solutions**:

| Cause | Solution |
|---|---|
| Cross-region access | Use CDN acceleration or Transfer Acceleration |
| Single-threaded download | Implement parallel range-based download |
| Bandwidth throttling | Check `x-oss-traffic-limit` setting |
| Large files | Use Range requests for segmented download |

### Download Interruption

**Solutions**:
1. Use **Range requests** for resumable download
2. Record the last downloaded byte position
3. Resume from that position on retry:
   ```python
   headers = {'Range': f'bytes={last_position}-'}
   result = bucket.get_object('large-file.zip', headers=headers)
   ```

### Connection Timeout

**Solutions**:
- Increase client timeout settings
- Use internal endpoint for same-region ECS access
- Check network connectivity and DNS resolution
- Verify firewall allows outbound connections to OSS endpoints

## Archive Storage Download Issues

### Cannot Download Archive Objects Directly

**Error**: `InvalidObjectState` - Object must be restored first.

**Solution**:
1. Initiate restore:
   ```python
   bucket.restore_object('archived-file.dat')
   ```
2. Wait for restore to complete (~1 minute for Archive, ~1-5 hours for Cold Archive)
3. Check restore status:
   ```python
   meta = bucket.head_object('archived-file.dat')
   # x-oss-restore: ongoing-request="false"  means ready
   ```
4. Download within the restore period (default 1 day, extendable to 7 days)

### Archive Direct Read Feature

For Buckets with **Archive Direct Read** enabled:
- Archive objects can be read directly without explicit restore
- Slightly higher latency for first access
- Additional data retrieval fees apply

## CORS-Related Download Issues

### Browser Shows CORS Error

**Symptoms**: XMLHttpRequest fails with "No 'Access-Control-Allow-Origin' header" in browser console.

**Solution**: Configure CORS rules on the Bucket:
1. Navigate to **Bucket > Permission Control > Cross-Origin Resource Sharing (CORS)**
2. Add CORS rule:
   - **Allowed Origins**: Your application domain (or `*` for testing)
   - **Allowed Methods**: GET, HEAD
   - **Allowed Headers**: `*`
   - **Expose Headers**: `x-oss-request-id, Content-Length, Content-Range, ETag`
   - **Max Age**: 3600

**If using CDN**: Configure CORS headers at CDN level (CDN may cache responses without CORS headers).

## Signed URL Download Issues

### Expired Signature

**Error**: 403 with `AccessDenied` after URL expiration.

**Solution**: Generate new signed URL with appropriate expiration time:
- For one-time downloads: 300-3600 seconds
- For sharing links: 3600-86400 seconds
- Maximum: 604800 seconds (7 days) for V4 signing

### URL Encoding Issues

**Problem**: Special characters in object key cause 404 or signature mismatch.

**Solution**: Ensure proper URL encoding. The SDK handles this automatically when using `sign_url()`. If constructing manually, encode the object key path.

## Troubleshooting Checklist

- [ ] Verify the object exists with the exact key (case-sensitive)
- [ ] Check Bucket and Object ACL/permissions
- [ ] For private objects, ensure signed URL or valid credentials
- [ ] Verify endpoint matches the Bucket's region
- [ ] Check Content-Type and Content-Disposition settings
- [ ] For archive objects, ensure restore is complete
- [ ] Configure CORS for browser-based downloads
- [ ] Check network connectivity and firewall rules
- [ ] Verify signed URL hasn't expired
