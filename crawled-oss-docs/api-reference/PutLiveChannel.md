# PutLiveChannel

Before you can upload audio and video data by using the Real-Time Messaging Protocol (RTMP), you must call the PutLiveChannel operation to create a LiveChannel. The response to the PutLiveChannel request includes the URL that is used to ingest streams to the LiveChannel and the URL that is used to play the ingested streams.

Note

You can use the returned URLs to ingest and play streams. Based on the returned LiveChannel name, you can also perform operations such as querying stream ingesting status, querying stream ingesting records, and disabling stream ingesting.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM Policy or Bucket Policy.

API

	

Action

	

Definition




PutLiveChannel

	

oss:PutLiveChannel

	

Creates a LiveChannel before you upload audio and video data by using the Real-Time Messaging Protocol (RTMP).

Request syntax
 
PUT /ChannelName?live HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT date
Content-Length: Size
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<LiveChannelConfiguration>
  <Description>ChannelDescription</Description>
  <Status>ChannelStatus</Status>
  <Target>
     <Type>HLS</Type>
     <FragDuration>FragDuration</FragDuration>
     <FragCount>FragCount</FragCount>
     <PlaylistName>PlaylistName</PlaylistName>
  </Target>
  <Snapshot>
    <RoleName>Snapshot ram role</RoleName>
    <DestBucket>Snapshot dest bucket</DestBucket>
    <NotifyTopic>Notify topic of MNS</NotifyTopic>
    <Interval>Snapshot interval in second</Interval>
  </Snapshot>
</LiveChannelConfiguration>
Request headers

Header

	

Type

	

Required

	

Description




ChannelName

	

String

	

Yes

	

The name of the LiveChannel that you want to create. The name must comply with the naming conventions for objects and cannot contain forward slashes (/).

Request parameters

Parameter

	

Type

	

Required

	

Description




LiveChannelConfiguration

	

Container

	

Yes

	

The container that stores the configurations of the LiveChannel.

Child nodes: Description, Status, and Target

Parent nodes: none




Description

	

String

	

No

	

The description of the LiveChannel. The description can be up to 128 bytes in length.

Child nodes: none

Parent nodes: LiveChannelConfiguration




Status

	

Enumerated string

	

No

	

The status of the LiveChannel.

Child nodes: none

Parent nodes: LiveChannelConfiguration

Valid values: enabled and disabled

Default value: enabled




Target

	

Container

	

Yes

	

The container that stores the configurations used by the LiveChannel to store uploaded data.

Child nodes: Type, FragDuration, FragCount, and PlaylistName

Parent nodes: LiveChannelConfiguration




Type

	

Enumerated string

	

Yes

	

The format in which the LiveChannel stores uploaded data.

Child nodes: none

Parent nodes: Target

Valid value: HLS

Note

When you set the value of Type to HLS, Object Storage Service (OSS) updates the m3u8 file each time when a ts file is generated. The maximum number of the latest ts files that can be included in the m3u8 file is specified by the FragCount parameter.

When you set the value of Type to HLS and the duration of the audio and video data written to the current ts file exceeds the duration specified by FragDuration, OSS switches to the next ts file to write data before the next key frame is received. If OSS does not receive the next key frame after max(2*FragDuration, 60s), OSS forcibly switches to the next ts file. In this case, stuttering may occur during the playback of the stream.




FragDuration

	

String

	

No

	

The duration of each ts file when you set the value of Type to HLS.

Unit: seconds

Child nodes: none

Parent nodes: Target

Valid values: [1, 100]

Default value: 5

Note

If you do not specify values for the FragDuration and FragCount parameters, the default values of the two parameters are used. You must specify the FragDuration and FragCount parameters at the same time.




FragCount

	

String

	

No

	

The number of ts files included in the m3u8 file when the value of Type is HLS.

Child nodes: none

Parent nodes: Target

Valid values: [1, 100]

Default value: 3

Note

If you do not specify values for the FragDuration and FragCount parameters, the default values of the two parameters are used. You must specify the FragDuration and FragCount parameters at the same time.




