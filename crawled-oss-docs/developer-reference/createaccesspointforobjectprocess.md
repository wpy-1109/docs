# CreateAccessPointForObjectProcess

Creates an Object FC Access Point.

## Usage notes


-

By default, an Alibaba Cloud account has the permissions to create an Object FC Access Point. To create an Object FC Access Point by using a RAM user or Security Token Service (STS), you must have the `oss:CreateAccessPointForObjectProcess` permission.

-

You can create up to 1,000 Object FC Access Points for an Alibaba Cloud account.

-

You can create up to 100 Object FC Access Points for a bucket.

## Request syntax


`xml
PUT /?accessPointForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length: 785
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointForObjectProcessConfiguration>
  <AccessPointName>ap-01</AccessPointName>
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
</CreateAccessPointForObjectProcessConfiguration>
`


## Request headers


-


-



-


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-access-point-for-object-process-name | String | Yes | fc-ap-01 | The name of the Object FC Access Point. The name of an Object FC Access Point must meet the following requirements:The name cannot exceed 63 characters in length.The name can contain only lowercase letters, digits, and hyphens (-) and cannot start or end with a hyphen (-). The name must be unique in the current region. |


For more information about other common request headers included in a CreateAccessPointForObjectProcess request, such as Host and Date, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


(https://www.alibabacloud.com/help/en/oss/create-access-point)


(https://www.alibabacloud.com/help/en/functioncompute/fc-2-0/create-a-function-in-the-function-compute-console)


(https://www.alibabacloud.com/help/en/functioncompute/fc-2-0/user-guide/manage-functions#section-ilq-rae-ceg)


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| CreateAccessPointForObjectProcessConfiguration | Container | Yes | N/A | The container that stores information about the Object FC Access Point. Parent nodes: noneChild nodes: AccessPointName and ObjectProcessConfiguration |
| AccessPointName | String | Yes | ap-01 | The name of the Object FC Access Point. For more information, see Create Object FC Access Points. |
| ObjectProcessConfiguration | Container | No | N/A | The container that stores the processing information about the Object FC Access Point. Parent nodes: CreateAccessPointForObjectProcessConfigurationChild nodes: AllowedFeature and TransformationConfigurations |
| AllowedFeatures | Container | No | N/A | The container that stores allowed features. Parent nodes: ObjectProcessConfigurationChild nodes: AllowedFeature |
| AllowedFeature | String | No | GetObject-Range | Specifies that Function Compute supports Range GetObject requests. Parent nodes: AllowedFeaturesChild nodes: none |
| TransformationConfigurations | Container | No | N/A | The container that stores the transformation configurations. Parent nodes: ObjectProcessConfigurationChild nodes: TransformationConfiguration |
| TransformationConfiguration | Container | No | N/A | The container that stores the transformation configurations. Parent nodes: TransformationConfigurationsChild nodes: Actions and ContentTransformation |
| Actions | Container | No | N/A | The container that stores the operations. Parent nodes: TransformationConfigurationChild nodes: Action |
| Action | String | No | GetObject | The supported OSS API operations. Only the GetObject operation is supported. Parent nodes: ActionsChild nodes: none |
| ContentTransformation | Container | No | N/A | The container that stores the content of the transformation configurations. Parent nodes: TransformationConfigurationChild nodes: FunctionCompute |
| FunctionCompute | Container | No | N/A | The container that stores the information about Function Compute. Parent nodes: ContentTransformationChild nodes: FunctionAssumeRoleArn and FunctionArn |
| FunctionAssumeRoleArn | String | No | acs:ram::111933544165:role/aliyunfcdefaultrole | The Alibaba Cloud Resource Name (ARN) of the role that Function Compute uses to access your resources in other cloud services. The default role is AliyunFCDefaultRole. For more information, see Quickly create a function. Parent nodes: FunctionComputeChild nodes: none |
| FunctionArn | String | No | acs:fc:cn-qingdao:111933544165:services/test-oss-fc.LATEST/functions/fc-01 | The ARN of the function. For more information, see Obtain the ARN of a function. |


## Response headers


The response to a CreateAccessPointForObjectProcess request contains only common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














| Element | Type | Example | Description |
| --- | --- | --- | --- |
| CreateAccessPointForObjectProcessResult | Container | N/A | The container that stores information about the Object FC Access Point. Child nodes: AccessPointForObjectProcessArn and Alias |
| AccessPointForObjectProcessArn | String | acs:oss:cn-qingdao:119335441657143:accesspointforobjectprocess/fc-ap-01 | The ARN of the Object FC Access Point. |
| AccessPointForObjectProcessAlias | String | fc-ap-01-3b00521f653d2b3223680ec39dbbe2-opapalias | The alias of the Object FC Access Point. |


## Examples


-

Sample request


`xml
PUT /?accessPointForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 785
Content-Type: application/xml
Host: oss-example.oss-cn-qingdao.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointForObjectProcessConfiguration>
  <AccessPointName>ap-01</AccessPointName>
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
            <FunctionAssumeRoleArn>acs:ram::111933544165:role/aliyunfcdefaultrole</FunctionAssumeRoleArn>
            <FunctionArn>acs:fc:cn-qingdao:111933544165:services/test-oss-fc.LATEST/functions/fc-01</FunctionArn>
          </FunctionCompute>
        </ContentTransformation>
      </TransformationConfiguration>
    </TransformationConfigurations>
  </ObjectProcessConfiguration>
</CreateAccessPointForObjectProcessConfiguration>
`


-

Sample response


`xml
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D
Date: Mon, 30 Oct 2023 03:15:40 GMT
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointForObjectProcessResult>
  <AccessPointForObjectProcessArn>acs:oss:cn-qingdao:119335441657143:accesspointforobjectprocess/fc-ap-01</AccessPointForObjectProcessArn>
  <AccessPointForObjectProcessAlias>fc-ap-01-3b00521f653d2b3223680ec39dbbe2-opapalias</AccessPointForObjectProcessAlias>
</CreateAccessPointForObjectProcessResult>

`


Thank you! We've received your  feedback.