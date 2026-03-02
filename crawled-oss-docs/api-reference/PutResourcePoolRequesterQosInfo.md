# PutResourcePoolRequesterQoSInfo

You can call PutResourcePoolRequesterQoSInfo to configure the throttling of a specific requester in a resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to configure bandwidth throttling rules for a bucket in a resource pool. Configuring as a RAM user or by using Security Token Service (STS) requires the oss:PutResourcePoolRequesterQoSInfo permission. For more information, see Common examples of RAM policies.

Syntax
 
PUT /?requesterQosInfo&resourcePool=ResourcePoolName&qosRequester=uid
Host: oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Content-Type: application/xml
Content-Length: content length

<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
  <TotalQps>-1</TotalQps>
  <IntranetQps>-1</IntranetQps>
  <ExtranetQps>-1</ExtranetQps>
</QoSConfiguration>
Request headers

All headers in a PutResourcePoolRequesterQoSInfo request are common request headers. For more information, see Common HTTP headers.

Request elements
Note

In the following table, the default value -1 specifies that the bucket bandwidth is not limited. The value 0 specifies that the bandwidth type is not supported. For example, the value 0 for ExtranetUploadBandwidth specifies that data cannot be uploaded to the specified bucket over a public network.

The total bandwidth specified for a requester cannot exceed the total bandwidth specified for the resource pool. The bandwidth specified for an individual item of a requester cannot exceed the total bandwidth for the requester. For example, if the total download bandwidth of all buckets is 100 Gbit/s, the download bandwidth over the Internet for a bucket cannot exceed 100 Gbit/s

The bandwidth specified for an individual item of a requester must be at least 5 Gbit/s.

Name

	

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




QoSConfiguration

	

Container

	

Yes

	

N/A

	

Container that stores the bandwidth throttling rules.

Parent nodes: none




TotalUploadBandwidth

	

Integer

	

Yes

	

10

	

Total upload bandwidth specified by the requester for the resource pool. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

Upload bandwidth over an internal network specified by the requester for the resource pool. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

Upload bandwidth over a public network specified by the requester for the resource pool. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

Yes

	

10

	

Total download bandwidth specified by the requester for the resource pool. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

Download bandwidth over an internal network specified by the requester for the resource pool. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

Download bandwidth over a public network specified by the requester for the resource pool. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration

Response headers

All headers in the response to a PutResourcePoolRequesterQoSInfo request are common response headers. For more information, see Common response headers.

Examples

Sample request

 
PUT /?requesterQosInfo&resourcePool=resource-pool-for-ai&qosRequester=300xxxx
Host: oss-cn-hangzhou.aliyuncs.com
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Type: application/xml
Content-Length: 454
Authorization: OSS qn6q****:77Dv****

<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
  <TotalQps>-1</TotalQps>
  <IntranetQps>-1</IntranetQps>
  <ExtranetQps>-1</ExtranetQps>
</QoSConfiguration>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 534****
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
ossutil

For information about the ossutil command that corresponds to the PutResourcePoolRequesterQoSInfo operation, see put-resource-pool-requester-qos-info.