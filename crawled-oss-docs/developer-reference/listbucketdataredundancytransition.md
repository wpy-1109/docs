# ListBucketDataRedundancyTransition

Lists all redundancy type change tasks in an Object Storage Service (OSS) bucket.

## Usage notes


-

To list all redundancy type change tasks in a bucket, you must have the `oss:ListBucketDataRedundancyTransition` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

## Request syntax


`http
GET /?redundancyTransition HTTP/1.1
Host: bucketname.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a ListBucketDataRedundancyTransition request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a ListBucketDataRedundancyTransition request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| ListBucketDataRedundancyTransition | Container | N/A | The container for listed redundancy type change tasks. Parent nodes: noneChild nodes: BucketDataRedundancyTransition |
| BucketDataRedundancyTransition | Container | N/A | The container for a specific redundancy type change task. Parent nodes: ListBucketDataRedundancyTransitionChild nodes: TaskId, CreateTime, StartTime, EndTime, Status, EstimatedRemainingTime, and ProcessPercentage |
| TaskId | String | 4be5beb0f74f490186311b268bf6 | The ID of the redundancy change task. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| CreateTime | String | 2023-11-17T08:40:17.000Z | The time when the redundancy type change task was created. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| StartTime | String | N/A | The time when the redundancy type change task started. This element is included in the response if the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| EndTime | String | N/A | The time when the redundancy type change task was complete. This element is included in the response if the task is in the Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| Status | String | Queueing | The status of the redundancy type change task. Valid values:Queueing Processing Finished Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| EstimatedRemainingTime | Integer | N/A | The estimated remaining time of the redundancy type change task. This element is included in the response if the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| ProcessPercentage | Integer | N/A | The progress of the redundancy type change task in percentage. This element is included in the response if the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |


## Examples


-

Sample request


`http
GET /?redundancyTransition HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
Date: Fri, 17 Nov 2023 08:40:17 GMT
Content-Type: application/xml
Content-Length: 346
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300

<?xml version="1.0" encoding="UTF-8"?>
<ListBucketDataRedundancyTransition>
  <BucketDataRedundancyTransition>
    <Bucket>examplebucket</Bucket>
    <TaskId>4be5beb0f74f490186311b268bf6</TaskId>
    <Status>Queueing</Status>
    <CreateTime>2023-11-17T08:40:17.000Z</CreateTime>
  </BucketDataRedundancyTransition>
  ...
</ListBucketDataRedundancyTransition>
`


## ossutil


For information about the ossutil command that corresponds to the ListBucketDataRedundancyTransition operation, see [list-bucket-data-redundancy-transition](https://www.alibabacloud.com/help/en/oss/developer-reference/list-bucket-data-redundancy-transition).

Thank you! We've received your  feedback.