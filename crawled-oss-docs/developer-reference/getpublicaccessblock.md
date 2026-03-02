# Call the GetPublicAccessBlock operation to query the Block Public Access configurations of OSS resources

Queries the Block Public Access configurations of Object Storage Service (OSS) resources.

## Usage notes


By default, an Alibaba Cloud account has the permissions to query the Block Public Access configurations of OSS resources. If you want to query the Block Public Access configurations of OSS resources by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:GetPublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`http
GET /?publicAccessBlock HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a GetPublicAccessBlock request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a GetPublicAccessBlock request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| PublicAccessBlockConfiguration | Container | N/A | The container in which the Block Public Access configurations are stored. Parent nodes: noneChild nodes: BlockPublicAccess |
| BlockPublicAccess | Boolean | true | Indicates whether Block Public Access is enabled for OSS resources. true: Block Public Access is enabled. false: Block Public Access is disabled. |


## Examples


-

Sample request


`http
GET /?publicAccessBlock HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q:77Dv
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


## OSS SDK


You can use OSS SDK for [Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/oss-global-block-public-access-using-oss-sdk-for-go-v2) to call the GetPublicAccessBlock operation.

## ossutil


For information about the ossutil command that corresponds to the GetPublicAccessBlock operation, see [get-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/get-public-access-block).

Thank you! We've received your  feedback.