# Data Migration Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/data-migration-overview

## Overview

Business data scattered across on-premises data centers, third-party cloud storage, or different regions/accounts of Alibaba Cloud OSS leads to complex operations and high costs. Alibaba Cloud provides Online Migration Service, CLI tools, and Offline Migration (Lightning Cube) to meet various migration scenarios.

## Migration Between Alibaba Cloud OSS Buckets

### Same-Region Migration

| Scenario | Recommended Tool | Details |
|---|---|---|
| Small to medium data, same account | **ossutil** `cp` command | Supports batch copy and resumable transfer |
| Large-scale or cross-account | **Same-Region Replication** | Automatic sync on add/modify/delete, no intermediate download needed |

### Cross-Region Migration

For Buckets in different regions (e.g., cn-hangzhou to cn-beijing):
- Use **Cross-Region Replication (CRR)**
- Leverages Alibaba Cloud internal network for secure transfer
- Automatic sync on source data changes
- Suitable for multi-site collaboration and real-time backup

## Third-Party Cloud Storage to OSS

Use **Alibaba Cloud Online Migration Service** for data from:
- AWS S3
- Tencent Cloud COS
- Huawei Cloud OBS
- ByteDance/Volcengine TOS
- Google Cloud GCS
- Microsoft Azure Blob
- Any S3-compatible object storage

**Benefits**: No migration environment setup required. Submit tasks online and monitor progress in real-time.

## Local File System to OSS

### Small-Scale (<5 GB)
Use **OSS Console** for direct upload. Simple, no extra tools needed. Suitable for ad-hoc uploads and test data.

### Medium-Scale
Two options:
1. **ossutil** `cp` command: Batch upload with resumable transfer and concurrency acceleration
2. **Online Migration Service** (LocalFS to OSS): Managed solution with centralized task management and monitoring

### Large-Scale (TB to PB)
Two options:
1. **Online Migration Service**: No environment setup, real-time monitoring, suitable for public network transfer
2. **Offline Migration (Lightning Cube)**: Physical media transfer for:
   - Data center migrations
   - Large enterprise archive files
   - Historical media assets
   - When public bandwidth is insufficient

## HTTP/HTTPS Source to OSS

Use **Online Migration Service** to migrate data from HTTP/HTTPS sources efficiently without additional environment setup.

## Big Data Storage to OSS

### HDFS Data to OSS
Use **Jindo DistCp** (MapReduce-based distributed file copy tool):
- Parallel task distribution across clusters
- Supports fault tolerance, resumable transfer, exception recovery
- Handles TB to PB scale migrations
- Suitable for data lake construction and big data computing

### OSS External Tables (gpossext) to OSS
Use **AnalyticDB PostgreSQL** for parallel import/export:
- High concurrency and throughput
- Suitable for large-scale data analysis, historical data archiving, cross-system data exchange

## Big Data Storage to OSS-HDFS

OSS-HDFS (JindoFS) is a cloud-native data lake storage product that provides HDFS-compatible interfaces with full POSIX support.

### HDFS Data to OSS-HDFS
Use **Jindo DistCp** with automatic error detection, retry, and task recovery.

### Between OSS-HDFS Buckets
Use **Jindo DistCp** for data partition adjustment, storage optimization, or cross-region scheduling.

### Semi-Managed JindoFS Cluster to OSS-HDFS
Use **JindoDistJob** tool for full and incremental migration with zero-downtime switching.

### Hive Tables and Partitions to OSS-HDFS
Use **JindoTable MoveTo** command:
- Automatically updates metadata after data copy
- Supports conditional filtering
- Batch partition migration
- Multiple data verification mechanisms

## Zero-Downtime Migration with Mirror Back-to-Origin

**Recommended approach**: First determine migration method, then configure mirror back-to-origin for business continuity.

### How It Works
1. Complete historical data migration
2. Switch business entry point to OSS
3. Mirror back-to-origin automatically fetches any un-migrated data when accessed
4. Data gradually backfilled until full migration is complete

### Use Case
A business originally deployed on another cloud platform needs to migrate to OSS without stopping online services. Configure mirror back-to-origin rules to automatically fetch and sync un-migrated data during the transition period.

## Migration Planning Checklist

- [ ] Assess data volume and choose appropriate migration method
- [ ] Identify source storage type (cloud, on-premises, HDFS, etc.)
- [ ] Plan for cross-region vs. same-region migration
- [ ] Consider bandwidth limitations and timeline requirements
- [ ] Configure mirror back-to-origin if zero-downtime is required
- [ ] Verify data integrity after migration
- [ ] Update application endpoints to use new OSS Bucket
