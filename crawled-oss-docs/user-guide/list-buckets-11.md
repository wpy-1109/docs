# How to list buckets in alphabetical order

Managing a large number of buckets manually is inefficient and error-prone. You can programmatically list all or some of your buckets to support automated tasks such as asset inventories, bulk operations, and permission audits. Buckets are listed in alphabetical order.

## How it works


The behavior of the list buckets operation depends on request parameters and pagination.

#### Request parameters


Set the following request parameters to filter and control the results.

















| Parameter | Description |
| --- | --- |
| prefix | Filter by prefix: Limits the response to buckets whose names begin with this string. |
| marker | Pagination token: Specifies the starting position for the list. Results begin with the first bucket that follows this marker alphabetically. |
| max-keys | Number of items per page: Specifies the maximum number of buckets to return per response. Valid values: 1–1000. Default: 100. |


#### Pagination


A basic list operation returns one page of data by default. If the number of buckets exceeds the per-page limit (determined by `max-keys`), you must use pagination to retrieve the complete list.


Pagination relies on two key fields in the server's response:


-

isTruncated (Boolean value): If true, more pages of data are available.

-

nextMarker (string): The marker for the start of the next page.


The core logic of pagination is as follows: Check the `isTruncated` flag. If it is true, use the `nextMarker` value from the response as the `marker` for your next request. Repeat this process until `isTruncated` is false.
Some SDKs (such as Python v2, Go v2, PHP v2, and C# v2) provide a Paginator that handles this loop automatically. For other SDKs, you must implement this logic yourself.
## List all buckets


This is the most basic list operation.

## Console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the navigation pane on the left, click Buckets.


The Buckets page displays all buckets under your account by default. To quickly get the number of buckets and their properties, click the export to CSV icon ![download](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/6269628461/p389377.jpg)in the upper-right corner.

## ossutil


You can use ossutil, a command line interface, to list buckets. For information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


The following command lists all buckets owned by the requester.


`bash
ossutil api list-buckets
`


For more information about this command, see [list-buckets (get-service)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-get-service).

## SDK


The following sections provide sample code for listing buckets using common SDKs. For sample code that uses other SDKs, see [SDK overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).

## Java


`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.Bucket;

import java.util.List;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();

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
            // List all buckets in all regions within the current Alibaba Cloud account.
            List<Bucket> buckets = ossClient.listBuckets();
            for (Bucket bucket : buckets) {
                System.out.println(" - " + bucket.getName());
            }
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


## Python


`python
import argparse
import alibabacloud_oss_v2 as oss

# Create a command line parameter parser and describe the purpose of the script. The example describes how to list all buckets in OSS.
parser = argparse.ArgumentParser(description="list buckets sample")

# Specify the command line parameter --region, which specifies the region in which the bucket is located. This parameter is required.
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
# Specify the command line parameter --endpoint, which specifies the endpoint that other services can use to access OSS. This parameter is optional.
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')

def main():
    # Parse the parameters provided in the command line to obtain the values entered by the user.
    args = parser.parse_args()

    # Load the authentication information required to access OSS from the environment variables.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Use the default configurations of the SDK to create a configuration object and specify the credential provider.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region

    # If a custom endpoint is provided, modify the endpoint parameter in the configuration object.
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    # Use the preceding configuration to initialize the OSSClient instance and allow the instance to interact with OSS.
    client = oss.Client(cfg)

    # Create a paginator to allow the ListBuckets operation to list a large number of buckets.
    paginator = client.list_buckets_paginator()

    # Traverse the listed buckets.
    for page in paginator.iter_page(oss.ListBucketsRequest()):
        # Display the name, location, creation date, and resource group ID of each bucket on each page.
        for o in page.buckets:
            print(f'Bucket: {o.name}, Location: {o.location}, Created: {o.creation_date}, Resource Group ID: {o.resource_group_id}')

# Call the main function to start the processing logic when the script is directly run.
if __name__ == "__main__":
    main() # Specify the entry points in functions of the script. The control program flow starts here.
`


## Go


`go
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

// Define the global variables
var (
	region string // The region.
)

// Use the init function to initialize command line parameters.
func init() {
	flag.StringVar(®ion, "region", "", "The region in which the bucket is located.")
}

func main() {
	// Parse the command line parameters.
	flag.Parse()

	// Check whether the region is empty.
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	// Load the default configurations and specify the credential provider and region.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region)

	// Create an OSSClient instance.
	client := oss.NewClient(cfg)

	// Create a request to list buckets.
	request := &oss.ListBucketsRequest{}

	// Create a paginator.
	p := client.NewListBucketsPaginator(request)

	var i int
	log.Println("kets:")

	// Traverse each page in the paginator.
	for p.HasNext() {
		i++

		// Obtain the data of the next page.
		page, err := p.NextPage(context.TODO())
		if err != nil {
			log.Fatalf("failed to get page %v, %v", i, err)
		}

		// Display information about each bucket on the page.
		for _, b := range page.Buckets {
			log.Printf("Bucket: %v, StorageClass: %v, Location: %v\n", oss.ToString(b.Name), oss.ToString(b.StorageClass), oss.ToString(b.Location))
		}
	}

}
`


## C#


`csharp
using OSS = AlibabaCloud.OSS.V2; // Create an alias for Alibaba Cloud OSS SDK to simplify subsequent use

var region = "cn-hangzhou"; // Required. Set the region where the bucket is located. In this example, the region is China (Hangzhou), so Region is set to cn-hangzhou
var endpoint = null as string;  // Optional. Specify the domain name to access the OSS service. For China (Hangzhou), the endpoint is https://oss-cn-hangzhou.aliyuncs.com

// Load the default configuration of the OSS SDK, which automatically reads credential information (such as AccessKey) from environment variables
var cfg = OSS.Configuration.LoadDefault();
// Explicitly set to use environment variables to obtain credentials for authentication (format: OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// Set the bucket region in the configuration
cfg.Region = region;
// If an endpoint is specified, override the default endpoint
if(endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// Create an OSS client instance using the configuration information
using var client = new OSS.Client(cfg);

// Create a paginator for the ListBuckets operation to handle paginated results
// ListBucketsRequest is a request model defined by the SDK, using the default constructor here (to get all buckets)
var paginator = client.ListBucketsPaginator(new OSS.Models.ListBucketsRequest());

Console.WriteLine("Buckets:");
await foreach (var page in paginator.IterPageAsync())
{
// Iterate through each bucket on the current page
    foreach (var bucket in page.Buckets ?? )
    {
    // Print bucket information: name, storage class, and location
    Console.WriteLine($"Bucket:{bucket.Name}, {bucket.StorageClass}, {bucket.Location}");
    }
}
`


## Node.js


`nodejs
const OSS = require('ali-oss');

const client = new OSS({
  // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourregion',
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that you have configured environment variables OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // Specify the name of your bucket.
  bucket: 'yourBucketName',
});

async function listBuckets() {
  try {
    // List all buckets in all regions within the current Alibaba Cloud account.
    const result = await client.listBuckets();
    console.log(result);
  } catch (err) {
    console.log(err);
  }
}

listBuckets();
`


## Harmony


`arkts
import Client, { RequestError } from '@aliyun/oss';

// Create an OSS client instance
const client = new Client({
  // Replace with the Access Key ID of the STS temporary access credential
  accessKeyId: 'yourAccessKeyId',
  // Replace with the Access Key Secret of the STS temporary access credential
  accessKeySecret: 'yourAccessKeySecret',
  // Replace with the Security Token of the STS temporary access credential
  securityToken: 'yourSecurityToken',
});

// List all buckets
const listBuckets = async () => {
  try {
    // Call the listBuckets method to list all buckets
    const res = await client.listBuckets({});

    // Print the returned result
    console.log(JSON.stringify(res));
  } catch (err) {
    // Catch and handle request errors
    if (err instanceof RequestError) {
      console.log('Error code: ', err.code); // Error code
      console.log('Error message: ', err.message); // Error description
      console.log('Request ID: ', err.requestId); // Unique identifier of the request
      console.log('HTTP status code: ', err.status); // HTTP response status code
      console.log('Error category: ', err.ec); // Error category
    } else {
      console.log('Unknown error: ', err); // Non-RequestError type error
    }
  }
};

// Call the function to list all buckets
listBuckets();

`


## Ruby


`ruby
require 'aliyun/oss'

client = Aliyun::OSS::Client.new(
  # In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)
# List all buckets in all regions within the current account.
buckets = client.list_buckets
buckets.each { |b| puts b.name }
`


## Android


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-4).


`androidjava
// List all buckets that belong to the current Alibaba Cloud account in all regions.
ListBucketsRequest request = new ListBucketsRequest();
ossClient.asyncListBuckets(request, new OSSCompletedCallback<ListBucketsRequest, ListBucketsResult>() {
    @Override
    public void onSuccess(ListBucketsRequest request, ListBucketsResult result) {
        List<OSSBucketSummary> buckets = result.getBuckets();
        for (int i = 0; i < buckets.size(); i++) {
            Log.i("info", "name: " + buckets.get(i).name + " "
                    + "location: " + buckets.get(i).location);
        }
    }

    @Override
    public void onFailure(ListBucketsRequest request, ClientException clientException, ServiceException serviceException) {
        // Handle request exceptions.
        if (clientException != null) {
            // Handle client-side exceptions, such as network errors.
            clientException.printStackTrace();
        }
        if (serviceException != null) {
            // Handle server-side exceptions.
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
`


## C++


`c++
#include <alibabacloud/oss/OssClient.h>
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* Initialize information about the account that is used to access OSS. */

    /* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";

    /* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
    std::string Region = "yourRegion";

    /* Initialize resources, such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* List all buckets that belong to the current Alibaba Cloud account. */
    ListBucketsRequest request;
    auto outcome = client.ListBuckets(request);

    if (outcome.isSuccess()) {
        /* Display information about the buckets. */
        std::cout <<" success, and bucket count is" << outcome.result().Buckets().size() << std::endl;
        std::cout << "Bucket name is" << std::endl;
        for (auto result : outcome.result().Buckets())
        {
            std::cout << result.Name() << std::endl;
        }
    }
    else {
        /* Handle exceptions. */
        std::cout << "ListBuckets fail" <<
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


## iOS


`objectc
OSSGetServiceRequest * getService = [OSSGetServiceRequest new];
// List all buckets in all regions within the current Alibaba Cloud account.
OSSTask * getServiceTask = [client getService:getService];
[getServiceTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        OSSGetServiceResult * result = task.result;
        NSLog(@"buckets: %@", result.buckets);
        NSLog(@"owner: %@, %@", result.ownerId, result.ownerDispName);
        [result.buckets enumerateObjectsUsingBlock:^(id  _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
            NSDictionary * bucketInfo = obj;
            NSLog(@"BucketName: %@", [bucketInfo objectForKey:@"Name"]);
            NSLog(@"CreationDate: %@", [bucketInfo objectForKey:@"CreationDate"]);
            NSLog(@"Location: %@", [bucketInfo objectForKey:@"Location"]);
        }];
    } else {
        NSLog(@"get service failed, error: %@", task.error);
    }
    return nil;
}];
// Implement synchronous blocking to wait for the task to complete.
// [getServiceTask waitUntilFinished];
`


## C


`c
#include "oss_api.h"
#include "aos_http_io.h"
/* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
const char *endpoint = "yourEndpoint";
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
    /* Call the aos_http_io_initialize method in main() to initialize global resources, such as network resources and memory resources. */
    if (aos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }
    /* Create a memory pool to manage memory. aos_pool_t is equivalent to apr_pool_t. The code used to create a memory pool is included in the APR library. */
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
    aos_table_t *resp_headers = NULL;
    aos_status_t *resp_status = NULL;
    oss_list_buckets_params_t *params = NULL;
    oss_list_bucket_content_t *content = NULL;
    int size = 0;
    params = oss_create_list_buckets_params(pool);
    /* List buckets. */
    resp_status = oss_list_bucket(oss_client_options, params, &resp_headers);
    if (aos_status_is_ok(resp_status)) {
        printf("list buckets succeeded\n");
    } else {
        printf("list buckets failed\n");
    }
    /* Display the buckets. */
    aos_list_for_each_entry(oss_list_bucket_content_t, content, &params->bucket_list, node) {
        printf("BucketName: %s\n", content->name.data);
        ++size;
    }
    /* Release the memory pool. This operation releases the memory resources allocated for the request. */
    aos_pool_destroy(pool);
    /* Release the allocated global resources. */
    aos_http_io_deinitialize();
    return 0;
}
`


## ossbrowser


After you log on to ossbrowser 2.0, click the All button on the left to display all buckets that belong to your account. For information about how to install and log on to ossbrowser 2.0, see [Install ossbrowser 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/installing-the-ossbrowser-2-0#2e1e5eee641da) and [Log on to ossbrowser 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/login-to-ossbrowser-2-0#85a24a9dcfg7v).


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7482101671/p886969.png)

## API


The preceding operations are based on API calls. If your program requires a high level of customization, you can directly send REST API requests. To do this, you must manually write code to calculate signatures. For more information, see [ListBuckets (GetService)](https://www.alibabacloud.com/help/en/oss/developer-reference/listbuckets#reference-ahf-k4t-tdb).

## List buckets with a specified prefix


You can set the `prefix` parameter to filter results on the server side. This returns only buckets whose names match the specified prefix.

## ossutil


List all buckets that have the prefix `example` owned by the requester.


`bash
ossutil api list-buckets --prefix example
`


For more information, see [list-buckets (get-service)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-get-service).

## SDK

## Java


For the complete sample code, see [List buckets (Java SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets).


`java
// 1. Create a request object.
ListBucketsRequest listBucketsRequest = new ListBucketsRequest();

// 2. Set the prefix parameter.
listBucketsRequest.setPrefix("example");

// 3. Execute the request.
BucketList bucketList = ossClient.listBuckets(listBucketsRequest);
`


## Python


For the complete sample code, see [List buckets (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-using-oss-sdk-for-python-v2).


`python
# Pass a request object with the prefix parameter to the iter_page method of the paginator.
for page in paginator.iter_page(oss.ListBucketsRequest(
    prefix='example'
)):
    # ... Loop processing ...
`


## Go


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-list-buckets).


`go
// 1. Create a request object and set the Prefix field.
request := &oss.ListBucketsRequest{
    Prefix: oss.Ptr("example"),
}

// 2. Use this request object to create a paginator.
p := client.NewListBucketsPaginator(request)
`


## Node.js


For the complete sample code, see [List buckets (Node.js SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-8).


`nodejs
// Specify the prefix in the parameter object of the listBuckets method.
const result = await client.listBuckets({
  prefix: 'example'
});
`


## Harmony


For the complete sample code, see [List buckets (Harmony SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-storage-space-using-harmony).


`arkts
// Key code: Pass an object containing the prefix when calling listBuckets.
const res = await client.listBuckets({
  prefix: 'bucketNamePrefix'
});
`


## Ruby


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-7).


`ruby
# Key code: Call list_buckets with :prefix as a parameter.
buckets = client.list_buckets(:prefix => 'example')
`


## List buckets after a specified position


You can set the `marker` parameter to specify the starting position for the list. This is a key step in implementing manual pagination.

## ossutil


List all buckets owned by the requester that come after examplebucket.


`bash
ossutil api list-buckets --marker examplebucket
`


For more information, see [list-buckets (get-service)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-get-service).

## SDK

## Java


For the complete sample code, see [List buckets (Java SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets).


`java
// 1. Set marker to "examplebucket" to list buckets that come after "examplebucket".
String nextMarker = "examplebucket";
BucketList bucketListing;

do {
    // 2. Send a request with the current marker.
    bucketListing = ossClient.listBuckets(new ListBucketsRequest()
            .withMarker(nextMarker)
            .withMaxKeys(200));

    // 3. Update the marker to get the next page.
    nextMarker = bucketListing.getNextMarker();
} while (bucketListing.isTruncated());
`


## Python


For the complete sample code, see [List buckets (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-using-oss-sdk-for-python-v2).


`python
# Set marker to "example-bucket" to list buckets that come after "example-bucket".
for page in paginator.iter_page(oss.ListBucketsRequest(
    marker="example-bucket"
)):
    # ... Iterate through page ...
`


## Go


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-list-buckets).


`go
// Set marker to "example-bucket" to list buckets that come after "example-bucket".
request := &oss.ListBucketsRequest{
    Marker: oss.Ptr("example-bucket"),
}

// Use this request to create a paginator.
p := client.NewListBucketsPaginator(request)
`


## Harmony


For the complete sample code, see [List buckets (Harmony SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-storage-space-using-harmony).


`arkts
// Set the initial value of marker to "examplebucket" to specify the starting point for the listing.
let marker: string | undefined = "examplebucket";
let isTruncated = true;

while (isTruncated) {
  // Use the current marker in the request.
  const res = await client.listBuckets({
    marker
  });
  // ...
  // Update the marker for the next loop.
  marker = res.data.nextMarker;
  isTruncated = res.data.isTruncated;
}
`


## Node.js


For the complete sample code, see [List buckets (Node.js SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-8).


`nodejs
// Set marker to 'examplebucket' to list buckets that come after 'examplebucket'.
const result = await client.listBuckets({
  marker: 'examplebucket'
});
`


## Android


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-4).


`androidjava
ListBucketsRequest request = new ListBucketsRequest();
// Set marker to "examplebucket" to list buckets that come after "examplebucket".
request.setMarker("examplebucket");

ossClient.asyncListBuckets(request, ...);
`


## iOS


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-10).


`objectc
OSSGetServiceRequest * getService = [OSSGetServiceRequest new];

// Set marker to "examplebucket" to list buckets that come after "examplebucket".
getService.marker = @"examplebucket";

// Use this request object to start an asynchronous task.
OSSTask * getServiceTask = [client getService:getService];
`


## List buckets in a specified resource group


You can list buckets based on a specified resource group ID.

## ossutil


List all buckets in the resource group with the ID `rg-123`.


`bash
ossutil api list-buckets --resource-group-id rg-123
`


For more information, see [list-buckets (get-service)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-get-service).

## SDK

## Java


For the complete sample code, see [List buckets (Java SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets).


`java
ListBucketsRequest listBucketsRequest = new ListBucketsRequest();

// Key code: Set the ID of the resource group to filter by.
listBucketsRequest.setResourceGroupId("rg-aek27tc");

// Pass the configured request object to the listBuckets method.
BucketList bucketList = ossClient.listBuckets(listBucketsRequest);
`


## Python


For the complete sample code, see [List buckets (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-using-oss-sdk-for-python-v2).


`python
# Key code: Construct a request in the iter_page method and specify resource_group_id.
for page in paginator.iter_page(oss.ListBucketsRequest(
    resource_group_id="rg-aek27tc"
)):
    # ... Iterate through page ...
`


## Go


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-list-buckets).


`go
// Key code: Create a request and set the ResourceGroupId field.
request := &oss.ListBucketsRequest{
    ResourceGroupId: oss.Ptr("rg-aek27tc"),
}

// Use this request to create a paginator.
p := client.NewListBucketsPaginator(request)
`


## PHP


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-list-buckets).


`php
// Key code: Construct a request in the iterPage method and specify resourceGroupId.
$iter = $paginator->iterPage(new Oss\Models\ListBucketsRequest(
    resourceGroupId: "rg-aekzfalvmw2sxby"
));
`


## Control the number of items returned per request


You can set the `max-keys` parameter to control the number of buckets returned in a single request. This parameter defines the page size.

## ossutil


Limit the number of buckets returned in this call to a maximum of 100.


`bash
ossutil api list-buckets --max-keys 100
`


For more information, see [list-buckets (get-service)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-get-service).

## SDK

## Java


For the complete sample code, see [List buckets (Java SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets).


`java
ListBucketsRequest listBucketsRequest = new ListBucketsRequest();

// Key code: Set the maxKeys parameter to 500 to limit the number of buckets returned to a maximum of 500.
listBucketsRequest.setMaxKeys(500);

// Pass the configured request object to the method.
BucketList bucketList = ossClient.listBuckets(listBucketsRequest);
`


## Python


For the complete sample code, see [List buckets (Python SDK V2)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-using-oss-sdk-for-python-v2).


`python
# Key code: Pass the max_keys parameter with a value of 10 when creating ListBucketsRequest.
# This causes the paginator to retrieve a maximum of 10 buckets per request.
for page in paginator.iter_page(oss.ListBucketsRequest(
    max_keys=10
)):
    # ... Iterate through page ...
`


## Go


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-list-buckets).


`go
// Key code: Set the MaxKeys field to 5 when creating ListBucketsRequest.
// The paginator will use this setting to retrieve a maximum of 5 buckets per request.
request := &oss.ListBucketsRequest{
    MaxKeys: 5,
}

p := client.NewListBucketsPaginator(request)
`


## Node.js


For the complete sample code, see [List buckets (Node.js SDK)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-8).


`nodejs
// Key code: Pass an object containing the 'max-keys' property when calling listBuckets.
// 'max-keys' is set to 500 to limit the number of buckets returned to a maximum of 500.
const result = await client.listBuckets({
  'max-keys': 500
});
`


## Android


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-4).


`androidjava
ListBucketsRequest request = new ListBucketsRequest();

// Key code: Set the maxKeys parameter to 500 to limit the number of buckets returned in this asynchronous request to a maximum of 500.
request.setMaxKeys(500);

ossClient.asyncListBuckets(request, ...);
`


## iOS


For the complete sample code, see [List buckets](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-10).


`objectc
OSSGetServiceRequest * getService = [OSSGetServiceRequest new];

// Key code: Set the maxKeys property of the getService request object to 500.
getService.maxKeys = 500;

OSSTask * getServiceTask = [client getService:getService];
`


## Limitations


You cannot use a Transfer Acceleration endpoint to list buckets. The Transfer Acceleration service resolves only third-level domain names that include a bucket name (for example, `https://BucketName.oss-accelerate.aliyuncs.com`), while the list buckets operation uses a root endpoint without a bucket name (for example, `https://oss-cn-hangzhou.aliyuncs.com`).


Thank you! We've received your  feedback.