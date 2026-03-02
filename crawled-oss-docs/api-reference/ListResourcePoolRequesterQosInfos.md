# ListResourcePoolRequesterQoSInfos

Queries the throttling configurations of all requesters in a resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to query the throttling configurations of all requesters in a resource pool. To query the throttling configurations of all requesters in a resource pool by using a RAM user or Security Token Service (STS), you must have the oss:ListResourcePoolRequesterQoSInfos permission. For more information, see Common examples of RAM policies.

Syntax
 
GET /?requesterQosInfo&resourcePool=ResourcePoolName&max-keys=2&continuation-token=1105678
Host: oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a ListResourcePoolRequesterQoSInfos request are common request headers. For more information, see Common request headers.

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

	

The maximum number of requesters whose throttling configurations you want to query.




continuation-token

	

String

	

No

	

1105678

	

The requester from which the throttling configurations are returned.

Response headers

All headers in the response to a ListResourcePoolRequesterQoSInfos request are common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




ListResourcePoolRequesterQoSInfosResult

	

Container

	

N/A

	

The container that stores the result of the request.

Parent nodes: none




ResourcePool

	

String

	

resource-pool-for-ai

	

The name of the resource pool.

Parent nodes: ListResourcePoolRequesterQoSInfosResult




ContinuationToken

	

String

	

1105678

	

The continuationToken that is used in this ListResourcePoolRequesterQoSInfos request.

Parent nodes: ListResourcePoolRequesterQoSInfosResult




NextContinuationToken

	

String

	

3105678

	

Indicates that this ListResourcePoolRequesterQoSInfos request contains subsequent results. The value of NextContinuationToken is used as the value of ContinuationToken to query subsequent results.

Parent nodes: ListResourcePoolRequesterQoSInfosResult




IsTruncated

	

Boolean

	

true

	

Indicates whether the queried results are truncated.

true indicates that not all results are returned this time.

false indicates that all results are returned this time.

Parent nodes: ListResourcePoolBucketsResult




RequesterQoSInfo

	

Container

	

N/A

	

The container that stores the quality of throttling configurations of the requesters.

Parent nodes: ListResourcePoolRequesterQoSInfosResult




Requester

	

String

	

311xxxx

	

The user ID (UID) of the requester.

Parent nodes: RequesterQoSInfo




QoSConfiguration

	

Container

	

N/A

	

The container that stores the quality of throttling configurations of the requesters.

Parent nodes: RequesterQoSInfo




TotalUploadBandwidth

	

Integer

	

10

	

The total upload bandwidth specified by the requester for the resource pool. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth over an internal network specified by the requester for the resource pool. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth over a public network specified by the requester for the resource pool. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

10

	

The total download bandwidth specified by the requester for the resource pool. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth over an internal network specified by the requester for the resource pool. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth over a public network specified by the requester for the resource pool. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration

Examples

Sample requests

 
GET /?requesterQosInfo&resourcePool=resource-pool-for-ai&continuation-token=1105678&max-keys=2
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Authorization: SignatureValue

Sample success responses

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: conetent length
x-oss-request-id: 1265

<?xml version="1.0" encoding="UTF-8"?>
<ListResourcePoolRequesterQoSInfosResult>
  <ResourcePool>resource-pool-for-ai</ResourcePool>
  <ContinuationToken>1105678</ContinuationToken>
  <NextContinuationToken>3105678</NextContinuationToken>
  <IsTruncated>true</IsTruncated>
  <RequesterQoSInfo>
    <Requester>311xxxx</Requester>
    <QoSConfiguration>
      <TotalUploadBandwidth>10</TotalUploadBandwidth>
      <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
      <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
      <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
      <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
      <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
    </QoSConfiguration>
  </RequesterQoSInfo>
  <RequesterQoSInfo>
    <Requester>312xxxx</Requester>
    <QoSConfiguration>
      <TotalUploadBandwidth>10</TotalUploadBandwidth>
      <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
      <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
      <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
      <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
      <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
    </QoSConfiguration>
  </RequesterQoSInfo>
</ListResourcePoolRequesterQoSInfosResult>
OSS SDKs

You can use OSS SDKs for the following programming languages to call ListResourcePoolRequesterQoSInfos:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the ListResourcePoolRequesterQoSInfos operation, see list-resource-pool-requester-qos-infos.