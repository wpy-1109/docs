# DeleteBucketLifecycle

You can call this operation to delete lifecycle rules for a bucket. After you call DeleteBucketLifecycle to delete all lifecycle rules for a bucket, the objects in the bucket are not deleted. Only the bucket owner can delete CORS rules for a bucket.

## Request syntax


`plaintext
DELETE /? lifecycle HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Examples


Sample requests


`plaintext
DELETE /? lifecycle HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: Thu, 17 Apr 2025 01:17:35 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=host,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample success responses


> NOTE:

> NOTE: 


> NOTE: Note 

HTTP status code 204 is returned if there are no lifecycle rules to delete.


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 14 Apr 2014 01:17:35 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 122
`


## OSS SDKs


The SDKs of the DeleteBucketLifecycle operation for various programming languages are as follows:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/lifecycle-1#undefined)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-lifecycle-management)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-lifecycle)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/lifecycle-rules-2#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules-3#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules-1#undefined)

## ossutil


For information about the ossutil command that corresponds to the DeleteBucketLifecycle operation, see [delete-bucket-lifecycle](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-lifecycle).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The error message returned because the specified bucket does not exist. |
| AccessDenied | 403 | The error message returned because you are not authorized to delete the lifecycle rules for the bucket. Only the bucket owner can delete the lifecycle rules for the bucket. |


Thank you! We've received your  feedback.