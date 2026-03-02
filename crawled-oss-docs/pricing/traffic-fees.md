# Traffic Fees

> Source: https://www.alibabacloud.com/help/en/oss/product-overview/traffic-fees

## Overview

Traffic fees are based on the type and volume of data transferred to and from your OSS buckets. Understanding traffic fee categories helps you optimize costs.

## Traffic Categories

### Free Traffic

| Traffic Type | Description |
|-------------|-------------|
| **Inbound (Upload)** | All data uploaded to OSS is free, regardless of method |
| **Intranet (Same Region)** | Traffic between OSS and other Alibaba Cloud services in the same region via internal endpoints |

### Charged Traffic

| Traffic Type | Rate Level | Description |
|-------------|-----------|-------------|
| **Internet Outbound** | Standard | Data downloaded from OSS directly over the internet |
| **CDN Back-to-Origin** | Lower than Internet | Traffic from OSS to Alibaba Cloud CDN edge nodes |
| **Cross-Region Replication** | Standard | Data transferred between OSS buckets in different regions |
| **Transfer Acceleration (Upload)** | Premium | Accelerated uploads using transfer acceleration |
| **Transfer Acceleration (Download)** | Premium | Accelerated downloads using transfer acceleration |

## Traffic Billing Details

### Internet Outbound Traffic

- Charged per GB based on tiered pricing
- Higher volume typically results in lower per-GB pricing
- Pricing varies by region
- This is typically the largest traffic cost for most applications

### CDN Back-to-Origin Traffic

- When using Alibaba Cloud CDN with OSS as origin
- Charged at a lower rate than direct Internet outbound
- CDN caching reduces back-to-origin requests, further saving costs
- Recommended for serving static content to end users

### Cross-Region Replication Traffic

- Incurred when using Cross-Region Replication (CRR)
- Charged based on the volume of data replicated
- Applies to both initial historical data replication and ongoing replication

### Transfer Acceleration Traffic

- Premium-priced traffic for using OSS Transfer Acceleration
- Provides accelerated data transfer over optimized network paths
- Separate pricing for upload and download acceleration
- Best for cross-region or cross-border large file transfers

## Cost Optimization

1. **Use CDN**: Distribute content via CDN to reduce direct Internet outbound costs
2. **Use internal endpoints**: Access OSS from same-region services via intranet (free)
3. **Monitor traffic patterns**: Identify unexpected spikes in traffic
4. **Purchase traffic resource plans**: Prepaid packages offer significant discounts
5. **Compress data**: Reduce file sizes before storage and transfer
6. **Cache effectively**: Implement client-side and CDN caching strategies
7. **Restrict access**: Use referer restrictions and bucket policies to prevent unauthorized access
