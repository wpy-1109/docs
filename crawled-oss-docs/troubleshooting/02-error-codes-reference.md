# OSS Error Codes and Self-Service Troubleshooting

Source: https://help.aliyun.com/zh/oss/user-guide/overview-14

## Error Response Structure

A typical OSS error response contains the following fields:

### Error Response Example
```xml
HTTP/1.1 400 Bad Request
Server: AliyunOSS
Date: Thu, 11 Aug 2019 01:44:54 GMT
Content-Type: application/xml
x-oss-request-id: 57ABD896CCB80C366955****
x-oss-ec: 0016-00000502

<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>MissingArgument</Code>
  <Message>Missing Some Required Arguments.</Message>
  <RequestId>57ABD896CCB80C366955****</RequestId>
  <HostId>oss-example.oss-cn-hangzhou.aliyuncs.com</HostId>
  <EC>0016-00000502</EC>
  <RecommendDoc>https://api.aliyun.com/troubleshoot?q=0016-00000502</RecommendDoc>
</Error>
```

### Key Fields

| Field | Description | Usage |
|---|---|---|
| **RecommendDoc** | Official solution link for this EC code | Primary: click to get recommended solution |
| **EC** | Fine-grained error code, uniquely identifies the error cause | Core: use for self-service troubleshooting |
| **HTTP Status Code** | General request result status (e.g., 400, 403, 404) | Initial: determine problem direction |
| **RequestId** | Unique request identifier | Required when contacting technical support |
| **Code** | OSS-defined general error code | Identify error category |
| **Message** | Detailed error description | Understand specific error |

### Response Headers

| Header | Description |
|---|---|
| `x-oss-ec` | Fine-grained error code (same as EC in body) |
| `x-oss-request-id` | Unique request ID for support tickets |

## Self-Service Troubleshooting Flow

### Step 1: Locate Key Information
1. Read the **Message** field for direct error description
2. Note the **EC** code for precise error identification
3. Note the **HTTP status code** for general category
4. Save the **RequestId** for support escalation

### Step 2: Get Solution
Two approaches:
1. **Visit RecommendDoc link** directly from error response
2. **Look up EC code** in the error code list if RecommendDoc is not present

### Step 3: Escalate If Needed
If self-service troubleshooting doesn't resolve the issue:
- Prepare the **RequestId**
- Describe the error scenario
- Contact Alibaba Cloud technical support

**Important**: EC codes are for troubleshooting only and may change. Do NOT build business logic that depends on EC codes.

## HTTP Error Code Reference

### 400 Bad Request

| Error Code | Description | Solution |
|---|---|---|
| `MissingArgument` | Required argument missing | Check API documentation for required parameters |
| `InvalidArgument` | Invalid argument value | Verify parameter values match expected format |
| `MalformedXML` | Request body XML is malformed | Validate XML structure and encoding |
| `InvalidBucketName` | Bucket name doesn't comply with naming rules | Use 3-63 chars: lowercase letters, numbers, hyphens |
| `InvalidObjectName` | Object key is invalid | Don't start with `/` or `\`; max 1023 bytes |
| `EntityTooLarge` | Object exceeds maximum size | Use multipart upload for files >5 GB |
| `EntityTooSmall` | Part size too small in multipart upload | Minimum part size is 100 KB (except last part) |
| `TooManyBuckets` | Bucket quota exceeded (default 100) | Request quota increase via support ticket |
| `InvalidDigest` | Content-MD5 doesn't match | Recalculate and send correct MD5 digest |
| `InvalidEncryptionAlgorithmError` | Unsupported encryption algorithm | Use supported algorithms: AES256, KMS |

### 403 Forbidden

| Error Code | Description | Solution |
|---|---|---|
| `AccessDenied` | Access denied | Check RAM policies, Bucket Policy, ACL, STS token validity |
| `SignatureDoesNotMatch` | Signature mismatch | Verify AccessKey Secret, signing algorithm, string-to-sign |
| `InvalidAccessKeyId` | AccessKey ID invalid or expired | Confirm AccessKey ID exists and is active in RAM console |
| `RequestTimeTooSkewed` | Time difference >15 minutes | Sync system clock with NTP server |
| `AccessDenied (Block Public Access)` | Public access blocked | Disable Block Public Access if public access is intended |
| `AccessDenied (Bucket Policy)` | Denied by Bucket Policy | Review Bucket Policy conditions (IP, Referer, etc.) |

### 404 Not Found

| Error Code | Description | Solution |
|---|---|---|
| `NoSuchBucket` | Bucket doesn't exist | Verify bucket name and region |
| `NoSuchKey` | Object doesn't exist | Verify exact object key (case-sensitive) |
| `NoSuchUpload` | Multipart upload ID doesn't exist | Upload may have been completed or aborted; reinitiate |
| `NoSuchCORSConfiguration` | No CORS rules configured | Configure CORS if cross-origin access is needed |
| `NoSuchWebsiteConfiguration` | No static website configuration | Configure static website hosting if needed |

### 405 Method Not Allowed

| Error Code | Description | Solution |
|---|---|---|
| `MethodNotAllowed` | HTTP method not supported | Use correct HTTP method for the API operation |

### 409 Conflict

| Error Code | Description | Solution |
|---|---|---|
| `BucketAlreadyExists` | Bucket name already taken globally | Choose a different, globally unique bucket name |
| `BucketNotEmpty` | Cannot delete non-empty Bucket | Delete all objects and abort incomplete multipart uploads first |
| `PositionNotEqualToLength` | Append position mismatch | Get current object length and use it as append position |
| `ObjectNotAppendable` | Object is not appendable type | Only objects created with AppendObject can be appended |

### 416 Range Not Satisfiable

| Error Code | Description | Solution |
|---|---|---|
| `InvalidRange` | Requested range is invalid | Ensure Range header is within 0 to content-length - 1 |

### 500 Internal Server Error

| Error Code | Description | Solution |
|---|---|---|
| `InternalError` | OSS internal error | Retry with exponential backoff |

### 503 Service Unavailable

| Error Code | Description | Solution |
|---|---|---|
| `ServiceUnavailable` | Service temporarily unavailable | Retry after delay |
| `SlowDown` | Request rate too high, throttled | Reduce request rate; use random key prefixes |
| `ServiceUnavailable (QPS)` | QPS limit exceeded | Distribute requests across partitions; contact support for higher limits |

## Getting the RequestId

### From HTTP Response Header
```
x-oss-request-id: 57ABD896CCB80C366955****
```

### From SDK Error Object
Most OSS SDKs expose the RequestId in the exception/error object:

**Java**:
```java
try {
    // OSS operation
} catch (OSSException e) {
    System.out.println("RequestId: " + e.getRequestId());
    System.out.println("ErrorCode: " + e.getErrorCode());
    System.out.println("EC: " + e.getEC());
}
```

**Python**:
```python
try:
    # OSS operation
except oss2.exceptions.OssError as e:
    print(f"RequestId: {e.request_id}")
    print(f"ErrorCode: {e.code}")
```

### From Browser Developer Tools
Open Network tab (F12) > Select the failed request > View Response Headers > Find `x-oss-request-id`

### From ossutil
Error messages from ossutil include the RequestId automatically.
