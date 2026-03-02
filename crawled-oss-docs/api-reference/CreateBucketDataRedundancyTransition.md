# Redundancy type conversion

Creates a redundancy type conversion task for a bucket.

Usage notes

Make sure that redundancy type conversion is supported in the region where the bucket is located. This feature is supported in the following regions: China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), and Germany (Frankfurt).

The redundancy type of the bucket must be locally redundant storage (LRS). You can only convert the redundancy type of a bucket from LRS to zone-redundant storage (ZRS).

The storage class of the bucket must be Standard, Infrequent Access (IA), or Archive. However, the storage class of objects in the bucket can be Cold Archive or Deep Cold Archive. Cold Archive and Deep Cold Archive objects are still stored as LRS after the change. You cannot change the storage redundancy type of a Cold Archive or Deep Cold Archive bucket.

To create a redundancy type conversion task for a bucket, you must have the oss:CreateBucketDataRedundancyTransition permission. For more information, see Attach a custom policy to a RAM user.

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see Regions and endpoints.

Request syntax
 
POST /?redundancyTransition&x-oss-target-redundancy-type=ZRS HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a CreateBucketDataRedundancyTransition request are common request headers. For more information, see Common request headers.

Request parameters

Parameter

	

Type

	

Required

	

Example

	

Description




x-oss-target-redundancy-type

	

String

	

Yes

	

ZRS

	

The redundancy type to which you want to convert the bucket. You can only convert the redundancy type of a bucket from LRS to ZRS.

Response headers

All headers in the response to a CreateBucketDataRedundancyTransition request are common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




BucketDataRedundancyTransition

	

Container

	

N/A

	

The container in which the redundancy type conversion task is stored.

Parent nodes: none

Child nodes: TaskId




TaskId

	

String

	

4be5beb0f74f490186311b268bf6****

	

The ID of the redundancy type conversion task. The ID can be used to view and delete the redundancy type conversion task.

Parent nodes: BucketDataRedundancyTransition

Child nodes: none

Examples

Sample request

 
POST /?redundancyTransition&x-oss-target-redundancy-type=ZRS HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200
x-oss-request-id: 655726F18EAD9B710C00B235
Date: Fri, 17 Nov 2023 08:40:17 GMT
Content-Type: application/xml
Content-Length: 151
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<BucketDataRedundancyTransition>
  <TaskId>4be5beb0f74f490186311b268bf6****</TaskId>
</BucketDataRedundancyTransition>
ossutil

For information about the ossutil command that corresponds to the CreateBucketDataRedundancyTransition operation, see create-bucket-data-redundancy-transition.

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucket

	

404

	

The bucket for which the redundancy type conversion task is created does not exist.




BucketDataRedundancyTransitionTaskNotSupport

	

400

	

The redundancy type of the bucket cannot be converted. You can only convert the redundancy type of a bucket from LRS to ZRS.




BucketDataRedundancyTransitionTaskAlreadyExist

	

409

	

A redundancy type conversion task is in progress.




BucketDataRedundancyTransitionTaskExceedLimit

	

400

	

The maximum number of redundancy type conversion tasks has been reached. Delete the completed tasks before you create new tasks.