# Call the GetBucketStat operation to obtain the storage capacity, the number of objects, and the number of multipart parts for a specified bucket.

You can call the GetBucketStat operation to obtain the storage capacity, the number of objects, and the number of multipart parts for a specified bucket.

## Usage notes


-

To call this operation, you must have the `oss:GetBucketStat` permission.

-

The data returned by this operation is not real-time and may be delayed by more than one hour.

-

The storage information returned by this operation is not guaranteed to be the latest. The LastModifiedTime value in a response may be earlier than the LastModifiedTime value in a previous response.

## Request syntax


`plaintext
GET /?stat HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














> IMPORTANT:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/storage-fees#concept-2558327)


> IMPORTANT:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/storage-fees#concept-2558327)


> IMPORTANT:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/storage-fees#concept-2558327)


> IMPORTANT:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/storage-fees#concept-2558327)


| Name | Type | Example | Description |
| --- | --- | --- | --- |
| BucketStat | Container | N/A | A container for the BucketStat structure. |
| Storage | Positive integer | 1600 | The total actual storage capacity of the bucket. Unit: bytes.Parent node: BucketStatChild node: None |
| ObjectCount | Positive integer | 230 | The total number of objects in the bucket.Parent node: BucketStatChild node: None |
| MultipartUploadCount | Positive integer | 40 | The number of multipart uploads that are initiated but not completed or aborted in the bucket.Parent node: BucketStatChild node: None |
| LiveChannelCount | Positive integer | 4 | The number of LiveChannels in the bucket.Parent node: BucketStatChild node: None |
| MultipartPartCount | Positive integer | 128 | The number of multipart parts uploaded to the bucket.Parent node: BucketStatChild node: None |
| MultipartPartStorage | Positive integer | 524288000 | The storage capacity of the multipart parts uploaded to the bucket. Unit: bytes.Parent node: BucketStatChild node: None |
| DeleteMarkerCount | Positive integer | 12 | The number of delete markers in the bucket.Parent node: BucketStatChild node: None |
| LastModifiedTime | Positive integer | 1643341269 | The time point of the obtained storage information. The value is a UNIX timestamp in seconds.Parent node: BucketStatChild node: None |
| StandardStorage | Positive integer | 430 | The storage capacity of Standard objects. Unit: bytes.Parent node: BucketStatChild node: None |
| StandardObjectCount | Positive integer | 66 | The number of Standard objects.Parent node: BucketStatChild node: None |
| StandardMultipartPartCount | Positive integer | 10 | The number of Standard multipart parts uploaded to the bucket.Parent node: BucketStatChild node: None |
| StandardMultipartPartStorage | Positive integer | 104857600 | The storage capacity of the Standard multipart parts uploaded to the bucket. Unit: bytes.Parent node: BucketStatChild node: None |
| InfrequentAccessStorage | Positive integer | 2359296 | The billable storage capacity of Infrequent Access (IA) objects. Unit: bytes.Important An object smaller than 64 KB is calculated as 64 KB. For more information about billing, see Storage fees.Parent node: BucketStatChild node: None |
| InfrequentAccessRealStorage | Positive integer | 360 | The actual amount of storage used by the Infrequent Access storage class, in bytes.Parent node: BucketStatChild node: None |
| InfrequentAccessObjectCount | Positive integer | 54 | The number of IA objects.Parent node: BucketStatChild node: None |
| InfrequentMultipartPartCount | Positive integer | 10 | The number of IA multipart parts uploaded to the bucket.Parent node: BucketStatChild node: None |
| InfrequentMultipartPartStorage | Positive integer | 104857600 | The storage capacity of the IA multipart parts uploaded to the bucket. Unit: bytes.Parent node: BucketStatChild node: None |
| ArchiveStorage | Positive integer | 2949120 | The billable storage capacity of Archive objects. Unit: bytes.Important An object smaller than 64 KB is calculated as 64 KB. For more information about billing, see Storage fees.Parent node: BucketStatChild node: None |
| ArchiveRealStorage | Positive integer | 450 | The actual storage capacity of Archive objects. Unit: bytes.Parent node: BucketStatChild node: None |
| ArchiveObjectCount | Positive integer | 74 | The number of Archive objects.Parent node: BucketStatChild node: None |
| ArchiveMultipartPartCount | Positive integer | 10 | The number of Archive multipart parts uploaded to the bucket.Parent node: BucketStatChild node: None |
| ArchiveMultipartPartStorage | Positive integer | 104857600 | The storage capacity of the Archive multipart parts uploaded to the bucket. Unit: bytes.Parent node: BucketStatChild node: None |
| ColdArchiveStorage | Positive integer | 2359296 | The billable storage capacity of Cold Archive objects. Unit: bytes.Important An object smaller than 64 KB is calculated as 64 KB. For more information about billing, see Storage fees.Parent node: BucketStatChild node: None |
| ColdArchiveRealStorage | Positive integer | 360 | The actual storage capacity of Cold Archive objects. Unit: bytes.Parent node: BucketStatChild node: None |
| ColdArchiveObjectCount | Positive integer | 36 | The number of Cold Archive objects.Parent node: BucketStatChild node: None |
| ColdArchiveMultipartPartCount | Positive integer | 10 | The number of Cold Archive multipart parts uploaded to the bucket.Parent node: BucketStatChild node: None |
| ColdArchiveMultipartPartStorage | Positive integer | 104857600 | The storage capacity of the Cold Archive multipart parts uploaded to the bucket. Unit: bytes.Parent node: BucketStatChild node: None |
| DeepColdArchiveStorage | Positive integer | 2359296 | The billable storage capacity of Deep Cold Archive objects. Unit: bytes.Important An object smaller than 64 KB is calculated as 64 KB. For more information about billing, see Storage fees.Parent node: BucketStatChild node: None |
| DeepColdArchiveRealStorage | Positive integer | 360 | The actual storage capacity of Deep Cold Archive objects. Unit: bytes.Parent node: BucketStatChild node: None |
| DeepColdArchiveObjectCount | Positive integer | 36 | The number of Deep Cold Archive objects.Parent node: BucketStatChild node: None |
| DeepColdArchiveMultipartPartCount | Positive integer | 10 | The number of Deep Cold Archive multipart parts uploaded to the bucket.Parent node: BucketStatChild node: None |
| DeepColdArchiveMultipartPartStorage | Positive integer | 104857600 | The storage capacity of the Deep Cold Archive multipart parts uploaded to the bucket. Unit: bytes.Parent node: BucketStatChild node: None |


## Examples


-

Sample request


`xml
GET /?stat HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 01:17:29 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`xml
<?xml version="1.0" encoding="UTF-8"?>
<BucketStat>
  <Storage>1600</Storage>
  <ObjectCount>230</ObjectCount>
  <MultipartUploadCount>40</MultipartUploadCount>
  <LiveChannelCount>4</LiveChannelCount>
  <LastModifiedTime>1643341269</LastModifiedTime>
  <StandardStorage>430</StandardStorage>
  <StandardObjectCount>66</StandardObjectCount>
  <InfrequentAccessStorage>2359296</InfrequentAccessStorage>
  <InfrequentAccessRealStorage>360</InfrequentAccessRealStorage>
  <InfrequentAccessObjectCount>54</InfrequentAccessObjectCount>
  <ArchiveStorage>2949120</ArchiveStorage>
  <ArchiveRealStorage>450</ArchiveRealStorage>
  <ArchiveObjectCount>74</ArchiveObjectCount>
  <ColdArchiveStorage>2359296</ColdArchiveStorage>
  <ColdArchiveRealStorage>360</ColdArchiveRealStorage>
  <ColdArchiveObjectCount>36</ColdArchiveObjectCount>
</BucketStat>
`


## SDK


The following software development kits (SDKs) are available for this operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-storage-capacity-of-a-bucket-1)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/query-the-storage-capacity-of-a-bucket-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-query-the-storage-capacity-of-a-bucket)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-query-the-storage-capacity-of-a-bucket)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/get-the-storage-capacity-of-a-storage-space)

## ossutil command-line tool


For more information about the ossutil command for the GetBucketStat operation, see [get-bucket-stat](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-stat).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | You do not have the permission to view the storage capacity information of the bucket. Only the bucket owner can view this information. |


Thank you! We've received your  feedback.