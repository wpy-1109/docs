# Enable versioning for data restoration and version control

Versioning is a bucket-level feature that protects your data by preserving historical versions of objects after they are overwritten or deleted. If you accidentally overwrite or delete an object, you can restore it to any of its historical versions.

## Use cases


We recommend that you use versioning in the following scenarios to better protect your data.


-

Accidental data deletion


Since OSS does not have a recycle bin, versioning is the primary way to recover accidentally deleted data.

-

File overwrites


For frequently modified files, such as in cloud drives or collaborative tools, versioning lets you retrieve any previous version from a specific point in time.

##  Usage notes


-

Billing


The versioning feature is free of charge. However, you are charged for the storage of the current version and all historical versions of objects. To manage storage costs, use lifecycle rules to delete unneeded historical versions automatically. For more information, see [Lifecycle](https://www.alibabacloud.com/help/en/oss/user-guide/overview-54/). In addition, you are charged for requests and traffic when you download or restore historical versions. For more information about billing, see [Metering and billing](https://www.alibabacloud.com/help/en/oss/billing-overview#concept-n4t-mwg-tdb).

-

Permissions


Only the bucket owner and Resource Access Management (RAM) users with the PutBucketVersioning permission can configure versioning.

-

Mutually exclusive features


If versioning for a bucket is enabled or suspended:


-

The rule that prohibits object overwrites does not take effect. For more information, see [Prohibit overwrites of objects](https://www.alibabacloud.com/help/en/oss/user-guide/prevent-file-overwrite).

-

The `x-oss-forbid-overwrite` request header, which is used to prevent an object from being overwritten, does not take effect during uploads. For more information, see [PutObject](https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#section-y1z-lkw-bz).

-

Versioning and OSS-HDFS


Do not enable both OSS-HDFS and versioning on the same bucket, as this can cause instability. If you must, suspend versioning as soon as possible and use lifecycle rules to clean up delete markers.

## Versioning states


A bucket's versioning can be in one of three states: Disabled (default), Enabled, or Suspended.


-

By default, versioning is disabled for a bucket. Once versioning is enabled on a bucket, it can never be returned to the Disabled state, and it can only be suspended.

-

When versioning is enabled for a bucket, OSS generates a globally unique random string as the version ID for each newly uploaded object. For more information about object operations when versioning is enabled, see [Object operations when versioning is enabled](https://www.alibabacloud.com/help/en/oss/user-guide/manage-objects-in-a-versioning-enabled-bucket#concept-xw4-bxs-zgb).

-

When versioning is suspended, any newly uploaded object is assigned a version ID of null. For more information about object operations when versioning is suspended, see [Manage objects in a versioning-suspended bucket](https://www.alibabacloud.com/help/en/oss/user-guide/manage-objects-in-a-versioning-suspended-bucket#concept-anp-wvq-dgb).


> NOTE:

> NOTE: 


> NOTE: Note 

When versioning is enabled, every version of an object is stored and incurs storage costs, including current and historical versions. To manage these costs, you can use lifecycle rules to automatically transition versions to lower-cost storage classes (such as Infrequent Access or Archive) or to delete historical versions that are no longer needed. For more information, see [Configure lifecycle rules based on the last modified time for versioning-enabled buckets to reduce storage costs](https://www.alibabacloud.com/help/en/oss/user-guide/configure-lifecycle-rules-to-manage-object-versions#concept-2514466).


## Data protection


The following table describes how OSS handles object overwrites and deletions in different versioning states. This helps you understand the data protection mechanism of versioning.




















| Versioning state | Overwrite an object | Delete an object |
| --- | --- | --- |
| Disabled | The existing object is overwritten and cannot be restored. You can only retrieve the latest version of the object. | The object is permanently deleted and cannot be retrieved. |
| Enabled | A new version ID is added for the object. Historical versions are not affected. | A delete marker is added for the object. The delete marker has a globally unique version ID. Historical versions are not affected. |
| Suspended | A new version with the ID null is created. This new version will overwrite any existing object or delete marker that also has a null version ID. All other historical versions (with unique IDs) are preserved. | A delete marker with a version ID of null is created for the object.If a historical version of the object or a delete marker with a version ID of null already exists, it is overwritten by the new delete marker. Other versions of the object or delete markers that do not have a null version ID are not affected. |


The following figures show how OSS handles the upload of an object with the same name or the deletion of an object when versioning is enabled or suspended for a bucket. The version numbers in the figures are shortened for simplicity.


-

Object overwrite operations when versioning is enabled


When you repeatedly upload an object to a bucket with versioning enabled, each upload operation creates a new version of the object with a unique version ID.


![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/4944169951/p143835.png)

-

Object deletion operations when versioning is enabled


When you delete an object from a bucket with versioning enabled, its historical versions are not physically deleted. Instead, OSS creates a delete marker, which becomes the current version of the object. If you upload an object with the same name again, a new version is created with a new version ID.


![2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/4944169951/p143867.png)

-

Object overwrite operations when versioning is suspended


When you upload an object to a bucket with versioning suspended, its historical versions are retained. The newly uploaded object becomes the current version and has a version ID of `null`. If you upload an object with the same name again, the new object overwrites the previous version that has a version ID of `null`.


![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5944169951/p143879.png)

-

Object deletion operations when versioning is suspended


When you delete an object from a bucket with versioning suspended, its historical versions are not physically deleted. Instead, OSS creates a delete marker, which becomes the current version of the object.


![4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5944169951/p143882.png)


As shown in the preceding figures, when versioning is enabled or suspended for your bucket, overwrite and delete operations create historical versions. If you accidentally overwrite or delete an object, you can restore it to any of its historical versions.

## Enable versioning


Use the OSS console


When versioning is enabled for a bucket, OSS specifies a unique ID for each version of an object stored in the bucket.


-

Enable versioning when you create a bucket.


-

Log on to the [OSS](https://oss.console.alibabacloud.com/) console.

-

Click Buckets, and then click Create Bucket.

-

On the Create Bucket page, configure the parameters.


In the Versioning section, set the Versioning switch to On. By default, this feature is Off. For more information about other parameters, see [Create buckets](https://www.alibabacloud.com/help/en/oss/manage-buckets-create-buckets#task-bcz-sbz-5db).

-

Click Create.

-

Enable versioning for an existing bucket.


-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the navigation pane on the left, choose Content Security > Versioning.

-

On the Versioning page, click Enable Now.

-

In the dialog box that appears, click Confirm On.


After you enable versioning, on the Objects page, click Show next to Previous Versions to view all file versions. To view only the current versions of files, click Hide next to Previous Versions. Hiding previous versions does not improve the performance of listing files. If the page responds slowly when you list files, see [Slow response speed](https://www.alibabacloud.com/help/en/oss/user-guide/faq-4#section-kdt-v86-wjs) to troubleshoot and resolve the issue.


Use Alibaba Cloud SDKs


The following examples show how to enable versioning using various SDKs. For more information, see [Introduction to SDKs](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.*;

public class Demo {
    public static void main(Stringargs) throws Exception {
        // Set the endpoint. Use China (Hangzhou) as an example. Set the endpoint to the actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Specify the region where the bucket is located, for example, cn-hangzhou.
        String region = "cn-hangzhou";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the bucket name, for example, examplebucket.
        String bucketName = "examplebucket";

        // Create an OSSClient instance.
        // When the OSSClient instance is no longer used, call the shutdown method to release resources.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        // Explicitly declare that the V4 signature algorithm is used.
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(credentialsProvider)
                .clientConfiguration(clientBuilderConfiguration)
                .region(region)
                .build();

        try {
            // Enable versioning.
            BucketVersioningConfiguration configuration = new BucketVersioningConfiguration();
            configuration.setStatus(BucketVersioningConfiguration.ENABLED);
            SetBucketVersioningRequest request = new SetBucketVersioningRequest(bucketName, configuration);
            ossClient.setBucketVersioning(request);
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

// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
$accessKeyId = getenv("OSS_ACCESS_KEY_ID");
$accessKeySecret = getenv("OSS_ACCESS_KEY_SECRET");
// Set the endpoint. Use Hangzhou as an example. Set the endpoint to the actual endpoint.
$endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
$bucket= "yourBucketName";

$ossClient = new OssClient($accessKeyId, $accessKeySecret, $endpoint);

try {
    // Enable versioning.
    $ossClient->putBucketVersioning($bucket, "Enabled");
} catch (OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}

print(__FUNCTION__ . ": OK" . "\n");
`

Node.js

`nodejs
const OSS = require("ali-oss");

const client = new OSS({
  // Specify the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: "oss-cn-hangzhou",
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Specify the bucket name, for example, examplebucket.
  bucket: "examplebucket",
});

async function putBucketVersioning() {
  // Enable versioning.
  const status = "Enabled";
  const result = await client.putBucketVersioning("examplebucket", status);
  console.log(result);
}
putBucketVersioning();
`

Python

`python
# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from oss2.models import BucketVersioningConfig
# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# Specify the endpoint based on the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
# Set yourBucketName to the name of the bucket.
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'yourBucketName')

# Create a bucket versioning configuration.
config = BucketVersioningConfig()
# Enable versioning.
config.status = oss2.BUCKET_VERSIONING_ENABLE

result = bucket.put_bucket_versioning(config)
# View the HTTP status code.
print('http response code:', result.status)
`

C#

`csharp
using Aliyun.OSS;
using Aliyun.OSS.Common;

// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "yourEndpoint";
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Specify the name of the bucket. Example: examplebucket.
var bucketName = "examplebucket";
// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
const string region = "cn-hangzhou";

// Create a ClientConfiguration instance and modify parameters as required.
var conf = new ClientConfiguration();

// Use the signature algorithm V4.
conf.SignatureVersion = SignatureVersion.V4;

// Create an OSSClient instance.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
try
{
    // Set the versioning status of the bucket to Enabled.
    client.SetBucketVersioning(new SetBucketVersioningRequest(bucketName, VersioningStatus.Enabled));
    Console.WriteLine("Create bucket Version succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Create bucket Version failed. {0}", ex.Message);
}
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
    // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
    provider, err := oss.NewEnvironmentVariableCredentialsProvider()
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(-1)
    }

    // Create an OSSClient instance.
    // Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Set the endpoint to the actual endpoint.
    client, err := oss.New("yourEndpoint", "", "", oss.SetCredentialsProvider(&provider))
    if err != nil {
       fmt.Println("Error:", err)
       os.Exit(-1)
  }

  // Create a bucket.
  // Set yourBucketName to the name of the bucket.
  err = client.CreateBucket("yourBucketName")
  if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
  }
  // The following code provides an example of how to set the versioning state of a bucket to Enabled.
  config := oss.VersioningConfig{Status: "Enabled"}
  err = client.SetBucketVersioning("yourBucketName", config)
  if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
  }
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
    /* Specify the bucket name, for example, examplebucket. */
    std::string BucketName = "examplebucket";

    /* Initialize network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);

    /* Create a bucket versioning configuration and set the status to Enabled. */
    SetBucketVersioningRequest setrequest(BucketName, VersioningStatus::Enabled);
    auto outcome = client.SetBucketVersioning(setrequest);

    if (!outcome.isSuccess()) {
        /* Handle exceptions. */
        std::cout << "SetBucketVersioning fail" <<
        ",code:" << outcome.error().Code() <<
        ",message:" << outcome.error().Message() <<
        ",requestId:" << outcome.error().RequestId() << std::endl;
        return -1;
    }

    /* Release network resources. */
    ShutdownSdk();
    return 0;
}
`


Use the ossutil command line interface


Use ossutil, a command line interface (CLI), to set the versioning state for a specified bucket. For information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


The following command enables versioning for a specified bucket.


`bash
ossutil api put-bucket-versioning --bucket examplebucket --versioning-configuration "{\"Status\":\"Enabled\"}"
`


For more information about this command, see [put-bucket-versioning](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-versioning).

## Suspend versioning


If a retention policy is enabled for a bucket, you cannot change the versioning state from Enabled to Suspended. However, you can change the state from Suspended to Enabled.


Use the OSS console


You can suspend versioning for a versioned bucket to stop OSS from generating new versions for objects. If a new version is generated for an object in a versioning-suspended bucket, OSS sets the ID of the new version to null and retains the previous versions of the object.


To suspend versioning for a bucket, perform the following steps:


-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the navigation pane on the left, choose Content Security > Versioning.

-

On the Versioning page, click Suspend.

-

In the dialog box that appears, click OK.


Use Alibaba Cloud SDKs


The following code examples show how to enable versioning for common SDKs. For code examples for other SDKs, see [Introduction to SDKs](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.*;

public class Demo {
    public static void main(Stringargs) throws Exception {
        // Set the endpoint. Use China (Hangzhou) as an example. Set the endpoint to the actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Specify the region where the bucket is located, for example, cn-hangzhou.
        String region = "cn-hangzhou";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the bucket name, for example, examplebucket.
        String bucketName = "examplebucket";

        // Create an OSSClient instance.
        // When the OSSClient instance is no longer used, call the shutdown method to release resources.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        // Explicitly declare that the V4 signature algorithm is used.
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(credentialsProvider)
                .clientConfiguration(clientBuilderConfiguration)
                .region(region)
                .build();

        try {
            // Suspend versioning.
            BucketVersioningConfiguration configuration = new BucketVersioningConfiguration();
            configuration.setStatus(BucketVersioningConfiguration.SUSPENDED);
            SetBucketVersioningRequest request = new SetBucketVersioningRequest(bucketName, configuration);
            ossClient.setBucketVersioning(request);
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

// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
$accessKeyId = getenv("OSS_ACCESS_KEY_ID");
$accessKeySecret = getenv("OSS_ACCESS_KEY_SECRET");
// Set the endpoint. Use Hangzhou as an example. Set the endpoint to the actual endpoint.
$endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
$bucket= "yourBucketName";

$ossClient = new OssClient($accessKeyId, $accessKeySecret, $endpoint);

try {
    // Suspend versioning.
    $ossClient->putBucketVersioning($bucket, "Suspended");
} catch (OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}

print(__FUNCTION__ . ": OK" . "\n");
`

Node.js

`nodejs
const OSS = require("ali-oss");

const client = new OSS({
  // Specify the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: "oss-cn-hangzhou",
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Specify the bucket name, for example, examplebucket.
  bucket: "examplebucket",
});

async function putBucketVersioning() {
  // Suspend versioning.
  const status = "Suspended";
  const result = await client.putBucketVersioning("examplebucket", status);
  console.log(result);
}
putBucketVersioning();
`

Python

`python
# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from oss2.models import BucketVersioningConfig
# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# Specify the endpoint based on the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
# Set yourBucketName to the name of the bucket.
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'yourBucketName')

# Create a bucket versioning configuration.
config = BucketVersioningConfig()
# Suspend versioning.
config.status = oss2.BUCKET_VERSIONING_SUSPEND

result = bucket.put_bucket_versioning(config)
# View the HTTP status code.
print('http response code:', result.status)
`

C#

`csharp
using Aliyun.OSS;
// Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "yourEndpoint";
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Specify the bucket name, for example, examplebucket.
var bucketName = "examplebucket";
// Initialize the OSSClient.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret);
try
{
    // Set the versioning state of the bucket to Suspended.
    client.SetBucketVersioning(new SetBucketVersioningRequest(bucketName, VersioningStatus.Suspended));
    Console.WriteLine("Create bucket Version succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Create bucket Version failed. {0}", ex.Message);
}
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
    // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
    provider, err := oss.NewEnvironmentVariableCredentialsProvider()
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(-1)
    }

    // Create an OSSClient instance.
    // Set yourEndpoint to the endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Set the endpoint to the actual endpoint.
    client, err := oss.New("yourEndpoint", "", "", oss.SetCredentialsProvider(&provider))
    if err != nil {
       fmt.Println("Error:", err)
       os.Exit(-1)
  }

  // Create a bucket.
  // Set yourBucketName to the name of the bucket.
  err = client.CreateBucket("yourBucketName")
  if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
  }
  // Suspend versioning.
  config := oss.VersioningConfig{Status: "Suspended"}
  err = client.SetBucketVersioning("yourBucketName", config)
  if err != nil {
    fmt.Println("Error:", err)
    os.Exit(-1)
  }
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
    /* Specify the bucket name, for example, examplebucket. */
    std::string BucketName = "examplebucket";

    /* Initialize network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);

    /* Create a bucket versioning configuration and set the status to Suspended. */
    SetBucketVersioningRequest setrequest(BucketName, VersioningStatus::Suspended);
    auto outcome = client.SetBucketVersioning(setrequest);

    if (!outcome.isSuccess()) {
        /* Handle exceptions. */
        std::cout << "SetBucketVersioning fail" <<
        ",code:" << outcome.error().Code() <<
        ",message:" << outcome.error().Message() <<
        ",requestId:" << outcome.error().RequestId() << std::endl;
        return -1;
    }

    /* Release network resources. */
    ShutdownSdk();
    return 0;
}
`


Use the ossutil command line interface


Use the ossutil CLI to set the versioning state for a specified bucket. For information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


The following command suspends versioning for a specified bucket.


`bash
ossutil api put-bucket-versioning --bucket examplebucket --versioning-configuration "{\"Status\":\"Suspended\"}"
`


For more information about this command, see [put-bucket-versioning](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-versioning).

## View versions


Use the ossutil CLI to view all versions of an object. For information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


The following command lists information about all versions of all objects in the `examplebucket` bucket.


`bash
ossutil api list-object-versions --bucket examplebucket
`


For more information about this command, see [list-object-versions](https://www.alibabacloud.com/help/en/oss/developer-reference/list-object-versions).

## Restore a version


Use the OSS console


When you delete an object from a bucket with versioning enabled, its historical versions are not physically deleted. Instead, a delete marker is created, which becomes the current version of the object. You can then restore a previous version in the console.


-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the navigation pane on the left, choose Object Management > Objects.

-

Click Show next to Previous Versions.

-

Select the version that you want to restore and click Restore at the bottom of the page.

-

In the dialog box that appears, click OK.


Use the ossutil command line interface


Use the ossutil CLI to restore a historical version of a deleted file. For information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


The following command restores the example.txt object in the `examplebucket` bucket to version 123.


`bash
ossutil revert oss://examplebucket/example.txt 123
`


For more information about this command, see [revert](https://www.alibabacloud.com/help/en/oss/developer-reference/revert-recovery-version).

## Related API operations


The preceding operations are implemented based on API operations. If your program has high customization requirements, directly call REST API operations. To do this, you must manually write code to calculate signatures. For more information, see [PutBucketVersioning](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketversioning#reference-w2w-nm3-fhb).

## Work with retention policies


In scenarios such as providing version protection for backup systems such as Veeam, tracking modification records of assets such as circuit design diagrams, or meeting compliance archiving requirements in the finance industry, you often need to allow continuous data updates while ensuring that all historical versions are immutable and cannot be deleted. To achieve this, enable both versioning and a retention policy for a bucket. Versioning ensures that when an object is overwritten or deleted, its previous version is retained as a historical version instead of being physically deleted. The retention policy sets a protection period for all object versions in the bucket. During this period, no version can be deleted or modified.


When you configure both versioning and a retention policy, they work together based on the following principles:


-

Order of enabling features: There are no constraints on the order in which you enable versioning and retention policies. Configure them flexibly as needed.

-

Allowed configurations:


-

Retention policy + Versioning disabled

-

Retention policy + Versioning enabled

-

Restrictions:


-

You cannot enable a retention policy for a bucket for which versioning is suspended.

-

After a retention policy is enabled, the following restrictions apply to the versioning state:


-

You cannot change the state from Enabled to Suspended.

-

You cannot change the state from Disabled to Suspended.

-

Object version protection mechanism:


-

The retention policy protects all versions of an object. No version can be deleted or modified during the protection period.

-

You can upload an object with the same name to create a new version, but the new version is also protected by the retention policy.

-

The retention policy does not apply to delete markers. The clearing of delete markers is not restricted by the retention policy.

-

Interaction with data replication:



-

Both the source and destination buckets support independent configurations for versioning and retention policies.

-

Version information is transferred normally during replication. The destination bucket manages versions based on its own configuration.

-

Attempting to delete a replicated version in the destination bucket will fail if it is protected by a retention policy, but will succeed after the policy expires.

## References


-

[Manage objects in a versioning-enabled bucket](https://www.alibabacloud.com/help/en/oss/user-guide/manage-objects-in-a-versioning-enabled-bucket)

-

[Manage objects in a versioning-suspended bucket](https://www.alibabacloud.com/help/en/oss/user-guide/manage-objects-in-a-versioning-suspended-bucket)

-

[Delete marker](https://www.alibabacloud.com/help/en/oss/user-guide/delete-marker)

-

[FAQ](https://www.alibabacloud.com/help/en/oss/user-guide/faq-4)


Thank you! We've received your  feedback.