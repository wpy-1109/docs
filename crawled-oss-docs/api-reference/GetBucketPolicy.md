# GetBucketPolicy

GetBucketPolicy retrieves the access policy of a specified bucket or vector bucket.

Request syntax
 
GET /?policy
Host: Host
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples

Bucket example

Request example

 
GET /?policy
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 09:09:13 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Response example

 
HTTP/1.1 200 OK
server: AliyunOSS
x-oss-server-time: 24
connection: keep-alive
x-oss-request-id: 5C6E9847BE0EBCD13DA90C11
date: Thu, 21 Feb 2019 12:23:35 GMT
content-type: application/json
{
  "Version":"1",
  "Statement":[
    {
      "Action":[
        "oss:PutObject",
        "oss:GetObject"
      ],
      "Effect":"Deny",
      "Principal":["1234567890"],
      "Resource":["acs:oss:*:1234567890:*/*"]
    }
  ]
}

Vector bucket example

The region in the Host of a vector bucket is specified by a standard Alibaba Cloud region ID, such as cn-hangzhou, not a legacy OSS region ID, such as oss-cn-hangzhou, which is used for general-purpose buckets.

Request example

 
GET /?policy
Host: exampebucket-123***456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 09:09:13 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Response example

 
HTTP/1.1 200 OK
server: AliyunOSS
x-oss-server-time: 24
connection: keep-alive
x-oss-request-id: 5C6E9847BE0EBCD13DA90C11
date: Thu, 21 Feb 2019 12:23:35 GMT
content-type: application/json
{
   "Version":"1",
   "Statement":[
   {
     "Action":[
       "oss:PutVectors",
       "oss:GetVectors"
    ],
    "Effect":"Deny",
    "Principal":["1234567890"],
    "Resource":["acs:ossvector:cn-hangzhou:1234567890:bucket/vector-example/*"]
   }
  ]
}
SDK

The following SDKs are available for this API:

Java

Python V2

Go V2

Node.js

PHP V2

.NET

C++

ossutil command-line tool

For the ossutil command that corresponds to the GetBucketPolicy operation, see get-bucket-policy.

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucketPolicy

	

404

	

No policy is configured for the requested bucket.