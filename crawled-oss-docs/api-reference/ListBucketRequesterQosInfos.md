# Operations related to the resource pool QoS

Queries the throttling configurations of all requesters for a bucket.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to query the throttling configurations of all requesters for a bucket. To query the throttling configurations of all requesters for a bucket by using a RAM user or Security Token Service (STS), you must have the oss:ListBucketRequesterQoSInfo permission. For more information, see Common examples of RAM policies.

Syntax
 
GET /?requesterQosInfo&max-keys=10&continuation-token=207xxxx
Host: BucketName.oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a ListBucketRequesterQoSInfos request are common request headers. For more information, see Common request headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




max-keys

	

String

	

No

	

10

	

The maximum number of requesters whose throttling configurations you want to query.




continuation-token

	

String

	

No

	

207xxxx

	

The requester from which the throttling configurations are returned.

Response headers

All headers in the response to a ListBucketRequesterQoSInfos request are common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




ListBucketRequesterQoSInfosResult

	

Container

	

N/A

	

The container that stores the result of the request.

Parent nodes: none




Bucket

	

String

	

oss-example

	

The name of the bucket.

Parent nodes: ListBucketRequesterQoSInfosResult




ContinuationToken

	

String

	

207xxxx

	

The continuationToken that is used in this ListBucketRequesterQoSInfos request.

Parent nodes: ListBucketRequesterQoSInfosResult




NextContinuationToken

	

String

	

262xxxx

	

Indicates that this ListBucketRequesterQoSInfos request contains subsequent results. The value of NextContinuationToken is used as the value of ContinuationToken to query subsequent results.

Parent nodes: ListBucketRequesterQoSInfosResult




IsTruncated

	

Boolean

	

true

	

Indicates whether the queried results are truncated.

true indicates that not all results are returned this time.

false indicates that all results are returned this time.

Parent nodes: ListBucketRequesterQoSInfosResult




RequesterQoSInfo

	

Container

	

N/A

	

The container that stores the throttling configurations of the requesters.

Parent nodes: RequesterQoSInfo




Requester

	

String

	

266xxxx

	

The user ID (UID) of the requester.

Parent nodes: RequesterQoSInfo




QoSConfiguration

	

Container

	

N/A

	

The container that stores the throttling configurations of the requester.

Parent nodes: RequesterQoSInfo




TotalUploadBandwidth

	

Integer

	

10

	

The total upload bandwidth of the requester for the bucket. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth over an internal network of the requester for the bucket. Internal networks include the classic network and virtual private cloud (VPC). Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth over a public network of the requester for the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

10

	

The total download bandwidth of the requester for the bucket. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth over an internal network of the requester for the bucket. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth over a public network of the requester for the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration

Examples

Sample request

 
GET /?requesterQosInfo&max-keys=2&continuation-token=207xxxx
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 1385
x-oss-request-id: 534****

<ListBucketRequesterQoSInfosResult>
  <Bucket>BucketName</Bucket>
  <ContinuationToken>207xxxx</ContinuationToken>
  <NextContinuationToken>262xxxx</NextContinuationToken>
  <IsTruncated>true</IsTruncated>
  <RequesterQoSInfo>
    <Requester>266xxxx</Requester>
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
    <Requester>276xxxx</Requester>
    <QoSConfiguration>
      <TotalUploadBandwidth>10</TotalUploadBandwidth>
      <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
      <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
      <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
      <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
      <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
    </QoSConfiguration>
  </RequesterQoSInfo>
</ListBucketRequesterQoSInfosResult>
OSS SDKs

You can use OSS SDKs for the following programming languages to call ListBucketRequesterQoSInfos:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the ListBucketRequesterQoSInfos operation, see list-bucket-requester-qos-infos.