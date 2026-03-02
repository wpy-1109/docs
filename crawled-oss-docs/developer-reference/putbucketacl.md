# PutBucketAcl

You can call this operation to configure or modify the ACL of a bucket.

## Usage notes


When you call the PutBucketAcl operation, take note of the following items:


-

To call this operation, you must have write permissions on the bucket.

-

PutBucketAcl uses the overwriting semantics. A new ACL overwrites the existing one.

-

If the specified bucket for which you want to set ACL does not exist when you call this operation, a new bucket is created.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).


| API | Action | Definition |
| --- | --- | --- |
| PutBucketAcl | oss:PutBucketAcl | Configures or modifies the ACL of a bucket. |


## Request structure


`plaintext
PUT /? acl HTTP/1.1
x-oss-acl: Permission
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers

















-


-


-


| Header | Type | Required | Sample value | Description |
| --- | --- | --- | --- | --- |
| x-oss-acl | String | Yes | private | The ACL that you want to set for the bucket.This header is included in PutBucketAcl requests to set the ACL of the bucket. If this header is not included, the ACL settings do not take effect.Valid values: public-read-write, public-read, and privatepublic-read-write: Any users, including anonymous users can read and write objects in the bucket. Exercise caution when you set the ACL of a bucket to public-read-write.public-read: Only the owner or authorized users of this bucket can write objects in the bucket. Other users, including anonymous users can only read objects in the bucket. Exercise caution when you set the ACL of a bucket to public-read.private: Only the owner or authorized users of this bucket can read and write objects in the bucket. Other users, including anonymous users cannot access the objects in the bucket without authorization. |


For the common request headers included in PutBucketAcl requests, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a PutBucketAcl request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Sample request


`plaintext
PUT /? acl HTTP/1.1
x-oss-acl: public-read
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


-

Sample success response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


-

Sample response to a request that includes invalid ACL settings


`plaintext
HTTP/1.1 400 Bad Request
x-oss-request-id: 56594298207FB3044385
Date: Fri, 24 Feb 2012 03:55:00 GMT
Content-Length: 309
Content-Type: text/xml; charset=UTF-8
Connection: keep-alive
Server: AliyunOSS

<? xml version="1.0" encoding="UTF-8"? >
<Error>
  <Code>InvalidArgument</Code>
  <Message>no such bucket access control exists</Message>
  <RequestId>5*9</RequestId>
  <HostId>*-test.example.com</HostId>
  <ArgumentName>x-oss-acl</ArgumentName>
  <ArgumentValue>error-acl</ArgumentValue>
</Error>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the PutBucketAcl operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-the-acl-of-a-bucket#section-za5-bj6-495)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-bucket-acls)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-acls-2#section-91l-4ge-djo)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-manage-the-acl-of-a-bucket)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-acls-5#section-hqc-qko-onk)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-acls-3#section-rul-ig0-7ge)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-the-acl-of-a-bucket-2#section-u46-dpo-nso)

## ossutil


For information about the ossutil command that corresponds to the PutBucketAcl operation, see [put-bucket-acl](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-access-permissions).

## Error codes











-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | The error message returned because the information for user authentication is not included in the PutBucketAcl request.The error message returned because you are not authorized to initiate a PutBucketAcl request. |


Thank you! We've received your  feedback.