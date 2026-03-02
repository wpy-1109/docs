# DeleteBucketPolicy

The DeleteBucketPolicy operation deletes the access policy for a specified bucket or Vector bucket.

Request syntax
 
DELETE /?policy
Host: Host
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples

Bucket example

Sample request

 
DELETE /?policy
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 12:55:10 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204 No Content
content-length: 0
server: AliyunOSS
x-oss-server-time: 31
connection: keep-alive
x-oss-request-id: 5C6E9FAF31A13327124B****
date: Thu, 21 Feb 2019 12:55:11 GMT

Vector bucket example

For Vector buckets, the Host header must contain a standard Alibaba Cloud region ID, such as cn-hangzhou. Do not use a legacy OSS region ID, such as oss-cn-hangzhou, which is used for standard buckets.

Sample request

 
DELETE /?policy
Host: exampebucket-123***456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 12:55:10 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204 No Content
content-length: 0
server: AliyunOSS
x-oss-server-time: 31
connection: keep-alive
x-oss-request-id: 5C6E9FAF31A13327124B****
date: Thu, 21 Feb 2019 12:55:11 GMT
SDK

SDKs for this API are available in the following languages:

Java

Python V2

Go V2

Node.js

PHP V2

.NET

C++

ossutil command-line interface

For information about the ossutil command that corresponds to the DeleteBucketPolicy operation, see delete-bucket-policy.