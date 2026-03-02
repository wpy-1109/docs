# GetBucketAcl

You can call this operation to query the access control list (ACL) of a bucket.

## Notes


The `oss:GetBucketAcl` permission is required to query the ACL of a bucket. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /? acl HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response elements











| Element | Type | Description |
| --- | --- | --- |
| AccessControlList | Container | The container that contains the ACL information.Parent node: AccessControlPolicy. |
| AccessControlPolicy | Container | The container that contains the result of the GetBucketACL request.Parent node: none. |
| DisplayName | String | The name of the bucket owner, which is currently the same as the user ID.Parent node: AccessControlPolicy and Owner. |
| Grant | Enumeration | The ACL for the bucket.Valid values: private, public-read, and public-read-write.Parent node: AccessControlPolicy and AccessControlList. |
| ID | String | The user ID of the bucket owner.Parent node: AccessControlPolicy and Owner. |
| Owner | Container | The container that contains the information about the bucket owner.Parent node: AccessControlPolicy. |


## Examples


Sample requests



`plaintext
GET /? acl HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 04:11:23 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample success responses



`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 04:11:23 GMT
Content-Length: 253
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS

<? xml version="1.0" ? >
<AccessControlPolicy>
    <Owner>
        <ID>0022012</ID>
        <DisplayName>user_example</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>public-read</Grant>
    </AccessControlList>
</AccessControlPolicy>
`


## OSS SDKs


The SDKs of the GetBucketAcl operation for various programming languages are as follows:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-the-acl-of-a-bucket#section-9vy-z0n-kix)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/create-bucket-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-create-bucket)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-create-bucket)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-1#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#undefined)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-4#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-2#undefined)

## ossutil


For information about the ossutil command that corresponds to the GetBucketAcl operation, see [get-bucket-acl](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-acl).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The error message returned because the specified bucket does not exist. |
| AccessDenied | 403 | The error message returned because you are not authorized to query the ACL of the bucket. Only the bucket owner can query the ACL of the bucket. |


Thank you! We've received your  feedback.