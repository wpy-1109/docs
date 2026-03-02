# Pay-by-requester

Pay-by-requester shifts data-access costs -- traffic and request fees -- from the bucket owner to the requester. The bucket owner pays only for storage. When enabled, anonymous access is disabled and all requests require authentication.

## How it works


Object Storage Service (OSS) processes each request as follows:


-

If the request includes the `x-oss-request-payer` header, OSS authenticates the requester. The requester pays all traffic and request fees.

-

If the request does not include the `x-oss-request-payer` header:


-

If the requester is the bucket owner, OSS processes the request. The bucket owner pays all costs.

-

If the requester is not the bucket owner, OSS rejects the request.

## Usage notes


Pay-by-requester is available only for buckets that have a region attribute.

## Configure pay-by-requester as the bucket owner

### Step 1: Enable pay-by-requester


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, click the name of the desired bucket.

-

In the left-side navigation pane, choose Bucket Settings > Pay-by-requester.

-

On the Pay-by-requester page, turn on the Pay-by-requester switch.

-

In the dialog box that appears, click OK.

### Step 2: Grant access permissions to the requester


Grant the requester access permissions with a bucket policy. Without a policy, the requester's access attempts are denied.


-

On the [Buckets](https://oss.console.alibabacloud.com/bucket/) page, click the name of the desired bucket.

-

In the left-side navigation pane, choose Permission Control > Bucket Policy.

-

On the Bucket Policy page, click Authorize on the Add in GUI tab.

-

In the Authorize panel, configure the policy. For Authorized User, select Other Accounts, and enter the requester's Alibaba Cloud account ID or the RAM role's Alibaba Cloud Resource Name (ARN). The format for the ARN is `arn:sts::{RoleOwnerUid}:assumed-role/{RoleName}/{RoleSessionName}`.

-

Click OK.

## Make a paid request as the requester


After the bucket owner enables pay-by-requester for a bucket, requesters must acknowledge that they will be charged for the request. The following sections show how to do this through the OSS console, SDKs, CLI (ossutil), or API.

### Console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click the plus sign (+) next to Favorite Paths.

-

In the Add Favorite Paths dialog box, configure the parameters as described in the following table.


| Parameter | Description |
| --- | --- |
| Adding method | Select Add from other authorized buckets to add the authorized bucket to your favorite paths. |
| Region | Select the region where the authorized bucket resides. |
| Bucket | Enter the name of the authorized bucket. |
| Pay-by-requester | Select I understand and agree to confirm that you will pay the associated fees. You will be billed for any resulting traffic and request fees. |


### SDKs


Add the header `x-oss-request-payer: requester` to every request. Without this header, OSS denies the request with an error response.


The following examples show how to set this header when calling PutObject, GetObject, or DeleteObject. The same approach applies to any other operation that reads or writes objects.

#### Java


`java
import com.aliyun.oss.ClientBuilderConfiguration;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.OSSException;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.*;
import java.io.ByteArrayInputStream;

public class Demo {
    public static void main(Stringargs) throws Exception{
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint. For more information about the endpoints of other regions, see Regions and endpoints.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the full path of the object. Example: exampledir/exampleobject.txt. Do not include the bucket name in the full path.
        String objectName = "exampledir/exampleobject.txt";
        Payer payer = Payer.Requester;
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
            // Specify the payer when a third party calls the PutObject operation.
            String content = "hello";
            PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, objectName, new ByteArrayInputStream(content.getBytes()));
            putObjectRequest.setRequestPayer(payer);
            ossClient.putObject(putObjectRequest);

            // Specify the payer when a third party calls the GetObject operation.
            GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, objectName);
            getObjectRequest.setRequestPayer(payer);
            OSSObject ossObject = ossClient.getObject(getObjectRequest);
            ossObject.close();

            // Specify the payer when a third party calls the DeleteObject operation.
            GenericRequest genericRequest = new GenericRequest(bucketName, objectName);
            genericRequest.setRequestPayer(payer);
            ossClient.deleteObject(genericRequest);
        } catch (OSSException oe) {
            System.out.println("Caught an OSSException, which means your request made it to OSS, "
                    + "but was rejected with an error response for some reason.");
            System.out.println("Error Message:" + oe.getErrorMessage());
            System.out.println("Error Code:" + oe.getErrorCode());
            System.out.println("Request ID:" + oe.getRequestId());
            System.out.println("Host ID:" + oe.getHostId());
        } catch (Throwable ce) {
            System.out.println("Caught an ClientException, which means the client encountered "
                    + "a serious internal problem while trying to communicate with OSS, "
                    + "such as not being able to access the network.");
            System.out.println("Error Message:" + ce.getMessage());
        } finally {
            // Shut down the OSSClient instance.
            if (ossClient != null) {
                ossClient.shutdown();
            }
        }
    }
}
`


#### Python


`python
# -*- coding: utf-8 -*-

import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from oss2.headers import OSS_REQUEST_PAYER

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"

# Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou. This parameter is required if you use the signature algorithm V4.
region = "cn-hangzhou"

# Specify the name of your bucket.
bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region)

# Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
object_name = 'exampledir/exampleobject.txt'
headers = dict()
headers[OSS_REQUEST_PAYER] = "requester"

# Specify the x-oss-request-payer header in the request to upload the object.
result = bucket.put_object(object_name, 'test-content', headers=headers)

# Specify the x-oss-request-payer header in the request to download the object.
result = bucket.get_object(object_name, headers=headers)

# Specify the x-oss-request-payer header in the request to delete the object.
result = bucket.delete_object(object_name, headers=headers);
`


#### Go


`go
package main

import (
	"fmt"
	"io"
	"os"
	"strings"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
	// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
	provider, err := oss.NewEnvironmentVariableCredentialsProvider()
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(-1)
	}
	// Create an OSSClient instance.
	// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Specify your actual endpoint.
	// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. Specify the actual region.
	clientOptions := oss.ClientOption{oss.SetCredentialsProvider(&provider)}
	clientOptions = append(clientOptions, oss.Region("yourRegion"))
	// Specify the version of the signature algorithm.
	clientOptions = append(clientOptions, oss.AuthVersion(oss.AuthV4))
	payerClient, err := oss.New("yourEndpoint", "", "", clientOptions...)
	if err != nil {
		fmt.Println("New Error:", err)
		os.Exit(-1)
	}

	// Specify the name of the bucket.
	payerBucket, err := payerClient.Bucket("examplebucket")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(-1)
	}

	// If pay-by-requester is enabled, external requesters must set the oss.RequestPayer(oss.Requester) parameter to access authorized content.
	// If pay-by-requester is not enabled, external requesters are not required to include the oss.RequestPayer(oss.Requester) parameter to access the authorized content.

	// Upload an object.
	// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
	key := "exampledir/exampleobject.txt"
	err = payerBucket.PutObject(key, strings.NewReader("objectValue"), oss.RequestPayer("requester"))
	if err != nil {
		fmt.Println("put Error:", err)
		os.Exit(-1)
	}

	// List all objects in the bucket.
	lor, err := payerBucket.ListObjects(oss.RequestPayer(oss.Requester))
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(-1)
	}
	// Display the names of objects in the bucket.
	for _, l := range lor.Objects {
		fmt.Println("the Key name is :", l.Key)
	}

	// Download the object.
	body, err := payerBucket.GetObject(key, oss.RequestPayer(oss.Requester))
	if err != nil {
		fmt.Println("Get Error:", err)
		os.Exit(-1)
	}
	// You must close the obtained stream after the object is read. Otherwise, connection leaks may occur. Consequently, no connections are available and an exception occurs.
	defer body.Close()

	// Read and display the obtained content.
	data, err := io.ReadAll(body)
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(-1)
	}
	fmt.Println("data:", string(data))

	// Delete the object.
	err = payerBucket.DeleteObject(key, oss.RequestPayer(oss.Requester))
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(-1)
	}
}
`


#### Node.js


`javascript
const OSS = require('ali-oss');
const bucket = 'bucket-name';
const payer = 'Requester';

const client = new OSS({
  // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to oss-cn-hangzhou.
  region: 'yourregion',
  // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // Specify the name of your bucket.
  bucket: 'yourBucketName',

});

async function main() {
  await put();
  await get();
  await del();
}

async function put() {
  const result = await client.putBucketRequestPayment(bucket, payer);
  console.log('putBucketRequestPayment:', result);
  // Specify the payer when a third party calls the PutObject operation.
  const response = await client.put('fileName', path.normalize('D:\\localpath\\examplefile.txt'), {
    headers: {
      'x-oss-request-payer': 'requester'
    }
  });
  console.log('put:', response);
}

async function get() {
  const result = await client.putBucketRequestPayment(bucket, payer);
  console.log('putBucketRequestPayment:', result);
  // Specify the payer when a third party calls the GetObject operation.
  const response = await client.get('fileName', {
    headers: {
      'x-oss-request-payer': 'requester'
    }
  });
  console.log('get:', response);
}

async function del() {
  const result = await client.putBucketRequestPayment(bucket, payer);
  console.log('putBucketRequestPayment:', result);
  // Specify the payer when a third party calls the DeleteObject operation.
  const response = await client.delete('fileName', {
    headers: {
      'x-oss-request-payer': 'requester'
    }
  });
  console.log('delete:', response);
}

main();
`


#### C#


`csharp
using System;
using System.IO;
using System.Text;
using Aliyun.OSS;
using Aliyun.OSS.Common;


namespace Samples
{
    public class Program
    {
        public static void Main(stringargs)
        {
            // Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
            var endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
            // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
            var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
            var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
            // Specify the name of the bucket. Example: examplebucket.
            var bucketName = "examplebucket";
            var objectName = "example.txt";
            var objectContent = "More than just cloud.";
            // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
            const string region = "cn-hangzhou";
            // Create a ClientConfiguration instance and modify parameters as required.
            var conf = new ClientConfiguration();
            // Use the signature algorithm V4.
            conf.SignatureVersion = SignatureVersion.V4;

            // Create an OSSClient instance.
            var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);

            try
            {
                bytebinaryData = Encoding.ASCII.GetBytes(objectContent);
                MemoryStream requestContent = new MemoryStream(binaryData);
                // Specify the payer when a third party calls the PutObject operation.
                var putRequest = new PutObjectRequest(bucketName, objectName, requestContent);
                putRequest.RequestPayer = RequestPayer.Requester;
                var result = client.PutObject(putRequest);

                // Specify the payer when a third party calls the GetObject operation.
                var getRequest = new GetObjectRequest(bucketName, objectName);
                getRequest.RequestPayer = RequestPayer.Requester;
                var getResult = client.GetObject(getRequest);

                // Specify the payer when a third party calls the DeleteObject operation.
                var delRequest = new DeleteObjectRequest(bucketName, objectName);
                delRequest.RequestPayer = RequestPayer.Requester;
                client.DeleteObject(delRequest);
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
        }
    }
}
`


#### PHP


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

// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
$provider = new EnvironmentVariableCredentialsProvider();
// In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
$endpoint = "http://oss-cn-hangzhou.aliyuncs.com";
// Specify the name of the bucket. Example: examplebucket.
$bucket= "examplebucket";
// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
$object = "exampledir/exampleobject.txt";

// Enable pay-by-requester for the bucket.
$options = array(
  OssClient::OSS_HEADERS => array(
  OssClient::OSS_REQUEST_PAYER => 'requester',
));

try {
    $config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
        "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
        "region"=> "cn-hangzhou"
    );
    $ossClient = new OssClient($config);
    // Specify the payer when a third party calls the PutObject operation.
    $content = "hello";
    $ossClient->putObject($bucket, $object, $content, $options);

    // Specify the payer when a third party calls the GetObject operation.
    $ossClient->getObject($bucket, $object, $options);

    // Specify the payer when a third party calls the DeleteObject operation.
    $ossClient->deleteObject($bucket, $object, $options);
} catch (OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}

