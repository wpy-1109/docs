# GetLiveChannelStat

Queries the stream ingestion status of a specified LiveChannel.

Request syntax
 
GET /ChannelName?live&comp=stat HTTP/1.1
Date: GMT date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response elements

Element

	

Type

	

Description




LiveChannelStat

	

Container

	

The container that stores the returned results of the GetLiveChannelStat request.

Child nodes: Status, ConnectedTime, Video, and Audio

Parent nodes: none




Status

	

Enumerated string

	

The current stream ingestion status of the LiveChannel.

Child nodes: none

Parent nodes: LiveChannelStat

Valid values: Disabled, Live, and Idle




ConnnectedTime

	

String

	

If Status is set to Live, this element indicates the time when the current client starts to ingest streams. The value of the element is in the ISO 8601 format.

Child nodes: none

Parent nodes: LiveChannelStat




RemoteAddr

	

String

	

If Status is set to Live, this element indicates the IP address of the current client that ingests streams.

Child nodes: none

Parent nodes: LiveChannelStat




Video

	

Container

	

The container that stores video stream information if Status is set to Live.

Note

Video and audio containers can be returned only if Status is set to Live. However, these two containers may not necessarily be returned if Status is set to Live. For example, if the client has connected to the LiveChannel but no audio or video stream is sent, these two containers are not returned.

Child nodes: Width, Height, FrameRate, Bandwidth, and Codec

Parent nodes: LiveChannelStat




Width

	

String

	

The width of the current video stream.

Unit: pixels.

Child nodes: none

Parent nodes: Video




Height

	

String

	

The height of the current video stream.

Unit: pixels.

Child nodes: none

Parent nodes: Video




FrameRate

	

String

	

The frame rate of the current video stream.

Child nodes: none

Parent nodes: Video




Bandwidth

	

String

	

The bitrate of the current video stream.

Unit: bit/s.

Child nodes: none

Parent nodes: Video




Codec

	

Enumerated string

	

The encoding format of the current video stream.

Child nodes: none

Parent nodes: Video




Audio

	

Container

	

The container that stores audio stream information if Status is set to Live.

Note

Video and audio containers can be returned only if Status is set to Live. However, these two containers may not necessarily be returned if Status is set to Live. For example, if the client has connected to the LiveChannel but no audio or video stream is sent, these two containers are not returned.

Child nodes: SampleRate, Bandwidth, and Codec

Parent nodes: LiveChannelStat




SampleRate

	

String

	

The sample rate of the current audio stream.

Child nodes: none

Parent nodes: Audio




Bandwidth

	

String

	

The bitrate of the current audio stream.

Note

Bandwidth indicates the average bitrate of the audio stream or video stream in the recent period. When LiveChannel is switched to the Live state, the returned value of Bandwidth may be 0.

Unit: bit/s.

Child nodes: none

Parent nodes: Audio




Codec

	

Enumerated string

	

The encoding format of the current audio stream.

Child nodes: none

Parent nodes: Audio

Examples

Sample request 1

 
GET /test-channel?live&comp=stat HTTP/1.1
Date: Thu, 25 Aug 2016 06:22:01 GMT
Host: test-bucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q**************:77Dv****************

Sample response 1

 
HTTP/1.1 200
content-length: 100
server: AliyunOSS
connection: close
x-oss-request-id: 57BE8E89B92475920B002164
date: Thu, 25 Aug 2016 06:22:01 GMT
content-type: application/xml
<?xml version="1.0" encoding="UTF-8"?>
<LiveChannelStat>
  <Status>Idle</Status>
</LiveChannelStat>

Sample request 2

 
GET /test-channel?live&comp=stat HTTP/1.1
Date: Thu, 25 Aug 2016 06:25:26 GMT
Host: test-bucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS qn6q**************:77Dv****************

Sample response 2

 
HTTP/1.1 200
content-length: 469
server: AliyunOSS
connection: close
x-oss-request-id: 57BE8F56B92475920B002187
date: Thu, 25 Aug 2016 06:25:26 GMT
content-type: application/xml
<?xml version="1.0" encoding="UTF-8"?>
<LiveChannelStat>
  <Status>Live</Status>
  <ConnectedTime>2016-08-25T06:25:15.000Z</ConnectedTime>
  <RemoteAddr>10.1.2.3:47745</RemoteAddr>
  <Video>
    <Width>1280</Width>
    <Height>536</Height>
    <FrameRate>24</FrameRate>
    <Bandwidth>0</Bandwidth>
    <Codec>H264</Codec>
  </Video>
  <Audio>
    <Bandwidth>0</Bandwidth>
    <SampleRate>44100</SampleRate>
    <Codec>ADPCM</Codec>
  </Audio>
</LiveChannelStat>