# Query the region of a bucket

If you have created a large number of buckets across regions, you can specify a bucket name to query the region of the bucket. This topic describes how to query the region of a bucket by specifying the bucket name.

## Scenarios


-

Data access optimization: Knowing the region where your bucket is located helps you choose an optimal data access path. For example, if your application is deployed in the same region as your bucket, you can configure access over the internal network to reduce latency and traffic costs.

-

Data storage regions for compliance: Some laws require that data must be stored in the specified regions to meet compliance requirements. In this case, your buckets must reside in the specified regions for compliance reasons.

-

Cross-region data redundancy or disaster recovery: If your application requires high availability, you need to store data in buckets across regions to support data replication and failover.

## Usage notes


-

For more information about the regions supported by OSS, see [OSS regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db).

-

For example, in China (Hangzhou) region, the Location field in the response is `oss-cn-hangzhou`.

## Methods

### Use the OSS console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, click the name of the bucket.


The region of the bucket is displayed in the upper-left corner of the page that appears.

### Use ossbrowser


You can use ossbrowser to perform the same bucket-level operations that you can perform in the OSS console. You can follow the on-screen instructions in ossbrowser to query the region of a bucket. For more information, see [Common operations](https://www.alibabacloud.com/help/en/oss/developer-reference/use-ossbrowser#concept-xmg-h33-wdb).

### Use OSS SDKs


The following sample code provides examples on how to query the region of a bucket by using OSS SDKs for common programming languages. For more information about how to query the region of a bucket by using OSS SDKs for other programming languages, see [Overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // Specify the endpoint of a region that is supported by OSS. Example: https://oss-cn-hangzhou.aliyuncs.com.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the bucket name. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Create an OSS Client instance.
        // Call the shutdown method to release associated resources when the OSS Client is no longer in use.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
        .endpoint(endpoint)
        .credentialsProvider(credentialsProvider)
        .clientConfiguration(clientBuilderConfiguration)
        .region(region)
        .build();

        try {
            String location = ossClient.getBucketLocation(bucketName);
            System.out.println(location);
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

Node.js

`nodejs
const OSS = require('ali-oss')

const client = new OSS({
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that you have configured environment variables OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'oss-cn-hangzhou',
  // Use the V4 signature algorithm.
  authorizationV4: true,
  // Specify the name of your bucket.
  bucket: 'yourBucketName',
  // Specify the public endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
 });

async function getLocation() {
  try {
    const result = await client.getBucketInfo();
    console.log(result.bucket.Location);
  } catch (e) {
    console.log(e);
  }
}

getLocation();
`

C#

`csharp
using Aliyun.OSS;
using Aliyun.OSS.Common;
// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Specify the name of the bucket.
var bucketName = "yourBucketName";

// Create an OSSClient instance.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret);
try
{
    // Query the region of the bucket.
    var result = client.GetBucketLocation(bucketName);
    Console.WriteLine("Get bucket:{0} Info succeeded ", bucketName);
    Console.WriteLine("bucket Location: {0}", result.Location);

}
catch (OssException ex)
{
    Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}",
        ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId);
}
`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* Initialize information about the account that is used to access OSS. */

    /* Specify the endpoint of a region that is supported by OSS. Example: https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";

    /* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
    std::string Region = "yourRegion";

    /* Specify the bucket name. */
    std::string BucketName = "yourBucketName";

    /* Initialize resources such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Query the region of the bucket. */
    GetBucketLocationRequest request(BucketName);
    auto outcome = client.GetBucketLocation(request);

    if (outcome.isSuccess()) {
        std::cout << "getBucketLocation success, location: " << outcome.result().Location() << std::endl;
    }
    else {
        /* Handle exceptions. */
        std::cout << "getBucketLocation fail" <<
        ",code:" << outcome.error().Code() <<
        ",message:" << outcome.error().Message() <<
        ",requestId:" << outcome.error().RequestId() << std::endl;
        ShutdownSdk();
        return -1;
    }

    /* Release resources such as network resources. */
    ShutdownSdk();
    return 0;
}
`

C

`c
#include "oss_api.h"
#include "aos_http_io.h"
/* Specify the endpoint of a region that is supported by OSS. Example: https://oss-cn-hangzhou.aliyuncs.com. */
const char *endpoint = "yourEndpoint";

/* Specify the bucket name. */
const char *bucket_name = "yourBucket";
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
    /* Specify whether to use CNAME to access OSS. The value 0 indicates that CNAME is not used. */
    options->config->is_cname = 0;
    /* Configure network parameters, such as the timeout period. */
    options->ctl = aos_http_controller_create(options->pool, 0);
}
int main(int argc, char *argv)
{
    /* Call the aos_http_io_initialize method in main() to initialize global resources, such as network and memory resources. */
    if (aos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }
    /* Create a pool for memory management. aos_pool_t is equivalent to apr_pool_t. The code that is used to create a memory pool is included in the APR library. */
    aos_pool_t *pool;
    /* Create a memory pool. The value of the second parameter is NULL. This value indicates that the pool does not inherit other memory pools. */
    aos_pool_create(&pool, NULL);
    /* Create and initialize options. This parameter includes global configuration information, such as endpoint, access_key_id, access_key_secret, is_cname, and curl. */
    oss_request_options_t *oss_client_options;
    /* Allocate the memory resources in the memory pool to the options. */
    oss_client_options = oss_request_options_create(pool);
    /* Initialize oss_client_options. */
    init_options(oss_client_options);
    /* Initialize the parameters. */
    aos_string_t bucket;
    aos_string_t oss_location;
    aos_table_t *resp_headers = NULL;
    aos_status_t *resp_status = NULL;
    /* Assign char* data to a bucket of the aos_string_t type. */
    aos_str_set(&bucket, bucket_name);
    /* Query the region of the bucket. */
    resp_status = oss_get_bucket_location(oss_client_options, &bucket, &oss_location, &resp_headers);
    if (aos_status_is_ok(resp_status)) {
        printf("get bucket location succeeded : %s \n", oss_location.data);
    } else {
        printf("get bucket location failed\n");
    }
    /* Release the memory pool. This operation releases memory resources allocated for the request. */
    aos_pool_destroy(pool);
    /* Release the allocated global resources. */
    aos_http_io_deinitialize();
    return 0;
}
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
	flag.StringVar(&bucketName, "bucket", "", "The `name` of the bucket.")
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

	// Create a request to query the region of the bucket.
	request := &oss.GetBucketLocationRequest{
		Bucket: oss.Ptr(bucketName), // The name of the bucket.
	}

	// Execute the request to query the region of the bucket and process the result.
	result, err := client.GetBucketLocation(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to get bucket location %v", err)
	}

	// Display the region of the bucket.
	log.Printf("get bucket location:%#v\n", *result.LocationConstraint)
}