print(__FUNCTION__ . ": OK" . "\n");
`


#### C++


`c++
#include <alibabacloud/oss/OssClient.h>
#include <fstream>
using namespace AlibabaCloud::OSS;
int main(void)
{
    /* Initialize information about the account that is used to access OSS. */

    /* Specify the endpoint of the region in which the bucket that the requester wants to access is located. */
    std::string Endpoint = "yourEndpoint";

    /* Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. */
    std::string Region = "yourRegion";

    /* Specify the name of the bucket that the requester wants to access. Example: examplebucket. */
    std::string BucketName = "examplebucket";
    /* Specify the full path of the object that the requester wants to access. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt. */
    std::string ObjectName = "exampleobject.txt";
    /* Initialize resources such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Enable pay-by-requester when you upload an object. */
    std::shared_ptr<std::iostream> content = std::make_shared<std::stringstream>();
    *content << "test cpp sdk";
    PutObjectRequest putrequest(BucketName, ObjectName, content);
    putrequest.setRequestPayer(RequestPayer::Requester);
    auto putoutcome = client.PutObject(putrequest);

    /* Enable pay-by-requester when you download an object into memory. */
    GetObjectRequest getrequest(BucketName, ObjectName);
    getrequest.setRequestPayer(RequestPayer::Requester);
    auto getoutcome = client.GetObject(getrequest);

    /* Enable pay-by-requester when you delete an object. */
    DeleteObjectRequest delrequest(BucketName, ObjectName);
    delrequest.setRequestPayer(RequestPayer::Requester);
    auto deloutcome = client.DeleteObject(delrequest);

    /* Release resources such as network resources. */
    ShutdownSdk();
    return 0;
}
`


### ossutil


[Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS) before getting started.


To download an object with the `cp` command, specify the `--request-payer=requester` parameter:


`bash
ossutil cp oss://examplebucket/examplefile.txt  /localpath  --request-payer=requester
`


### API


Include the `x-oss-request-payer: requester` header in your RESTful API request and include this header in the signature calculation. For details, see [Include a signature in the header](https://www.alibabacloud.com/help/en/oss/developer-reference/recommend-to-use-signature-version-4).


`http
GET /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 06:38:30 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


