# GetBucketResourceGroup

Queries the ID of the resource group to which a bucket belongs.

## Usage notes


By default, an Alibaba Cloud account has the permission to query the resource group of a bucket. To query the resource group of a bucket by using a RAM user or Security Token Service (STS), you must have the `oss:GetBucketResourceGroup` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request structure


`plaintext
GET /?resourceGroup
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


Request headers involved in this API operation contain only common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response headers involved in this API operation contain only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














| Element | Type | Example | Description |
| --- | --- | --- | --- |
| BucketResourceGroupConfiguration | Container | N/A | The container that contains the ID of the resource group. Child nodes: ResourceGroupId |
| ResourceGroupId | String | rg-aek27tc | The ID of the resource group to which the bucket belongs. If the bucket belongs to the default resource group, the returned resource group ID is rg-default-id. Parent nodes: BucketResourceGroupConfiguration |


## Examples


Sample requests


`plaintext
GET /?resourceGroup
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 07:51:28 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample responses


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Sat, 8 May 2021 07:51:28 GMT
Connection: keep-alive
Content-Length: 531
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<BucketResourceGroupConfiguration>
  <ResourceGroupId>rg-xxxxxx</ResourceGroupId>
</BucketResourceGroupConfiguration>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call GetBucketResourceGroup:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/resource-group-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-query-information-about-a-bucket#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-5)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-4)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/query-information-about-a-bucket)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-3)

-

[PHP](https://www.alibabacloud.com/help/en/oss/developer-reference/query-information-about-a-bucket-1)

-

[.Net](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-using-oss-sdk-for-csharp-v1#undefined)

## ossutil


For information about the ossutil command that corresponds to the GetBucketResourceGroup operation, see [get-bucket-resource-group](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-resource-group).

## Error codes











-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The error message returned because the requested bucket does not exist. |
| AccessDenied | 403 | Possible causes:The information for user authentication is not imported when you initiate the request. The error message returned because you are not authorized to perform the GetBucketResourceGroup operation. |


Thank you! We've received your  feedback.