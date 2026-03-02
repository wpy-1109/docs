# Troubleshooting 403 Forbidden Errors

Source: https://help.aliyun.com/zh/oss/

## Overview

HTTP 403 Forbidden is the most common OSS error. It indicates that the request was understood but the server refuses to authorize it. This guide covers all common causes and solutions.

## Cause 1: AccessDenied - Insufficient Permissions

### Symptoms
```xml
<Code>AccessDenied</Code>
<Message>You have no right to access this object because of bucket acl.</Message>
```

### Diagnosis
1. Check Bucket ACL: Is it private? If so, anonymous access is denied.
2. Check Object ACL: Object-level ACL overrides Bucket ACL.
3. Check RAM Policy: Does the RAM user/role have the necessary `oss:*` permissions?
4. Check Bucket Policy: Are there deny rules blocking the request?

### Solutions
- **RAM Policy**: Ensure the user has appropriate `oss:GetObject`, `oss:PutObject`, etc.
- **Bucket ACL**: Set to public-read if public access is intended (not recommended for production)
- **Signed URLs**: Generate signed URLs for temporary access to private objects
- **STS Tokens**: Ensure STS token hasn't expired and has correct permissions

### Common RAM Policy Examples

**Allow full access to a specific Bucket**:
```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "oss:*",
            "Resource": [
                "acs:oss:*:*:my-bucket",
                "acs:oss:*:*:my-bucket/*"
            ]
        }
    ]
}
```

**Allow read-only access**:
```json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "oss:GetObject",
                "oss:GetObjectAcl",
                "oss:ListObjects",
                "oss:GetBucketLocation"
            ],
            "Resource": [
                "acs:oss:*:*:my-bucket",
                "acs:oss:*:*:my-bucket/*"
            ]
        }
    ]
}
```

## Cause 2: SignatureDoesNotMatch

### Symptoms
```xml
<Code>SignatureDoesNotMatch</Code>
<Message>The request signature we calculated does not match the signature you provided.</Message>
```

### Common Causes
1. **Wrong AccessKey Secret**: Verify in RAM console
2. **String-to-sign mismatch**: Check HTTP method, headers, resource path
3. **URL encoding issues**: Special characters in object keys need proper encoding
4. **Content-Type mismatch**: Content-Type in signature must match the actual header
5. **Expired signature**: Check the Expires timestamp
6. **Wrong signature version**: Ensure V1 vs V4 signature matches your configuration

### Debugging Steps
1. Compare your string-to-sign with the one in the error response
2. Use OSS SDK instead of manual signing (SDK handles signing correctly)
3. Check for extra whitespace or encoding issues in headers
4. Verify the AccessKey pair is for the correct Alibaba Cloud account

## Cause 3: InvalidAccessKeyId

### Symptoms
```xml
<Code>InvalidAccessKeyId</Code>
<Message>The OSS Access Key Id you provided does not exist in our records.</Message>
```

### Solutions
1. Verify AccessKey ID in RAM console
2. Check if the AccessKey has been disabled or deleted
3. If using STS, ensure the token hasn't expired
4. Verify you're using AccessKey for the correct account

## Cause 4: RequestTimeTooSkewed

### Symptoms
```xml
<Code>RequestTimeTooSkewed</Code>
<Message>The difference between the request time and the current time is too large.</Message>
```

### Solution
OSS requires client time to be within **15 minutes** of server time.

1. Sync system clock with NTP:
   ```bash
   # Linux
   sudo ntpdate ntp.aliyun.com

   # Or using chrony
   sudo chronyc makestep
   ```
2. Check timezone configuration
3. If running in containers, ensure host time is synchronized

## Cause 5: Referer Restriction (Anti-Hotlinking)

### Symptoms
```xml
<Code>AccessDenied</Code>
<Message>You are denied by bucket referer policy.</Message>
```

### Solutions
1. Check Bucket anti-hotlinking configuration
2. Add the requesting domain to the Referer whitelist
3. Decide whether to allow empty Referer requests
4. For API/SDK calls, the Referer header may be empty - ensure configuration allows this

## Cause 6: Block Public Access

### Symptoms
403 error when trying to set Bucket to public-read or public-read-write.

### Solution
1. Navigate to **Bucket > Permission Control > Block Public Access**
2. Disable Block Public Access if public access is intended
3. Alternatively, use signed URLs or Bucket Policy for controlled access

## Cause 7: IP Address Restriction

### Symptoms
```xml
<Code>AccessDenied</Code>
<Message>Access denied by authorizer's policy.</Message>
```

### Solutions
1. Check Bucket Policy for IP address conditions
2. Verify your current public IP matches the allowed list
3. Note that proxy/NAT may change your apparent IP
4. For ECS instances, use internal endpoints (different IP range)

## Cause 8: VPC Endpoint Restriction

### Symptoms
Access denied when accessing from specific VPC environments.

### Solutions
1. Check if Bucket Policy restricts to specific VPC IDs
2. Verify VPC endpoint configuration
3. Ensure the request is routed through the correct endpoint

## Troubleshooting Checklist

- [ ] Verify AccessKey ID and Secret are correct and active
- [ ] Check RAM policy permissions for the specific action
- [ ] Review Bucket Policy for deny rules
- [ ] Check Bucket and Object ACL settings
- [ ] Verify system clock is synchronized (within 15 minutes)
- [ ] Check anti-hotlinking (Referer) configuration
- [ ] Verify Block Public Access setting
- [ ] Check for IP address restrictions in policies
- [ ] If using STS, verify token expiration
- [ ] Check the RequestId and EC code for specific diagnosis
