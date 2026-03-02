# Manage Block Public Access for an access point

Enables Block Public Access for an access point.

Usage notes

By default, an Alibaba Cloud account has the permissions to enable Block Public Access for an access point. If you want to enable Block Public Access for an access point by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the oss:PutAccessPointPublicAccessBlock permission. For more information, see Common examples of RAM policies.

If you enable Block Public Access, existing public access permissions are ignored and you cannot configure public access permissions. If you disable Block Public Access, existing public access permissions take effect and you can configure public access permissions.

Request syntax
 
PUT /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>
Request headers

All headers in a PutAccessPointPublicAccessBlock request are common request headers. For more information, see Common request headers.

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




PublicAccessBlockConfiguration

	

Container

	

Yes

	

N/A

	

The container in which the Block Public Access configurations are stored.

Parent nodes: none

Child nodes: BlockPublicAccess




BlockPublicAccess

	

Boolean

	

No

	

true

	

Specifies whether to enable Block Public Access for the access point.

true: enables Block Public Access.

false (default): disables Block Public Access.

Response headers

The response to a PutAccessPointPublicAccessBlock request contains only common response headers. For more information, see Common response headers.

Examples

Sample request

 
PUT /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 148
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q**************:77Dv****************

<?xml version="1.0" encoding="UTF-8"?>
<PublicAccessBlockConfiguration>
  <BlockPublicAccess>true</BlockPublicAccess>
</PublicAccessBlockConfiguration>

Sample success response

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS
OSS SDK

You can use OSS SDK for Go V2 to call the PutAccessPointPublicAccessBlock operation.