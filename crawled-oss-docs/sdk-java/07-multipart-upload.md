# Java SDK - Multipart Upload

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-12

## Overview

Multipart upload is recommended for files larger than 5 GB (up to 48.8 TB). The process involves:
1. **Initiate** - Start the multipart upload and get an upload ID
2. **Upload Parts** - Upload the file in parts (minimum 100 KB each, except the last)
3. **Complete** - Combine all parts into a single object

## V1 SDK - Complete Multipart Upload Example

```java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.internal.Mimetypes;
import com.aliyun.oss.model.*;
import java.io.*;
import java.util.*;

public class MultipartUploadExample {
    public static void main(String[] args) throws Exception {
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        String region = "cn-hangzhou";
        EnvironmentVariableCredentialsProvider credentialsProvider =
            CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        String bucketName = "examplebucket";
        String objectName = "exampleobject.txt";
        String filePath = "/path/to/large/file.txt";

        // Create client with V4 signature
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(credentialsProvider)
                .clientConfiguration(clientBuilderConfiguration)
                .region(region)
                .build();

        try {
            // Step 1: Initiate multipart upload
            InitiateMultipartUploadRequest initRequest =
                new InitiateMultipartUploadRequest(bucketName, objectName);
            ObjectMetadata metadata = new ObjectMetadata();
            metadata.setContentType(
                Mimetypes.getInstance().getMimetype(new File(filePath), objectName));
            initRequest.setObjectMetadata(metadata);

            InitiateMultipartUploadResult initResult =
                ossClient.initiateMultipartUpload(initRequest);
            String uploadId = initResult.getUploadId();

            // Step 2: Upload parts
            List<PartETag> partETags = new ArrayList<>();
            long partSize = 5 * 1024 * 1024L; // 5MB per part

            File sampleFile = new File(filePath);
            long fileLength = sampleFile.length();
            int partCount = (int) (fileLength / partSize);
            if (fileLength % partSize != 0) {
                partCount++;
            }

            for (int i = 0; i < partCount; i++) {
                long startPos = i * partSize;
                long curPartSize = (i + 1 == partCount)
                    ? (fileLength - startPos) : partSize;

                InputStream inStream = new FileInputStream(filePath);
                inStream.skip(startPos);

                UploadPartRequest uploadPartRequest = new UploadPartRequest();
                uploadPartRequest.setBucketName(bucketName);
                uploadPartRequest.setKey(objectName);
                uploadPartRequest.setUploadId(uploadId);
                uploadPartRequest.setInputStream(inStream);
                uploadPartRequest.setPartSize(curPartSize);
                uploadPartRequest.setPartNumber(i + 1);

                UploadPartResult uploadPartResult =
                    ossClient.uploadPart(uploadPartRequest);
                partETags.add(uploadPartResult.getPartETag());
                inStream.close();
            }

            // Step 3: Complete multipart upload
            CompleteMultipartUploadRequest completeRequest =
                new CompleteMultipartUploadRequest(
                    bucketName, objectName, uploadId, partETags);
            ossClient.completeMultipartUpload(completeRequest);

            System.out.println("Multipart upload completed successfully!");

        } catch (OSSException oe) {
            System.out.println("Error Message:" + oe.getErrorMessage());
            System.out.println("Error Code:" + oe.getErrorCode());
            System.out.println("Request ID:" + oe.getRequestId());
        } catch (ClientException ce) {
            System.out.println("Error Message:" + ce.getMessage());
        } finally {
            ossClient.shutdown();
        }
    }
}
```

## V2 SDK - Multipart Upload

