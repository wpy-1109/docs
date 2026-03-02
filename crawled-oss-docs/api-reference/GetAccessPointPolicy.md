# GetAccessPointPolicy

Queries the configurations of access point policies.

Usage notes

By default, an Alibaba Cloud account has the permissions to query the configurations of access point policies. To query the configurations of access point policies by using a RAM user or Security Token Service (STS), you must have the oss:GetAccessPointPolicy permission.

Request syntax
 
GET /?accessPointPolicy HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
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

The response to a GetAccessPointPolicy request contains only common response headers. For more information, see Common HTTP headers.

Examples

Sample request

 
GET /?accessPointPolicy HTTP/1.1
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 230
Content-Type: application/xml
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: ap-01
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e    

Sample response

 
HTTP/1.1 200
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
content-type: application/json 
Authorization: OSS qn6q**************:77Dv****************    
{
   "Version":"1",
   "Statement":[
   {
     "Action":[
       "oss:PutObject",
       "oss:GetObject"
    ],
    "Effect":"Deny",
    "Principal":["27737962156157xxxx"],
    "Resource":[
       "acs:oss:cn-hangzhou:111933544165xxxx:accesspoint/$ap-01",
       "acs:oss:cn-hangzhou:111933544165xxxx:accesspoint/$ap-01/object/*"
     ]
   }
  ]
 }	

ossutil

For information about the ossutil command that corresponds to the GetAccessPointPolicy operation, see get-access-point-policy.