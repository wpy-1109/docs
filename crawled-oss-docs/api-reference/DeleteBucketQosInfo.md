# Operations related to the resource pool QoS

Deletes bandwidth throttling rules for a bucket in a resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to delete bandwidth throttling rules for a bucket in a resource pool. Deleting bandwidth throttling rules as a RAM user or by using Security Token Service (STS) requires the oss:DeleteBucketQoSInfo permission. For more information, see Common Examples of RAM Policy.

Syntax
 
DELETE /?qosInfo HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DeleteBucketQosInfo request are common request headers. For more information, see Common Request Headers.

Response headers

All headers in the response to a DeleteBucketQosInfo request are common response headers. For more information, see Common Response Headers.

Example

Sample request

 
DELETE /?qosInfo HTTP/1.1
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

You can use OSS SDKs for the following programming languages to call DeleteBucketQosInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the DeleteBucketQosInfo operation, see delete-bucket-qos-info.