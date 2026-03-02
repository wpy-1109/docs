# API Operation Calling Fees

> Source: https://www.alibabacloud.com/help/en/oss/product-overview/api-operation-calling-fees

## Overview

OSS charges fees based on the number of API requests made to your buckets. Fees are calculated per 10,000 requests and vary by request type.

## Request Categories

### Write Requests (PUT/POST/COPY)

Charged per 10,000 requests. Includes:

- PutObject
- PostObject
- CopyObject
- AppendObject
- InitiateMultipartUpload
- UploadPart
- CompleteMultipartUpload
- PutBucketLifecycle
- PutBucketACL
- PutBucketPolicy
- PutBucketWebsite
- PutBucketLogging
- PutBucketNotification
- PutBucketReplication
- Other PUT/POST operations

### Read Requests (GET/HEAD)

Charged per 10,000 requests. Includes:

- GetObject
- HeadObject
- GetBucketInfo
- GetBucketACL
- ListObjects (ListObjectsV2)
- ListBuckets
- GetBucketLocation
- GetBucketLifecycle
- Other GET/HEAD operations

### Free Requests

- DeleteObject
- DeleteObjects (batch delete)
- AbortMultipartUpload

## Data Retrieval Requests

In addition to standard API request fees, accessing data in non-Standard storage classes incurs data retrieval fees:

| Storage Class | Retrieval Fee Basis |
|--------------|-------------------|
| **Infrequent Access (IA)** | Per GB of data retrieved |
| **Archive** | Per GB of data restored |
| **Cold Archive** | Per GB of data restored (varies by priority) |
| **Deep Cold Archive** | Per GB of data restored (varies by priority) |

## Billing Calculation

```
Request Fee = (Number of Requests / 10,000) × Unit Price per 10,000 Requests
```

## Cost Optimization

1. **Batch operations**: Use batch delete instead of individual deletes
2. **List wisely**: Use pagination with appropriate max-keys to reduce listing requests
3. **Cache responses**: Implement client-side caching to reduce repeated GET requests
4. **Use conditional requests**: Use If-Modified-Since, If-None-Match headers
5. **Lifecycle rules**: Automate object management to reduce manual API calls
6. **Request packages**: Purchase prepaid request packages for predictable workloads
