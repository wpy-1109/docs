# Sensitive Data Protection Best Practices

Source: https://help.aliyun.com/zh/oss/use-cases/sensitive-data-protection

## Overview

Combine OSS with Alibaba Cloud Data Security Center (DSC) to identify, classify, and protect sensitive data stored in object storage. This is essential for compliance with data protection regulations and safeguarding PII.

## Integration with Data Security Center (DSC)

### Capabilities

1. **Sensitive Data Discovery**: Automatically scan OSS buckets to identify sensitive data
2. **Data Classification**: Classify discovered data by sensitivity level
3. **Data Masking**: Apply masking rules to sensitive fields
4. **Audit Logging**: Track access to sensitive data
5. **Compliance Reporting**: Generate reports for regulatory compliance

### Supported Data Types for Detection

| Category | Examples |
|---|---|
| Personal Information | Names, phone numbers, email addresses, physical addresses |
| Identity Documents | ID card numbers, passport numbers, driver's license numbers |
| Financial Data | Bank account numbers, credit card numbers |
| Medical Data | Patient records, diagnosis codes |
| Authentication | Passwords, AccessKeys, tokens, certificates |
| Custom Patterns | User-defined regex patterns for business-specific data |

### Data Masking in Table Files

For CSV, Excel, and other tabular data stored in OSS:
1. Configure DSC to scan target Bucket
2. Define masking rules (hash, redact, partial mask, etc.)
3. DSC creates masked copies of sensitive files
4. Original files can be access-controlled or deleted

### ID Card Image Masking

For scanned ID card images stored in OSS:
1. DSC uses OCR to detect ID numbers in images
2. Automatically applies masking (blur, blackout) to sensitive areas
3. Generates masked versions of images

## Server-Side Encryption

### SSE-KMS (Key Management Service)

- Keys managed by Alibaba Cloud KMS
- Support for customer-managed keys (CMK)
- Key rotation support
- Audit trail for key usage

**Configuration**:
```
x-oss-server-side-encryption: KMS
x-oss-server-side-encryption-key-id: <CMK-ID>
```

### SSE-OSS (OSS-Managed Keys)

- Fully managed encryption, no key management needed
- AES-256 encryption
- Simplest configuration

**Configuration**:
```
x-oss-server-side-encryption: AES256
```

### Default Bucket Encryption

Configure encryption at the Bucket level so all objects are automatically encrypted:
1. Navigate to **Bucket > Data Encryption**
2. Select encryption method (KMS or OSS-managed)
3. Optionally specify a CMK ID for KMS

## Access Logging and Auditing

### OSS Access Logs

Enable access logging to track all requests:
- Who accessed what data and when
- IP addresses and user agents
- Request types and response codes
- Integrate with SLS for real-time analysis

### ActionTrail Integration

Track management operations:
- Bucket creation/deletion
- ACL changes
- Policy modifications
- Encryption configuration changes

## Compliance Frameworks

OSS supports compliance with:
- **China Cybersecurity Law**: Data localization, encryption requirements
- **GDPR**: Data protection for EU citizens' data
- **SOC 2 Type II**: Security controls audit
- **ISO 27001**: Information security management
- **PCI DSS**: Payment card data protection
- **HIPAA**: Healthcare data protection (via BAA with Alibaba Cloud)

## Best Practices

1. **Scan all Buckets** with DSC to discover unknown sensitive data
2. **Classify data** by sensitivity level and apply appropriate protection
3. **Enable encryption** (SSE-KMS recommended) for all Buckets containing sensitive data
4. **Restrict access** using RAM policies with least privilege principle
5. **Enable access logging** and retain logs for compliance periods
6. **Regular audits**: Review access patterns and permissions quarterly
7. **Data masking**: Apply masking before sharing data with developers/testers
8. **Key rotation**: Rotate encryption keys according to your security policy
