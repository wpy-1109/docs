# Performance Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/oss-performance-best-practices/

## Overview

This guide describes multiple methods to leverage Alibaba Cloud OSS's distributed architecture to improve data processing speed, reduce latency, and accelerate application responsiveness.

## 1. Replace Sequential Prefixes with Random Prefixes

OSS automatically partitions data based on the UTF-8 encoding order of object keys to support large-scale file management and high-concurrency requests. Using sequential prefixes (timestamps, dictionary-ordered strings) can cause partition overload.

When request rates exceed **2,000 requests/second** (download, upload, delete, copy, get metadata = 1 operation; batch delete N files, list N files = N operations), this causes:

- **Hot partition formation**: High-frequency requests concentrate on specific partitions, exhausting I/O capacity or triggering automatic rate limiting
- **Rate limiting**: Hot partitions trigger continuous partition rebalancing, extending request processing time

**Note**: Partition rebalancing is based on real-time system state analysis, not fixed splitting rules. Files with sequential prefixes may remain in hot partitions after rebalancing.

### Solution 1: Add Hexadecimal Hash Prefixes

**Before** (sequential timestamp prefix):
```
sample-bucket-01/2024-07-19/customer-1/file1
sample-bucket-01/2024-07-19/customer-2/file2
sample-bucket-01/2024-07-19/customer-3/file3
```

**After** (4-character MD5 hash prefix):
```
sample-bucket-01/9b11/2024-07-19/customer-1/file1
sample-bucket-01/9fc2/2024-07-19/customer-2/file2
sample-bucket-01/d1b3/2024-07-19/customer-3/file3
```

A 4-character hexadecimal prefix provides 16^4 = **65,536 possible combinations**. With a per-partition limit of 2,000 ops/sec, this supports theoretical throughput of over 130 million operations/second.

To list files for a specific date, list all objects in the bucket and filter by date.

### Solution 2: Reverse Object Keys

**Before** (millisecond Unix timestamp):
```
sample-bucket-02/1513160001245.log
sample-bucket-02/1513160001722.log
sample-bucket-02/1513160001836.log
```

**After** (reversed):
```
sample-bucket-02/5421000613151.log
sample-bucket-02/2271000613151.log
sample-bucket-02/6381000613151.log
```

The first 3 digits represent milliseconds (1,000 possible values), the 4th digit changes every second, the 5th every 10 seconds, etc. Reversing greatly increases prefix randomness, distributing load evenly across partitions.

## 2. Use Byte Range Fetches

When downloading large files (>100 MB), network instability may interrupt transfers. Use HTTP Range requests to download partial content:

```http
GET /ObjectName HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 19 Jul 2024 17:27:45 GMT
Authorization: SignatureValue
Range: bytes=[$ByteRange]
```

The Range header specifies data segments within 0 to `content-length - 1`.

## 3. Use OSS Transfer Acceleration

Enable Transfer Acceleration for:
- Long-distance data transfers (e.g., from mainland China to overseas regions)
- Uploading/downloading GB or TB-level large files

Transfer Acceleration uses globally distributed data centers and intelligent routing to direct users to the nearest access point, providing end-to-end acceleration for uploads and downloads using optimized network protocols.

## 4. Use CDN for Frequently Accessed Content

CDN replicates static content to edge nodes worldwide, allowing users to retrieve content from the nearest node.

**How it works**:
1. User requests an OSS object
2. CDN checks if the edge node has the object
3. If not cached or expired, CDN fetches from the origin OSS and caches at the edge
4. When origin content changes, CDN automatically updates edge node caches

CDN effectively reduces origin OSS load, improves access speed and stability, and is especially suitable for enterprises with globally distributed users.

## 5. Use Latest OSS SDK Version

Latest SDK versions provide:
- **New feature support**: Latest APIs, optimized algorithms, more efficient encoding
- **Error handling and retry mechanisms**: Automatic handling of common errors (e.g., HTTP 503), reducing failures from network issues
- **Transfer management**: Higher-level transfer management with automatic connection scaling and range requests
- **Multi-threading support**: Parallel request processing for improved data throughput
- **Memory management optimization**: Reduced memory overhead, improved efficiency
- **Compatibility enhancements**: Bug fixes and improved compatibility with third-party libraries and OS platforms

## 6. Co-locate OSS and ECS in the Same Region

Deploying ECS instances and OSS buckets in the same region:
- Significantly reduces data transfer latency
- Improves read speed and overall application performance
- **Eliminates internal network traffic fees** when using internal endpoints
- Reduces total cost for large data transfers

Use internal endpoints for ECS-to-OSS communication within the same region.

## 7. Implement Timeout Retries for Latency-Sensitive Applications

OSS rate-limits management APIs (GetService/ListBuckets, PutBucket, GetBucketLifecycle, etc.). High request rates may trigger HTTP 503 responses.

**Key limits**:
- Single Alibaba Cloud account total QPS: **10,000**
- Per-partition limit applies even below total QPS threshold
- Contact technical support for higher QPS requirements

**Retry strategies**:
- For large requests (>128 MB): Measure throughput and retry the slowest 5%
- For small requests (<512 KB): Latency typically within tens of milliseconds; retry GET/PUT after 2 seconds
- Use exponential backoff: retry after 2s, then 4s, then exit
- For fixed-size requests: Identify and retry the slowest 1% of requests

## 8. Achieve High Throughput Through Horizontal Scaling and Parallel Requests

OSS is a massive distributed system. Leverage its scale by:

### Parallel Requests
- Launch multiple simultaneous request connections across multiple threads or instances
- Upload and download data in parallel
- Distribute load across multiple network paths

### Tuning Concurrency
1. Start with a single request
2. Measure current network bandwidth and resource usage
3. Identify bottleneck resources (highest utilization)
4. Calculate possible concurrent requests (e.g., if 1 request = 10% CPU, support up to 10 concurrent)

### Horizontal Connection Scaling
- Treat OSS as a large distributed system, not a single network endpoint
- Send multiple concurrent requests for best performance
- Distribute requests across different connections to maximize bandwidth
- **OSS has no connection limits per bucket**

### Increase Retry Counts
- Configure SDK timeout and retry values based on your application's fault tolerance requirements
- Consider increasing retries given OSS's large scale
