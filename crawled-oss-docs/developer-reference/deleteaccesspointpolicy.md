# Delete an access point policy by calling the DeleteAccessPointPolicy operation

Deletes an access point policy.

## Usage notes


By default, an Alibaba Cloud account has the permissions to delete an access point policy. To delete an access point policy by using a RAM user or Security Token Service (STS) you must have the `oss:DeleteAccessPointPolicy` permission.

## Request syntax


`plaintext
DELETE /?accessPointPolicy HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: apname
Authorization: SignatureValue
`


## Request headers


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-access-point-name | String | Yes | ap-01 | The name of the access point. |


This request contains other common request headers, such as Date and Authorization. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a DeleteAccessPointPolicy request contains only common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`plaintext
DELETE /?accessPointPolicy HTTP/1.1
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 230
Content-Type: application/xml
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-name: ap-01
Authorization: OSS qn6q:77Dv
`


-

Sample response


`plaintext
HTTP/1.1 200
x-oss-request-id: 5C1B138A109F4E405B2D
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## ossutil


For information about the ossutil command that corresponds to the DeleteAccessPointPolicy operation, see [delete-access-point-policy](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-access-point-policy).

Thank you! We've received your  feedback.