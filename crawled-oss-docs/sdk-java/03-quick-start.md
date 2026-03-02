# Java SDK - Quick Start

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/java-quick-start

## Complete Working Example

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.*;
import java.io.*;
import java.util.List;

public class OssQuickStart {
    public static void main(String[] args) {
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID");
        String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET");
        String bucketName = "my-example-bucket";
        String objectName = "example-object.txt";

        OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

        try {
            // 1. Create a bucket
            ossClient.createBucket(bucketName);
            System.out.println("Bucket created: " + bucketName);

            // 2. Upload an object (string content)
            String content = "Hello OSS! This is a quick start example.";
            ossClient.putObject(bucketName, objectName,
                new ByteArrayInputStream(content.getBytes()));
            System.out.println("Object uploaded: " + objectName);

            // 3. Download the object
            OSSObject ossObject = ossClient.getObject(bucketName, objectName);
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(ossObject.getObjectContent()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Content: " + line);
            }
            reader.close();
            ossObject.close();

            // 4. List objects in the bucket
            ObjectListing objectListing = ossClient.listObjects(bucketName);
            List<OSSObjectSummary> summaries = objectListing.getObjectSummaries();
            for (OSSObjectSummary summary : summaries) {
                System.out.println("Object: " + summary.getKey() +
                    " Size: " + summary.getSize());
            }

            // 5. Delete the object
            ossClient.deleteObject(bucketName, objectName);
            System.out.println("Object deleted: " + objectName);

            // 6. Delete the bucket
            ossClient.deleteBucket(bucketName);
            System.out.println("Bucket deleted: " + bucketName);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            ossClient.shutdown();
        }
    }
}
```

## V2 SDK Quick Start

```java
package com.example.oss;

import com.aliyun.sdk.service.oss2.OSSClient;
import com.aliyun.sdk.service.oss2.OSSClientBuilder;
import com.aliyun.sdk.service.oss2.credentials.CredentialsProvider;
import com.aliyun.sdk.service.oss2.credentials.EnvironmentVariableCredentialsProvider;
import com.aliyun.sdk.service.oss2.models.*;

public class QuickStartV2 {
    public static void main(String[] args) {
        String region = "cn-hangzhou";
        String bucket = "your-bucket-name";
        String key = "your-object-name";

        CredentialsProvider provider = new EnvironmentVariableCredentialsProvider();
        OSSClientBuilder clientBuilder = OSSClient.newBuilder()
                .credentialsProvider(provider)
                .region(region);

        try (OSSClient client = clientBuilder.build()) {
            String data = "hello world";

            PutObjectResult result = client.putObject(PutObjectRequest.newBuilder()
                    .bucket(bucket)
                    .key(key)
                    .body(BinaryData.fromString(data))
                    .build());

            System.out.printf("status code:%d, request id:%s, eTag:%s\n",
                    result.statusCode(), result.requestId(), result.eTag());

        } catch (Exception e) {
            System.out.printf("error:\n%s", e);
        }
    }
}
```
