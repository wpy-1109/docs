# Operations related to the resource pool QoS

You can call PutBucketRequesterQoSInfo to configure throttling rules for a requester accessing a bucket within a resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to configure throttling rules for a requester accessing a bucket. Configuration as a RAM user or by using Security Token Service (STS) requires the oss:PutBucketRequesterQoSInfo permission. For more information, see RAM policy examples.

Syntax
 
PUT /?requesterQosInfo&qosRequester=uid
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue

<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>
Request headers

All headers in a PutBucketRequesterQoSInfo request are common request headers. For more information, see Common request headers.

Request parameters
Note

In the following table, the default value -1 specifies that the bucket bandwidth is not limited. The value 0 specifies that the bandwidth type is not supported. For example, the value 0 for ExtranetUploadBandwidth specifies that data cannot be uploaded to the specified bucket over a public network.

The total bandwidth threshold configured for a requester cannot exceed the total bandwidth specified for the resource pool. For example, if the total download bandwidth of all buckets is 100 Gbit/s, the download bandwidth over the Internet for a requester cannot exceed 100 Gbit/s.

The bandwidth thresholds for each item specified for the requester cannot be lower than 5 Gbit/s.

Parameter

	

Type

	

Required

	

Example

	

Description




qosRequester

	

String

	

Yes

	

300xxxx

	

User ID (UID) of the requester.

Parent nodes: none




QoSConfiguration

	

Container

	

Yes

	

N/A

	

Container that stores the results.

Parent nodes: none




TotalUploadBandwidth

	

Integer

	

Yes

	

10

	

Total upload bandwidth of the requester for the bucket. Unit: Gbit/s.

Parent node: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

Upload bandwidth over an internal network of the requester for the bucket. Internal networks include the classic network and virtual private cloud (VPC). Unit: Gbit/s.

Parent node: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

Upload bandwidth over a public network of the requester for the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent node: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

Yes

	

10

	

Total download bandwidth of the requester for the bucket. Unit: Gbit/s.

Parent node: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

Download bandwidth over an internal network of the requester for the bucket. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent node: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

Download bandwidth over a public network of the requester for the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent node: QoSConfiguration

Response headers

All headers in the response to a PutBucketRequesterQoSInfo request are common response headers. For more information, see Common response headers.

Example

Sample request

 
PUT /?requesterQosInfo&qosRequester=300xxxx
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Length: 209
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 534****
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call PutBucketRequesterQoSInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the PutBucketRequesterQoSInfo operation, see put-bucket-requester-qos-info.