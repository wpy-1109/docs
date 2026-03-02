# Call the PutBucketLogging operation to enable the log storage feature for a bucket

Enables logging for a bucket. After you enable and configure logging for a bucket, Object Storage Service (OSS) generates log objects based on a predefined naming convention. This way, access logs are generated and stored in the specified bucket on an hourly basis.

## Usage notes


-

The `oss:PutBucketLogging` permission is required for enabling logging for a bucket by calling the PutBucketLogging operation. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

The source bucket for which logs are generated and the destination bucket in which the logs are stored can be the same or different. However, the destination bucket must belong to the same Alibaba Cloud account in the same region as the source bucket.

-

OSS generates bucket access logs on an hourly basis. However, requests in an hour may be recorded in the log generated for the previous or subsequent hour.


For more information about the naming conventions of log objects and log format, see [Logging](https://www.alibabacloud.com/help/en/oss/user-guide/logging#section-ap2-qc2-ef2).

-

Before you disable logging, OSS keeps generating log objects. Delete log objects that you no longer need to reduce your storage costs.


You can configure lifecycle rules to regularly delete log objects. For more information, see [Lifecycle rules based on the last modified time](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#concept-y2g-szy-5db).

-

More fields may be added to OSS logs. We recommend that developers consider potential compatibility issues when they develop log processing tools.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM policies](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).

















| API | Action | Definition |
| --- | --- | --- |
| PutBucketLogging | oss:PutBucketLogging | Enables logging for a bucket. |
| oss:PutObject | When enabling logging for a bucket, if the logs are written to another bucket, this permission is required for the destination bucket. |


## Request syntax


`plaintext
PUT /?logging HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Authorization: SignatureValue
Host: Host
<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus>
    <LoggingEnabled>
        <TargetBucket>TargetBucket</TargetBucket>
        <TargetPrefix>TargetPrefix</TargetPrefix>
    </LoggingEnabled>
</BucketLoggingStatus>
`


## Request headers


A PutBucketLogging request contains only common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements

















| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| BucketLoggingStatus | Container | Yes | N/A | The container that stores the logging status information. Child nodes: LoggingEnabledParent nodes: none |
| LoggingEnabled | Container | This parameter is required when you enable logging. | N/A | The container that stores the access log information. Child nodes: TargetBucket, TargetPrefix and LoggingRoleParent nodes: BucketLoggingStatus |
| TargetBucket | String | This parameter is required when you enable logging. | examplebucket | The bucket that stores access logs. Child nodes: noneParent nodes: BucketLoggingStatus and LoggingEnabled |
| TargetPrefix | String | No | MyLog- | The prefix of the saved log objects. This element can be left empty. Child nodes: noneParent nodes: BucketLoggingStatus and LoggingEnabled |
| LoggingRole | String | No | AliyunOSSLoggingDefaultRole | The role with permissions for logging.Child nodes: noneParent node: BucketLoggingStatus.LoggingEnabled |


## Response headers


All headers in the response to a PutBucketLogging request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Examples for buckets


-

Sample request for enabling logging


`plaintext
PUT /?logging HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Length: 186
Date: Thu, 17 Apr 2025 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus>
    <LoggingEnabled>
        <TargetBucket>examplebucket</TargetBucket>
        <TargetPrefix>MyLog-</TargetPrefix>
        <LoggingRole>AliyunOSSLoggingDefaultRole</LoggingRole>
    </LoggingEnabled>
</BucketLoggingStatus>
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E888648906008B
Date: Fri, 04 May 2012 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


-

Sample request for disabling logging


To disable logging for a bucket, only send an empty BucketLoggingStatus. Example:


`plaintext
PUT /?logging HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Type: application/xml
Content-Length: 86
Date: Thu, 17 Apr 2025 04:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus>
</BucketLoggingStatus>
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674125A4D8906008B
Date: Fri, 04 May 2012 04:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


Examples for vector buckets
When specifying the `Host` for a vector bucket, use the standard Alibaba Cloud region ID (example: `cn-hangzhou`). Do not use the legacy OSS region ID (example: `oss-cn-hangzhou`) used for general-purpose buckets.

Sample request for enabling logging


`http
PUT /?logging HTTP/1.1
Host: exampebucket-123*456.cn-hangzhou.oss-vectors.aliyuncs.com
Content-Length: 186
Content-Type: application/json
Date: Thu, 17 Apr 2025 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

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


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E888648906008B
Date: Fri, 04 May 2012 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## OSS SDKs


Use OSS SDKs for the following programming languages to call the PutBucketLogging operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-1#undefined)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-logging-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-logging-2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-logging-5)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-12#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-2#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-8#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-6#undefined)

## ossutil


For information about the ossutil command that corresponds to the PutBucketLogging operation, see [put-bucket-logging](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-logging).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The error message returned because the source bucket does not exist. |
| InvalidTargetBucketForLogging | 400 | The error message returned because the source bucket and the destination bucket do not belong to the same data center. |
| InvalidDigest | 400 | The error message returned because the Content-MD5 value of the message body is inconsistent with the Content-MD5 value of the request header. |
| MalformedXML | 400 | The error message returned because the XML format in the request is invalid. |
| InvalidTargetBucketForLogging | 403 | The error message returned because the requester is not the owner of the destination bucket. |
| AccessDenied | 403 | The error message returned because the requester is not the owner of the source bucket. |


Thank you! We've received your  feedback.