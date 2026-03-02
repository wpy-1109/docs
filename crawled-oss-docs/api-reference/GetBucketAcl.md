# GetBucketAcl

You can call this operation to query the access control list (ACL) of a bucket.

Notes

The oss:GetBucketAcl permission is required to query the ACL of a bucket. For more information, see Attach a custom policy to a RAM user.

Request syntax
 
GET /? acl HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response elements

Element

	

Type

	

Description




AccessControlList

	

Container

	

The container that contains the ACL information.

Parent node: AccessControlPolicy.




AccessControlPolicy

	

Container

	

The container that contains the result of the GetBucketACL request.

Parent node: none.




DisplayName

	

String

	

The name of the bucket owner, which is currently the same as the user ID.

Parent node: AccessControlPolicy and Owner.




Grant

	

Enumeration

	

The ACL for the bucket.

Valid values: private, public-read, and public-read-write.

Parent node: AccessControlPolicy and AccessControlList.




ID

	

String

	

The user ID of the bucket owner.

Parent node: AccessControlPolicy and Owner.




Owner

	

Container

	

The container that contains the information about the bucket owner.

Parent node: AccessControlPolicy.

Examples

Sample requests

 
GET /? acl HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 04:11:23 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample success responses

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Fri, 24 Feb 2012 04:11:23 GMT 
Content-Length: 253
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS

<? xml version="1.0" ? >
<AccessControlPolicy>
    <Owner>
        <ID>0022012****</ID>
        <DisplayName>user_example</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>public-read</Grant>
    </AccessControlList>
</AccessControlPolicy>
OSS SDKs

The SDKs of the GetBucketAcl operation for various programming languages are as follows:

Java

Python V2

PHP V2

Go V2

C

.NET

Android

Node.js

Ruby

ossutil

For information about the ossutil command that corresponds to the GetBucketAcl operation, see get-bucket-acl.

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucket

	

404

	

The error message returned because the specified bucket does not exist.




AccessDenied

	

403

	

The error message returned because you are not authorized to query the ACL of the bucket. Only the bucket owner can query the ACL of the bucket.