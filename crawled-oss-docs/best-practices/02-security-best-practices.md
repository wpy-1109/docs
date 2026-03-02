# Security Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/security-best-practices/

## Overview

When using OSS, you need to guard against multiple risks to ensure secure and stable data storage and transmission. This guide covers common risk types and countermeasures including account security risks, malicious traffic attacks, data loss risks, sensitive data masking, and Bucket security configuration risks.

## Risk Mitigation Strategies

### 1. Set ACL to Private Access

Unless you explicitly require anyone (including anonymous users) to read/write your OSS resources, **never set Bucket or Object ACL to public-read or public-read-write**.

- **Public-read-write**: Anyone (including anonymous users) can read and write Objects in the Bucket.
  - WARNING: Any internet user can access and write data to Objects in the Bucket. This may cause data leakage, cost surges, and potential illegal content uploads.
- **Public-read**: Only the Bucket owner can write; anyone can read.
  - WARNING: Any internet user can access Objects, potentially causing data leakage and cost surges.

**Recommendation**: Set Bucket and Object ACL to **private**. Only the Bucket owner can perform read/write operations.

Methods to set ACL:
- OSS Console
- API/SDK (SetBucketAcl, SetObjectAcl)
- ossutil CLI

### 2. Never Hardcode AccessKeys in Source Code

Hardcoding AccessKeys in code leads to key leakage when source code is exposed. Local encrypted storage is also insecure because encryption/decryption data resides in memory, which can be dumped.

**For server-side applications**: Use the Alibaba Cloud SDK Managed Credentials Plugin to avoid hardcoding AccessKeys. This solves the problem of AccessKey leakage due to source code or compiled artifact exposure.

**IMPORTANT**: This approach is NOT suitable for client-side applications. Never embed any form of AccessKey in client-side code.

### 3. Use RAM Users for OSS Access

The primary Alibaba Cloud account AccessKey has full API access permissions, which is high-risk. **Always create and use RAM (Resource Access Management) users** for API access and daily operations.

Benefits:
- Control user permissions for resource operations
- Enable multi-user collaboration without sharing the primary account key
- Assign minimum necessary permissions to reduce security risks

**Example RAM Policy** - Deny a RAM user access to a specific bucket:
```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "oss:*",
            "Resource": [
                "acs:oss:*:*:examplebucket",
                "acs:oss:*:*:examplebucket/*"
            ]
        }
    ]
}
```

You can also:
- Deny RAM users from deleting any files in a Bucket
- Grant RAM users read-only access to specific Bucket resources

### 4. Enable Multi-Factor Authentication (MFA)

MFA is a simple and effective security best practice. When enabled, logging into the Alibaba Cloud console requires both the account password and a dynamic verification code from the MFA device.

- Enable MFA for Alibaba Cloud accounts
- Enable MFA for RAM users

### 5. Use STS Temporary Authorization for OSS Access

Use Security Token Service (STS) to issue temporary access credentials to other users. These credentials allow access to OSS resources within a specified time period without exposing your long-term keys.

Key benefits:
- Time-limited access
- No long-term key exposure
- Fine-grained permission control

### 6. Configure Bucket Policy with Least Privilege

Bucket Policy allows you to authorize other users to access specified OSS resources. Follow these principles:

#### a. Avoid Authorizing the Entire Bucket
Over-broad resource authorization can lead to unauthorized data access. In production, always specify resource paths rather than authorizing the entire Bucket.

#### b. Never Allow Anonymous Access
Anonymous access means anyone who knows the Endpoint and Bucket name can access OSS. Since Endpoints are enumerable and Bucket names can be extracted from authorized file URLs, anonymous access poses extreme security risks.

#### c. Set Reasonable Actions
The console's simplified settings provide four authorization operations (Actions), but they may not match your exact business needs. Use advanced settings to grant minimum permissions. For example, file downloads typically only need `oss:GetObject` permission, not the full read-only set including `oss:ListObjects`.

### 7. Enable HTTPS Access

HTTPS prevents:
- Man-in-the-middle attacks
- Domain hijacking
- Chrome blocking HTTP resources on HTTPS sites

Always enable HTTPS to solve multiple risk issues at minimal cost.

### 8. Restrict Source IP Addresses

If the IP addresses accessing OSS resources are fixed and enumerable, strongly recommend configuring IP address restrictions in Bucket Policy.

Example: Grant RAM user "Test" download permission for objects under the `log/` directory in `examplebucket`, restricted to specific IP addresses.

## Sensitive Data Protection

### Integration with Data Security Center (DSC)

Combine OSS with Alibaba Cloud Data Security Center (DSC) for sensitive data identification, classification, grading, and protection.

Use DSC to:
- **Mask sensitive data in OSS table files**: Automatically detect and mask PII and other sensitive information in CSV, Excel, and other tabular data stored in OSS.
- **Mask ID numbers in ID card images**: Detect and mask identification numbers in scanned ID card images stored in OSS.

## Risk Prevention for Malicious Traffic

To reduce the risk of large financial losses caused by malicious access traffic:
- Configure bandwidth throttling
- Set up request rate limits
- Enable pay-by-requester mode for shared data
- Use CDN with anti-hotlinking (Referer whitelist)
- Set up CloudMonitor alerts for abnormal traffic patterns

## Data Loss Prevention

To reduce risks of data loss caused by accidental operations:
- Enable versioning to maintain object history
- Configure cross-region replication (CRR) for disaster recovery
- Set up scheduled backups using HBR (Hybrid Backup Recovery)
- Use WORM (Write Once Read Many) policies for compliance
- Configure retention policies to prevent premature deletion

## Bucket Security Configuration Compliance

Regular security audits should check:
- ACL settings (ensure private where appropriate)
- Encryption configuration (SSE-KMS or SSE-OSS)
- Logging enabled for audit trails
- CORS configuration (restrict allowed origins)
- Referer whitelist configuration
- Block public access settings
