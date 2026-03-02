# Create an access point by calling the CreateAccessPoint operation

Creates an access point.

## Usage notes


-

By default, an Alibaba Cloud account has the permissions to create an access point. To create an access point by using a RAM user or Security Token Service (STS), you must have the `oss:CreateAccessPoint` permission.

-

You can create up to 1,000 access points for an Alibaba Cloud account.

-

You can create up to 100 access points for a bucket.

## Request syntax


`plaintext
PUT /?accessPoint HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointConfiguration>
  	<AccessPointName>ap-01</AccessPointName>
    <NetworkOrigin>vpc</NetworkOrigin>
    <VpcConfiguration>
      <VpcId>vpc-t4nlw426y44rd3iq4xxxx</VpcId>
    </VpcConfiguration>
</CreateAccessPointConfiguration>
`


## Request headers


All headers in a CreateAccessPoint request are common request headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


-


-


-


-


-


-


> IMPORTANT:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/oss-supported-gateway-endpoint-regions)


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| CreateAccessPointConfiguration | Container | Yes | N/A | The container that stores the information about the access point. Parent nodes: noneChild nodes: AccessPointName, NetworkOrigin, and VpcConfiguration |
| AccessPointName | String | Yes | ap-01 | The name of the access point. The name of the access point must meet the following requirements:The name must be unique in a region of your Alibaba Cloud account. The name cannot end with -ossalias. The name can contain only lowercase letters, digits, and hyphens (-). It cannot start or end with a hyphen (-). The name must be 3 to 19 characters in length. Parent nodes: CreateAccessPointConfigurationChild nodes: none |
| NetworkOrigin | String | Yes | vpc | The network origin of the access point. Valid values:vpc: You can use a specific virtual private cloud (VPC) ID to access the access point. internet: You can use public endpoints and internal endpoints to access the access point. Parent nodes: CreateAccessPointConfigurationChild nodes: none |
| VpcConfiguration | Container | No | N/A | The container that stores the information about the VPC. Parent nodes: CreateAccessPointConfigurationChild nodes: VpcId |
| VpcId | String | No | vpc-t4nlw426y44rd3iq4xxxx | The ID of the VPC. The VPC ID is required only if you set the NetworkOrigin parameter to vpc. Important When you use an access point to restrict the VPC, make sure that the region of the VPC matches the region of the gateway endpoint supported by OSS. Otherwise, authentication requests cannot be associated with the corresponding VPC, which leads to authentication failures. For more information, see Regions of gateway endpoints supported by OSS. Parent nodes: VpcIdChild nodes: none |


## Response headers


The response to a CreateAccessPoint request contains only common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| CreateAccessPointResult | Container | N/A | The container that stores the information about the access point. Child nodes: AccessPointArn and Alias |
| AccessPointArn | String | acs:oss:cn-hangzhou:128364106451xxxx:accesspoint/ap-01 | The Alibaba Cloud Resource Name (ARN) of the access point. |
| Alias | String | ap-01-45ee7945007a2f0bcb595f63e2215cxxxx-ossalias | The alias of the access point. |


## Examples


-

Sample requests


`plaintext
PUT /?accessPoint HTTP/1.1
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q:77Dv
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointConfiguration>
  	<AccessPointName>ap-01</AccessPointName>
    <NetworkOrigin>vpc</NetworkOrigin>
    <VpcConfiguration>
      <VpcId>vpc-t4nlw426y44rd3iq4xxxx</VpcId>
    </VpcConfiguration>
</CreateAccessPointConfiguration>
`


-

Sample success responses


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2Dxxxx
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointResult>
  <AccessPointArn>acs:oss:cn-hangzhou:128364106451xxxx:accesspoint/ap-01</AccessPointArn>
  <Alias>ap-01-45ee7945007a2f0bcb595f63e2215cxxxx-ossalias</Alias>
</CreateAccessPointResult>
`


## ossutil


For information about the ossutil command that corresponds to the CreateAccessPoint operation, see [create-access-point](https://www.alibabacloud.com/help/en/oss/developer-reference/create-access-point).

Thank you! We've received your  feedback.