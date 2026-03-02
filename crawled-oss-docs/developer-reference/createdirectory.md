# CreateDirectory

You can call this operation to create a directory. This operation is applicable only to buckets that have the hierarchical namespace feature enabled.

## Notes


-

To create a directory, you must have the PutObject permission.

-

When you create a directory, OSS returns 200 OK if the directory you want to create has the same name as an existing directory and you have the permissions to access the existing directory. However, OSS does not perform creation operations.

-

When you create a directory, data cannot be imported to the directory. The Content-Length value of the directory can be set only to 0.

-

The Content-Type value of the directory can be set only to application/x-directory, which cannot be modified.

-

When you create a directory, the absolute path of the directory cannot contain consecutive forward slashes (/).

## Syntax


`plaintext
POST /objectName?x-oss-dir HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers














(https://www.ietf.org/rfc/rfc2616.txt)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ddd-signatures-to-urls#concept-xqh-2df-xdb)


| Header | Type | Required | Description |
| --- | --- | --- | --- |
| Authorization | String | No | Specifies that the request is authorized. For more information, see RFC 2616. The Authorization header is required in most cases. However, if you use a signed URL in a request, this header is not required. For more information, see Generate a signed URL. Default value: null |


This API operation must also include common request headers such as Host and Date. For more information about common request headers, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response headers involved in this API operation contain only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Sample requests


`plaintext
POST /desktop/oss?x-oss-dir HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 29 Apr 2021 05:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample success responses


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A64485981
Date: Thu, 29 Apr 2021 05:21:12 GMT
Last-Modified: Wed, 24 Feb 2021 06:07:48 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call CreateDirectory operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories#concept-2058101)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories-3)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories-2)

-

[PHP](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories-14)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories-4)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/c-management-directory)

## Error code











-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | Possible causes:When you create a directory, you do not have permissions to access the specified bucket. When you create a directory, the directory you want to create has the same name as an existing directory, but you do not have the permissions to access the existing directory. |
| FileAlreadyExists | 409 | The error message is returned because an existing object at the same directory level has the same name. For example: The desktop directory contains an object named osstest. You cannot create a directory named osstest in the desktop directory. |


Thank you! We've received your  feedback.