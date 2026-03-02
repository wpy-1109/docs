# DeleteAccessPointPolicyForObjectProcess

Deletes the permission policies of an Object FC Access Point.

## Usage notes


By default, an Alibaba Cloud account has the permissions to delete the permission policies of an Object FC Access Point. To delete the permission policies of an Object FC Access Point by using a RAM user or Security Token Service (STS), you must have the `oss:DeleteAccessPointPolicyForObjectProcess` permission.

## Request syntax


`xml
DELETE /?accessPointPolicyForObjectProcess HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue
`


## Request headers


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-access-point-for-object-process-name | String | Yes | fc-ap-01 | The name of the Object FC Access Point. |


For more information about other common request headers included in a DeleteAccessPointPolicyForObjectProcess request, such as Host and Date, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a DeleteAccessPointPolicyForObjectProcess request contains only common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`xml
DELETE /?accessPointPolicyForObjectProcess HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 0
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
x-oss-access-point-for-object-process-name: fc-ap-01
Authorization: SignatureValue
`


-

Sample response


`xml
HTTP/1.1 204
x-oss-request-id: 5C1B138A109F4E405B2D
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


Thank you! We've received your  feedback.