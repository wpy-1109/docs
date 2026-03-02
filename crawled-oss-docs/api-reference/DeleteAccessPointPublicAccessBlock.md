# Manage Block Public Access for an access point

Deletes the Block Public Access configurations of an access point.

Usage notes

By default, an Alibaba Cloud account has the permissions to delete the Block Public Access configurations of an access point. If you want to delete the Block Public Access configurations of an access point by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the oss:DeleteAccessPointPublicAccessBlock permission. For more information, see Common examples of RAM policies.

Request syntax
 
DELETE /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a DeleteAccessPointPublicAccessBlock request are common request headers. For more information, see Common request headers.

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

The response to a DeleteAccessPointPublicAccessBlock request contains only common response headers. For more information, see Common response headers.

Examples

Sample request

 
DELETE /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q**************:77Dv****************

Sample success response

 
HTTP/1.1 204 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS
OSS SDK

You can use OSS SDK for Go V2 to call the DeleteAccessPointPublicAccessBlock operation.

ossutil

For information about the ossutil command that corresponds to the DeleteAccessPointPublicAccessBlock operation, see delete-access-point-public-access-block.