# Configure a resource group to which a bucket belongs.

You can use resource groups to manage resources. You can group the buckets to which you want to grant the same permissions to the same resource group and then grant permissions to the resource group. This improves the efficiency of authorization. This topic describes how to call the PutBucketResourceGroup operation to configure a resource group to which a bucket belongs.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).














| API | Action | Definition |
| --- | --- | --- |
| PutBucketResourceGroup | oss:PutBucketResourceGroup | Configures a resource group for a bucket. |


## Request syntax


`xml
PUT /?resourceGroup
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<BucketResourceGroupConfiguration>
  <ResourceGroupId>rg-aekz</ResourceGroupId>
</BucketResourceGroupConfiguration>
`


## Request headers


The request headers in a PutBucketResourceGroup request are only common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements

















| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| BucketResourceGroupConfiguration | Container | Yes | N/A | The container that stores the ID of the resource group. Child nodes: ResourceGroupId |
| ResourceGroupId | String | Yes | rg-aekz | The ID of the resource group to which the bucket belongs. If this element is not specified, the bucket is moved to the default resource group. Parent nodes: BucketResourceGroupConfiguration |


## Response headers


The response to a PutBucketResourceGroup request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Sample request


`xml
PUT /?resourceGroup
Content-Length: 0
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 01:33:47 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218
<?xml version="1.0" encoding="UTF-8"?>
<BucketResourceGroupConfiguration>
  <ResourceGroupId>rg-aekz</ResourceGroupId>
</BucketResourceGroupConfiguration>
`


Sample success response


`xml
HTTP/1.1 200 OK
x-oss-request-id: 5D3663FBB007B79097FC
Date: Sat, 8 May 2021 01:33:47 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call PutBucketResourceGroup:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-using-oss-sdk-for-csharp-v1)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/resource-group-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-resource-groups)

## ossutil


For information about the ossutil command that corresponds to the PutBucketResourceGroup operation, see [put-bucket-resource-group](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-resource-group).

## Error codes











-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | Possible causes:The information for user authentication is not imported when you initiate the request. You do not have the permissions to perform the operation. |
| ResourceGroupIdPreCheckError | 400 | The specified ID of the resource group is invalid or does not exist. The ID of the resource group fails the precheck. |


Thank you! We've received your  feedback.