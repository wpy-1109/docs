# How to quickly get started with OSS on CloudBox

Object Storage Service (OSS) on CloudBox allows you to monitor and process local data. OSS on CloudBox is suitable for scenarios that require low latency and unified management of multiple branches. This topic describes the basic operations of OSS on CloudBox, including creating an OSS on CloudBox bucket and uploading objects to and downloading objects from an OSS on CloudBox bucket.

## Prerequisites


-

OSS on CloudBox is supported only in the China (Hangzhou), China (Shanghai), China (Shenzhen), China (Heyuan), China (Beijing), and China (Chengdu) regions.

-

A cloud box is purchased. For more information, see [Purchase a cloud box](https://www.alibabacloud.com/help/en/cloud-box/getting-started/purchase-a-cloud-box#task-2231309).

-

A Virtual Private Cloud (VPC) and a vSwitch are created in the OSS on CloudBox. For more information, see [Create a VPC and a vSwitch](https://www.alibabacloud.com/help/en/vpc/user-guide/create-and-manage-a-vpc#section-znz-rbv-vrx).

-

A VPC internal network is set up, and a single tunnel is configured to provide secure connection. To apply for this feature, please contact [technical support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex).

## Step 1: Create an OSS on CloudBox bucket


Use the OSS console


-

Log on to the [OSS](https://oss.console.alibabacloud.com/) console.

-

In the left-side navigation pane, choose Data Service > OSS on CloudBox Buckets.

-

On the OSS on CloudBox Buckets page, click Create Bucket in the upper-left corner.

-

In the Create Bucket panel, specify the name of the OSS on CloudBox bucket, retain the default settings for other parameters, and then click OK.


The name of the OSS on CloudBox bucket must meet the following requirements:


-

The specified name of the OSS on CloudBox bucket cannot be the same as the name of an existing OSS on CloudBox bucket in the cloud box.

- The name can contain only lowercase letters, digits, and hyphens (-).
- The name must start and end with a lowercase letter or a digit.
- The name must be 3 to 63 characters in length.

Use OSS SDK for Java


You can create an OSS on CloudBox bucket only by using OSS SDK for Java. The version of OSS SDK for Java must be 3.15.0 or later.


`java
import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.model.CreateBucketRequest;
import com.aliyun.oss.common.auth.DefaultCredentialProvider;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.common.auth.CredentialsProviderFactory;
import com.aliyun.oss.common.auth.EnvironmentVariableCredentialsProvider;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // Specify the data endpoint of the OSS on CloudBox bucket.
        String endpoint = "https://cb-f8z7yvzgwfkl9q0h.cn-hangzhou.oss-cloudbox.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the OSS on CloudBox bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the region in which the OSS on CloudBox bucket is located.
        String region = "cn-hangzhou";
        // Specify the ID of the cloud box.
        String cloudBoxId = "cb-f8z7yvzgwfkl9q0h";


        // Create an OSSClient instance.
        ClientBuilderConfiguration conf = new ClientBuilderConfiguration();
        conf.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(new DefaultCredentialProvider(credentialsProvider.getCredentials()))
                .clientConfiguration(conf)
                .region(region)
                .cloudBoxId(cloudBoxId)
                .build();

        try {
            // Create a CreateBucketRequest object.
            CreateBucketRequest createBucketRequest = new CreateBucketRequest(bucketName);

            // Set the ACL of the OSS on CloudBox bucket to public-read. The default ACL is private.
            //createBucketRequest.setCannedACL(CannedAccessControlList.PublicRead);

            // Create the OSS on CloudBox bucket.
            ossClient.createBucket(createBucketRequest);
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
    }
}
`


Use ossutil


You can use ossutil to create an OSS on CloudBox bucket. For more information, see [put-bucket](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket#595bc9a51bbhb).


Use the OSS API


If your business requires a high level of customization, you can directly call RESTful APIs. To directly call a RESTful API, you must include the signature calculation in your code. For more information, see [PutBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#doc-api-Oss-PutBucket).

## Step 2: Upload an object


Use OSS SDK for Java


You can use only OSS SDK for Java to upload a local file to an OSS on CloudBox bucket. The version of OSS SDK for Java must be 3.15.0 or later. The following sample code provides an example on how to use OSS SDK for Java to upload a local file to an OSS on CloudBox bucket:


`java
import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.model.PutObjectRequest;
import java.io.File;
import com.aliyun.oss.common.auth.DefaultCredentialProvider;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.common.auth.CredentialsProviderFactory;
import com.aliyun.oss.common.auth.EnvironmentVariableCredentialsProvider;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // Specify the data endpoint of the OSS on CloudBox bucket.
        String endpoint = "https://cb-f8z7yvzgwfkl9q0h.cn-hangzhou.oss-cloudbox.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the OSS on CloudBox bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the region in which the OSS on CloudBox bucket is located.
        String region = "cn-hangzhou";
        // Specify the ID of the cloud box.
        String cloudBoxId = "cb-f8z7yvzgwfkl9q0h";
        // Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
        String objectName = "exampledir/exampleobject.txt";
        // Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt.
        // If the path of the local file is not specified, the local file is uploaded from the path of the project to which the sample program belongs.
        String filePath= "D:\\localpath\\examplefile.txt";

        // Create an OSSClient instance.
        ClientBuilderConfiguration conf = new ClientBuilderConfiguration();
        conf.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(new DefaultCredentialProvider(credentialsProvider.getCredentials()))
                .clientConfiguration(conf)
                .region(region)
                .cloudBoxId(cloudBoxId)
                .build();

        try {
            // Create a PutObjectRequest object.
            PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, objectName, new File(filePath));
            // The following sample code provides an example on how to specify the storage class and access control list (ACL) of an object when you upload the object:
            // ObjectMetadata metadata = new ObjectMetadata();
            // metadata.setHeader(OSSHeaders.OSS_STORAGE_CLASS, StorageClass.Standard.toString());
            // metadata.setObjectAcl(CannedAccessControlList.Private);
            // putObjectRequest.setMetadata(metadata);

            // Upload the local file.
            ossClient.putObject(putObjectRequest);
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
    }
}
`


Use ossutil


You can use ossutil to upload an object to an OSS on CloudBox bucket by using simple upload. For more information, see [Upload objects](https://www.alibabacloud.com/help/en/oss/developer-reference/cp-upload-file#ab9857b49etf7).


Use the OSS API


If your business requires a high level of customization, you can directly call the RESTful APIs. To directly call an API, you must include the signature calculation in your code. For more information, see [PutObject](https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb).

## Step 3: Download an object


Use OSS SDK for Java


You can download objects from an OSS on CloudBox bucket by using only OSS SDK for Java. The version of OSS SDK for Java must be 3.15.0 or later. The following sample code provides an example on how to download an object by using OSS SDK for Java:


`java
package com.aliyun.oss.demo;

import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.model.GetObjectRequest;
import java.io.File;
import com.aliyun.oss.common.auth.DefaultCredentialProvider;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.common.auth.CredentialsProviderFactory;
import com.aliyun.oss.common.auth.EnvironmentVariableCredentialsProvider;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // Specify the data endpoint of the OSS on CloudBox bucket.
        String endpoint = "https://cb-f8z7yvzgwfkl9q0h.cn-hangzhou.oss-cloudbox.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the OSS on CloudBox bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the region in which the OSS on CloudBox bucket is located.
        String region = "cn-hangzhou";
        // Specify the ID of the cloud box.
        String cloudBoxId = "cb-f8z7yvzgwfkl9q0h";
        // Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
        String objectName = "exampledir/exampleobject.txt";
        // Specify the full path of the local file.
        String pathName = "D:\\localpath\\examplefile.txt";

        // Create an OSSClient instance.
        ClientBuilderConfiguration conf = new ClientBuilderConfiguration();
        conf.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(new DefaultCredentialProvider(credentialsProvider.getCredentials()))
                .clientConfiguration(conf)
                .region(region)
                .cloudBoxId(cloudBoxId)
                .build();

        try {
            // Download the object as a local file in the specified path. If a file that has the same name already exists in the path, the downloaded object overwrites the file. Otherwise, the downloaded object is saved in the path.
            // If you do not specify a local path for the downloaded object, the downloaded object is saved to the path of the project to which the sample program belongs.
            ossClient.getObject(new GetObjectRequest(bucketName, objectName), new File(pathName));
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
    }
}
`


Use ossutil


You can use ossutil to upload an object to an OSS on CloudBox bucket by using simple upload. For more information, see [Download objects](https://www.alibabacloud.com/help/en/oss/developer-reference/cp-download-file#7449fac053umg).


Use the OSS API


If your business requires a high level of customization, you can directly call the RESTful APIs. To directly call an API, you must include the signature calculation in your code. For more information, see [GetObject](https://www.alibabacloud.com/help/en/oss/developer-reference/getobject#concept-dcn-tp1-kfb).

Thank you! We've received your  feedback.