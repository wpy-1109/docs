# Object FC Access Points

Deletes an Object FC Access Point.

Usage notes

By default, an Alibaba Cloud account has the permissions to delete an Object FC Access Point. To delete an Object FC Access Point by using a RAM user or Security Token Service (STS), you must have the oss:DeleteAccessPointForObjectProcess permission.

Request syntax
 
DELETE /?accessPointForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue
Request headers

Header

	

Type

	

Required

	

Example

	

Description




x-oss-access-point-for-object-process-name

	

String

	

Yes

	

fc-ap-01

	

The name of the Object FC Access Point.

For more information about other common request headers included in a DeleteAccessPointForObjectProcess request, such as Host and Date, see Common HTTP headers.

Response headers

The response to a DeleteAccessPointForObjectProcess request contains only common response headers. For more information, see Common HTTP headers.

Examples

Sample request

 
DELETE /?accessPointForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: OSS qn6q**************:77Dv****************

Sample response

 
HTTP/1.1 204 OK
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 30 Oct 2023 03:15:40 GMT