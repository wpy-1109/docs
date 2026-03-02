# ListResourcePoolBucketGroups

The ListResourcePoolBucketGroups operation lists bucket groups in the specified resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has full permissions on resources in the account. If you want to perform the operation as a RAM user or by using a RAM role, ask the owner of the Alibaba Cloud account or the administrator to grant you the oss:ListResourcePoolBucketGroups permission by using a RAM policy or bucket policy.

Request syntax
 
GET /?resourcePoolBucketGroup&resourcePool=ResourcePoolName&continuation-token=abc&max-keys=2
Host: oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

This operation requires only common request headers. For more information, see Common HTTP headers.

Request elements

Name

	

Type

	

Required

	

Example

	

Description




resourcePool

	

string

	

Yes

	

resource-pool-for-ai

	

The name of the resource pool.




max-keys

	

Integer

	

No

	

2

	

The maximum number of buckets to return from the resource pool.




continuation-token

	

string

	

No

	

abc

	

The token from which the list operation starts.

Response headers

This operation returns only common response headers. For more information, see Common response headers.

Response elements

Name

	

Type

	

Example

	

Description




ListResourcePoolBucketGroupsResult

	

container

	

N/A

	

The container that stores the result of the request.

Parent node: none




ResourcePool

	

string

	

resource-pool-for-ai

	

The name of the resource pool.

Parent node: ListResourcePoolBucketGroupsResult




ContinuationToken

	

string

	

abcd

	

The continuationToken that was used in this ListResourcePoolBucketGroups request.

Parent node: ListResourcePoolBucketGroupsResult




NextContinuationToken

	

string

	

defg

	

Indicates that this ListResourcePoolBucketGroups request contains subsequent results. The value of NextContinuationToken can be used as the value of ContinuationToken in another ListResourcePoolBucketGroups request to query subsequent entries.

Parent node: ListResourcePoolBucketGroupsResult




IsTruncated

	

Boolean

	

true

	

Indicates whether the result is truncated.

true: indicates that not all entries are returned this time.

false: indicates that all entries are returned this time.

Parent node: ListResourcePoolBucketGroupsResult




ResourcePoolBucketGroup

	

container

	

N/A

	

The container that stores information about the bucket group.

Parent node: ListResourcePoolBucketGroupsResult




Name

	

string

	

test-group

	

The name of the bucket group.

Parent node: ResourcePoolBucketGroup




GroupBucketInfo

	

container

	

N/A

	

The information about the bucket group.

Parent node: ResourcePoolBucketGroup




BucketName

	

string

	

examplebucket

	

The name of the bucket.

Parent node: GroupBucketInfo

Examples

Sample request

 
GET /?resourcePoolBucketGroup&resourcePool=resource-pool-for-ai&continuation-token=abc&maxKeys=2
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Authorization: SignatureValue

Sample response

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 5678
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<ListResourcePoolBucketGroupsResult>
  <ResourcePool>rp-for-ai</ResourcePool>
  <ContinuationToken>abcd</ContinuationToken>
  <NextContinuationToken>defg</NextContinuationToken>
  <IsTruncated>true</IsTruncated>
  <ResourcePoolBucketGroup>
    <Name>test-group<Name/>
    <GroupBucketInfo>
      <BucketName>bucket-01</BucketName>
    <GroupBucketInfo>
    <GroupBucketInfo>
      <BucketName>bucket-02</BucketName>
    <GroupBucketInfo>
  </ResourcePoolBucketGroup>
</ListResourcePoolBucketGroupsResult>
SDKs

The following OSS SDKs encapsulate the ListResourcePoolBucketGroups operation to simplify usage:

Python V2

Go V2