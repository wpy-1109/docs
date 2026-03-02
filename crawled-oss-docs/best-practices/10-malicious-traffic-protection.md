# Malicious Traffic Protection Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/reduce-the-risks-of-unexpectedly-high-fees-caused-by-malicious-access-traffic

## Overview

If your OSS resources are targeted by malicious traffic attacks, you may incur unexpectedly high outbound traffic charges. This guide provides comprehensive strategies to protect against traffic abuse and control costs.

## Risk Scenarios

- **Hotlinking**: Other websites embedding your OSS resources (images, videos) directly
- **DDoS attacks**: Distributed denial-of-service attacks generating massive traffic
- **Crawler abuse**: Automated bots excessively downloading your content
- **Leaked URLs**: Signed URLs being shared beyond intended recipients

## Protection Strategies

### 1. Configure Referer Whitelisting (Anti-Hotlinking)

Restrict OSS access to requests from authorized domains only.

**Configuration**:
- Navigate to **Bucket > Permission Control > Anti-Hotlinking**
- Set **Referer Whitelist** with your authorized domains
- Optionally deny requests with empty Referer headers

**Example whitelist**:
```
https://www.example.com
https://*.example.com
```

**Limitations**: Referer headers can be spoofed. Use in combination with other measures.

### 2. Enable Requester Pays Mode

When data consumers should bear the traffic costs:
- Enable **Requester Pays** on the Bucket
- Requestors must include `x-oss-request-payer: requester` in their requests
- Bucket owner is not charged for outbound traffic from authenticated requests

### 3. Set Up CDN with URL Authentication

- Front your OSS Bucket with CDN
- Enable **URL Authentication** on CDN to generate time-limited signed URLs
- Configure CDN-level Referer restrictions
- Set bandwidth caps on CDN domain

### 4. Configure Bandwidth Throttling

Limit the maximum bandwidth for individual connections:
- Use **Single Connection Bandwidth Throttling** to cap per-request bandwidth
- Prevents any single client from consuming all available bandwidth

**API parameter**: `x-oss-traffic-limit`
- Value range: 819200 (100 KB/s) to 838860800 (100 MB/s)
- Unit: bit/s

### 5. Set Up CloudMonitor Alerts

Configure real-time monitoring and alerts for abnormal traffic patterns:

**Recommended alert rules**:
- Outbound traffic exceeds N GB in 1 hour
- Request count exceeds N per minute
- 4xx/5xx error rate exceeds threshold
- Bandwidth utilization exceeds threshold

### 6. Use CloudMonitor for OSS Throttling Monitoring

Monitor OSS throttling information in real-time to detect when your bucket is being rate-limited, which often indicates abnormal traffic patterns.

### 7. Use SLS Alerts to Protect OSS Resources

Configure alerts in Simple Log Service (SLS) based on OSS access logs:
- Detect unusual access patterns (geographic anomalies, time-of-day anomalies)
- Alert on sudden spikes in specific object access
- Track and alert on high-frequency 403 errors (potential attack indicators)

### 8. Configure Bucket Policy IP Restrictions

For known client IP ranges, restrict access at the Bucket Policy level:

```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "oss:*",
            "Resource": "acs:oss:*:*:examplebucket/*",
            "Condition": {
                "NotIpAddress": {
                    "acs:SourceIp": [
                        "192.168.1.0/24",
                        "10.0.0.0/8"
                    ]
                }
            }
        }
    ]
}
```

### 9. Block Public Access

For Buckets that should only be accessed by authorized services:
- Enable **Block Public Access** to prevent accidental public exposure
- Use VPC endpoints for internal service access

### 10. Set Budget Alerts

Configure cost alerts in the Alibaba Cloud Billing console:
- Set daily/monthly spending thresholds
- Receive notifications before costs exceed budgets
- Consider enabling spending caps if available

## Emergency Response Plan

If you detect a malicious traffic attack:

1. **Immediately** set Bucket ACL to **private** if currently public
2. Enable **Block Public Access**
3. Review and restrict Bucket Policy
4. Check for leaked AccessKeys and rotate if necessary
5. Enable **Requester Pays** if appropriate
6. Contact Alibaba Cloud support for DDoS protection
7. Review access logs to identify attack patterns
8. Consider enabling Anti-DDoS service for severe cases

## Cost Impact Examples

| Scenario | Potential Daily Cost Impact |
|---|---|
| 1 TB outbound via public internet | ~500 CNY (peak hours) |
| 10 TB outbound via public internet | ~5,000 CNY |
| 100 TB outbound via public internet | ~50,000 CNY |

These costs highlight the importance of proactive protection measures.
