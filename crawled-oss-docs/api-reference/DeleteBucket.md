# DeleteBucket

Call DeleteBucket to delete a bucket.

Important

Only the bucket owner has permission to delete the bucket.

To prevent accidental deletion, Object Storage Service (OSS) does not allow you to delete a non-empty bucket.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM Policy or Bucket Policy.

API

	

Action

	

Description




DeleteBucket

	

oss:DeleteBucket

	

Deletes a bucket.

Request syntax
 
DELETE / HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples

Sample request for deleting an empty bucket

 
DELETE / HTTP/1.1
Host: test.oss-cn-hangzhou.aliyuncs.com
Accept-Encoding: identity
User-Agent: aliyun-sdk-python/2.6.0(Windows/7/AMD64;3.7.0)
Accept: */*
Connection: keep-alive
date: Tue, 15 Jan 2019 08:19:04 GMT
authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Content-Length: 0

Sample response

 
HTTP/1.1 204 No Content
Server: AliyunOSS
Date: Tue, 15 Jan 2019 08:19:04 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5C3D9778CC1C2AEDF85B****
x-oss-server-time: 190

Sample request for deleting a bucket that does not exist

 
DELETE / HTTP/1.1
Host: test.oss-cn-hangzhou.aliyuncs.com
Accept-Encoding: identity
User-Agent: aliyun-sdk-python/2.6.0(Windows/7/AMD64;3.7.0)
Accept: */*
Connection: keep-alive
date: Tue, 15 Jan 2019 07:53:24 GMT
authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Content-Length: 0

Sample response

 
HTTP/1.1 404 Not Found
Server: AliyunOSS
Date: Tue, 15 Jan 2019 07:53:25 GMT
Content-Type: application/xml
Content-Length: 288
Connection: keep-alive
x-oss-request-id: 5C3D9175B6FC201293AD****

<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>NoSuchBucket</Code>
  <Message>The specified bucket does not exist.</Message>
  <RequestId>5C3D9175B6FC201293AD****</RequestId>
  <HostId>test.oss-cn-hangzhou.aliyuncs.com</HostId>
  <BucketName>test</BucketName>
  <EC>0015-00000101</EC>
</Error>

Sample request for deleting a non-empty bucket

 
DELETE / HTTP/1.1
Host: test.oss-cn-hangzhou.aliyuncs.com
Accept-Encoding: identity
User-Agent: aliyun-sdk-python/2.6.0(Windows/7/AMD64;3.7.0)
Accept: */*
Connection: keep-alive
date: Thu, 17 Apr 2025 07:35:06 GMT
authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Content-Length: 0

Sample response

 
HTTP/1.1 409 Conflict
Server: AliyunOSS
Date: Tue, 15 Jan 2019 07:35:06 GMT
Content-Type: application/xml
Content-Length: 296
Connection: keep-alive
x-oss-request-id: 5C3D8D2A0ACA54D87B43****
x-oss-server-time: 16

<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>BucketNotEmpty</Code>
  <Message>The bucket has objects. Please delete them first.</Message>
  <RequestId>5C3D8D2A0ACA54D87B43****</RequestId>
  <HostId>test.oss-cn-hangzhou.aliyuncs.com</HostId>
  <BucketName>test</BucketName>
  <EC>0015-00000301</EC>
</Error>
SDK

You can use OSS SDKs for the following programming languages to call the DeleteBucket operation:

Java

Python V2

PHP V2

Go V2

C

C++

.NET

Android

iOS

Node.js

Ruby

Command-line tool ossutil

For the ossutil command that corresponds to the DeleteBucket operation, see delete-bucket.

Error codes

Error code

	

HTTP status code

	

Description




AccessDenied

	

403 Forbidden

	

The error message returned because you do not have the permissions to delete the bucket. Only the bucket owner can delete the bucket.