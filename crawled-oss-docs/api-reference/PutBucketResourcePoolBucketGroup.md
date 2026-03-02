# PutBucketResourcePoolBucketGroup

You can call PutBucketResourcePoolBucketGroup to add a bucket within a resource pool to a bucket group.

Notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has full permissions on resources in the account. To configure as a RAM user or a RAM role, the oss:PutBucketResourcePoolBucketGroup permission granted using the RAM Policy or Bucket Policy is required.

This operation is available only for adding buckets within a resource pool to a bucket group. You cannot add buckets that are not in a resource pool to a bucket group.

Request syntax
 
PUT /?reourcePool=<resourcePoolName>&resourcePoolBucketGroup=<resourcePoolBucketGroupName>
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a PutBucketResourcePoolBucketGroup request are common request headers. For more information, see Common Request Headers.

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

	

Name of the resource pool.




resourcePoolBucketGroup

	

string

	

No

	

test-group

	

Name of the bucket group to which the bucket within the resource pool is added. If the parameter is empty, it indicates that the bucket is removed from the bucket group.




BucketName

	

string

	

Yes

	

examplebucket

	

Name of the bucket to be added to the resource pool.

Response headers

All headers in the response to a PutBucketResourcePoolBucketGroup request are common response headers. For more information, see Common Response Headers.

Example

Sample request

 
PUT /?resourcePool=resource-pool-for-ai&resourcePoolBucketGroup=test-group
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Authorization: SignatureValue

Sample response

 
HTTP/1.1 200 OK
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 0
OSS SDKs

You can use OSS SDKs for the following programming languages to call PutBucketResourcePoolBucketGroup:

Python V2

Go V2