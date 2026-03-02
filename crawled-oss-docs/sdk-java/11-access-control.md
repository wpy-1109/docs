# Java SDK - Access Control

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/access-control

## Bucket ACL

### ACL Types

| ACL | Description |
|-----|-------------|
| `Private` | Only the owner can read/write |
| `PublicRead` | Anyone can read; only owner can write |
| `PublicReadWrite` | Anyone can read and write |

### Set Bucket ACL

```java
ossClient.setBucketAcl(bucketName, CannedAccessControlList.Private);
```

### Get Bucket ACL

```java
AccessControlList acl = ossClient.getBucketAcl(bucketName);
System.out.println("Bucket ACL: " + acl.getCannedACL());
```

## Object ACL

### ACL Types

| ACL | Description |
|-----|-------------|
| `Default` | Inherits from bucket |
| `Private` | Only the owner can read/write |
| `PublicRead` | Anyone can read; only owner can write |
| `PublicReadWrite` | Anyone can read and write |

### Set Object ACL

```java
ossClient.setObjectAcl(bucketName, objectName, CannedAccessControlList.PublicRead);
```

### Get Object ACL

```java
ObjectAcl objectAcl = ossClient.getObjectAcl(bucketName, objectName);
System.out.println("Object ACL: " + objectAcl.getPermission());
```

## Bucket Policy

Use JSON-based policies for fine-grained access control:

```java
String policyText = "{" +
    "\"Version\": \"1\"," +
    "\"Statement\": [{" +
    "    \"Effect\": \"Allow\"," +
    "    \"Principal\": [\"*\"]," +
    "    \"Action\": [\"oss:GetObject\"]," +
    "    \"Resource\": [\"acs:oss:*:*:mybucket/public/*\"]" +
    "}]" +
    "}";

ossClient.setBucketPolicy(bucketName, policyText);
```

### Get Bucket Policy

```java
GetBucketPolicyResult policyResult = ossClient.getBucketPolicy(bucketName);
System.out.println("Policy: " + policyResult.getPolicyText());
```

### Delete Bucket Policy

```java
ossClient.deleteBucketPolicy(bucketName);
```

## STS Temporary Credentials

For temporary, scoped access:

```java
String stsEndpoint = "sts.aliyuncs.com";
String roleArn = "<your-role-arn>";
String roleSessionName = "session-name";

// Get STS token using RAM SDK
// AssumeRoleResponse response = client.getAcsResponse(assumeRoleRequest);
// String accessKeyId = response.getCredentials().getAccessKeyId();
// String accessKeySecret = response.getCredentials().getAccessKeySecret();
// String securityToken = response.getCredentials().getSecurityToken();

OSS ossClient = new OSSClientBuilder().build(
    endpoint, accessKeyId, accessKeySecret, securityToken);
```

## CORS Configuration

```java
SetBucketCORSRequest corsRequest = new SetBucketCORSRequest(bucketName);

CORSRule rule = new CORSRule();
rule.addAllowedOrigin("https://example.com");
rule.addAllowedMethod("GET");
rule.addAllowedMethod("PUT");
rule.addAllowedHeader("*");
rule.setMaxAgeSeconds(3600);

corsRequest.addCorsRule(rule);
ossClient.setBucketCORS(corsRequest);
```
