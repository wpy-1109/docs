# Troubleshooting SDK Errors

Source: https://help.aliyun.com/zh/oss/

## Overview

SDK errors can originate from client-side issues (configuration, network), or server-side issues (permissions, validation). This guide covers common SDK errors across different programming languages.

## Universal SDK Issues

### 1. Connection Timeout

**Symptoms**: `ConnectionError`, `TimeoutError`, or `SocketTimeoutException`

**Causes and Solutions**:

| Cause | Solution |
|---|---|
| Incorrect endpoint | Use correct regional endpoint: `oss-cn-hangzhou.aliyuncs.com` |
| Network connectivity | Verify DNS resolution and port 443/80 accessibility |
| Firewall blocking | Whitelist OSS endpoint IPs or domains |
| Proxy not configured | Configure HTTP/HTTPS proxy settings in SDK |
| VPN interference | Test without VPN or configure VPN routing |

### 2. DNS Resolution Failures

**Symptoms**: `UnknownHostException` or similar DNS errors

**Solutions**:
- Verify endpoint format: `oss-{region}.aliyuncs.com` (no bucket prefix)
- Use internal endpoint for ECS: `oss-{region}-internal.aliyuncs.com`
- Try IP-based access if DNS is unreliable
- Configure DNS servers: `100.100.2.136` (Alibaba Cloud internal DNS)

### 3. SSL/TLS Certificate Errors

**Symptoms**: `SSLError`, `CertificateException`

**Solutions**:
- Update CA certificates on the system
- Ensure system time is correct (expired certs appear invalid with wrong time)
- Update SDK to latest version
- Don't disable SSL verification in production

### 4. Memory Issues with Large Files

**Symptoms**: `OutOfMemoryError`, high memory usage

**Solutions**:
- Use streaming upload/download instead of loading entire file into memory
- Use multipart upload for large files
- Configure appropriate buffer sizes

## Java SDK Issues

### ClientException vs OSSException

```java
try {
    ossClient.putObject(bucketName, objectKey, inputStream);
} catch (OSSException oe) {
    // Server-side error
    System.out.println("Error Code: " + oe.getErrorCode());
    System.out.println("Request ID: " + oe.getRequestId());
    System.out.println("EC: " + oe.getEC());
} catch (ClientException ce) {
    // Client-side error (network, configuration)
    System.out.println("Error Message: " + ce.getMessage());
}
```

### Common Java SDK Issues

**Connection Pool Exhaustion**:
```java
// Always close OSSClient when done
ossClient.shutdown();

// Or use try-with-resources pattern
// Always close OSSObject after reading
OSSObject object = ossClient.getObject(bucketName, key);
try (InputStream is = object.getObjectContent()) {
    // Read content
}
```

**Thread Safety**: The `OSSClient` is thread-safe. Create one instance and reuse across threads.

### Maven Dependency Conflicts

**Symptoms**: `NoSuchMethodError`, `ClassNotFoundException`

**Solution**: Check for conflicting versions of dependencies:
```xml
<dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>aliyun-sdk-oss</artifactId>
    <version>3.17.4</version> <!-- Use latest version -->
</dependency>
```

## Python SDK Issues

### Common Python Errors

**oss2.exceptions.ServerError**:
```python
try:
    bucket.put_object('key', data)
except oss2.exceptions.ServerError as e:
    print(f"Status: {e.status}, Code: {e.code}")
    print(f"Request ID: {e.request_id}")
    print(f"Message: {e.message}")
```

**RequestError (Network issues)**:
```python
except oss2.exceptions.RequestError as e:
    # Network error, DNS failure, timeout
    print(f"Network error: {e}")
```

### Endpoint Configuration
```python
# Wrong - includes bucket name in endpoint
auth = oss2.Auth('key-id', 'key-secret')
bucket = oss2.Bucket(auth, 'https://my-bucket.oss-cn-hangzhou.aliyuncs.com', 'my-bucket')

# Correct
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'my-bucket')

# Internal endpoint (from ECS in same region)
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou-internal.aliyuncs.com', 'my-bucket')
```

## Node.js SDK Issues

### Common Configuration Errors

```javascript
// Wrong region format
const client = new OSS({
  region: 'cn-hangzhou', // Missing 'oss-' prefix
  accessKeyId: '...',
  accessKeySecret: '...',
  bucket: 'my-bucket'
});

// Correct
const client = new OSS({
  region: 'oss-cn-hangzhou',
  accessKeyId: '...',
  accessKeySecret: '...',
  bucket: 'my-bucket'
});
```

### Async/Promise Handling
```javascript
// Always handle errors in async operations
try {
  const result = await client.put('object-key', fileBuffer);
  console.log(result);
} catch (err) {
  console.error('Error:', err.code, err.message);
  console.error('RequestId:', err.params?.requestId);
}
```

### Browser.js Specific Issues

**STS Token Required**: Browser.js SDK must use STS temporary credentials:
```javascript
const client = new OSS({
  region: 'oss-cn-hangzhou',
  accessKeyId: stsToken.AccessKeyId,
  accessKeySecret: stsToken.AccessKeySecret,
  stsToken: stsToken.SecurityToken,
  bucket: 'my-bucket'
});
```

## Go SDK Issues

### Error Handling Pattern
```go
import "github.com/aliyun/aliyun-oss-go-sdk/oss"

err := bucket.PutObject("key", reader)
if err != nil {
    switch typedErr := err.(type) {
    case oss.ServiceError:
        fmt.Println("Code:", typedErr.Code)
        fmt.Println("RequestId:", typedErr.RequestId)
        fmt.Println("StatusCode:", typedErr.StatusCode)
    case oss.UnexpectedStatusCodeError:
        fmt.Println("Unexpected status:", typedErr.Got())
    default:
        fmt.Println("Error:", err)
    }
}
```

## Debugging Tips

### Enable SDK Logging

**Python**:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Java**:
```
-Dorg.slf4j.simpleLogger.log.com.aliyun.oss=debug
```

**Node.js**:
```javascript
const client = new OSS({
  // ... config
  timeout: 60000,  // Increase timeout for debugging
});
```

### Network Debugging
```bash
# Test connectivity
curl -v https://oss-cn-hangzhou.aliyuncs.com

# Test DNS resolution
nslookup oss-cn-hangzhou.aliyuncs.com

# Test with ossutil (validates credentials and connectivity)
ossutil ls oss://bucket-name/ -e oss-cn-hangzhou.aliyuncs.com
```
