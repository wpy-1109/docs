# GetAccessPointConfigForObjectProcess

Queries the configurations of an Object FC Access Point.

Usage notes

By default, an Alibaba Cloud account has the permissions to query the configurations of an Object FC Access Point. To query the configurations of an Object FC Access Point by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the oss:GetAccessPointConfigForObjectProcess permission.

Request syntax
 
GET /?accessPointConfigForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
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

For more information about other common request headers included in a GetAccessPointConfigForObjectProcess request, such as Host and Date, see Common request headers.

Response headers

The response to a GetAccessPointConfigForObjectProcess request contains only common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




GetAccessPointConfigForObjectProcessResult

	

Container

	

N/A

	

The container that stores the configurations of the Object FC Access Point.




ObjectProcessConfiguration

	

Container

	

N/A

	

The container that stores the processing information about the Object FC Access Point.




AllowedFeatures

	

Container

	

N/A

	

The container that stores allowed features.




TransformationConfigurations

	

Container

	

N/A

	

The container that stores the transformation configurations.




TransformationConfiguration

	

Container

	

N/A

	

The container that stores the transformation configurations.




Actions

	

Container

	

N/A

	

The container that stores the operations.




Action

	

String

	

GetObject

	

The supported OSS API operations. Only the GetObject operation is supported.




ContentTransformation

	

Container

	

N/A

	

The container that stores the content of the transformation configurations.




FunctionCompute

	

Container

	

N/A

	

The container that stores information about Function Compute.




FunctionAssumeRoleArn

	

String

	

acs:ram::111933544165****:role/aliyunossobjectfcforossdefaultrole

	

The Alibaba Cloud Resource Name (ARN) of the role used for accessing and managing your Function Compute resources.




FunctionArn

	

String

	

acs:oss:cn-qingdao:111933544165****:services/oss-fc.LATEST/functions/oss-fc-fc-02

	

The ARN of the function.




PublicAccessBlockConfiguration

	

Container

	

N/A

	

The container in which the Block Public Access configurations are stored.

Parent nodes: PutAccessPointConfigForObjectProcessConfiguration

Child nodes: BlockPublicAccess




BlockPublicAccess

	

Boolean

	

true

	

Indicates whether Block Public Access is enabled for the Object FC Access Point.

true: Block Public Access is enabled.

false (default): Block Public Access is disabled.

Examples

Sample request

 
GET /?accessPointConfigForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetAccessPointConfigForObjectProcessResult>
  <ObjectProcessConfiguration>
    <AllowedFeatures/>
    <TransformationConfigurations>
      <TransformationConfiguration>
        <Actions>
          <Action>getobject</Action>
        </Actions>
        <ContentTransformation>
          <FunctionCompute>
            <FunctionAssumeRoleArn>acs:ram::111933544165****:role/aliyunossobjectfcforossdefaultrole</FunctionAssumeRoleArn>
            <FunctionArn>acs:oss:cn-qingdao:111933544165****:services/oss-fc.LATEST/functions/oss-fc-02</FunctionArn>
          </FunctionCompute>
        </ContentTransformation>
      </TransformationConfiguration>
    </TransformationConfigurations>
  </ObjectProcessConfiguration>
  <PublicAccessBlockConfiguration>
    <BlockPublicAccess>true</BlockPublicAccess>
  </PublicAccessBlockConfiguration> 
</GetAccessPointConfigForObjectProcessResult>