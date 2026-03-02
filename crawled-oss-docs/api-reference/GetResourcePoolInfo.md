# GetResourcePoolInfo

Queries the information about a resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has the permissions to query the throttling configurations of a resource pool. To query the information about a resource pool by using a Resource Access Management (RAM) user or Security Token Service (STS), you must have the oss:GetResourcePoolInfo permission. For more information, see Attach a custom policy to a RAM user.

Request syntax
 
GET /?resourcePoolInfo&resourcePool=ResourcePoolName
Host: oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetResourcePoolInfo request are common request headers. For more information, see Common request headers.

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

Response headers

All headers in the response to a GetResourcePoolInfo request are common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




GetResourcePoolInfoResponse

	

Container

	

N/A

	

The container that stores the result of the request.

Parent nodes: none.




Region

	

String

	

oss-cn-hangzhou

	

The region in which the resource pool resides.

Parent nodes: GetResourcePoolInfoResponse.




Name

	

String

	

resource-pool-for-ai

	

The name of the resource pool.

Parent nodes: GetResourcePoolInfoResponse.




Owner

	

String

	

103xxxx

	

The unique identifier (UID) of the account to which the resource pool belongs.

Parent nodes: GetResourcePoolInfoResponse.




CreateTime

	

String

	

2024-11-29T08:42:32.000Z

	

The time when the resource pool was created. The time follows the ISO 8601 standard.

Parent nodes: GetResourcePoolInfoResponse.




QoSConfiguration

	

Container

	

N/A

	

The container that stores the throttling configurations of the resource pool.

Parent nodes: GetResourcePoolInfoResponse.




TotalUploadBandwidth

	

Integer

	

10

	

The total upload bandwidth of the resource pool. Unit: Gbit/s.

Parent nodes: QoSConfiguration.




IntranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth of the resource pool over internal networks. Internal networks include the classic network and virtual private clouds (VPCs). Unit: Gbit/s.

The value -1 indicates that the upload bandwidth over internal networks is not limited.

Parent nodes: QoSConfiguration.




ExtranetUploadBandwidth

	

Integer

	

-1

	

The upload bandwidth of the resource pool over public networks. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration.




TotalDownloadBandwidth

	

Integer

	

10

	

The total download bandwidth of the resource pool. Unit: Gbit/s.

Parent nodes: QoSConfiguration.




IntranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth of the resource pool over internal networks. Internal networks include the classic network and VPCs. Unit: Gbit/s.

The value -1 indicates that the download bandwidth over internal networks is not limited.

Parent nodes: QoSConfiguration.




ExtranetDownloadBandwidth

	

Integer

	

-1

	

The download bandwidth of the resource pool over public networks. Public networks include the Internet and acceleration endpoints. Unit: Gbit/s.

Parent nodes: QoSConfiguration.

Examples

Sample requests

 
GET /?resourcePoolInfo&resourcePool=resource-pool-for-ai
Host: oss-cn-hangzhou.aliyuncs.com
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample success responses

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 624
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<GetResourcePoolInfoResponse>
  <Region>oss-cn-hangzhou</Region>
  <Name>resource-pool-for-ai</Name>
  <Owner>103xxxx</Owner>
  <CreateTime>2024-11-29T08:42:32.000Z</CreateTime>
  <QoSConfiguration>
    <TotalUploadBandwidth>10</TotalUploadBandwidth>
    <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
    <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
    <TotalDownloadBandwidth>10</TotalDownloadBandwidth>
    <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
    <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
  </QoSConfiguration>
</GetResourcePoolInfoResponse>
OSS SDKs

You can use OSS SDKs for the following programming languages to call GetResourcePoolInfo:

Python V2

Go V2

ossutil

For information about the ossutil command that corresponds to the GetResourcePoolInfo operation, see get-resource-pool-info.