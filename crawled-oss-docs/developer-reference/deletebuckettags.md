# DeleteBucketTags

Deletes tags configured for a bucket.

## Notes


The `oss:DeleteBucketTagging` permission is required to deletes tags configured for a bucket by calling the DeleteBucketTags operation. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).


> NOTE:

> NOTE: 


> NOTE: Note 

If no tag is configured for the bucket or the tags that you want to delete do not exist, OSS returns HTTP status code 204.


## Request syntax


`plaintext
DELETE /?tagging HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DeleteBucketTags request are common request headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DeleteBucketTags request are common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request sent to delete all tags of a bucket


`plaintext
DELETE /?tagging HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 25 Dec 2018 17:35:24 GMT
Authorization: OSS qn6q:77Dv
`


Sample response


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 5C22E0EFD127F6810B1A
Date: Tue, 25 Dec 2018 17:35:24 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 293
`


-

Sample request sent to delete tags whose keys are k1 and k2


`plaintext
DELETE /?tagging=k1,k2 HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 25 Dec 2018 17:35:24 GMT
Authorization: OSS qn6q:77Dv
`


Sample response


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 5C22E0EFD127F6810B1A92A8
Date: Tue, 25 Dec 2018 17:35:24 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 293
`


## SDKs


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-tagging-4#section-pc6-9dz-682)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-tagging-3#section-pc6-9dz-682)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-bucket-tagging#undefined)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-bucket-tagging-1#section-5d1-tmc-9fr)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-tagging-2#section-2g4-lka-aqj)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-tagging-1#concept-2482306)

-

[PHP](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-tagging-1#concept-1956276)

## ossutil


For information about the ossutil command that corresponds to the DeleteBucketTags operation, see [delete-bucket-tags](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-tags).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 No Content | The bucket does not exist. |
| AccessDenied | 403 Forbidden | You do not have permissions to delete the tags of the bucket. Only the owner of a bucket can delete the tags of the bucket. |


Thank you! We've received your  feedback.