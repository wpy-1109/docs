# CleanRestoredObject

When you restore a Cold Archive or Deep Cold Archive object in Object Storage Service (OSS), a temporary replica is created to allow access. You are charged for the storage of this replica until the object returns to the frozen state. To end the restored state early and stop incurring storage fees, you can send a CleanRestoredObject request. After the request is complete, the object returns to the frozen state and cannot be read.

## Syntax


`shell
POST /ObjectName?cleanRestoredObject HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a CleanRestoredObject request are common request headers. For more information, see [Common Request Headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a CleanRestoredObject request are common response headers. For more information, see [Common Response Headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`shell
POST /ObjectName?cleanRestoredObject HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 20 Sep 2024 08:32:21 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


-

The RestoreObject request has not been initiated for the object, or the CleanRestoredObject request has been processed.


`shell
HTTP/1.1 409 Conflict
Date: Fri, 20 Sep 2024 08:32:21 GMT
Content-Length: 556
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>ArchiveRestoreFileStale</Code>
  <Message>The archive file or restore info stale</Message>
  <RequestId>5374A2880232A65C2300</RequestId>
  <HostId>10.101.XX.XX</HostId>
</Error>
`


-

The RestoreObject request has been initiated for the object, and restoration is in progress.


`shell
HTTP/1.1 409 Conflict
Date: Fri, 20 Sep 2024 08:32:21 GMT
Content-Length: 556
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>ArchiveRestoreNotFinished</Code>
  <Message>The archive file's restore is not finished.</Message>
  <RequestId>5374A2880232A65C2300</RequestId>
  <HostId>10.101.XX.XX</HostId>
</Error>
`


-

The RestoreObject request has been initiated for the object, and restoration is complete.


`shell
HTTP/1.1 200 Ok
Date: Fri, 20 Sep 2024 08:32:21 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300
`


Thank you! We've received your  feedback.