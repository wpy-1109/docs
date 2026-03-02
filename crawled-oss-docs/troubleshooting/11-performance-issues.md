# Troubleshooting Performance Issues

Source: https://help.aliyun.com/zh/oss/

## Overview

This guide covers diagnosing and resolving OSS performance issues including slow transfers, high latency, and throughput limitations.

## Diagnosing Performance Issues

### Key Metrics to Monitor

| Metric | Where to Check | Healthy Range |
|---|---|---|
| Request latency (P50/P99) | CloudMonitor | <100ms for small objects |
| Error rate (4xx/5xx) | CloudMonitor, Access logs | <1% |
| Throughput | CloudMonitor | Depends on workload |
| Cache hit rate (CDN) | CDN Console | >80% for static content |
| Network bandwidth | ECS/client monitoring | Not saturated |

### Identifying Bottlenecks

1. **Server-side**: Check for 503 (throttling), high latency in access logs
2. **Network**: High RTT, packet loss, DNS issues
3. **Client-side**: CPU/memory constraints, thread pool exhaustion, connection limits

## Common Performance Issues

### 1. Slow Upload Speed

**Diagnosis**:
- Test with different file sizes
- Compare internal vs external endpoint performance
- Check single vs multi-threaded upload

**Solutions**:

| Solution | When to Use |
|---|---|
| Multipart upload | Files >100 MB |
| Transfer Acceleration | Cross-region or cross-border |
| Internal endpoints | ECS in same region |
| Parallel upload threads | Multiple files or large files |
| Increase part size | For very large files (>1 GB) |

### 2. Slow Download Speed

**Solutions**:
- Use CDN for frequently accessed content
- Use Range requests for partial/parallel download
- Use internal endpoints from same-region ECS
- Enable Transfer Acceleration for cross-region access

### 3. High First-Byte Latency

**Possible Causes**:
- DNS resolution time
- TCP connection establishment
- TLS handshake (for HTTPS)
- Server processing time

**Solutions**:
- Use connection pooling (reuse connections)
- Pre-resolve DNS
- Use HTTP/2 (via CDN)
- Use internal endpoints

### 4. Partition Hotspot Throttling

**Symptoms**: 503 SlowDown for specific key prefixes.

**Cause**: Sequential key prefixes cause hot partitions.

**Solution**: Add random hash prefixes to object keys (see Performance Best Practices doc).

### 5. ListObjects Performance

**Problem**: ListObjects is slow for Buckets with millions of objects.

**Solutions**:
- Use `prefix` and `delimiter` to narrow results
- Limit `max-keys` to reasonable page size (100-1000)
- Use OSS Inventory for bulk object auditing instead of listing
- Use `marker`/`continuation-token` for pagination

## Network Optimization

### Same-Region Access

Always use internal endpoints for ECS-to-OSS within the same region:
```
Internal: oss-cn-hangzhou-internal.aliyuncs.com
Public:   oss-cn-hangzhou.aliyuncs.com
```

**Benefits**: Zero traffic cost, lower latency, higher bandwidth.

### Cross-Region Access

Options ranked by performance:
1. **CDN** (best for read-heavy, cacheable content)
2. **Transfer Acceleration** (best for uploads and large file transfers)
3. **ECS reverse proxy in target region** (for custom logic)
4. **Direct access** (acceptable for occasional access)

### Connection Optimization

```python
# Python: Reuse session for connection pooling
import oss2

auth = oss2.Auth('key-id', 'key-secret')
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'my-bucket')
# Reuse this bucket instance across requests
```

```java
// Java: Configure connection pool
ClientBuilderConfiguration config = new ClientBuilderConfiguration();
config.setMaxConnections(200);          // Max connections
config.setSocketTimeout(10000);         // Socket timeout
config.setConnectionTimeout(10000);     // Connection timeout
config.setMaxErrorRetry(3);             // Max retries

OSSClient ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret, config);
```

## Throughput Optimization

### Parallel Operations

```python
from concurrent.futures import ThreadPoolExecutor

def upload_file(args):
    key, file_path = args
    with open(file_path, 'rb') as f:
        bucket.put_object(key, f)

files = [('key1', 'file1'), ('key2', 'file2'), ...]

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(upload_file, files)
```

### Batch Operations

Use batch APIs when available:
- `DeleteMultipleObjects`: Delete up to 1,000 objects per request
- `ListObjectsV2`: List up to 1,000 objects per request
- Use multipart upload for individual large files

## Monitoring and Alerting

### CloudMonitor Setup

Configure alerts for:
- P99 latency exceeding threshold (e.g., >500ms)
- 5xx error rate exceeding 1%
- Bandwidth utilization >80%
- Request count sudden spikes

### Access Log Analysis

Enable access logging and analyze with SLS:
```sql
-- Find slowest requests
SELECT request_uri, request_time, http_status
FROM oss_access_log
WHERE request_time > 1000  -- requests taking >1 second
ORDER BY request_time DESC
LIMIT 100
```
