# How to make query requests by calling GetUserAntiDDosInfo

Queries Anti-DDoS instances.

## Notes


By default, an Alibaba Cloud account has the permissions to query Anti-DDoS instances. To make query requests as a RAM user or using Security Token Service (STS), you must have the `oss:GetUserAntiDDosInfo` permission. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /?antiDDos HTTP/1.1
Date:  GMT Date
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a GetUserAntiDDosInfo request are common request headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a GetUserAntiDDosInfo request are common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| AntiDDOSListConfiguration | Container | N/A | The container that stores the list of Anti-DDoS instances. Parent nodes: noneChild nodes: Marker, IsTruncated, and AntiDDOSConfiguration |
| AntiDDOSConfiguration | Container | N/A | The container that stores information about the Anti-DDoS instance. Parent node: AntiDDOSListConfigurationChild nodes: InstanceId, Bucket, Owner, Ctime, Mtime, and Status |
| InstanceId | String | cbcac8d2-4f75-4d6d-9f2e-c3447f73 | The ID of the Anti-DDoS instance. Parent nodes: AntiDDOSConfigurationChild nodes: none |
| Owner | String | 114893010724 | The ID of the owner of the Anti-DDoS instance. Parent nodes: AntiDDOSConfigurationChild nodes: none |
| Ctime | String | 1626769503 | The time when the Anti-DDoS instance was created. The value is a timestamp. Parent nodes: AntiDDOSConfigurationChild nodes: none |
| Mtime | String | 1626769840 | The time when the Anti-DDoS instance was last updated. The value is a timestamp. Parent nodes: AntiDDOSConfigurationChild nodes: none |
| ActiveTime | String | 1626769845 | The time when the Anti-DDoS instance was activated. The value is a timestamp. Parent nodes: AntiDDOSConfigurationChild nodes: none |
| Status | String | Defending | The status of the Anti-DDoS instance. Init Defending HaltDefending Parent nodes: AntiDDOSConfigurationChild nodes: none |


## Example


-

Sample request


`plaintext
GET /?antiDDos HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
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

<AntiDDOSListConfiguration>
    <AntiDDOSConfiguration>
        <InstanceId>cbcac8d2-4f75-4d6d-9f2e-c3447f73</InstanceId>
        <Owner>114893010724</Owner>
        <Ctime>12345667</Ctime>
        <Mtime>12345667</Mtime>
        <ActiveTime>12345680</ActiveTime>
        <Status>Init</Status>
    </AntiDDOSConfiguration>
 </AntiDDOSListConfiguration>
`


Thank you! We've received your  feedback.