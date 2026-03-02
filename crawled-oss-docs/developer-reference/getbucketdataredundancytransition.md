# GetBucketDataRedundancyTransition

Queries redundancy type change tasks of a bucket.

## Usage notes


-

To query redundancy type change tasks of a bucket, you must have the `oss:GetBucketDataRedundancyTransition` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

## Request syntax


`http
GET /?redundancyTransition&x-oss-redundancy-transition-taskid=xxx HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a GetBucketDataRedundancyTransition request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request parameters

















| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-redundancy-transition-taskid | String | Yes | 751f5243f8ac4ae89f34726534d1 | The ID of the redundancy type change task. |


## Response headers


All headers in the response to a GetBucketDataRedundancyTransition request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| BucketDataRedundancyTransition | Container | N/A | The container in which the redundancy type change task is stored. Parent nodes: noneChild nodes: TaskId, CreateTime, StartTime, EndTime, Status, EstimatedRemainingTime, and ProcessPercentage |
| TaskId | String | 909c6c818dd041d1a44e0fdc66aa | The ID of the redundancy type change task. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| CreateTime | String | 2023-11-17T09:14:39.000Z | The time when the redundancy type change task was created. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| StartTime | String | 2023-11-17T09:14:39.000Z | The time when the redundancy type change task was performed. This element is available when the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| EndTime | String | N/A | The time when the redundancy type change task was finished. This element is available when the task is in the Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| Status | String | Processing | The state of the redundancy type change task. Valid values:Queueing Processing Finished Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| EstimatedRemainingTime | Integer | 100 | The estimated period of time that is required for the redundancy type change task. Unit: hours. This element is available when the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| ProcessPercentage | Integer | 0 | The progress of the redundancy type change task in percentage. Valid values: 0 to 100. This element is available when the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |


## Examples


-

Sample request


`http
GET /?redundancyTransition&x-oss-redundancy-transition-taskid=909c6c818dd041d1a44e0fdc66aa HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample responses


-

Sample response for a redundancy type change task in the Queueing state


`http
HTTP/1.1 200 OK
Server: AliyunOSS
x-oss-request-id: 655726F18EAD9B710C0
Date: Fri, 17 Nov 2023 08:40:17 GMT
Content-Type: application/xml
Content-Length: 216

<?xml version="1.0" encoding="UTF-8"?>
<BucketDataRedundancyTransition>
  <Bucket>examplebucket</Bucket>
  <TaskId>4be5beb0f74f490186311b268bf6</TaskId>
  <Status>Queueing</Status>
  <CreateTime>2023-11-17T09:11:58.000Z</CreateTime>
</BucketDataRedundancyTransition>
`


-

Sample response for a redundancy type change task in the Processing state


`http
HTTP/1.1 200 OK
Server: AliyunOSS
x-oss-request-id: 655726F18EAD9B710C00
Date: Fri, 17 Nov 2023 08:40:17 GMT
Content-type: application/xml
Content-length: 397

<?xml version="1.0" encoding="UTF-8"?>
<BucketDataRedundancyTransition>
  <Bucket>examplebucket</Bucket>
  <TaskId>909c6c818dd041d1a44e0fdc66aa</TaskId>
  <Status>Processing</Status>
  <CreateTime>2023-11-17T09:14:39.000Z</CreateTime>
  <StartTime>2023-11-17T09:14:39.000Z</StartTime>
  <ProcessPercentage>0</ProcessPercentage>
  <EstimatedRemainingTime>100</EstimatedRemainingTime>
</BucketDataRedundancyTransition>
`


-

Sample response for a redundancy type change task in the Finished state


`http
HTTP/1.1 200 OK
Server: AliyunOSS
x-oss-request-id: 655726F18EAD9B710C00
Date: Fri, 17 Nov 2023 08:40:17 GMT
Content-type: application/xml
Content-length: 420

<?xml version="1.0" encoding="UTF-8"?>
<BucketDataRedundancyTransition>
  <Bucket>examplebucket</Bucket>
  <TaskId>909c6c818dd041d1a44e0fdc66aa</TaskId>
  <Status>Finished</Status>
  <CreateTime>2023-11-17T09:14:39.000Z</CreateTime>
  <StartTime>2023-11-17T09:14:39.000Z</StartTime>
  <ProcessPercentage>100</ProcessPercentage>
  <EstimatedRemainingTime>0</EstimatedRemainingTime>
  <EndTime>2023-11-18T09:14:39.000Z</EndTime>
</BucketDataRedundancyTransition>
`


## ossutil


For information about the ossutil command that corresponds to the GetBucketDataRedundancyTransition operation, see [get-bucket-data-redundancy-transition](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-data-redundancy-transition).

## Error codes


| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The bucket whose redundancy type change tasks you want to query does not exist. |
| BucketDataRedundancyTransitionTaskNotExist | 404 | No redundancy type change tasks exist. |


Thank you! We've received your  feedback.