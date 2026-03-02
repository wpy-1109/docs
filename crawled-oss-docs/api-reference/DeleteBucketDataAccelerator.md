# OSS accelerator

Call the DeleteBucketDataAccelerator operation to delete an OSS accelerator.

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




DeleteBucketDataAccelerator

	

oss:DeleteBucketDataAccelerator

	

Deletes a bucket accelerator.

Request syntax
 
DELETE /?dataAccelerator=&x-oss-datalake-cache-available-zone=cn-wulanchabu-b HTTP/1.1
Date: GMT Date
Content-Length：ContentLength
Authorization: SignatureValue 
Host: BUCKETNAME.cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com
Request headers

This operation involves common request headers. For more information, see Common Request Headers.

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

	

The identity parameter for OSS accelerator API operations. This parameter can have any value.




x-oss-datalake-cache-available-zone

	

string

	

Yes

	

cn-wulanchabu-b

	

Specifies the zone in which to delete the accelerator for the bucket.

Response headers

This operation involves common response headers. For more information, see Common Response Headers.

Examples

Delete the OSS accelerator for the target bucket in the specified zone in the Ulanqab region.

Sample request

 
DELETE /?dataAccelerator=&x-oss-datalake-cache-available-zone=cn-wulanchabu-b HTTP/1.1
Date: Sun, 05 Sep 2021 23:00:00 GMT
Content-Length: 556
Authorization: OSS4-HMAC-SHA256 Credential=****
Host: http://BUCKETNAME.cn-wulanchabu-b-internal.oss-data-acc.aliyuncs.com

Sample response

 
HTTP/1.1 204 No Content
Server: AliyunOSS
Date: Fri, 27 Jun 2025 03:32:05 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 685E10B48AB8A632320CAC86
Error codes

Error code

	

HTTP status code

	

Description




NoSuchConfiguration

	

404

	

The accelerator is not enabled for the current bucket in the corresponding zone.