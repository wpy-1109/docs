# DeleteAccessPoint

Deletes an access point.

Usage notes

By default, an Alibaba Cloud account has the permissions to delete an access point. To delete an access point by using a RAM user or Security Token Service (STS), you must have the oss:DeleteAccessPoint permission.

Request syntax
 
DELETE /?accessPoint HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: ContentType
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: apname
Authorization: SignatureValue
Request headers

Header

	

Type

	

Required

	

Example

	

Description




x-oss-access-point-name

	

String

	

Yes

	

ap-01

	

The name of the access point.

This request contains other common request headers, such as Date and Authorization. For more information, see Common HTTP headers.

Response headers

The response to a DeleteAccessPoint request contains only common response headers. For more information, see Common HTTP headers.

Examples

Sample request

 
DELETE /?accessPoint HTTP/1.1
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 10
Content-Type: application/xml
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: ap-01
Authorization: OSS qn6q**************:77Dv****************    

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
ossutil

For information about the ossutil command that corresponds to the DeleteAccessPoint operation, see delete-access-point.