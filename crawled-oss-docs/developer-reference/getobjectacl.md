# call GetObjectACL to obtain access privileges of a file

Queries the access control list (ACL) of an object in a bucket.

## Versioning


By default, when you call the GetObjectACL operation to query the ACL of an object, only the ACL of the current version of the object is returned. You can specify the versionId parameter in the request to query the ACL of a specified version of an object. If the specified version is a delete marker, Object Storage Service (OSS) returns 404 Not Found.


> NOTE:

> NOTE: 


> NOTE: Note 

If you call the GetObjectACL operation to query the ACL of an object for which no ACL is configured, OSS returns the default ACL of this object. In this case, the ACL of this object is the same as the ACL of the bucket in which the object is stored. For example, if the ACL of the bucket in which the object is stored is private, the ACL of the object is also private.


## Syntax


`plaintext
GET /ObjectName?acl HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a GetObjectACL request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a GetObjectACL request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














-


-


-


-


| Element | Type | Sample Value | Description |
| --- | --- | --- | --- |
| AccessControlList | Container | N/A | The container that stores the ACL information. Parent nodes: AccessControlPolicy |
| AccessControlPolicy | Container | N/A | The container that stores the results of the GetObjectACL request. Parent nodes: none |
| DisplayName | String | 0022012 | The name of the bucket owner, which is the same as the user ID. Parent nodes: AccessControlPolicy.Owner |
| Grant | Enumerated string | private | The ACL of the object. Default value: default. Valid values:default: The ACL of the object is the same as the ACL of the bucket in which the object is stored.private: The ACL of the object is private.public-read: The ACL of the object is public read.public-read-write: The ACL of the object is public read/write.Parent nodes: AccessControlPolicy.AccessControlList |
| ID | String | 0022012 | The user ID of the bucket owner. Parent nodes: AccessControlPolicy.Owner |
| Owner | Container | N/A | The container that stores the information about the bucket owner. Parent nodes: AccessControlPolicy |


## Examples


-

Query the ACL of an object in an unversioned bucket


Sample requests


`plaintext
GET /test-object?acl HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 29 Apr 2015 05:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample responses


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A64485981
Date: Wed, 29 Apr 2015 05:21:12 GMT
Content-Length: 253
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" ?>
<AccessControlPolicy>
    <Owner>
        <ID>0022012</ID>
        <DisplayName>0022012</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>public-read </Grant>
    </AccessControlList>
</AccessControlPolicy>
`


-

Query the ACL of an object in a versioned bucket


Sample requests


`plaintext
GET /example?acl&versionId=CAEQMhiBgMC1qpSD0BYiIGQ0ZmI5ZDEyYWVkNTQwMjBiNTliY2NjNmY3ZTVk HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:30:10 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample responses


`plaintext
HTTP/1.1 200 OK
x-oss-version-id: CAEQMhiBgMC1qpSD0BYiIGQ0ZmI5ZDEyYWVkNTQwMjBiNTliY2NjNmY3ZTVk
x-oss-request-id: 5CAC3BF2B7AEADE017000621
Date: Tue, 09 Apr 2019 06:30:10 GMT
Content-Length: 261
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy>
  <Owner>
    <ID>1234513715092</ID>
    <DisplayName>1234513715092</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>public-read</Grant>
  </AccessControlList>
</AccessControlPolicy>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the GetObjectACL operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-acls-2#undefined)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-object-acls)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-the-acl-of-an-object-2#section-kj0-97g-p10)

-

[Harmony](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-acl-using-harmony-sdk)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-file-access)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-acls-3#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-acls-13#undefined)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-acls-9)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-acls-11#undefined)

## ossutil


For information about the ossutil command that corresponds to the GetObjectACL operation, see [get-object-acl](https://www.alibabacloud.com/help/en/oss/developer-reference/get-object-acl).

## Error codes














| Error code | HTTP status code | Error message | Description |
| --- | --- | --- | --- |
| AccessDenied | 403 | You do not have read acl permission on this object. | The error message returned because you are not authorized to perform the GetObjectACL operation. Only the bucket owner has permissions to call the GetObjectACL operation to query the ACL of an object in the bucket. |
| FileAlreadyExists | 409 | The object you specified already exists and is a directory. | The error message returned because the object whose ACL you want to query is a directory in a bucket for which the hierarchical namespace feature is enabled. |


Thank you! We've received your  feedback.