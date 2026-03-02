# Java SDK - Error Handling

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/java-error-handling

## Exception Types

The OSS Java SDK throws two types of exceptions:

### OSSException (Server-Side Errors)

Thrown when the request reaches OSS but is rejected. Contains:
- **Error Code**: Specific OSS error code
- **Error Message**: Human-readable error description
- **Request ID**: Unique request identifier for troubleshooting
- **Host ID**: The OSS endpoint that processed the request

### ClientException (Client-Side Errors)

Thrown when the client encounters issues before reaching OSS:
- Network connectivity problems
- DNS resolution failures
- Timeout errors

## Error Handling Pattern

```java
import com.aliyun.oss.OSSException;
import com.aliyun.oss.ClientException;

try {
    // OSS operations
    ossClient.putObject(bucketName, objectName, new File(filePath));

} catch (OSSException oe) {
    System.out.println("Caught an OSSException, which means your request made it to OSS, "
        + "but was rejected with an error response for some reason.");
    System.out.println("Error Message:" + oe.getErrorMessage());
    System.out.println("Error Code:" + oe.getErrorCode());
    System.out.println("Request ID:" + oe.getRequestId());
    System.out.println("Host ID:" + oe.getHostId());
} catch (ClientException ce) {
    System.out.println("Caught an ClientException, which means the client encountered "
        + "a serious internal problem while trying to communicate with OSS, "
        + "such as not being able to access the network.");
    System.out.println("Error Message:" + ce.getMessage());
} finally {
    if (ossClient != null) {
        ossClient.shutdown();
    }
}
```

## V2 SDK Error Handling

```java
try {
    PutObjectResult result = client.putObject(PutObjectRequest.newBuilder()
        .bucket(bucket)
        .key(key)
        .body(BinaryData.fromString(data))
        .build());
} catch (Exception e) {
    ServiceException se = ServiceException.asCause(e);
    if (se != null) {
        System.out.printf("ServiceException: requestId:%s, errorCode:%s\n",
            se.requestId(), se.errorCode());
    }
}
```

## Common Error Codes

| Error Code | HTTP Status | Description |
|------------|-------------|-------------|
| `AccessDenied` | 403 | Access denied |
| `BucketAlreadyExists` | 409 | Bucket already exists |
| `BucketNotEmpty` | 409 | Bucket is not empty |
| `EntityTooLarge` | 400 | Entity too large (>5GB for PutObject) |
| `InvalidAccessKeyId` | 403 | Invalid AccessKey ID |
| `InvalidArgument` | 400 | Invalid argument |
| `InvalidBucketName` | 400 | Invalid bucket name |
| `InvalidObjectName` | 400 | Invalid object name |
| `NoSuchBucket` | 404 | Bucket does not exist |
| `NoSuchKey` | 404 | Object does not exist |
| `NoSuchUpload` | 404 | Multipart upload does not exist |
| `RequestTimeTooSkewed` | 403 | Client time differs too much from server |
| `SignatureDoesNotMatch` | 403 | Signature mismatch |
| `TooManyBuckets` | 400 | Too many buckets |

## Image Processing

Apply image processing operations when downloading:

```java
// Resize image
GetObjectRequest request = new GetObjectRequest(bucketName, objectName);
request.setProcess("image/resize,m_fixed,w_100,h_100");
OSSObject ossObject = ossClient.getObject(request);

// Watermark
request.setProcess("image/watermark,text_SGVsbG8gT1NT,type_d3F5LXplbmhlaQ,size_30");

// Format conversion
request.setProcess("image/format,png");

// Multiple operations (pipeline)
request.setProcess("image/resize,w_200/watermark,text_SGVsbG8/format,jpg");
```

## Image Styles

```java
// Use a predefined image style
GetObjectRequest request = new GetObjectRequest(bucketName, objectName);
request.setProcess("style/my-style-name");
OSSObject ossObject = ossClient.getObject(request);
```
