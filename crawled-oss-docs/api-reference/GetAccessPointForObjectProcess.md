# Object FC Access Points

Queries basic information about an Object FC Access Point.

Usage notes

By default, an Alibaba Cloud account has the permissions to query basic information about an Object FC Access Point. To query basic information about an Object FC Access Point by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the oss:GetAccessPointForObjectProcess permission.

Request syntax
 
GET /?accessPointForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue
Request headers

Header

	

Type

	

Required

	

Example

	

Description




x-oss-access-point-for-object-process-name

	

String

	

Yes

	

fc-ap-01

	

The name of the Object FC Access Point.

For more information about other common request headers included in a GetAccessPointForObjectProcess request, such as Host and Date, see Common request headers.

Response headers

The response to a GetAccessPointForObjectProcess request contains only common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




GetAccessPointForObjectProcessResult

	

Container

	

N/A

	

The container that stores information about the Object FC Access Point.

Parent nodes: none

Child nodes: AccessPointNameForObjectProcess, AccessPointForObjectProcessAlias, AccessPointName, AccountId, AccessPointForObjectProcessArn, CreationDate, Status, and Endpoints




AccessPointNameForObjectProcess

	

String

	

fc-ap-01

	

The name of the Object FC Access Point.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




AccessPointForObjectProcessAlias

	

String

	

fc-ap-01-3b00521f653d2b3223680ec39dbbe2****-opapalias

	

The alias of the Object FC Access Point.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




AccessPointName

	

String

	

ap-01

	

The name of the access point.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




AccountId

	

String

	

111933544165****

	

The UID of the Alibaba Cloud account to which the Object FC Access Point belongs.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




AccessPointForObjectProcessArn

	

String

	

acs:oss:cn-qingdao:119335441657143:accesspointforobjectprocess/fc-ap-01

	

The ARN of the Object FC Access Point.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




CreationDate

	

String

	

1626769503

	

The time when the Object FC Access Point was created. The value is a timestamp.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




Status

	

	

enable

	

The status of the Object FC Access Point. Valid values:

enable: The Object FC Access Point is created.

disable: The Object FC Access Point is disabled.

creating: The Object FC Access Point is being created.

deleting: The Object FC Access Point is deleted.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: none




Endpoints

	

Container

	

N/A

	

The container that stores the endpoints of the Object FC Access Point.

Parent nodes: GetAccessPointForObjectProcessResult

Child nodes: PublicEndpoint and InternalEndpoint




PublicEndpoint

	

String

	

fc-ap-01-111933544165****.oss-cn-qingdao.oss-object-process.aliyuncs.com

	

The public endpoint of the Object FC Access Point.

Parent nodes: Endpoints

Child nodes: none




InternalEndpoint

	

String

	

fc-ap-01-111933544165****.oss-cn-qingdao-internal.oss-object-process.aliyuncs.com

	

The internal endpoint of the Object FC Access Point.

Parent nodes: Endpoints

Child nodes: none




PublicAccessBlockConfiguration

	

Container

	

N/A

	

The container in which the Block Public Access configurations are stored.

Parent nodes: GetAccessPointResult

Child nodes: BlockPublicAccess




BlockPublicAccess

	

Boolean

	

true

	

Indicates whether Block Public Access is enabled for the Object FC Access Point.

true: Block Public Access is enabled.

false: Block Public Access is disabled.

Parent nodes: PublicAccessBlockConfiguration

Child nodes: none

Examples

Sample request

 
GET /?accessPointForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 870
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointForObjectProcessResult>
  <AccessPointNameForObjectProcess>fc-ap-01</AccessPointNameForObjectProcess>
  <AccessPointForObjectProcessAlias>fc-ap-01-3b00521f653d2b3223680ec39dbbe2****-opapalias</AccessPointForObjectProcessAlias>
  <AccessPointName>ap-01</AccessPointName>
  <AccountId>111933544165****</AccountId>
  <AccessPointForObjectProcessArn>acs:oss:cn-qingdao:11933544165****:accesspointforobjectprocess/fc-ap-01</AccessPointForObjectProcessArn>
  <CreationDate>1626769503</CreationDate>
  <Status>enable</Status>
  <Endpoints>
    <PublicEndpoint>fc-ap-01-111933544165****.oss-cn-qingdao.oss-object-process.aliyuncs.com</PublicEndpoint>
    <InternalEndpoint>fc-ap-01-111933544165****.oss-cn-qingdao-internal.oss-object-process.aliyuncs.com</InternalEndpoint>
  </Endpoints>
  <PublicAccessBlockConfiguration>
    <BlockPublicAccess>true</BlockPublicAccess>
  </PublicAccessBlockConfiguration>
</GetAccessPointForObjectProcessResult>