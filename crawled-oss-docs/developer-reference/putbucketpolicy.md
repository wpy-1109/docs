# what is the putbucketpolicy operation

You can call the PutBucketPolicy operation to set an authorization policy for a specified bucket or vector bucket.

## Permissions


An Alibaba Cloud account has all permissions by default. In contrast, a Resource Access Management (RAM) user or RAM role has no permissions by default. An Alibaba Cloud account or an administrator must grant permissions to the RAM user or RAM role using a [RAM policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or a [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).











| API | Action | Description |
| --- | --- | --- |
| PutBucketPolicy | oss:PutBucketPolicy | Sets the authorization policy for the specified bucket. |


## Request syntax


`plaintext
PUT /?policy
Host: Host
Date: GMT Date
Authorization: SignatureValue
Policy written in JSON
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Bucket example


-

Request sample


`plaintext
PUT /?policy
Content-Length: 230
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 12:51:09 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
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
`


-

Response sample


`plaintext
HTTP/1.1 200 OK
content-length: 0
server: AliyunOSS
x-oss-server-time: 87
connection: keep-alive
x-oss-request-id: 5C6E9EBD5CC26B28EE41
date: Thu, 21 Feb 2019 12:51:09 GMT
`


Vector bucket example
For a vector bucket, the region parameter in the Host uses a standard Alibaba Cloud region ID, such as cn-hangzhou, instead of a legacy OSS region, such as oss-cn-hangzhou, which is used for general-purpose buckets.

-

Request sample


`plaintext
PUT /?policy
Content-Length: 230
Host: exampebucket-123*456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 12:51:09 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
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
`


-

Response sample


`plaintext
HTTP/1.1 200 OK
content-length: 0
server: AliyunOSS
x-oss-server-time: 87
connection: keep-alive
x-oss-request-id: 5C6E9EBD5CC26B28EE41
date: Thu, 21 Feb 2019 12:51:09 GMT
`


## SDK


You can call this operation using the SDKs for the following programming languages:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-and-manage-bucket-policies)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-bucket-policies)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-policies)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-configure-and-manage-bucket-policies)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-1)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policies-2)

## ossutil command-line tool


For information about the corresponding ossutil command, see [put-bucket-policy](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-policy).

Thank you! We've received your  feedback.