# Java SDK - Presigned URLs

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/authorize-access-3

## Generate Presigned Download URL (GET)

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import java.net.URL;
import java.util.Date;

OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

// Set expiration to 1 hour from now
Date expiration = new Date(System.currentTimeMillis() + 3600 * 1000);

URL signedUrl = ossClient.generatePresignedUrl(bucketName, objectName, expiration);
System.out.println("Signed GET URL: " + signedUrl.toString());

ossClient.shutdown();
```

## Generate Presigned Upload URL (PUT)

```java
import com.aliyun.oss.model.GeneratePresignedUrlRequest;
import com.aliyun.oss.HttpMethod;

GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(
    bucketName, objectName, HttpMethod.PUT);
request.setExpiration(new Date(System.currentTimeMillis() + 3600 * 1000));
request.setContentType("application/octet-stream");

URL signedUrl = ossClient.generatePresignedUrl(request);
System.out.println("Signed PUT URL: " + signedUrl.toString());
```

## Presigned URL with Custom Headers

```java
GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(
    bucketName, objectName);
request.setMethod(HttpMethod.PUT);
request.setExpiration(new Date(System.currentTimeMillis() + 3600 * 1000));

Map<String, String> headers = new HashMap<>();
headers.put("Content-Type", "text/plain");
request.setHeaders(headers);

URL signedUrl = ossClient.generatePresignedUrl(request);
```

## Presigned URL with Callback

```java
import com.aliyun.oss.internal.OSSHeaders;
import java.util.Base64;

String callbackUrl = "http://www.example.com/callback";
String callbackBody = "{\"callbackUrl\":\"" + callbackUrl +
    "\",\"callbackBody\":\"bucket=${bucket}&object=${object}&my_var_1=${x:var1}\"}";
String callbackBase64 = Base64.getEncoder().encodeToString(callbackBody.getBytes());

String callbackVarJson = "{\"x:var1\":\"value1\",\"x:var2\":\"value2\"}";
String callbackVarBase64 = Base64.getEncoder().encodeToString(callbackVarJson.getBytes());

Map<String, String> headers = new HashMap<>();
headers.put(OSSHeaders.OSS_HEADER_CALLBACK, callbackBase64);
headers.put(OSSHeaders.OSS_HEADER_CALLBACK_VAR, callbackVarBase64);

GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(
    bucketName, objectName);
request.setMethod(HttpMethod.PUT);
request.setExpiration(new Date(System.currentTimeMillis() + 3600 * 1000));
request.setHeaders(headers);

URL url = ossClient.generatePresignedUrl(request);
```

## Presigned URL for Multipart Upload

You can generate presigned URLs for each part in a multipart upload:

```java
// 1. Initiate multipart upload
InitiateMultipartUploadRequest initRequest =
    new InitiateMultipartUploadRequest(bucketName, objectName);
InitiateMultipartUploadResult initResult = ossClient.initiateMultipartUpload(initRequest);
String uploadId = initResult.getUploadId();

// 2. Generate presigned URL for each part
long expireTime = 3600 * 1000L;
Map<String, String> headers = new HashMap<>();

for (int i = 0; i < partCount; i++) {
    String signUrl = getSignUrl(ossClient, bucketName, objectName,
        HttpMethod.PUT, expireTime, i + 1, uploadId, headers);
    // Use signUrl to upload part via HTTP PUT
}
```

## Using Presigned URLs with HTTP Clients

Once you have a presigned URL, any HTTP client can use it:

```java
// Example: Upload using Apache HttpClient
CloseableHttpClient httpClient = HttpClients.createDefault();
HttpPut httpPut = new HttpPut(signedUrl.toString());
httpPut.setEntity(new FileEntity(new File(filePath)));
httpPut.setHeader("Content-Type", "application/octet-stream");

CloseableHttpResponse response = httpClient.execute(httpPut);
System.out.println("Response: " + response.getStatusLine().getStatusCode());
httpClient.close();
```
