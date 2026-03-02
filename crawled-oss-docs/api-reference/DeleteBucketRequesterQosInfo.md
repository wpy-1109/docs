# Operations related to the resource pool QoS

Call the DeleteBucketRequesterQoSInfo operation to delete the throttling configurations for a requester accessing a bucket.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to delete the throttling configurations for a requester in a resource pool. Deleting configurations as a RAM user or by using Security Token Service (STS) requires the oss:DeleteBucketRequesterQoSInfo permission. For more information, see Common Examples of RAM Policies.

Syntax
 
DELETE /?requesterQosInfo&qosRequester=uid
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DeleteBucketRequesterQoSInfo request are common request headers. For more information, see Common Request Headers.

Request parameter

Name

	

Type

	

Required

	

Sample value

	

Description




qosRequester

	

String

	

Yes

	

300xxxx

	

The user ID (UID) of the requester.

Response headers

All headers in the response to a DeleteBucketRequesterQoSInfo request are common response headers. For more information, see Common Response Headers.

Example

Sample request

 
DELETE /?requesterQosInfo&qosRequester=300xxxx
Host: oss-example.oss-cn-hangzhou.aliyuncs.com  
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 534****
OSS SDKs

You can use OSS SDKs for the following programming languages to call DeleteBucketRequesterQoSInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the DeleteBucketRequesterQoSInfo operation, see delete-bucket-requester-qos-info.