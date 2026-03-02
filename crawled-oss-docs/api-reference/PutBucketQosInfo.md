# Operations related to the resource pool QoS

Configures bandwidth throttling rules for a bucket in a resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to configure bandwidth throttling rules for a bucket in a resource pool. To configure bandwidth throttling rules for a bucket by using a RAM user or Security Token Service (STS), you must have the oss:PutBucketQoSInfo permission. For more information, see Common examples of RAM policies.

Syntax
 
PUT /?qosInfo HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<QoSConfiguration>
  <TotalUploadBandwidth>10</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>
Request headers

All headers in a PutBucketQoSInfo request are common request headers. For more information, see Common request headers.

Request elements
Note

In the following table, the default value -1 specifies that the bucket bandwidth is not limited. The value 0 specifies that the bandwidth type is not supported. For example, the value 0 for ExtranetUploadBandwidth specifies that data cannot be uploaded to the specified bucket over a public network.

The total bandwidth specified for a bucket cannot exceed the total bandwidth specified for the resource pool. The total bandwidth specified for a bucket cannot exceed the total bandwidth specified for all buckets. For example, if the total download bandwidth of all buckets is 100 Gbit/s, the download bandwidth over the Internet for a bucket cannot exceed 100 Gbit/s.

Element

	

Type

	

Required

	

Example

	

Description




QoSConfiguration

	

Container

	

Yes

	

N/A

	

The container that stores the bandwidth throttling rules.

Parent nodes: none




TotalUploadBandwidth

	

Integer

	

Yes

	

10

	

The total upload bandwidth of the bucket. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

The upload bandwidth over an internal network of the bucket. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetUploadBandwidth

	

Integer

	

Yes

	

-1

	

The upload bandwidth over a public network of the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration




TotalDownloadBandwidth

	

Integer

	

Yes

	

10

	

The total download bandwidth of the bucket. Unit: Gbit/s.

Parent nodes: QoSConfiguration




IntranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

The download bandwidth over an internal network of the bucket. Internal networks include the classic network and VPC. Unit: Gbit/s.

Parent nodes: QoSConfiguration




ExtranetDownloadBandwidth

	

Integer

	

Yes

	

-1

	

The download bandwidth over a public network of the bucket. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration

Response headers

All headers in the response to a PutBucketQoSInfo request are common response headers. For more information, see Common response headers.

Examples

Sample requests

 
PUT /?qosInfo HTTP/1.1
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

Sample success responses

 
HTTP/1.1 200 OK
x-oss-request-id: 534****
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call PutBucketQoSInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the PutBucketQoSInfo operation, see put-bucket-qos-info.