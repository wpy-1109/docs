# Java SDK - Lifecycle Rules

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/lifecycle-rules-12

## Overview

Lifecycle rules allow you to automatically transition or expire objects based on age, access time, or other criteria.

## Set Lifecycle Rules

### Basic Expiration Rule

```java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.*;
import java.util.ArrayList;
import java.util.List;

EnvironmentVariableCredentialsProvider credentialsProvider =
    CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();

ClientBuilderConfiguration config = new ClientBuilderConfiguration();
config.setSignatureVersion(SignVersion.V4);
OSS ossClient = OSSClientBuilder.create()
    .endpoint(endpoint)
    .credentialsProvider(credentialsProvider)
    .clientConfiguration(config)
    .region(region)
    .build();

try {
    SetBucketLifecycleRequest request = new SetBucketLifecycleRequest(bucketName);

    // Rule: Delete objects with prefix "logs/" after 30 days
    LifecycleRule rule = new LifecycleRule("rule1", "logs/",
        LifecycleRule.RuleStatus.Enabled);
    rule.setExpirationDays(30);

    request.AddLifecycleRule(rule);
    ossClient.setBucketLifecycle(request);
} finally {
    ossClient.shutdown();
}
```

### Storage Transition Rule (Access Time-Based)

```java
// Enable access monitoring first
ossClient.putBucketAccessMonitor(bucketName,
    AccessMonitor.AccessMonitorStatus.Enabled.toString());

LifecycleRule rule = new LifecycleRule("rule1", "logs/",
    LifecycleRule.RuleStatus.Enabled);

// Transition to IA storage after 30 days without access
LifecycleRule.StorageTransition storageTransition =
    new LifecycleRule.StorageTransition();
storageTransition.setStorageClass(StorageClass.IA);
storageTransition.setExpirationDays(30);
storageTransition.setIsAccessTime(true);
storageTransition.setReturnToStdWhenVisit(false);
storageTransition.setAllowSmallFile(true);

List<LifecycleRule.StorageTransition> transitions = new ArrayList<>();
transitions.add(storageTransition);
rule.setStorageTransition(transitions);
```

### Noncurrent Version Transition (for Versioned Buckets)

```java
LifecycleRule rule2 = new LifecycleRule("rule2", "dir/",
    LifecycleRule.RuleStatus.Enabled);

LifecycleRule.NoncurrentVersionStorageTransition transition =
    new LifecycleRule.NoncurrentVersionStorageTransition();
transition.setStorageClass(StorageClass.IA);
transition.setNoncurrentDays(10);
transition.setIsAccessTime(true);
transition.setReturnToStdWhenVisit(true);
transition.setAllowSmallFile(false);

List<LifecycleRule.NoncurrentVersionStorageTransition> transitions =
    new ArrayList<>();
transitions.add(transition);
rule2.setNoncurrentVersionStorageTransitions(transitions);
```

## Get Lifecycle Rules

```java
List<LifecycleRule> rules = ossClient.getBucketLifecycle(bucketName);
for (LifecycleRule rule : rules) {
    System.out.println("Rule ID: " + rule.getId());
    System.out.println("Prefix: " + rule.getPrefix());
    System.out.println("Status: " + rule.getStatus());
    System.out.println("Expiration Days: " + rule.getExpirationDays());
}
```

## Delete Lifecycle Rules

```java
ossClient.deleteBucketLifecycle(bucketName);
```

## Lifecycle Actions

| Action | Description |
|--------|-------------|
| **Transition** | Move objects to IA, Archive, Cold Archive, or Deep Cold Archive |
| **Expiration** | Delete objects after specified days or on a specific date |
| **AbortMultipartUpload** | Clean up incomplete multipart uploads |
| **NoncurrentVersionTransition** | Transition noncurrent versions in versioned buckets |
| **NoncurrentVersionExpiration** | Delete noncurrent versions |
