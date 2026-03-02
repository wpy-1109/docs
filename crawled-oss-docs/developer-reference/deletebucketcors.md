# Disable CORS and delete all CORS rules of a bucket by calling DeleteBucketCors

You can call this operation to disable cross-origin resource sharing (CORS) for a specific bucket and delete all CORS rules configured for the bucket.

## Request structure


`plaintext
DELETE /? cors HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


DeleteBucketCors requests contain only common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


Responses for DeleteBucketCors requests contain only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Sample request


`plaintext
DELETE /? cors HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 05:45:34 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 204 No Content
x-oss-request-id: 5051845BC4689A033D00
Date: Fri, 24 Feb 2012 05:45:34 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call DeleteBucketCors:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-1#undefined)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/cross-domain-resource-sharing-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/cross-domain-resource-sharing-for-php-sdk-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/cross-domain-resource-sharing-for-go-sdk-v2)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-10#undefined)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-3#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-9#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-8#section-r9f-ft5-q04)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-6#undefined)

## ossutil


For information about the ossutil command that corresponds to the DeleteBucketCors operation, see [delete-bucket-cors](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-a-cross-domain-resource-sharing-rule).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The error message returned because the specified bucket does not exist. |
| AccessDenied | 403 | The error message returned because you are not authorized to perform this operation. Only the owner of a bucket can delete the CORS rules configured for the bucket. |


Thank you! We've received your  feedback.