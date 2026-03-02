# OSS Troubleshooting & Error Codes

> Source: Alibaba Cloud OSS Documentation - Error Responses & Troubleshooting

## Error Response Format

OSS returns errors in XML format:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>NoSuchBucket</Code>
  <Message>The specified bucket does not exist.</Message>
  <RequestId>5C3D9175B6FC201293AD****</RequestId>
  <HostId>examplebucket.oss-cn-hangzhou.aliyuncs.com</HostId>
  <BucketName>examplebucket</BucketName>
</Error>
```

Key fields:
- **Code**: Machine-readable error code
- **Message**: Human-readable error description
- **RequestId**: Unique request identifier (critical for support tickets)
- **HostId**: The OSS endpoint that processed the request

## Complete Error Code Reference

### 4xx Client Errors

| HTTP Status | Error Code | Description | Solution |
|-------------|------------|-------------|----------|
| 400 | InvalidBucketName | Bucket name violates naming rules | Use 3-63 chars, lowercase, numbers, hyphens |
| 400 | InvalidObjectName | Object name is invalid | Object key max 1023 bytes, use URL encoding |
| 400 | TooManyBuckets | Exceeded max bucket limit | Request quota increase or delete unused buckets |
| 400 | InvalidArgument | Invalid request argument | Check parameter values and formats |
| 400 | MalformedXML | Request body XML is malformed | Validate XML syntax |
| 400 | InvalidDigest | Content-MD5 doesn't match body | Recalculate MD5 hash |
| 400 | IncompleteBody | Request body is incomplete | Retry upload, check network stability |
| 400 | FileImmutable | Object is immutable (WORM) | Cannot modify WORM-protected objects |
| 400 | EntityTooLarge | Object exceeds max size | Use multipart upload for large files |
| 400 | EntityTooSmall | Part size too small in multipart | Minimum part size is 100 KB (except last) |
| 400 | InvalidEncryptionAlgorithmError | Invalid encryption algorithm | Use AES256, KMS, or SM4 |
| 403 | AccessDenied | Authorization failure | Check RAM policy, bucket policy, ACL |
| 403 | InvalidAccessKeyId | AccessKey ID doesn't exist | Verify AccessKey ID is correct and active |
| 403 | SignatureDoesNotMatch | Signature verification failed | Check canonical request construction |
| 403 | RequestTimeTooSkewed | Clock difference > 15 minutes | Sync system clock with NTP |
| 403 | InvalidObjectState | Object state invalid for operation | Check storage class, restore if archived |
| 404 | NoSuchBucket | Bucket doesn't exist | Verify bucket name and region |
| 404 | NoSuchKey | Object doesn't exist | Verify object key, check lifecycle rules |
| 404 | NoSuchUpload | Multipart upload doesn't exist | Upload may have been aborted or completed |
| 405 | MethodNotAllowed | HTTP method not allowed | Check allowed methods for the endpoint |
| 409 | BucketAlreadyExists | Bucket name already taken | Choose a different bucket name |
| 409 | BucketNotEmpty | Bucket contains objects | Delete all objects and multipart uploads first |
| 409 | ObjectNotAppendable | Object is not appendable | Only appendable objects support append |
| 409 | PositionNotEqualToLength | Append position mismatch | Use correct append position |
| 412 | PreconditionFailed | Precondition in header not met | Check If-Match, If-None-Match conditions |
| 416 | InvalidRange | Requested range not satisfiable | Check Range header values |

### 5xx Server Errors

| HTTP Status | Error Code | Description | Solution |
|-------------|------------|-------------|----------|
| 500 | InternalError | Server internal error | Retry with exponential backoff |
| 503 | ServiceUnavailable | Service temporarily unavailable | Retry with exponential backoff |
| 503 | SlowDown | Request rate exceeded limit | Reduce request rate, implement backoff |
| 503 | Throttling | Request throttled | Distribute requests, use multiple buckets |

## Common Troubleshooting Scenarios

### AccessDenied (403)

**Possible Causes:**
1. Incorrect or expired AccessKey pair
2. Missing or incorrect RAM policy
3. Bucket policy restrictions
4. STS token expired
5. Unsigned request to private resource
6. IP restriction in bucket policy
7. VPC endpoint restrictions

**Troubleshooting Steps:**
1. Verify AccessKey ID and Secret are correct and active
2. Check RAM policy allows the specific action on the resource
3. Review bucket policy for deny rules
4. For STS, ensure token hasn't expired
5. Use RAM Policy Simulator to debug authorization

### SignatureDoesNotMatch (403)

**Possible Causes:**
1. Incorrect string-to-sign construction
2. Wrong encoding of parameters
3. Mismatch between signature version (V1 vs V4)
4. Proxy or CDN modifying request headers
5. Special characters in object key not properly encoded

**Troubleshooting Steps:**
1. Compare your canonical request with the expected format
2. Ensure correct URL encoding
3. Check signature version matches endpoint requirements
4. Use latest SDK version (handles signing automatically)
5. Enable debug logging to see the constructed signature

### RequestTimeTooSkewed (403)

**Cause:** Client clock differs from server by more than 15 minutes.

**Solution:**
1. Synchronize system clock using NTP
2. Use `ntpdate` or `chrony` on Linux
3. Check timezone settings (OSS uses UTC)

### NoSuchBucket (404)

**Possible Causes:**
1. Typo in bucket name
2. Bucket deleted
3. Wrong region endpoint
4. Bucket hasn't propagated yet (rare)

**Solution:**
1. Verify bucket name in OSS Console
2. Use correct regional endpoint
3. Check if bucket was recently deleted

### NoSuchKey (404)

**Possible Causes:**
1. Object path incorrect
2. Object deleted or expired (lifecycle rules)
3. URL encoding issues
4. Versioning: object has delete marker

**Solution:**
1. List objects to verify the key exists
2. Check lifecycle rules for expiration
3. Verify URL encoding of special characters
4. For versioned buckets, check for delete markers

### Upload Failures

**Common Issues:**
- **Timeout**: Increase connection and read timeouts
- **Network instability**: Use multipart upload with checkpoint resume
- **Large file**: Use multipart upload (required for files > 5 GB)
- **Content-MD5 mismatch**: Ensure correct MD5 calculation

### Download Failures

**Common Issues:**
- **Archived object**: Restore the object first (wait for restore to complete)
- **403 on private object**: Use signed URL or SDK with credentials
- **Slow download**: Use Transfer Acceleration or CDN
- **Partial content**: Set correct Range header

### CORS Errors (Browser)

**Symptoms:** Browser console shows CORS-related errors.

**Solution:**
1. Configure CORS rules on the bucket:
   - Allowed Origins: Your domain (or `*` for testing)
   - Allowed Methods: GET, PUT, POST, DELETE, HEAD
   - Allowed Headers: `*` or specific headers
   - Expose Headers: ETag, x-oss-request-id
   - Max Age: 3600
2. Verify CORS rules apply to the correct bucket
3. Check browser developer tools for the specific CORS error

### Slow Transfer

**Possible Causes:**
1. Geographic distance to OSS endpoint
2. Network congestion
3. Single-threaded upload/download
4. Small part size in multipart

**Solutions:**
1. Use Transfer Acceleration
2. Use CDN for downloads
3. Use internal endpoint for same-region access
4. Increase concurrent jobs and part size
5. Use multipart upload/download

## Diagnostic Tools

### RequestId

Always capture the **RequestId** from error responses. It's the fastest way to get help from Alibaba Cloud support.

```bash
# Get RequestId from response headers
curl -v https://bucket.oss-region.aliyuncs.com/object 2>&1 | grep x-oss-request-id
```

### ossutil probe

```bash
# Test network connectivity
ossutil probe --probe-item download-speed --object oss://bucket/object

# Upload probe
ossutil probe --probe-item upload-speed --bucket oss://bucket
```

### CloudMonitor

- Monitor request latency, error rates, bandwidth
- Set alarms for abnormal patterns
- View dashboard for bucket-level metrics

### Access Logging

Enable access logging to analyze request patterns:
```bash
ossutil api put-bucket-logging --bucket mybucket --logging-enabled \
  --target-bucket log-bucket --target-prefix mybucket-logs/
```
