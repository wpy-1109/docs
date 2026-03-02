# Billing Overview

> Source: https://www.alibabacloud.com/help/en/oss/product-overview/billing-overview

## Overview

Alibaba Cloud Object Storage Service (OSS) charges are based on several dimensions including storage, data transfer, API requests, and additional features. This page provides a comprehensive overview of all billing items.

## Billing Methods

### 1. Pay-As-You-Go (PAYG)

- **Default billing method**
- Billed hourly or daily based on actual usage
- No upfront commitment
- Best for unpredictable or variable workloads, short-term projects, testing/development

### 2. Subscription / Resource Plans (Prepaid)

- Purchase storage capacity and/or data transfer in advance at a discounted rate
- Significant discounts compared to PAYG (often 15-40%+ savings)
- Available in monthly, semi-annual, or annual subscriptions
- Resource plans can cover: storage capacity, downstream data transfer, API request packages
- Any usage exceeding the plan is billed at PAYG rates
- Best for predictable, steady-state workloads

### 3. Storage Capacity Units (SCUs)

- Deductible plans that can be applied across multiple storage products
- Provides flexibility across storage services

## Billing Items

### Storage Fees

Charged based on the storage class and the volume of data stored:

| Storage Class | Use Case | Relative Cost | Min Billable Size | Min Storage Duration |
|--------------|----------|---------------|-------------------|---------------------|
| **Standard (LRS)** | Frequently accessed data | Highest | None | None |
| **Standard (ZRS)** | Frequently accessed, zone-redundant | Higher | None | None |
| **Infrequent Access (IA)** | Data accessed less than once/month | Lower | 64 KB | 30 days |
| **Archive** | Long-term archival, rare access | Much lower | 64 KB | 60 days |
| **Cold Archive** | Compliance/backup, very rare access | Very low | 64 KB | 180 days |
| **Deep Cold Archive** | Ultra-long-term retention | Lowest | 64 KB | 180 days |

> **Note:** For IA, Archive, Cold Archive, and Deep Cold Archive classes, objects deleted or overwritten before the minimum storage duration still incur charges for the full minimum period.

### Traffic / Data Transfer Fees

| Traffic Type | Charged? | Notes |
|-------------|----------|-------|
| **Inbound traffic (upload)** | Free | |
| **Intranet traffic (same region)** | Free | |
| **Outbound traffic over the Internet** | Charged per GB | Main cost driver for many workloads |
| **CDN back-to-origin traffic** | Charged (lower rate) | Lower than direct Internet outbound |
| **Cross-region replication traffic** | Charged per GB | |
| **Transfer acceleration** | Charged (premium rate) | For accelerated uploads/downloads |

### API Request Fees

| API Call Type | Description |
|--------------|-------------|
| **PUT/POST/COPY requests** | Charged per 10,000 requests (write-class operations) |
| **GET/HEAD requests** | Charged per 10,000 requests (read-class operations) |
| **DELETE requests** | Free |

### Data Retrieval Fees

Applicable to IA, Archive, Cold Archive, and Deep Cold Archive storage classes:

| Storage Class | Retrieval Speed | Approximate Restore Time |
|--------------|----------------|-------------------------|
| **Infrequent Access** | Immediate | Instant |
| **Archive** | Expedited / Standard | Minutes to hours |
| **Cold Archive** | Expedited / Standard / Bulk | 1-12 hours |
| **Deep Cold Archive** | Standard / Bulk | Up to 12+ hours |

### Additional Fees

| Fee Type | Description |
|----------|-------------|
| **Data processing (IMG)** | Image Processing operations |
| **Object tagging** | Per 10,000 tags/month |
| **Transfer acceleration** | Premium for accelerated uploads/downloads |
| **Temporary storage** | For multipart uploads not completed |

## Regional Pricing Variations

OSS pricing differs by region:

| Region Group | Relative Pricing |
|-------------|-----------------|
| **Mainland China** (Hangzhou, Shanghai, Beijing, Shenzhen) | Generally lowest |
| **Hong Kong (China)** | Between mainland and international |
| **International** (Singapore, US, Frankfurt, Sydney, Mumbai, Dubai, Tokyo, London) | Typically slightly higher |

> Data transfer fees also vary by region and traffic type.

## Cost Optimization Tips

1. **Use lifecycle rules** to automatically transition objects to cheaper storage classes
2. **Purchase resource plans** for predictable workloads to save 20-40%
3. **Enable CDN** to reduce outbound traffic costs
4. **Choose the right storage class** based on access patterns
5. **Monitor usage** via the Alibaba Cloud console billing dashboard
6. **Clean up multipart uploads** that are no longer needed
7. **Use object tagging** wisely to avoid unnecessary tag fees

## References

- Pricing Page: https://www.alibabacloud.com/product/oss/pricing
- Storage Fees: https://www.alibabacloud.com/help/en/oss/product-overview/storage-fees
- Traffic Fees: https://www.alibabacloud.com/help/en/oss/product-overview/traffic-fees
- API Request Fees: https://www.alibabacloud.com/help/en/oss/product-overview/api-operation-calling-fees
