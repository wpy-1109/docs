# GetStyle

Queries information about a specific image style configured for a bucket.

Usage notes

By default, an Alibaba Cloud account has the permission to query a specific image style of a bucket. If you want to query an image style as a RAM user or by using Security Token Service (STS), you must grant the RAM user the oss:GetStyle permission. For more information, see Common examples of RAM policies.

Request syntax
Note

To query a specific image style configured for a bucket, you need to specify the name of the style by using the styleName parameter, as in GET /?style&styleName=imagestyle HTTP/1.1.

 
GET /?style&styleName=styleName HTTP/1.1
Date:  GMT Date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a GetStyle request are common request headers. For more information, see Common HTTP headers.

Response headers

All headers in the response to a GetStyle request are common response headers. For more information, see Common HTTP headers.

Response elements

Element

	

Type

	

Example

	

Description




Style

	

Container

	

N/A

	

The container that stores information about the style.

Parent nodes: none

Child nodes: Name, Content, CreateTime, and LastModifyTime




Name

	

String

	

imagestyle

	

The name of the image style.

Parent nodes: Style

Child nodes: none




Content

	

String

	

image/resize,p_50

	

The content of the image style.

Parent nodes: Style

Child nodes: none




Category

	

String

	

image

	

The category of the style.

Parent nodes: Style

Child nodes: none




CreateTime

	

String

	

Wed, 20 May 2020 12:07:15 GMT

	

The time when the style was created.

Parent nodes: Style

Child nodes: none




LastModifyTime

	

String

	

Wed, 21 May 2020 12:07:15 GMT

	

The time when the image style was modified.

Parent nodes: Style

Child nodes: none

Examples

Sample requests

 
GET /?style&styleName=imagestyle HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Content-Length: 63
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample responses

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:28:35 GMT
Content-Type: application/xml
Content-Length: 239
Connection: keep-alive
x-oss-request-id: 6221A383CBD8483439E7****
<?xml version="1.0" encoding="UTF-8"?>
<Style>
 <Name>imagestyle</Name>
 <Content>image/resize,p_50</Content>
 <Category>image</Category>
 <CreateTime>Wed, 20 May 2020 12:07:15 GMT</CreateTime>
 <LastModifyTime>Wed, 21 May 2020 12:07:15 GMT</LastModifyTime>
</Style>
OSS SDK

You can use OSS SDK for Python to call the GetStyle operation.

ossutil

For information about the ossutil command that corresponds to the GetStyle operation, see get-style.