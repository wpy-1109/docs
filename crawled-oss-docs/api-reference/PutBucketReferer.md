# PutBucketReferer

Configures a Referer whitelist or blacklist for an Object Storage Service (OSS) bucket.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM Policy or Bucket Policy.

API

	

Action

	

Definition




PutBucketReferer

	

oss:PutBucketReferer

	

Configures hotlink protection for a bucket.

Request syntax
 
PUT /?referer HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<RefererConfiguration>
  <AllowEmptyReferer>false</AllowEmptyReferer>
  <AllowTruncateQueryString>true</AllowTruncateQueryString>
  <TruncatePath>true</TruncatePath>
  <RefererList>
    <Referer>http://www.aliyun.com</Referer>
    <Referer>https://www.aliyun.com</Referer>
    <Referer>http://www.*.com</Referer>
    <Referer>https://www.?.aliyuncs.com</Referer>
  </RefererList>
  <RefererBlacklist>
    <Referer>http://www.refuse.com</Referer>
    <Referer>https://*.hack.com</Referer>
    <Referer>http://ban.*.com</Referer>
    <Referer>https://www.?.deny.com</Referer>
  </RefererBlacklist>
</RefererConfiguration>
Request elements

Element

	

Type

	

Required

	

Example

	

Description




RefererConfiguration

	

Container

	

Yes

	

N/A

	

The container that stores the hotlink protection configurations.

Child nodes: AllowEmptyReferer, AllowTruncateQueryString, and RefererList

Parent nodes: none




AllowEmptyReferer

	

Enumerated string

	

Yes

	

false

	

Specifies whether to allow a request whose Referer field is empty. Valid values:

true (default)

false

Parent nodes: RefererConfiguration




AllowTruncateQueryString

	

Enumerated string

	

No

	

true

	

Specifies whether to truncate the query string in the URL when the Referer is matched. Valid values:

true

false (default)

Parent nodes: RefererConfiguration




TruncatePath

	

Enumerated string

	

No

	

true

	

Specifies whether to truncate the path and parts that follow the path in the URL when the Referer is matched. Valid values:

true

Important

If TruncatePath is set to true, the value of AllowTruncateQueryString must be also true because the query string follows the path component. When the path is truncated, the query string is also truncated.

false (default)

Parent nodes: RefererConfiguration




RefererList

	

Container

	

Yes

	

N/A

	

The container that stores the Referer whitelist.

Note

The PutBucketReferer operation overwrites the existing Referer whitelist with the Referer whitelist specified in RefererList. If RefererList is not specified in the request, which specifies that no Referer elements are included, the PutBucketReferer operation clears the existing Referer whitelist.

Parent nodes: RefererConfiguration

Child nodes: Referer




RefererBlacklist

	

Container

	

No

	

N/A

	

The container that stores the Referer blacklist.

Note

The PutBucketReferer operation overwrites the existing Referer blacklist with the Referer blacklist specified in RefererBlacklist. If RefererBlacklist is not specified in the request, which specifies that no Referer elements are included, the PutBucketReferer operation clears the existing Referer blacklist.

Parent nodes: RefererConfiguration

Child nodes: Referer




Referer

	

String

	

No

	

http://www.aliyun.com

	

The addresses in the Referer whitelist or blacklist.

Parent nodes: RefererList or RefererBlacklist

For more information about the common request headers in the PutBucketReferer operation, such as Host and Date, see Common request headers.

Response headers

All headers in the response to a PutBucketReferer request are common response headers. For more information, see Common response headers.

Examples

Sample requests

Sample request that does not contain a Referer whitelist or a Referer blacklist

 
PUT /?referer HTTP/1.1
Host: BucketName.oss.example.com
Content-Length: 247
Date: Thu, 17 Apr 2025 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<RefererConfiguration>
  <AllowEmptyReferer>true</AllowEmptyReferer>
  <RefererList/>
</RefererConfiguration>                            

Sample request that contains only a Referer whitelist

 
PUT /?referer HTTP/1.1
Host: BucketName.oss.example.com
Content-Length: 247
Date: Thu, 17 Apr 2025 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<RefererConfiguration>
  <AllowEmptyReferer>false</AllowEmptyReferer>
  <AllowTruncateQueryString>true</AllowTruncateQueryString>
  <TruncatePath>true</TruncatePath>
  <RefererList>
    <Referer>http://www.aliyun.com</Referer>
    <Referer>https://www.aliyun.com</Referer>
    <Referer>http://www.*.com</Referer>
    <Referer>https://www.?.aliyuncs.com</Referer>
  </RefererList>
</RefererConfiguration>                            

Sample request that contains a Referer whitelist and a Referer blacklist

 
PUT /?referer HTTP/1.1
Host: BucketName.oss.example.com
Content-Length: ***
Date: Thu, 17 Apr 2025 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<RefererConfiguration>
  <AllowEmptyReferer>false</AllowEmptyReferer>
  <AllowTruncateQueryString>true</AllowTruncateQueryString>
  <TruncatePath>true</TruncatePath>
  <RefererList>
    <Referer>http://www.aliyun.com</Referer>
    <Referer>https://www.aliyun.com</Referer>
    <Referer>http://www.*.com</Referer>
    <Referer>https://www.?.aliyuncs.com</Referer>
  </RefererList>
  <RefererBlacklist>
    <Referer>http://www.refuse.com</Referer>
    <Referer>https://*.hack.com</Referer>
    <Referer>http://ban.*.com</Referer>
    <Referer>https://www.?.deny.com</Referer>
  </RefererBlacklist>
</RefererConfiguration>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Fri, 04 May 2012 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
x-oss-server-time: 110
OSS SDKs

You can use OSS SDKs for the following programming languages to call the PutBucketReferer operation:

Java

Python V2

Node.js

Go V2

Android

C

C++

.NET

Ruby

ossutil

For information about the ossutil command that corresponds to the PutBucketReferer operation, see put-bucket-referer.

Error codes

Error code

	

HTTP status code

	

Description




AccessDenied

	

403

	

You are not authorized to perform the PutBucketReferer operation. Only the owner of a bucket can initiate PutBucketReferer requests.




InvalidDigest

	

400

	

The Content-MD5 value of the message body calculated by OSS is inconsistent with the Content-MD5 value in the request header. After the Content-MD5 request header is uploaded, OSS calculates the MD5 hash based on the message body and checks whether the calculated MD5 hash is the same as the Content-MD5 value specified in the request header. If the MD5 hashes are inconsistent, this error code is returned.




InlineDataTooLarge

	

400

	

The Referer whitelist and blacklist exceed the upper limit of 20 KB. Reduce the entries in the Referer whitelist and blacklist.