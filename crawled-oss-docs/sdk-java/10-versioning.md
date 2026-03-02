# Java SDK - Versioning

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/versioning-8

## Overview

When versioning is enabled, OSS preserves all versions of every object. Each version gets a unique version ID.

## Enable Versioning

```java
BucketVersioningConfiguration config = new BucketVersioningConfiguration();
config.setStatus(BucketVersioningConfiguration.ENABLED);

SetBucketVersioningRequest request = new SetBucketVersioningRequest(bucketName, config);
ossClient.setBucketVersioning(request);
```

## Suspend Versioning

```java
BucketVersioningConfiguration config = new BucketVersioningConfiguration();
config.setStatus(BucketVersioningConfiguration.SUSPENDED);

SetBucketVersioningRequest request = new SetBucketVersioningRequest(bucketName, config);
ossClient.setBucketVersioning(request);
```

## Get Versioning Status

```java
GetBucketVersioningRequest getRequest = new GetBucketVersioningRequest(bucketName);
BucketVersioningConfiguration result = ossClient.getBucketVersioning(getRequest);
System.out.println("Versioning status: " + result.getStatus());
```

## Download a Specific Version

```java
GetObjectRequest request = new GetObjectRequest(bucketName, objectName);
request.setVersionId("versionId");
OSSObject ossObject = ossClient.getObject(request);
```

## Delete a Specific Version

```java
ossClient.deleteVersion(bucketName, objectName, "versionId");
```

## List Object Versions

```java
ListVersionsRequest listRequest = new ListVersionsRequest();
listRequest.setBucketName(bucketName);

VersionListing versionListing = ossClient.listVersions(listRequest);
for (OSSVersionSummary version : versionListing.getVersionSummaries()) {
    System.out.printf("Key: %s, VersionId: %s, IsLatest: %s, Size: %d\n",
        version.getKey(), version.getVersionId(),
        version.isLatest(), version.getSize());
}
```

## Restore a Previous Version

To restore a previous version, copy it as the current version:

```java
CopyObjectRequest copyRequest = new CopyObjectRequest(
    bucketName, objectName, bucketName, objectName);
copyRequest.setSourceVersionId("previousVersionId");
ossClient.copyObject(copyRequest);
```
