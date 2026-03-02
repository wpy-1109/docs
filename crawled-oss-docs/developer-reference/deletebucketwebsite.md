# DeleteBucketWebsite

Disables the static website hosting mode and clears the redirection rules for a bucket. Only the owner of a bucket can disable the static website hosting mode for the bucket.

## Note


The `oss:DeleteBucketWebsite` permission is required for disabling the static website hosting mode and clearing the redirection rules for a bucket by calling DeleteBucketWebsite. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Syntax


`plaintext
DELETE /?website HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DeleteBucketWebsite request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DeleteBucketWebsite request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Example


Sample request


`plaintext
DELETE /?website HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 05:45:34 GMT
Authorization: OSS qn6q:77Dv
`


Sample response


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 534B371674E88A4D8906008B
Date: Fri, 24 Feb 2012 05:45:34 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
`


Complete code


`plaintext
DELETE /?website HTTP/1.1
Date: Fri, 27 Jul 2018 09:10:52 GMT
Host: test.oss-cn-hangzhou-internal.aliyuncs.com
Authorization: OSS qn6q:77Dv
User-Agent: aliyun-sdk-python-test/0.4.0

HTTP/1.1 204 No Content
Server: AliyunOSS
Date: Fri, 27 Jul 2018 09:10:52 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5B5AE19C188DC1CE81DAD7C8
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call DeleteBucketWebsite:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting-2#undefined)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting-1#undefined)

-

[PHP](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting-6#undefined)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-static-website-hosting)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting-9#undefined)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting-10#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/static-website-hosting-7#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-and-manage-static-website-hosting#undefined)

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 Not Found | The bucket that you want to disable the static website hosting mode for does not exist. |
| AccessDenied | 403 Forbidden | You do not have the permission to disable the static website hosting mode for the bucket. Only the owner of a bucket can disable the static website hosting mode for a bucket. |


Thank you! We've received your  feedback.