```java
import com.aliyun.sdk.service.oss2.OSSClient;
import com.aliyun.sdk.service.oss2.models.*;
import com.aliyun.sdk.service.oss2.transport.BinaryData;
import com.aliyun.sdk.service.oss2.io.BoundedInputStream;
import com.aliyun.sdk.service.oss2.credentials.EnvironmentVariableCredentialsProvider;
import java.io.*;
import java.util.*;

String region = "cn-hangzhou";
String bucket = "my-bucket";
String key = "large-files/video.mp4";
String filePath = "/path/to/large/file.mp4";
CredentialsProvider provider = new EnvironmentVariableCredentialsProvider();

try (OSSClient client = OSSClient.newBuilder()
        .credentialsProvider(provider)
        .region(region)
        .build()) {

    // Step 1: Initiate multipart upload
    InitiateMultipartUploadResult initResult = client.initiateMultipartUpload(
        InitiateMultipartUploadRequest.newBuilder()
            .bucket(bucket)
            .key(key)
            .build());
    String uploadId = initResult.initiateMultipartUpload().uploadId();

    // Step 2: Upload parts
    File file = new File(filePath);
    long fileSize = file.length();
    long partSize = 5 * 1024 * 1024; // 5MB per part
    List<Part> parts = new ArrayList<>();
    int partNumber = 1;

    for (long start = 0; start < fileSize; start += partSize) {
        long currentPartSize = Math.min(partSize, fileSize - start);
        try (InputStream is = new FileInputStream(file)) {
            is.skip(start);
            BoundedInputStream boundedStream = new BoundedInputStream(is, currentPartSize);

            UploadPartResult partResult = client.uploadPart(
                UploadPartRequest.newBuilder()
                    .bucket(bucket)
                    .key(key)
                    .uploadId(uploadId)
                    .partNumber((long) partNumber)
                    .body(BinaryData.fromStream(boundedStream))
                    .build());

            parts.add(Part.newBuilder()
                .partNumber((long) partNumber)
                .eTag(partResult.eTag())
                .build());
            partNumber++;
        }
    }

    // Step 3: Complete multipart upload
    CompleteMultipartUploadResult completeResult = client.completeMultipartUpload(
        CompleteMultipartUploadRequest.newBuilder()
            .bucket(bucket)
            .key(key)
            .uploadId(uploadId)
            .completeMultipartUpload(
                CompleteMultipartUpload.newBuilder()
                    .parts(parts)
                    .build())
            .build());

    System.out.printf("Multipart upload completed: statusCode=%d, eTag=%s\n",
        completeResult.statusCode(), completeResult.completeMultipartUpload().eTag());
}
```

## Resumable Upload

For uploads that may be interrupted:

```java
UploadFileRequest uploadFileRequest = new UploadFileRequest(bucketName, objectName);
uploadFileRequest.setUploadFile(filePath);
uploadFileRequest.setPartSize(1024 * 1024);     // 1MB per part
uploadFileRequest.setTaskNum(10);                // 10 concurrent threads
uploadFileRequest.setEnableCheckpoint(true);     // Enable checkpoint for resume
uploadFileRequest.setCheckpointFile("/path/to/checkpoint/file");

UploadFileResult result = ossClient.uploadFile(uploadFileRequest);
```

## Abort Multipart Upload

```java
AbortMultipartUploadRequest abortRequest =
    new AbortMultipartUploadRequest(bucketName, objectName, uploadId);
ossClient.abortMultipartUpload(abortRequest);
```

## List Multipart Uploads

```java
// List uploaded parts
ListPartsRequest listPartsRequest =
    new ListPartsRequest(bucketName, objectName, uploadId);
PartListing partListing = ossClient.listParts(listPartsRequest);
for (PartSummary part : partListing.getParts()) {
    System.out.printf("Part: %d, Size: %d, ETag: %s\n",
        part.getPartNumber(), part.getSize(), part.getETag());
}

// List all ongoing multipart uploads
ListMultipartUploadsRequest listRequest =
    new ListMultipartUploadsRequest(bucketName);
MultipartUploadListing listing = ossClient.listMultipartUploads(listRequest);
for (MultipartUpload upload : listing.getMultipartUploads()) {
    System.out.printf("Key: %s, UploadId: %s\n",
        upload.getKey(), upload.getUploadId());
}
```
