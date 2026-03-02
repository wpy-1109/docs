# Cost Optimization Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/cost-optimization

## Overview

When using OSS, you can reduce costs by planning storage types based on business data changes and leveraging prepaid vs. pay-as-you-go strategies.

**Note**: Pricing examples use rates published on July 30, 2024. Actual prices may vary; check the OSS pricing page for current rates.

## 1. Monitor Bucket Capacity Growth

Track storage costs by monitoring capacity growth:

- Use **CloudLens** to analyze Bucket usage patterns, tracking daily/weekly/monthly access trends
- Export CSV usage reports at the account level to review per-Bucket storage capacity
- If growth is abnormal, consider setting ACL to private and configuring Bucket Policy to prevent unauthorized uploads

## 2. Reduce Outbound Traffic and Data Retrieval Costs

If you authorize other users to access your Bucket data via public internet, enable **Requester Pays** mode so the requestor pays for:
- Outbound internet traffic
- Data retrieval costs for Infrequent Access storage

**Important**: Downstream traffic packages cannot offset outbound traffic costs generated under Requester Pays mode.

## 3. Configure Lifecycle Rules

### Storage Type Transitions Based on Access Frequency

| Storage Type | Use Case | Access Frequency |
|---|---|---|
| **Standard** | Hot data with frequent real-time access | Single file accessed >1 time/month |
| **Infrequent Access (IA)** | Warm data with lower access but real-time read needs | Single file accessed <1 time/month |
| **Archive** | Cold data for long-term storage, ~1 minute restore time | Single file accessed <1 time per 90 days |

Use Object prefixes or tags to filter specific data for lifecycle rules. Automatically migrate cold data to lower-cost archive storage while keeping hot data in Standard storage.

### Detailed Cost Example

**Scenario**: User A has 100 TB of business data (10 million Objects) stored as Standard (zone-redundant) in the cn-hangzhou region.

#### Phase 1: High-Frequency Access (Early Business)
All 100 TB accessed ~5 times/month.

| Storage Type | Data | Storage Cost | API Cost | Retrieval Cost | **Total/month** |
|---|---|---|---|---|---|
| Standard (ZRS) | 100 TB | 15,360 CNY | 30 CNY | 0 | **15,390 CNY** |
| IA (ZRS) | 100 TB | 10,240 CNY | 500 CNY | 16,640 CNY | **27,380 CNY** |

**Result**: Standard storage is more cost-effective for frequently accessed data.

#### Phase 2: 90% Data Access Decreases
90 TB accessed ~1 time/month; 10 TB remains highly accessed.

| Storage Type | Data | Storage Cost | API Cost | Retrieval Cost | **Total/month** |
|---|---|---|---|---|---|
| Standard (ZRS) | 10 TB | 1,536 CNY | 0 | 0 | 1,536 CNY |
| IA (ZRS) | 90 TB | 9,216 CNY | 90 CNY | 2,995.2 CNY | 12,301.2 CNY |
| **Combined** | 100 TB | | | | **13,837.2 CNY** |

**Result**: ~10.1% savings vs. keeping all data in Standard storage.

**Action**: Configure lifecycle rules to automatically transition files to IA 30 days after last access.

#### Phase 3: Mature Business, Quarterly Access
90 TB accessed ~1 time/quarter; 10 TB still frequently accessed.

| Storage Type | Data | Storage Cost | API Cost | Retrieval Cost | **Total/month** |
|---|---|---|---|---|---|
| Standard (ZRS) | 10 TB | 1,536 CNY | 0 | 0 | 1,536 CNY |
| Archive (ZRS) | 90 TB | 3,041.3 CNY | 30 CNY | 1,843 CNY | 4,914.3 CNY |
| **Combined** | 100 TB | | | | **6,450.3 CNY** |

**Result**: 53.4% additional savings vs. IA storage. Total 58% savings vs. all-Standard.

**Action**: Configure lifecycle rules:
- 30 days after last access: Standard -> IA
- 60 days after last access: IA -> Archive

### Clean Up Historical Version Objects

When versioning is enabled, overwrites and deletes are preserved as historical versions. Accumulated versions increase storage costs.

**Action**: Configure lifecycle rules to automatically delete Objects whose historical versions exceed a specified number of days (e.g., 200 days since last modification).

### Clean Up Expired Multipart Upload Fragments

Incomplete multipart uploads (Parts not merged via CompleteMultipartUpload) persist in the Bucket and incur storage fees.

**Action**: Configure lifecycle rules to automatically delete fragments older than a specified period (e.g., 2 days since creation).

## 4. Purchase Resource Packages

### Cost Comparison: Pay-As-You-Go vs. Resource Packages

**Scenario**: 100 TB of IA (zone-redundant) data, accessed once/month, 10 million objects.

#### Without Resource Packages

| Item | Cost |
|---|---|
| Storage (0.10 CNY/GB/month) | 10,240 CNY |
| Outbound traffic (0.50 CNY/GB peak hours) | 51,200 CNY |
| Data retrieval (0.0325 CNY/GB) | 3,328 CNY |
| **Total** | **64,768 CNY** |

#### With Resource Packages

| Item | Cost |
|---|---|
| IA-ZRS Storage Package (100 TB, 1 month) | 9,216 CNY |
| Downstream Traffic Package (100 TB) | 43,008 CNY |
| Data retrieval (pay-as-you-go only) | 3,328 CNY |
| **Total** | **55,552 CNY** |

**Result**: Resource packages save approximately **14%** compared to pure pay-as-you-go.

## 5. Additional Cost Optimization Strategies

- **Use internal endpoints**: Access OSS from ECS in the same region via internal endpoints (free traffic)
- **Enable CDN acceleration**: Reduce direct OSS outbound traffic costs
- **Enable Gzip compression**: Reduce transfer data volume
- **Use Storage Capacity Units (SCU)**: Available since 2024, can offset multiple storage product costs
- **Intelligent Tiering**: Automatically moves objects between access tiers based on access patterns
- **Delete unnecessary data**: Regular audits with OSS Inventory to identify and remove unused objects
