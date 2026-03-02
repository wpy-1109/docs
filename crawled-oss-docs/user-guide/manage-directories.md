# Manage OSS directories

To simplify the organization and management of large numbers of objects, which can be difficult in a flat structure, Object Storage Service (OSS) offers the directory feature that simulates a folder structure.

## How it works


OSS uses a flat storage structure and does not have real folders. The directories you see in the console are not physical folders but visual representations created based on the `/` separator in object names.


For example, when you see the following hierarchical structure in the console:


`plaintext
examplebucket
    └── log/
       ├── date1.txt
       ├── date2.txt
       ├── date3.txt
    └── destfolder/
       └── 2021/
          ├── photo.jpg
`


OSS actually stores only these objects:


`plaintext
log/date1.txt
log/date2.txt
destfolder/2021/photo.jpg
`


## Create a directory


You can create a directory in two ways:


-

Automatic creation when you upload an object: When you upload an object whose name contains a path, OSS automatically creates the corresponding directory.

-

Manual creation of an empty directory: This operation creates a zero-byte object with a name ending in `/` that serves as a placeholder for the empty directory.

## Console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/), and navigate to the Object Management > Objects page of the target bucket.

-

Click Create Directory.

-

Enter a Directory Name and click OK.


Follow these naming rules for directories:


-

The directory name must be UTF-8 encoded and cannot contain emojis.

-

