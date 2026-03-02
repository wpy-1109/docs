# Single-connection bandwidth throttling in Object Storage Service (OSS)

Accessing files (objects) in Object Storage Service (OSS) can consume a large amount of bandwidth. On clients where traffic shaping is difficult to control, this can affect other applications. To avoid this issue, you can use the single-connection bandwidth throttling feature provided by OSS to control traffic during operations such as file uploads and downloads. This ensures sufficient network bandwidth for other applications.

## Usage notes


Include the x-oss-traffic-limit parameter in PutObject, AppendObject, PostObject, CopyObject, UploadPart, UploadPartCopy, and GetObject requests and specify a throttling value. The value must be between 819200 and 838860800. The unit is bit/s.

## Throttle client requests


You can throttle client requests only using software development kits (SDKs). The following code provides examples of how to throttle upload or download requests using common SDKs. For code examples that use other SDKs, see [SDK overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).

### Simple upload and download throttling
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.GetObjectRequest;
import com.aliyun.oss.model.PutObjectRequest;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

public class Demo {
    public static void main(Stringargs) throws Throwable {
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
        String objectName = "exampledir/exampleobject.txt";
        // Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt.
        // If you do not specify the path of the local file, the local file is uploaded from the path of the project to which the sample program belongs.
        String localFileName = "D:\\localpath\\examplefile.txt";
        // Specify the full path to which you want to download the object. If a file that has the same name already exists, the downloaded object overwrites the file. Otherwise, the downloaded object is saved in the path.
        // If you do not specify a path for the downloaded object, the downloaded object is saved to the path of the project to which the sample program belongs.
        String downLoadFileName = "D:\\localpath\\exampleobject.txt";

        // Set the bandwidth limit to 100 KB/s.
        int limitSpeed = 100 * 1024 * 8;
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
            // Configure bandwidth throttling for object upload.
            InputStream inputStream = new FileInputStream(localFileName);
            PutObjectRequest PutObjectRequest = new PutObjectRequest(bucketName, objectName, inputStream);
            PutObjectRequest.setTrafficLimit(limitSpeed);
            ossClient.putObject(PutObjectRequest);

            // Configure bandwidth throttling for object download.
            GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, objectName);
            getObjectRequest.setTrafficLimit(limitSpeed);
            File localFile = new File(downLoadFileName);
            ossClient.getObject(getObjectRequest, localFile);
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
// Specify the full path of the object. Example: exampledir/exampleobject.txt. Do not include the bucket name in the full path.
$object = "exampledir/exampleobject.txt";
// Specify the content of the object.
$content = "hello world";

$config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
        "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
        "region"=> "cn-hangzhou"
    );
    $ossClient = new OssClient($config);

// Set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
$options = array(
      OssClient::OSS_HEADERS => array(
              OssClient::OSS_TRAFFIC_LIMIT => 819200,
));

try {
    // Configure bandwidth throttling for object upload.
    $ossClient->putObject($bucket, $object, $content, $options);

    // Configure bandwidth throttling for object download.
    $ossClient->getObject($bucket, $object, $options);
} catch (OssException $e) {
    printf(__FUNCTION__ . ": FAILED\n");
    printf($e->getMessage() . "\n");
    return;
}

print(__FUNCTION__ . ": OK" . "\n");
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
  bucket: 'yourbucketname'
});

// Configure the speed limit by using the request header.
const headers = {
 // Set the minimum bandwidth to 100 KB/s.
 'x-oss-traffic-limit': 8 * 1024 * 100
}

// Configure bandwidth throttling for the object to be uploaded.
async function put() {
  // Specify the path of the object.
  const filePath = 'D:\\localpath\\examplefile.txt';
  // Create a file stream for the object.
  const fileStream = fs.createReadStream(filePath);
  const result = await client.putStream('file-name', fileStream, {
    // Set the request header properly.
    headers,
    // Set the default timeout period to 60000. Unit: milliseconds. If the duration of an object upload exceeds the timeout period, an exception is thrown. When you configure bandwidth throttling for object uploads, modify the timeout period.
    timeout: 60000
  });
  console.log(result);
}

put()

// Configure bandwidth throttling for the object to be downloaded.
async function get() {
  const result = await client.get('file name', {
    headers,
    // Set the default timeout period to 60000. Unit: milliseconds. If the duration of an object download exceeds the timeout period, an exception is thrown. When you configure bandwidth throttling for object downloads, modify the timeout period.
    timeout: 60000
  })
  console.log(result)
}

get()
`

Python

`python
# -*- coding: utf-8 -*-

import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from oss2.models import OSS_TRAFFIC_LIMIT

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"
# Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou. This parameter is required if you use the signature algorithm V4.
region = "cn-hangzhou"

