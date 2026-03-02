# DeleteLiveChannel

You can call this operation to delete a specified LiveChannel.

Request structure
Note

If you send a DeleteLiveChannel request to delete a LiveChannel to which a client is ingesting streams, the request fails.

When you call this operation to delete a LiveChannel, only the LiveChannel is deleted. Files generated during stream ingestion are not deleted.

 
DELETE /ChannelName? live HTTP/1.1
Date: GMT date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

A DeleteLiveChannel request contains only common request headers. For more information, see Common request headers.

Response headers

The response to a DeleteLiveChannel request contains only common response headers. For more information, see Common response headers.

Examples

Sample request

 
DELETE /test-channel? live HTTP/1.1
Date: Thu, 25 Aug 2016 07:32:26 GMT
Host: test-bucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204
content-length: 0
server: AliyunOSS
connection: keep-alive
x-oss-request-id: 57BE9F0AB92475920B0*****
date: Thu, 25 Aug 2016 07:32:26 GMT