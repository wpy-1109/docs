# obtain the access policy of a bucket by calling the GetBucketPolicy operation

GetBucketPolicy retrieves the access policy of a specified bucket or vector bucket.

## Request syntax


`plaintext
GET /?policy
Host: Host
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Bucket example


-

Request example


`plaintext
GET /?policy
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 09:09:13 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Response example


`plaintext
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
`


Vector bucket example
The region in the Host of a vector bucket is specified by a standard Alibaba Cloud region ID, such as cn-hangzhou, not a legacy OSS region ID, such as oss-cn-hangzhou, which is used for general-purpose buckets.

-

Request example


`plaintext
GET /?policy
Host: exampebucket-123*456.cn-hangzhou.oss-vectors.aliyuncs.com
Date: Thu, 17 Apr 2025 09:09:13 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Response example


`plaintext
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
`


## SDK


The following SDKs are available for this API:


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


For the ossutil command that corresponds to the GetBucketPolicy operation, see [get-bucket-policy](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-policy).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucketPolicy | 404 | No policy is configured for the requested bucket. |


Thank you! We've received your  feedback.