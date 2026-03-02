# Backup and Disaster Recovery Best Practices

Source: https://help.aliyun.com/zh/oss/use-cases/back-up-buckets

## Overview

Alibaba Cloud OSS provides multiple mechanisms for data backup and disaster recovery, ensuring business continuity and data integrity across various failure scenarios.

## Backup Strategies

### 1. Cross-Region Replication (CRR)

The primary disaster recovery mechanism for OSS data.

**Features**:
- Automatic, asynchronous replication of objects to a target Bucket in a different region
- Support for same-account and cross-account replication
- Configurable scope: entire Bucket or prefix-based
- Optional replication of delete operations, historical data, and KMS-encrypted objects

**Configuration**:
1. Navigate to **Bucket > Redundancy and Fault Tolerance > Cross-Region Replication**
2. Select target region and Bucket
3. Choose replication scope and options
4. Specify IAM role for replication

**RPO (Recovery Point Objective)**: Minutes (depends on object size and replication lag)

### 2. Zone-Redundant Storage (ZRS)

Data is automatically stored across three availability zones within a region.

**Benefits**:
- Survives single AZ failures
- 99.9999999999% (12 nines) data durability
- No additional configuration needed (selected at Bucket creation)
- Automatic failover, transparent to applications

**Available for**: Standard, IA storage classes

### 3. Hybrid Backup Recovery (HBR)

Scheduled backup service for OSS data.

**Features**:
- Create backup plans with customizable schedules
- Define retention policies (keep last N backups, keep for N days)
- Support incremental backups
- Cross-region backup storage
- Backup verification and restore testing

**Configuration**:
1. Navigate to **Bucket > Data Protection > Scheduled Backup**
2. Create a backup plan
3. Set schedule (hourly, daily, weekly)
4. Configure retention policy

### 4. Versioning

Maintains all historical versions of every object.

**Use for**:
- Protection against accidental overwrites and deletes
- Point-in-time recovery
- Audit trail of all object modifications

## Disaster Recovery Architecture

### Active-Passive (Recommended for most scenarios)

```
Primary Region (cn-hangzhou)          DR Region (cn-beijing)
┌─────────────────────┐              ┌─────────────────────┐
│  Primary Bucket     │  ──CRR──>    │  DR Bucket          │
│  (Read/Write)       │              │  (Read-only backup) │
└─────────────────────┘              └─────────────────────┘
         |                                     |
    Application                          Failover only
```

### Active-Active (For global distribution)

```
Region A (cn-hangzhou)                Region B (us-west-1)
┌─────────────────────┐              ┌─────────────────────┐
│  Bucket A           │  <──CRR──>   │  Bucket B           │
│  (Read/Write)       │              │  (Read/Write)       │
└─────────────────────┘              └─────────────────────┘
         |                                     |
  Asia Users                           US Users
```

**Note**: Active-Active requires bidirectional CRR and careful conflict resolution for concurrent writes to the same object.

## Recovery Procedures

### Failover to DR Region

1. Update application configuration to use DR Bucket endpoint
2. Update DNS or load balancer to point to DR region
3. Verify data integrity in DR Bucket
4. Resume operations

### Restore from HBR Backup

1. Open HBR Console
2. Select backup plan and restore point
3. Choose target Bucket (same or different)
4. Start restore job
5. Monitor restore progress

### Restore Deleted Object (Versioning)

1. List versions: `ListObjectVersions`
2. Find the version before deletion
3. Copy the version: `CopyObject` with `x-oss-copy-source` specifying the version ID

## RTO and RPO Guidelines

| Strategy | RPO | RTO | Cost |
|---|---|---|---|
| Zone-Redundant Storage | 0 | 0 (automatic) | Included in ZRS pricing |
| Cross-Region Replication | Minutes | Minutes-Hours | CRR traffic + target storage |
| HBR Scheduled Backup | Hours-Days | Hours | HBR + storage costs |
| Versioning | 0 (per operation) | Minutes | Additional version storage |

## Best Practices Checklist

- [ ] Enable Zone-Redundant Storage for critical Buckets
- [ ] Configure Cross-Region Replication for disaster recovery
- [ ] Set up HBR scheduled backups for compliance
- [ ] Enable versioning for protection against accidental operations
- [ ] Do NOT replicate delete operations to DR Buckets
- [ ] Regularly test restore procedures
- [ ] Document and maintain a disaster recovery runbook
- [ ] Set up monitoring and alerts for replication lag
- [ ] Use lifecycle rules to manage backup retention and costs
