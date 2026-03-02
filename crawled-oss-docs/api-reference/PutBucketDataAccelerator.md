# OSS accelerator

You can call the PutBucketDataAccelerator operation to create an OSS accelerator or modify its configuration.

Usage notes

The OSS accelerator API can only be called in an internal network environment in the same region as OSS. You must use the corresponding accelerator domain name. For example, you can use an ECS instance in the Ulanqab region, which is the same region as OSS, to operate the OSS accelerator using the API. The following table lists the supported zones and corresponding OSS accelerator domain names for each region.

Region

	

Zone

	

OSS accelerator domain name




Beijing

	

cn-beijing-h

	

cn-beijing-h-internal.oss-data-acc.aliyuncs.com




Shanghai

	

cn-shanghai-g

	

cn-shanghai-g-internal.oss-data-acc.aliyuncs.com




Shenzhen

	

cn-shenzhen-c

	

cn-shenzhen-c-internal.oss-data-acc.aliyuncs.com




Hangzhou

	

cn-hangzhou-j

	

cn-hangzhou-j-internal.oss-data-acc.aliyuncs.com




Ulanqab

	

cn-wulanchabu-b

	

cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com




Singapore

	

ap-southeast-1c

	

ap-southeast-1c-internal.oss-data-acc.aliyuncs.com

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM Policy or Bucket Policy.

API

	

Action

	

Description




PutBucketDataAccelerator

	

oss:PutBucketDataAccelerator

	

Creates a bucket accelerator or modifies its configuration.

Request syntax
 
PUT /?dataAccelerator HTTP/1.1
Date: GMT Date
Content-Length：ContentLength
Content-Type: application/xml
Authorization: SignatureValue 
Host: BUCKETNAME.cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com

<DataAcceleratorConfiguration>
  <AvailableZone>cn-wulanchabu-b</AvailableZone>
  <Quota>200</Quota>
  <AcceleratePaths>
    <DefaultCachePolicy>write-back</DefaultCachePolicy>
    <Path>
      <Name>AccelerationPath</Name>
      <CachePolicy>sync-warmup</CachePolicy>
    </Path>
  </AcceleratePaths>
</DataAcceleratorConfiguration>
Request headers

This operation uses common request headers. For more information, see Common Request Headers.

Request parameters

Name

	

Type

	

Required

	

Example

	

Description




dataAccelerator

	

string

	

Yes

	

None

	

The identifier parameter for OSS accelerator API operations. This parameter can have any value.

Request body

Name

	

Type

	

Required

	

Example

	

Description




DataAcceleratorConfiguration

	

Container

	

Yes

	

N/A

	

The container for accelerator configuration

Child nodes:

AvailableZone

Quota

AcceleratePaths

Parent node: None




AvailableZone

	

string

	

Yes

	

cn-wulanchabu-b

	

The zone of the accelerator. Currently supported zones:

cn-beijing-h (Beijing)

cn-shanghai-g (Shanghai)

cn-shenzhen-c (Shenzhen)

cn-hangzhou-j (Hangzhou)

cn-wulanchabu-b (Ulanqab)

ap-southeast-1c (Singapore)




Quota

	

Positive integer

	

Yes

	

100

	

The capacity of the accelerator in GB.

The accelerator capacity cannot be modified again within one hour after creation or modification.




AcceleratePaths

	

Container

	

Yes

	

N/A

	

The container for acceleration policy configuration

Child nodes:

DefaultCachePolicy

Path

Parent node:

DataAcceleratorConfiguration




Path

	

Container

	

No

	

N/A

	

The container for acceleration path configuration

Child nodes:

Name

CachePolicy

Parent node:

AcceleratePaths




Name

	

string

	

Yes

	

test/dir/

	

The specified acceleration path prefix

Child nodes: None

Parent node: Path




CachePolicy

	

string

	

Yes

	

sync-warmup, write-back

	

The acceleration policy for the path. Available acceleration policies:

sync-warmup (synchronous warm-up when writing)

write-back (warm-up when reading)

Child nodes: None

Parent node: Path




DefaultCachePolicy

	

string

	

Yes

	

sync-warmup, write-back

	

The default acceleration policy for the entire bucket. This policy takes effect only when no Path is configured. Available acceleration policies:

sync-warmup (synchronous warm-up when writing)

write-back (warm-up when reading)

Child nodes: None

Parent node: AcceleratePaths

Response headers

This operation uses common response headers. For more information, see Common Response Headers.

Examples

Create an OSS accelerator

Request example

 
PUT /?dataAccelerator= HTTP/1.1
Date: Sun, 05 Sep 2021 23:00:00 GMT
Content-Length: 556
Content-Type: application/xml
Authorization: OSS4-HMAC-SHA256 Credential=****
Host: http://BUCKETNAME.cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com

<DataAcceleratorConfiguration>
  <AvailableZone>cn-wulanchabu-b</AvailableZone>
  <Quota>200</Quota>
  <AcceleratePaths>
    <DefaultCachePolicy>write-back</DefaultCachePolicy>
    <Path>
      <Name>AccelerationPath</Name>
      <CachePolicy>sync-warmup</CachePolicy>
    </Path>
  </AcceleratePaths>
</DataAcceleratorConfiguration>

Response example

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 27 Jun 2025 02:19:45 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 685DFFC18AB8A63132C65285
Error codes

Error code

	

HTTP status code

	

Description




TooManyAccelerationPolicyPaths

	

400

	

Too many acceleration paths are configured.




InvalidCachePathPolicy

	

400

	

The acceleration policy is invalid.




InvalidQuota

	

400

	

The accelerator capacity is invalid.




DataAcceleratorQuotaFrozen

	

403

	

The accelerator capacity is locked and cannot be modified.




DataAcceleratorAvailableZoneNotSupported

	

400

	

The accelerator cannot be created in this zone.