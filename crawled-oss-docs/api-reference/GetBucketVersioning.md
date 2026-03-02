# GetBucketVersioning

You can call this operation to query the versioning state of a bucket.

Request syntax
 
GET /? versioning HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Example

	

Description




VersioningConfiguration

	

Container

	

N/A

	

The container that stores the versioning state of the bucket.

Child nodes: Status

Parent nodes: none




Status

	

String

	

Enabled

	

The versioning state of the bucket.

Parent nodes: VersioningConfiguration

Valid values:

Enabled: indicates that versioning is enabled for the bucket.

Suspended: indicates that versioning is suspended for the bucket.

Note

If versioning is not enabled for a bucket, the Status element is not contained in the response elements.

Examples

Sample request

 
GET /?versioning HTTP/1.1
Host: bucket-versioning.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 02:28:18 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample responses

Sample response for a bucket for which versioning is enabled

 
HTTP/1.1 200 OK
x-oss-request-id: 5CAC0342B7AEADE01700****
Date: Tue, 09 Apr 2019 02:28:18 GMT 
Content-Length: 121
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<? xml version="1.0" encoding="UTF-8"? >
<VersioningConfiguration>
    <Status>Enabled</Status>
</VersioningConfiguration>

Sample response for a bucket for which versioning is disabled

If versioning is disabled for the requested bucket, the versioning state of the bucket is not contained in the XML body of the response.

 
HTTP/1.1 200 OK
x-oss-request-id: 5CAC015CB7AEADE01700****
Date: Tue, 09 Apr 2019 02:20:12 GMT 
Content-Length: 74
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<VersioningConfiguration xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com"/>
OSS SDKs

You can use OSS SDKs for the following programming languages to call the GetBucketVersioning operation:

Java

Python

Go V2

C++

.NET

Node.js

ossutil

For information about the ossutil command that corresponds to the GetBucketVersioning operation, see get-bucket-versioning.

Error codes

Error code

	

HTTP status code

	

Description




AccessDenied

	

403

	

The error message returned because you do not have permissions to query the versioning state of the bucket.

Only the bucket owner or RAM users that have the GetBucketVersioning permission can query the versioning state of a bucket.




NoSuchBucket

	

404

	

The error message returned because the specified bucket does not exist.