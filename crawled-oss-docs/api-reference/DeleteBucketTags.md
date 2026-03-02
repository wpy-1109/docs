# DeleteBucketTags

Deletes tags configured for a bucket.

Notes

The oss:DeleteBucketTagging permission is required to deletes tags configured for a bucket by calling the DeleteBucketTags operation. For more information, see Attach a custom policy to a RAM user.

Note

If no tag is configured for the bucket or the tags that you want to delete do not exist, OSS returns HTTP status code 204.

Request syntax
 
DELETE /?tagging HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DeleteBucketTags request are common request headers. For more information, see Common HTTP headers.

Response headers

All headers in the response to a DeleteBucketTags request are common response headers. For more information, see Common HTTP headers.

Examples

Sample request sent to delete all tags of a bucket

 
DELETE /?tagging HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 25 Dec 2018 17:35:24 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample response

 
HTTP/1.1 204 No Content
x-oss-request-id: 5C22E0EFD127F6810B1A****
Date: Tue, 25 Dec 2018 17:35:24 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 293

Sample request sent to delete tags whose keys are k1 and k2

 
DELETE /?tagging=k1,k2 HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 25 Dec 2018 17:35:24 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample response

 
HTTP/1.1 204 No Content
x-oss-request-id: 5C22E0EFD127F6810B1A92A8
Date: Tue, 25 Dec 2018 17:35:24 GMT
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
x-oss-server-time: 293
SDKs

Java

Python

Go V2

C++

Node.js

.NET

PHP

ossutil

For information about the ossutil command that corresponds to the DeleteBucketTags operation, see delete-bucket-tags.

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucket

	

404 No Content

	

The bucket does not exist.




AccessDenied

	

403 Forbidden

	

You do not have permissions to delete the tags of the bucket. Only the owner of a bucket can delete the tags of the bucket.