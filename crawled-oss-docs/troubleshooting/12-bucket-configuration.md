# Troubleshooting Bucket Configuration Issues

Source: https://help.aliyun.com/zh/oss/

## Overview

This guide covers common issues with Bucket configuration including lifecycle rules, versioning, replication, logging, and other Bucket-level settings.

## Lifecycle Rule Issues

### Rules Not Taking Effect

**Symptoms**: Objects not transitioning or being deleted as expected.

**Possible Causes**:
1. **Rule status**: Ensure rule is **Enabled**, not Disabled
2. **Prefix mismatch**: Verify prefix matches target objects exactly
3. **Timing**: Lifecycle rules execute once per day (not real-time). Changes may take up to 24 hours
4. **Minimum storage duration**: Objects in IA/Archive have minimum storage periods
   - IA: 30 days minimum
   - Archive: 60 days minimum
   - Cold Archive: 180 days minimum
5. **Tag mismatch**: If using tag-based rules, verify object tags match

**Debugging**:
```bash
# Check lifecycle configuration
ossutil lifecycle get oss://bucket-name

# Check object metadata to verify current storage class
ossutil stat oss://bucket-name/object-key
```

### Objects Deleted Unexpectedly

**Cause**: Lifecycle rules may be deleting objects unintentionally.

**Prevention**:
- Review all lifecycle rules carefully
- Use prefixes to limit rule scope
- Enable versioning before setting deletion rules
- Test rules with a small subset first

### Minimum Storage Duration Charges

**Issue**: Transitioning or deleting objects before minimum storage duration incurs full-period charges.

**Example**: An IA object deleted after 15 days still incurs charges for 30 days.

**Solution**: Plan lifecycle transitions to align with minimum storage durations.

## Versioning Issues

### Cannot Disable Versioning

**Behavior**: Once enabled, versioning can be **suspended** but not disabled. Suspended versioning stops creating new versions but retains existing versions.

### Storage Costs Increasing with Versioning

**Cause**: All previous versions are retained, consuming storage.

**Solution**: Configure lifecycle rules for non-current versions:
```json
{
    "Rules": [
        {
            "ID": "cleanup-old-versions",
            "Status": "Enabled",
            "NoncurrentVersionExpiration": {
                "NoncurrentDays": 90
            }
        }
    ]
}
```

### Delete Markers Accumulating

**Cause**: Deleting objects in a versioned Bucket creates delete markers instead of removing data.

**Solution**: Configure lifecycle rules to clean up expired delete markers:
```json
{
    "Rules": [
        {
            "ID": "cleanup-delete-markers",
            "Status": "Enabled",
            "Expiration": {
                "ExpiredObjectDeleteMarker": true
            }
        }
    ]
}
```

## Cross-Region Replication Issues

### Replication Lag

**Symptoms**: Objects not appearing in target Bucket immediately.

**Causes**:
- Large objects take longer to replicate
- High replication volume
- Cross-region network latency

**Monitoring**: Check CRR progress in OSS Console > Redundancy and Fault Tolerance.

### Replication Failures

**Common Causes**:
1. **IAM role permissions**: CRR role lacks permissions on source or target
2. **Target Bucket doesn't exist**: Verify target Bucket name and region
3. **Encryption incompatibility**: KMS-encrypted objects may require special CRR configuration
4. **Versioning not enabled**: CRR requires versioning on both source and target Buckets

## Logging Issues

### Access Logs Not Generated

**Causes**:
- Logging not enabled on the Bucket
- Target log Bucket is in a different region
- Insufficient permissions for log delivery

**Solution**:
1. Navigate to **Bucket > Logging and Monitoring > Access Logging**
2. Enable logging
3. Specify the target Bucket and prefix
4. Target Bucket must be in the same region

### Log Format

Access logs are stored as text files with fields separated by spaces:
```
RemoteIP Reserved Reserved Time Request HTTPStatus SentBytes RequestTime Referer UserAgent HostName RequestID LoggingFlag RequesterPay
```

## WORM Policy Issues

### Cannot Delete Objects

**Cause**: WORM (Write Once Read Many) retention policy prevents deletion.

**Important**: A locked WORM policy **cannot** be shortened or removed. Objects covered by the policy cannot be deleted until the retention period expires.

**Solutions**:
- Wait for the retention period to expire
- For unlocked policies, you can delete the policy
- Plan retention periods carefully before locking

## Static Website Hosting Issues

### HTML Files Download Instead of Displaying

**Cause**: Accessing via OSS default domain forces download for security.

**Solution**: Bind a custom domain name to enable browser rendering.

### 404 Errors with SPA

**Cause**: Client-side routes don't correspond to server-side files.

**Solution**: Set default 404 page to `index.html` and error response code to `200`.

## Encryption Issues

### SSE-KMS Key Not Found

**Cause**: CMK ID specified doesn't exist in the region's KMS service.

**Solution**:
- Verify CMK ID in KMS Console
- Ensure CMK is in the same region as the Bucket
- Check CMK status (not disabled or pending deletion)

### Cross-Region Access with KMS

**Issue**: KMS keys are region-specific. Cross-region replication of KMS-encrypted objects requires KMS key in both regions.

## Bucket Deletion Issues

### BucketNotEmpty

**Error**: Cannot delete Bucket with existing objects.

**Solution**:
```bash
# Delete all objects (including all versions if versioning is enabled)
ossutil rm oss://bucket-name/ -r --all-versions

# Delete incomplete multipart uploads
ossutil rm oss://bucket-name/ -r --all-type

# Then delete the Bucket
ossutil rm oss://bucket-name -b
```

### Cannot Delete Bucket with WORM Policy

**Solution**: WORM-protected objects cannot be deleted until retention expires. You must wait for all protected objects' retention periods to expire.
