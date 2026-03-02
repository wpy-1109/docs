# Cross-Region Replication (CRR)

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication

## Overview

Cross-region replication (CRR) enables automatic, asynchronous copying of objects across OSS buckets in different Alibaba Cloud regions. This provides geographic redundancy for disaster recovery and data locality for global applications.

## Prerequisites

- Source and destination buckets must both be in the same versioning state (both non-versioned, or both versioned)
- Source and destination buckets must be in different regions (cross-region)
- Both buckets can belong to the same or different Alibaba Cloud accounts (cross-account CRR is supported)
- Both buckets must not already have conflicting CRR rules

## Configuration via OSS Console

1. Log in to the [OSS Console](https://oss.console.aliyun.com/)
2. Select the **source bucket**
3. Navigate to **Data Management** > **Cross-Region Replication**
4. Click **Enable Cross-Region Replication**
5. Configure the rule:

| Setting | Description |
|---------|-------------|
| **Source Region** | Auto-populated based on the source bucket |
| **Destination Region** | Select the target region |
| **Destination Bucket** | Choose or create the destination bucket |
| **Replication Scope** | Entire Bucket or Objects with Specified Prefix |
| **Replicate Historical Data** | Choose whether to replicate existing objects |
| **Replication Policy** | Added/Changed only, or Added/Changed/Deleted |
| **KMS-based Encryption** | Optionally enable for encrypted object replication |
| **Transfer Acceleration** | Enable for faster cross-region transfer |

6. Click **OK** to save

## Configuration via API

### PutBucketReplication (XML)

```xml
PUT /?replication HTTP/1.1
Host: source-bucket.oss-cn-hangzhou.aliyuncs.com

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

## Configuration via SDK (Java)

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.*;

public class CRRConfig {
    public static void main(String[] args) {
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        String accessKeyId = "<yourAccessKeyId>";
        String accessKeySecret = "<yourAccessKeySecret>";
        String sourceBucket = "source-bucket";
        String targetBucket = "destination-bucket";
        String targetRegion = "oss-cn-beijing";

        OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

        AddBucketReplicationRequest request = new AddBucketReplicationRequest(sourceBucket);
        request.setTargetBucketName(targetBucket);
        request.setTargetBucketLocation(targetRegion);
        request.setReplicationRuleID("rule1");
        request.setEnableHistoricalObjectReplication(true);

        ossClient.addBucketReplication(request);
        System.out.println("CRR rule configured successfully.");

        ossClient.shutdown();
    }
}
```

## Configuration via ossutil CLI

```bash
ossutil replication --method put \
  oss://source-bucket \
  --target-bucket oss://destination-bucket \
  --target-location oss-cn-beijing \
  --enable-historical-object-replication true
```

## Key Configuration Options

| Option | Description |
|--------|-------------|
| **Replication Scope** | Entire bucket or prefix-based |
| **Historical Data** | Enable/disable replication of existing objects |
| **Delete Sync** | Replicate delete operations (optional) |
| **KMS Encryption** | Support replication of KMS-encrypted objects |
| **Transfer Acceleration** | Speed up cross-region data transfer |
| **RTC (Replication Time Control)** | Guarantee replication within a specific time (if available) |

## Important Notes

- **One-way replication**: CRR is unidirectional (source to destination)
- **No cascading**: If Bucket A replicates to Bucket B, objects replicated into B will not be further replicated to Bucket C
- **Costs**: Data transfer fees and request fees apply for CRR
- **Eventual consistency**: Replication is asynchronous
- **Versioning**: Both buckets must be in the same versioning state
