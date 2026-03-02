# PutStyle

Creates an image style. You can include one or multiple Image Processing (IMG) parameters in an image style.

Usage notes

By default, an Alibaba Cloud account has the permissions to create image styles. If you want to create an image style as a RAM user or by using Security Token Service (STS), you must grant the RAM user the oss:PutStyle permission. For more information, see Common examples of RAM policies.

Request syntax
Note

When you create an image style, you must use the styleName parameter to specify the image style name. Sample code: PUT /?style&styleName=imagestyle HTTP/1.1.

 
PUT /?style&styleName=styleName HTTP/1.1
Date:  GMT Date
Content-Length: ContentLength
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a PutStyle request are common request headers. For more information about common request headers, see Common HTTP headers.

Request parameters

Parameter

	

Type

	

Required

	

Example

	

Description




Style

	

Container

	

Yes

	

N/A

	

The container that stores the image style content.

Parent nodes: none

Child nodes: Content




Content

	

String

	

Yes

	

image/resize,p_50

	

The content of the image style. You can include one or multiple IMG parameters in an image style.

You can include one IMG parameter in an image style. For example, you can use image/resize,p_50 to resize the image by 50%.

You can include multiple IMG parameters in an image style. For example, you can use image/resize,p_63/quality,q_90 to resize the image by 63% and then set the relative quality of the image to 90%.

Parent nodes: Style

Child nodes: none

Response headers

All headers in the response to a PutStyle request are common response headers. For more information about common response headers, see Common HTTP headers.

Examples

Sample requests

 
PUT /?style&styleName=imagestyle HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Content-Length: 63
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<Style>
 <Content>image/resize,p_50</Content>
</Style>

Sample success responses

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:34:24 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 534B371674E88A4D8906****
SDK

You can use OSS SDKs for the following programming languages to call PutStyle operation:

Python

ossutil

For information about the ossutil command that corresponds to the PutStyle operation, see put-style.