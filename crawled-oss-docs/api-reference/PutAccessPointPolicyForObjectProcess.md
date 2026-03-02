# PutAccessPointPolicyForObjectProcess

Configures permission policies for an Object FC Access Point.

Usage notes

By default, an Alibaba Cloud account has the permissions to configure permission policies for an Object FC Access Point. To configure permission policies for an Object FC Access Point by using a RAM user or Security Token Service (STS), you must have the oss:PutAccessPointPolicyForObjectProcess permission.

Request syntax
 
PUT /?accessPointPolicyForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue
Policy written in JSON
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

For more information about other common request headers included in a PutAccessPointPolicyForObjectProcess request, such as Host and Date, see Common HTTP headers.

Response headers

The response to a PutAccessPointPolicyForObjectProcess request contains only common response headers. For more information, see Common HTTP headers.

Examples

Sample request

 
PUT /?accessPointPolicyForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 240
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e 

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

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 30 Oct 2023 03:15:40 GMT