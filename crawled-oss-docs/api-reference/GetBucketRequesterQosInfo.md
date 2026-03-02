# Operations related to the resource pool QoS

You can call GetBucketRequesterQoSInfo to query the throttling configurations for a requester accessing a bucket in a resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to query the throttling configurations of all requesters for a bucket. Making query requests as a RAM user or by using Security Token Service (STS) requires the oss:GetBucketRequesterQoSInfo permission. For more information, see RAM policy common examples.

Syntax
 
GET /?requesterQosInfo&qosRequester=uid
Host: BucketName.oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetBucketRequesterQoSInfo request are common request headers. For more information, see Common HTTP headers.

Request elements

Name

	

Type

	

Required

	

Example

	

Description




qosRequester

	

String

	

Yes

	

300xxxx

	

The user ID (UID) of the requester.

Response headers

All headers in the response to a GetBucketRequesterQoSInfo request are common response headers. For more information, see Common response headers.

Response elements

Name

	

Type

	

Example

	

Description




RequesterQoSInfo

	

Container

	

N/A

	

Container that stores the result of the request.

Parent nodes: none




Requester

	

String

	

300xxxx

	

User ID (UID) of the requester.

Parent node: RequesterQoSInfo




QoSConfiguration

	

Container

	

N/A

	

Container that stores the throttling configurations of the requester.

Parent node: RequesterQoSInfo




TotalUploadBandwidth

	

Integer

	

10

	

Total upload bandwidth specified by the requester for the resource pool. Unit: Gbit/s.

Parent node: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

-1

	

Upload bandwidth over an internal network specified by the requester for the resource pool. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent node: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

-1

	

Upload bandwidth over a public network specified by the requester for the resource pool. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent node: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

10

	

Total download bandwidth specified by the requester for the resource pool. Unit: Gbit/s.

Parent node: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

-1

	

Download bandwidth over an internal network specified by the requester for the resource pool. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent node: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

-1

	

Download bandwidth over a public network specified by the requester for the resource pool. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent node: QoSConfiguration

Examples

Sample request

 
GET /?requesterQosInfo&qosRequester=300xxxx
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 515
x-oss-request-id: 534****

<RequesterQoSInfo>
  <Requester>300xxxx</Requester>
  <QoSConfiguration>
    <TotalUploadBandwidth>10</TotalUploadBandwidth>
    <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
    <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
    <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
    <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
    <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
  </QoSConfiguration>
</RequesterQoSInfo>
OSS SDKs

You can use OSS SDKs for the following programming languages to call GetBucketRequesterQoSInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the GetBucketRequesterQoSInfo operation, see get-bucket-requester-qos-info.