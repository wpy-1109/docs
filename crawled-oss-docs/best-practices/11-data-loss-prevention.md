# Data Loss Prevention Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/reduce-the-risks-of-data-loss-caused-by-accidental-operations

## Overview

Data loss in OSS can result from accidental deletion, overwriting, or unauthorized operations. This guide covers strategies to protect against data loss at multiple levels.

## 1. Enable Versioning

Versioning maintains a complete history of all object changes, allowing recovery from accidental deletions or overwrites.

### How It Works
- Every object PUT creates a new version
- Deleted objects are marked with a delete marker (not actually removed)
- Previous versions can be restored at any time

### Configuration
1. Navigate to **Bucket > Redundancy and Fault Tolerance > Versioning**
2. Enable versioning
3. Once enabled, versioning can be suspended but not disabled

### Version Cleanup
Use lifecycle rules to manage old versions:
```
After 90 days: Transition non-current versions to IA storage
After 365 days: Delete non-current versions
```

## 2. Cross-Region Replication (CRR)

Maintain a backup copy of your data in a different geographic region.

### Benefits
- Protection against regional outages or disasters
- Automatic, asynchronous replication of new and modified objects
- Supports same-account and cross-account replication

### Configuration Options
- **Full replication**: Replicate all objects
- **Prefix-based replication**: Only replicate objects matching specified prefixes
- **Replicate delete operations**: Optionally propagate deletions to target Bucket
- **Replicate historical data**: Optionally include existing objects

### Best Practice
- Do NOT enable delete operation replication for disaster recovery scenarios (prevents accidental cascade deletions)

## 3. Scheduled Backups with HBR

Use Hybrid Backup Recovery (HBR) for periodic backups:
- Schedule regular backup plans (daily, weekly)
- Set retention policies for backup data
- Test restore procedures periodically

## 4. WORM (Write Once Read Many) Policies

For compliance and regulatory requirements:
- Data becomes immutable once written
- Cannot be deleted or overwritten during the retention period
- Supports time-based retention policies
- Meets SEC Rule 17a-4, FINRA, CFTC compliance requirements

### Configuration
1. Navigate to **Bucket > Data Protection > Retention Policy**
2. Set retention period (1 day to 70 years)
3. Lock the policy to make it irreversible

**WARNING**: Once locked, a WORM policy cannot be shortened or removed. Data covered by the policy cannot be deleted until the retention period expires.

## 5. Prevent Accidental Overwrite

Enable the **Prevent Object Overwrite** feature:
- When enabled, PUT requests for existing objects are rejected
- Requires explicit action to update existing objects
- Use `x-oss-forbid-overwrite: true` header in API requests

## 6. Access Control Best Practices

### Principle of Least Privilege
- Grant only the minimum permissions required
- Use separate RAM users/roles for different applications
- Regularly audit and revoke unnecessary permissions

### Delete Protection
- Create RAM policies that explicitly deny `oss:DeleteObject` for critical buckets
- Require MFA for delete operations on sensitive data
- Use Bucket Policy conditions to restrict who can delete objects

```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "oss:DeleteObject",
                "oss:DeleteBucket"
            ],
            "Resource": [
                "acs:oss:*:*:critical-bucket",
                "acs:oss:*:*:critical-bucket/*"
            ]
        }
    ]
}
```

## 7. Monitoring and Alerting

Set up proactive monitoring:
- Alert on unusual delete operation volumes
- Monitor versioning status changes
- Track object count trends (sudden drops indicate potential issues)
- Alert on ACL or policy changes

## Recovery Procedures

### Restore a Deleted Object (with Versioning)
1. List object versions: `GET /?versions&prefix=<object-key>`
2. Identify the version to restore
3. Copy the version to create a new current version

### Restore from CRR Target
1. Access the target Bucket in the replication region
2. Copy required objects back to the source Bucket

### Restore from HBR Backup
1. Access HBR console
2. Select the backup plan and restore point
3. Initiate restore to the target Bucket

## Recommended Protection Layers

| Layer | Protection Against | Recovery Time |
|---|---|---|
| Versioning | Accidental delete/overwrite | Immediate |
| CRR | Regional failure | Minutes (RPO) |
| HBR Backup | Data corruption, ransomware | Hours |
| WORM | Unauthorized deletion | N/A (prevention) |
