# ListLiveChannel

Lists specified LiveChannels.

Request syntax
 
GET /?live HTTP/1.1
Date: GMT date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request elements

Element

	

Type

	

Required

	

Description




marker

	

String

	

No

	

The name of the LiveChannel after which the list operation starts. LiveChannels whose names are alphabetically after the value of the marker parameter are returned.




max-keys

	

String

	

No

	

The maximum number of LiveChannels that can be returned in the operation.

Valid values: 1 to 1000

Default value: 100




prefix

	

String

	

No

	

The prefix that the names of the LiveChannels that you want to return must contain. If you specify a prefix in the request, the specified prefix is included in the response.

For more information about the common request headers included in ListLiveChannel requests such as Host and Date, see Common request headers.

Response elements

Element

	

Type

	

Description




ListLiveChannelResult

	

Container

	

The container that stores the results of the ListLiveChannel request.

Child nodes: Prefix, Marker, MaxKeys, IsTruncated, NextMarker, and LiveChannel

Parent nodes: none




Prefix

	

String

	

The prefix that the names of the returned LiveChannels contain.

Child nodes: none

Parent nodes: ListLiveChannelResult




Marker

	

String

	

The name of the LiveChannel after which the ListLiveChannel operation starts.

Child nodes: none

Parent nodes: ListLiveChannelResult




MaxKeys

	

String

	

The maximum number of returned LiveChannels in the response.

Child nodes: none

Parent nodes: ListLiveChannelResult




IsTruncated

	

String

	

Indicates whether all results are returned.

true: All results are returned.

false: Not all results are returned.

Child nodes: none

Parent nodes: ListLiveChannelResult




NextMarker

	

String

	

If not all results are returned, the NextMarker parameter is included in the response to indicate the Marker value of the next request.

Child nodes: none

Parent nodes: ListLiveChannelResult




LiveChannel

	

Container

	

The container that stores the information about each returned LiveChannel.

Child nodes: Name, Description, Status, LastModified, PublishUrls, and PlayUrls

Parent nodes: ListLiveChannelResult




Name

	

String

	

The name of the LiveChannel.

Child nodes: none

Parent nodes: LiveChannel




Description

	

String

	

The description of the LiveChannel.

Child nodes: none

Parent nodes: LiveChannel




Status

	

Enumerated string

	

The status of the LiveChannel.

Child nodes: none

Parent nodes: LiveChannel

Valid values:

disabled: The LiveChannel is disabled.

enabled: The LiveChannel is enabled.




LastModified

	

String

	

The time when the LiveChannel configuration is last modified.

Standard: ISO 8601.

Child nodes: none

Parent nodes: LiveChannel




PublishUrls

	

Container

	

The container that stores the URL used to ingest a stream to the LiveChannel.

Child nodes: Url

Parent nodes: LiveChannel




Url

	

String

	

The URL used to ingest a stream to the LiveChannel.

Child nodes: none

Parent nodes: PublishUrls




PlayUrls

	

Container

	

The container that stores the URL used to play a stream ingested to the LiveChannel.

Child nodes: Url

Parent nodes: LiveChannel




Url

	

String

	

The URL used to play a stream ingested to the LiveChannel.

Child nodes: none

Parent nodes: PlayUrls

For more information about the common response headers such as ETag and x-oss-request-id contained in the responses to ListLiveChannel requests, see Common response headers.

Examples

Sample request

 
GET /?live&max-keys=1 HTTP/1.1
Date: Thu, 25 Aug 2016 07:50:09 GMT
Host: test-bucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 200
content-length: 656
server: AliyunOSS
connection: close
x-oss-request-id: 57BEA331B92475920B00****
date: Thu, 25 Aug 2016 07:50:09 GMT
content-type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<ListLiveChannelResult>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys>1</MaxKeys>
  <IsTruncated>true</IsTruncated>
  <NextMarker>channel-0</NextMarker>
  <LiveChannel>
    <Name>channel-0</Name>
    <Description></Description>
    <Status>disabled</Status>
    <LastModified>2016-07-30T01:54:21.000Z</LastModified>
    <PublishUrls>
      <Url>rtmp://test-bucket.oss-cn-hangzhou.aliyuncs.com/live/channel-0</Url>
    </PublishUrls>
    <PlayUrls>
      <Url>http://test-bucket.oss-cn-hangzhou.aliyuncs.com/channel-0/playlist.m3u8</Url>
    </PlayUrls>
  </LiveChannel>
</ListLiveChannelResult>