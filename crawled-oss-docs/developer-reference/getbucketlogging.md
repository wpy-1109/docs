# view the access log configuration of a bucket by calling GetBucketLogging

You can call the GetBucketLogging operation to view the access log configuration of a bucket. Only the bucket owner can perform this operation.

## Usage notes


To call the GetBucketLogging operation, you must have the `oss:GetBucketLogging` permission. For more information, see [Grant custom access policies to RAM users](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /?logging HTTP/1.1
Host: Host
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














> NOTE:

> NOTE: 


> NOTE: 


| Name | Type | Example | Description |
| --- | --- | --- | --- |
| BucketLoggingStatus | Container | Not applicable | A container for the access log status.Child element: LoggingEnabledParent element: NoneNote If no logging rule is set for the source bucket, OSS still returns an XML message body, but the BucketLoggingStatus element is empty. |
| LoggingEnabled | Container | Not applicable | A container for access log information. This element is returned when logging is enabled and is not returned when logging is disabled.Child elements: TargetBucket, TargetPrefix, and LoggingRoleParent element: BucketLoggingStatus |
| TargetBucket | String | mybucketlogs | The bucket where access logs are stored.Child element: NoneParent element: BucketLoggingStatus.LoggingEnabled |
| TargetPrefix | String | mybucket-access_log/ | The prefix of the access log files that are saved.Child element: NoneParent element: BucketLoggingStatus.LoggingEnabled |
| LoggingRole | String | AliyunOSSLoggingDefaultRole | The role for log storage authorization.Child element: NoneParent element: BucketLoggingStatus.LoggingEnabled |


## Examples


Example for a bucket


Request example


`plaintext
Get /?logging HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 05:31:04 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


-

Sample response for setting a log rule


`plaintext
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 04 May 2012 05:31:04 GMT
Connection: keep-alive
Content-Length: 280
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
    <LoggingEnabled>
        <TargetBucket>mybucketlogs</TargetBucket>
        <TargetPrefix>mybucket-access_log/</TargetPrefix>
        <LoggingRole>AliyunOSSLoggingDefaultRole</LoggingRole>
    </LoggingEnabled>
</BucketLoggingStatus>
`


-

Response for a bucket without a logging rule


`plaintext
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 04 May 2012 05:31:04 GMT
Connection: keep-alive
Content-Length: 110
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
</BucketLoggingStatus>
`


Example for a vector bucket
The region parameter in the Host header for a vector bucket uses a standard Alibaba Cloud region ID, such as cn-hangzhou, instead of a legacy OSS region ID used for general-purpose buckets, such as oss-cn-hangzhou.

Request example


`plaintext
Get /?logging HTTP/1.1
Host: exampebucket-123*456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 05:31:04 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 04 May 2012 05:31:04 GMT
Connection: keep-alive
Content-Length: 280
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus>
    <LoggingEnabled>
        <TargetBucket>mybucketlogs</TargetBucket>
        <TargetPrefix>mybucket-access_log/</TargetPrefix>
        <LoggingRole>AliyunOSSLoggingDefaultRole</LoggingRole>
    </LoggingEnabled>
</BucketLoggingStatus>
`


## SDK


This operation is supported by the following SDKs:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-1#concept-32019-zh)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-logging-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-logging-2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-logging-5)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-12#concept-89684-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-2#concept-48308-zh)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-8#concept-32080-zh)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-6#concept-32125-zh)

## ossutil command-line tool


For the ossutil command that corresponds to the GetBucketLogging operation, see [get-bucket-logging](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-logging).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The specified bucket does not exist. |
| AccessDenied | 403 | You do not have the permission to view the access log configuration of the bucket. This permission is granted only to the bucket owner. |


Thank you! We've received your  feedback.