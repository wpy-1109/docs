# GetResourcePoolRequesterQoSInfo

You can call GetResourcePoolRequesterQoSInfo to query the throttling configurations of a specific requester in a resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to query the throttling configurations of a specific requester in a resource pool. Making query requests as a RAM user or by using Security Token Service (STS) requires the oss:GetResourcePoolRequesterQoSInfo permission. For more information, see Common examples of RAM policies.

Syntax
 
GET /?requesterQosInfo&resourcePool=ResourcePoolName&qosRequester=uid
Host: oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetResourcePoolRequesterQoSInfo request are common request headers. For more information, see Common HTTP headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




resourcePool

	

String

	

Yes

	

resource-pool-for-ai

	

Name of the resource pool.




qosRequester

	

String

	

Yes

	

300xxxx

	

User ID (UID) of the requester.

Response headers

All headers in the response to a GetResourcePoolRequesterQoSInfo request are common response headers. For more information, see Common response headers.

Response elements

Element

	

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

Example

Sample request

 
GET /?requesterQosInfo&resourcePool=resource-pool-for-ai&qosRequester=300xxxx
Host: oss-cn-hangzhou.aliyuncs.com   
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS qn6q****:77Dv****

Sample response

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Type: application/xml
Content-Length: 452

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
ossutil

For information about the ossutil command that corresponds to the GetResourcePoolRequesterQoSInfo operation, see get-resource-pool-requester-qos-info.