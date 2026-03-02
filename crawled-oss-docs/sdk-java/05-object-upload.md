# Java SDK - Object Upload

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/simple-upload-11

## Simple Upload (PutObject)

Suitable for files **up to 5 GB** in size. For larger files, use multipart upload.

### Upload a Local File

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.PutObjectRequest;
import java.io.File;

public class SimpleUploadExample {
    public static void main(String[] args) {
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        String accessKeyId = "<yourAccessKeyId>";
        String accessKeySecret = "<yourAccessKeySecret>";
        String bucketName = "<yourBucketName>";
        String objectName = "exampledir/exampleobject.txt";
        String filePath = "/path/to/local/file.txt";

        OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

        try {
            PutObjectRequest putObjectRequest = new PutObjectRequest(
                bucketName, objectName, new File(filePath));
            ossClient.putObject(putObjectRequest);
            System.out.println("File uploaded successfully.");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            ossClient.shutdown();
        }
    }
}
```

### Upload a String (InputStream)

```java
String content = "Hello OSS! This is a simple upload example.";
ossClient.putObject(bucketName, objectName,
    new ByteArrayInputStream(content.getBytes()));
```

### Upload with Metadata

```java
import com.aliyun.oss.model.ObjectMetadata;
import com.aliyun.oss.model.PutObjectRequest;

ObjectMetadata metadata = new ObjectMetadata();
metadata.setContentType("image/jpeg");
metadata.addUserMetadata("x-oss-meta-author", "example-user");

PutObjectRequest putObjectRequest = new PutObjectRequest(
    bucketName, objectName, new File(filePath));
putObjectRequest.setMetadata(metadata);

ossClient.putObject(putObjectRequest);
```

### V2 SDK - Upload

```java
String data = "hello world";

PutObjectResult result = client.putObject(PutObjectRequest.newBuilder()
    .bucket(bucket)
    .key(key)
    .body(BinaryData.fromString(data))
    .build());

System.out.printf("status code:%d, request id:%s, eTag:%s\n",
    result.statusCode(), result.requestId(), result.eTag());
```

## Append Upload

Appends data to an existing object. The object type becomes Appendable.

```java
AppendObjectRequest appendObjectRequest = new AppendObjectRequest(
    bucketName, objectName,
    new ByteArrayInputStream("first part".getBytes()));
appendObjectRequest.setPosition(0L);

AppendObjectResult appendResult = ossClient.appendObject(appendObjectRequest);

// Append more data
appendObjectRequest = new AppendObjectRequest(
    bucketName, objectName,
    new ByteArrayInputStream("second part".getBytes()));
appendObjectRequest.setPosition(appendResult.getNextPosition());

ossClient.appendObject(appendObjectRequest);
```

## Upload with Progress Callback

```java
ossClient.putObject(new PutObjectRequest(bucketName, objectName, new File(filePath))
    .withProgressListener(new ProgressListener() {
        @Override
        public void progressChanged(ProgressEvent progressEvent) {
            long bytes = progressEvent.getBytes();
            System.out.println("Bytes transferred: " + bytes);
        }
    }));
```

## Upload with Server Callback

```java
PutObjectRequest put = new PutObjectRequest(bucketName, objectName, filePath);

Map<String, String> callbackParams = new HashMap<>();
callbackParams.put("callbackUrl", "http://oss-demo.aliyuncs.com:23450");
callbackParams.put("callbackHost", "yourCallbackHost");
callbackParams.put("callbackBodyType", "application/json");
callbackParams.put("callbackBody", "{\"mimeType\":${mimeType},\"size\":${size}}");
put.setCallbackParam(callbackParams);

ossClient.putObject(put);
```

## Key Parameters

| Parameter | Description |
|-----------|-------------|
| `endpoint` | The region-specific OSS endpoint |
| `bucketName` | The name of the target bucket |
| `objectName` | The full object key (path + filename) in OSS |
| `filePath` / `InputStream` | The data source to upload |
| `ObjectMetadata` | Optional metadata (Content-Type, user-defined headers) |

## Important Notes

- **Max size**: 5 GB per single `PutObject` call
- **Overwrites**: If an object with the same name exists, it will be overwritten
- **Authentication**: Use AccessKey ID/Secret, STS tokens, or RAM roles