Forward slashes (`/`) are used in a directory name to indicate subdirectories. Use forward slashes (`/`) in a directory name to create a nested directory structure. The directory name cannot start with a forward slash (`/`) or a backslash (`\`). The directory name cannot contain consecutive forward slashes (`//`).

-

The subdirectory name cannot be two consecutive periods (`..`).

-

The directory name must be 1 to 254 characters in length.

## ossutil


The following example shows how to create a directory named `dir/` in the `examplebucket` bucket.


`bash
ossutil mkdir oss://examplebucket/dir
`


For more information, see [mkdir (create a directory)](https://www.alibabacloud.com/help/en/oss/developer-reference/mkdir-create-directory#c557acd62dc2b).

## SDK


The following code provides examples of how to create a directory using common SDKs. For more information about how to create a directory using other SDKs, see [Introduction to OSS SDKs](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import java.io.ByteArrayInputStream;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // The China (Hangzhou) region is used as an example for the endpoint. Specify the endpoint based on your actual region.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Do not hardcode your access credentials in your code. Leaked credentials can compromise the security of all your resources. This example gets credentials from environment variables. Configure the environment variables before running the code.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Set bucketName to the name of your bucket, for example, examplebucket.
        String bucketName = "examplebucket";
        // Set dirName to the name of the directory created using method 1.
        String dirName = "exampledir/";
        // Set dirName2 to the name of the directory created using method 2.
        String dirName2 = "exampledir1/";

        // Create an OSSClient instance.
        OSS ossClient = new OSSClientBuilder().build(endpoint, credentialsProvider);

        try {
            // Method 1: Create a directory by calling the createDirectory operation. Before you use this method, you must enable hierarchical namespace.
            ossClient.createDirectory(bucketName, dirName);

            // Method 2: Create a directory by uploading an empty string.
            ossClient.putObject(bucketName, dirName2, new ByteArrayInputStream("".getBytes()));
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

PHP

`php
<?php
if (is_file(__DIR__ . '/../autoload.php')) {
    require_once __DIR__ . '/../autoload.php';
}
if (is_file(__DIR__ . '/../vendor/autoload.php')) {
    require_once __DIR__ . '/../vendor/autoload.php';
}

use OSS\Credentials\EnvironmentVariableCredentialsProvider;
use OSS\OssClient;
use OSS\CoreOssException;
// Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
$provider = new EnvironmentVariableCredentialsProvider();
// Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
$endpoint = "yourEndpoint";
// Set bucket to the name of your bucket, for example, examplebucket.
$bucket= "examplebucket";
// Set object to the directory name. The name must end with a forward slash (/).
$object = "exampledir/";
$content = "";
try{
    $config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
    );
    $ossClient = new OssClient($config);

    $ossClient->putObject($bucket, $object, $content);
} catch(OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}
print(__FUNCTION__ . "OK" . "\n");

// You can set headers when you upload an object, such as setting the access permission to private or specifying custom metadata.
$options = array(
    OssClient::OSS_HEADERS => array(
        'x-oss-object-acl' => 'private',
        'x-oss-meta-info' => 'your info'
    ),
);
try{
    $config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
    );
    $ossClient = new OssClient($config);

    $ossClient->putObject($bucket, $object, $content, $options);
} catch(OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}
print(__FUNCTION__ . "OK" . "\n");
`

Node.js

`nodejs
const OSS = require('ali-oss');

const client = new OSS({
  // Set yourregion to the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourregion',
  // Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Set bucket to the name of your bucket.
  bucket: 'examplebucket',
});

async function putBuffer () {
  try {
    // Set the directory name. The name must end with a forward slash (/).
    const result = await client.put('exampledir/', new Buffer(''));
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

putBuffer();
`

Python

`python
# -*- coding: utf-8 -*-

import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
# Set the bucket name.
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'examplebucket')

# Set the directory name. The name must end with a forward slash (/).
bucket.put_object('exampledir/', '')
`

C#

`csharp
using System.Text;
using Aliyun.OSS;

// Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "yourEndpoint";
// Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Set bucketName to the name of your bucket, for example, examplebucket.
var bucketName = "examplebucket";
// Set objectName to the directory name. The name must end with a forward slash (/).
var objectName = "exampledir/";
var objectContent = "";

// Create an OssClient instance.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret);
try
{
    bytebinaryData = Encoding.ASCII.GetBytes(objectContent);
    MemoryStream requestContent = new MemoryStream(binaryData);
    // Create the directory.
    client.PutObject(bucketName, objectName, requestContent);
    Console.WriteLine("Put object succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
`

C

`c
#include "oss_api.h"
#include "aos_http_io.h"
/* Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
const char *endpoint = "yourEndpoint";

/* Set bucket_name to the name of your bucket, for example, examplebucket. */
const char *bucket_name = "examplebucket";
/* Set object_name to the directory name. The name must end with a forward slash (/). */
const char *object_name = "exampledir/";
const char *object_content = "";
void init_options(oss_request_options_t *options)
{
    options->config = oss_config_create(options->pool);
    /* Initialize the aos_string_t type with a char* string. */
    aos_str_set(&options->config->endpoint, endpoint);
    /* Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set. */
    aos_str_set(&options->config->access_key_id, getenv("OSS_ACCESS_KEY_ID"));
    aos_str_set(&options->config->access_key_secret, getenv("OSS_ACCESS_KEY_SECRET"));
    /* Specify whether a CNAME is used. 0 indicates that no CNAME is used. */
    options->config->is_cname = 0;
    /* Set network parameters, such as the timeout period. */
    options->ctl = aos_http_controller_create(options->pool, 0);
}
int main(int argc, char *argv)
{
    /* Call the aos_http_io_initialize method at the program entry to initialize global resources such as the network and memory. */
    if (aos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }
    /* The memory pool (pool) is used for memory management. It is equivalent to apr_pool_t. The implementation code is in the apr library. */
    aos_pool_t *pool;
    /* Create a memory pool. The second parameter is NULL, which indicates that the memory pool does not inherit from another memory pool. */
    aos_pool_create(&pool, NULL);
    /* Create and initialize options. This parameter includes global configuration information such as endpoint, access_key_id, access_key_secret, is_cname, and curl. */
    oss_request_options_t *oss_client_options;
    /* Allocate memory to options in the memory pool. */
    oss_client_options = oss_request_options_create(pool);
    /* Initialize the client option oss_client_options. */
    init_options(oss_client_options);
    /* Initialize parameters. */
    aos_string_t bucket;
    aos_string_t object;
    aos_list_t buffer;
    aos_buf_t *content = NULL;
    aos_table_t *headers = NULL;
    aos_table_t *resp_headers = NULL;
    aos_status_t *resp_status = NULL;
    aos_str_set(&bucket, bucket_name);
    aos_str_set(&object, object_name);
    aos_list_init(&buffer);
    content = aos_buf_pack(oss_client_options->pool, object_content, strlen(object_content));
    aos_list_add_tail(&content->node, &buffer);
    /* Upload the file. */
    resp_status = oss_put_object_from_buffer(oss_client_options, &bucket, &object, &buffer, headers, &resp_headers);
    /* Check whether the upload was successful. */
    if (aos_status_is_ok(resp_status)) {
        printf("put object from buffer succeeded\n");
    } else {
        printf("put object from buffer failed\n");
    }
    /* Destroy the memory pool. This is equivalent to releasing the memory allocated to resources during the request. */
    aos_pool_destroy(pool);
    /* Release the previously allocated global resources. */
    aos_http_io_deinitialize();
    return 0;
}
`


## Rename a directory


Renaming a directory is not a single atomic operation. All tools use the same underlying workflow:


-

Copy: Recursively copy all objects from the source directory to the destination directory.

-

Delete: After confirming that the copy operation is successful, permanently delete the source directory and all objects within it.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Because renaming requires copying and deleting every object in the directory, this operation can be time-consuming for large directories and incur significant costs for API calls and data transfer. Evaluate the impact carefully before proceeding.


-

If the hierarchical namespace feature is enabled, rename a directory directly.

## Console


-

Log on to the [OSS](https://oss.console.alibabacloud.com/) console.

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left-side navigation tree, choose Object Management > Objects.

-

Rename or move the directory.


Delete a directory by specifying its name in the prefix option of the ossutil [rm](https://www.alibabacloud.com/help/en/oss/developer-reference/rm-deleted#92f2e900803ke) command.








![edit](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9779712261/p277398.png)





-



-




| Use case | Action |
| --- | --- |
| Rename a directory | Hover over the target directory, click the icon, and rename the directory. The directory name cannot start with a forward slash (/). |
| Move a directory | To move a directory, you provide a new name that specifies the target path. If the new name starts with a forward slash (/), it is treated as an absolute path from the bucket's root directory. Enter the target directory as needed:To move the subdirectory subdir from the parent directory destdir to the parent directory destfolder, enter /destfolder/subdir as the new name.To move the subdirectory subdir from the parent directory destdir to the Bucket's root directory, enter /subdir as the new name. |


## SDK


Renaming directories is only supported using the Java SDK, which requires version 3.12.0 or later.


`java
import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.model.*;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
        String endPoint = "yourEndpoint";
        // Do not hardcode your access credentials in your code. Leaked credentials can compromise the security of all your resources. This example gets credentials from environment variables. Configure the environment variables before running the code.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Set bucketName to the name of your bucket, for example, examplebucket.
        String bucketName = "examplebucket";
        // Set sourceDir to the absolute path of the source directory. The absolute path cannot contain the bucket name.
        String sourceDir = "exampledir";
        // Set destinationDir to the absolute path of the destination directory, which must be in the same bucket as the source directory. The absolute path cannot contain the bucket name.
        String destinationDir = "newexampledir";

        // Create an OSSClient instance.
        OSS ossClient = new OSSClientBuilder().build(endPoint, credentialsProvider);

        try {
            // Rename the source directory in the bucket to the destination directory.
            RenameObjectRequest renameObjectRequest = new RenameObjectRequest(bucketName, sourceDir, destinationDir);
            ossClient.renameObject(renameObjectRequest);
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


## API


If your application has high customization requirements, make REST API requests. To do this, you must manually write code to calculate the signature. For more information, see [RenameObject](https://www.alibabacloud.com/help/en/oss/developer-reference/rename#concept-2057575).

-

If the hierarchical namespace feature is disabled, list all objects in the directory, copy them to a new prefix, then delete the source objects to rename the directory.


> NOTE:

> NOTE: 


> NOTE: Note 

To copy many objects, use Data Online Migration for batch copy operations. For more information, see [Migrate data between Alibaba Cloud OSS buckets](https://www.alibabacloud.com/help/en/data-online-migration/user-guide/tutorial-for-data-migration-between-oss-buckets/).


## ossutil


When using ossutil, manually perform the copy and delete steps to complete the renaming process.


-

Copy objects
Use the [cp](https://www.alibabacloud.com/help/en/oss/developer-reference/cp-1) command with the `--recursive (-r)` option to copy all content from the `old-dir/` directory to the `new-dir/` directory in the `examplebucket` bucket.


`bash
ossutil cp oss://examplebucket/old-dir/ oss://examplebucket/new-dir/ -r
`


-

(Optional) Verify the copy operation
Use the [ls](https://www.alibabacloud.com/help/en/oss/developer-reference/ls-list-resources-under-the-account-level) command to check the new directory and ensure that all objects are copied successfully.


`bash
ossutil ls oss://examplebucket/new-dir/
`


-

Delete the source directory
After you confirm that the copy operation is successful, use the [rm](https://www.alibabacloud.com/help/en/oss/developer-reference/rm-deleted) command with the `--recursive (-r) ` option to delete the source directory `old-dir/`.


> WARNING:

> NOTE: 


> NOTE: Warning 

This operation permanently deletes the `old-dir/` directory and all objects in it. Deleted data cannot be recovered. Proceed with caution.


`bash
ossutil rm oss://examplebucket/old-dir/ -r
`


## SDK


As described, renaming a directory using an SDK requires you to combine multiple API calls. For implementation details, see the SDK documentation for the following core operations:


-

[List objects](https://www.alibabacloud.com/help/en/oss/user-guide/list-objects-18)

-

[Copy objects](https://www.alibabacloud.com/help/en/oss/user-guide/copy-objects-16)

-

[Delete objects](https://www.alibabacloud.com/help/en/oss/user-guide/delete-objects-18)

## API


To rename a directory using the API, combine the following API calls:


-

Copy: [CopyObject](https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject)

-

List: [ListObjectsV2 (GetBucketV2)](https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects-v2)

-

Delete: [DeleteObject](https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject)


## Delete a directory


> WARNING:

> NOTE: 


> NOTE: Warning 

Deleting a directory also deletes all its subdirectories and objects. Proceed with caution.


## Console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

Navigate to the Object Management > Objects page of the target bucket.

-

Select the directory to delete and click Permanently Delete in the Actions column.

-

In the dialog box that appears, click OK.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Do not refresh or close the page while the deletion task is in progress, as this will interrupt the operation.


## ossutil


The following example shows how to delete the directory `test/` from the `examplebucket` bucket.


`bash
ossutil rm oss://examplebucket/test/ -r
`


For more information, see [rm](https://www.alibabacloud.com/help/en/oss/developer-reference/rm-deleted).

## SDK


Delete a directory and all its objects by specifying a `Prefix`. For example, to delete the `log` directory and all its objects from the `examplebucket` bucket, set the `Prefix` parameter in the sample code to `log/`.
Java

`java
import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.model.*;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.ArrayList;
import java.util.List;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // The China (Hangzhou) region is used as an example for the endpoint. Specify the endpoint based on your actual region.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Do not hardcode your access credentials in your code. Leaked credentials can compromise the security of all your resources. This example gets credentials from environment variables. Configure the environment variables before running the code.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Set bucketName to the name of your bucket, for example, examplebucket.
        String bucketName = "examplebucket";
        // Set directoryName to the absolute path of the directory. The absolute path cannot contain the bucket name.
        String directoryName = "exampledir";
        // Set prefix to the full path of the directory to delete. The full path cannot contain the bucket name.
        final String prefix = "log/";

        // Create an OSSClient instance.
        OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

        try {
            // Method 1: Recursively delete a directory by calling the deleteDirectory operation. Before you use this method, you must enable hierarchical namespace.
            DeleteDirectoryRequest deleteDirectoryRequest = new DeleteDirectoryRequest(bucketName, directoryName);
            deleteDirectoryRequest.setDeleteRecursive(true);
            DeleteDirectoryResult deleteDirectoryResult = ossClient.deleteDirectory(deleteDirectoryRequest);

            // View the deletion result.
            // A maximum of 100 directories and files can be deleted at a time. If not all items are deleted in one go, the server returns a nextDeleteToken. You can use this token to continue deleting the remaining data.
            // The nextDeleteToken is used by the server to find the starting point for the next deletion.
            String nextDeleteToken = deleteDirectoryResult.getNextDeleteToken();
            System.out.println("delete next token:" + nextDeleteToken);
            // The absolute path of the deleted directory.
            System.out.println("delete dir name :" + deleteDirectoryResult.getDirectoryName());
            // The total number of files and directories deleted this time.
            System.out.println("delete number:" + deleteDirectoryResult.getDeleteNumber());


            // Method 2: Delete the directory and all files in it by traversing the results of listObjects.
            String nextMarker = null;
            ObjectListing objectListing = null;
            do {
                ListObjectsRequest listObjectsRequest = new ListObjectsRequest(bucketName)
                        .withPrefix(prefix)
                        .withMarker(nextMarker);

                objectListing = ossClient.listObjects(listObjectsRequest);
                if (objectListing.getObjectSummaries().size() > 0) {
                    List<String> keys = new ArrayList<String>();
                    for (OSSObjectSummary s : objectListing.getObjectSummaries()) {
                        System.out.println("key name: " + s.getKey());
                        keys.add(s.getKey());
                    }
                    DeleteObjectsRequest deleteObjectsRequest = new DeleteObjectsRequest(bucketName).withKeys(keys).withEncodingType("url");
                    DeleteObjectsResult deleteObjectsResult = ossClient.deleteObjects(deleteObjectsRequest);
                    List<String> deletedObjects = deleteObjectsResult.getDeletedObjects();
                    try {
                        for(String obj : deletedObjects) {
                            String deleteObj =  URLDecoder.decode(obj, "UTF-8");
                            System.out.println(deleteObj);
                        }
                    } catch (UnsupportedEncodingException e) {
                        e.printStackTrace();
                    }
                }

                nextMarker = objectListing.getNextMarker();
            } while (objectListing.isTruncated());
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

PHP

`php
<?php
if (is_file(__DIR__ . '/../autoload.php')) {
   require_once __DIR__ . '/../autoload.php';
}
if (is_file(__DIR__ . '/../vendor/autoload.php')) {
   require_once __DIR__ . '/../vendor/autoload.php';
}

use OSS\OssClient;
use OSS\Core\OssException;
// Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
$accessKeyId = getenv("OSS_ACCESS_KEY_ID");
$accessKeySecret = getenv("OSS_ACCESS_KEY_SECRET");
// Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
$endpoint = "yourEndpoint";
// Set the bucket name.
$bucket = "examplebucket";

try {
   $ossClient = new OssClient($accessKeyId, $accessKeySecret, $endpoint, false);
   $option = array(
      OssClient::OSS_MARKER => null,
      // Set OSS_PREFIX to the full path of the directory to delete. The full path cannot contain the bucket name.
      OssClient::OSS_PREFIX => "log/",
      OssClient::OSS_DELIMITER=>'',
   );
   $bool = true;
   while ($bool){
      $result = $ossClient->listObjects($bucket,$option);
      $objects = array();
      if(count($result->getObjectList()) > 0){
         foreach ($result->getObjectList() as $key => $info){
            printf("key name:".$info->getKey().PHP_EOL);
            $objects= $info->getKey();
         }
         // Delete the directory and all files in it.
         $delObjects = $ossClient->deleteObjects($bucket, $objects);
         foreach ($delObjects as $info){
            $obj = strval($info);
            printf("Delete ".$obj." : Success" . PHP_EOL);
         }
      }

      if($result->getIsTruncated() === 'true'){
         $option[OssClient::OSS_MARKER] = $result->getNextMarker();
      }else{
         $bool = false;
      }
   }
   printf("Delete Objects : OK" . PHP_EOL);
} catch (OssException $e) {
   printf("Delete Objects : Failed" . PHP_EOL);
   printf($e->getMessage() . PHP_EOL);
   return;
}
`

Node.js

`nodejs
const OSS = require('ali-oss');

const client = new OSS({
  // Set yourregion to the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourregion',
  // Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Set bucket to the name of your bucket.
  bucket: 'yourbucketname'
});

// Handle failed requests to prevent promise.all from being interrupted and to return the failure reason and the name of the failed file.
async function handleDel(name, options) {
  try {
    await client.delete(name);
  } catch (error) {
    error.failObjectName = name;
    return error;
  }
}

// Delete multiple files.
async function deletePrefix(prefix) {
  const list = await client.list({
    prefix: prefix,
  });

  list.objects = list.objects || ;
  const result = await Promise.all(list.objects.map((v) => handleDel(v.name)));
  console.log(result);
}
// Delete the directory and all files in it.
deletePrefix('log/')
`

Python

`python
# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
# Set the bucket name.
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'examplebucket')
prefix = "exampledir/"

# Delete the directory and all files in it.
for obj in oss2.ObjectIterator(bucket, prefix=prefix):
    bucket.delete_object(obj.key)
`

Go

`go
package main

import (
    "fmt"
    "os"

    "github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
    // Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
    provider, err := oss.NewEnvironmentVariableCredentialsProvider()
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(-1)
    }

    // Create an OSSClient instance.
    // Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
    client, err := oss.New("yourEndpoint", "", "", oss.SetCredentialsProvider(&provider))
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(-1)
    }

    // Set the bucket name.
    bucket, err := client.Bucket("examplebucket")
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(-1)
    }

    marker := oss.Marker("")
    // Set prefix to the full path of the directory to delete. The full path cannot contain the bucket name.
    prefix := oss.Prefix("log/")
    count := 0
    for {
        lor, err := bucket.ListObjects(marker, prefix)
        if err != nil {
            fmt.Println("Error:", err)
            os.Exit(-1)
        }

        objects := string{}
        for _, object := range lor.Objects {
            objects = append(objects, object.Key)
        }
        // Delete the directory and all files in it.
        // Set oss.DeleteObjectsQuiet to true to prevent the deletion result from being returned.
        delRes, err := bucket.DeleteObjects(objects, oss.DeleteObjectsQuiet(true))
        if err != nil {
            fmt.Println("Error:", err)
            os.Exit(-1)
        }

        if len(delRes.DeletedObjects) > 0 {
            fmt.Println("these objects deleted failure,", delRes.DeletedObjects)
            os.Exit(-1)
        }

        count += len(objects)

        prefix = oss.Prefix(lor.Prefix)
        marker = oss.Marker(lor.NextMarker)
        if !lor.IsTruncated {
            break
        }
    }
    fmt.Printf("success,total delete object count:%d\n", count)
}
`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* Initialize OSS account information. */

    /* Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";
    /* Set the bucket name. */
    std::string BucketName = "examplebucket";
    /* Set keyPrefix to the full path of the directory to delete. The full path cannot contain the bucket name. */
    std::string keyPrefix = "log/";

    /* Initialize resources such as the network. */
    InitializeSdk();

    ClientConfiguration conf;
    /* Get access credentials from environment variables. Before you run this example, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);

    std::string nextMarker = "";
    bool isTruncated = false;
    do {
            ListObjectsRequest request(BucketName);
            request.setPrefix(keyPrefix);
            request.setMarker(nextMarker);
            auto outcome = client.ListObjects(request);

            if (!outcome.isSuccess()) {
                /* Handle exceptions. */
                std::cout << "ListObjects fail" <<
                ",code:" << outcome.error().Code() <<
                ",message:" << outcome.error().Message() <<
                ",requestId:" << outcome.error().RequestId() << std::endl;
                break;
            }
            for (const auto& object : outcome.result().ObjectSummarys()) {
                DeleteObjectRequest request(BucketName, object.Key());
                /* Delete the directory and all files in it. */
                auto delResult = client.DeleteObject(request);
            }
            nextMarker = outcome.result().NextMarker();
            isTruncated = outcome.result().IsTruncated();
    } while (isTruncated);

    /* Release resources such as the network. */
    ShutdownSdk();
    return 0;
}
`


## API


If your program requires extensive customization, make REST API requests directly. To do this, you must manually write code to calculate the signature. For more information, see [DeleteObject](https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject#reference-iqc-mqv-wdb).

## Query the number and size of objects in a directory

#### Method 1: Get statistics by listing objects


Suitable for directories containing a relatively small number of objects, such as fewer than 10,000.


-

In the navigation pane on the left for the target bucket, choose Object Management > Objects.

-

Click the statistics icon to the right of the target directory.


![filesize.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5922584071/p694302.jpg)

#### Method 2: Perform periodic queries using a bucket inventory


Suitable for periodic analysis of directories containing a very large number of objects, such as millions or billions.


-

In the navigation pane on the left for the target bucket, choose Data Management > Bucket Inventory.

-

Click Create Inventory. On the Create Inventory panel, select a Inventory Storage Bucket. For the inventory content, select Object Size. For Object Prefix, enter the name of the directory to query, such as `random_files/`. Keep the default settings for the other parameters.


![screenshot_2025-07-04_18-14-09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7690170671/p982552.png)

-

View the inventory results.


-

On the Objects page, find the generated inventory file in the `/Inventory Report Bucket/Inventory ID/data/` path.


-

Download the inventory file to your local machine to view the number and size of files in the directory.


In the inventory file, column A represents the bucket name, column B lists the directory and all objects within it, and column C shows the size of each corresponding object.


![screenshot_2025-07-04_18-28-44](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0238430671/p982555.png)


For more information, see [Bucket inventory](https://www.alibabacloud.com/help/en/oss/user-guide/bucket-inventory).

#### Method 3: Perform complex queries using MetaSearch


Suitable for near real-time statistical queries on the number and size of objects in a directory, especially when you require flexible filtering conditions, such as by prefix, time, or file type.


-

In the navigation pane on the left for the target bucket, choose Object Management > Data Indexing.

-

On the Data Indexing page, click Enable data indexing, select MetaSearch, then click Enable.


> NOTE:

> NOTE: 


> NOTE: Note 

Enabling MetaSearch may take some time, depending on the number of objects in the bucket.


-

Set Object Name to Prefix Match and enter `random_files/` as the prefix. Keep the default settings for other parameters.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1776780571/p976633.png)

-

Configure the output method.


-

Set Object Sort Order to Default.

-

For Data Aggregation, select By Sum for Object Size.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1776780571/p976634.png)

-

Click Query Now. The results will show the total number and size of all objects in the `random_files/` directory.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1776780571/p976635.png)


For more information, see [MetaSearch](https://www.alibabacloud.com/help/en/oss/user-guide/scalar-retrieval/).

## Apply in production

### Access control


OSS bases access control on prefix matching for object names, not on the directory placeholder object itself.


For example, to grant a user read-only access to all objects in the `logs/` directory:


-

Incorrect: Set permissions on the zero-byte `logs/` placeholder object.

-

Correct: Create a Resource Access Management (RAM) policy where the `Resource` field is set to `acs:oss:*:*:your-bucket-name/logs/*`. This policy matches all objects whose names begin with the `logs/` prefix, regardless of whether the `logs/` placeholder object exists.

### Performance optimization


-

Directory depth: Avoid deeply nested directory structures (for example, `a/b/c/d/.../file.log`), as this can degrade the performance of list operations.

-

Large-scale renames: Renaming a directory that contains a large number of objects generates a high volume of API calls and traffic, incurring significant costs. Avoid this practice in your system design.


Thank you! We've received your  feedback.