`

Python

`python
import argparse
import alibabacloud_oss_v2 as oss

# Create a command line parameter parser to query the loction of a specified bucket.
parser = argparse.ArgumentParser(description="Get the location of a specified OSS bucket.")

# Specify the --region parameter to indicate the region in which the bucket is located. This parameter is required.
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)

# Specify the --bucket parameter, which specifies the name of the bucket. This command line parameter is required.
parser.add_argument('--bucket', help='The name of the bucket to get the location for.', required=True)

# Specify the --endpoint parameter to indicate the endpoint of the region in which the bucket is located. This parameter is optional.
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS.')

def main():
    """
    Main function used to parse command line arguments and obtain the location information of the specified bucket.
    """

    args = parser.parse_args()  # Parse the command line parameters.

    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Use the default configuration of the SDK and specify the credentials provider and region.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region

    # If the endpoint parameter is provided, specify the endpoint.
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    # Use the configurations to create an OSS Client instance.
    client = oss.Client(cfg)

    # Build a request to fetch the region details of the specified bucket.
    request = oss.GetBucketLocationRequest(bucket=args.bucket)

    # Execute the request and get the response result。
    result = client.get_bucket_location(request)

    # Display the status code, request ID, and location information of the response result.
    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
          f' location: {result.location}'
    )

if __name__ == "__main__":
    main()  # Script entry point, call the main function when the file is run directly
`

PHP

`php
<?php

require_once __DIR__ . '/../vendor/autoload.php'; // Introduce autoload files to load dependency libraries.

use AlibabaCloud\Oss\V2 as Oss;

// Define the description of command-line parameters.
$optsdesc = [
    "region" => ['help' => 'The region in which the bucket is located.', 'required' => True], // The region in which the bucket is located is required. For example: oss-cn-hangzhou.
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // (Optional) The endpoint of the region in which the bucket is located.
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // (Required) The name of the bucket.
];
$longopts = \array_map(function ($key) {
    return "$key:"; // Add a colon (:) to the end of each parameter to indicate that a value is required.
}, array_keys($optsdesc));

// Parse the command-line parameters.
$options = getopt("", $longopts);

// Check whether the required parameters are configured.
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help"; // Display the required but missing parameters.
        exit(1);
    }
}

// Obtain the values of the command line parameters.
$region = $options["region"]; // The region in which the bucket is located.
$bucket = $options["bucket"]; // The name of the bucket.

// Use environment variables to load the AccessKey ID and AccessKey secret.
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // Load access credentials from environment variables.

// Use the default configuration of the SDK.
$cfg = Oss\Config::loadDefault(); // Load the default configuration of the SDK.
$cfg->setCredentialsProvider($credentialsProvider); // Specify the credential provider.
$cfg->setRegion($region); // Specify the region.
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // Specify the endpoint if one is provided.
}

// Create an OSS client instance.
$client = new Oss\Client($cfg);

// Create a request to query the region of a bucket.
$request = new Oss\Models\GetBucketLocationRequest($bucket);

// Call the getBucketLocation method.
$result = $client->getBucketLocation($request);

// Display the result.
printf(
    'status code:' . $result->statusCode . PHP_EOL . // The HTTP status code.
    'request id:' . $result->requestId . PHP_EOL . // The unique ID of the request.
    'bucket location:' . var_export($result->location, true) // The region in which the bucket is located.
);

`


### Use ossutil


You can use ossutil to query the region in which a bucket is located. For more information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


The following sample code shows how to query the region in which `examplebucket` is located.


`bash
ossutil api get-bucket-location --bucket examplebucket
`


For more information, see [get-bucket-location](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-location).

## Related API operation


The operations described above are fundamentally implemented based on the RESTful API, which you can directly call if your business requires a high level of customization. To directly call an API, you must include the signature calculation in your code. For more information, see [GetBucketLocation](https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlocation#reference-e11-qtv-tdb).


Thank you! We've received your  feedback.