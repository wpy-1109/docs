# OSS Best Practices

> Source: Alibaba Cloud OSS Documentation - Best Practices

## Data Migration

### Migration Tools & Methods

| Tool | Use Case | Scale |
|------|----------|-------|
| **OSS Migration Service** | On-premises to OSS, cross-cloud | Large scale |
| **Data Transport (Lightning Cube)** | Offline migration via physical devices | Terabytes to petabytes |
| **ossutil** | CLI-based batch operations | Medium scale |
| **ossimport** | Distributed migration tool | Large scale |
| **Cross-Region Replication (CRR)** | OSS-to-OSS across regions | Continuous |
| **Rclone / S3 tools** | Third-party tools via S3-compatible endpoint | Various |

### Migration Best Practices

- Use **multipart upload** for files > 100 MB
- Enable **transfer acceleration** for cross-border migrations
- Plan migration windows and use **incremental sync** to minimize downtime
- Validate data integrity with **CRC-64 checksums** or **Content-MD5** headers
- Use **back-to-origin rules** for seamless migration without downtime

## Performance Optimization

### Upload/Download Performance

- **Multipart Upload**: Split large files into 100 MB - 1 GB parts, upload in parallel
- **Transfer Acceleration**: Uses global edge nodes for faster long-distance transfers
- **CDN Integration**: Pair with Alibaba Cloud CDN for frequently accessed content
- **Range GET**: Download partial objects to reduce bandwidth

### Request Performance

- **Randomize Object Key Prefixes**: Avoid sequential/timestamp naming that causes hotspots
- **Multiple Buckets**: Distribute high-request workloads
- **Connection Pooling**: Reuse HTTP connections in SDK clients
- **Exponential Backoff**: Handle 503 throttling gracefully

### Caching

- Set **Cache-Control** and **Expires** headers for CDN-served objects
- Use **OSS Select** to query CSV/JSON in-place

## Security Best Practices

### Access Control

- **Principle of Least Privilege**: Use dedicated RAM users/roles for applications
- **STS Temporary Credentials**: Never embed long-term AccessKeys in client code
- **Private by Default**: Keep bucket ACL private unless absolutely necessary
- **Bucket Policies**: IP-based restrictions, VPC-based access
- **Anti-Hotlinking**: Configure Referer whitelist

### Data Encryption

| Method | Description |
|--------|-------------|
| **SSE-KMS** | Managed by KMS with CMK rotation support |
| **SSE-OSS** | Fully managed by OSS with AES-256 |
| **Client-Side** | Encrypt before upload for end-to-end encryption |
| **TLS/HTTPS** | Enforce via bucket policy |

### Monitoring & Auditing

- Enable **OSS Logging** (access logs in separate bucket)
- Use **ActionTrail** for API-level auditing
- Configure **Cloud Monitor** alarms for anomalies
- Enable **Anti-Hotlinking**

### Data Protection

- **Versioning**: Protect against accidental deletion/overwrite
- **WORM**: Write Once Read Many for regulatory compliance
- **Cross-Region Replication**: Geo-redundancy for disaster recovery

## Cost Optimization

### Storage Classes

| Storage Class | Use Case | Min Duration |
|---------------|----------|--------------|
| **Standard** | Frequently accessed (hot data) | None |
| **Infrequent Access (IA)** | Accessed < once/month | 30 days |
| **Archive** | Accessed < once/quarter | 60 days |
| **Cold Archive** | Long-term archival | 180 days |
| **Deep Cold Archive** | Compliance archival | 180 days |

### Cost-Saving Strategies

- **Lifecycle Rules**: Auto-transition or delete objects
- **Storage Capacity Units (SCUs)**: Prepaid packages (up to 50%+ discount)
- **Multipart Upload Cleanup**: Abort incomplete uploads via lifecycle rules
- **CDN for Egress**: OSS-to-CDN traffic is cheaper than direct internet egress
- **Batch Small Files**: Reduce unnecessary LIST/GET operations

## Architecture Patterns

### Static Website Hosting

1. Create bucket with static website hosting enabled
2. Upload HTML/CSS/JS/images
3. Bind custom domain with CNAME
4. Enable CDN for global delivery
5. Configure HTTPS with SSL certificate

### Data Lake

1. Use OSS as central data lake storage
2. Organize data with prefixes (raw/, processed/, analytics/)
3. Integrate with MaxCompute, EMR, Data Lake Analytics
4. Use lifecycle rules for tiered storage
5. Enable OSS-HDFS for Hadoop compatibility

### Media Processing Pipeline

1. Upload media to OSS
2. Trigger Function Compute / MPS on upload
3. Process (transcode, thumbnail, watermark)
4. Store processed results back to OSS
5. Deliver via CDN

### Backup & Disaster Recovery

1. Enable versioning on primary bucket
2. Configure CRR to secondary region
3. Set lifecycle rules for version cleanup
4. Use WORM for compliance retention
5. Test recovery procedures regularly

### Lifecycle Rules Example

```
Rule: "archive-old-logs"
Scope: Prefix = "logs/"
├── Transition to IA: 30 days after creation
├── Transition to Archive: 90 days after creation
├── Transition to Cold Archive: 365 days after creation
├── Expire/Delete: 2555 days (7 years)
└── Abort incomplete multipart uploads: 7 days
```
