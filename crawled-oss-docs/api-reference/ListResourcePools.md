# ListResourcePools

Invoke ListResourcePools to retrieve details about all resource pools associated with the current Alibaba Cloud account, including names and creation times.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account is authorized to access information about all resource pools under the account. To access this information via a RAM user or Security Token Service (STS), you must have the oss:ListResourcePools permission. For detailed instructions, see RAM policy examples.

Request syntax
 
GET /?resourcePool&max-keys=10&continuation-token=abcd
Host: oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

This operation only requires common request headers and does not need specific ones. For more information, see Common request headers.

Request elements

Name

	

Type

	

Required

	

Example value

	

Description




max-keys

	

Integer

	

No

	

10

	

The maximum number of resource pool information entries returned this time.




continuation-token

	

String

	

No

	

abcd

	

The resource pool from which information starts to be returned.

Response headers

This operation only requires common response headers and does not need specific ones. For more information, see Common response headers.

Response elements

Name

	

Type

	

Example value

	

Description




ListResourcePoolsResult

	

Container

	

N/A

	

The container that stores the result of the request.

Parent nodes: none




Region

	

String

	

oss-cn-hangzhou

	

The region where the resource pool is located.

Parent nodes: ListResourcePoolsResult




Owner

	

String

	

103xxxx

	

The unique identifier (UID) of the account to which the resource pool belongs.

Parent nodes: ListResourcePoolsResult




ContinuationToken

	

String

	

abcd

	

The continuationToken that is used in this ListResourcePools request.

Parent nodes: ListResourcePoolsResult




NextContinuationToken

	

String

	

xyz

	

Indicates that this ListResourcePools request contains subsequent results. The value of NextContinuationToken is used as the value of ContinuationToken to query subsequent results.

Parent nodes: ListResourcePoolsResult




IsTruncated

	

Boolean value

	

true

	

Indicates whether the queried results are truncated.

true indicates that not all results are returned this time.

false indicates that all results are returned this time.

Parent nodes: ListResourcePoolsResult




ResourcePool

	

Container

	

N/A

	

The container that stores the result of the resource pool list.

Parent nodes: ListResourcePoolsResult




Name

	

String

	

resource-pool-for-ai

	

The name of the resource group.

Parent nodes: ResourcePool




CreateTime

	

String

	

2024-11-29T08:42:32.000Z

	

The time when the resource pool was created. The time follows the ISO 8601 standard.

Parent nodes: ResourcePool

Examples

Query Example

 
GET /?resourcePool&max-keys=10&continuation-token=abcd
Host: oss-cn-hangzhou.aliyuncs.com
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample Success Response

 
HTTP/1.1 200 OK
Date: Fri, 27 Dec 2024 03:21:12 GMT
Content-Length: 655
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<ListResourcePoolsResult>
  <Region>oss-cn-hangzhou</Region>
  <Owner>103xxxx</Owner>
  <ContinuationToken>abcd</ContinuationToken>
  <NextContinuationToken>xyz</NextContinuationToken>
  <IsTruncated>true</IsTruncated>
  <ResourcePool>
    <Name>resource-pool-for-ai</Name>
    <CreateTime>2024-11-29T08:42:32.000Z</CreateTime>
  </ResourcePool>
  <ResourcePool>
    <Name>resource-pool-for-video</Name>
    <CreateTime>2024-11-29T08:42:32.000Z</CreateTime>
  </ResourcePool>
  <ResourcePool>
    <Name>resource-pool-for-datalake</Name>
    <CreateTime>2024-11-29T08:42:32.000Z</CreateTime>
  </ResourcePool>
</ListResourcePoolsResult>
SDK

You can use OSS SDKs for the following programming languages to call ListResourcePools:

Python V2

Go V2

Command line tool ossutil

For the ossutil command corresponding to the ListResourcePools operation, see list-resource-pools.