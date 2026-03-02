# DeleteBucketCors

You can call this operation to disable cross-origin resource sharing (CORS) for a specific bucket and delete all CORS rules configured for the bucket.

Request structure
 
DELETE /? cors HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

DeleteBucketCors requests contain only common request headers. For more information, see Common request headers.

Response headers

Responses for DeleteBucketCors requests contain only common response headers. For more information, see Common response headers.

Examples

Sample request

 
DELETE /? cors HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com  
Date: Thu, 17 Apr 2025 05:45:34 GMT  
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204 No Content 
x-oss-request-id: 5051845BC4689A033D00****
Date: Fri, 24 Feb 2012 05:45:34 GMT
Connection: keep-alive
Content-Length: 0  
Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call DeleteBucketCors:

Java

Python V2

PHP V2

Go V2

C++

C

.NET

Node.js

Ruby

ossutil

For information about the ossutil command that corresponds to the DeleteBucketCors operation, see delete-bucket-cors.

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucket

	

404

	

The error message returned because the specified bucket does not exist.




AccessDenied

	

403

	

The error message returned because you are not authorized to perform this operation. Only the owner of a bucket can delete the CORS rules configured for the bucket.