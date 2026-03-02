# How to change the status of an Anti-DDoS instance by calling UpdateUserAntiDDosInfo

Changes the status of an Anti-DDoS instance.

## Note


By default, an Alibaba Cloud account has the permissions to change the status of an Anti-DDoS instance. To change the status of an Anti-DDoS instance by using a RAM user or Security Token Service (STS), you must have the `oss:UpdateUserAntiDDosInfo` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
POST /?antiDDos HTTP/1.1
Date:  GMT Date
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73
x-oss-defender-status: HaltDefending
`


## Request headers


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-defender-instance | String | Yes | cbcac8d2-4f75-4d6d-9f2e-c3447f73 | The ID of the Anti-DDoS instance. |
| x-oss-defender-status | String | Yes | HaltDefending | The new status of the Anti-DDoS instance. Set the value toHaltDefending |


For more information about other common request headers that are included in an UpdateUserAntiDDosInfo request, such as Host and Date, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to an UpdateUserAntiDDosInfo request are common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Example


-

Sample request


`plaintext
POST /?antiDDos HTTP/1.1
Date:  Thu, 17 Apr 2025 05:34:24 GMT
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73
x-oss-defender-status: HaltDefending
`


-

Sample response


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:34:24 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 534B371674E88A4D8906
`


Thank you! We've received your  feedback.