# Use bucket tags to classify and manage buckets

Object Storage Service (OSS) allows you to classify and manage buckets by using bucket tags. You can use the bucket tagging feature to configure tags for buckets that are used for different purposes and configure access control lists (ACLs) for buckets that have specific tags.

## Notes


-

Only the bucket owner and users who are granted the `oss:PutBucketTagging` permission can configure tags for buckets. If other users attempt to configure tags for buckets, the 403 Forbidden message that contains the AccessDenied error code is returned.

-

You can configure up to 20 tags (key-value pairs) for each bucket.

-

The key and value of a tag must be encoded in UTF-8.

-

The key can be up to 64 characters in length. It is case-sensitive and cannot be empty. The key cannot start with `http://`, `https://`, or `Aliyun`. These prefixes are not case-sensitive.

-

The value of a tag can be up to 128 characters in length and can be empty.

## Procedure

### Use the OSS console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left-side navigation tree, choose Bucket Settings > Bucket Tagging.

-

On the Bucket Tagging page, click Create Tag.

-

Click + Tag to enter the key and value of a tag, or select an existing tag.


To add multiple tags to the bucket, click + Tag.

-

Click Save.

### Use OSS SDKs


The following code provides examples on how to configure tags for a bucket by using OSS SDKs for common programming languages. For more information about how to configure tags for a bucket by using OSS SDKs for other programming languages, see [Overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.SetBucketTaggingRequest;

public class Demo {

    public static void main(Stringargs) throws Exception {
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Create an OSSClient instance.
        // Call the shutdown method to release resources when the OSSClient is no longer in use.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
        .endpoint(endpoint)
        .credentialsProvider(credentialsProvider)
        .clientConfiguration(clientBuilderConfiguration)
        .region(region)
        .build();

        try {
            // Configure tags for the bucket.
            SetBucketTaggingRequest request = new SetBucketTaggingRequest(bucketName);
            // Specify the key and value of the tag. For example, set the key to owner and value to John.
            request.setTag("owner", "John");
            request.setTag("location", "hangzhou");
            ossClient.setBucketTagging(request);
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
  // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourregion',
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that you have configured environment variables OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // Specify the name of your bucket.
  bucket: 'yourBucketName',
});

// Configure tags for the bucket.
async function putBucketTags(bucketName, tag) {
  try {
    const result = await client.putBucketTags(bucketName, tag);
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

const tag = { a: '1', b: '2' };
putBucketTags('bucketName', tag)
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
	region     string // The region in which the bucket is located.
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

	// Create an OSSClient instance.
	client := oss.NewClient(cfg)

	// Create a request to configure tags for the bucket.
	request := &oss.PutBucketTagsRequest{
		Bucket: oss.Ptr(bucketName), // The name of the bucket.
		Tagging: &oss.Tagging{
			&oss.TagSet{
				oss.Tag{
					{
						Key:   oss.Ptr("k1"), // The key of a tag.
						Value: oss.Ptr("v1"), // The value of a tag.
					},
					{
						Key:   oss.Ptr("k2"), // The key of a tag.
						Value: oss.Ptr("v2"), // The value of a tag.
					},
					{
						Key:   oss.Ptr("k3"), // The key of a tag.
						Value: oss.Ptr("v3"), // The value of a tag.
					},
				},
			},
		},
	}

	// Send the request to configure tags for a bucket.
	result, err := client.PutBucketTags(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put bucket tags %v", err)
	}

	// Display the result of the tag configuration.
	log.Printf("put bucket tags result:%#v\n", result)
}

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
c.SetRegion(region);
try
{
    // Configure tags for the bucket.
    var setRequest = new SetBucketTaggingRequest(bucketName);

    var tag1 = new Tag
    {
        Key = "project",
        Value = "projectone"
    };

    var tag2 = new Tag
    {
        Key = "user",
        Value = "jsmith"
    };

    setRequest.AddTag(tag1);
    setRequest.AddTag(tag2);
    client.SetBucketTagging(setRequest);
    Console.WriteLine("Set bucket:{0} Tagging succeeded ", bucketName);
}
catch (OssException ex)
{
    Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}",
        ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId);
}
catch (Exception ex)
{
    Console.WriteLine("Failed with error info: {0}", ex.Message);
}
`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* Initialize information about the account used to access OSS. */

    /* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";

    /* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
    std::string Region = "yourRegion";

    /* Specify the name of the bucket. Example: examplebucket. */
    std::string BucketName = "examplebucket";

    /* Initialize resources such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Configure tags for the bucket. */
    SetBucketTaggingRequest request(BucketName);
    Tag tag1("yourTagkey1","yourTagValue1");
    Tag tag2("yourTagkey2", "yourTagValue2");
    TagSet tagset;
    tagset.push_back(tag1);
    tagset.push_back(tag2);
    Tagging taging;
    taging.setTags(tagset);
    request.setTagging(taging);
    auto outcome = client.SetBucketTagging(request);

    if (outcome.isSuccess()) {
            std::cout << " SetBucketTagging success " << std::endl;
    }
    else {
        /* Handle exceptions. */
        std::cout << "SetBucketTagging fail" <<
        ",code:" << outcome.error().Code() <<
        ",message:" << outcome.error().Message() <<
        ",requestId:" << outcome.error().RequestId() << std::endl;
        return -1;
    }

    /* Release resources such as network resources. */
    ShutdownSdk();
    return 0;
}
`

Python

`python
import argparse
import alibabacloud_oss_v2 as oss

# Create a command-line parameter parser for parsing parameters from the command line.
parser = argparse.ArgumentParser(description="put bucket tags sample")

# (Required) Specify the region parameter, which specifies the region in which the bucket is located.
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)

# (Required) Specify the --bucket parameter, which specifies the name of the bucket.
parser.add_argument('--bucket', help='The name of the bucket.', required=True)

# (Optional) Specify the --endpoint parameter, which specifies the endpoint that other services can use to access OSS.
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')

def main():
    # Parse the command-line parameters.
    args = parser.parse_args()

    # Load access credentials (AccessKey ID and AccessKey secret) from environment variables.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load the default configurations of the SDK.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located.
    cfg.region = args.region

    # If a custom endpoint is provided, update the endpoint attribute with the provided endpoint.
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    # Use the preceding configurations to initialize the OSSClient instance.
    client = oss.Client(cfg)

    # Call the put_bucket_tags method to configure tags for the bucket.
    result = client.put_bucket_tags(
        oss.PutBucketTagsRequest(
            bucket=args.bucket,  # The name of the bucket.
            tagging=oss.Tagging(  # Create a tag set.
                tag_set=oss.TagSet(  # The tag set contains multiple tags.
                    tags=[  # Define a list of tags.
                        oss.Tag(  # The first tag.
                            key='test_key',  # The tag key.
                            value='test_value',  # The tag value.
                        ),
                        oss.Tag(  # The second tag.
                            key='test_key2',  # The tag key.
                            value='test_value2',  # The tag value.
                        ),
                    ],
                ),
            ),
        )
    )

    # Display the HTTP status code of the operation and request ID.
    print(f'status code: {result.status_code}, '  # The HTTP status code, which indicates whether the request succeeded.
          f'request id: {result.request_id}')    # The request ID, which is used to debug or trace a request.


if __name__ == "__main__":
    # Specify the entry points in the main function of the script when the script is directly run.
    main()

`

PHP

`php
<?php

// Automatically load objects and dependency libraries.
require_once __DIR__ . '/../vendor/autoload.php';

use AlibabaCloud\Oss\V2 as Oss;

// Specify command line parameters.
$optsdesc = [
    "region" => ['help' => 'The region in which the bucket is located', 'required' => True], // The region parameter is required.
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // The endpoint parameter is optional.
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

// Use environment variables to load the credential information (AccessKey ID and AccessKey secret).
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// Use the default configuration of the SDK.
$cfg = Oss\Config::loadDefault();

// Specify the credential provider.
$cfg->setCredentialsProvider($credentialsProvider);

// Specify the region.
$cfg->setRegion($region);

// Specify the endpoint if one is provided.
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// Create an OSSClient instance.
$client = new Oss\Client($cfg);

// Create tags containing multiple key-value pairs for the bucket.
$tagging = new Oss\Models\Tagging(
    tagSet: new Oss\Models\TagSet(
        tags: [new Oss\Models\Tag(key: 'key1', value: 'value1'), new Oss\Models\Tag(key: 'key2', value: 'value2')]
    )
);

// Create a request object for configuring tags and include the tagging information.
$request = new Oss\Models\PutBucketTagsRequest(bucket: $bucket, tagging: $tagging);

// Configure tags for the bucket using the putBucketTags method.
$result = $client->putBucketTags($request);

// Output the result.
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP status code.
    'request id:' . $result->requestId // Unique ID of the request.
);

`


### Use ossutil


For more information about how to configure bucket tags by using ossutil, see [Add tags to a bucket or modify the tags of a bucket](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-tagging#section-ri0-ucz-koy).

### Use the OSS API


If your business requires a high level of customization, you can directly call RESTful APIs. To directly call an API, you must include the signature calculation in your code. For more information, see [PutBucketTags](https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckettags#concept-261782).

## Example


In a company, each project is assigned a distinct OSS Bucket for data storage. By tagging these buckets associated with different projects, you can enforce fine-grained access control through RAM policies, ensuring that users from each project can only read and write data in buckets with designated tags. This approach effectively prevents unauthorized cross-project access. For more information, see [Authorize a RAM user to read and write data in buckets with specific tags](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#47e0a1f8d9b0b).


Thank you! We've received your  feedback.