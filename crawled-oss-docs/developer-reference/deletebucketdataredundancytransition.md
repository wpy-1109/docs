# DeleteBucketDataRedundancyTransition

Deletes a redundancy type conversion task of a bucket.

## Usage notes


-

To delete a redundancy type conversion task of a bucket, you must have the `oss:DeleteBucketDataRedundancyTransition` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

-

Redundancy type conversion tasks in the Processing state cannot be deleted.

## Request syntax


`http
DELETE /?redundancyTransition&x-oss-redundancy-transition-taskid=xxx HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DeleteBucketDataRedundancyTransition request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request parameters


| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-redundancy-transition-taskid | String | Yes | 4be5beb0f74f490186311b268bf6 | The ID of the redundancy type conversion task. |


## Response headers


All headers in the response to a DeleteBucketDataRedundancyTransition request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`http
DELETE /?redundancyTransition&x-oss-redundancy-transition-taskid=4be5beb0f74f490186311b268bf6 HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 204 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 17 Nov 2023 08:40:17 GMT
Server: AliyunOSS
`


## ossutil


For information about the ossutil command that corresponds to the DeleteBucketDataRedundancyTransition operation, see [delete-bucket-data-redundancy-transition](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-bucket-data-redundancy-transition).

## Error codes


| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The bucket whose redundancy type conversion task you want to delete does not exist. |
| BucketDataRedundancyTransitionTaskNotExist | 404 | The redundancy type conversion task that you want to delete does not exist. |
| BucketDataRedundancyTransitionTaskStatusConflict | 409 | The redundancy type conversion task is in the Processing state and cannot be deleted. |


Thank you! We've received your  feedback.