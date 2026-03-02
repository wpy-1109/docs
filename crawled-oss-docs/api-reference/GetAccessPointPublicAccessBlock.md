# Manage Block Public Access for an access point

Queries the Block Public Access configurations of an access point.

Usage notes

By default, an Alibaba Cloud account has the permissions to query the Block Public Access configurations of an access point. If you want to query the Block Public Access configurations of an access point by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the oss:GetAccessPointPublicAccessBlock permission. For more information, see Common examples of RAM policies.

Request syntax
 
GET /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a GetAccessPointPublicAccessBlock request are common request headers. For more information, see Common request headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




x-oss-access-point-name

	

String

	

Yes

	

ap-01

	

The name of the access point.

Response headers

The response to a GetAccessPointPublicAccessBlock request contains only common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




PublicAccessBlockConfiguration

	

Container

	

N/A

	

The container in which the Block Public Access configurations are stored.

Parent nodes: none

Child nodes: BlockPublicAccess




BlockPublicAccess

	

Boolean

	

true

	

Indicates whether Block Public Access is enabled for the access point.

true: Block Public Access is enabled.

false: Block Public Access is disabled.

Examples

Sample request

 
GET /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q**************:77Dv****************

Sample success response

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
OSS SDK

You can use OSS SDK for Go V2 to call the GetAccessPointPublicAccessBlock operation.

ossutil

For information about the ossutil command that corresponds to the GetAccessPointPublicAccessBlock operation, see get-access-point-public-access-block.