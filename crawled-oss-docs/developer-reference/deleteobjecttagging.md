# Invoke the DeleteObjectTagging operation to delete the tagging information of a specified object

You can call this operation to delete the tags of a specified object.

## Versioning


By default, when you call DeleteObjectTagging to delete the tags of an object, the tags of the current version of the object are deleted. You can specify the versionId parameter in the request to delete the tags of a specified version of an object. If the current version of the object is a delete marker, OSS returns 404 Not Found.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).


| API | Action | Definition |
| --- | --- | --- |
| DeleteObjectTagging | oss:DeleteObjectTagging | Deletes the tags of an object. |
| oss:DeleteObjectVersionTagging | Deletes the tags of a specified version of an object. |


## Request structure


`plaintext
DELETE /objectname?tagging
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Mon, 18 Mar 2019 08:25:17 GMT
Authorization: SignatureValue
`


## Request headers


All headers in a DeleteObjectTagging request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DeleteObjectTagging request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Delete the tags of an object in an unversioned bucket.


In this example, an object named objectname is stored in an unversioned bucket named bucketname. A DeleteObjectTagging request is sent to delete all tags of objectname.


Sample request


`plaintext
DELETE /objectname?tagging
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 03:00:33 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
204 (No Content)
content-length: 0
server: AliyunOSS
x-oss-request-id: 5CAC0AD16D0232E2051B
date: Tue, 09 Apr 2019 03:00:33 GMT
`


-

Delete the tags of an object in a versioned bucket.


In this example, an object named objectname is stored in a versioned bucket named bucketname. A DeleteObjectTagging request is sent to delete all tags of a specified version of objectname.


Sample request


`plaintext
DELETE /objectname?tagging&versionId=CAEQExiBgID.jImWlxciIDQ2ZjgwODIyNDk5MTRhNzBiYmQwYTZkMTYzZjM0
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 24 Jun 2020 09:01:09 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
204 (No Content)
content-length: 0
server: AliyunOSS
x-oss-request-id: 5EF3165525D95C3338E8
date: Wed, 24 Jun 2020 09:01:09 GMT
x-oss-version-id: CAEQExiBgID.jImWlxciIDQ2ZjgwODIyNDk5MTRhNzBiYmQwYTZkMTYzZjM0
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call DeleteObjectTagging:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-the-tags-of-an-object-1#concept-727776)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-delete-object-tags)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-object-tags-using-oss-sdk-for-php-v2)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/object-tagging-4)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-object-tags-2#concept-727374)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-object-tags#concept-2512416)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-the-tags-of-an-object-2#concept-2404257)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/object-tagging-1)

## ossutil


For information about the ossutil command that corresponds to the DeleteObjectTagging operation, see [delete-object-tagging](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-object-tagging).

## Error code











| Error code | HTTP status code | Description |
| --- | --- | --- |
| FileAlreadyExists | 409 | The error message returned because the object whose tags you want to delete is a directory in a bucket with the hierarchical namespace feature enabled. |


Thank you! We've received your  feedback.