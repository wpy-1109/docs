# PutLiveChannelStatus

Changes the status of a LiveChannel to enabled or disabled.

Usage notes

When you call PutLiveChannelStatus, take note of the following items:

If a LiveChannel is disabled, OSS prohibits you from ingesting streams to the LiveChannel. If you are ingesting a stream to a disabled LiveChannel, your client is disconnected from the LiveChannel after approximately 10 seconds.

If no stream is ingested to a LiveChannel, You can re-create the LiveChannel by calling PutLiveChannel to change the status of the LiveChannel.

If a stream is being ingested to a LiveChannel, you can only call PutLiveChannelStatus to change the status of the LiveChannel to disabled.

Permissions

By default, an Alibaba Cloud account has full permissions on resources in the account. In contrast, RAM users and RAM roles associated with an Alibaba Cloud account initially have no permissions. To manage resources by using a RAM user or role, you must grant the required permissions via RAM policies or Bucket policies.

API

	

Action

	

Description




PutLiveChannelStatus

	

oss:PutLiveChannelStatus

	

Changes the status of a LiveChannel to enabled or disabled.

Request syntax
 
PUT /ChannelName?live&status=NewStatus HTTP/1.1
Date: Tue, 25 Dec 2018 17:35:24 GMT
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request elements

Element

	

Type

	

Required

	

Description




status

	

String

	

Yes

	

The status of the LiveChannel.

Valid values:

enabled

disabled

Request headers

All headers in a PutLiveChannelStatus request are common request headers. For more information, see Common HTTP headers.

Response headers

All headers in the response to a PutLiveChannelStatus request are common response headers. For more information, see Common HTTP headers.

Examples

Sample request

 
PUT /test-channel?live&status=disabled HTTP/1.1
Date: Tue, 25 Dec 2018 17:35:24 GMT
Host: test-bucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q**************:77Dv****************

Sample response

 
HTTP/1.1 200
Content-Length: 0
Server: AliyunOSS
Connection: close
x-oss-request-id: 57BE8422B92475920B00****
Date: Tue, 25 Dec 2018 17:35:24 GMT