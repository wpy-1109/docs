# Query information about an access point by calling the GetAccessPoint operation

Queries information about an access point.

## Usage notes


By default, an Alibaba Cloud account has the permissions to query information about an access point. To query information about an access point by using a RAM user or Security Token Service (STS), you must have the `oss:GetAccessPoint` permission.

## Request syntax


`plaintext
GET /?accessPoint HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: ContentType
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: apname
Authorization: SignatureValue
`


## Request headers


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-access-point-name | String | Yes | ap-01 | The name of the access point. |


This request contains other common request headers, such as Date and Authorization. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a GetAccessPoint request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


-


-


-


-


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| GetAccessPointResult | Container | N/A | The container that stores the information about the access point. Parent nodes: noneChild nodes: AccessPointName, Bucket, AccountId, NetworkOrigin, VpcConfiguration, AccessPointArn, CreationDate, Alias, Status, and Endpoints |
| AccessPointName | String | ap-01 | The name of the access point. Parent nodes: GetAccessPointResultChild nodes: none |
| Bucket | String | oss-example | The name of the bucket for which the access point is configured. Parent nodes: GetAccessPointResultChild nodes: none |
| AccountId | String | 111933544165xxxx | The ID of the Alibaba Cloud account for which the access point is configured. Parent nodes: GetAccessPointResultChild nodes: none |
| NetworkOrigin | String | vpc | The network origin of the access point. Valid values:vpc: You can use a specific virtual private cloud (VPC) ID to access the access point. internet: You can use public and internal endpoints to access the access point. Parent nodes: GetAccessPointResultChild nodes: none |
| VpcConfiguration | Container | N/A | The container that stores the information about the VPC. Parent nodes: GetAccessPointResultChild nodes: VpcId |
| VpcId | String | vpc-t4nlw426y44rd3iq4xxxx | The ID of the VPC. Parent nodes: VpcConfigurationChild nodes: none |
| AccessPointArn | String | arn:acs:oss:cn-hangzhou:111933544165xxxx:accesspoint/ap-01 | The Alibaba Cloud Resource Name (ARN) of the access point. Parent nodes: GetAccessPointResultChild nodes: none |
| CreationDate | String | 1626769503 | The time when the access point was created. The value is a timestamp. Parent nodes: GetAccessPointResultChild nodes: none |
| Alias | String | ap-01-ossalias | The alias of the access point. Parent nodes: GetAccessPointResultChild nodes: none |
| Status |  | enable | The status of the access point. Valid values:enable: The access point is created. disable: The access point is disabled. creating: The access point is being created. deleting: The access point is deleted. Parent nodes: GetAccessPointResultChild nodes: none |
| Endpoints | Container | N/A | The container that stores the network origin information about the access point. Parent nodes: GetAccessPointResultChild nodes: PublicEndpoint and InternalEndpoint |
| PublicEndpoint | String | ap-01.oss-cn-hangzhou.oss-accesspoint.aliyuncs.com | The public endpoint of the access point. Parent nodes: EndpointsChild nodes: none |
| InternalEndpoint | String | ap-01.oss-cn-hangzhou-internal.oss-accesspoint.aliyuncs.com | The internal endpoint of the access point. Parent nodes: EndpointsChild nodes: none |
| PublicAccessBlockConfiguration | Container | N/A | The container that stores the Block Public Access configurations. Parent nodes: GetAccessPointResultChild nodes: BlockPublicAccess |
| BlockPublicAccess | Boolean | true | Indicates whether Block Public Access is enabled for the access point. true: Block Public Access is enabled. false: Block Public Access is disabled. Parent nodes: PublicAccessBlockConfigurationChild nodes: none |


## Examples


-

Sample request


`plaintext
GET /?accessPoint HTTP/1.1
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 10
Content-Type: application/xml
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: ap-01
Authorization: OSS qn6q:77Dv
`


-

Sample success response


`plaintext
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointResult>
  <AccessPointName>ap-01</AccessPointName>
  <Bucket>oss-example</Bucket>
  <AccountId>111933544165xxxx</AccountId>
  <NetworkOrigin>vpc</NetworkOrigin>
  <VpcConfiguration>
     <VpcId>vpc-t4nlw426y44rd3iq4xxxx</VpcId>
  </VpcConfiguration>
  <AccessPointArn>arn:acs:oss:cn-hangzhou:111933544165xxxx:accesspoint/ap-01</AccessPointArn>
  <CreationDate>1626769503</CreationDate>
  <Alias>ap-01-ossalias</Alias>
  <Status>enable</Status>
  <Endpoints>
    <PublicEndpoint>ap-01.oss-cn-hangzhou.oss-accesspoint.aliyuncs.com</PublicEndpoint>
    <InternalEndpoint>ap-01.oss-cn-hangzhou-internal.oss-accesspoint.aliyuncs.com</InternalEndpoint>
  </Endpoints>
  <PublicAccessBlockConfiguration>
    <BlockPublicAccess>true</BlockPublicAccess>
  </PublicAccessBlockConfiguration>
</GetAccessPointResult>
`


## ossutil


For information about the ossutil command that corresponds to the GetAccessPoint operation, see [get-access-point](https://www.alibabacloud.com/help/en/oss/developer-reference/get-access-point).

Thank you! We've received your  feedback.