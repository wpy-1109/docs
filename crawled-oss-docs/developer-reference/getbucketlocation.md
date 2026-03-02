# Call GetBucketLocation to query the location of a bucket

Queries the region of an Object Storage Service (OSS) bucket. Only the bucket owner can query the region of a bucket.

## Request syntax


`plaintext
GET /?location HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














| Element | Type | Example | Description |
| --- | --- | --- | --- |
| LocationConstraint | String | oss-cn-hangzhou | The OSS region ID, which specifies the region in which the bucket is located. |


## Examples


Sample requests


`plaintext
Get /?location HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 05:31:04 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample success responses


`plaintext
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 15 Mar 2013 05:31:04 GMT
Connection: keep-alive
Content-Length: 90
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<LocationConstraint>oss-cn-hangzhou</LocationConstraint >
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call GetBucketLocation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-region-of-a-bucket#concept-2348417)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-region-of-the-bucket-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-query-the-storage-capacity-of-a-bucket)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-region-of-a-bucket-1#concept-2351980)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-query-the-region-of-a-bucket)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-region-of-a-bucket-4#concept-2365064)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-region-of-a-bucket-5#concept-2502722)

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | You do not have the permissions to query the region of the bucket. Only the owner of a bucket can query the region in which the bucket is located. |


Thank you! We've received your  feedback.