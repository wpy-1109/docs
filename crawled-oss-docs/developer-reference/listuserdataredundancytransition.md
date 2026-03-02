# ListUserDataRedundancyTransition

Lists all redundancy type change tasks of a requester.

## Usage notes


-

To list all redundancy type change tasks of a requester, you must have the `oss:ListUserDataRedundancyTransition` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

## Request syntax


`http
GET /?redundancyTransition&continuation-token=xxx&max-keys=10 HTTP.1
Host: oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a ListUserDataRedundancyTransition request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request parameters

















| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| continuation-token | String | No | abc | The token from which the list operation must start. |
| max-keys | Integer | No | 10 | The maximum number of redundancy type change tasks that can be returned. Valid values: 1 to 100. |


## Response headers


All headers in the response to a ListUserDataRedundancyTransition request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


-


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| ListBucketDataRedundancyTransition | Container | N/A | The container in which the listed redundancy type change tasks are stored. Parent nodes: noneChild nodes: BucketDataRedundancyTransition, IsTruncated, and NextContinuationToken |
| BucketDataRedundancyTransition | Container | N/A | The container in which the redundancy type change task is stored. Parent nodes: ListBucketDataRedundancyTransitionChild nodes: TaskId, CreateTime, StartTime, EndTime, Status, EstimatedRemainingTime, and ProcessPercentage |
| TaskId | String | 4be5beb0f74f490186311b268bf6j | The ID of the redundancy type change task. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| CreateTime | String | 2023-11-17T08:40:17.000Z | The time when the redundancy type change task was created. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| StartTime | String | 2023-11-17T10:40:17.000Z | The time when the redundancy type change task was performed. This element is available when the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| EndTime | String | N/A | The time when the redundancy type change task was finished. This element is available when the task is in the Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| Status | String | Processing | The state of the redundancy type change task. Valid values:Queueing Processing Finished Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| EstimatedRemainingTime | Integer | 16 | The estimated period of time that is required for the redundancy type change task. Unit: hours. This element is available when the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| ProcessPercentage | Integer | 50 | The progress of the redundancy type change task in percentage. This element is included in the response if the task is in the Processing or Finished state. Parent nodes: BucketDataRedundancyTransitionChild nodes: none |
| IsTruncated | Boolean | false | Indicates whether the returned results are truncated. Valid values:true: indicates that not all results are returned for the request. false: indicates that all results are returned for the request. Parent nodes: ListBucketDataRedundancyTransitionChild nodes: none |
| NextContinuationToken | String | N/A | Indicates that this ListUserDataRedundancyTransition request contains subsequent results. You must set NextContinuationToken to continuation-token to continue obtaining the results. Parent nodes: ListBucketDataRedundancyTransitionChild nodes: none |


## Examples


-

Sample request


`http
GET /?dataRedundancyTransition&continuation-token=abc&max-keys=10 HTTP/1.1
Host: examplebucket1.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
Date: Fri, 17 Nov 2023 08:40:17 GMT
Content-Type: application/xml
Content-Length: 437
Server: AliyunOSS
x-oss-request-id: 655726F18EAD9B710C00

<?xml version="1.0" encoding="UTF-8"?>
<ListBucketDataRedundancyTransition>
  <IsTruncated>false</IsTruncated>
  <NextContinuationToken></NextContinuationToken>
  <BucketDataRedundancyTransition>
    <Bucket>examplebucket1</Bucket>
    <TaskId>4be5beb0f74f490186311b268bf6</TaskId>
    <Status>Queueing</Status>
    <CreateTime>2023-11-17T08:40:17.000Z</CreateTime>
  </BucketDataRedundancyTransition>
  <BucketDataRedundancyTransition>
    <Bucket>examplebucket2</Bucket>
    <TaskId>4be5beb0f74f490186311b268bf6j</TaskId>
    <Status>Processing</Status>
    <CreateTime>2023-11-17T08:40:17.000Z</CreateTime>
    <StartTime>2023-11-17T10:40:17.000Z</StartTime>
    <ProcessPercentage>50</ProcessPercentage>
    <EstimatedRemainingTime>16</EstimatedRemainingTime>
  </BucketDataRedundancyTransition>
  <BucketDataRedundancyTransition>
    <Bucket>examplebucket3</Bucket>
    <TaskId>4be5beb0er4f490186311b268bf6j</TaskId>
    <Status>Finished</Status>
    <CreateTime>2023-11-17T08:40:17.000Z</CreateTime>
    <StartTime>2023-11-17T11:40:17.000Z</StartTime>
    <ProcessPercentage>100</ProcessPercentage>
    <EstimatedRemainingTime>0</EstimatedRemainingTime>
    <EndTime>2023-11-18T09:40:17.000Z</EndTime>
  </BucketDataRedundancyTransition>
  ...
</ListBucketDataRedundancyTransition>
`


Thank you! We've received your  feedback.