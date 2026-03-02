# ListResourcePoolBuckets

Use the ListResourcePoolBuckets operation to retrieve a list of buckets within a specified resource pool.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has permission to retrieve the list of buckets in a specified resource pool. To access this list through a RAM user or Security Token Service, you must have the oss:ListResourcePoolBuckets permission. For detailed instructions, see RAM policy common examples.

Request syntax
 
GET /?resourcePoolBuckets&resourcePool=ResourcePoolName&max-keys=2&continuation-token=abc
Host: oss-cn-shanghai.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

This operation uses only common request headers. For more information, see common request headers.

Request elements

Name

	

Type

	

Required

	

Example value

	

Description




resourcePool

	

String

	

Yes

	

resource-pool-for-ai

	

The name of the resource pool.




max-keys

	

Integer

	

No

	

10

	

The maximum number of buckets to return in this request.




continuation-token

	

String

	

No

	

rp-bucket-01

	

The bucket from which to start returning information.

Response headers

This operation uses only common response headers. For more information, see common response headers.

Response elements

Name

	

Type

	

Example value

	

Description




ListResourcePoolBucketsResult

	

Container

	

N/A

	

The container that stores the result of the request.

Parent nodes: none




ContinuationToken

	

String

	

abcd

	

The continuationToken that is used in this ListResourcePoolBuckets request.

Parent nodes: ListResourcePoolBucketsResult




NextContinuationToken

	

String

	

xyz

	

Indicates that this ListResourcePoolBuckets request contains subsequent results. The value of NextContinuationToken is used as the value of ContinuationToken to query subsequent results.

Parent nodes: ListResourcePoolBucketsResult




IsTruncated

	

Boolean value

	

true

	

Indicates whether the queried results are truncated.

true indicates that not all results are returned this time.

false indicates that all results are returned this time.

Parent nodes: ListResourcePoolBucketsResult




ResourcePoolBucket

	

Container

	

N/A

	

The container that stores the bucket list results in the resource pool.

Parent nodes: ListResourcePoolBucketsResult




Name

	

String

	

rp-bucket-01

	

The name of the bucket.

Parent nodes: ResourcePoolBucket




Group

	

String

	

test-group-1

	

The name of the bucket group.




JoinTime

	

String

	

2024-11-29T08:42:32.000Z

	

The time when the bucket joins the resource pool, in ISO8601 format.

Parent nodes: ResourcePoolBucket

Examples

Query example

 
GET /?resourcePoolBuckets&resourcePool=resource-pool-for-ai&continuation-token=abc&maxKeys=2
Host: oss-cn-hangzhou.aliyuncs.com
Date: Fri, 27 Dec 2024 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample success response

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 510
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<ListResourcePoolBucketsResult>
  <ResourcePool>resource-pool-for-ai</ResourcePool>
  <ContinuationToken>abcd</ContinuationToken>
  <NextContinuationToken>defg</NextContinuationToken>
  <IsTruncated>true</IsTruncated>
  <ResourcePoolBucket>
    <Name>rp-bucket-01</Name>
    <Group>test-group-1</Group>
    <JoinTime>2024-11-29T08:42:32.000Z</JoinTime>
  </ResourcePoolBucket>
  <ResourcePoolBucket>
    <Name>rp-bucket-02</Name>
    <Group>test-group-1</Group>
    <JoinTime>2024-11-29T08:42:32.000Z</JoinTime>
  </ResourcePoolBucket>
</ListResourcePoolBucketsResult>
OSS SDKs

You can use OSS SDKs for the following programming languages to call ListResourcePoolBuckets:

Python V2

Go V2

Command line tool ossutil

For the ossutil command corresponding to the ListResourcePoolBuckets operation, see list-resource-pool-buckets.