# GetAccessPointPolicyForObjectProcess

Queries the permission policies of an Object FC Access Point.

Usage notes

By default, an Alibaba Cloud account has the permissions to query the permission policies of an Object FC Access Point. To query the permission policies of an Object FC Access Point by using a RAM user or Security Token Service (STS), you must have the oss:GetAccessPointPolicyForObjectProcess permission.

Request syntax
 
GET /?accessPointPolicyForObjectProcess HTTP/1.1
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

For more information about other common request headers included in a GetAccessPointPolicyForObjectProcess request, such as Host and Date, see Common HTTP headers.

Response headers

The response to a GetAccessPointPolicyForObjectProcess request contains only common response headers. For more information, see Common HTTP headers.

Examples

Sample request

 
GET /?accessPointPolicyForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 30 Oct 2023 03:15:40 GMT
<?xml version="1.0" encoding="UTF-8"?>
{
	"Version": "1",
	"Statement": [{
		"Effect": "Allow",
		"Action": [
			"oss:GetObject"
		],
		"Principal": [
			"23721626365841xxxx"
		],
		"Resource": [
			"acs:oss:cn-qingdao:111933544165xxxx:accesspointforobjectprocess/fc-ap-001/object/*"
		]
	}]
}