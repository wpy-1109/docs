# Troubleshooting Signature Errors

Source: https://help.aliyun.com/zh/oss/

## Overview

Signature errors (SignatureDoesNotMatch) are among the most common OSS issues. OSS uses HMAC-SHA1 (V1) or HMAC-SHA256 (V4) to authenticate requests. Any mismatch in the signing process results in a 403 error.

## Understanding OSS Signatures

### Signature V1 (Default)
```
Signature = Base64(HMAC-SHA1(AccessKeySecret,
    VERB + "\n"
    + Content-MD5 + "\n"
    + Content-Type + "\n"
    + Date + "\n"
    + CanonicalizedOSSHeaders
    + CanonicalizedResource
))

Authorization: OSS AccessKeyId:Signature
```

### Signature V4 (Recommended)
```
Signature = HMAC-SHA256(SigningKey, StringToSign)

Authorization: OSS4-HMAC-SHA256
    Credential=AccessKeyId/date/region/oss/aliyun_v4_request,
    SignedHeaders=...,
    Signature=...
```

## Common Signature Errors

### 1. Wrong AccessKey Secret

**Symptom**: Every request fails with SignatureDoesNotMatch.

**Diagnosis**:
- Verify AccessKey ID matches the Secret
- Check for copy-paste errors (trailing spaces, wrong characters)
- Ensure the AccessKey is for the correct Alibaba Cloud account
- Check if the AccessKey has been rotated/regenerated

### 2. String-to-Sign Mismatch

**Symptom**: The error response includes the expected string-to-sign.

**Debugging**:
Compare your string-to-sign with the one from OSS:

```xml
<StringToSignBytes>47 45 54 0A 0A 0A ...</StringToSignBytes>
```

**Common Causes**:
- Wrong HTTP verb (GET vs POST)
- Extra or missing headers in canonical headers
- Wrong resource path encoding
- Missing or extra newline characters

### 3. Date/Time Issues

**Symptom**: Intermittent signature failures.

**Causes**:
- System clock drift (>15 minutes from server time)
- Using local time instead of GMT/UTC in Date header
- Time zone calculation errors

**Solution**:
```bash
# Sync clock
sudo ntpdate ntp.aliyun.com

# Use UTC in requests
date -u
```

### 4. Content-Type Mismatch

**Symptom**: Signature fails even though other fields look correct.

**Cause**: Content-Type in the signature string doesn't match the actual request header.

**Solution**:
- Ensure Content-Type is consistent between signature and request
- For empty Content-Type, use empty string in signature
- SDKs handle this automatically; avoid manually overriding

### 5. URL Encoding Issues

**Symptom**: Signature fails for objects with special characters in the key.

**Problematic Characters**: spaces, `+`, `%`, `#`, `?`, `&`, `=`, Chinese characters

**Solution**:
- Use RFC 3986 URL encoding for object keys in the canonical resource
- Encode path separators `/` only in object key portion, not Bucket portion
- Use SDK methods that handle encoding automatically

### 6. Signed URL Expiration

**Symptom**: Previously working URL suddenly returns 403.

**Cause**: The Expires timestamp has passed.

**Solution**:
- Generate new signed URL with appropriate expiration
- V1 signed URLs: custom expiration time
- V4 signed URLs: maximum 604800 seconds (7 days)

### 7. Canonical Headers Issues

**Symptom**: Signature fails when using custom x-oss-* headers.

**Rules for Canonical OSS Headers**:
1. Include all headers starting with `x-oss-`
2. Convert header names to lowercase
3. Sort headers alphabetically
4. Combine values for duplicate header names with comma
5. Trim whitespace from header values
6. Separate header name and value with colon (no space)
7. End each header line with `\n`

**Example**:
```
x-oss-copy-source:/source-bucket/source-object
x-oss-meta-author:alice
x-oss-meta-tag:v1
```

### 8. Sub-Resource Ordering

**Symptom**: Signature fails when using query parameters for sub-resources.

**Rules**:
- Sub-resources must be sorted alphabetically
- Separate sub-resources with `&`
- Include only recognized sub-resources in the signature

**Recognized sub-resources include**: `acl`, `cors`, `delete`, `lifecycle`, `location`, `logging`, `policy`, `requestPayment`, `restore`, `tagging`, `uploadId`, `uploads`, `versionId`, `versioning`, `versions`, `website`

## SDK-Specific Issues

### Java SDK
```java
// Common mistake: not closing input stream
// This causes connection leaks and eventual failures
OSSObject object = ossClient.getObject(bucketName, objectKey);
try (InputStream is = object.getObjectContent()) {
    // Process content
} // Auto-closes the stream
```

### Python SDK
```python
# Ensure endpoint doesn't include bucket name
# Wrong:
bucket = oss2.Bucket(auth, 'https://my-bucket.oss-cn-hangzhou.aliyuncs.com', 'my-bucket')

# Correct:
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'my-bucket')
```

### JavaScript SDK
```javascript
// Ensure region format is correct
// Wrong: region: 'cn-hangzhou'
// Correct: region: 'oss-cn-hangzhou'
const client = new OSS({
  region: 'oss-cn-hangzhou',
  accessKeyId: '...',
  accessKeySecret: '...',
  bucket: 'my-bucket'
});
```

## Debugging Techniques

### 1. Enable SDK Debug Logging
Most OSS SDKs support debug logging that shows the string-to-sign:

**Python**:
```python
import logging
logging.getLogger('oss2').setLevel(logging.DEBUG)
```

**Java**:
```xml
<logger name="com.aliyun.oss" level="DEBUG"/>
```

### 2. Compare String-to-Sign
Extract the string-to-sign from both client and server error response, and compare byte by byte.

### 3. Use SDK Instead of Manual Signing
If you're manually constructing signatures, switch to the official SDK. Manual signing is error-prone and the SDK handles all edge cases.

### 4. Test with ossutil
Use ossutil to verify that the AccessKey works:
```bash
ossutil ls oss://bucket-name/ --access-key-id=xxx --access-key-secret=yyy
```

## Prevention

1. **Always use official SDKs** instead of manual signing
2. **Keep SDKs updated** to the latest version
3. **Use STS** instead of long-term AccessKeys in client applications
4. **Sync system clocks** with NTP
5. **Use environment variables** for AccessKeys (never hardcode)
