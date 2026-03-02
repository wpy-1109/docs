# Java SDK - Encryption

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-12

## Server-Side Encryption (SSE)

### SSE-OSS (AES-256, Managed by OSS)

Set bucket-level default encryption:

```java
ServerSideEncryptionByDefault sseConfig = new ServerSideEncryptionByDefault();
sseConfig.setSSEAlgorithm(SSEAlgorithm.AES256);

ServerSideEncryptionConfiguration encryptionConfig =
    new ServerSideEncryptionConfiguration();
encryptionConfig.setApplyServerSideEncryptionByDefault(sseConfig);

SetBucketEncryptionRequest request =
    new SetBucketEncryptionRequest(bucketName, encryptionConfig);
ossClient.setBucketEncryption(request);
```

### SSE-KMS (Key Management Service)

```java
ServerSideEncryptionByDefault sseConfig = new ServerSideEncryptionByDefault();
sseConfig.setSSEAlgorithm(SSEAlgorithm.KMS);
sseConfig.setKMSMasterKeyID("<your-cmk-id>"); // Optional: specify CMK

ServerSideEncryptionConfiguration encryptionConfig =
    new ServerSideEncryptionConfiguration();
encryptionConfig.setApplyServerSideEncryptionByDefault(sseConfig);

SetBucketEncryptionRequest request =
    new SetBucketEncryptionRequest(bucketName, encryptionConfig);
ossClient.setBucketEncryption(request);
```

### Per-Object Encryption

```java
ObjectMetadata metadata = new ObjectMetadata();

// SSE-OSS
metadata.setServerSideEncryption(ObjectMetadata.AES_256_SERVER_SIDE_ENCRYPTION);

// Or SSE-KMS
metadata.setServerSideEncryption("KMS");
metadata.setServerSideEncryptionKeyId("<your-cmk-id>");

ossClient.putObject(bucketName, objectName, inputStream, metadata);
```

### Get Bucket Encryption Configuration

```java
ServerSideEncryptionConfiguration config =
    ossClient.getBucketEncryption(bucketName);
System.out.println("Algorithm: " +
    config.getApplyServerSideEncryptionByDefault().getSSEAlgorithm());
```

### Delete Bucket Encryption Configuration

```java
ossClient.deleteBucketEncryption(bucketName);
```

## Client-Side Encryption

Encrypt data before uploading:

```java
// Client-side encryption with RSA
// Use OSSEncryptionClient for automatic client-side encryption
// OSSEncryptionClient ossEncryptionClient = new OSSEncryptionClientBuilder().build(
//     endpoint, credentialsProvider, rsaKeyPair);
// ossEncryptionClient.putObject(bucketName, objectName, inputStream);
```

## Encryption Types Summary

| Type | Algorithm | Key Management | Use Case |
|------|-----------|----------------|----------|
| **SSE-OSS** | AES-256 | Fully managed by OSS | Simple encryption at rest |
| **SSE-KMS** | AES-256 via KMS | KMS-managed, optional CMK | Compliance, key rotation |
| **Client-Side** | RSA/AES | Customer-managed | End-to-end encryption |
