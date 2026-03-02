# GetBucketPolicyStatus

Checks whether the current bucket policy allows public access.

Note

By default, an Alibaba Cloud account has the permissions to check whether the current bucket policy allows public access. If you want to check whether the current bucket policy allows public access by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the oss:GetBucketPolicyStatus permission.

Request syntax
 
GET /?policyStatus HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a GetBucketPolicyStatus request are common request headers. For more information, see Common request headers.

Response headers

The response to a GetBucketPolicyStatus request contains only common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




PolicyStatus

	

Container

	

N/A

	

The container that stores public access information.

Parent nodes: none

Child nodes: IsPublic




IsPublic

	

Boolean

	

true

	

Indicates whether the current bucket policy allows public access.

true

false

Example

Sample request

 
GET /?policyStatus HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization:  OSS qn6q**************:77Dv****************

Sample success response

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<PolicyStatus>
   <IsPublic>true</IsPublic>
</PolicyStatus>
OSS SDKs

You can use OSS SDKs for the following programming languages to call the GetBucketPolicyStatus operation:

Java

Python V2

Go V2

Node.js

PHP V2

.NET

C++

ossutil

For information about the ossutil command that corresponds to the GetBucketPolicyStatus operation, see get-bucket-policy-status.