# Anti-DDoS Pro

Initializes Anti-DDoS instances for a bucket.

Usage notes

By default, an Alibaba Cloud account has the permissions to initialize Anti-DDoS instances for a bucket. To initialize Anti-DDoS instances for a bucket by using a RAM user or Security Token Service (STS), you must have the oss:InitBucketAntiDDosInfo permission. For more information, see 为RAM用户授权自定义的权限策略.

Request syntax
 
PUT /?antiDDos HTTP/1.1
Date:  GMT Date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73****
x-oss-defender-type: AntiDDosPremimum
<AntiDDOSConfiguration>
  <Cnames>
    <Domain>abc1.example.cn</Domain>
    <Domain>abc2.example.cn</Domain>
  </Cnames>
</AntiDDOSConfiguration>
Request headers

Header

	

Type

	

Required

	

Example

	

Description




x-oss-defender-instance

	

String

	

Yes

	

cbcac8d2-4f75-4d6d-9f2e-c3447f73****

	

The ID of the Anti-DDoS instance.




x-oss-defender-type

	

String

	

Yes

	

AntiDDosPremimum

	

The type of the Anti-DDoS instance. Set the value to

AntiDDosPremimum.




AntiDDOSConfiguration

	

Container

	

No

	

N/A

	

The container that stores the configurations of Anti-DDoS instances.




Cnames

	

Container

	

No

	

N/A

	

The container that stores the list of domain names.




Domain

	

String

	

No

	

abc1.example.cn

	

The custom domain names that you want to protect. You can add up to five custom domain names for each bucket to the protection list of an Anti-DDoS instance.

For more information about other common request headers that are included in an InitBucketAntiDDosInfo request, such as Host and Date, see Common HTTP headers.

Response headers

All headers in the response to an InitBucketAntiDDosInfo request are common response headers. For more information about common response headers, see Common HTTP headers.

Examples

Sample request

 
PUT /?antiDDos HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73****
x-oss-defender-type: AntiDDosPremimum

Sample success response

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:34:24 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 534B371674E88A4D8906****
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73****
x-oss-server-time: 130