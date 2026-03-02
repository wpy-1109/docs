# How to access OSS using AWS SDKs

Object Storage Service (OSS) is compatible with the AWS S3 API. Simply configure the endpoint and access credential toaccess OSS using an AWS SDK without changing your code.


-

Endpoint: Use an S3-compatible public endpoint (`https://s3.oss-{region}.aliyuncs.com`) or internal endpoint (`https://s3.oss-{region}-internal.aliyuncs.com`). Replace `{region}` with the actual region ID, such as `cn-hangzhou`. For a complete list of regions, see [Regions and Endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Due to a [policy change](https://www.alibabacloud.com/en/notice/oss_update_notice_policy_change_in_calling_data_api_operations_via_the_default_public_domain_name_45a) to improve compliance and security, starting March 20, 2025, new OSS users must [use a custom domain name](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names) (CNAME) to perform data API operations on OSS buckets located in Chinese mainland regions. Default public endpoints are restricted for these operations. Refer to the [official announcement](https://www.alibabacloud.com/en/notice/oss_update_notice_policy_change_in_calling_data_api_operations_via_the_default_public_domain_name_45a) for a complete list of the affected operations. If you access your data via HTTPS, you must [bind a valid SSL Certificate](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-by-https-protocol) to your custom domain. This is mandatory for OSS Console access, as the console enforces HTTPS.


-

Access credential: Create an AccessKey pair with OSS access permissions in [Resource Access Management (RAM)](https://ram.console.alibabacloud.com/users/create).

## Java


AWS SDK for Java 2.x


`java
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;
import java.net.URI;

S3Client s3Client = S3Client.builder()
    .endpointOverride(URI.create("https://s3.oss-cn-hangzhou.aliyuncs.com"))
    .region(Region.AWS_GLOBAL)
    .serviceConfiguration(
        S3Configuration.builder()
            .pathStyleAccessEnabled(false)
            .chunkedEncodingEnabled(false)
            .build()
    )
    .build();
`


AWS SDK for Java 1.x


`java
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
    .withEndpointConfiguration(new EndpointConfiguration(
        "https://s3.oss-cn-hangzhou.aliyuncs.com",
        "cn-hangzhou"))
    .withPathStyleAccessEnabled(false)
    .withChunkedEncodingDisabled(false)
    .build();
`


When you use AWS SDK for Java 1.x, calling `close()` on the `S3ObjectInputStream` returned by `getObject` immediately discards any unread data. Read the data completely before you close the stream.


`java
S3Object object = s3Client.getObject("my-bucket", "file.txt");
InputStream input = object.getObjectContent();

bytedata = IOUtils.toByteArray(input);

input.close();
`


## Python


`python
import boto3
from botocore.config import Config

s3 = boto3.client(
    's3',
    endpoint_url='https://s3.oss-cn-hangzhou.aliyuncs.com',
    config=Config(
        signature_version='s3',
        s3={'addressing_style': 'virtual'}
    )
)

`


## Node.js


AWS SDK for Node.js 3.0


`nodejs
import { S3Client } from '@aws-sdk/client-s3';

const client = new S3Client({
    endpoint: 'https://s3.oss-cn-hangzhou.aliyuncs.com',
    region: 'cn-hangzhou'
});
`


AWS SDK for Node.js 2.0


`nodejs
const AWS = require('aws-sdk');

const s3 = new AWS.S3({
    endpoint: 'https://s3.oss-cn-hangzhou.aliyuncs.com',
    region: 'cn-hangzhou'
});
`


## Go


AWS SDK for Go 2.0


`go
import (
    "context"
    "github.com/aws/aws-sdk-go-v2/aws"
    awsconfig "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)

cfg, _ := awsconfig.LoadDefaultConfig(context.TODO(),
    awsconfig.WithEndpointResolverWithOptions(
        aws.EndpointResolverWithOptionsFunc(func(service, region string, options ...interface{}) (aws.Endpoint, error) {
            return aws.Endpoint{
                URL: "https://s3.oss-cn-hangzhou.aliyuncs.com",
            }, nil
        }),
    ),
)
client := s3.NewFromConfig(cfg)
`


AWS SDK for Go 1.0


`go
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)

sess := session.Must(session.NewSessionWithOptions(session.Options{
    Config: aws.Config{
        Endpoint: aws.String("https://s3.oss-cn-hangzhou.aliyuncs.com"),
        Region:   aws.String("cn-hangzhou"),
    },
    SharedConfigState: session.SharedConfigEnable,
}))
svc := s3.New(sess)
`


## .NET


AWS SDK for .NET 3.x


`csharp
using Amazon.S3;

var config = new AmazonS3Config
{
    ServiceURL = "https://s3.oss-cn-hangzhou.aliyuncs.com"
};
var client = new AmazonS3Client(config);
`


AWS SDK for .NET 2.x


`csharp
using Amazon.S3;

var config = new AmazonS3Config
{
    ServiceURL = "https://s3.oss-cn-hangzhou.aliyuncs.com"
};
var client = new AmazonS3Client(config);
`


## PHP


AWS SDK for PHP 3.x


`php
<?php
require_once __DIR__ . '/vendor/autoload.php';
use Aws\S3\S3Client;

$s3Client = new S3Client([
    'version' => '2006-03-01',
    'region'  => 'cn-hangzhou',
    'endpoint' => 'https://s3.oss-cn-hangzhou.aliyuncs.com'
]);
`


AWS SDK for PHP 2.x


`php
<?php
require_once __DIR__ . '/vendor/autoload.php';
use Aws\S3\S3Client;

$s3Client = S3Client::factory([
    'version' => '2006-03-01',
    'region'  => 'cn-hangzhou',
    'base_url' => 'https://s3.oss-cn-hangzhou.aliyuncs.com'
]);
`


## Ruby


AWS SDK for Ruby 3.x


`ruby
require 'aws-sdk-s3'

s3 = Aws::S3::Client.new(
  endpoint: 'https://s3.oss-cn-hangzhou.aliyuncs.com',
  region: 'cn-hangzhou'
)
`


AWS SDK for Ruby 2.x


`ruby
require 'aws-sdk'

s3 = AWS::S3::Client.new(
  s3_endpoint: 's3.oss-cn-hangzhou.aliyuncs.com',
  region: 'cn-hangzhou',
  s3_force_path_style: false
)

`


## C++


Requires SDK 1.7.68 or later.


`c++
#include <aws/s3/S3Client.h>
#include <aws/core/client/ClientConfiguration.h>

Aws::Client::ClientConfiguration config;
config.endpointOverride = "s3.oss-cn-hangzhou.aliyuncs.com";
config.region = "cn-hangzhou";

Aws::S3::S3Client s3_client(config);
`


## Browser


Frontend web applications must use temporary credentials from Security Token Service (STS). Do not hard-code permanent AccessKeys in the client. The server calls the [AssumeRole](https://api.aliyun.com/api/Sts/2015-04-01/AssumeRole?RegionId=cn-hangzhou) operation to obtain temporary credentials and returns them to the client. For a complete tutorial, see [Use STS temporary credentials to access OSS](https://www.alibabacloud.com/help/en/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss).


`javascript
import { S3Client } from '@aws-sdk/client-s3';

// Obtain STS temporary credentials from the server
async function getSTSCredentials() {
    const response = await fetch('https://your-server.com/api/sts-token');
    return await response.json();
}

// Initialize the S3 client with temporary credentials
const client = new S3Client({
    region: 'cn-hangzhou',
    endpoint: 'https://s3.oss-cn-hangzhou.aliyuncs.com',
    credentials: async () => {
        const creds = await getSTSCredentials();
        return {
            accessKeyId: creds.accessKeyId,
            secretAccessKey: creds.secretAccessKey,
            sessionToken: creds.securityToken,
            expiration: new Date(creds.expiration)
        };
    }
});
`


## Android


Mobile applications (Android) must use temporary credentials from Security Token Service (STS). Do not hard-code permanent AccessKeys in the client. The server calls the [AssumeRole](https://api.aliyun.com/api/Sts/2015-04-01/AssumeRole?RegionId=cn-hangzhou) operation to obtain temporary credentials and returns them to the client. For a complete tutorial, see [Use STS temporary credentials to access OSS](https://www.alibabacloud.com/help/en/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss).


`java
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.auth.BasicSessionCredentials;
import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;

// Implement a credentials provider to obtain STS temporary credentials from the server.
public class OSSCredentialsProvider implements AWSCredentialsProvider {
    @Override
    public AWSCredentials getCredentials() {
        // Obtain STS temporary credentials from your server.
        // Request https://your-server.com/api/sts-token.
        String accessKeyId = fetchFromServer("accessKeyId");
        String secretKeyId = fetchFromServer("secretKeyId");
        String securityToken = fetchFromServer("securityToken");

        return new BasicSessionCredentials(accessKeyId, secretKeyId, securityToken);
    }

    @Override
    public void refresh() {
        // Refresh the credentials.
    }
}

// Create the S3 client.
AmazonS3 s3Client = AmazonS3Client.builder()
    .withCredentials(new OSSCredentialsProvider())
    .withEndpointConfiguration(new EndpointConfiguration(
        "https://s3.oss-cn-hangzhou.aliyuncs.com", ""))
    .build();

// Business logic.
s3Client.putObject("my-bucket", "test.txt", "Hello OSS");
`


## iOS


Mobile applications (iOS) must use temporary credentials from Security Token Service (STS). Do not hard-code permanent AccessKeys in the client. The server calls the [AssumeRole](https://api.aliyun.com/api/Sts/2015-04-01/AssumeRole?RegionId=cn-hangzhou) operation to obtain temporary credentials and returns them to the client. For a complete tutorial, see [Use STS temporary credentials to access OSS](https://www.alibabacloud.com/help/en/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss).


`objectc
#import <AWSS3/AWSS3.h>

// Implement the credentials provider.
@interface OSSCredentialsProvider : NSObject <AWSCredentialsProvider>
@end

@implementation OSSCredentialsProvider

- (AWSTask<AWSCredentials *> *)credentials {
    return [[AWSTask taskWithResult:nil] continueWithBlock:^id(AWSTask *task) {
        // Obtain STS temporary credentials from the server.
        NSString *accessKey = [self fetchFromServer:@"accessKeyId"];
        NSString *secretKey = [self fetchFromServer:@"secretKeyId"];
        NSString *sessionToken = [self fetchFromServer:@"securityToken"];

        AWSCredentials *credentials = [[AWSCredentials alloc]
            initWithAccessKey:accessKey
            secretKey:secretKey
            sessionKey:sessionToken
            expiration:[NSDate dateWithTimeIntervalSinceNow:3600]];

        return [AWSTask taskWithResult:credentials];
    }];
}

@end

// Configure the S3 client.
AWSEndpoint *endpoint = [[AWSEndpoint alloc] initWithURLString:@"https://s3.oss-cn-hangzhou.aliyuncs.com"];
AWSServiceConfiguration *configuration = [[AWSServiceConfiguration alloc]
    initWithRegion:AWSRegionUnknown
    endpoint:endpoint
    credentialsProvider:[[OSSCredentialsProvider alloc] init]];

[AWSS3 registerS3WithConfiguration:configuration forKey:@"OSS"];
AWSS3 *s3 = [AWSS3 S3ForKey:@"OSS"];

// Business logic.
AWSS3PutObjectRequest *request = [AWSS3PutObjectRequest new];
request.bucket = @"my-bucket";
request.key = @"test.txt";
request.body = [@"Hello OSS" dataUsingEncoding:NSUTF8StringEncoding];

[[s3 putObject:request] continueWithBlock:^id(AWSTask *task) {
    if (task.error) {
        NSLog(@"Error: %@", task.error);
    } else {
        NSLog(@"Success");
    }
    return nil;
}];
`


## FAQ

#### Upload failure: InvalidArgument: aws-chunked encoding is not supportedDescription: An error occurs when you upload a file:


`plaintext
InvalidArgument: aws-chunked encoding is not supported with the specified x-amz-content-sha256 value
`


Root cause:


This is the most common issue when you access OSS using an AWS SDK. OSS supports the AWS Signature V4 algorithm, but there is a difference in transfer encoding:


-

AWS S3: Uses chunked encoding by default to transfer large files.

-

OSS: Does not support chunked encoding for transfers.


Cause analysis:


The Signature V4 implementation in some SDKs is tied to chunked encoding:


-

Python (boto3): Signature V4 forces the use of chunked encoding, which cannot be disabled. You must switch to Signature V2.

-

Java: You can disable chunked encoding through configuration.

-

Go/Node.js: Chunked encoding is not used by default. No special handling is required.


Solutions (by SDK):






































| SDK | Solution | Reason |
| --- | --- | --- |
| Python (boto3) | Use Signature V2: signature_version='s3' | The boto3 Signature V4 implementation is tied to chunked encoding and cannot be disabled. |
| Java 1.x | Signature V4 + .withChunkedEncodingDisabled(true) | Chunked encoding can be disabled. |
| Java 2.x | Signature V4 + .chunkedEncodingEnabled(false) | Chunked encoding can be disabled. |
| Go v1 | Signature V4 | Does not use chunked encoding by default. |
| Go v2 | Signature V4. Note that the Manager may use it for large file uploads. | The Manager feature might use chunked encoding. |
| Node.js v3 | Signature V4 | Does not use chunked encoding by default. |


Python example (before and after fix):


`python
# Incorrect configuration (boto3's V4 implementation uses chunked encoding)
s3 = boto3.client('s3',
    endpoint_url='https://oss-cn-hongkong.aliyuncs.com',
    config=Config(signature_version='v4'))

# Correct configuration (boto3 uses V2 signature)
s3 = boto3.client('s3',
    endpoint_url='https://oss-cn-hongkong.aliyuncs.com',
    config=Config(signature_version='s3'))  # V2 signature is the stable solution for boto3
`


Technical details:


The OSS implementation of Signature V4 follows the AWS Signature Version 4 specification but has the following requirements:


-

The request header must include `x-oss-content-sha256: UNSIGNED-PAYLOAD`.

-

The `Transfer-Encoding: chunked` transfer method must not be used.


You can make most SDKs compatible through configuration. However, the Signature V4 implementation in boto3 is tightly coupled with chunked encoding. Therefore, you must use Signature V2 with boto3.

#### SDK and signature version selectionVersion selection reference:



































| Language | SDK version | Signature version | Key configuration points |
| --- | --- | --- | --- |
| Python | Latest boto3 version | Signature V2 (s3) | The boto3 Signature V4 implementation is not compatible with OSS. |
| Java 1.x | Latest 1.x | Signature V4 | Chunked encoding must be disabled. |
| Java 2.x | Latest 2.x | Signature V4 | Chunked encoding must be disabled. |
| Node.js | v3 | Signature V4 (default) | - |
| Go v1 | Latest v1 | Signature V4 (default) | - |
| Go v2 | Latest v2 | Signature V4 (default) | Note the Manager for large file uploads. |


Signature version details:


-

OSS Signature V4: OSS fully supports the AWS Signature V4 algorithm.

-

Signature V2: This is a special case for boto3. You must use Signature V2 because of limitations in the SDK implementation.

-

Compatibility: With the exception of boto3, all other SDKs can use Signature V4 to access OSS.


Version selection for new projects:


























| Scenario | Optional Solutions | Reason |
| --- | --- | --- |
| New Python project | boto3 + Signature V2 | boto3 does not currently support OSS Signature V4. |
| New Java project | Java 2.x + Signature V4 | Better performance. |
| New Node.js project | v3 + Signature V4 | - |
| New Go project | Go v1 + Signature V4 | Recommended. |
| Existing project migration | Keep the current SDK version. | Minimizes the risk of breaking changes. |


#### Signature error: SignatureDoesNotMatch


You might encounter a `SignatureDoesNotMatch` error. This error indicates that the signature calculated by the server does not match the signature provided by the client.


The most common cause is using an AWS AccessKey instead of an OSS AccessKey in your code. AWS access credentials and OSS access credentials are two completely separate systems and cannot be used interchangeably. Check parameters such as `aws_access_key_id` and `aws_secret_access_key` in your code. Make sure that you are using the AccessKey ID and AccessKey secret created in the OSS console.


The second most common cause is server clock drift. The S3 signature algorithm includes a timestamp in the signature. The OSS server verifies the difference between the request time and its own server time. If the clock on your server is more than 15 minutes off from the standard time, all requests are rejected. You can check your server's UTC time by running the `date -u` command. If the time is incorrect, use `ntpdate` or a system time synchronization service to correct it.


A third cause is an incorrect Endpoint configuration. The signature calculation fails if the Endpoint points to an AWS domain name, such as `s3.amazonaws.com`, or specifies the wrong OSS region. The standard format of an OSS Endpoint is `https://oss-{region}.aliyuncs.com`. The region in the Endpoint must match the region where the bucket is located, such as `oss-cn-hangzhou` or `oss-cn-beijing`.


When you use boto3, there is another specific cause. If `signature_version='s3'` is not configured, boto3 uses the default Signature V4, which causes the signature to fail. The correct boto3 configuration must include the `Config(signature_version='s3')` parameter.


A simple way to verify your configuration is to use the ossutil command line interface. Run `ossutil ls oss://your-bucket --access-key-id <key> --access-key-secret <secret> --endpoint oss-cn-hangzhou.aliyuncs.com`. If the command successfully lists the bucket's contents, your access credentials and Endpoint are correct. This indicates that the problem is in your code's configuration.

#### Bucket access errors


`NoSuchBucket` or `AccessDenied` errors indicate that the specified bucket cannot be accessed. The most common cause is a mismatch between the Endpoint and the bucket's region.


Each OSS bucket belongs to a specific region, such as `cn-hangzhou` or `cn-beijing`. When you access a bucket, the Endpoint must use the domain name that corresponds to the bucket's region. For example, if your bucket is in the Hangzhou region, the Endpoint is `oss-cn-hangzhou.aliyuncs.com`. You cannot use the Endpoint for the Beijing region, `oss-cn-beijing.aliyuncs.com`. This behavior is different from AWS S3, which allows cross-region access and performs automatic redirection. OSS does not support cross-region access. Using an incorrect Endpoint results in a `NoSuchBucket` error.


A second cause is an issue with the RAM permission configuration. Check if the RAM user associated with your OSS AccessKey has permission to access the target bucket. In the RAM console, confirm that the user is granted the necessary permissions, such as `oss:ListObjects`, `oss:GetObject`, and `oss:PutObject`.


A third cause is related to bucket naming conventions. OSS supports two URL styles: virtual host style (`bucket-name.oss-cn-hangzhou.aliyuncs.com`) and path style (`oss-cn-hangzhou.aliyuncs.com/bucket-name`). When you use the virtual host style, the bucket name must comply with DNS naming conventions and cannot contain an underscore (_). If your bucket name contains an underscore, you must use the path style in your SDK configuration or create a new bucket with a compliant name.

#### Performance optimization


Uploading and downloading large files are common requirements for object storage applications. AWS SDKs provide several transfer acceleration mechanisms that are also effective with OSS.


When you use Python boto3, you can configure multipart upload parameters with `TransferConfig`. When a file is larger than the configured threshold, boto3 automatically splits the file into multiple parts and uploads them concurrently. This significantly increases transfer speed. The `multipart_threshold` parameter controls the file size threshold for enabling multipart uploads. `max_concurrency` controls the number of concurrent upload threads. `multipart_chunksize` controls the size of each part. Properly configuring these parameters can increase the upload speed for large files over 100 MB by several times.


When you use the Java SDK, the `TransferManager` class encapsulates features such as multipart upload, concurrent transfers, and automatic retries. `TransferManager` automatically selects the optimal transfer strategy based on the file size, which means you do not need to manually handle the part logic.


When you use the Go SDK, you can call `s3manager.Uploader` instead of directly calling `PutObject`. The `Uploader` has a built-in concurrent multipart upload feature that can automatically split large files for concurrent uploads and handle retry logic for failed uploads.


When you use the Node.js SDK, you can use the `Upload` class from the `@aws-sdk/lib-storage` package. This class supports streaming uploads, which lets you start uploading a file while it is still being read. This reduces memory usage. For an example, see the Node.js section above.


All these transfer acceleration mechanisms are based on the S3 Multipart Upload API. OSS is fully compatible with these APIs, so you can use them directly without changing your code.


Thank you! We've received your  feedback.