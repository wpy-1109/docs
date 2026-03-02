# DeleteCname

Deletes the CNAME record that is mapped to a bucket.

Request syntax
 
POST /?cname&comp=delete HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Content-Type: application/xml
Content-Length: 186
Date: GMT Date
Authorization: SignatureValue
Request headers

The request headers in a RestoreObject request are only common request headers. For more information, see Common request headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




BucketCnameConfiguration

	

Container

	

Yes

	

N/A

	

The container that stores the CNAME record.

Parent nodes: none

Child nodes: Cname




Cname

	

Container

	

Yes

	

N/A

	

The container in which the CNAME information is stored.

Parent nodes: BucketCnameConfiguration

Child nodes: Domain




Domain

	

String

	

Yes

	

example.com

	

The custom domain name.

Parent nodes: Cname

Child nodes: none

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples

Sample request

 
POST /?cname&comp=delete HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Type: application/xml
Content-Length: 186
Date: Thu, 17 Apr 2025 15:39:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<BucketCnameConfiguration>
  <Cname>
    <Domain>example.com</Domain>
  </Cname>
</BucketCnameConfiguration>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D
Date: Mon, 26 Jul 2021 13:08:38 GMT
Content-Length: 118
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call DeleteCname:

Java

Python V2

Go V2

Node.js

PHP V2

ossutil

For information about the ossutil command that corresponds to the DeleteCname operation, see delete-cname.

Error codes

Error code

	

HTTP status code

	

Description




AccessDenied

	

403

	

The error message returned because you do not have the permissions to call the DeleteCname operation. Only the bucket owner and RAM users that are granted the oss:DeleteCname permission can delete the CNAME records mapped to the bucket.




NoSuchCname

	

404

	

The error message returned because no CNAME record is mapped to the bucket.