PlaylistName

	

String

	

No

	

The name of the generated m3u8 file when the value of Type is HLS. The name must be 6 to 128 bytes in length. The name must end with .m3u8.

Child nodes: none

Parent nodes: Target

Default value: playlist.m3u8




Snapshot

	

Container

	

No

	

The container that stores the options of the high-frequency snapshot operations.

Child nodes: RoleName, DestBucket, NotifyTopic, and Interval

Parent nodes: LiveChannelConfiguration




RoleName

	

String

	

No

	

The name of the role used to perform high-frequency snapshot operations. The role must have the write permissions on DestBucket and the permissions to send messages to NotifyTopic.

Child nodes: none

Parent nodes: Snapshot




DestBucket

	

String

	

No

	

The bucket that stores the results of high-frequency snapshot operations. The bucket must belong to the same owner as the current bucket.

Child nodes: none

Parent nodes: Snapshot




NotifyTopic

	

String

	

No

	

The MNS topic used to notify users of the results of high-frequency snapshot operations.

Child nodes: none

Parent nodes: Snapshot




Interval

	

NUMERIC

	

Yes

	

The interval of high-frequency snapshot operations. If no key frame, such as an inline frame, exists within the interval, no snapshot is captured.

Unit: seconds

Child nodes: none

Parent nodes: Snapshot

Valid values: [1, 100]

By default, this parameter is left empty.

Response parameters

Parameter

	

Type

	

Description




CreateLiveChannelResult

	

Container

	

The container that stores the response to the CreateLiveChannel request.

Child nodes: PublishUrls and PlayUrls

Parent nodes: none




PublishUrls

	

Container

	

The container that stores the URL used to ingest streams to the LiveChannel.

Child nodes: Url

Parent nodes: CreateLiveChannelResult




Url

	

String

	

The URL used to ingest streams to the LiveChannel.

Child nodes: none

Parent nodes: PublishUrls

Note

The URL used to ingest streams is not signed. If the access control list (ACL) of the bucket is not public read/write, you must add a signature to the URL before you use the URL to access the bucket.

The URL used to play streams is not signed. If the ACL of the bucket is private, you must add a signature to the URL before you use the URL to access the bucket.




PlayUrls

	

Container

	

The container that stores the URL used to play the streams ingested to the LiveChannel.

Child nodes: Url

Parent nodes: CreateLiveChannelResult




Url

	

String

	

The URL used to play the streams ingested to the LiveChannel.

Child nodes: none

Parent nodes: PlayUrls

Examples

Sample requests

 
PUT /test-channel?live HTTP/1.1
Date: Wed, 24 Aug 2016 11:11:28 GMT
Content-Length: 333
Host: test-bucket.oss-cn-hangzhou.aliyuncs.com
Authorization: OOSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<LiveChannelConfiguration>
    <Description/>
    <Status>enabled</Status>
    <Target>
        <Type>HLS</Type>
        <FragDuration>2</FragDuration>
        <FragCount>3</FragCount>
    </Target>
    <Snapshot>
        <RoleName>role_for_snapshot</RoleName>
        <DestBucket>snapshotdest</DestBucket>
        <NotifyTopic>snapshotnotify</NotifyTopic>
        <Interval>1</Interval>
     </Snapshot>
</LiveChannelConfiguration>

Sample responses

 
HTTP/1.1 200
content-length: 259
server: AliyunOSS
x-oss-server-time: 4
connection: close
x-oss-request-id: 57BD8419B92475920B0002F1
date: Wed, 24 Aug 2016 11:11:28 GMT
x-oss-bucket-storage-type: standard
content-type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<CreateLiveChannelResult>
  <PublishUrls>
    <Url>rtmp://test-bucket.oss-cn-hangzhou.aliyuncs.com/live/test-channel</Url>
  </PublishUrls>
  <PlayUrls>
    <Url>http://test-bucket.oss-cn-hangzhou.aliyuncs.com/test-channel/playlist.m3u8</Url>
  </PlayUrls>
</CreateLiveChannelResult>