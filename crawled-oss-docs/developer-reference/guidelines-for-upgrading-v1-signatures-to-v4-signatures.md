# Guide to upgrading from Signature V1 to Signature V4

To enhance security, Object Storage Service (OSS) is phasing out Signature V1. Upgrade to Signature V4 as soon as possible to ensure your applications continue to function correctly.

## How to upgrade from Signature V1 to Signature V4


Follow the corresponding guide to complete the upgrade based on your current usage.














(https://mvnrepository.com/artifact/com.aliyun.oss/aliyun-sdk-oss/3.17.4)


(https://github.com/aliyun/alibabacloud-oss-python-sdk-v2)


(https://github.com/aliyun/aliyun-oss-python-sdk)


(https://github.com/aliyun/alibabacloud-oss-go-sdk-v2)


(https://github.com/aliyun/aliyun-oss-go-sdk)


(https://github.com/aliyun/alibabacloud-oss-php-sdk-v2)


(https://github.com/aliyun/aliyun-oss-php-sdk)


(https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2)


(https://github.com/aliyun/aliyun-oss-csharp-sdk)


(https://github.com/ali-sdk/ali-oss)


(https://github.com/aliyun/aliyun-oss-cpp-sdk)


(https://github.com/aliyun/aliyun-oss-c-sdk)


(https://github.com/aliyun/alibabacloud-oss-swift-sdk-v2)


(https://github.com/aliyun/aliyun-oss-ios-sdk)


(https://github.com/aliyun/aliyun-oss-android-sdk)


(https://www.alibabacloud.com/help/en/oss/install-ossutil2#87f83bc380nla)


(https://github.com/aliyun/ossutil/releases)


(https://www.alibabacloud.com/help/en/oss/developer-reference/install-ossfs-2-0#98192769e00ws)


(https://www.alibabacloud.com/help/en/oss/developer-reference/install-ossfs-1-0#title-sog-1f0-t50)


| Tool | Type | Versions that support V4 | Upgrade guide |
| --- | --- | --- | --- |
| OSS SDK | Java | Version 3.17.4 and later | OSS SDK |
| Python V2 | All versions |
| Python V1 | Version 2.18.4 and later |
| Go V2 | All versions |
| Go V1 | Version 3.0.2 and later |
| PHP V2 | All versions |
| PHP V1 | Version 2.7.0 and later |
| C# V2 | All versions |
| C# V1 | Version 2.14.0 and later |
| JavaScript | Version 6.20.0 and later |
| C++ | Version 1.10.0 and later |
| C | Version 3.11.0 and later |
| Swift | All versions |
| Objective-C | Version 2.11.1 and later |
| Android | Version 2.3 and later |
| ossutil | ossutil 2.0 | All versions | ossutil |
| ossutil 1.0 | Version 1.7.12 and later |
| ossfs | ossfs 2.0 | All versions | ossfs |
| ossfs 1.0 | Version 1.91.4 and later |
| API (manual signature construction) | For information about how to upgrade a manually constructed V1 signature algorithm to V4, see API (manual signature construction). |
| OSS console | OSS upgrades automatically. The process is transparent to users. |


### OSS SDK

## Java


-

Upgrade [OSS SDK for Java](https://github.com/aliyun/aliyun-oss-java-sdk) to version 3.17.4 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `SignVersion.V4`.

#### Code sample


`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;

public class OSSClientV4 {

    public static void main(Stringargs) throws Exception {
        // Specify the endpoint of the region in which the bucket is located. In this example, the endpoint of the China (Hangzhou) region is used.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Specify the ID of the region of the bucket. In this example, the ID of the China (Hangzhou) region is used: cn-hangzhou.
        String region = "cn-hangzhou";

        // Obtain credentials from the environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();

        // Create an OSSClient instance.
        // When you no longer use the OSSClient instance, call the shutdown method to release resources.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        // Explicitly declare the use of the V4 signature algorithm.
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(credentialsProvider)
                .clientConfiguration(clientBuilderConfiguration)
                .region(region)
                .build();

        // Use the OSSClient instance to initiate requests, such as uploading, downloading, or managing objects.

        // When you no longer use the OSSClient instance, call the shutdown method to release resources.
        ossClient.shutdown();
    }
}
`


## Python

## Python V2


-

All versions of [OSS SDK for Python V2](https://github.com/aliyun/alibabacloud-oss-python-sdk-v2) support Signature V4 by default.

-

When you initialize an OSS Client with Signature V4, you must perform the following step:


Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

#### Code sample


`
import alibabacloud_oss_v2 as oss

def main():
    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load the default configuration of the SDK and specify the credential provider.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider

    # Method 1: Specify only the region.
    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = 'cn-hangzhou'

    # # Method 2: Specify the endpoint and region.
    # # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    # cfg.region = 'cn-hangzhou'
    # # Specify the public endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
    # # To use the HTTP protocol, set the endpoint to http://oss-cn-hangzhou.aliyuncs.com.
    # cfg.endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'

    # Use the configuration to create a Client instance.
    client = oss.Client(cfg)

    # Use the Client instance to perform subsequent operations.

# Call the main function when the script is directly run.
if __name__ == "__main__":
    main()  # The entry point of the script. When the script is directly run, the main function is called.
`


## Python V1


-

Upgrade [OSS SDK for Python V1](https://github.com/aliyun/aliyun-oss-python-sdk) to version 2.18.4 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `oss2.ProviderAuthV4`.

#### Code sample


`python
# -*- coding: utf-8 -*-
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the environment variables are configured.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())
# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = 'yourEndpoint'
# Specify the region of the endpoint. Example: cn-hangzhou.
region = 'cn-hangzhou'

# Specify the name of the bucket.
bucket = oss2.Bucket(auth, endpoint, 'examplebucket', region=region)
`


## Go

## Go V2


-

All versions of [OSS SDK for Go V2](https://github.com/aliyun/aliyun-oss-go-sdk) support Signature V4 by default.

-

When you initialize an OSS Client with Signature V4, you must perform the following step:


Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

#### Code sample


`
package main

import (
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

func main() {
	// Method 1: Specify only the region
	// Specify the region where the bucket is located. For example, if the region is China (Hangzhou), specify the region as cn-hangzhou
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion("cn-hangzhou")

	// Method 2: Specify both the region and endpoint
	// Specify the region where the bucket is located. For example, if the region is China (Hangzhou), specify the region as cn-hangzhou
	// Specify the public endpoint that corresponds to the region where the bucket is located. For example, if the region is China (Hangzhou), specify the endpoint as 'https://oss-cn-hangzhou.aliyuncs.com'. If you want to use the HTTP protocol, specify 'http://oss-cn-hangzhou.aliyuncs.com' when you specify the endpoint
	// cfg := oss.LoadDefaultConfig().
	//     WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
	//     WithRegion("cn-hangzhou").
	//     WithEndpoint("https://oss-cn-hangzhou.aliyuncs.com")

	// Create an OSS client
	client := oss.NewClient(cfg)

	// Use the client to perform subsequent operations...
}

`


## Go V1


> NOTE:

> NOTE: 


> NOTE: Note 

All versions of OSS SDK for Go V2 support Signature V4 by default. [Migrate from Go V1 to Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/migration-guide-in-go).


-

Upgrade [OSS SDK for Go V1](https://github.com/aliyun/alibabacloud-oss-go-sdk-v2) to version 3.0.2 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `oss.AuthV4`.

#### Code sample


`go
package main

import (
	"log"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

// Call handleError to handle unrecoverable errors and terminate the program after recording the error messages.
func handleError(err error) {
	log.Fatalf("Error: %v", err)
}

// Use setupClient to create and configure an OSSClient instance.
// Parameters:
//
//	endpoint: endpoint of the region in which the bucket is located.
//	region: the region in which the bucket is located.
//
// Return the created OSSClient instance.
func setupClient(endpoint, region string) (*oss.Client, error) {
	// Obtain access credentials from environment variables.
	provider, err := oss.NewEnvironmentVariableCredentialsProvider()
	if err != nil {
		return nil, err
	}

	// Create an OSSClient instance and use the signature algorithm V4.
	client, err := oss.New(endpoint, "", "", oss.SetCredentialsProvider(&provider), oss.AuthVersion(oss.AuthV4), oss.Region(region))
	if err != nil {
		return nil, err
	}

	return client, nil
}

func main() {
	// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Specify your actual endpoint.
	endpoint := "yourEndpoint"

	// Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou.
	region := "yourRegion"

	// Check whether the environment variables are configured.
	if endpoint == "" || region == "" {
		log.Fatal("Please set yourEndpoint and yourRegion.")
	}

	// Create and configure an OSSClient instance.
	client, err := setupClient(endpoint, region)
	if err != nil {
		handleError(err)
	}

	// Display the client information.
	log.Printf("Client: %#v\n", client)
}

`


## PHP

## PHP V2


-

All versions of [OSS SDK for PHP V2](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2) support Signature V4 by default.

-

When you initialize an OSS Client with Signature V4, you must perform the following step:


Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.


`
<?php

// Include the autoload file to load dependencies.
require_once __DIR__ . '/../vendor/autoload.php';

use AlibabaCloud\Oss\V2 as Oss;

// Use EnvironmentVariableCredentialsProvider to retrieve the AccessKey ID and AccessKey secret from environment variables.
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

# Load the default configuration of the SDK and specify the credential provider.
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider(credentialsProvider: $credentialsProvider); // Specify the credential provider.

// Method 1: Specify only the region.
// Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
$cfg->setRegion(region: "cn-hangzhou");

// // Method 2: Specify the endpoint and region.
// // Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
// // Specify the public endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
// // To use the HTTP protocol, set the endpoint to http://oss-cn-hangzhou.aliyuncs.com.
// $cfg->setRegion(region: 'cn-hangzhou')->setEndpoint(endpoint: 'https://oss-cn-hangzhou.aliyuncs.com');

// Create an OSSClient instance.
$client = new Oss\Client($cfg);

// Use the OSSClient instance to perform subsequent operations.
`


## PHP V1


-

Upgrade [OSS SDK for PHP V1](https://github.com/aliyun/aliyun-oss-php-sdk) to version 2.7.0 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `OSS_SIGNATURE_VERSION_V4`.

#### Code sample


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
use OSS\Core\OssException;

try {
    // Obtain access credentials from environment variables and store them in the provider. Before you run this sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
    $provider = new EnvironmentVariableCredentialsProvider();
    // Specify the Endpoint of the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the Endpoint to https://oss-cn-hangzhou.aliyuncs.com.
    $endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
    $config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
        "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
        // Specify the region that corresponds to the Endpoint. For example, cn-hangzhou.
        "region" => "cn-hangzhou"
    );
    $ossClient = new OssClient($config);
} catch (OssException $e) {
    printf($e->getMessage() . "\n");
    return;
}
`


## C#

## C# V2


-

All versions of [OSS SDK for C# V2](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2) support Signature V4 by default.

-

When you initialize an OSS Client with Signature V4, you must perform the following step:


Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.


`
using OSS = AlibabaCloud.OSS.V2; // Create an alias for Alibaba Cloud OSS SDK to simplify subsequent use

var region = "cn-hangzhou"; // Required. Set the region where the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou
var endpoint = null as string;  // Optional. Specify the endpoint for accessing the OSS service. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com

// Load the default configuration of OSS SDK, which automatically reads credential information (such as AccessKey) from environment variables
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

// Use the created client for subsequent operations...
`


## C# V1


-

Upgrade [OSS SDK for C# V1](https://github.com/aliyun/aliyun-oss-csharp-sdk) to version 2.14.0 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `SignVersion.V4`.

#### Code sample


`csharp
using Aliyun.OSS;
using Aliyun.OSS.Common;
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret=Environment.GetEnvironmentVariable ("OSS_ACCESS_KEY_SECRET");

// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
const string region = "cn-hangzhou";

// Create a ClientConfiguration instance and modify the default parameters based on your requirements.
var conf = new ClientConfiguration();

// Specify the V4 signature.
conf.SignatureVersion = SignatureVersion.V4;

// Create an OSSClient instance.
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
`


## Node.js


-

Upgrade [OSS SDK for Node.js](https://github.com/ali-sdk/ali-oss) to version 6.20.0 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [dedicated OSS region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `oss-cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `authorizationV4`.


`
const OSS = require('ali-oss');

const client = new OSS({
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables have been configured.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'oss-cn-hangzhou',
  // Use the V4 signature algorithm
  authorizationV4: true,
  // Specify the name of the bucket.
  bucket: 'yourBucketName',
  // Specify the public endpoint for the region where the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
});
`


## Browser.js


-

Upgrade [OSS SDK for Browser.js](https://github.com/ali-sdk/ali-oss) to version 6.20.0 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [dedicated OSS region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `oss-cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `authorizationV4`.

#### Code sample


`html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
  </head>
  <body>
    <!-- Import the SDK file -->
    <script
      type="text/javascript"
      src="https://gosspublic.alicdn.com/aliyun-oss-sdk-6.20.0.min.js"
    ></script>
    <script type="text/javascript">
      const client = new OSS({
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
        region: 'yourRegion',
	authorizationV4: true,
        // Specify the temporary AccessKey pair obtained from Security Token Service (STS). The AccessKey pair consists of an AccessKey ID and an AccessKey secret.
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // Specify the security token obtained from STS.
        stsToken: 'yourSecurityToken',
        // Specify the name of the bucket. Example: examplebucket.
        bucket: "examplebucket",
      });
    </script>
  </body>
</html>
`


## C++


-

Upgrade [OSS SDK for C++](https://github.com/aliyun/aliyun-oss-cpp-sdk) to version 1.10.0 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `SignatureVersionType::V4`.

#### Code sample


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

    /* Release resources, such as network resources. */
    ShutdownSdk();
    return 0;
}
`


## C


-

Upgrade [OSS SDK for C](https://github.com/aliyun/aliyun-oss-c-sdk) to version 3.11.0 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `signature_version = 4`.

#### Code sample


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
    /* Use a char* string to initialize the aos_string_t data type. */
    aos_str_set(&options->config->endpoint, endpoint);
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    aos_str_set(&options->config->access_key_id, getenv("OSS_ACCESS_KEY_ID"));
    aos_str_set(&options->config->access_key_secret, getenv("OSS_ACCESS_KEY_SECRET"));
    // Specify two additional parameters.
    aos_str_set(&options->config->region, region);
    options->config->signature_version = 4;
    /* Specify whether to use CNAME to access OSS. The value 0 indicates that CNAME is not used. */
    options->config->is_cname = 0;
    /* Specify network parameters. The second parameter in this function specifies the ownership of ctl. By default, the value of the second parameter is 0. */
    options->ctl = aos_http_controller_create(options->pool, 0);
}
int main() {
    aos_pool_t *p;
    oss_request_options_t *options;
    /* Initialize global variables. You need to initialize global variables only once in the program lifecycle. */
    if (aos_http_io_initialize(NULL, 0) != AOSE_OK) {
        return -1;
    }
    /* Initialize the memory pool and options. */
    aos_pool_create(&p, NULL);
    options = oss_request_options_create(p);
    init_options(options);
    /* The logic code. In this example, the logic code is omitted. */
    /* Release the memory pool. This operation releases the memory resources allocated for the request. */
    aos_pool_destroy(p);
    /* Release global resources that are allocated. You need to release global resources only once in the program lifecycle. */
    aos_http_io_deinitialize();
    return 0;
}
`


## Swift


-

All versions of [OSS SDK for Swift](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2) support Signature V4 by default.

-

When you initialize an OSS Client with Signature V4, you must perform the following step:


Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.


`
import AlibabaCloudOSS
import Foundation

@main
struct Main {
    static func main() async {
        // Specify the region where the bucket is located. Example: China (Hangzhou) is cn-hangzhou.
        let region = "cn-hangzhou"
        // Optional. Specify the endpoint to access OSS. For China (Hangzhou), set the Endpoint to https://oss-cn-hangzhou.aliyuncs.com.
        let endpoint: String? = nil

        // Obtain access credentials from environment variables. Before you run this code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
        let credentialsProvider = EnvironmentCredentialsProvider()

        // Configure the OSS client parameters.
        let config = Configuration.default()
            .withRegion(region)        // Set the region where the bucket is located.
            .withCredentialsProvider(credentialsProvider)  // Set the access credentials.

        // Set a custom endpoint.
        if let endpoint = endpoint {
            config.withEndpoint(endpoint)
        }

        // Create an OSS client instance.
        let client = Client(config)
    }
}
`


## iOS


-

Upgrade [OSS SDK for iOS](https://github.com/aliyun/aliyun-oss-ios-sdk) to version 2.11.1 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `OSSSignVersionV4`.

#### Code sample


`objectc
// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
NSString *endpoint = @"yourEndpoint";
// Specify the temporary AccessKey pair obtained from STS. An AccessKey pair consists of an AccessKey ID and an AccessKey secret.
NSString *accessKeyId = @"yourAccessKeyId";
NSString *accessKeySecret = @"yourAccessKeySecret";
// Specify the security token obtained from STS.
NSString *securityToken = @"yourSecurityToken";
NSString *region = @"yourRegion";

id<OSSCredentialProvider> credentialProvider = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:accessKeyId secretKeyId:accessKeySecret securityToken:securityToken];
OSSClientConfiguration *configuration = [OSSClientConfiguration new];
configuration.signVersion = OSSSignVersionV4;
OSSClient *client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credentialProvider clientConfiguration:configuration];
client.region = region;
`


## Android


-

Upgrade [OSS SDK for Android](https://github.com/aliyun/aliyun-oss-android-sdk) to version 2.3 or later.

-

When you initialize an OSS Client with Signature V4, you must perform the following steps:


-

Specify the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket as the identifier for the request region. For example, the region ID for China (Hangzhou) is `cn-hangzhou`.

-

Explicitly declare the use of the V4 signature algorithm. For example: `SignVersion.V4`.

#### Code sample


`androidjava
// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
String endpoint = "yourEndpoint";
// Specify the temporary AccessKey pair obtained from STS.
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// Specify the security token obtained from STS.
String securityToken = "yourSecurityToken";
// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
String region = "yourRegion";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration config = new ClientConfiguration();
config.setSignVersion(SignVersion.V4);
// Create an OSSClient instance.
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);
`


### ossutil

## ossutil 2.0


All versions of the [ossutil 2.0 command line interface](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/) support Signature V4 by default.


Compared with Signature V1, when you use Signature V4, you must set the `Region` parameter to the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket when you [configure ossutil](https://www.alibabacloud.com/help/en/oss/configure-ossutil2).

#### Sample command


`bash
Please enter Region [cn-hangzhou]:cn-hangzhou
`


## ossutil 1.0


> NOTE:

> NOTE: 


> NOTE: Note 

All versions of ossutil 2.0 support Signature V4 by default. [Migrate from ossutil 1.0 to ossutil 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/migration-guide/).


Version 1.7.12 and later of the [ossutil 1.0 command line interface](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-59/) support Signature V4.


Compared with Signature V1, when you use Signature V4, you must do the following in the command:


-

Set the `--sign-version` option to `v4`.

-

Set the `--region` option to the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket.

#### Sample command


`plaintext
./ossutil64 --sign-version v4 --region cn-hangzhou mb oss://examplebucket
`


### ossfs

## ossfs 2.0


All versions of [ossfs 2.0 (Preview)](https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-2-0/) support Signature V4, but use Signature V1 by default.


-

Before you upgrade, run the `ossfs --version` command to check the current version and complete the following prerequisites based on your version.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

The uninstallation will interrupt your services. Perform this operation during off-peak hours.


Unmount the mounted OSS file system. Replace `<mountpoint>` with your actual directory.


`shell
sudo umount <mountpoint>
`


After unmounting, follow the sample command to upgrade.

-

Compared with Signature V1, when you use Signature V4, you must do the following in the mount command:


-

Set the `oss_region` option to the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket.

#### Sample command


`shell
ossfs2 mount /tmp/ossfs2-bucket/ -c /etc/ossfs2.conf   --oss_region=cn-hongkong
`


## ossfs 1.0


Version 1.91.4 and later of [ossfs 1.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-overview/) support Signature V4.


-

Before you upgrade, run the `ossfs --version` command to check the current version and complete the following prerequisites based on your version.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

The uninstallation will interrupt your services. Perform this operation during off-peak hours.


## Upgrade to V4 if the version requirement is met


Unmount the mounted OSS file system. Replace `<mountpoint>` with your actual directory.


`shell
sudo umount <mountpoint>
`


After unmounting, follow the Sample command to upgrade.

## Upgrade to V4 if the version requirement is not met


-

Unmount the mounted OSS file system. Replace `<mountpoint>` with your actual directory.


`shell
sudo umount <mountpoint>
`


-

Uninstall the old version.


If you installed ossfs using a package manager, such as `apt` or `yum`, run the following command:


`shell
sudo apt remove ossfs  # For Ubuntu/Debian systems
sudo yum remove ossfs  # For CentOS/Anolis/Alibaba Cloud Linux systems
`


If you compiled and installed ossfs from source code, go to the installation directory and run the following command:


`shell
sudo make uninstall
`


-

[Download and install the new version](https://www.alibabacloud.com/help/en/oss/developer-reference/install-ossfs-1-0#title-bht-wue-lqb).


After you install the new version, follow the Sample command to upgrade.

-

Compared with Signature V1, when you use Signature V4, you must do the following in the mount command:


-

Set the `sigv4` option.

-

Set the `region` option to the [region ID](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#e7e1c8a6e071v) of the bucket.

#### Sample command


`shell
ossfs examplebucket -o sigv4 -o region=cn-hangzhou  /tmp/ossfs -o url=http://oss-cn-hangzhou.aliyuncs.com
`


### API (manual signature construction)


Use an OSS SDK to send requests because the SDK automatically calculates the signature. If you cannot use an OSS SDK, you must manually construct a V4 signature and ensure that the request is correct.











(https://www.alibabacloud.com/help/en/oss/developer-reference/recommend-to-use-signature-version-4)


(https://www.alibabacloud.com/help/en/oss/developer-reference/add-signatures-to-urls)


(https://www.alibabacloud.com/help/en/oss/developer-reference/signature-version-4-recommend)


| Signature method | Description | References |
| --- | --- | --- |
| Include the signature in the header | In OSS, the most common method for identity verification is to include the signature in the Authorization header of an HTTP request. All OSS operations, except for those that use POST signatures or URL signatures, require authentication through the Authorization header. | Include a V4 signature in the header |
| Include the signature in the URL | You can grant third-party access to your OSS resources for a specific validity period without revealing your access credentials by generating a signed URL that includes the signature and other necessary request information. | Include a V4 signature in the URL |
| POST request signature | The PostObject signature is a mechanism that lets you upload files directly to OSS through an HTML form. This mechanism allows users to construct an HTML form on a client, such as a web browser. The form includes fields for the file to upload and other necessary parameters, such as the signature, AccessKey pair, bucket name, and object key. When the form is submitted, this information is sent to OSS through an HTTP POST request, and OSS verifies the validity of the POST request. | V4 signature for POST requests |


## Signature V1 deprecation timeline and impact


According to the [Alibaba Cloud Object Storage Service Signature Version 1 Discontinuation Announcement](https://www.alibabacloud.com/zh/notice/notice_on_the_discontinuation_of_the_oss_v1_signature_algorithm_40f?_p_lc=1), Signature V1 for Alibaba Cloud Object Storage Service will be gradually phased out for new customers (new UIDs) starting from March 1, 2025. Starting from September 1, 2025, Signature V1 will no longer be updated or maintained and will not be available for new buckets.

## Comparison between Signature V1 and Signature V4


(https://www.alibabacloud.com/help/en/oss/developer-reference/include-signatures-in-the-authorization-header)


(https://www.alibabacloud.com/help/en/oss/developer-reference/recommend-to-use-signature-version-4)





| Item | Signature V1 | Signature V4 |
| --- | --- | --- |
| Signature algorithm | HMAC-SHA1 | HMAC-SHA256 |
| Signed URL validity period | The signing time can be more than 7 days in the past. The validity period can exceed 7 days. | The signing time is limited to the past 7 days. The validity period is limited to 7 days. |
| Construction of the signature string | The signature string includes the HTTP method, Content-MD5, Content-Type, date, canonicalized headers, and resource path. | The signature string has a more complex structure, which includes the request method, canonicalized URI, canonicalized query parameters, canonicalized headers, additional signed headers, and payload hash. |
| Canonicalized headers and query parameters | Only headers that are prefixed with `x-oss-` are canonicalized. Only some query parameters are included in the signature. | All headers that are prefixed with `x-oss-` and default signed headers (such as `content-type` and `content-md5`) are canonicalized. Additional signed headers are also supported. |
| Resource path encoding | The forward slash (/) in the resource path is encoded. | The / in resource paths is not escaped, whereas the / in query parameters must be escaped as %2F. |
| Timestamp and date format | Uses the standard HTTP date format, for example, Wed, 21 Oct 2015 07:28:00 GMT. | Uses the ISO 8601 format for UTC time, for example, 20151021T072800Z. |
| Region information | The signature does not include region information. | The signature rules introduce the concept of a region. Both the signature string and the signature key must include the region ID. |


## FAQ

### How can I quickly check whether I am using Signature V1 or Signature V4?


Use [Real-time log query](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/) or a packet capture tool, such as Wireshark or Fiddler, to view the `Authorization` field in the HTTP request header sent to OSS.


-

Signature V1: The `Authorization` field starts with `OSS` and has the following format:


`shell
Authorization: OSS <AccessKeyId>:<Signature>
`


-

Signature V4: The `Authorization` field starts with `OSS4-HMAC-SHA256` and has the following format:


`shell
Authorization: OSS4-HMAC-SHA256 Credential=<AccessKeyId>/<Date>/<Region>/oss/aliyun_v4_request, AdditionalHeaders=<Headers>, Signature=<Signature>
`


### How to troubleshoot a `SignatureDoesNotMatch` error


If the signature calculation is incorrect, the system returns the `SignatureDoesNotMatch` error code. To quickly locate the problem, compare the signature-related information that is generated by the server and the client. The response that is returned by the server contains the following key information:


-

`CanonicalRequest`: The canonicalized query string that is generated by the server.

-

`StringToSign`: The string-to-sign that is generated by the server based on the canonicalized request.

-

`Signature`: The final signature value that is calculated by the server.


By comparing these fields with the corresponding fields that are generated by the client, you can quickly identify differences and locate the source of the error. For example:


-

If `CanonicalRequest` is inconsistent, the concatenation order or format of the request parameters may be incorrect.

-

If the `StringToSign` is inconsistent, the date, region, or cloud product information may be set incorrectly.

-

If the `Signature` is inconsistent, there may be an issue with the derived key calculation or the signature algorithm implementation.


Thank you! We've received your  feedback.