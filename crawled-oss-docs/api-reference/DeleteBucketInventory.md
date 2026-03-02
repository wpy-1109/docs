# DeleteBucketInventory

You can call this operation to delete a specified inventory task of a bucket.

Usage notes

By default, an Alibaba Cloud account has the permissions to delete a specified inventory task of a bucket. If you want to delete a specified inventory task as a RAM user or by using STS, you must have the oss:DeleteBucketInventory permission.

If the request is successful, 204 is returned.

Request syntax
 
DELETE /?inventory&inventoryId=list1 HTTP/1.1
Request elements

Element

	

Type

	

Required

	

Description




inventoryId

	

String

	

Yes

	

The ID of the inventory task to delete.

Examples

Sample request

 
  DELETE /?inventory&inventoryId=list1 HTTP/1.1
  Host: BucketName.oss.aliyuncs.com
  Date: Wed, 14 May 2014 02:11:22 GMT
  Authorization: signatureValue

Sample response

 
  HTTP/1.1 204 No Content
  x-oss-request-id: 56594298207FB3044385****
  Date: Wed, 14 May 2014 02:11:22 GMT
  Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call DeleteBucketInventory operation:

Java

Python V2

Go V2

Node.js

C++

.NET

ossutil

For information about the ossutil command that corresponds to the DeleteBucketInventory operation, see delete-bucket-inventory.

Error codes

Error code

	

HTTP status code

	

Description




InvalidRequest

	

400

	

The error message returned because the request is invalid.




AccessDenied

	

403

	

The error message returned because your information for authentication is not included in the DeleteBucketInventory request.

The error message returned because you are not authorized to perform this operation.