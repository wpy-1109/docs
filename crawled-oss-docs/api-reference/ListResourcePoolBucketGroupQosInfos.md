# ListResourcePoolBucketGroupQoSInfos

Lists the throttling configurations of a bucket group in a resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has full permissions on resources in the account. If you want to list resources using a Resource Access Management (RAM) user or role, you must grant the user or role the oss:ListResourcePoolBucketGroupQoSInfos policy using the Alibaba Cloud account or the account administrator. For more information, see RAM policies or a Bucket Policy.

Request syntax
 
GET /?resourcePoolBucketGroupQoSInfo&resourcePool=ResourcePoolName&continuation-token=abcd&max-keys=2
Host: oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a ListResourcePoolBucketGroupQoSInfos request are common request headers. For more information, see Common Request Headers.

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

	

The name of the resource pool.




max-keys

	

Integer

	

No

	

2

	

The maximum number of bucket groups to return.




continuation-token

	

String

	

No

	

abcd

	

The bucket group from which the throttling configurations are returned.

Response headers

All headers in the response to a ListResourcePoolBucketGroupQoSInfos request are common response headers. For more information, see Common Response Headers.

Response elements

Element

	

Type

	

Example

	

Description




ListResourcePoolBucketGroupQoSInfosResult

	

Container

	

N/A

	

The container that stores the throttling configurations of bucket groups in a resource pool.

Parent nodes: none




ResourcePool

	

String

	

test-group

	

The name of the resource pool.

Parent nodes: ListResourcePoolBucketGroupQoSInfosResult




ContinuationToken

	

String

	

1105678

	

The continuationToken used in the request.

Parent nodes: ListResourcePoolBucketGroupQoSInfosResult




NextContinuationToken

	

String

	

3105678

	

Indicates that the request contains subsequent results. The value of NextContinuationToken is used as the value of ContinuationToken in the next query for subsequent results.

Parent nodes: ListResourcePoolBucketGroupQoSInfosResult




IsTruncated

	

Boolean

	

true

	

Indicates whether the queried results are truncated. Valid values:

true: Not all results are returned for the request.

false: All results are returned for the request.

Parent nodes: ListResourcePoolBucketGroupQoSInfosResult




ResourcePoolBucketGroupQoSInfo

	

Container

	

N/A

	

The container that stores the throttling configurations of bucket groups in a resource pool.

Parent nodes: ListResourcePoolBucketGroupQoSInfosResult




BucketGroup

	

String

	

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

	

The total upload bandwidth of the bucket group. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth of the bucket group over internal networks, including the classic network and virtual private clouds (VPCs). Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth of the bucket group over public networks, including the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

10

	

The total download bandwidth of the bucket group. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth of the bucket group over internal networks, including the classic network and VPCs. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth of the bucket group over public networks, including the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration

Examples

Sample requests

 
GET /?resourcePoolBucketGroupQoSInfo&resourcePool=resource-pool-for-ai&continuation-token=1105678&max-keys=2
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Authorization: SignatureValue

Sample responses

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 1386
x-oss-request-id: 534B************

<?xml version="1.0" encoding="UTF-8"?>
<ListResourcePoolBucketGroupQoSInfosResult>
  <ResourcePool>resource-pool-for-ai</ResourcePool>
  <ContinuationToken>1105678</ContinuationToken>
  <NextContinuationToken>3105678</NextContinuationToken>
  <IsTruncated>true</IsTruncated>
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
  <ResourcePoolBucketGroupQoSInfo>
    <BucketGroup>test-group-02<BucketGroup/>
    <QoSConfiguration>
      <TotalUploadBandwidth>10</TotalUploadBandwidth>
      <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
      <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
      <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
      <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
      <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
    </QoSConfiguration>
  </ResourcePoolBucketGroupQoSInfo>
</ListResourcePoolBucketGroupQoSInfosResult>
OSS SDKs

You can use OSS SDKs for the following programming languages to call the ListResourcePoolBucketGroupQoSInfos operation:

Python V2

Go V2