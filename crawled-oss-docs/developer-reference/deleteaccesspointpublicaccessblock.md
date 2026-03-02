# Call the DeleteBucketPublicAccessBlock operation to delete the Block Public Access configurations of an access point

Deletes the Block Public Access configurations of an access point.

## Usage notes


By default, an Alibaba Cloud account has the permissions to delete the Block Public Access configurations of an access point. If you want to delete the Block Public Access configurations of an access point by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:DeleteAccessPointPublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`http
DELETE /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a DeleteAccessPointPublicAccessBlock request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-access-point-name | String | Yes | ap-01 | The name of the access point. |


## Response headers


The response to a DeleteAccessPointPublicAccessBlock request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`http
DELETE /?publicAccessBlock&x-oss-access-point-name=ap-01 HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q:77Dv
`


-

Sample success response


`http
HTTP/1.1 204 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS
`


## OSS SDK


You can use OSS SDK for [Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/access-point-level-block-public-access-using-oss-sdk-for-go-v2) to call the DeleteAccessPointPublicAccessBlock operation.

## ossutil


For information about the ossutil command that corresponds to the DeleteAccessPointPublicAccessBlock operation, see [delete-access-point-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-access-point-public-access-block).


Thank you! We've received your  feedback.