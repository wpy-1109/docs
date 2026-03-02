# Cancel the MultipartUpload event and delete the associated part data with AbortMultipartUpload

Cancels a multipart upload task and deletes the parts uploaded in the task.

## Notes


-

Upload ID


The upload ID of the multipart upload task is required to call the AbortMutipartUpload operation.

-

The parts that correspond to the upload ID not uploaded


After you call the AbortMutipartUpload operation, parts that are being uploaded are not deleted.

-

The parts that correspond to the upload ID uploaded


-

If the CompleteMutipartUpload operation is called, no parts or objects are deleted and the NoSuchUpload error code is reported after you call the AbortMutipartUpload operation. This is because no operations are allowed by using the upload ID of the multipart upload task after the CompleteMutipartUpload operation is called.

-

If the CompleteMutipartUpload operation is not called, only parts that are uploaded are deleted after you call the AbortMutipartUpload operation.

-

Storage fees


We recommend that you complete or cancel multipart upload tasks in a timely manner because parts that are uploaded by these tasks consume the storage capacity and incur storage fees.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).














| API | Action | Definition |
| --- | --- | --- |
| AbortMultipartUpload | oss:AbortMultipartUpload | Cancels a multipart upload task and deletes uploaded parts. |


## Request syntax


`plaintext
DELETE /ObjectName?uploadId=UploadId HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: Signature
`


## Request elements

















| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| uploadId | String | Yes | 0004B9895DBBB6E | The ID of the multipart upload task. |


For more information about other common request headers, such as Host and Date, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#reference-mhp-zdy-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`plaintext
Delete /multipart.data?&uploadId=0004B9895DBBB6E  HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 22 Feb 2012 08:32:21 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`plaintext
HTTP/1.1 204
Server: AliyunOSS
Content-length: 0
Connection: keep-alive
x-oss-request-id: 059a22ba-6ba9-daed-5f3a-e48027df
Date: Wed, 22 Feb 2012 08:32:21 GMT
x-oss-server-time: 86
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the AbortMultipartUpload operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/java-multipart-upload#concept-84786-zh)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-multipart-upload)

-

[Harmony](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-harmony-sdk)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-sdk-for-php-v2)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-9#concept-90222-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-10#concept-91103-zh)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-11)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-8#concept-90222-zh)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-3#concept-hgg-3vb-dhb)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-6#concept-1925841)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-7)

## ossutil


For information about the ossutil command that corresponds to the AbortMultipartUpload operation, see [abort-multipart-upload](https://www.alibabacloud.com/help/en/oss/developer-reference/abort-multipart-upload).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchUpload | 404 | The specified upload ID does not exist. |


Thank you! We've received your  feedback.