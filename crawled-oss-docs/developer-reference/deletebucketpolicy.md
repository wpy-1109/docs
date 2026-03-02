# delete a bucket access policy by using DeleteBucketPolicy

The DeleteBucketPolicy operation deletes the access policy for a specified bucket or Vector bucket.

## Request syntax


`plaintext
DELETE /?policy
Host: Host
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Bucket example


-

Sample request


`plaintext
DELETE /?policy
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 12:55:10 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`plaintext
HTTP/1.1 204 No Content
content-length: 0
server: AliyunOSS
x-oss-server-time: 31
connection: keep-alive
x-oss-request-id: 5C6E9FAF31A13327124B
date: Thu, 21 Feb 2019 12:55:11 GMT
`


Vector bucket example
For Vector buckets, the Host header must contain a standard Alibaba Cloud region ID, such as cn-hangzhou. Do not use a legacy OSS region ID, such as oss-cn-hangzhou, which is used for standard buckets.

-

Sample request


`plaintext
DELETE /?policy
Host: exampebucket-123*456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 12:55:10 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`plaintext
HTTP/1.1 204 No Content
content-length: 0
server: AliyunOSS
x-oss-server-time: 31
connection: keep-alive
x-oss-request-id: 5C6E9FAF31A13327124B
date: Thu, 21 Feb 2019 12:55:11 GMT
`


## SDK


SDKs for this API are available in the following languages:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-and-manage-bucket-policies)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-bucket-policies)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-policies)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-configure-and-manage-bucket-policies)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-1)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policies-2)

## ossutil command-line interface


For information about the ossutil command that corresponds to the DeleteBucketPolicy operation, see [delete-bucket-policy](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-policy).

Thank you! We've received your  feedback.