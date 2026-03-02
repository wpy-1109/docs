# Call the PutPublicAccessBlock operation to globally enable Block Public Access for OSS

This operation globally enables Block Public Access for all resources in Object Storage Service (OSS).

## Usage notes


-

By default, an Alibaba Cloud account has the permissions to globally enable Block Public Access for OSS resources. If you use a Resource Access Management (RAM) user or access credentials provided by Security Token Service (STS) to perform this operation, you must have the `oss:PutPublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

If you enable Block Public Access, existing public access permissions are ignored, and new public access permissions cannot be created. If you disable Block Public Access, existing public access permissions remain in effect, and you can create new public access permissions.

## Request syntax


`http
PUT /?publicAccessBlock HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
`


## Request headers


This operation uses only common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


-


-


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| PublicAccessBlockConfiguration | Container | Yes | N/A | The container that stores the Block Public Access information.Parent node: NoneChild node: BlockPublicAccess |
| BlockPublicAccess | Boolean | No | true | Specifies whether to enable Block Public Access.true: Enables Block Public Access.false (default): Disables Block Public Access. |


## Response headers


The response to this operation includes only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`http
PUT /?publicAccessBlock HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 148
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS
`


## SDK


The SDKs for this operation are as follows:


-

Python V2

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/oss-global-block-public-access-using-oss-sdk-for-go-v2)

-

PHP V2

## ossutil command-line tool


For information about the ossutil command that corresponds to this operation, see [put-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/put-public-access-block).


Thank you! We've received your  feedback.