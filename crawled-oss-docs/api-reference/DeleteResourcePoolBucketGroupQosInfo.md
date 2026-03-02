# DeleteResourcePoolBucketGroupQoSInfo

Call DeleteResourcePoolBucketGroupQoSInfo to delete the throttling configuration of a bucket group in a resource pool.

Usage notes

Resource pool QoS is in invitational preview. If the throughput of your OSS buckets in a region has reached or exceeded 500 Gbit/s, you can contact technical support to apply for this feature.

By default, an Alibaba Cloud account has full permissions on resources in the account. If you want to delete a resource as a RAM user or by using a RAM role, the Alibaba Cloud account or an administrator must grant the oss:DeleteResourcePoolBucketGroupQoSInfo permission by using a RAM Policy or a bucket policy.

Syntax
 
DELETE /?resourcePoolBucketGroupQosInfo&resourcePool=resource-pool-for-ai&resourcePoolBucketGroup=test-group
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 0
Authorization: SignatureValue
Request headers

All headers in a DeleteResourcePoolBucketGroupQoSInfo request are common request headers. For more information, see Common Request Headers.

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




resourcePoolBucketGroup

	

string

	

Yes

	

test-group

	

The name of the bucket group in the resource pool.

Response headers

All headers in the response to a DeleteResourcePoolBucketGroupQoSInfo request are common response headers. For more information, see Common Response Headers.

Examples

Sample request

 
DELETE /?resourcePoolBucketGroupQosInfo&resourcePool=resource-pool-for-ai&resourcePoolBucketGroup=test-group
Host: oss-cn-shanghai.aliyuncs.com
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 0
Authorization: SignatureValue

Sample response

 
HTTP/1.1 204 No Content 
Date: Sun, 11 Aug 2024 17:45:00 GMT
Content-Length: 0
OSS SDKs

The following SDKs for different programming languages are available for the DeleteResourcePoolBucketGroupQoSInfo operation:

Python V2

Go V2