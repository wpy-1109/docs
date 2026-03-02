# DeleteBucketEncryption

You can call this operation to delete encryption rules configured for a bucket.

## Notes


The `oss:DeleteBucketEncryption` permission is required for deleting encryption rules configured for a bucket by calling DeleteBucketEncryption. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).


> NOTE:

> NOTE: 


> NOTE: Note 

Only the bucket owner or authorized RAM users can delete encryption rules configured for a bucket. Otherwise, OSS returns the 403 error. For more information about bucket encryption, see [Server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db).


## Request syntax


`plaintext
DELETE /? encryption HTTP/1.1
Date: GMT Date
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`plaintext
DELETE /? encryption HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 20 Dec 2018 11:35:24 GMT
Authorization: OSS qn6q:77Dv
`


-

Sample response


`plaintext
HTTP/1.1 204 OK
x-oss-request-id: 5C22E0EFD127F6810B1A
Date: Tue, 20 Dec 2018 11:37:05 GMT
Connection: keep-alive
Content-Length: 0
`


## OSS SDKs


You can use the following SDKs for various programming languages to call DeleteBucketEncryption:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-6#concept-266387)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-5#concept-265074)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-server-side-encryption)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-1#concept-2311158)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-4#concept-2482290)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-7#concept-2382981)

## ossutil


For information about the ossutil command that corresponds to the DeleteBucketEncryption operation, see [delete-bucket-encryption](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-encryption).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | The error message returned because you do not have permissions to delete encryption rules configured for the bucket. |
| NoSuchBucket | 404 | The error message returned because the bucket of which encryption rules that you want to delete does not exist. |


Thank you! We've received your  feedback.