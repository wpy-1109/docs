# Call the PutBucketPublicAccessBlock operation to enable Block Public Access for a bucket

Enables Block Public Access for a bucket.

## Usage notes


-

By default, an Alibaba Cloud account has the permissions to enable Block Public Access for a bucket. If you want to enable Block Public Access for a bucket by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:PutBucketPublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

If you enable Block Public Access, existing public access permissions are ignored and you cannot configure public access permissions. If you disable Block Public Access, existing public access permissions take effect and you can configure public access permissions.

## Request syntax


`http
PUT /?publicAccessBlock HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
`


## Request headers


All headers in a PutBucketPublicAccessBlock request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


-


-


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| PublicAccessBlockConfiguration | Container | Yes | N/A | The container in which the Block Public Access configurations are stored. Parent nodes: noneChild nodes: BlockPublicAccess |
| BlockPublicAccess | Boolean | No | true | Specifies whether to enable Block Public Access for the bucket. true: enables Block Public Access. false (default): disables Block Public Access. |


## Examples


-

Sample request


`http
PUT /?publicAccessBlock HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 148
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q:77Dv

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
`


-

Sample success response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS
`


## OSS SDK


You can use OSS SDK for [Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/blocking-public-access-at-the-bucket-level-using-oss-sdk-for-go-v2) to call the PutBucketPublicAccessBlock operation.

## ossutil


For information about the ossutil command that corresponds to the PutBucketPublicAccessBlock operation, see [put-bucket-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-public-access-block).

Thank you! We've received your  feedback.