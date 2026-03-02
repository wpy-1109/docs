# Real-time access of Archive objects

Enables or disables real-time access of Archive objects for a bucket.

Usage notes

To enable real-time access of Archive objects for a bucket, you must have the oss:PutBucketArchiveDirectRead permission. For more information, see Attach a custom policy to a RAM user.

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and endpoints, see Regions and endpoints.

After you enable real-time access of Archive objects for a bucket, when you access Archive objects that are not restored in the bucket, you are charged Archive data retrieval fees based on the size of the accessed Archive data (RetrievalDataArchiveDirect). When you access Archive objects that are restored in the bucket, you are not charged Archive data retrieval fees. For more information, see Data processing fees.

Request syntax
 
PUT /?bucketArchiveDirectRead HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Authorization: SignatureValue
Host: BucketName.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<ArchiveDirectReadConfiguration>
    <Enabled>true</Enabled>
</ArchiveDirectReadConfiguration>
Request headers

All headers in a PutBucketArchiveDirectRead request are common request headers. For more information, see Common HTTP headers.

Request elements

Element

	

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

	

Specifies whether to enable real-time access of Archive objects for a bucket. Valid values:

true

false

Response headers

All headers in the response to a PutBucketArchiveDirectRead request are common response headers. For more information about common response headers, see Common HTTP headers.

Examples

Sample request

 
PUT /?bucketArchiveDirectRead HTTP/1.1
Date: Mon, 24 Apr 2023 15:56:37 GMT
Content-Length: 60
Content-Type: application/xml
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Host: oss-example.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<ArchiveDirectReadConfiguration>
    <Enabled>true</Enabled>
</ArchiveDirectReadConfiguration>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Mon, 24 Apr 2023 15:56:37 GMT
Content-Length: 60
Connection: keep-alive
Server: AliyunOSS
ossutil

For information about the ossutil command that corresponds to the PutBucketArchiveDirectRead operation, see put-bucket-archive-direct-read.