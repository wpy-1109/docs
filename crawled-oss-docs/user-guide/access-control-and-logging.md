# Access control and logs for vector buckets in Alibaba Cloud OSS

Vector buckets provide access control and log management features to ensure data security, compliance, and observability.

## Access control


Vector buckets support bucket policies and RAM policies.


-

Bucket policy: A resource-based authorization policy that you can attach to a bucket to grant other Alibaba Cloud accounts, Resource Access Management (RAM) users, or anonymous users access to specified vector resources.

-

RAM policy: An identity-based authorization policy that you can attach to RAM users, user groups, or roles to define which vector bucket resources they can access.

### Supported actions


(https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorbucket)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvectorbucket)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorbuckets)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectorbucket)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy#reference-2424532)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicy#reference-2424982)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpolicy#reference-2424995)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorindex)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvectorindex)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorindexes)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectorindex)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/queryvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectors)


| API | Action | Description |
| --- | --- | --- |
| PutVectorBucket | oss:PutVectorBucket | Creates a vector bucket. |
| GetVectorBucket | oss:GetVectorBucket | Gets the details of a vector bucket. |
| ListVectorBuckets | oss:ListVectorBuckets | Lists all vector buckets owned by the requester. |
| DeleteVectorBucket | oss:DeleteVectorBucket | Deletes a vector bucket. |
| PutBucketLogging | oss:PutBucketLogging | Enables the log storage feature for a vector bucket. |
| oss:PutObject | Writes logs from the source vector bucket to a destination bucket when you enable log storage for the source vector bucket. |
| GetBucketLogging | oss:GetBucketLogging | Views the log storage configuration of a vector bucket. |
| DeleteBucketLogging | oss:DeleteBucketLogging | Disables the log storage feature for a vector bucket. |
| PutBucketPolicy | oss:PutBucketPolicy | Sets the authorization policy for a specified vector bucket. |
| GetBucketPolicy | oss:GetBucketPolicy | Gets the authorization policy of a specified vector bucket. |
| DeleteBucketPolicy | oss:DeleteBucketPolicy | Deletes the authorization policy of a specified vector bucket. |
| PutVectorIndex | oss:PutVectorIndex | Creates a vector index. |
| GetVectorIndex | oss:GetVectorIndex | Gets the details of a vector index. |
| ListVectorIndexes | oss:ListVectorIndexes | Lists all vector indexes in a vector bucket. |
| DeleteVectorIndex | oss:DeleteVectorIndex | Deletes a vector index. |
| PutVectors | oss:PutVectors | Writes vector data. |
| GetVectors | oss:GetVectors | Gets specified vector data. |
| ListVectors | oss:ListVectors | Lists all vector data in a vector index. |
| QueryVectors | oss:QueryVectors | Performs a vector similarity search. |
| DeleteVectors | oss:DeleteVectors | Deletes specified vector data from a vector index. |


### Resource description format


























