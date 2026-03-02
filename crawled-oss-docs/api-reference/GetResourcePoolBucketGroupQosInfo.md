# GetResourcePoolBucketGroupQoSInfo

Use GetResourcePoolBucketGroupQoSInfo command to retrieve the throttling configuration of a bucket group in a resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has full permissions. To retrieve information as a RAM user or by using a RAM role, the Alibaba Cloud account or administrator must grant the oss:GetResourcePoolBucketGroupQoSInfo permission through RAM Policy or Bucket Policy.

Syntax
 
GET /?resourcePoolBucketGroupQosInfo&resourcePool=<ResourcePoolName>&resourcePoolBucketGroup=<resourcePoolBucketGroupName>
Host: oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetResourcePoolBucketGroupQoSInfo request are common request headers. For more information, see Common Request Headers.

Request elements

Name

	

Type

	

Required

	

Example

	

Description




resourcePool

	

string

	

Yes

	

resource-pool-for-ai

	

The name of the resource pool.




ResourcePoolBucketGroup

	

string

	

Yes

	

test-group

	

The name of the bucket group.

Response headers

All headers in the response to a GetResourcePoolBucketGroupQoSInfo request are common response headers. For more information, see Common Response Headers.

Response elements

Name

	

Type

	

Example

	

Description




ResourcePoolBucketGroupQoSInfo

	

Container

	

N/A

	

The container that stores the throttling configuration information of a bucket group in a resource pool.

Parent nodes: none




resourcePoolBucketGroup

	

string

	

test-group

	

The name of the bucket group.

Parent nodes: ResourcePoolBucketGroupQoSInfo




QoSConfiguration

	

Container

	

N/A

	

The container that stores the throttling configuration information.

Parent nodes: ResourcePoolBucketGroupQoSInfo




TotalUploadBandwidth

	

Integer

	

10

	

The total upload bandwidth of the bucket group. Unit: Gbps.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

-1

	

The internal upload bandwidth of the bucket group, including the internal upload bandwidth of the classic network and VPC network. Unit: Gbps.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

-1

	

The external upload bandwidth of the bucket group, including the upload bandwidth of the public network and acceleration endpoint. Unit: Gbps.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

10

	

The total download bandwidth of the bucket group. Unit: Gbps.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

-1

	

The internal download bandwidth of the bucket group, including the internal download bandwidth of the classic network and VPC network. Unit: Gbps.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

-1

	

The external download bandwidth of the bucket group, including the download bandwidth of the public network and acceleration endpoint. Unit: Gbps.

Parent nodes: QoSConfiguration

Examples

Request example

 
GET /?resourcePoolBucketGroupQosInfo&resourcePool=resource-pool-for-ai&resourcePoolBucketGroup=test-group
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Authorization: SignatureValue

Response example

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Type: application/xml
Content-Length: 457

<ResourcePoolBucketGroupQoSInfo>
  <BucketGroup>test-group</BucketGroup>
  <QoSConfiguration>
    <TotalUploadBandwidth>10</TotalUploadBandwidth>
    <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
    <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
    <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
    <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
    <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
  </QoSConfiguration>
</ResourcePoolBucketGroupQoSInfo>
OSS SDKs

You can use OSS SDKs for the following programming languages to call the GetResourcePoolBucketGroupQoSInfo operation:

Python V2

Go V2