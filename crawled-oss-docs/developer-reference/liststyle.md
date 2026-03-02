# Query all image styles of a bucket by calling ListStyle

Queries all image styles of a bucket.

## Usage notes


By default, an Alibaba Cloud account has the permissions to query all image styles of a bucket. To query image styles of a bucket by using a RAM user or Security Token Service (STS), you must have the `oss:ListStyle` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /?style HTTP/1.1
Date:  GMT Date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a ListStyle request are common request headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a ListStyle request are common response headers. For more information about common response headers, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














| Element | Type | Example | Description |
| --- | --- | --- | --- |
| StyleList | Container | N/A | The container that was used to query image styles. Parent nodes: noneChild nodes: Style |
| Style | Container | N/A | The container that was used to query the content of image styles. Parent nodes: StyleListChild nodes: Name, Content, CreateTime, and LastModifyTime |
| Name | String | imagestyle | The name of the image styles. Parent nodes: StyleChild nodes: none |
| Content | String | image/resize,p_50 | The content of the image styles. Parent nodes: StyleChild nodes: none |
| Category | String | image | The categories of the image styles. Parent nodes: StyleChild nodes: none |
| CreateTime | String | Wed, 20 May 2020 12:07:15 GMT | The time when the image styles were created. Parent nodes: StyleChild nodes: none |
| LastModifyTime | String | Wed, 21 May 2020 12:07:15 GMT | The time when the image styles were modified. Parent nodes: StyleChild nodes: none |


## Examples


-

Sample request


`plaintext
GET /?style HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Content-Length: 63
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample success response


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 04:43:37 GMT
Content-Type: application/xml
Content-Length: 695
Connection: keep-alive
x-oss-request-id: 622198F90612433336EC66A6

<?xml version="1.0" encoding="UTF-8"?>
<StyleList>
 <Style>
 <Name>imagestyle</Name>
 <Content>image/resize,p_50</Content>
 <Category>image</Category>
 <CreateTime>Wed, 20 May 2020 12:07:15 GMT</CreateTime>
 <LastModifyTime>Wed, 21 May 2020 12:07:15 GMT</LastModifyTime>
 </Style>
 <Style>
 <Name>imagestyle1</Name>
 <Content>image/resize,w_200</Content>
 <Category>image</Category>
 <CreateTime>Wed, 20 May 2020 12:08:04 GMT</CreateTime>
 <LastModifyTime>Wed, 21 May 2020 12:08:04 GMT</LastModifyTime>
 </Style>
 <Style>
 <Name>imagestyle2</Name>
 <Content>image/resize,w_300</Content>
 <Category>image</Category>
 <CreateTime>Fri, 12 Mar 2021 06:19:13 GMT</CreateTime>
 <LastModifyTime>Fri, 13 Mar 2021 06:27:21 GMT</LastModifyTime>
 </Style>
</StyleList>
`


## OSS SDK


You can use OSS SDK for [Python](https://www.alibabacloud.com/help/en/oss/developer-reference/python-sdk-image-styles) to call the ListStyle operation.

## ossutil


For information about the ossutil command that corresponds to the ListStyle operation, see [list-style](https://www.alibabacloud.com/help/en/oss/developer-reference/list-style).

Thank you! We've received your  feedback.