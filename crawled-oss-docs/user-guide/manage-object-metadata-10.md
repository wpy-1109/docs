# Manage object metadata by configuring HTTP headers

Objects that are stored in Object Storage Service (OSS) consist of keys, data, and object metadata. Object metadata describes the object. Object metadata includes standard HTTP headers and user metadata. You can create custom HTTP request policies such as object cache policies and forced object download policies by configuring standard HTTP headers. You can also configure user metadata to identify the purposes or attributes of objects.

## Standard HTTP headers


OSS retains the standard HTTP headers of each object that is uploaded to a bucket. The following table describes the standard HTTP headers.








(https://www.alibabacloud.com/help/en/oss/user-guide/configure-the-content-type-header#concept-5041)


-


-


-


-


-


(https://www.ietf.org/rfc/rfc2616.txt)


> NOTE:

> NOTE: 


> NOTE: 




-


-


-


> NOTE:

> NOTE: 


> NOTE: 

-



-




(https://www.alibabacloud.com/help/en/oss/images-downloaded-as-an-attachment-instead-of-being-previewed-by-using-a-url#concept-2331929)


> NOTE:

> NOTE: 


> NOTE: 


-


-


-


-


-





(https://www.alibabacloud.com/help/en/oss/user-guide/what-are-the-operations-that-affect-the-lastmodified-attribute-of-oss-objects)


> NOTE:

> NOTE: 


> NOTE: 


| Standard HTTP header | Description |
| --- | --- |
| Content-Type | The media type of the object. The browser determines the format and encoding type that are used to read the object based on the media type of the object. If this header is not specified, OSS assigns a value based on the extension of the object name. If the object name does not have an extension, the default value application/octet-stream is used as the media type of the object. For more information about how to specify the media type of the object, see How do I configure the Content-Type header? |
| Content-Encoding | The method that is used to encode the object. You must specify this header based on the encoding type of the object. Otherwise, the browser that serves as the client may fail to parse the encoding type of the object, or the object may fail to be downloaded. If the object is not encoded, leave this header empty. Valid values:identity (default): OSS does not compress or encode the object. gzip: OSS uses the LZ77 compression algorithm created by Lempel and Ziv in 1977 and 32-bit cyclic redundancy check (CRC) to encode the object. compress: OSS uses the Lempel–Ziv–Welch (LZW) compression algorithm to encode the object. deflate: OSS uses the zlib library and the deflate algorithm to encode the object. br: OSS uses the Brotli algorithm to encode the object. For more information about Content-Encoding, see RFC 2616. Important If you want static web page objects, such as HTML, JavaScript, XML, and JSON objects, to be compressed into GZIP objects when you access the objects, you must leave this header empty and add the Accept-Encoding: gzip header to your request. |
| Content-Language | The language of the object content. For example, if the content of an object is written in simplified Chinese, you can set this header to zh-CN. |
| Content-Disposition | The method that is used to display the object. Valid values:Content-Disposition:inline: The object is displayed in the browser for a content preview. Content-Disposition:attachment: The object is downloaded to the specified download path of the browser with the original object name. Content-Disposition:attachment; filename="yourFileName": The object is downloaded to the specified download path of the browser with a custom object name. yourFileName specifies the custom name of the downloaded object, such as example.jpg. If you want to download the object to the specified download path of the browser, take note of the following items:Note If the name of the object contains special characters such as asterisks (*) or forward slashes (/), the name of the downloaded object may be escaped. For example, if you download example*.jpg to your local computer, example*.jpg may be escaped as example_.jpg. To prevent a download of an object with Chinese characters included in the object name from creating a local file with garbled characters in the file name, you must URL-encode the Chinese characters in the object name. For example, to ensure that the Test.txt object in OSS is downloaded as a local file that has the original object name Test.txt, you must set the Content-Disposition header to attachment;filename=%E6%B5%8B%E8%AF%95.txt;filename*=UTF-8''%E6%B5%8B%E8%AF%95.txt, which derives from "attachment;filename="+URLEncoder.encode("Test","UTF-8")+".txt;filename*=UTF-8''"+URLEncoder.encode("Test","UTF-8")+".txt". Whether an object is previewed or downloaded as an attachment when the object is accessed by using the object URL is determined by the creation time of the bucket in which the object is stored, the activation time of OSS, and the domain name type. For more information, see What do I do if an image object is downloaded as an attachment but cannot be previewed when I access the image object by using its URL? |
| Cache-Control | Note If Cache-Control is not set, OSS will not return this field in the response header, that is, the Cache-Control field does not exist. At this point, the caching behavior of the Object will be determined by the caching policy of the browser itself. The caching behavior of the object. Valid values:no-cache: The cached content cannot be used directly. Cached content must be validated with the server to check whether object content is updated. If the object content is updated, the cached content expires and the object is downloaded from the server again. If the object content is not updated, the cache does not expire, and the object is directly available from the cache. no-store: All content of the object is not cached. public: All content of the object is cached. private: All content of the object is cached only on the client. max-age=<seconds>: the validity period of the cached content. Unit: seconds. This option is available only in HTTP 1.1. |
| Expires | The expiration time of the cache in UTC. Example: 2022-10-12T00:00:00.000Z. If max-age=<seconds> is included in the Cache-Control header settings, max-age=<seconds> takes precedence over the value of Expires. |
| Last-Modified | The time when the object was last modified. The Last-Modified header is automatically updated by OSS for cache control, synchronization, and data management. The value of this header is in UTC and cannot be manually changed. For more information, see What are the operations that affect the LastModified attribute of OSS objects? Note The object update time shown in the OSS console is the local time that is converted from the UTC time for a consistent time display. For example, if an object was last updated at 13:31:54 on February 28, 2024 in UTC and you are checking the object in the UTC+8 time zone, the update time of the object that you see in the OSS console is 21:31:54, February 28, 2024. |
| Content-Length | The size of the object. Unit: bytes. |


## User metadata


When you upload an object, you can add user metadata to identify the purposes or attributes of the object.


-

You can configure multiple user metadata headers for an object. However, the total size of the user metadata of an object cannot exceed 8 KB.

-

User metadata is a set of key-value pairs. The name of a user metadata header must start with `x-oss-meta-`. For example, `x-oss-meta-last-modified:20210506` indicates that the local file was last modified on May 6, 2021.

-

When you call the GetObject operation or the HeadObject operation, the user metadata of the object is returned as HTTP headers.

## Procedure

### Use the OSS console


You can configure object metadata for up to 100 objects at a time by using the OSS console.


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left-side navigation tree, choose Object Management > Objects.

-

Configure standard HTTP headers and user metadata.


-

Configure HTTP headers for multiple objects at a time


Select the objects for which you want to configure metadata and click Set Object Metadata.

-

Configure HTTP headers for a single object


Find the object in the object list and choose ![more ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/2197678661/p508856.jpg) > Set Object Metadata.

-

Click OK.

### Use ossbrowser


You can use ossbrowser to perform the same object-level operations that you can perform in the OSS console. You can follow the on-screen instructions in ossbrowser to configure object metadata. For more information about how to use ossbrowser, see [Use ossbrowser](https://www.alibabacloud.com/help/en/oss/developer-reference/use-ossbrowser#title-kzi-qkt-skx).

### Use OSS SDKs


The following sample code provides an example on how to configure object metadata by using OSS SDKs for common programming languages. For more information about how to configure object metadata by using OSS SDKs for other programming languages, see [Overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.ClientException;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.common.utils.BinaryUtil;
import com.aliyun.oss.common.utils.DateUtil;
import com.aliyun.oss.model.ObjectMetadata;
import java.io.ByteArrayInputStream;

public class Demo {
    public static void main(Stringargs) throws Exception {
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the bucket name. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the full path of the object. Do not include the bucket name in the full path. Example: testfolder/exampleobject.txt.
        String objectName = "testfolder/exampleobject.txt";
        String content = "Hello OSS";
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Create an OSSClient instance.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
        .endpoint(endpoint)
        .credentialsProvider(credentialsProvider)
        .clientConfiguration(clientBuilderConfiguration)
        .region(region)
        .build();

        try {
            // Add metadata for the uploaded object.
            ObjectMetadata meta = new ObjectMetadata();

            String md5 = BinaryUtil.toBase64String(BinaryUtil.calculateMd5(content.getBytes()));
            // Enable MD5 verification. After MD5 verification is enabled, OSS calculates the MD5 hash of the uploaded object and compares this MD5 hash with that specified in the request. If the two values are different, an error is reported.
            meta.setContentMD5(md5);
            // Specify the type of content to upload. The browser determines the format and encoding type that are used to read the object based on the content type of the object. If the content type is not specified, a content type is generated based on the object name extension. If no extension is available, the default value application/octet-stream is used as the content type.
            meta.setContentType("text/plain");
            // Specify a name for the object when the content is downloaded.
            meta.setContentDisposition("attachment; filename=\"DownloadFilename\"");
            // Specify the length of the object to upload. If the actual object length is greater than the specified length, the object is truncated. Only the content of the specified length is uploaded. If the actual object length is smaller than the specified length, all content of the object is uploaded.
            meta.setContentLength(content.length());
            // Specify the caching behavior of the web page when the content is downloaded.
            meta.setCacheControl("Download Action");
            // Specify the expiration time of the cache in UTC.
            meta.setExpirationTime(DateUtil.parseIso8601Date("2022-10-12T00:00:00.000Z"));
            // Specify the content encoding format when the content is downloaded.
            meta.setContentEncoding("gzip");
            // Configure the HTTP headers.
            meta.setHeader("yourHeader", "yourHeaderValue");

            // Upload the object.
            ossClient.putObject(bucketName, objectName, new ByteArrayInputStream(content.getBytes()), meta);
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

// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
$provider = new EnvironmentVariableCredentialsProvider();
// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
$endpoint = "yourEndpoint";
// Specify the name of the bucket. Example: examplebucket.
$bucket= "examplebucket";
// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
$object = "exampledir/exampleobject.txt";
$content = file_get_contents(__FILE__);
$options = array(
    OssClient::OSS_HEADERS => array(
        'Expires' => '2012-10-01 08:00:00',
        'Content-Disposition' => 'attachment; filename="xxxxxx"',
        'x-oss-meta-self-define-title' => 'user define meta info',
    ));
try{
    $config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
        "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
        "region"=> "cn-hangzhou"
    );
    $ossClient = new OssClient($config);
    // Configure object metadata when you upload the object.
    $ossClient->putObject($bucket, $object, $content, $options);
} catch(OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}
print(__FUNCTION__ . ": OK" . "\n");

`

Node.js

`nodejs
const OSS = require('ali-oss');

const client = new OSS({
  // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourRegion',
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Specify the name of the bucket.
  bucket: 'examplebucket'
});

async function put() {
  try {
    let meta = { year: 2016, people: 'mary' };
    let result = await client.put('object-name', path.normalize('D:\\localpath\\examplefile.txt'), meta);
  console.log(result);
  } catch (e) {
    console.log(e);
  }
}

put();
`

Python

`python
# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"

# Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou. This parameter is required if you use the signature algorithm V4.
region = "cn-hangzhou"

# Specify the name of your bucket.
bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region)

# Specify the full path of the object. Example: exampledir/exampleobject.txt. Do not include the bucket name in the full path.
object_name = 'exampledir/exampleobject.txt'
# Specify the string that you want to upload.
content = '{"age": 1}'
# Configure HTTP headers. For example, set the Content-Type header to 'application/json; charset=utf-8'.
bucket.put_object(object_name, content, headers={'Content-Type': 'application/json; charset=utf-8'})
`

C#

`csharp
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Util;

// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "yourEndpoint";
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Specify the name of the bucket.
var bucketName = "examplebucket";
// Specify the full path of the object. Do not include the bucket name in the full path.
var objectName = "exampleobject.txt";
// Specify the full path of the local object that you want to upload. By default, if you do not specify the full path of the local object, the local object is uploaded from the path of the project to which the sample program belongs.
var localFilename = "D:\\localpath\\examplefile.txt";
// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
const string region = "cn-hangzhou";

// Create a ClientConfiguration instance and modify the default parameters based on your requirements.
var conf = new ClientConfiguration();

// Use the signature algorithm V4.
conf.SignatureVersion = SignatureVersion.V4;

// Create an OSSClient instance.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
try
{
    using (var fs = File.Open(localFilename, FileMode.Open))
    {
        // Create metadata for the object. You can configure HTTP headers for the object.
        var metadata = new ObjectMetadata()
        {
            // Specify the content type of the object.
            ContentType = "text/html",
            // Specify the expiration time of the cache in UTC.
            ExpirationTime = DateTime.Parse("2025-10-12T00:00:00.000Z"),
        };
        // Specify the length of the object content to upload. If the actual object length is greater than the specified length, the object is truncated. Only the content of the specified length is uploaded. If the actual object length is smaller than the specified length, all content of the object is uploaded.
        metadata.ContentLength = fs.Length;
        // Specify the caching behavior of the web page when the object is downloaded.
        metadata.CacheControl = "No-Cache";
        // Set mykey1 to myval1.
        metadata.UserMetadata.Add("mykey1", "myval1");
        // Set mykey2 to myval2.
        metadata.UserMetadata.Add("mykey2", "myval2");
        var saveAsFilename = "Filetest123.txt";
        var contentDisposition = string.Format("attachment;filename*=utf-8''{0}", HttpUtils.EncodeUri(saveAsFilename, "utf-8"));
        // Specify a default object name when the required content is saved as an object.
        metadata.ContentDisposition = contentDisposition;
        // Upload the object and configure object metadata.
        client.PutObject(bucketName, objectName, fs, metadata);
        Console.WriteLine("Put object succeeded");
        // Query object metadata.
        var oldMeta = client.GetObjectMetadata(bucketName, objectName);
        // Configure new object metadata.
        var newMeta = new ObjectMetadata()
        {
            ContentType = "application/octet-stream",
            ExpirationTime = DateTime.Parse("2035-11-11T00:00:00.000Z"),
            // Specify the content encoding format of the object when the object is downloaded.
            ContentEncoding = null,
            CacheControl = ""
        };
        // Configure user metadata.
        newMeta.UserMetadata.Add("author", "oss");
        newMeta.UserMetadata.Add("flag", "my-flag");
        newMeta.UserMetadata.Add("mykey2", "myval2-modified-value");
        // Use the ModifyObjectMeta method to modify the object metadata.
        client.ModifyObjectMeta(bucketName, objectName, newMeta);
    }
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
`

Android-Java

`androidjava
// Create a request to synchronously query object metadata.
// Specify the name of the bucket and the full path of the object. In this example, the bucket name is examplebucket and the full path of the object is exampledir/exampleobject.txt. Do not include the bucket name in the full path of the object.
HeadObjectRequest head = new HeadObjectRequest("examplebucket", "exampledir/exampleobject.txt");

// Query the object metadata.
OSSAsyncTask task = oss.asyncHeadObject(head, new OSSCompletedCallback<HeadObjectRequest, HeadObjectResult>() {
    @Override
    public void onSuccess(HeadObjectRequest request, HeadObjectResult result) {

    // Obtain the length of the object.
        Log.d("headObject", "object Size: " + result.getMetadata().getContentLength());
    // Query the type of the object.
        Log.d("headObject", "object Content Type: " + result.getMetadata().getContentType());
    }

    @Override
    public void onFailure(HeadObjectRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // Handle request exceptions.
        if (clientExcepion != null) {
            // Handle client exceptions, such as network exceptions.
            clientExcepion.printStackTrace();
        }
        if (serviceException != null) {
            // Handle service exceptions.
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});

// task.waitUntilFinished(); // Wait until the object metadata is queried.
`

Object C

`objectc
OSSHeadObjectRequest * request = [OSSHeadObjectRequest new];
// Specify the bucket name. Example: examplebucket.
request.bucketName = @"examplebucket";
// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
request.objectKey = @"exampledir/exampleobject.txt";

OSSTask * headTask = [client headObject:request];

[headTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"head object success!");
        OSSHeadObjectResult * result = task.result;
        NSLog(@"header fields: %@", result.httpResponseHeaderFields);
        for (NSString * key in result.objectMeta) {
            NSLog(@"ObjectMeta: %@ - %@", key, [result.objectMeta objectForKey:key]);
        }
    } else {
        NSLog(@"head object failed, error: %@" ,task.error);
    }
    return nil;
}];
`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
using namespace AlibabaCloud::OSS;

int main(void)
{

    /* Initialize information about the account that is used to access OSS. */

    /* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";
    /* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
    std::string Region = "yourRegion";
    /* Specify the name of the bucket. Example: examplebucket. */
    std::string BucketName = "examplebucket";
    /* Specify the full path of the object. Do not include the bucket name in the full path of the object. Example: exampledir/exampleobject.txt. */
    std::string ObjectName = "exampledir/exampleobject.txt";

    /* Initialize resources such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Configure the HTTP headers. */
    auto meta = ObjectMetaData();
    meta.setContentType("text/plain");
    meta.setCacheControl("max-age=3");
    /* Configure the user metadata of the object. */
    meta.UserMetaData()["meta"] = "meta-value";

    std::shared_ptr<std::iostream> content = std::make_shared<std::stringstream>();
    *content << "Thank you for using Aliyun Object Storage Service!";
    auto outcome = client.PutObject(BucketName, ObjectName, content, meta);

    if (!outcome.isSuccess()) {
        /* Handle exceptions. */
        std::cout << "PutObject fail" <<
        ",code:" << outcome.error().Code() <<
        ",message:" << outcome.error().Message() <<
        ",requestId:" << outcome.error().RequestId() << std::endl;
        return -1;
    }

    /* Release resources, such as network resources. */
    ShutdownSdk();
    return 0;
}
`

C

`c
#include "oss_api.h"
#include "aos_http_io.h"
/* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
const char *endpoint = "yourEndpoint";
/* Specify the name of the bucket. Example: examplebucket. */
const char *bucket_name = "examplebucket";
/* Specify the full path of the object. Do not include the bucket name in the full path of the object. Example: exampledir/exampleobject.txt. */
const char *object_name = "exampledir/exampleobject.txt";
const char *object_content= "hello world";
/* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
const char *region = "yourRegion";
void init_options(oss_request_options_t *options)
{
    options->config = oss_config_create(options->pool);
    /* Use a char* string to initialize aos_string_t. */
    aos_str_set(&options->config->endpoint, endpoint);
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    aos_str_set(&options->config->access_key_id, getenv("OSS_ACCESS_KEY_ID"));
    aos_str_set(&options->config->access_key_secret, getenv("OSS_ACCESS_KEY_SECRET"));
    // Specify two additional parameters.
    aos_str_set(&options->config->region, region);
    options->config->signature_version = 4;
    /* Specify whether to use CNAME. The value 0 indicates that CNAME is not used. */
    options->config->is_cname = 0;
    /* Specify network parameters, such as the timeout period. */
    options->ctl = aos_http_controller_create(options->pool, 0);
}
int main(int argc, char *argv)
{
    /* Call the aos_http_io_initialize method in main() to initialize global resources, such as network resources and memory resources. */
    if (aos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }
    /* Create a memory pool to manage memory. aos_pool_t is equivalent to apr_pool_t. The code that is used to create a memory pool is included in the APR library. */
    aos_pool_t *pool;
    /* Create a memory pool. The value of the second parameter is NULL. This value specifies that the pool does not inherit other memory pools. */
    aos_pool_create(&pool, NULL);
    /* Create and initialize options. This parameter specifies global configuration information such as endpoint, access_key_id, access_key_secret, is_cname, and curl. */
    oss_request_options_t *oss_client_options;
    /* Allocate the memory resources in the memory pool to the options. */
    oss_client_options = oss_request_options_create(pool);
    /* Initialize oss_client_options. */
    init_options(oss_client_options);
    /* Initialize the parameters. */
    aos_string_t bucket;
    aos_string_t object;
    aos_table_t *headers;
    aos_list_t buffer;
    aos_table_t *resp_headers = NULL;
    aos_status_t *resp_status = NULL;
    aos_buf_t *content = NULL;
    char *content_length_str = NULL;
    char *object_type = NULL;
    char *object_author = NULL;
    int64_t content_length = 0;
    aos_str_set(&bucket, bucket_name);
    aos_str_set(&object, object_name);
    headers = aos_table_make(pool, 2);
    /* Configure user metadata. */
    apr_table_set(headers, "Expires", "Fri, 28 Feb 2032 05:38:42 GMT");
    apr_table_set(headers, "x-oss-meta-author", "oss");
    aos_list_init(&buffer);
    content = aos_buf_pack(oss_client_options->pool, object_content, strlen(object_content));
    aos_list_add_tail(&content->node, &buffer);
    /* Upload an object from the cache. */
    resp_status = oss_put_object_from_buffer(oss_client_options, &bucket, &object,
               &buffer, headers, &resp_headers);
    if (aos_status_is_ok(resp_status)) {
        printf("put object from buffer with md5 succeeded\n");
    } else {
        printf("put object from buffer with md5 failed\n");
    }
    /* Query object metadata. */
    resp_status = oss_get_object_meta(oss_client_options, &bucket, &object, &resp_headers);
    if (aos_status_is_ok(resp_status)) {
        content_length_str = (char*)apr_table_get(resp_headers, OSS_CONTENT_LENGTH);
        if (content_length_str != NULL) {
            content_length = atol(content_length_str);
        }
        object_author = (char*)apr_table_get(resp_headers, OSS_AUTHORIZATION);
        object_type = (char*)apr_table_get(resp_headers, OSS_OBJECT_TYPE);
        printf("get object meta succeeded, object author:%s, object type:%s, content_length:%ld\n", object_author, object_type, content_length);
    } else {
        printf("req:%s, get object meta failed\n", resp_status->req_id);
    }
    /* Release the memory pool. This operation releases memory resources allocated for the request. */
    aos_pool_destroy(pool);
    /* Release the allocated global resources. */
    aos_http_io_deinitialize();
    return 0;
}
`

Ruby

`ruby
require 'aliyun/oss'
client = Aliyun::OSS::Client.new(
  # Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # Obtain access credentials from environment variables. Before you run the code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)

# Specify the name of the bucket. Example: examplebucket.
bucket = client.get_bucket('examplebucket')

# Configure object metadata during simple uploads.
bucket.put_object(
  'my-object-1',
  :file => 'local-file',
  :metas => {'year' => '2016', 'people' => 'mary'})

# Configure object metadata during append uploads.
bucket.append_object(
  'my-object-2', 0,
  :file => 'local-file',
  :metas => {'year' => '2016', 'people' => 'mary'})

# Configure object metadata during resumable uploads.
bucket.resumable_upload(
  'my-object',
  'local-file',
  :metas => {'year' => '2016', 'people' => 'mary'})
`

Go

`go
package main

import (
	"context"
	"flag"
	"log"
	"strings"
	"time"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

// Define global variables.
var (
	region     string // Region in which the bucket is located.
	bucketName string // The name of the bucket.
	objectName string // The name of the object.
)

// Specify the init function used to initialize command line parameters.
func init() {
	flag.StringVar(&region, "region", "", "The region in which the bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.")
	flag.StringVar(&objectName, "object", "", "The name of the object.")
}

func main() {
	// Parse command line parameters.
	flag.Parse()

	// Check whether the name of the bucket is specified.
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	// Check whether the region is specified.
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	// Check whether the name of the object is specified.
	if len(objectName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, object name required")
	}

	// Specify the content that you want to upload.
	content := "hi oss"

	// Load the default configurations and specify the credential provider and region.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region)

	// Create an OSS client.
	client := oss.NewClient(cfg)

	// Create a request to upload an object.
	request := &oss.PutObjectRequest{
		Bucket:  oss.Ptr(bucketName),                                                          // Name of the bucket.
		Key:     oss.Ptr(objectName),                                                          // Name of the object.
		Body:    strings.NewReader(content),                                                   // Content to be uploaded.
		Expires: oss.Ptr(time.Date(2038, 12, 31, 12, 0, 0, 0, time.UTC).Format(time.RFC1123)), // Expiration time of the object.
		Acl:     oss.ObjectACLPublicRead,
		Metadata: map[string]string{ // Custom metadata.
			"Author": "alibaba oss sdk", // Author of the object.
			"Date":   "2024-07-01",      // Creation date of the object.
		},
	}

	// Execute the upload request.
	result, err := client.PutObject(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put object %v", err)
	}

	// Log the result.
	log.Printf("put object result:%#v\n", result)
}

`


### Use ossutil


You can use ossutil to configure object metadata. For more information, see [set-meta (manage object metadata)](https://www.alibabacloud.com/help/en/oss/developer-reference/set-meta#concept-303809).

### Use the OSS API


If your business requires a high level of customization, you can directly call RESTful APIs. To directly call an API, you must include the signature calculation in your code. For more information, see [PutObject](https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb).


Thank you! We've received your  feedback.