| Resource level | Format | Example |
| --- | --- | --- |
| All vector resources | acs:ossvector:*:*:* | acs:ossvector:*:*:* |
| Vector bucket | acs:ossvector:{region}:{account_id}:{bucket_name} | acs:ossvector:*:*:my-vector-bucket |
| Vector index | acs:ossvector:{region}:{account_id}:{bucket_name}/{index_name} | acs:ossvector:*:*:my-vector-bucket/my-index |
| Vector data | acs:ossvector:{region}:{account_id}:{bucket_name}/{index_name}/* | acs:ossvector:*:*:my-vector-bucket/my-index/* |


### Bucket policy


You can use a bucket policy to grant RAM users and other accounts access to specified OSS resources.

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target bucket. In the navigation pane on the left, choose Access Control > Bucket Authorization Policy.

-

Click Add By Syntax Policy and enter the policy in the editor. For example, to grant users read and write permissions on the vector data in `my-vector-bucket`:


`json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "oss:PutVectors",
        "oss:GetVectors"
      ],
      "Principal": [
         "*"
      ],
      "Resource": [
        "acs:ossvector:*:*:my-vector-bucket/my-index/*"
      ]
    }
  ]
}
`


-

Click OK to create the policy.

## ossutil


The following example shows how to use a JSON configuration file to set an authorization policy for a vector bucket that allows a specified user to perform vector-related operations. The content of vector-policy.json is as follows:


`json
{
   "Version":"1",
   "Statement":[
       {
         "Action":[
           "oss:PutVectors",
           "oss:GetVectors"
        ],
        "Effect":"Deny",
        "Principal":["1234567890"],
        "Resource":["acs:ossvector:cn-hangzhou:1234567890:*"]
       }
    ]
}
`


`bash
ossutil vectors-api put-bucket-policy --bucket vector-example --body file://vector-policy.json
`


You can use JSON configuration parameters to set the vector bucket policy:


`bash
ossutil vectors-api put-bucket-policy --bucket vector-example --body "{\"Version\":\"1\",\"Statement\":[{\"Action\":[\"oss:PutVectors\",\"oss:GetVectors\",\"oss:QueryVectors\"],\"Effect\":\"Allow\",\"Principal\":[\"1234567890\"],\"Resource\":[\"acs:ossvector:cn-hangzhou:1234567890:bucket/vector-example/*\"]}]}"
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="A sample for putting a bucket policy for a vector bucket")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--account_id', help='The account id.', required=True)

def main():
    args = parser.parse_args()

    # Loading credentials values from the environment variables
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)


    policy_content = '''
        {
           "Version":"1",
           "Statement":[
               {
                 "Action":[
                   "oss:PutVectors",
                   "oss:GetVectors"
                ],
                "Effect":"Deny",
                "Principal":["1234567890"],
                "Resource":["acs:ossvector:cn-hangzhou:1234567890:*"]
               }
            ]
         }
    '''

    result = vector_client.put_bucket_policy(oss_vectors.models.PutBucketPolicyRequest(
        bucket=args.bucket,
        body=policy_content
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
    )

if __name__ == "__main__":
    main()
`


## Go


`
package main

import (
	"context"
	"flag"
	"log"
	"strings"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
)

var (
	region     string
	bucketName string
	accountId  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
}

func main() {
	flag.Parse()
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accounId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.PutBucketPolicyRequest{
		Bucket: oss.Ptr(bucketName),
		Body: strings.NewReader(`{
			   "Version":"1",
			   "Statement":[
			   {
				 "Action":[
				   "oss:PutVectors",
				   "oss:GetVectors"
				],
				"Effect":"Deny",
				"Principal":["1234567890"],
				"Resource":["acs:ossvector:cn-hangzhou:1234567890:*"]
			   }
			  ]
			 }`),
	}
	result, err := client.PutBucketPolicy(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put vector bucket policy %v", err)
	}

	log.Printf("put vector bucket policy result:%#v\n", result)
}

`


## API


You can call the [PutBucketPolicy](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy) operation to set an authorization policy for a vector bucket.

### RAM policy


Vector buckets support RAM policies. You can use the [Resource Access Management (RAM) console](https://ram.console.alibabacloud.com/) to configure permissions for vector buckets for RAM users or roles. RAM policies support granting permissions at the index level.

## Log management


Vector buckets support the access log feature. You can store access records in a specified OSS bucket for security audits, performance analysis, and troubleshooting.

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target bucket. In the navigation pane on the left, choose Log Management > Log Storage.

-

Turn on the Log Storage switch and configure the following parameters:


-

Target Storage Location: Select a bucket to store the log files. The bucket must be in the same region as the vector bucket.

-

Log Prefix: Set the directory and prefix for the log files, such as `MyLog-`.

-

Authorization Role: Use the default Simple Log Service role AliyunOSSLoggingDefaultRole or select a custom role.

## ossutil


The following example shows how to enable log storage for a bucket named `examplebucket`. The log file prefix is `MyLog-`, and the bucket that stores the access logs is `examplebucket`.


-

You can use a JSON configuration file. The content of bucket-logging-status.json is as follows:


`json
{
  "BucketLoggingStatus": {
    "LoggingEnabled": {
      "TargetBucket": "examplebucket",
      "TargetPrefix": "MyLog-",
      "LoggingRole": "AliyunOSSLoggingDefaultRole"
    }
  }
}
`


The following is a sample command:


`bash
ossutil vectors-api put-bucket-logging --bucket examplebucket --bucket-logging-status file://bucket-logging-status.json
`


-

You can use JSON configuration parameters. The following is a sample command:


`bash
ossutil vectors-api put-bucket-logging --bucket examplebucket --bucket-logging-status "{\"BucketLoggingStatus\":{\"LoggingEnabled\":{\"TargetBucket\":\"examplebucket\",\"TargetPrefix\":\"MyLog-\",\"LoggingRole\":\"AliyunOSSLoggingDefaultRole\"}}}"
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector put bucket logging sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--account_id', help='The account id.', required=True)
parser.add_argument('--target_bucket', help='The name of the target bucket.', required=True)

def main():
    args = parser.parse_args()

    # Load credential values from environment variables.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Use the default configuration of the SDK.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)

    result = vector_client.put_bucket_logging(oss_vectors.models.PutBucketLoggingRequest(
        bucket=args.bucket,
        bucket_logging_status=oss_vectors.models.BucketLoggingStatus(
            logging_enabled=oss_vectors.models.LoggingEnabled(
                target_bucket=args.target_bucket,
                target_prefix='log-prefix',
                logging_role='AliyunOSSLoggingDefaultRole'
            )
        )
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
    )

if __name__ == "__main__":
    main()

`


## Go


`
package main

import (
	"context"
	"flag"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

var (
	region     string
	bucketName string
	accountId  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
}

func main() {
	flag.Parse()
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accounId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.PutBucketLoggingRequest{
		Bucket: oss.Ptr(bucketName),
		BucketLoggingStatus: &vectors.BucketLoggingStatus{
			&vectors.LoggingEnabled{
				TargetBucket: oss.Ptr("TargetBucket"),
				TargetPrefix: oss.Ptr("TargetPrefix"),
				LoggingRole:  oss.Ptr("AliyunOSSLoggingDefaultRole"),
			},
		},
	}
	result, err := client.PutBucketLogging(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put vector bucket logging %v", err)
	}

	log.Printf("put vector bucket logging result:%#v\n", result)
}

`


## API


You can call the [PutBucketLogging](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging) operation to enable log storage for a vector bucket.

### Log file naming convention


The naming convention for stored log files is as follows:


`plaintext
<TargetPrefix><SourceBucket>YYYY-mm-DD-HH-MM-SS-UniqueString
`








| Field | Description |
| --- | --- |
| TargetPrefix | The prefix of the log file name. |
| SourceBucket | The name of the source bucket that generates the access logs. |
| YYYY-mm-DD-HH-MM-SS | The time partition of the log. From left to right, the fields represent year, month, day, hour, minute, and second. The stored logs are organized by the hour. For example, if HH is 01, it indicates logs from 01:00:00 to 01:59:59. MM and SS are both pushed as 00. |
| UniqueString | A system-generated string that uniquely identifies the log file. |


### Log format and example


-

Log format


OSS access logs contain information about the requester and the accessed resource. The log entries are formatted as follows:


`plaintext
RemoteIP Reserved Reserved Time "RequestURL" HTTPStatus SentBytes RequestTime "Referer" "UserAgent" "HostName" "RequestID" "LoggingFlag" "RequesterAliyunID" "Operation" "BucketName" "ObjectName" ObjectSize ServerCostTime "ErrorCode" RequestLength "UserID" DeltaDataSize "SyncRequest" "StorageClass" "TargetStorageClass" "TransmissionAccelerationAccessPoint" "AccessKeyID" "BucketARN"
`














-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-



-


> NOTE:

> NOTE: 


> NOTE: 


| Field | Example value | Description |
| --- | --- | --- |
| RemoteIP | 192.168.0.1 | The IP address of the requester. |
| Reserved | - | Reserved field. The value is fixed at -. |
| Reserved | - | Reserved field. The value is fixed at -. |
| Time | 03/Jan/2021:14:59:49 +0800 | The time when OSS received the request. |
| RequestURL | GET /example.jpg HTTP/1.0 | The request URL that includes the query string.OSS ignores query string parameters that start with x-, but these parameters are recorded in the access log. You can use query string parameters that start with x- to mark a request and then use this mark to quickly find the corresponding log. |
| HTTPStatus | 200 | The HTTP status code returned by OSS. |
| SentBytes | 999131 | The downstream traffic generated by the request, in bytes. |
| RequestTime | 127 | The time taken to complete the request, in ms. |
| Referer | http://www.aliyun.com/product/oss | The HTTP Referer of the request. |
| UserAgent | curl/7.15.5 | The User-Agent header of the HTTP request. |
| HostName | examplebucket.oss-cn-hangzhou.aliyuncs.com | The destination domain name accessed by the request. |
| RequestID | 5FF16B65F05BC932307A3C3C | The request ID. |
| LoggingFlag | true | Indicates whether log storage is enabled. Valid values:true: Log storage is enabled.false: Log storage is not enabled. |
| RequesterAliyunID | 16571836914537 | The user ID of the requester. A value of - indicates an anonymous access. |
| Operation | GetObject | The request type. |
| BucketName | examplebucket | The name of the destination bucket. |
| ObjectName | example.jpg | The name of the destination object. |
| ObjectSize | 999131 | The size of the destination object, in bytes. |
| ServerCostTime | 88 | The time OSS spent processing the request, in milliseconds. |
| ErrorCode | - | The error code returned by OSS. A value of - indicates that no error code was returned. |
| RequestLength | 302 | The length of the request, in bytes. |
| UserID | 16571836914537 | The ID of the bucket owner. |
| DeltaDataSize | - | The change in the object size. A value of - indicates that the request does not involve writing to the object. |
| SyncRequest | - | The request type. Valid values:-: A general request.cdn: An origin request from Alibaba Cloud CDN.lifecycle: A request to dump or delete data through a lifecycle rule. |
| StorageClass | Standard | The storage class of the destination object. Valid values:Standard: Standard.IA: Infrequent Access.Archive: Archive Storage.Cold Archive: Cold Archive.DeepCold Archive: Deep Cold Archive.-: The object storage class was not obtained. |
| TargetStorageClass | - | Indicates whether the storage class of the object was converted by a lifecycle rule or a CopyObject operation. Valid values:Standard: Converted to Standard.IA: Converted to Infrequent Access.Archive: Converted to Archive Storage.Cold Archive: Converted to Cold Archive.DeepCold Archive: Converted to Deep Cold Archive.-: The operation does not involve converting the object storage class. |
| TransmissionAccelerationAccessPoint | - | The transfer acceleration endpoint used when accessing the destination bucket through an acceleration endpoint. For example, if a requester accesses the destination bucket through an endpoint in the China (Hangzhou) region, the value is cn-hangzhou.A value of - indicates that an acceleration endpoint was not used or the transfer acceleration endpoint is in the same region as the destination bucket. |
| AccessKeyID | LTAI | The AccessKey ID of the requester.If the request is initiated from the console, the log field displays a temporary AccessKey ID that starts with TMP.If the request is initiated using a tool or a software development kit (SDK) with a long-term key, the log field displays a common AccessKey ID, such as LTAI.If the request is initiated using Security Token Service (STS) temporary access credentials, the log field displays a temporary AccessKey ID that starts with STS.Note A value of - in the AccessKey ID field indicates an anonymous request. |
| BucketArn | acs:oss* | The globally unique resource descriptor of the bucket. |


-

Log example


`plaintext
192.168.0.1 - - [03/Jan/2021:14:59:49 +0800] "GET /example.jpg HTTP/1.0" 200 999131 127 "http://www.aliyun.com/product/oss" "curl/7.15.5" "examplebucket.oss-cn-hangzhou.aliyuncs.com" "5FF16B65F05BC932307A3C3C" "true" "16571836914537" "GetObject" "examplebucket" "example.jpg" 999131 88 "-" 302 "16571836914537" - "cdn" "standard" "-" "-" "LTAI" "acs:oss*"
`


After log files are stored in the specified OSS bucket, you can import them into Simple Log Service for analysis. For more information about how to import data, see [Import OSS data](https://www.alibabacloud.com/help/en/sls/import-data-from-oss-to-log-service#task-2372154). For more information about the analysis features of Simple Log Service, see [Query and analysis overview](https://www.alibabacloud.com/help/en/sls/log-analysis-overview#concept-nyf-cjq-zdb).

Thank you! We've received your  feedback.