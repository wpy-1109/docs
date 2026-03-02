# OSS Security and Access Control FAQ

Source: https://help.aliyun.com/zh/oss/faq-overview

## Authentication FAQ

### What is the difference between RAM Policy and Bucket Policy?
| Feature | RAM Policy | Bucket Policy |
|---|---|---|
| **Attached to** | RAM user/role/group | Bucket resource |
| **Cross-account** | Requires role assumption | Direct cross-account grants |
| **Anonymous access** | Not supported | Supported |
| **Use case** | Managing your own users | Sharing with external users |

### When should I use STS temporary credentials?
Use STS when:
- Client applications (mobile, web) need direct OSS access
- You want time-limited, permission-restricted access
- You don't want to expose long-term AccessKeys
- Third-party applications need temporary access

### How long can STS tokens last?
- Minimum: 900 seconds (15 minutes)
- Maximum: 43200 seconds (12 hours, for role-based STS)
- Default: 3600 seconds (1 hour)

### What is a signed URL and when should I use it?
A signed URL is a pre-authenticated URL that grants temporary access to a specific object. Use when:
- Sharing private files with external users
- Providing download links in emails or web pages
- No SDK is available on the client side

## Encryption FAQ

### What encryption options does OSS support?
1. **SSE-KMS**: Server-side encryption using KMS-managed keys
   - Supports customer-managed keys (CMK)
   - Key rotation support
   - Audit trail for key usage
2. **SSE-OSS**: Server-side encryption using OSS-managed keys
   - Fully managed, no key management needed
   - AES-256 encryption
3. **Client-side encryption**: Application encrypts before upload
   - User manages keys entirely
   - Data is encrypted at rest and in transit

### Can I enable encryption for existing objects?
Server-side encryption only applies to newly uploaded objects. To encrypt existing objects:
1. Enable default encryption on the Bucket
2. Use `CopyObject` to copy objects in-place (this re-encrypts them)

### Does encryption affect performance?
SSE-KMS and SSE-OSS have minimal performance impact as encryption/decryption happens on the server side. Client-side encryption depends on your application's processing power.

## Access Control FAQ

### How do I make a single file public?
Options (from most to least restrictive):
1. **Signed URL**: Generate a temporary public URL (recommended)
2. **Object ACL**: Set the specific object to `public-read`
3. **Bucket Policy**: Allow anonymous access to specific object keys

### How do I restrict access by IP address?
Use Bucket Policy with IP conditions:
```json
{
    "Version": "1",
    "Statement": [{
        "Effect": "Deny",
        "Principal": "*",
        "Action": "oss:*",
        "Resource": ["acs:oss:*:*:bucket/*"],
        "Condition": {
            "NotIpAddress": {
                "acs:SourceIp": ["203.0.113.0/24"]
            }
        }
    }]
}
```

### How do I restrict access to a specific VPC?
Use Bucket Policy with VPC conditions or configure Access Points with VPC restrictions.

### What does "Block Public Access" do?
When enabled, it prevents:
- Setting Bucket ACL to public-read or public-read-write
- Setting Object ACL to public-read or public-read-write
- Bucket Policy grants allowing anonymous access

This is a safety net to prevent accidental public exposure. It's enabled by default for new Buckets.

## Compliance FAQ

### Does OSS support WORM (immutable storage)?
Yes. OSS supports time-based retention policies:
- Set retention period from 1 day to 70 years
- Once locked, the policy cannot be shortened or removed
- Objects cannot be deleted until retention expires
- Meets SEC 17a-4(f), FINRA, CFTC requirements

### What compliance certifications does OSS have?
- ISO 27001 (Information Security)
- SOC 2 Type II
- PCI DSS
- GDPR readiness
- China Cybersecurity Law compliance
- Various industry-specific certifications

### How do I enable access logging for audit?
1. Navigate to **Bucket > Logging and Monitoring > Access Logging**
2. Enable logging
3. Specify target Bucket and prefix for log storage
4. Logs include: requester identity, operation type, time, source IP, etc.
