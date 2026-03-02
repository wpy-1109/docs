# GetBucketReferer

Queries the Referer configurations of a bucket.

Note

The oss:GetBucketReferer permission is required for querying the Referer configurations of a bucket. For more information, see Attach a custom policy to a RAM user.

Request syntax
 
GET /?referer HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response elements

Element

	

Type

	

Example

	

Description




RefererConfiguration

	

Container

	

N/A

	

The container that stores the Referer configurations.

Parent nodes: none

Child nodes: AllowEmptyReferer, AllowTruncateQueryString, and RefererList




AllowEmptyReferer

	

Enumerated string

	

false

	

Indicates whether requests with empty Referer fields are allowed. Valid values:

true

false

Parent nodes: RefererConfiguration




AllowTruncateQueryString

	

Enumerated string

	

true

	

Indicates whether the query string in the URL is truncated. Valid values:

true

false

Parent nodes: RefererConfiguration




TruncatePath

	

Enumerated string

	

true

	

Indicates whether the path and parts that follow the path in the URL are truncated. Valid values:

true

false

Parent nodes: RefererConfiguration




RefererList

	

Container

	

N/A

	

The container that stores the Referer whitelist.

Parent nodes: RefererConfiguration

Child nodes: Referer




RefererBlacklist

	

Container

	

N/A

	

The container that stores the Referer blacklist.

Parent nodes: RefererConfiguration

Child nodes: Referer




Referer

	

String

	

http://www.aliyun.com

	

The addresses in the Referer whitelist or blacklist.

Parent nodes: RefererList or RefererBlacklist

For more information about common response headers in the GetBucketReferer operation, such as Date and x-oss-request-id, see Common HTTP headers.

Examples

Sample requests

 
Get /?referer HTTP/1.1
Host: oss-example.oss.aliyuncs.com  
Date: Thu, 13 Sep 2012 07:51:28 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample success responses

Sample response that does not contain a Referer whitelist or a Referer blacklist

Note

If the bucket does not have a Referer whitelist or a Referer blacklist, Object Storage Service (OSS) returns the default value of AllowEmptyReferer and an empty RefererList.

 
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906****
Date: Thu, 13 Sep 2012 07:56:46 GMT
Connection: keep-alive
Content-Length: ***  
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<RefererConfiguration>
  <AllowEmptyReferer>true</AllowEmptyReferer>
  < RefererList />
</RefererConfiguration>

Sample response that contains only a Referer whitelist

 
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906****
Date: Thu, 13 Sep 2012 07:51:28 GMT
Connection: keep-alive
Content-Length: 218  
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<RefererConfiguration>
  <AllowEmptyReferer>true</AllowEmptyReferer>
  <AllowTruncateQueryString>true</AllowTruncateQueryString>
  <TruncatePath>true</TruncatePath>
  <RefererList>
    <Referer>http://www.aliyun.com</Referer>
    <Referer>https://www.aliyun.com</Referer>
    <Referer>http://www.*.com</Referer>
    <Referer>https://www.?.aliyuncs.com</Referer>
  </RefererList>
</RefererConfiguration>

Sample response that contains a Referer whitelist and a Referer blacklist

 
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906****
Date: Thu, 13 Sep 2012 07:51:28 GMT
Connection: keep-alive
Content-Length: ***
Server: AliyunOSS
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
OSS SDKs

You can use OSS SDKs for the following programming languages to call the GetBucketReferer operation:

Java

PHP

Python

Go V2

C

.NET

Node.js

Ruby

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucket

	

404

	

The error message returned because the bucket does not exist.




AccessDenied

	

403

	

You do not have the permissions to query the Referer configurations of the bucket. Only the bucket owner can query the Referer configurations of the bucket.