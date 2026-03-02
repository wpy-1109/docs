# Call the GetBucketPublicAccessBlock operation to query the Block Public Access configurations of a bucket

Queries the Block Public Access configurations of a bucket.

## Usage notes


By default, an Alibaba Cloud account has the permissions to query the Block Public Access configurations of a bucket. If you want to query the Block Public Access configurations of a bucket by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:GetBucketPublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`http
GET /?publicAccessBlock HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a GetBucketPublicAccessBlock request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a GetBucketPublicAccessBlock request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| PublicAccessBlockConfiguration | Container | N/A | The container in which the Block Public Access configurations are stored. Parent nodes: noneChild nodes: BlockPublicAccess |
| BlockPublicAccess | Boolean | true | Indicates whether Block Public Access is enabled for the bucket. true: Block Public Access is enabled. false: Block Public Access is disabled. |


## Examples


-

Sample request


`http
GET /?publicAccessBlock HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample success response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call GetBucketPublicAccessBlock:


-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/blocking-public-access-at-the-bucket-level-using-oss-sdk-for-go-v2)

## ossutil


For information about the ossutil command that corresponds to the GetBucketPublicAccessBlock operation, see [get-bucket-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-public-access-block).

Thank you! We've received your  feedback.