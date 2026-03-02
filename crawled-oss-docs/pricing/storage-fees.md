# Storage Fees

> Source: https://www.alibabacloud.com/help/en/oss/product-overview/storage-fees

## Overview

Storage fees are charged based on the storage class and the volume of data stored in your OSS buckets. OSS offers multiple storage classes to help you optimize costs based on data access patterns.

## Storage Classes and Pricing Tiers

### Standard Storage

- **Use case**: Frequently accessed data, active content
- **Durability**: 99.9999999999% (12 nines, ZRS)
- **Availability**: 99.99% (ZRS) / 99.9% (LRS)
- **Redundancy options**: Locally Redundant Storage (LRS) or Zone-Redundant Storage (ZRS)
- **No minimum storage duration**
- **No minimum billable object size**
- **No data retrieval fee**

### Infrequent Access (IA) Storage

- **Use case**: Data accessed less than once per month
- **Minimum storage duration**: 30 days
- **Minimum billable object size**: 64 KB
- **Data retrieval fee**: Yes, per GB retrieved
- **Cost savings**: Significant discount compared to Standard

### Archive Storage

- **Use case**: Long-term archival data, accessed rarely
- **Minimum storage duration**: 60 days
- **Minimum billable object size**: 64 KB
- **Data retrieval**: Requires restore operation (minutes to hours)
- **Cost savings**: Much lower than Standard and IA

### Cold Archive Storage

- **Use case**: Compliance, backup, very rarely accessed data
- **Minimum storage duration**: 180 days
- **Minimum billable object size**: 64 KB
- **Data retrieval**: Requires restore operation (hours)
- **Three restore priorities**: Expedited (1 hour), Standard (2-5 hours), Bulk (5-12 hours)

### Deep Cold Archive Storage

- **Use case**: Ultra-long-term retention, almost never accessed
- **Minimum storage duration**: 180 days
- **Minimum billable object size**: 64 KB
- **Data retrieval**: Requires restore operation (up to 12+ hours)
- **Two restore priorities**: Standard (up to 12 hours), Bulk (up to 48 hours)
- **Lowest storage cost** of all classes

## Early Deletion Fees

For IA, Archive, Cold Archive, and Deep Cold Archive classes:
- If objects are deleted, overwritten, or transitioned to another storage class **before** the minimum storage duration expires, you are still charged storage fees for the remainder of the minimum storage period.

## Small Object Fees

For IA, Archive, Cold Archive, and Deep Cold Archive classes:
- Objects smaller than 64 KB are billed as if they are 64 KB.
- Consider combining small objects or keeping them in Standard storage.

## Billing Calculation

Storage fees are typically calculated as:

```
Daily Storage Fee = Storage Volume (GB) × Unit Price per GB per Day
Monthly Storage Fee = Average Daily Storage Volume (GB) × Unit Price per GB per Month
```

The storage volume is sampled at regular intervals and averaged over the billing period.

## Cost Optimization

1. **Lifecycle rules**: Automatically transition objects to cheaper tiers based on age
2. **Delete unnecessary data**: Remove objects no longer needed
3. **Combine small objects**: Avoid small object overhead in non-Standard classes
4. **Resource plans**: Purchase prepaid storage for predictable workloads
5. **Monitor storage metrics**: Use the OSS console to track storage growth
