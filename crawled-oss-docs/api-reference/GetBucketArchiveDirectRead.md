# Real-time access of Archive objects

Queries whether real-time access of Archive objects is enabled for a bucket.

Usage notes

To check whether real-time access of Archive objects is enabled for a bucket, you must have the oss:GetBucketArchiveDirectRead permission. For more information, see Attach a custom policy to a RAM user.

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see Regions and endpoints.

Request syntax
 
GET /?bucketArchiveDirectRead HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetBucketArchiveDirectRead request are common request headers. For more information, see Common HTTP headers.

Response headers

All headers in the response to a GetBucketArchiveDirectRead request are common response headers. For more information about common response headers, see Common HTTP headers.

Header

	

Type

	

Required

	

Example

	

Description




ArchiveDirectReadConfiguration

	

Container

	

Yes

	

N/A

	

The container that stores the configurations for real-time access of Archive objects.




Enabled

	

Boolean

	

Yes

	

true

	

Indicates whether real-time access of Archive objects is enabled for the bucket. Valid values:

true

false

Examples

Sample request

 
GET /?bucketArchiveDirectRead HTTP/1.1 
Host: oss-example.oss-cn-hangzhou.aliyuncs.com 
Date: Mon, 24 Apr 2023 15:56:37 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample response

 
GET /?bucketArchiveDirectRead HTTP/1.1
Date: Mon, 24 Apr 2023 15:56:37 GMT
Content-Length: 60
Content-Type: application/xml
Authorization: OSS qn6q**************:77Dv****************
Host: oss-example.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<ArchiveDirectReadConfiguration>
    <Enabled>true</Enabled>
</ArchiveDirectReadConfiguration>
ossutil

For information about the ossutil command that corresponds to the GetBucketArchiveDirectRead operation, see get-bucket-archive-direct-read.