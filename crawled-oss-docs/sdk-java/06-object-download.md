# Java SDK - Object Download

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/simple-download-11

## Simple Download (GetObject)

### Download to Local File

```java
ossClient.getObject(new GetObjectRequest(bucketName, objectName),
    new File("/path/to/local/file.txt"));
```

### Streaming Download

```java
OSSObject ossObject = ossClient.getObject(bucketName, objectName);
InputStream inputStream = ossObject.getObjectContent();

BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
String line;
while ((line = reader.readLine()) != null) {
    System.out.println(line);
}
reader.close();
ossObject.close();
```

### Range Download

Download only a specific byte range of the object:

```java
GetObjectRequest request = new GetObjectRequest(bucketName, objectName);
request.setRange(0, 1023); // Download first 1KB

OSSObject ossObject = ossClient.getObject(request);
InputStream inputStream = ossObject.getObjectContent();
// ... read the stream
ossObject.close();
```

### Conditional Download

Download only if conditions are met:

```java
GetObjectRequest request = new GetObjectRequest(bucketName, objectName);
request.setModifiedSinceConstraint(sinceDate);  // Only if modified since
// or
request.setUnmodifiedSinceConstraint(sinceDate);  // Only if NOT modified since
// or
request.setMatchingETagConstraints(etagList);     // Only if ETag matches
// or
request.setNonmatchingETagConstraints(etagList);  // Only if ETag doesn't match

OSSObject ossObject = ossClient.getObject(request);
```

### V2 SDK - Download

```java
try (GetObjectResult result = client.getObject(
        GetObjectRequest.newBuilder()
            .bucket(bucket)
            .key(key)
            .build())) {

    byte[] data = IOUtils.toByteArray(result.body());
    String content = new String(data);

    System.out.printf("Object downloaded: statusCode=%d, requestId=%s, " +
        "eTag=%s, contentLength=%d\n",
        result.statusCode(), result.requestId(),
        result.eTag(), result.contentLength());
    System.out.println("Content: " + content);
}
```

## Resumable Download

For large files, use resumable download with checkpoint support:

```java
DownloadFileRequest downloadFileRequest = new DownloadFileRequest(bucketName, objectName);
downloadFileRequest.setDownloadFile("/path/to/local/file.txt");
downloadFileRequest.setPartSize(1024 * 1024);  // 1MB per part
downloadFileRequest.setTaskNum(10);              // 10 concurrent threads
downloadFileRequest.setEnableCheckpoint(true);   // Enable checkpoint
downloadFileRequest.setCheckpointFile("/path/to/checkpoint/file");

DownloadFileResult result = ossClient.downloadFile(downloadFileRequest);
```

## Download with Progress

```java
GetObjectRequest request = new GetObjectRequest(bucketName, objectName);
request.setProgressListener(new ProgressListener() {
    @Override
    public void progressChanged(ProgressEvent progressEvent) {
        long bytes = progressEvent.getBytes();
        ProgressEventType eventType = progressEvent.getEventType();
        System.out.println("Event: " + eventType + ", Bytes: " + bytes);
    }
});

ossClient.getObject(request, new File("/path/to/local/file.txt"));
```

## List Objects

```java
// Simple listing
ObjectListing objectListing = ossClient.listObjects(bucketName);
for (OSSObjectSummary objectSummary : objectListing.getObjectSummaries()) {
    System.out.println("Key: " + objectSummary.getKey() +
        " Size: " + objectSummary.getSize());
}

// With prefix filter
ListObjectsRequest listRequest = new ListObjectsRequest(bucketName);
listRequest.setPrefix("photos/");
listRequest.setMaxKeys(100);
ObjectListing listing = ossClient.listObjects(listRequest);
```

## Delete Objects

```java
// Delete single object
ossClient.deleteObject(bucketName, objectName);

// Delete multiple objects
List<String> keys = Arrays.asList("key1", "key2", "key3");
DeleteObjectsRequest deleteRequest = new DeleteObjectsRequest(bucketName);
deleteRequest.setKeys(keys);
ossClient.deleteObjects(deleteRequest);
```

## Copy Objects

```java
CopyObjectResult copyResult = ossClient.copyObject(
    sourceBucketName, sourceObjectName,
    destBucketName, destObjectName);
System.out.println("ETag: " + copyResult.getETag());
```
