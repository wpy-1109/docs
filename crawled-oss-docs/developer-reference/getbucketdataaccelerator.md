# GetBucketDataAccelerator

Call the GetBucketDataAccelerator operation to query OSS accelerator information.

## Usage notes


The OSS accelerator API can only be called in an internal network environment in the same region as OSS. You must use the corresponding accelerator domain name. For example, you can use an ECS instance in the Ulanqab region, which is the same region as OSS, to operate the OSS accelerator using the API. The following table lists the supported zones and corresponding OSS accelerator domain names for each region.















































| Region | Zone | OSS accelerator domain name |
| --- | --- | --- |
| Beijing | cn-beijing-h | cn-beijing-h-internal.oss-data-acc.aliyuncs.com |
| Shanghai | cn-shanghai-g | cn-shanghai-g-internal.oss-data-acc.aliyuncs.com |
| Shenzhen | cn-shenzhen-c | cn-shenzhen-c-internal.oss-data-acc.aliyuncs.com |
| Hangzhou | cn-hangzhou-j | cn-hangzhou-j-internal.oss-data-acc.aliyuncs.com |
| Ulanqab | cn-wulanchabu-b | cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com |
| Singapore | ap-southeast-1c | ap-southeast-1c-internal.oss-data-acc.aliyuncs.com |


## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).














| API | Action | Description |
| --- | --- | --- |
| GetBucketDataAccelerator | oss:GetBucketDataAccelerator | View bucket accelerator information. |


## Request syntax


`http
GET /?dataAccelerator=&x-oss-datalake-cache-available-zone=cn-wulanchabu-b&verbose= HTTP/1.1
Date: GMT Date
Content-Length：ContentLength
Content-Type: application/xml
Authorization: SignatureValue
Host: BUCKETNAME.cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com
`


## Request headers


This operation uses common request headers. For more information, see [Common Request Headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request parameters





| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| dataAccelerator | string | Yes | None | The identifier parameter for OSS accelerator API operations. This parameter can have any value. |
| x-oss-datalake-cache-available-zone | string | No | cn-wulanchabu-b | If this parameter exists, it specifies to view accelerator information for a specific zone.Otherwise, all accelerator information for the bucket is returned. |
| verbose | string | No | None | If this parameter exists, it specifies to view all acceleration path information. Otherwise, only basic accelerator information is returned without acceleration path information.This parameter can have any value. |


## Response headers


This operation uses common response headers. For more information, see [Common Response Headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














































































































| Name | Type | Example | Description |
| --- | --- | --- | --- |
| DataAccelerator | container | None | The container that stores accelerator information configured for the bucket.Child nodes:NameBucketBasicInfomationParent nodes: none |
| Name | string | mybucket_data-acc | The name of the accelerator.Child nodes: noneParent nodes: DataAccelerator |
| BucketName | string | mybucket | The name of the bucket.Child nodes: noneParent nodes: DataAccelerator |
| BasicInfomation | container | None | The container that stores information about a specific accelerator.Child nodes:AvailableZoneQuotaAcceleratePathsCreationDateQuotaFrozenUntilParent nodes:DataAccelerator |
| Quota | positive integer | 100 | The capacity of the accelerator.Child nodes: noneParent nodes: BasicInfomation |
| AvailableZone | string | cn-wulanchabu-b | The zone of the accelerator.Child nodes: noneParent nodes: BasicInfomation |
| CreationDate | positive integer | 123456789123 | The timestamp when the accelerator was created.Child nodes: noneParent nodes: BasicInfomation |
| QuotaFrozenUntil | positive integer | 123456789123 | The timestamp when the accelerator quota will be unfrozen. The quota cannot be modified before this timestamp.Child nodes: noneParent nodes: BasicInfomation |
| AcceleratePaths | container | None | The container that stores acceleration policy configurations.Child nodes:DefaultCachePolicyPathParent nodes:BasicInfomation |
| Path | container | None | The container that stores acceleration path configurations.Child nodes:CachePolicyNameParent nodes: AcceleratePaths |
| Name | string | test/dir/ | The specified acceleration path prefix.Child nodes: noneParent nodes: Path |
| CachePolicy | string | sync-warmup, write-back | The acceleration policy for the path. The value must be one of the following parameters, otherwise the acceleration policy does not take effect.sync-warmup (synchronous warm-up during write)write-back (warm-up during read)Child nodes: noneParent nodes: Path |
| DefaultCachePolicy | string | sync-warmup, write-back | The acceleration policy for the entire bucket. The value must be one of the following parameters.sync-warmup (synchronous warm-up during write)write-back (warm-up during read)Child nodes: noneParent nodes: AcceleratePaths |


## Examples


Query the OSS accelerator configuration information for the target bucket in the China (Ulanqab) region.


-

Sample request


`http
GET /?dataAccelerator=&x-oss-datalake-cache-available-zone=cn-wulanchabu-b&verbose= HTTP/1.1
Date: Sun, 05 Sep 2021 23:00:00 GMT
Content-Length: 556
Authorization: OSS4-HMAC-SHA256 Credential=
Host: http://BUCKETNAME.cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com
`


-

Sample response


`http
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 27 Jun 2025 02:57:27 GMT
Content-Type: application/xml
Content-Length: 459
Connection: keep-alive
x-oss-request-id: 685E08978AB8A63836D81586

<?xml version="1.0" encoding="UTF-8"?>
<DataAccelerator>
  <Name>mybucket_data-acc</Name>
  <BucketName>mybucket</BucketName>
  <BasicInfomation>
    <Quota>200</Quota>
    <AvailableZone>cn-wulanchabu-b</AvailableZone>
    <AcceleratePaths>
      <Path>
        <Name>AccelerationPath</Name>
        <CachePolicy>sync-warmup</CachePolicy>
      </Path>
      <DefaultCachePolicy>write-back</DefaultCachePolicy>
    </AcceleratePaths>
    <CreationDate>1751013420658</CreationDate>
    <QuotaFrozenUntil>1751017020624</QuotaFrozenUntil>
  </BasicInfomation>
</DataAccelerator>
`


## Error codes


| Error code | HTTP status code | Description |
| --- | --- | --- |
| DataAcceleratorNotFound | 404 | The current bucket does not have any accelerators enabled. |
| NoSuchConfiguration | 404 | The current bucket does not have an accelerator enabled in the corresponding zone. |


Thank you! We've received your  feedback.