# Java SDK - Bucket Operations

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/java-manage-buckets

## Create a Bucket

```java
// Simple creation
ossClient.createBucket(bucketName);

// With options (storage class, ACL, redundancy)
CreateBucketRequest createBucketRequest = new CreateBucketRequest(bucketName);
createBucketRequest.setStorageClass(StorageClass.Standard);
createBucketRequest.setCannedACL(CannedAccessControlList.Private);
createBucketRequest.setDataRedundancyType(DataRedundancyType.LRS);
ossClient.createBucket(createBucketRequest);
```

### V2 SDK

```java
PutBucketResult result = client.putBucket(
    PutBucketRequest.newBuilder()
        .bucket(bucketName)
        .build());

System.out.printf("Bucket created: statusCode=%d, requestId=%s\n",
    result.statusCode(), result.requestId());
```

## List Buckets

```java
List<Bucket> buckets = ossClient.listBuckets();
for (Bucket bucket : buckets) {
    System.out.println("Bucket: " + bucket.getName());
}
```

## Check if a Bucket Exists

```java
boolean exists = ossClient.doesBucketExist(bucketName);
System.out.println("Bucket exists: " + exists);
```

## Get Bucket Info

```java
BucketInfo info = ossClient.getBucketInfo(bucketName);
System.out.println("Location: " + info.getBucketLocation());
System.out.println("CreationDate: " + info.getBucket().getCreationDate());
System.out.println("StorageClass: " + info.getBucket().getStorageClass());
```

## Get Bucket Location

```java
String location = ossClient.getBucketLocation(bucketName);
System.out.println("Location: " + location);
```

## Set Bucket ACL

```java
ossClient.setBucketACL(bucketName, CannedAccessControlList.PublicRead);
```

## Get Bucket ACL

```java
AccessControlList acl = ossClient.getBucketAcl(bucketName);
System.out.println("Bucket ACL: " + acl.getCannedACL());
```

## Delete a Bucket

```java
ossClient.deleteBucket(bucketName);
```

**Note:** A bucket must be empty before it can be deleted. Delete all objects and incomplete multipart uploads first.

## API Reference

| Method | Description | Parameters | Return |
|--------|-------------|------------|--------|
| `createBucket(bucketName)` | Creates a new bucket | `bucketName` (String) | `Bucket` |
| `listBuckets()` | Lists all buckets | None | `List<Bucket>` |
| `doesBucketExist(bucketName)` | Checks if a bucket exists | `bucketName` (String) | `boolean` |
| `getBucketInfo(bucketName)` | Gets bucket metadata | `bucketName` (String) | `BucketInfo` |
| `getBucketLocation(bucketName)` | Gets bucket region | `bucketName` (String) | `String` |
| `setBucketAcl(bucketName, acl)` | Sets bucket ACL | `bucketName`, `CannedAccessControlList` | `void` |
| `getBucketAcl(bucketName)` | Gets bucket ACL | `bucketName` (String) | `AccessControlList` |
| `deleteBucket(bucketName)` | Deletes a bucket | `bucketName` (String) | `void` |