# Specify the name of the bucket.
bucket = oss2.Bucket(auth, endpoint, "examplebucket", region=region)

# Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
object_name = 'exampledir/exampleobject.txt'
# Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt. By default, if you do not specify the path of the local file, the local file is uploaded from the path of the project to which the sample program belongs.
local_file_name = 'D:\\localpath\\examplefile.txt'
# Specify the local path to which you want to download the object. If a file that has the same name already exists, the downloaded object overwrites the file. If no file that has the same name exists, the downloaded object is saved in the path.
# If you do not specify a path for the downloaded object, the downloaded object is saved to the path of the project to which the sample program belongs.
down_file_name = 'D:\\localpath\\exampleobject.txt'

# Configure the headers parameter to set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
limit_speed = (100 * 1024 * 8)
headers = dict()
headers[OSS_TRAFFIC_LIMIT] = str(limit_speed)

# Configure bandwidth throttling for object upload.
result = bucket.put_object_from_file(object_name, local_file_name, headers=headers)
print('http response status:', result.status)

# Configure bandwidth throttling for object download.
result = bucket.get_object_to_file(object_name, down_file_name, headers=headers)
print('http response status:', result.status)
`

C#

`csharp
using System.Text;
using Aliyun.OSS;
using Aliyun.OSS.Common;

// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Specify the name of the bucket. Example: examplebucket.
var bucketName = "examplebucket";
// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
var objectName = "exampledir/exampleobject.txt";
var objectContent = "More than just cloud.";
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
    bytebinaryData = Encoding.ASCII.GetBytes(objectContent);
    MemoryStream requestContent = new MemoryStream(binaryData);
    // Set the bandwidth limit for object upload to 100 KB/s, which is equal to 819,200 bit/s.
    var putRequest = new PutObjectRequest(bucketName, objectName, requestContent)
    {
        TrafficLimit = 100*1024*8
    };
    client.PutObject(putRequest);
    Console.WriteLine("Put object succeeded");

    // Set the bandwidth limit for object download to 100 KB/s, which is equal to 819,200 bit/s.
    var getRequest = new GetObjectRequest(bucketName, objectName)
    {
        TrafficLimit = 100 * 1024 * 8
    };
    var getResult = client.GetObject(getRequest);
    Console.WriteLine("Get object succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
`

Go

`go
package main

import (
	"log"
	"os"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
	// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
	provider, err := oss.NewEnvironmentVariableCredentialsProvider()
	if err != nil {
		log.Fatalf("Failed to create credentials provider: %v", err)
	}

	// Create an OSSClient instance.
	// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Specify your actual endpoint.
	// Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou. Specify the actual region.
	options := oss.ClientOption{oss.SetCredentialsProvider(&provider)}
	options = append(options, oss.Region("yourRegion"))
	// Specify the version of the signature algorithm.
	options = append(options, oss.AuthVersion(oss.AuthV4))
	client, err := oss.New("yourEndpoint", "", "", options...)
	if err != nil {
		log.Fatalf("Failed to create OSS client: %v", err)
	}

	// Specify the name of the bucket. Example: examplebucket.
	bucketName := "examplebucket"
	bucket, err := client.Bucket(bucketName)
	if err != nil {
		log.Fatalf("Failed to get bucket '%s': %v", bucketName, err)
	}

	// Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt.
	// If you do not specify the path of the local file, the local file is uploaded from the path of the project to which the sample program belongs.
	localFilePath := "D:\\localpath\\examplefile.txt"
	fd, err := os.Open(localFilePath)
	if err != nil {
		log.Fatalf("Failed to open local file '%s': %v", localFilePath, err)
	}
	defer fd.Close()

	// Specify the bandwidth limit for the upload. The value of the parameter must be a number. Default unit: bit/s. In this example, the bandwidth limit is set to 5 MB/s.
	var traffic int64 = 41943040

	// Configure bandwidth throttling for object upload.
	// Specify the full path of the object. Do not include the bucket name in the full path.
	objectName := "exampledir/exampleobject.txt"
	err = bucket.PutObject(objectName, fd, oss.TrafficLimitHeader(traffic))
	if err != nil {
		log.Fatalf("Failed to upload object '%s': %v", objectName, err)
	}

	// Configure bandwidth throttling for object download.
	// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt. Then, specify the full path of the local file. Example: D:\\localpath\\exampleobject.txt.
	downloadFilePath := "D:\\localpath\\exampleobject.txt"
	err = bucket.GetObjectToFile(objectName, downloadFilePath, oss.TrafficLimitHeader(traffic))
	if err != nil {
		log.Fatalf("Failed to download object '%s' to '%s': %v", objectName, downloadFilePath, err)
	}

	log.Println("Upload and download completed successfully")
}

`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
#include <fstream>
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

    /* Initialize resources, such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Upload the object. */
    std::shared_ptr<std::iostream> content = std::make_shared<std::fstream>("yourLocalFilename", std::ios::in|std::ios::binary);
    PutObjectRequest putrequest(BucketName, ObjectName,content);
    /* Set the maximum speed to upload the object to 100 KB/s. */
    putrequest.setTrafficLimit(819200);
    auto putoutcome = client.PutObject(putrequest);

    /* Download the object to local memory. */
    GetObjectRequest getrequest(BucketName, ObjectName);
    /* Set the maximum speed to download the object to 100 KB/s. */
    getrequest.setTrafficLimit(819200);
    auto getoutcome = client.GetObject(getrequest);

    /* Release resources, such as network resources. */
    ShutdownSdk();
    return 0;
}
`


### Multipart upload throttling
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class DemoApi2 {

    public static void main(Stringargs) throws Exception {
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the full path of the object. Example: exampledir/exampleobject.txt. Do not include the bucket name in the full path.
        String objectName = "exampledir/exampleobject.txt";
        // Set the bandwidth limit to 100 KB/s.
        int limitSpeed = 100 * 1024 * 8;
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
            // Create an InitiateMultipartUploadRequest object.
            InitiateMultipartUploadRequest request = new InitiateMultipartUploadRequest(bucketName, objectName);


            // Initialize the multipart upload task.
            InitiateMultipartUploadResult upresult = ossClient.initiateMultipartUpload(request);
            // Obtain the upload ID, which uniquely identifies the multipart upload task. You can use the upload ID to perform related operations, such as canceling and querying the multipart upload task.
            String uploadId = upresult.getUploadId();

            // partETags is the set of PartETags. A PartETag consists of the part number and ETag of an uploaded part
            List<PartETag> partETags =  new ArrayList<PartETag>();
            // Specify the size of each part, which is used to calculate the number of parts of the object. Unit: bytes.
            final long partSize = 1 * 1024 * 1024L;   // Set the part size to 1 MB.

            // Specify the full path of the local file that you want to upload. By default, if you do not specify the full path of the local file, the local file is uploaded from the path of the project to which the sample program belongs.
            final File sampleFile = new File("D:\\localpath\\examplefile.txt");
            long fileLength = sampleFile.length();
            int partCount = (int) (fileLength / partSize);
            if (fileLength % partSize != 0) {
                partCount++;
            }
            // Upload all parts.
            for (int i = 0; i < partCount; i++) {
                long startPos = i * partSize;
                long curPartSize = (i + 1 == partCount) ? (fileLength - startPos) : partSize;
                InputStream instream = new FileInputStream(sampleFile);
                // Skip the parts that are uploaded.
                instream.skip(startPos);
                UploadPartRequest uploadPartRequest = new UploadPartRequest();
                uploadPartRequest.setBucketName(bucketName);
                uploadPartRequest.setKey(objectName);
                uploadPartRequest.setUploadId(uploadId);
                uploadPartRequest.setInputStream(instream);
                // Specify the size of each part. Each part except the last part must be equal to or greater than 100 KB.
                uploadPartRequest.setPartSize(curPartSize);
                // Specify part numbers. Each part has a part number. The number ranges from 1 to 10000. If the specified number is beyond the range, OSS returns an InvalidArgument error code.
                uploadPartRequest.setPartNumber( i + 1);
                // Specify the bandwidth limit.
                uploadPartRequest.setTrafficLimit(limitSpeed);
                // Parts are not necessarily uploaded in order. They can be uploaded from different OSS clients. OSS sorts the parts based on their part numbers and combines them into a complete object.
                UploadPartResult uploadPartResult = ossClient.uploadPart(uploadPartRequest);
                // Each time a part is uploaded, OSS returns a result that contains a PartETag. The PartETags are stored in partETags.
                partETags.add(uploadPartResult.getPartETag());
            }


            // Create a CompleteMultipartUploadRequest object.
            // When you call the CompleteMultipartUpload operation, you must provide all valid PartETags. After OSS receives the PartETags, OSS verifies all parts one by one. After all parts are verified, OSS combines these parts into a complete object.
            CompleteMultipartUploadRequest completeMultipartUploadRequest =
                    new CompleteMultipartUploadRequest(bucketName, objectName, uploadId, partETags);

            // Complete the multipart upload task.
            CompleteMultipartUploadResult completeMultipartUploadResult = ossClient.completeMultipartUpload(completeMultipartUploadRequest);
            System.out.println(completeMultipartUploadResult.getETag());
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
use OSS\Core\OssException;
use OSS\Core\OssUtil;

// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
$provider = new EnvironmentVariableCredentialsProvider();
// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
$endpoint = "yourEndpoint";
// Specify the name of the bucket. Example: examplebucket.
$bucket= "examplebucket";
// Specify the full path of the object. Example: exampledir/exampleobject.txt. Do not include the bucket name in the full path.
$object = "exampledir/exampleobject.txt";
// Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt. By default, if you do not specify the path of the local file, the file is uploaded from the path of the project to which the sample program belongs.
$uploadFile = "D:\\localpath\\examplefile.txt";

/
* Step 1: Initiate a Multipart upload task and obtain the upload ID.
*/
try{
  $config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
        "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
        "region"=> "cn-hangzhou"
    );
    $ossClient = new OssClient($config);

  // Obtain the upload ID. An upload ID is the unique identifier for a multipart upload task. You can use an upload ID to perform related operations such as canceling or querying the multipart upload task.
  $uploadId = $ossClient->initiateMultipartUpload($bucket, $object);
} catch(OssException $e) {
  printf(__FUNCTION__ . ": initiateMultipartUpload FAILED\n");
  printf($e->getMessage() . "\n");
  return;
}
print(__FUNCTION__ . ": initiateMultipartUpload OK" . "\n");
/ Step 2: Upload parts.
*/
$partSize = 10 * 1024 * 1024;
$uploadFileSize = filesize($uploadFile);
$pieces = $ossClient->generateMultiuploadParts($uploadFileSize, $partSize);
$responseUploadPart = array();
$uploadPosition = 0;
$isCheckMd5 = true;
foreach ($pieces as $i => $piece) {
  $fromPos = $uploadPosition + (integer)$piece[$ossClient::OSS_SEEK_TO];
  $toPos = (integer)$piece[$ossClient::OSS_LENGTH] + $fromPos - 1;
  $upOptions = array(
    // Upload the object.
    $ossClient::OSS_FILE_UPLOAD => $uploadFile,
    // Specify part numbers.
    $ossClient::OSS_PART_NUM => ($i + 1),
    // Specify the position from which the multipart upload task starts.
    $ossClient::OSS_SEEK_TO => $fromPos,
    // Specify the object length.
    $ossClient::OSS_LENGTH => $toPos - $fromPos + 1,
    // Specify whether to enable MD5 verification. A value of true indicates that MD5 verification is enabled.
    $ossClient::OSS_CHECK_MD5 => $isCheckMd5,
    // Set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
    $options = array(
      OssClient::OSS_HEADERS => array(
        OssClient::OSS_TRAFFIC_LIMIT => 819200,
      ))

  );
  // Enable MD5 verification.
  if ($isCheckMd5) {
    $contentMd5 = OssUtil::getMd5SumForFile($uploadFile, $fromPos, $toPos);
    $upOptions[$ossClient::OSS_CONTENT_MD5] = $contentMd5;
  }
  try {
    // Upload the parts.
    $responseUploadPart= $ossClient->uploadPart($bucket, $object, $uploadId, $upOptions);
  } catch(OssException $e) {
    printf(__FUNCTION__ . ": initiateMultipartUpload, uploadPart - part#{$i} FAILED\n");
    printf($e->getMessage() . "\n");
    return;
  }
  printf(__FUNCTION__ . ": initiateMultipartUpload, uploadPart - part#{$i} OK\n");
}
// The $uploadParts parameter is an array that consists of the ETag and PartNumber parameters of each part.
$uploadParts = array();
foreach ($responseUploadPart as $i => $eTag) {
  $uploadParts= array(
    'PartNumber' => ($i + 1),
    'ETag' => $eTag,
  );
}
/
* Step 3: Complete the multipart upload task.
*/
try {
  // All valid values of the $uploadParts parameter are required for the CompleteMultipartUpload operation. After OSS receives the values of the $uploadParts parameter, OSS verifies all parts one by one. After the verification of all parts is completed, OSS combines these parts into a complete object.
  $ossClient->completeMultipartUpload($bucket, $object, $uploadId, $uploadParts);
  }  catch(OssException $e) {
  printf(__FUNCTION__ . ": completeMultipartUpload FAILED\n");
  printf($e->getMessage() . "\n");
  return;
  }
  printf(__FUNCTION__ . ": completeMultipartUpload OK\n");
`

Python

`python
# -*- coding: utf-8 -*-
import os
from oss2 import SizedFileAdapter, determine_part_size
from oss2.headers import OSS_TRAFFIC_LIMIT
from oss2.models import PartInfo
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"
# Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou. This parameter is required if you use the signature algorithm V4.
region = "cn-hangzhou"

# Specify the name of the bucket.
bucket = oss2.Bucket(auth, endpoint, "examplebucket", region=region)

# Specify the full path of the object. The full path of the object cannot contain the bucket name. Example: exampledir/exampleobject.txt.
key = 'exampledir/exampleobject.txt'
# Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt.
filename = 'D:\\localpath\\examplefile.txt'

total_size = os.path.getsize(filename)
# Use the determine_part_size method to determine the part size.
part_size = determine_part_size(total_size, preferred_size=100 * 1024)

# Initiate a multipart upload task.
upload_id = bucket.init_multipart_upload(key).upload_id
parts = # Configure the headers parameter to set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
limit_speed = (100 * 1024 * 8)
headers = dict()
headers[OSS_TRAFFIC_LIMIT] = str(limit_speed)

# Upload the parts one by one.
with open(filename, 'rb') as fileobj:
    part_number = 1
    offset = 0
    while offset < total_size:
        num_to_upload = min(part_size, total_size - offset)
        # Call the SizedFileAdapter(fileobj, size) method to generate a new object and recalculate the position from which the append operation starts.
        result = bucket.upload_part(key, upload_id, part_number,
                                    SizedFileAdapter(fileobj, num_to_upload), headers=headers)
        parts.append(PartInfo(part_number, result.etag))

        offset += num_to_upload
        part_number += 1

# Complete the multipart upload task.
# The following code provides an example on how to configure headers when you complete the multipart upload task:
headers = dict()
# Specify the access control list (ACL) of the object. In this example, this parameter is set to OBJECT_ACL_PRIVATE, which indicates that the ACL of the object is private.
# headers["x-oss-object-acl"] = oss2.OBJECT_ACL_PRIVATE
bucket.complete_multipart_upload(key, upload_id, parts, headers=headers)
# bucket.complete_multipart_upload(key, upload_id, parts)

# Verify the result of the multipart upload task.
with open(filename, 'rb') as fileobj:
    assert bucket.get_object(key).read() == fileobj.read()
`

Go

`go
package main

import (
	"io"
	"log"
	"os"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
	// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
	provider, err := oss.NewEnvironmentVariableCredentialsProvider()
	if err != nil {
		log.Fatalf("Failed to create credentials provider: %v", err)
	}

	// Create an OSSClient instance.
	// Set yourEndpoint to the endpoint of the bucket. For the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Specify the actual endpoint for other regions.
	// Set yourRegion to the region where the bucket is located. For the China (Hangzhou) region, set the region to cn-hangzhou. Specify the actual region for other regions.
	options := oss.ClientOption{oss.SetCredentialsProvider(&provider)}
	options = append(options, oss.Region("yourRegion"))
	// Set the signature version.
	options = append(options, oss.AuthVersion(oss.AuthV4))
	client, err := oss.New("yourEndpoint", "", "", options...)
	if err != nil {
		log.Fatalf("Failed to create OSS client: %v", err)
	}

	// Specify the bucket name. Example: examplebucket.
	bucketName := "examplebucket"
	bucket, err := client.Bucket(bucketName)
	if err != nil {
		log.Fatalf("Failed to get bucket '%s': %v", bucketName, err)
	}

	// Set the upload bandwidth throttling. The parameter is a number and the default unit is bit/s. In this example, the value is set to 5 MB/s.
	traffic := int64(41943040)

	// Perform a multipart upload for a large file.
	// Split the file into three parts. The number of parts can vary based on the file size.
	localFilePath := "localFile"
	chunks, err := oss.SplitFileByPartNum(localFilePath, 3)
	if err != nil {
		log.Fatalf("Failed to split file '%s': %v", localFilePath, err)
	}

	// Open the file.
	fd, err := os.Open(localFilePath)
	if err != nil {
		log.Fatalf("Failed to open local file '%s': %v", localFilePath, err)
	}
	defer fd.Close()

	// Initialize the file to upload.
	objectName := "exampledir/exampleobject.txt"
	imur, err := bucket.InitiateMultipartUpload(objectName)
	if err != nil {
		log.Fatalf("Failed to initiate multipart upload for '%s': %v", objectName, err)
	}

	// Upload parts and throttle the bandwidth.
	var parts oss.UploadPart
	for _, chunk := range chunks {
		_, err := fd.Seek(chunk.Offset, io.SeekStart)
		if err != nil {
			log.Fatalf("Failed to seek to offset %d in file '%s': %v", chunk.Offset, localFilePath, err)
		}
		part, err := bucket.UploadPart(imur, fd, chunk.Size, chunk.Number, oss.TrafficLimitHeader(traffic))
		if err != nil {
			log.Fatalf("Failed to upload part %d of '%s': %v", chunk.Number, objectName, err)
		}
		parts = append(parts, part)
	}

	// Complete the upload.
	_, err = bucket.CompleteMultipartUpload(imur, parts)
	if err != nil {
		log.Fatalf("Failed to complete multipart upload for '%s': %v", objectName, err)
	}

	log.Println("Multipart upload completed successfully")
}

`


## Throttle bandwidth using a file URL


For files with public-read or public-read-write permissions, you can append the throttling parameter `x-oss-traffic-limit=<value>` to the file URL to throttle access. For example, the URL `https://examplebucket.oss-cn-hangzhou.aliyuncs.com/video.mp4?x-oss-traffic-limit=819200` specifies that the download speed for the video.mp4 file is throttled to 100 KB/s. The following figure shows the throttling effect:![video](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1368247461/p208908.png)

## Throttle bandwidth using a signed URL


When you use an SDK to generate a signed URL to access a private file, you must include the throttling parameter in the signature calculation. The following code provides examples of how to add the throttling parameter to a signed URL using common SDKs. For code examples that use other SDKs, see [SDK overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.GeneratePresignedUrlRequest;
import com.aliyun.oss.model.GetObjectRequest;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.net.URL;
import java.util.Date;

public class Demo {
    public static void main(Stringargs) throws Throwable {
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
        String objectName = "exampledir/exampleobject.txt";

        // Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt.
        // If you do not specify the path of the local file, the local file is uploaded from the path of the project to which the sample program belongs.
        String localFileName = "D:\\localpath\\examplefile.txt";

        // Specify the full path to which you want to download the object. If a file that has the same name already exists, the downloaded object overwrites the file. Otherwise, the downloaded object is saved in the path.
        // If you do not specify a path for the downloaded object, the downloaded object is saved to the path of the project to which the sample program belongs.
        String downLoadFileName = "D:\\localpath\\exampleobject.txt";

        // Set the bandwidth limit to 100 KB/s.
        int limitSpeed = 100 * 1024 * 8;
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
            // Generate a signed URL that includes the bandwidth throttling parameter for object upload and set the validity period of the URL to 60 seconds.
            Date date = new Date();
            date.setTime(date.getTime() + 60 * 1000);
            GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(bucketName, objectName, HttpMethod.PUT);
            request.setExpiration(date);
            request.setTrafficLimit(limitSpeed);
            URL signedUrl = ossClient.generatePresignedUrl(request);
            System.out.println("put object url" + signedUrl);

            // Configure bandwidth throttling for object upload.
            InputStream inputStream = new FileInputStream(localFileName);
            ossClient.putObject(signedUrl, inputStream, -1, null, true);

            // Generate a signed URL that includes the bandwidth throttling parameter for object download and set the validity period of the URL to 60 seconds.
            date = new Date();
            date.setTime(date.getTime() + 60 * 1000);
            request = new GeneratePresignedUrlRequest(bucketName, objectName, HttpMethod.GET);
            request.setExpiration(date);
            request.setTrafficLimit(limitSpeed);
            signedUrl = ossClient.generatePresignedUrl(request);
            System.out.println("get object url" + signedUrl);

            // Configure bandwidth throttling for object download.
            GetObjectRequest getObjectRequest =  new GetObjectRequest(signedUrl, null);
            ossClient.getObject(getObjectRequest, new File(downLoadFileName));
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
use OSS\Core\OssException;

// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
$provider = new EnvironmentVariableCredentialsProvider();
// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
$endpoint = "yourEndpoint";
// Specify the name of the bucket. Example: examplebucket.
$bucket= "examplebucket";
// Specify the full path of the object. Example: exampledir/exampleobject.txt. Do not include the bucket name in the full path.
$object = "exampledir/exampleobject.txt";

$config = array(
        "provider" => $provider,
        "endpoint" => $endpoint,
        "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
        "region"=> "cn-hangzhou"
    );
    $ossClient = new OssClient($config);

// Set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
$options = array(
        OssClient::OSS_TRAFFIC_LIMIT => 819200,
);

// Generate a signed URL for object upload with single-connection bandwidth throttling configured and set the validity period of the URL to 60 seconds.
$timeout = 60;
$signedUrl = $ossClient->signUrl($bucket, $object, $timeout, "PUT", $options);
print($signedUrl);

// Generate a signed URL for object download with single-connection bandwidth throttling configured and set the validity period of the URL to 120 seconds.
$timeout = 120;
$signedUrl = $ossClient->signUrl($bucket, $object, $timeout, "GET", $options);
print($signedUrl);
`

Python

`python
# -*- coding: utf-8 -*-

import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider
from oss2.models import OSS_TRAFFIC_LIMIT

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"
# Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou. This parameter is required if you use the signature algorithm V4.
region = "cn-hangzhou"

# Specify the name of the bucket.
bucket = oss2.Bucket(auth, endpoint, "examplebucket", region=region)

# Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
object_name = 'exampledir/exampleobject.txt'
# Specify the full path of the local file that you want to upload. Example: D:\\localpath\\examplefile.txt. By default, if you do not specify the path of the local file, the local file is uploaded from the path of the project to which the sample program belongs.
local_file_name = 'D:\\localpath\\examplefile.txt'
# Specify the local path to which you want to download the object. If a file that has the same name already exists, the downloaded object overwrites the file. If no file that has the same name exists, the downloaded object is saved in the path.
# If you do not specify a path for the downloaded object, the downloaded object is saved to the path of the project to which the sample program belongs.
down_file_name = 'D:\\localpath\\exampleobject.txt'

# Configure the params parameter to set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
limit_speed = (100 * 1024 * 8)
params = dict()
params[OSS_TRAFFIC_LIMIT] = str(limit_speed)

# Generate a signed URL that includes the bandwidth throttling parameter for object upload and set the validity period of the URL to 60 seconds.
url = bucket.sign_url('PUT', object_name, 60, params=params)
print('put object url:', url)

# Configure bandwidth throttling for object upload.
result = bucket.put_object_with_url_from_file(url, local_file_name)
print('http response status:', result.status)

# Generate a signed URL that includes the bandwidth throttling parameter for object download and set the validity period of the URL to 60 seconds.
url = bucket.sign_url('GET', object_name, 60, params=params)
print('get object url:', url)

# Configure bandwidth throttling for object download.
result = bucket.get_object_with_url_to_file(url, down_file_name)
print('http response status:', result.status)
`

Go

`go
package main

import (
	"log"
	"os"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
	// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
	provider, err := oss.NewEnvironmentVariableCredentialsProvider()
	if err != nil {
		log.Fatalf("Failed to create credentials provider: %v", err)
	}

	// Create an OSSClient instance.
	// Set yourEndpoint to the endpoint of the bucket. For the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. Specify the actual endpoint for other regions.
	// Set yourRegion to the region where the bucket is located. For the China (Hangzhou) region, set the region to cn-hangzhou. Specify the actual region for other regions.
	clientOptions := oss.ClientOption{oss.SetCredentialsProvider(&provider)}
	clientOptions = append(clientOptions, oss.Region("yourRegion"))
	// Set the signature version.
	clientOptions = append(clientOptions, oss.AuthVersion(oss.AuthV4))
	client, err := oss.New("yourEndpoint", "", "", clientOptions...)
	if err != nil {
		log.Fatalf("Failed to create OSS client: %v", err)
	}

	// Specify the bucket name. Example: examplebucket.
	bucketName := "examplebucket"
	bucket, err := client.Bucket(bucketName)
	if err != nil {
		log.Fatalf("Failed to get bucket '%s': %v", bucketName, err)
	}

	// Use a signed URL to upload a file.
	// Specify the full path of the local file. Example: D:\\localpath\\exampleobject.txt.
	localFilePath := "D:\\localpath\\exampleobject.txt"
	fd, err := os.Open(localFilePath)
	if err != nil {
		log.Fatalf("Failed to open local file '%s': %v", localFilePath, err)
	}
	defer fd.Close()

	// Set the upload bandwidth throttling. The parameter is a number and the default unit is bit/s. In this example, the value is set to 5 MB/s.
	traffic := int64(41943040)

	// Obtain the URL for uploading the file.
	// Specify the full path of the object. The full path cannot contain the bucket name.
	objectName := "exampledir/exampleobject.txt"
	strURL, err := bucket.SignURL(objectName, oss.HTTPPut, 60, oss.TrafficLimitParam(traffic))
	if err != nil {
		log.Fatalf("Failed to generate signed URL for uploading '%s': %v", objectName, err)
	}

	// Upload the local file.
	err = bucket.PutObjectWithURL(strURL, fd)
	if err != nil {
		log.Fatalf("Failed to upload object '%s': %v", objectName, err)
	}

	// Use a signed URL to download a file.
	// Obtain the URL for downloading the file.
	strURL, err = bucket.SignURL(objectName, oss.HTTPGet, 60, oss.TrafficLimitParam(traffic))
	if err != nil {
		log.Fatalf("Failed to generate signed URL for downloading '%s': %v", objectName, err)
	}

	// Specify the full path to which the object is downloaded.
	downloadFilePath := "D:\\localpath\\exampleobject.txt"
	err = bucket.GetObjectToFileWithURL(strURL, downloadFilePath)
	if err != nil {
		log.Fatalf("Failed to download object '%s' to '%s': %v", objectName, downloadFilePath, err)
	}

	log.Println("Upload and download completed successfully")
}

`

C#

`csharp
using System.Text;
using Aliyun.OSS;
using Aliyun.OSS.Common;

// Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
var endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// Specify the name of the bucket. Example: examplebucket.
var bucketName = "examplebucket";
// Specify the full path of the object. Do not include the bucket name in the full path. Example: exampledir/exampleobject.txt.
var objectName = "exampledir/exampleobject.txt";
var objectContent = "More than just cloud.";
var downloadFilename  = "D:\\localpath\\examplefile.txt";
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
    // Generate a signed URL to upload the object.
    var generatePresignedUriRequest = new GeneratePresignedUriRequest(bucketName, objectName, SignHttpMethod.Put)
    {
        Expiration = DateTime.Now.AddHours(1),
    };

    // Set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
    generatePresignedUriRequest.AddQueryParam("x-oss-traffic-limit", "819200");

    var signedUrl = client.GeneratePresignedUri(generatePresignedUriRequest);
    // Use the signed URLs to upload the object.
    var buffer = Encoding.UTF8.GetBytes(objectContent);
    using (var ms = new MemoryStream(buffer))
    {
        client.PutObject(signedUrl, ms);
    }
    Console.WriteLine("Put object by signatrue succeeded. {0} ", signedUrl.ToString());


    var metadata = client.GetObjectMetadata(bucketName, objectName);
    var etag = metadata.ETag;
    // Generate a signed URL to download the object.
    // Set the bandwidth limit to 100 KB/s, which is equal to 819,200 bit/s.
    var req = new GeneratePresignedUriRequest(bucketName, objectName, SignHttpMethod.Get);
    req.AddQueryParam("x-oss-traffic-limit", "819200");

    var uri = client.GeneratePresignedUri(req);
    // Use the signed URL to download the object.
    OssObject ossObject = client.GetObject(uri);
    using (var file = File.Open(downloadFilename, FileMode.OpenOrCreate))
    {
        using (Stream stream = ossObject.Content)
        {
            int length = 4 * 1024;
            var buf = new byte[length];
            do
            {
                length = stream.Read(buf, 0, length);
                file.Write(buf, 0, length);
            } while (length != 0);
        }
    }
    Console.WriteLine("Get object by signatrue succeeded. {0} ", uri.ToString());
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
`

C++

`cpp
#include <alibabacloud/oss/OssClient.h>
#include <fstream>
using namespace AlibabaCloud::OSS;
int main(void)
{
    /* Initialize information about the account that is used to access OSS. */

    /* Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com. */
    std::string Endpoint = "yourEndpoint";
    /*Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.*/
    std::string Region = "yourRegion";
    /* Specify the name of the bucket. Example: examplebucket. */
    std::string BucketName = "examplebucket";
    /* Specify the full path of the object. Do not include the bucket name in the full path of the object. Example: exampledir/exampleobject.txt. */
    std::string ObjectName = "exampledir/exampleobject.txt";

    /* Initialize resources, such as network resources. */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured. */
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* Set the validity period of the signed URL to 32,400 seconds. */
    std::time_t expires = std::time(nullptr) + 1200;
    /* Generate the signed URL that is used to upload the object. */
    GeneratePresignedUrlRequest putrequest(BucketName, ObjectName, Http::Put);
    putrequest.setExpires(expires);
    /* Set the maximum speed to upload the object to 100 KB/s. */
    putrequest.setTrafficLimit(819200);
    auto genOutcome = client.GeneratePresignedUrl(putrequest);
    std::shared_ptr<std::iostream> content = std::make_shared<std::stringstream>();
    *content << "test cpp sdk";
    /* Display the signed upload URL. */
    std::cout << "Signed upload URL:" << genOutcome.result() << std::endl;

    /* Use the signed URL to upload the object. */
    auto outcome = client.PutObjectByUrl(genOutcome.result(), content);
    /* Generate the signed URL that is used to download the object. */
    GeneratePresignedUrlRequest getrequest(BucketName, ObjectName, Http::Get);
    getrequest.setExpires(expires);
    /* Set the maximum speed to download the object to 100 KB/s. */
    getrequest.setTrafficLimit(819200);
    genOutcome = client.GeneratePresignedUrl(getrequest);
    /* Display the signed download URL. */
    std::cout << "Signed download URL:" << genOutcome.result() << std::endl;
    /* Use the signed URL to download the object. */
    auto goutcome = client.GetObjectByUrl(genOutcome.result());

    /* Release resources, such as network resources. */
    ShutdownSdk();
    return 0;
}

`


Thank you! We've received your  feedback.