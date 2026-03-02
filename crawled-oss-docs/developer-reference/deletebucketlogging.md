# Disable access logging for a bucket by calling DeleteBucketLogging

Call the DeleteBucketLogging operation to disable the access logging feature for a bucket. Only the bucket owner can call this operation.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).











| API | Action | Definition |
| --- | --- | --- |
| DeleteBucketLogging | oss:DeleteBucketLogging | Disables logging for a bucket. |


## Request syntax


`plaintext
DELETE /?logging HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Example for a general-purpose bucket


Sample request


`plaintext
DELETE /?logging HTTP/1.1
Host: Host
Date: Thu, 17 Apr 2025 05:35:24 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


> NOTE:

> NOTE: 


> NOTE: Note 

If access logging is disabled for the target bucket, a 204 status code is returned.


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 05:35:24 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 198
`


Example for a vector bucket
For a vector bucket, the region parameter in the Host header uses a standard Alibaba Cloud region ID, such as cn-hangzhou, instead of a legacy OSS region ID used for general-purpose buckets, such as oss-cn-hangzhou.

Sample request


`plaintext
DELETE /?logging HTTP/1.1
Host: exampebucket-123*456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 05:35:24 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


> NOTE:

> NOTE: 


> NOTE: Note 

If access logging is disabled for the target bucket, a 204 status code is returned.


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 05:35:24 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 198
`


## SDK


Use the following software development kits (SDKs) to call this operation:


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


For information about the ossutil command that corresponds to the DeleteBucketLogging operation, see [delete-bucket-logging](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-logging).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The specified bucket does not exist. |
| AccessDenied | 403 | You do not have the permission to disable the access logging feature for the bucket. Only the bucket owner can disable the access logging feature for the bucket. |


Thank you! We've received your  feedback.