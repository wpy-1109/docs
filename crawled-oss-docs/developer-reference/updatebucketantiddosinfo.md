# How UpdateBucketAntiDDosInfo works

Updates the status of Anti-DDoS instances of a bucket.

## Usage notes


By default, an Alibaba Cloud account has the permissions to update the status of Anti-DDoS instances of a bucket. To update the status of Anti-DDoS instances of a bucket by using a RAM user or Security Token Service (STS), you must have the `oss:UpdateBucketAntiDDosInfo` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
POST /?antiDDos HTTP/1.1
Date:  GMT Date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73
x-oss-defender-status: Init
<AntiDDOSConfiguration>
  <Cnames>
    <Domain>abc1.example.cn</Domain>
    <Domain>abc2.example.cn</Domain>
  </Cnames>
</AntiDDOSConfiguration>
`


## Request headers


-


-


-


> IMPORTANT:

> NOTE: 


> NOTE: 

-


-


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-defender-instance | String | Yes | cbcac8d2-4f75-4d6d-9f2e-c3447f73 | The ID of the Anti-DDoS instance. |
| x-oss-defender-status | String | Yes | Init | The new status of the Anti-DDoS instance. Valid values:Init: You must specify the custom domain name that you want to protect. Defending: You can select whether to specify the custom domain name that you want to protect. HaltDefending: You do not need to specify the custom domain name that you want to protect. Important If you change the CNAME record that is mapped to the custom domain name, the value of this header must be the status of the Anti-DDoS instance. If you do not want a bucket to be protected by an Anti-DDoS instance, set this header to HaltDefending. |
| AntiDDOSConfiguration | Container | No | N/A | The container that stores the configurations of Anti-DDoS instances. |
| Cnames | Container | No | N/A | The container that stores the list of domain names of Anti-DDoS instances. |
| Domain | String | No | abc1.example.cn | The custom domain names that you want to protect. You can add up to five custom domain names for each bucket to the protection list of an Anti-DDoS instance. |


For more information about other common request headers that are included in an UpdateBucketAntiDDosInfo request, such as Host and Date, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to an UpdateBucketAntiDDosInfo request are common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample requests


`plaintext
POST /?antiDDos HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-defender-instance: cbcac8d2-4f75-4d6d-9f2e-c3447f73
x-oss-defender-status: Init
<AntiDDOSConfiguration>
  <Cnames>
    <Domain>abc1.example.cn</Domain>
    <Domain>abc2.example.cn</Domain>
  </Cnames>
</AntiDDOSConfiguration>
`


-

Sample responses


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:34:24 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 534B371674E88A4D8906
`


Thank you! We've received your  feedback.