## Best practices

### Use bucket policies instead of RAM roles for access control


When a requester accesses data by assuming a RAM role, the account to which the RAM role belongs pays for the request.


-

Incorrect: Allowing the requester to assume a RAM role from the bucket owner's account. All requests run as the bucket owner, and the bucket owner is charged for traffic and request fees -- defeating the purpose of pay-by-requester.

-

Correct: Grant the requester access permissions directly through a bucket policy.

### Generate presigned URLs from the requester's account


-

Incorrect: The bucket owner uses access credentials (an AccessKey pair or an STS temporary credential) to generate and share a presigned URL. The requester runs the request as the bucket owner, and the bucket owner is billed.

-

Correct: The requester generates the presigned URL using identity credentials (an AccessKey pair or an STS temporary credential) and includes the `x-oss-request-payer=requester` parameter. For information about signature calculation, see [Include a signature in the URL](https://www.alibabacloud.com/help/en/oss/developer-reference/add-signatures-to-urls). When this URL is used, the requester who generated it is billed.

### Separate static website hosting from pay-by-requester buckets


Enabling pay-by-requester disables anonymous access, which is required for static website hosting. Your website becomes unavailable. To avoid this, host your website's frontend assets (HTML, CSS, JS) in a separate bucket from data that requires pay-by-requester.

## Billing


When pay-by-requester is enabled, the requester pays for the following items. The bucket owner continues to pay for all other items. For a complete list, see [OSS Pricing](https://www.alibabacloud.com/product/oss/pricing).








(https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees)


(https://www.alibabacloud.com/help/en/oss/data-processing-fees)


| Fee | Billable item |
| --- | --- |
| Outbound traffic over the Internet |
| Origin traffic |
| Request fees | Number of PUT requests |
| Number of GET requests |
| Data processing | Retrieval of IA objects |
| Retrieval of Archive objects |


Thank you! We've received your  feedback.