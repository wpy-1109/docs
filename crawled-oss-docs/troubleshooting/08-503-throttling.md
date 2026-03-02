# Troubleshooting 503 Errors and Throttling

Source: https://help.aliyun.com/zh/oss/

## Overview

HTTP 503 (Service Unavailable) and throttling errors occur when request rates exceed OSS limits or when specific partitions are overloaded. This guide explains OSS rate limits, throttling mechanisms, and strategies to handle them.

## OSS Rate Limits

### Account-Level Limits
| Metric | Limit | Notes |
|---|---|---|
| Total QPS per account | 10,000 | Across all Buckets |
| Management API QPS | Lower limits | GetService, PutBucket, etc. |
| Single partition QPS | ~2,000 | Based on key prefix distribution |

### Partition-Level Behavior
- OSS automatically partitions data based on object key UTF-8 order
- Each partition has a throughput limit (~2,000 QPS)
- Sequential key prefixes may concentrate on a single partition
- OSS dynamically rebalances partitions based on load

## Common 503 Error Codes

### ServiceUnavailable
**Cause**: OSS service is temporarily unavailable.
**Solution**: Retry with exponential backoff.

### SlowDown
**Cause**: Request rate exceeds partition or account limits.
**Solution**:
1. Reduce request rate
2. Implement exponential backoff with jitter
3. Use random key prefixes to distribute load

### Reduce your request rate
**Cause**: Specific partition is overloaded due to hot keys.
**Solution**:
1. Randomize object key prefixes (hash prefix)
2. Distribute requests across multiple connections
3. Wait for automatic partition rebalancing

## Retry Strategy: Exponential Backoff with Jitter

```python
import time
import random

def retry_with_backoff(func, max_retries=5, base_delay=1.0):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            # Exponential backoff with full jitter
            delay = min(base_delay * (2 ** attempt), 30)  # Cap at 30 seconds
            jitter = random.uniform(0, delay)
            time.sleep(jitter)
```

```java
// Java retry with exponential backoff
int maxRetries = 5;
long baseDelay = 1000; // 1 second

for (int attempt = 0; attempt < maxRetries; attempt++) {
    try {
        // OSS operation
        break;
    } catch (OSSException e) {
        if (e.getErrorCode().equals("SlowDown") || e.getErrorCode().equals("ServiceUnavailable")) {
            if (attempt < maxRetries - 1) {
                long delay = Math.min(baseDelay * (long)Math.pow(2, attempt), 30000);
                long jitter = (long)(Math.random() * delay);
                Thread.sleep(jitter);
            } else {
                throw e;
            }
        } else {
            throw e;
        }
    }
}
```

## Strategies to Avoid Throttling

### 1. Randomize Key Prefixes

**Before** (hot partition):
```
logs/2024-01-01/event-001.json
logs/2024-01-01/event-002.json
logs/2024-01-01/event-003.json
```

**After** (distributed):
```
a3f2/logs/2024-01-01/event-001.json
7b1c/logs/2024-01-01/event-002.json
e9d4/logs/2024-01-01/event-003.json
```

### 2. Parallel Connections with Rate Control

```python
from concurrent.futures import ThreadPoolExecutor
import time

class RateLimitedUploader:
    def __init__(self, bucket, max_workers=10, rate_limit=1000):
        self.bucket = bucket
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        self.rate_limit = rate_limit  # requests per second
        self.interval = 1.0 / rate_limit

    def upload_file(self, key, data):
        time.sleep(self.interval)  # Simple rate limiting
        return self.bucket.put_object(key, data)

    def upload_batch(self, files):
        futures = []
        for key, data in files:
            future = self.executor.submit(self.upload_file, key, data)
            futures.append(future)
        return [f.result() for f in futures]
```

### 3. Pre-warm for Traffic Spikes

If you anticipate a sudden traffic increase:
1. Contact Alibaba Cloud support in advance
2. Request partition pre-splitting for expected key ranges
3. Gradually ramp up traffic over hours/days

### 4. Use Different Buckets for Different Access Patterns

Separate hot and cold data into different Buckets:
- Hot data Bucket: Optimized for high QPS
- Archive Bucket: Optimized for storage cost

## Monitoring Throttling

### CloudMonitor Alerts

Set up alerts for:
- **Server error rate** (5xx errors) > threshold
- **Throttling count** per minute
- **QPS approaching limit**

### OSS Logging

Enable access logging and analyze for throttling patterns:
```
# Look for 503 responses in access logs
grep "503" oss-access-log.txt | awk '{print $NF}' | sort | uniq -c | sort -rn
```

### Real-Time Throttling Monitoring

Use CloudMonitor to monitor OSS throttling information in real-time:
- View throttling events per Bucket
- Identify which operations are being throttled
- Correlate with request patterns

## When to Contact Support

- If you consistently need >10,000 QPS per account
- If you're experiencing throttling despite using random prefixes
- If you need guaranteed throughput for a specific time window
- Before planned large-scale migrations or events
