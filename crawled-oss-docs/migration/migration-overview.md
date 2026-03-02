# Migration Overview - Migrate Data to Alibaba Cloud OSS

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/migrate-data-from-amazon-s3-to-alibaba-cloud-oss

## Overview

Alibaba Cloud provides multiple methods for migrating data to OSS from various sources, including Amazon S3, other cloud providers, on-premises systems, and between OSS buckets.

## Migration Methods

### 1. Data Online Migration (Recommended)

Data Online Migration is Alibaba Cloud's fully managed, serverless online migration service. It is the recommended method for migrating data from third-party cloud storage to OSS.

**Key Features:**
- No infrastructure setup required
- Supports scheduled and incremental migrations
- Built-in monitoring and logging
- Handles large-scale data transfers efficiently
- Automatic bandwidth throttling
- Verification and retry mechanisms

**Supported Sources:**
- Amazon S3
- Azure Blob Storage
- Google Cloud Storage
- Other HTTP/HTTPS sources
- OSS (cross-region or cross-account)

**Steps:**
1. Create an Alibaba Cloud RAM user with OSS permissions
2. Obtain your source credentials (e.g., AWS Access Key ID and Secret Access Key)
3. Configure a migration job in the Alibaba Cloud Data Online Migration console
4. Specify the source (e.g., S3 bucket) and destination (OSS bucket)
5. Start the migration and monitor progress

### 2. OSSImport (Legacy/Self-Managed Tool)

OSSImport is a standalone tool for migrating data to OSS from various sources.

**Two Deployment Modes:**

| Mode | Use Case | Data Scale |
|------|----------|------------|
| **Standalone** | Small-scale migrations, simple setup | Less than 30 TB |
| **Distributed** | Large-scale migrations, parallel processing | More than 30 TB |

**Key Features:**
- Resumable transfers - can resume interrupted migrations
- Incremental migration - supports syncing only new/changed files
- Traffic control - allows bandwidth throttling
- Data verification - checks data integrity after migration
- Flexible filtering - supports prefix-based filtering of objects
- Detailed logging for monitoring and troubleshooting

**Workflow:**
1. Download the ossimport package
2. Configure `local_job.cfg` (standalone) or `job.cfg` (distributed) with source/destination details
3. Start the migration using the provided scripts
4. Monitor progress via logs or the console

### 3. Cross-Region Replication (CRR) - OSS to OSS

For ongoing replication between OSS buckets in different regions.

**Key Features:**
- One-way, asynchronous replication from source to destination
- Supports replicating all objects or objects with specific prefixes
- Option to replicate historical data
- Option to replicate delete operations
- Supports KMS-encrypted object replication
- Transfer acceleration support

**Configuration via Console:**
1. Select the source bucket
2. Navigate to **Data Management** > **Cross-Region Replication**
3. Click **Enable Cross-Region Replication**
4. Configure the rule (destination region/bucket, scope, policies)
5. Click OK to save

**Configuration via API (XML):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ReplicationConfiguration>
  <Rule>
    <Destination>
      <Bucket>destination-bucket</Bucket>
      <Location>oss-cn-beijing</Location>
    </Destination>
    <HistoricalObjectReplication>enabled</HistoricalObjectReplication>
    <PrefixSet>
      <Prefix>logs/</Prefix>
    </PrefixSet>
  </Rule>
</ReplicationConfiguration>
```

**Configuration via SDK (Java):**
```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.*;

OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

AddBucketReplicationRequest request = new AddBucketReplicationRequest(sourceBucket);
request.setTargetBucketName(targetBucket);
request.setTargetBucketLocation(targetRegion);
request.setReplicationRuleID("rule1");
request.setEnableHistoricalObjectReplication(true);

ossClient.addBucketReplication(request);
ossClient.shutdown();
```

### 4. S3 API Compatibility

OSS is compatible with many Amazon S3 APIs, allowing existing S3-based applications to work with OSS with minimal changes. Simply swap endpoints and credentials for minimal code changes.

## Choosing the Right Migration Method

| Factor | Data Online Migration | OSSImport | CRR |
|--------|----------------------|-----------|-----|
| **Management** | Fully managed (cloud) | Self-managed | Fully managed |
| **Scalability** | Automatic | Manual (distributed mode) | Automatic |
| **Best For** | Most migration scenarios | Custom/complex requirements | Ongoing OSS-to-OSS sync |
| **Setup** | Minimal | Requires deployment | Minimal |
| **Source** | Multi-cloud | Multi-source | OSS only |
| **Status** | Actively recommended | Legacy tool | Actively supported |

## Key Considerations

- **Network latency and costs**: Cross-region transfers incur egress charges on the source cloud and potentially ingress processing on Alibaba Cloud
- **Data consistency**: Use incremental sync to catch changes during migration
- **IAM credentials**: You need source credentials with appropriate read permissions
- **Endpoint configuration**: Specify the correct source region endpoint and OSS region endpoint
- **Verification**: Always verify data integrity after migration completes
