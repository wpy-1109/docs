# Operations related to the resource pool QoS

You can call GetBucketQoSInfo to query the throttling configurations for a specific requester accessing a bucket.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to query the throttling configurations of all requesters for a bucket in a resource pool. Making query requests as a RAM user or by using Security Token Service (STS) requires the oss:GetBucketQoSInfo permission. For more information, see RAM policy common examples.

Syntax
 
GET /?qosInfo HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetBucketQoSInfo request are common request headers. For more information, see Common HTTP headers.

Response headers

All headers in the response to a GetBucketQoSInfo request are common response headers. For more information, see Common response headers.

Response elements

Name

	

Type

	

Example

	

Description




QoSConfiguration

	

Container

	

N/A

	

Container that stores the result of the request.

Parent nodes: none




TotalUploadBandwidth

	

Integer

	

10

	

Total upload bandwidth of the bucket. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

-1

	

Upload bandwidth over an internal network of the bucket. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

-1

	

Upload bandwidth over a public network of the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

10

	

Total download bandwidth of the bucket. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

-1

	

Download bandwidth over an internal network of the bucket. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

-1

	

Download bandwidth over a public network of the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration

Examples

Sample request

 
Get /?qosInfo HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com   
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Type: application/xml
Content-Length: 556
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 534****

<?xml version="1.0" encoding="UTF-8"?>
<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>
OSS SDKs

You can use OSS SDKs for the following programming languages to call GetBucketQoSInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the GetBucketQoSInfo operation, see get-bucket-qos-info.