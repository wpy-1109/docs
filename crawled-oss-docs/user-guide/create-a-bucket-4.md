# How to create a bucket

A bucket is the fundamental container for storing objects in Object Storage Service (OSS). It offers unlimited storage capacity and scales elastically.

## Basic configuration


The following core bucket settings cannot be changed after creation.


-

Bucket name: Must be globally unique. Use department or business identifiers to simplify management. Example: `hr-documents`.

-

Region: Determines where your data is physically stored. Choose a region based on the following priorities:


-

Compliance: Choose a region that meets your regulatory requirements.

-

Performance: To reduce network latency, choose the region closest to your target users. If you access data from other Alibaba Cloud products, such as ECS, select the same region to benefit from free internal network traffic and minimize cross-region latency.

-

Feature availability: Refer to the [Release notes](https://www.alibabacloud.com/help/en/oss/release-notes) to confirm that the region supports the required features.

-

Cost optimization: After the preceding requirements are met, choose a region with more favorable [pricing](https://www.alibabacloud.com/product/oss/pricing).


If you create a bucket and specify only the bucket name and region, OSS applies these default settings: Standard storage, Zone-Redundant Storage (ZRS), Private, and Block Public Access enabled.

## Console


-

On the Buckets page of the [OSS console](https://oss.console.alibabacloud.com/bucket), click Create Bucket.

-

In the Create Bucket panel, set the Bucket Name and Region, then click Create.

## ossutil


Use ossutil to create a bucket. For installation instructions, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


-

Configure the required region for your bucket.


`bash
ossutil config
`


-

Press Enter to skip the other configuration prompts until the region prompt appears:


`bash
Please enter Region [cn-hangzhou]:
`


Enter the target region ID, such as `cn-beijing`, and press Enter, or press Enter to accept the default `cn-hangzhou`. You can find region IDs in [OSS regions and endpoints.](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e583bfe5e6sme).

-

Create a bucket named examplebucket.


`bash
ossutil mb oss://examplebucket
`


-

Verify that the bucket was created.


`bash
ossutil ls
`


For more information about this command, see [mb (create a bucket)](https://www.alibabacloud.com/help/en/oss/developer-reference/mb-create-storage-space).

## SDK


The following code samples show how to create a bucket using common SDKs. For code samples for other SDKs, see [SDK introduction](https://www.alibabacloud.com/help/en/oss/developer-reference/sdk-code-samples/).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.*;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // Set yourEndpoint to the Endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the Endpoint to https://oss-cn-hangzhou.aliyuncs.com.
        String endpoint = "yourEndpoint";
        // Obtain access credentials from environment variables. Before you run this sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the bucket name.
        String bucketName = "examplebucket";
        // Specify the resource group ID. If you do not specify a resource group ID, the bucket belongs to the default resource group.
        //String rsId = "rg-aek27tc";
        // Specify the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set Region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Create an OSSClient instance.
        // When the OSSClient instance is no longer in use, call the shutdown method to release resources.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
        .endpoint(endpoint)
        .credentialsProvider(credentialsProvider)
        .clientConfiguration(clientBuilderConfiguration)
        .region(region)
        .build();

        try {
            // Create a bucket and enable the hierarchical namespace feature.
            CreateBucketRequest createBucketRequest = new CreateBucketRequest(bucketName).withHnsStatus(HnsStatus.Enabled);
            // To specify the storage class, ACL, and data redundancy type when you create the bucket, see the following code.
            // This example shows how to set the storage class of the bucket to Standard.
            createBucketRequest.setStorageClass(StorageClass.Standard);
            // The default data redundancy type is LRS, which is DataRedundancyType.LRS.
            createBucketRequest.setDataRedundancyType(DataRedundancyType.LRS);
            // Set the ACL of the bucket to public-read. The default ACL is private.
            createBucketRequest.setCannedACL(CannedAccessControlList.PublicRead);
            // When you create a bucket in a region that supports resource groups, you can configure a resource group for the bucket.
            //createBucketRequest.setResourceGroupId(rsId);

            ossClient.createBucket(createBucketRequest);

            // Create the bucket.
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

Python

`python
import argparse
import alibabacloud_oss_v2 as oss

# Create a command line argument parser.
parser = argparse.ArgumentParser(description="put bucket sample")
# Specify the required command line parameter --region, which specifies the region in which the bucket is located.
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
# Specify the required command line parameter --bucket, which specifies the name of the bucket.
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
# Specify the optional command line parameter --endpoint, which specifies the endpoint that other services can use to access OSS.
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')

def main():
    args = parser.parse_args()  # Parse command line parameters.

    # Load access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load the default configurations of the SDK and specify the credential provider.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    # Specify the region in which the bucket is located.
    cfg.region = args.region
    # If the endpoint parameter is provided, specify the endpoint that other services can use to access OSS.
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    # Use the configurations to create an OSSClient instance.
    client = oss.Client(cfg)

    # Execute the request to create a bucket and set its storage class to Standard.
    result = client.put_bucket(oss.PutBucketRequest(
        bucket=args.bucket,
        create_bucket_configuration=oss.CreateBucketConfiguration(
            storage_class='Standard'
        )
    ))
    # Output the HTTP status code in the response and the request ID used to check whether the request is successful.
    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
    )


if __name__ == "__main__":
    main()  # Entry point of the script. The main function is invoked when the file is run directly.
`

Go

`go
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

// Specify the global variables.
var (
	region     string // The region.
	bucketName string // The name of the bucket.
)

// Specify the init function used to initialize command line parameters.
func init() {
	flag.StringVar(&region, "region", "", "The region in which the bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.")
}

func main() {
	// Parse command line parameters.
	flag.Parse()

	// Check whether the bucket name is empty.
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	// Check whether the region is empty.
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	// Load the default configurations and specify the credential provider and region.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region)

	// Create an OSS client.
	client := oss.NewClient(cfg)

	request := &oss.PutBucketRequest{
		Bucket: oss.Ptr(bucketName), // The name of the bucket.
	}

	// Send a request to create a bucket.
	result, err := client.PutBucket(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put bucket %v", err)
	}

	// Display the result of the bucket creation.
	log.Printf("put bucket result:%#v\n", result)
}

`

PHP

`php
<?php

// Automaticically load objects and dependency libraries.
require_once __DIR__ . '/../vendor/autoload.php';

use AlibabaCloud\Oss\V2 as Oss;

// Specify command line parameters.
$optsdesc = [
    "region" => ['help' => 'The region in which the bucket is located.', 'required' => True], // The region parameter is required. Example: oss-cn-hangzhou.
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // The endpoint parameter is optional.
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // The name of the bucket is required.
];

// Generate a list of long options for parsing command line parameters.
$longopts = \array_map(function ($key) {
    return "$key:"; // The colon (:) following each parameter indicates that the parameter is required.
}, array_keys($optsdesc));

// Parse command line parameters.
$options = getopt("", $longopts);

// Check whether the required parameters have been configured.
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help"; // Specifies that the required parameters are not configured.
        exit(1);
    }
}

// Retrieve the values of the command line parameters.
$region = $options["region"]; // Region in which the bucket is located.
$bucket = $options["bucket"]; // Name of the bucket.

// Load the credential information (AccessKeyId and AccessKeySecret) from environment variables.
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// Use the default configuration of the SDK.
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // Specify the credential provider.
$cfg->setRegion($region); // Specify the region.
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // Specify the endpoint if one is provided.
}

// Create an OSSClient instance.
$client = new Oss\Client($cfg);

// Create a request to initiate bucket creation.
$request = new Oss\Models\PutBucketRequest($bucket);

// Call the putBucket method.
$result = $client->putBucket($request);

// Output the result.
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP status code.
    'request id:' . $result->requestId // Unique ID of the request.
);

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
// Specify the name of the bucket.
var bucketName = "examplebucket";
// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
const string region = "cn-hangzhou";

// Create a ClientConfiguration instance and modify the default parameters based on your requirements.
var conf = new ClientConfiguration();

// Use the signature algorithm V4.
conf.SignatureVersion = SignatureVersion.V4;

// Create an OSSClient instance.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
// Create a bucket.
try
    {
        var request = new CreateBucketRequest(bucketName);
        // Set the access control list (ACL) of the bucket to PublicRead. The default value is private.
        request.ACL = CannedAccessControlList.PublicRead;
        // Set the redundancy type of the bucket to zone-redundant storage (ZRS).
        request.DataRedundancyType = DataRedundancyType.ZRS;
        client.CreateBucket(request);
        Console.WriteLine("Create bucket succeeded");
    }
    catch (Exception ex)
    {
        Console.WriteLine("Create bucket failed. {0}", ex.Message);
    }
`

Node.js

`nodejs
const OSS = require('ali-oss');

const client = new OSS({
  // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourregion',
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that you have configured environment variables OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // Specify the name of the bucket.
  bucket: 'yourBucketName',
});

// Create the bucket.
async function putBucket() {
  try {
    const options = {
      storageClass: 'Standard', // By default, the storage class of a bucket is Standard. To set the storage class of the bucket to Archive, set storageClass to Archive.
      acl: 'private', // By default, the access control list (ACL) of a bucket is private. To set the ACL of the bucket to public read, set acl to public-read.
      dataRedundancyType: 'LRS' // By default, the redundancy type of a bucket is locally redundant storage (LRS). To set the redundancy type of the bucket to zone-redundant storage (ZRS), set dataRedundancyType to ZRS.
    }
    // Specify the name of the bucket.
    const result = await client.putBucket('examplebucket', options);
    console.log(result);
  } catch (err) {
    console.log(err);
  }
}

putBucket();
`

Ruby

`ruby
require 'aliyun/oss'
client = Aliyun::OSS::Client.new(
  # In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)
# Specify the name of the bucket. Example: examplebucket.
client.create_bucket('examplebucket')
`

Android-Java

`androidjava
// Construct a request to create a bucket.
// Specify the name of the bucket.
CreateBucketRequest createBucketRequest=new CreateBucketRequest("examplebucket");.
// Specify the access control list (ACL) of the bucket.
// createBucketRequest.setBucketACL(CannedAccessControlList.Private);
// Specify the storage class of the bucket.
// createBucketRequest.setBucketStorageClass(StorageClass.Standard);

// Create the bucket asynchronously.
OSSAsyncTask createTask = oss.asyncCreateBucket(createBucketRequest, new OSSCompletedCallback<CreateBucketRequest, CreateBucketResult>() {
    @Override
    public void onSuccess(CreateBucketRequest request, CreateBucketResult result) {
        Log.d("asyncCreateBucket", "Success");
    }
    @Override
    public void onFailure(CreateBucketRequest request, ClientException clientException, ServiceException serviceException) {
        // Handle request exceptions.
        if (clientException != null) {
            // Handle client exceptions, such as network exceptions.
            clientException.printStackTrace();
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
`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* Initialize the OSS account information. */

    /* Set yourEndpoint to the Endpoint of the region in which the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the Endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";

    /* Set yourRegion to the region in which the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the Region to cn-hangzhou. */
    std::string Region = "yourRegion";

    /* Specify the bucket name. Example: examplebucket. */
    std::string BucketName = "examplebucket";

    /* Initialize network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Specify the name, storage class, and ACL of the new bucket. */
    CreateBucketRequest request(BucketName, StorageClass::IA, CannedAccessControlList::PublicReadWrite);
    /* Set the data disaster recovery type to zone-redundant storage. */
    request.setDataRedundancyType(DataRedundancyType::ZRS);

    /* Create the bucket. */
    auto outcome = client.CreateBucket(request);

    if (!outcome.isSuccess()) {
        /* Handle the exception. */
        std::cout << "CreateBucket fail" <<
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

Object C

`objectc
// Construct a request to create a bucket.
OSSCreateBucketRequest * create = [OSSCreateBucketRequest new];
// Set the bucket name to examplebucket.
create.bucketName = @"examplebucket";
// Set the access control list (ACL) of the bucket to private.
create.xOssACL = @"private";
// Set the storage class of the bucket to Infrequent Access (IA).
create.storageClass = OSSBucketStorageClassIA;

OSSTask * createTask = [client createBucket:create];

[createTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"create bucket success!");
    } else {
        NSLog(@"create bucket failed, error: %@", task.error);
    }
    return nil;
}];
// Implement synchronous blocking to wait for the task to complete.
// [createTask waitUntilFinished];
`

C

`c
#include "oss_api.h"
#include "aos_http_io.h"
/* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
const char *endpoint = "yourEndpoint";
/* Specify the name of the bucket. Example: examplebucket. */
const char *bucket_name = "examplebucket";
/* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
const char *region = "yourRegion";

void init_options(oss_request_options_t *options)
{
    options->config = oss_config_create(options->pool);
    /* Use a char* string to initialize data of the aos_string_t type. */
    aos_str_set(&options->config->endpoint, endpoint);
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    aos_str_set(&options->config->access_key_id, getenv("OSS_ACCESS_KEY_ID"));
    aos_str_set(&options->config->access_key_secret, getenv("OSS_ACCESS_KEY_SECRET"));
    // Specify two additional parameters.
    aos_str_set(&options->config->region, region);
    options->config->signature_version = 4;
    /* Specify whether to use CNAME to access OSS. The value of 0 indicates that CNAME is not used.  */
    options->config->is_cname = 0;
    /* Configure network parameters, such as the timeout period. */
    options->ctl = aos_http_controller_create(options->pool, 0);
}
int main(int argc, char *argv)
{
    /* Call the aos_http_io_initialize method in main() to initialize global resources, such as network resources and memory resources.  */
    if (aos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }
    /* Create a memory pool to manage memory. aos_pool_t is equivalent to apr_pool_t. The code used to create a memory pool is included in the APR library. */
    aos_pool_t *pool;
    /* Create a memory pool. The value of the second parameter is NULL. This value specifies that the pool does not inherit other memory pools. */
    aos_pool_create(&pool, NULL);
    /* Create and initialize options. This parameter includes global configuration information, such as endpoint, access_key_id, access_key_secret, is_cname, and curl. */
    oss_request_options_t *oss_client_options;
    /* Allocate the memory resources in the memory pool to the options. */
    oss_client_options = oss_request_options_create(pool);
    /* Initialize oss_client_options. */
    init_options(oss_client_options);
    /* Initialize the parameters. */
    aos_string_t bucket;
    oss_acl_e oss_acl = OSS_ACL_PRIVATE;
    aos_table_t *resp_headers = NULL;
    aos_status_t *resp_status = NULL;
    /* Assign char* data to a bucket of the aos_string_t type.  */
    aos_str_set(&bucket, bucket_name);
    /* Create the bucket. */
    resp_status = oss_create_bucket(oss_client_options, &bucket, oss_acl, &resp_headers);
    /* Determine whether the bucket is created.  */
    if (aos_status_is_ok(resp_status)) {
        printf("create bucket succeeded\n");
    } else {
        printf("create bucket failed\n");
    }
    /* Release the memory pool. This operation releases the memory resources allocated for the request. */
    aos_pool_destroy(pool);
    /* Release the allocated global resources.  */
    aos_http_io_deinitialize();
    return 0;
}
`


## API


Specify the name and region in the Host header when you call the [PutBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#doc-api-Oss-PutBucket) operation.

## Storage class


OSS provides five [storage classes](https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#section-tbz-dt6-bg2): Standard, Infrequent Access (IA), Archive, Cold Archive, and Deep Cold Archive. The default storage class is Standard. These classes offer decreasing storage costs in exchange for higher data retrieval costs and longer retrieval times to suit data with different access frequencies.


Objects inherit the storage class of the bucket by default. Although you cannot change the storage class of a bucket after it is created, you can use [lifecycle](https://www.alibabacloud.com/help/en/oss/user-guide/overview-54/) rules to automatically transition the storage class of objects to optimize costs.


-

Standard


Suitable for active data where a single file is accessed more than once a month. It supports real-time access. This is the preferred choice if you are unsure about data access frequency. You can later use lifecycle rules to automatically transition objects to a lower-cost storage class.

-

Infrequent Access (IA):


Suitable for warm data where a single file is accessed once a month or less, such as backup files and operation logs. It supports real-time access but has a minimum storage duration of 30 days. If you delete an object before 30 days have passed, you are still charged for 30 days of storage. This storage class is not suitable for temporary or test data.

-

Archive:


Suitable for cold data where a single file is accessed less than once every 90 days. It supports real-time access of Archive objects. You can also choose to restore the object first and then read it. Restoration takes about 1 minute. It has a minimum storage duration of 60 days.
Restore: The process of making an object in an archive storage class temporarily accessible for reading. This process requires a waiting period.
-

Cold Archive


Suitable for data where a single file is accessed less than once a year. You must restore the data before you can read it. Restoration takes 1 to 12 hours. This class has lower costs and a minimum storage duration of 180 days.

-

Deep Cold Archive


This is the lowest-cost option and is suitable for data where a single file is accessed less than once a year. Restoration takes 12 or 48 hours. It has a minimum storage duration of 180 days. Creating a bucket with this storage class is not recommended. We recommend that you use lifecycle rules to automatically transition data to this class.

## Console


When you create a bucket, you can configure the bucket storage class based on your needs.

## ossutil


The following command creates a bucket named `examplebucket` with the Infrequent Access (IA) storage class.


`bash
ossutil mb oss://examplebucket --storage-class IA
`


For more information about this command, see [mb (create a bucket)](https://www.alibabacloud.com/help/en/oss/developer-reference/mb-create-storage-space).

## OSS SDK


The following code samples show how to create a bucket using common SDKs. For code samples for other SDKs, see [SDK introduction](https://www.alibabacloud.com/help/en/oss/developer-reference/sdk-code-samples/).

## Java


To set the storage class, you can configure the `CreateBucketRequest` object as follows.


`java
// Prepare a request object that contains the storage class.
CreateBucketRequest createBucketRequest = new CreateBucketRequest("your-bucket-name");
createBucketRequest.setStorageClass(StorageClass.IA); // Specify the storage class here.

// Options: StorageClass.Standard, StorageClass.IA, StorageClass.Archive, etc.
`


For a complete example, see [Create a bucket (Java SDK V1)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket).

## Python


When you call the `client.put_bucket` method, you can specify the storage class using the `create_bucket_configuration` parameter.


`python
# Prepare a request object that contains the storage class.
req = oss.PutBucketRequest(
    bucket="your-bucket-name",
    create_bucket_configuration=oss.CreateBucketConfiguration(
        storage_class='IA'  # Specify the storage class here.
    )
)

# Options: 'Standard', 'IA', 'Archive', 'ColdArchive', 'DeepColdArchive'
`


For a complete example, see [Create a bucket (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-bucket-using-oss-sdk-for-python-v2).

## Go


To set the storage class, you can configure the `CreateBucketConfiguration` field when you create a `PutBucketRequest`.


`go
request := &oss.PutBucketRequest{
    Bucket: oss.Ptr("your-bucket-name"),
    CreateBucketConfiguration: &oss.CreateBucketConfiguration{
        StorageClass: oss.StorageClassIA, // Specify the storage class here.
    },
}

// Options: oss.StorageClassStandard, oss.StorageClassIA, oss.StorageClassArchive, etc.
`


For a complete example, see [Create a bucket (Go SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-create-bucket).

## PHP


To set the storage class, you can pass a `CreateBucketConfiguration` object to the constructor when you create a `PutBucketRequest` object.


`php
// Prepare a request object that contains configurations such as the storage class.
$request = new Oss\Models\PutBucketRequest(
    "your-bucket-name",
    null, // acl
    null, // resourceGroupId
    new Oss\Models\CreateBucketConfiguration(
        'IA',             // Specify the storage class here.
    )
);

/ Optional storage classes: 'Standard', 'IA', 'Archive', 'ColdArchive', 'DeepColdArchive'
*/
`


For a complete example, see [Create a bucket (PHP SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-create-bucket).

## C#


To set the storage class, you can create a `CreateBucketRequest` object and configure its properties as follows.


`csharp
// Prepare a request object that contains the storage class configuration.
var request = new CreateBucketRequest("your-bucket-name");
request.StorageClass = StorageClass.IA;             // Specify the storage class here.

// Optional storage classes: StorageClass.Standard, StorageClass.IA, StorageClass.Archive, etc.
`


For a complete example, see [Create buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1).

## Node.js


To set the storage class, you can create an `options` object and pass it to the `putBucket` method.


`nodejs
// Prepare an options object that contains the storage class configuration.
const options = {
  storageClass: 'IA',              // Specify the storage class here.
};

// Optional storage classes: 'Standard', 'IA', 'Archive', 'ColdArchive', 'DeepColdArchive'
`


For a complete example, see [Create a bucket (Node.js SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-4).

## Android


To set the storage class or access permissions, you can create and configure a `CreateBucketRequest` object as follows.


`androidjava
// Prepare a request object that contains configurations such as the storage class.
CreateBucketRequest createBucketRequest = new CreateBucketRequest("your-bucket-name");
createBucketRequest.setBucketStorageClass(StorageClass.IA);         // Specify the storage class here.

// Optional storage classes: StorageClass.Standard, StorageClass.IA, StorageClass.Archive, etc.
`


For a complete example, see [Create a bucket (Android SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-5).

## iOS


To set the storage class, create an `OSSCreateBucketRequest` object and configure the following properties.


`objectc
// Prepare a request object that contains configurations such as the storage class.
OSSCreateBucketRequest *create = [OSSCreateBucketRequest new];
create.bucketName = @"your-bucket-name";
create.storageClass = OSSBucketStorageClassIA;     // Specify the storage class here.

// Optional storage classes: OSSBucketStorageClassStandard, OSSBucketStorageClassIA, etc.
`


For a complete example, see [Create a bucket](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-1).

## API


When you call [PutBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#doc-api-Oss-PutBucket), you can specify the storage class of the bucket in the StorageClass request element.

## Storage redundancy type


The data redundancy type determines the disaster recovery capabilities, durability, and availability of your data. The default type is zone-redundant storage. You can [upgrade](https://www.alibabacloud.com/help/en/oss/user-guide/converting-storage-redundancy-types) from locally redundant storage to zone-redundant storage, but you cannot downgrade.


-

Zone-redundant storage (ZRS) - Recommended for production environments


Your data is stored across multiple zones (AZs) in the same region. This ensures business continuity if an entire zone fails and provides higher data durability and service availability.

-

Locally redundant storage (LRS) - For non-critical or test data


Your data is stored redundantly within a single zone at a lower cost. It can withstand hardware failures but cannot guarantee data access if a zone fails.

## Console


Select the Redundancy Type for the bucket in the Basic Information section when you create a bucket.

## ossutil


Create a bucket named `examplebucket` with the LRS redundancy type.


`bash
ossutil mb oss://examplebucket --redundancy-type LRS
`


For more information about this command, see [mb (create a bucket)](https://www.alibabacloud.com/help/en/oss/developer-reference/mb-create-storage-space).

## OSS SDKs

## Java


To set the redundancy type, configure the `CreateBucketRequest` object as follows.


`java
// Prepare a request object that contains the redundancy type.
CreateBucketRequest createBucketRequest = new CreateBucketRequest("your-bucket-name");
createBucketRequest.setDataRedundancyType(DataRedundancyType.ZRS); // Specify the storage redundancy type here.

// Options: DataRedundancyType.ZRS, DataRedundancyType.LRS
`


For a complete example, see [Create a bucket (OSS SDK for Java 1.0)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket).

## Python


When you call the `client.put_bucket` method, you can specify the storage redundancy type using the `create_bucket_configuration` parameter.


`python
# Prepare a request object that contains the storage redundancy type.
req = oss.PutBucketRequest(
    bucket="your-bucket-name",
    create_bucket_configuration=oss.CreateBucketConfiguration(
        data_redundancy_type='ZRS'  # Specify the storage redundancy type here.
    )
)

# Options: 'ZRS', 'LRS'
`


For a complete example, see [Create a bucket (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-bucket-using-oss-sdk-for-python-v2).

## Go


To set the storage redundancy type, you can configure the `CreateBucketConfiguration` field when you create a `PutBucketRequest`.


`go
request := &oss.PutBucketRequest{
    Bucket: oss.Ptr("your-bucket-name"),
    CreateBucketConfiguration: &oss.CreateBucketConfiguration{
        DataRedundancyType: oss.DataRedundancyZRS, // Specify the storage redundancy type here.
    },
}

// Options: oss.DataRedundancyZRS, oss.DataRedundancyLRS
`


For a complete example, see [Create a bucket (Go SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-create-bucket).

## PHP


To set the storage redundancy type, you can pass a `CreateBucketConfiguration` object to the constructor when you create a `PutBucketRequest` object.


`php
// Prepare a request object that contains configurations such as the storage redundancy type.
$request = new Oss\Models\PutBucketRequest(
    "your-bucket-name",
    null, // acl
    null, // resourceGroupId
    new Oss\Models\CreateBucketConfiguration(
        null,             // Specify the storage redundancy type here.
        'ZRS'
    )
);

/ Optional storage redundancy types: 'ZRS', 'LRS'
*/
`


For a complete example, see [Create a bucket (PHP SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-create-bucket).

## C#


To set the storage redundancy type, you can create a `CreateBucketRequest` object and configure its properties as follows.


`csharp
// Prepare a request object that contains the storage redundancy type configuration.
var request = new CreateBucketRequest("your-bucket-name");
request.DataRedundancyType = DataRedundancyType.ZRS;        // Specify the storage redundancy type here.

// Optional storage redundancy types: DataRedundancyType.ZRS, DataRedundancyType.LRS
`


For a complete example, see [Create buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1).

## Node.js


To set the storage redundancy type, you can create an `options` object and pass it to the `putBucket` method.


`nodejs
// Prepare an options object that contains the storage redundancy type configuration.
const options = {
  dataRedundancyType: 'LRS',    // Specify the storage redundancy type here.
};

// Optional storage redundancy types: 'ZRS', 'LRS'
`


For a complete example, see [Create a bucket (Node.js SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-4).

## API


When you call [PutBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#doc-api-Oss-PutBucket), you can specify the storage redundancy type of the bucket in the DataRedundancyType request element.

## Access control list (ACL)


The access control list (ACL) controls the anonymous access policy for a bucket. The default permission is private, which you can change at any time after the bucket is created. Objects inherit the bucket's access permissions by default. You can also [set permissions for individual objects](https://www.alibabacloud.com/help/en/oss/user-guide/object-acl).


-

Private - Strongly recommended


This is the default and most secure setting. Only the bucket owner and users who are explicitly granted permissions through RAM policies or bucket policies can access the bucket. We recommend that you always use this setting. To grant access to other users, see [Overview of permission and access control](https://www.alibabacloud.com/help/en/oss/user-guide/permissions-and-access-control-overview#concept-e4s-mhv-tdb).

-

Public-read - Use with caution


No authentication is required. Anyone, including anonymous visitors, can read objects but cannot write to them.


-

Your data will be fully public. This may result in unexpected charges for outbound traffic over the Internet. This setting is suitable for scenarios that require public sharing, such as hosting static website resources.

-

If you must enable public-read, configure [hotlink protection](https://www.alibabacloud.com/help/en/oss/user-guide/hotlink-protection) to allow access only from specific sources, such as your website domain, to prevent bandwidth theft from unauthorized hotlinking.

-

Public-read-write - Not recommended


Anyone can read, write, and even delete objects in the bucket. This poses an extremely high security risk and can lead to substantial fees. Use this setting only for special scenarios, such as public resource repositories, and never for general use.

## Console


For security reasons, the [OSS console](https://oss.console.alibabacloud.com/overview) enables Block Public Access by default and supports creating only private buckets.


To change the ACL to Public Read or Public Read/Write, you can perform the following steps:


-

Click the name of the target bucket.

-

In the navigation pane on the left, choose Permission Control > Block Public Access and disable the policy.

-

Go to the ACL tab and click Settings.

-

Follow the on-screen instructions to change the bucket ACL to Public Read or Public Read/Write.

## ossutil


The following command creates a bucket named examplebucket and sets its access control list (ACL) to private.


`bash
ossutil mb oss://examplebucket --acl=private
`


For more information about this command, see [mb (create a bucket)](https://www.alibabacloud.com/help/en/oss/developer-reference/mb-create-storage-space).

## OSS SDKs

## Java


To set the access permissions, you can configure the `CreateBucketRequest` object as follows.


`java
// Prepare a request object that contains the access permissions.
CreateBucketRequest createBucketRequest = new CreateBucketRequest("your-bucket-name");
createBucketRequest.setCannedACL(CannedAccessControlList.private); // Specify the bucket ACL here.

// Options: CannedAccessControlList.private, CannedAccessControlList.PublicRead,CannedAccessControlList.PublicReadWrite
`


For a complete example, see [Create a bucket (Java SDK V1)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket).

## Python


When you call the `client.put_bucket` method, you can specify the access permissions using the `create_bucket_configuration` parameter.


`python
# Prepare a request object that contains the access permissions.
req = oss.PutBucketRequest(
    bucket="your-bucket-name",
    create_bucket_configuration=oss.CreateBucketConfiguration(
        access_control_policy='pricate'  # Specify the access permissions here.
    )
)

# Options: 'pricate', 'public-read','public-read-write'
`


For a complete example, see [Create a bucket (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-bucket-using-oss-sdk-for-python-v2).

## Go


To set the access permissions, you can configure the `Acl` field when you create a `PutBucketRequest`.


`go
// Prepare a request object that contains configurations such as access permissions.
request := &oss.PutBucketRequest{
    Bucket: oss.Ptr("your-bucket-name"),
    Acl:    oss.BucketACLPrivate, // Specify the access permissions here.
    CreateBucketConfiguration: &oss.CreateBucketConfiguration{
    },
}

// Optional access permissions: oss.BucketACLPrivate, oss.BucketACLPublicRead, oss.BucketACLPublicReadWrite
`


For a complete example, see [Create a bucket (Go SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-create-bucket).

## PHP


To set the access permissions, you can configure the `Acl` field when you create a `PutBucketRequest`.


`php
// Prepare a request object that contains configurations such as access permissions.
$request = new Oss\Models\PutBucketRequest(
    "your-bucket-name",
    'private', // Specify the access permissions here (second parameter).
    null,      // resourceGroupId
    new Oss\Models\CreateBucketConfiguration(
        'IA',      // Specify the storage class here.
        'ZRS'      // Specify the redundancy type here.
    )
);

/ Optional access permissions: 'private', 'public-read', 'public-read-write'
*/
`


For a complete example, see [Create a bucket (PHP SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-create-bucket).

## C#


To set the access permissions, you can create a `CreateBucketRequest` object and configure its properties as follows.


`csharp
// Prepare a request object that contains the access permission configuration.
var request = new CreateBucketRequest("your-bucket-name");
request.ACL = CannedAccessControlList.private;       // Specify the access permissions here.

// Optional access permissions: CannedAccessControlList.private, CannedAccessControlList.PublicRead,CannedAccessControlList.PublicReadWrite
`


For a complete example, see [Create buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1).

## Node.js


To set the access permissions, you can create an `options` object and pass it to the `putBucket` method.


`nodejs
// Prepare an options object that contains the access permissions.
const options = {
  acl: 'private',     // Specify the access permissions here.
};

// Optional access permissions: 'private', 'public-read','public-read-write'
`


For a complete example, see [Create a bucket (Node.js SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-4).

## Android


To set the access permissions, you can create and configure a `CreateBucketRequest` object as follows.


`androidjava
// Prepare a request object that contains configurations such as access permissions.
CreateBucketRequest createBucketRequest = new CreateBucketRequest("your-bucket-name");
createBucketRequest.setBucketACL(CannedAccessControlList.Private); // Specify the access permissions here.

// Optional access permissions: CannedAccessControlList.Private, CannedAccessControlList.PublicRead,CannedAccessControlList.PublicReadWrite
`


For a complete example, see [Create a bucket (Android SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-5).

## iOS


To set the access permissions, you can create an `OSSCreateBucketRequest` object and configure its properties as follows.


`objectc
// Prepare a request object that contains configurations such as access permissions.
OSSCreateBucketRequest *create = [OSSCreateBucketRequest new];
create.bucketName = @"your-bucket-name";
create.xOssACL = @"private";    // Specify the access permissions here.

// Optional access permissions: private,public-read, public-read-write, etc.
`


For a complete example, see [Create a bucket](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-1).

## API


When you call the [PutBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#doc-api-Oss-PutBucket) operation, you can specify the ACL of the bucket in the `x-oss-acl` request header.

## Block Public Access


A global security switch that prevents accidental public exposure of data due to incorrect ACL or bucket policy configurations.


When enabled, you can create only private buckets. You cannot set public-read or public-read-write ACLs, or create bucket policies with public access semantics. By default, Block Public Access is enabled when you create a bucket in OSS. If your business requires public access, you can manually disable this feature after the bucket is created. However, for security reasons, we do not recommend that you disable it.

## Optional configurations


Configure these features during or after bucket creation based on actual use cases.


-

Versioning


This feature prevents accidental deletion or overwriting of data. When you upload an object with the same name, a new version is created instead of overwriting the existing one. You can restore a previous version with a single click after an accidental operation. For more information, see [Versioning](https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/).

-

Server-side encryption


This feature automatically encrypts static data. OSS encrypts data when it is written and decrypts it when it is read. We recommend that you enable at least the 'Fully managed by OSS' option. For more information, see [Server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8).

-

Resource group


This feature is suitable for multi-team collaboration. You can group buckets by department or project for independent permission management and cost accounting. For more information, see [Use resource groups](https://www.alibabacloud.com/help/en/oss/user-guide/configure-a-resource-group).

-

Real-time log query


When this feature is enabled, you can quickly query and analyze access logs in the console to see who accessed which files and when. This helps you investigate unusual access or perform user behavior analysis. For more information, see [Real-time log query](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/).

-

Scheduled backup


This feature supports automated data backup. For more information, see [Configure scheduled backup for a bucket](https://www.alibabacloud.com/help/en/oss/user-guide/configure-scheduled-backup#92bd44f121lvg).

-

OSS-HDFS


This feature is suitable for data lake scenarios. It allows big data frameworks such as Spark to directly analyze OSS data without data migration. For more information, see [What is the OSS-HDFS service?](https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs-overview).

-

Bucket tagging


This feature facilitates batch management and cost analysis. You can classify buckets using key-value tags, such as `department:research`. For more information, see [Manage bucket tags](https://www.alibabacloud.com/help/en/oss/user-guide/manage-bucket-tags#concept-1925905).

## Billing Creating a bucket is free. You are charged for actual usage after you store data in the bucket. To avoid unnecessary fees, note the following points when you configure your bucket:


-

Match storage redundancy with resource plans
The resource plan type must exactly match the bucket's storage redundancy type. For example, an LRS resource plan cannot be used to offset the costs of a ZRS bucket, and vice versa. Confirm your selection during creation.

-

Special billing for non-Standard storage classes
Although the Infrequent Access, Archive, Cold Archive, and Deep Cold Archive storage classes have lower storage costs, they have minimum storage durations and incur [data retrieval fees](https://www.alibabacloud.com/help/en/oss/data-processing-fees).


-

Early deletion or modification: If a file is deleted or modified before its minimum storage duration is met, OSS still charges storage fees for the remaining duration.

-

Data reads: Except for the Standard storage class, accessing data in any other storage class incurs additional data retrieval fees.

-

Risks of public access
If you set the ACL to public-read or public-read-write, your data is exposed to the Internet. This can lead to malicious traffic consumption and result in unexpectedly high traffic fees.

## FAQ

### Can I change the bucket name and region after the bucket is created?


No. The name and region cannot be changed after creation, so you must plan them in advance. To make changes, you must use [data migration](https://www.alibabacloud.com/help/en/oss/user-guide/data-migration-overview) to copy the data from the old bucket to a new bucket with the desired settings.


Thank you! We've received your  feedback.