# Call the DeleteBucketPublicAccessBlock operation to delete the Block Public Access configurations of a bucket

Deletes the Block Public Access configurations of a bucket.

## Usage notes


By default, an Alibaba Cloud account has the permissions to delete the Block Public Access configurations of a bucket. If you want to delete the Block Public Access configurations of a bucket by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:DeleteBucketPublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`http
DELETE /?publicAccessBlock HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a DeleteBucketPublicAccessBlock request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a DeleteBucketPublicAccessBlock request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`http
DELETE /?publicAccessBlock HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample success response


`http
HTTP/1.1 204 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call DeleteBucketPublicAccessBlock:


-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/blocking-public-access-at-the-bucket-level-using-oss-sdk-for-go-v2)

## ossutil


For information about the ossutil command that corresponds to the DeleteBucketPublicAccessBlock operation, see [delete-bucket-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-public-access-block).

Thank you! We've received your  feedback.