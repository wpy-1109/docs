# PutAccessPointConfigForObjectProcess

Changes the configurations of an Object FC Access Point.

Notes

By default, an Alibaba Cloud account has the permissions to change the configurations of an Object FC Access Point. If you want to change the configurations of an Object FC Access Point as a RAM user or by using Security Token Service (STS), you must have the oss:PutAccessPointConfigForObjectProcess permission.

Request syntax
 
PUT /?accessPointConfigForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length：ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<PutAccessPointConfigForObjectProcessConfiguration>
  <ObjectProcessConfiguration>
    <AllowedFeatures>
      <AllowedFeature>GetObject-Range</AllowedFeature>
    </AllowedFeatures>
    <TransformationConfigurations>
      <TransformationConfiguration>
        <Actions>
          <Action>GetObject</Action>
        </Actions>
        <ContentTransformation>
          <FunctionCompute>
            <FunctionAssumeRoleArn>string</FunctionAssumeRoleArn>
            <FunctionArn>string</FunctionArn>
          </FunctionCompute>          
        </ContentTransformation>
      </TransformationConfiguration>
    </TransformationConfigurations>
  </ObjectProcessConfiguration>
  <PublicAccessBlockConfiguration>
    <BlockPublicAccess>true</BlockPublicAccess>
  </PublicAccessBlockConfiguration>
</PutAccessPointConfigForObjectProcessConfiguration>
Request headers

Name

	

Type

	

Required

	

Example

	

Description




x-oss-access-point-for-object-process-name

	

string

	

Yes

	

fc-ap-01

	

The name of the Object FC Access Point. The name of an Object FC Access Point must meet the following requirements:

The name cannot exceed 63 characters in length

The name can contain only lowercase letters, digits, and hyphens (-). The name cannot start or end with a hyphen.

The name must be unique in the current region.

For more information about other common request headers included in a PutAccessPointConfigForObjectProcess request, such as Host and Date, see Common HTTP headers.

Request elements

Name

	

Type

	

Required

	

Example

	

Description




PutAccessPointConfigForObjectProcessConfiguration

	

The container

	

Yes

	

None

	

The container that stores information about the Object FC Access Point.

Parent nodes: none

Child nodes: AccessPointName and ObjectProcessConfiguration




ObjectProcessConfiguration

	

The container

	

No

	

None

	

The container that stores the processing information about the Object FC Access Point.

Parent nodes: PutAccessPointConfigForObjectProcessConfiguration

Child nodes: AllowedFeature and TransformationConfigurations




AllowedFeatures

	

The container

	

No

	

None

	

The container that stores allowed features.

Parent nodes: ObjectProcessConfiguration

Child nodes: AllowedFeature




AllowedFeature

	

string

	

No

	

GetObject-Range

	

Specifies that Function Compute supports Range GetObject requests.

Parent nodes: AllowedFeatures

Child nodes: none




TransformationConfigurations

	

The container

	

No

	

None

	

The container that stores the transformation configurations.

Parent nodes: ObjectProcessConfiguration

Child nodes: TransformationConfiguration




TransformationConfiguration

	

The container

	

No

	

None

	

The container that stores the transformation configurations.

Parent nodes: TransformationConfigurations

Child nodes: Actions and ContentTransformation




Actions

	

The container

	

No

	

None

	

The container that stores the operations.

Parent nodes: TransformationConfiguration

Child nodes: Action




Action

	

string

	

No

	

GetObject

	

The supported OSS API operations. Only the GetObject operation is supported.

Parent nodes: Actions

Child nodes: none




ContentTransformation

	

The container

	

No

	

None

	

The container that stores the content of the transformation configurations.

Parent nodes: TransformationConfiguration

Child nodes: FunctionCompute




FunctionCompute

	

The container

	

No

	

None

	

The container that stores information about Function Compute.

Parent nodes: ContentTransformation

Child nodes: FunctionAssumeRoleArn and FunctionArn




FunctionAssumeRoleArn

	

string

	

No

	

acs:ram::111933544165****:role/aliyunossobjectfcforossdefaultrole

	

The Alibaba Cloud Resource Name (ARN) of the role that OSS uses to access or operate on your Function Compute resources. The default role is AliyunOSSObjectFcForOSSDefaultRole. For more information, see Create a function.

Parent nodes: FunctionCompute

Child nodes: none




FunctionArn

	

string

	

No

	

acs:oss:cn-qingdao:111933544165****:services/oss-fc.LATEST/functions/oss-fc-02

	

The Alibaba Cloud Resource Name (ARN) of another function that you want to associate to an Object FC Access Point. For more information, see Obtain the ARN of a function.

Parent nodes: FunctionCompute

Child nodes: none




PublicAccessBlockConfiguration

	

The container

	

Yes

	

None

	

The container that stores the Block Public Access configurations.

Parent nodes: PutAccessPointConfigForObjectProcessConfiguration

Child nodes: BlockPublicAccess




BlockPublicAccess

	

Boolean

	

No

	

true

	

Specifies whether to enable Block Public Access for the Object FC Access Point.

true: Block Public Access is enabled.

false (default): Block Public Access is disabled.

Parent nodes: PublicAccessBlockConfiguration

Child nodes: none

Response headers

The response to a PutAccessPointConfigForObjectProcess request contains only common response headers. For more information, see Common Response Headers.

Examples

Sample requests

 
PUT /?accessPointConfigForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length：750
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<PutAccessPointConfigForObjectProcessConfiguration>
  <ObjectProcessConfiguration>
    <AllowedFeatures>
      <AllowedFeature>GetObject-Range</AllowedFeature>
    </AllowedFeatures>
    <TransformationConfigurations>
      <TransformationConfiguration>
        <Actions>
          <Action>GetObject</Action>
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
</PutAccessPointConfigForObjectProcessConfiguration>

Sample command output:

 
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 30 Oct 2023 03:15:40 GMT