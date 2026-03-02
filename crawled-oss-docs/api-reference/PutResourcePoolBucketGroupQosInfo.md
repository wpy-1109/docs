# PutResourcePoolBucketGroupQoSInfo

Configures or modifies the bandwidth throttling settings of a bucket group in a resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has full permissions. If you want to perform the operation as a RAM user or by using a RAM role, ask the owner of the Alibaba Cloud account or the administrator to grant you the oss:PutResourcePoolBucketGroupQoSInfo permission by using a RAM policy or Bucket policy.

Request syntax
 
PUT /?resourcePoolBucketGroupQosInfo&resourcePool=<ResourcePoolName>&resourcePoolBucketGroup=<ResourcePoolBucketGroupName>
Host: oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Content-Type: application/xml
Content-Length: content length
Request headers

All headers in a PutResourcePoolBucketGroupQoSInfo request are common request headers. For more information, see Common request headers.

Request elements
Note

The bandwidth throttling settings in the following table default to -1, which indicates that the bandwidth is not limited. The value 0 for these settings indicates that the bandwidth type is prohibited. For example, the value 0 for ExtranetUploadBandwidth indicates that data cannot be uploaded to the specified bucket over a public network.

The total bandwidth for a bucket group cannot exceed the total bandwidth of the resource pool. An individual bandwidth throttling setting for a bucket group cannot exceed the total bandwidth of that type. For example, if the total download bandwidth is configured as 10 Gbit/s, the public network download bandwidth cannot exceed 10 Gbit/s.

An individual bandwidth throttling setting of a bucket group cannot be less than 5 Gbit/s.

Name

	

Type

	

Required

	

Example

	

Description




resourcePool

	

String

	

Yes

	

resource-pool-for-ai

	

The name of the resource pool.




resourcePoolBucketGroup

	

String

	

Yes

	

test-group

	

The name of the bucket group.




QoSConfiguration

	

Container

	

Yes

	

N/A

	

The container for the bandwidth throttling configuration.

Parent node: none




TotalUploadBandwidth

	

Integer

	

Yes

	

10

	

The total upload bandwidth of the bucket group. Unit: Gbit/s.

Parent node: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

The internal network upload bandwidth of the bucket group, including the upload bandwidth over the classic network and virtual private cloud (VPC). Unit: Gbit/s.

Parent node: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

The public network upload bandwidth of the bucket group, including the upload bandwidth over the public network and acceleration endpoint. Unit: Gbit/s.

Parent node: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

Yes

	

10

	

The total download bandwidth of the bucket group. Unit: Gbit/s.

Parent node: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

The internal network download bandwidth of the bucket group, including the download bandwidth over the classic network and VPC. Unit: Gbit/s.

Parent node: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

The public network download bandwidth of the bucket group, including the download bandwidth over the public network and acceleration endpoint. Unit: Gbit/s.

Parent node: QoSConfiguration

Response headers

All headers in the response to a PutResourcePoolBucketGroupQoSInfo request are common response headers. For more information, see Common response headers.

Examples

Sample request

 
PUT /?resourcePoolBucketGroupQosInfo&resourcePool=resource-pool-for-ai&resourcePoolBucketGroup=test-group
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Type: application/xml
Content-Length: content length

<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>

Sample success response

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 0