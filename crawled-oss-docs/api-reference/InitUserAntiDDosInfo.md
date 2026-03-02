# Anti-DDoS Pro

Creates Anti-DDoS instances.

Note

By default, an Alibaba Cloud account has the permissions to create Anti-DDoS instances. To create Anti-DDoS instances by using a RAM user or Security Token Service (STS), you must have the oss:InitUserAntiDDosInfo permission. For more information, see Common examples of RAM policies.

Request syntax
 
PUT /?antiDDos HTTP/1.1
Date:  GMT Date
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in an InitUserAntiDDosInfo request are common request headers. For more information, see Common HTTP headers.

Response headers

Header

	

Type

	

Example

	

Description




x-oss-defender-instance

	

String

	

cbcac8d2-4f75-4d6d-9f2e-c3447f73****

	

The ID of the Anti-DDoS instance.

For more information about other common response headers that are included in the response to an InitUserAntiDDosInfo request, such as x-oss-request-id and Content-Type, see Common HTTP headers.

Example

Sample request

 
PUT /?antiDDos HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:34:24 GMT
Connection: keep-alive
x-oss-request-id: 534B371674E88A4D8906****
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73****