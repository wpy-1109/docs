# Call the DeletePublicAccessBlock operation to delete the Block Public Access configurations of OSS resources

Deletes the Block Public Access configurations of Object Storage Service (OSS) resources.

## Usage notes


By default, an Alibaba Cloud account has the permissions to delete the Block Public Access configurations of OSS resources. If you want to delete the Block Public Access configurations of OSS resources by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:DeletePublicAccessBlock` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`http
DELETE /?publicAccessBlock HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a DeletePublicAccessBlock request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a DeletePublicAccessBlock request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`http
DELETE /?publicAccessBlock HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
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


You can use OSS SDK for [Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/oss-global-block-public-access-using-oss-sdk-for-go-v2) to call the DeletePublicAccessBlock operation.

## ossutil


For information about the ossutil command that corresponds to the DeletePublicAccessBlock operation, see [delete-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-public-access-block).

Thank you! We've received your  feedback.