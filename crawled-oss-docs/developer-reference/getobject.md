# Object Storage Service GetObject API

Retrieves an object from a bucket. To call this operation, you must have read permissions on the object.

## Request syntax


`http
GET /ObjectName HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Range: bytes=ByteRange (optional)
If-Modified-Since: GMT Date (optional)
If-Unmodified-Since: GMT Date (optional)
If-Match: ETag (optional)
If-None-Match: ETag (optional)
Accept-Encoding: encoding (optional)
x-oss-multi-range-behavior: multi-range (optional)
`


For information about how to calculate the signature for the Authorization header, see [Authorization request header](https://www.alibabacloud.com/help/en/oss/developer-reference/recommend-to-use-signature-version-4#c14032b6692nr).


When you download large objects (larger than 100 MB) from OSS, the transfer can fail due to network issues. You can use HTTP Range requests to retrieve a large object in parts. This approach enables resumable and concurrent downloads and improves transfer reliability. For more information, see [How to obtain OSS resources in segments using HTTP Range requests](https://www.alibabacloud.com/help/en/oss/how-to-obtain-oss-resources-by-segmenting-http-range-requests).

## Usage notes


The GetObject operation supports access over both HTTP and HTTPS by default. It also supports multi-range downloads, which let you specify multiple byte ranges in a single request to improve download efficiency.


-

To allow access only over HTTPS, you can use a [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/) to grant access.

-

If the object is in the Archive storage class, you must first send a RestoreObject request or enable real-time access of Archive objects for the bucket before you can download the object.

-

The GetObject operation is compatible with standard RFC protocols.

## Permissions


By default, an Alibaba Cloud account has full permissions on all resources within the account. However, Resource Access Management (RAM) users and RAM roles do not have any permissions by default. The Alibaba Cloud account owner or an administrator must grant permissions to RAM users or RAM roles by using a [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or a [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).


The following table lists the required permissions.


























| API | Action | Description |
| --- | --- | --- |
| GetObject | oss:GetObject | Downloads an object. |
|  | oss:GetObjectVersion | Required when you download a specific version of an object by specifying versionId. |
|  | kms:Decrypt | Required when the object metadata contains X-Oss-Server-Side-Encryption: KMS. |


## Request parameters

### Request headers


OSS supports custom response headers in GET requests. When a request succeeds and returns `200 OK`, the response headers are set to the values that you specify in the request.
OSS does not support custom response headers in GET requests for anonymous access.


































| Name | Type | Required | Description |
| --- | --- | --- | --- |
| Range | String | No | The byte range of the object to retrieve. Specify the range in the format bytes=start-end. For example, bytes=0-9 retrieves the first 10 bytes. When the x-oss-multi-range-behavior header is set to multi-range, you can specify multiple ranges separated by commas. For example, bytes=0-1,3-4,5-6,7-8. A maximum of 50 range intervals are supported. If the specified range is valid, OSS returns a 206 Partial Content response that includes a Content-Range header indicating the total size and the returned range (for example, Content-Range: bytes 0-9/44). If the specified range is invalid, the entire object is returned and the response does not include a Content-Range header. Default value: none |
| x-oss-multi-range-behavior | String | No | Enables the multi-range download feature. Set this header to multi-range to specify multiple byte ranges in the Range header. If the specified range is invalid, the entire object is returned. Default value: none |
| If-Modified-Since | String | No | A conditional header. If the specified time is earlier than the actual last-modified time of the object, or the specified time is invalid, OSS returns the object with a 200 OK status. If the specified time is the same as or later than the actual last-modified time, OSS returns 304 Not Modified. Format: GMT (for example, Fri, 13 Nov 2015 14:47:53 GMT). You can use this header together with If-Unmodified-Since. Default value: none |
| If-Unmodified-Since | String | No | A conditional header. If the specified time is the same as or later than the actual last-modified time of the object, OSS returns the object with a 200 OK status. If the specified time is earlier than the actual last-modified time, OSS returns 412 Precondition Failed. Format: GMT (for example, Fri, 13 Nov 2015 14:47:53 GMT). You can use this header together with If-Modified-Since. Default value: none |
| If-Match | String | No | A conditional header. If the ETag you provide matches the ETag of the object, OSS returns the object with a 200 OK status. If the ETag does not match, OSS returns 412 Precondition Failed. The ETag of an object is used to check whether the content of the object has changed. You can use the ETag value to verify data integrity. You can use this header together with If-None-Match. Default value: none |
| If-None-Match | String | No | A conditional header. If the ETag you provide does not match the ETag of the object, OSS returns the object with a 200 OK status. If the ETag matches, OSS returns 304 Not Modified. You can use this header together with If-Match. Default value: none |
| Accept-Encoding | String | No | The encoding type that the client accepts. To receive the response in Gzip compressed format, set this header to gzip (for example, Accept-Encoding: gzip). OSS determines whether to apply Gzip compression based on the Content-Type and size of the object. Gzip compression is applied only when both of the following conditions are met: the object size is at least 1 KB, and the Content-Type is one of the supported types. If Gzip compression is applied, the response does not include the ETag or Content-Length headers. Supported Content-Type values: text/cache-manifest, text/xml, text/css, text/html, text/plain, application/javascript, application/x-javascript, application/rss+xml, application/json, text/json. Default value: none |


### Query parameters


You can use the following query parameters to override certain response headers. These parameters require a signed request and are not supported for anonymous access.





























| Name | Type | Required | Description |
| --- | --- | --- | --- |
| response-content-language | String | No | Specifies the Content-Language header that OSS returns in the response. Default value: none |
| response-expires | String | No | Specifies the Expires header that OSS returns in the response. Default value: none |
| response-cache-control | String | No | Specifies the Cache-Control header that OSS returns in the response. Default value: none |
| response-content-disposition | String | No | Specifies the Content-Disposition header that OSS returns in the response. Default value: none |
| response-content-encoding | String | No | Specifies the Content-Encoding header that OSS returns in the response. Default value: none |


## Response parameters

### Response headers














| Name | Type | Description |
| --- | --- | --- |
| x-oss-server-side-encryption | String | If the object is stored with server-side encryption, the object is automatically decrypted and returned when you send a GET request. This header indicates the server-side encryption algorithm used for the object. |
| x-oss-sealed-time | String | If the object is an appendable object on which the Seal operation has been performed, this header indicates the time when the Seal operation was performed. The value format is Sat, 11 Oct 2025 06:41:42 GMT. |
| x-oss-tagging-count | String | The number of tags associated with the object. This header is returned only if you have the permissions to read tags. |
| x-oss-expiration | String | The expiration time of the object based on lifecycle rules configured for the bucket. The behavior of this header depends on the versioning state of the bucket. |


### Symbolic link behavior


If the requested object is a symbolic link, the response contains the content of the target object. The following rules apply to the response headers:


-

`Content-Length`, `ETag`, and `Content-MD5` reflect the metadata of the target object.

-

`Last-Modified` is set to the most recent modification time between the target object and the symbolic link.

-

All other headers reflect the metadata of the symbolic link itself.

### Folder object behavior


When the requested object is a folder, custom response headers such as Range in the request are ignored. The response has the following characteristics:


-

`Content-Type: application/x-directory`

-

`Content-Length: 0`

-

`ETag: "null"`

## Versioning


By default, a GetObject request returns only the current version of an object. You can retrieve a specific version by including the `versionId` query parameter.


-

No versionId specified: Returns the current version of the object.

-

versionId specified: Returns the specified version.

-

versionId set to null: Returns the version that has a null versionId.


If the current version of the object is a delete marker and you do not specify a versionId, OSS returns a `404 Not Found` error with the `x-oss-delete-marker: true` header. If you specify the versionId of a delete marker, OSS returns a `405 Method Not Allowed` error with the `Allow: DELETE` header.

### x-oss-expiration behavior


The `x-oss-expiration` response header indicates the expiration time of an object based on lifecycle rules. Its behavior depends on the versioning state of the bucket:














| Versioning state | Request includes versionId | Object matches lifecycle delete rule | x-oss-expiration returned |
| --- | --- | --- | --- |
| Enabled | No | Yes | Yes |
| Enabled | Yes | Yes or No | No |
| Not enabled | N/A | Yes | Yes |
| Not enabled | N/A | No | No |


## Multi-range download


Multi-range download allows you to retrieve multiple byte ranges of an object in a single request. This feature is useful for scenarios that require selective data retrieval.


To enable multi-range download, include the `x-oss-multi-range-behavior: multi-range` request header. The following rules apply:


-

A maximum of 50 range intervals can be specified per request.

-

If any specified range is invalid, the entire object is returned.

-

The response uses the `multipart/byteranges` content type with a boundary delimiter separating each range segment.

### Billing and throttling


When you use the multi-range feature, both billing and throttling calculations account for the number of byte-range segments in each request:


-

Billing: The number of GetObject API calls for billing equals the number of API calls multiplied by the number of byte-range segments per call.

-

Throttling: The same logic applies. The number of GetObject API calls counted toward throttling equals the number of API calls multiplied by the number of byte-range segments per call.

## Examples

### Basic download


Request


`http
GET /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 06:38:30 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response (object is a file)


`http
HTTP/1.1 200 OK
x-oss-request-id: 3a8f-2e2d-7965-3ff9-51c875b*
x-oss-object-type: Normal
Date: Fri, 24 Feb 2012 06:38:30 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
ETag: "5B3C1A2E0563E1B002CC607C*"
Content-Type: image/jpg
Content-Length: 344606
Server: AliyunOSS
[344606 bytes of object data]
`


Response (object is a folder)


When the object is a folder, custom request headers such as Range are ignored.


`http
HTTP/1.1 200 OK
x-oss-request-id: 3a8f-2e2d-7965-3ff9-51c875b*
x-oss-object-type: Normal
Date: Wed, 31 Mar 2021 06:38:30 GMT
Last-Modified: Tue, 30 Mar 2021 06:07:48 GMT
ETag: "null"
Content-Type: application/x-directory
Content-Length: 0
Server: AliyunOSS
`


### Range download


Request


`http
GET /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 28 Feb 2012 05:38:42 GMT
Range: bytes=100-900
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 206 Partial Content
x-oss-request-id: 28f6-15ea-8224-234e-c0ce407*
x-oss-object-type: Normal
Date: Fri, 28 Feb 2012 05:38:42 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
ETag: "5B3C1A2E05E1B002CC607C*"
Accept-Ranges: bytes
Content-Range: bytes 100-900/344606
Content-Type: image/jpg
Content-Length: 801
Server: AliyunOSS
[801 bytes of object data]
`


### Multi-range download


Request


`http
GET /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 28 Feb 2012 05:38:42 GMT
Range: bytes=0-1,3-4,5-6,7-8
x-oss-multi-range-behavior: multi-range
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 206 Partial Content
x-oss-request-id: 28f6-15ea-8224-234e-c0ce407*
x-oss-object-type: Normal
Date: Fri, 28 Feb 2012 05:38:42 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
ETag: "5B3C1A2E05E1B002CC607C*"
Accept-Ranges: bytes
Content-Type: multipart/byteranges;boundary=63ce7776-c104-417f-8a65-ccaa3b17f428
Content-Length: 446
Server: AliyunOSS

--63ce7776-c104-417f-8a65-ccaa3b17f428
Content-type: text/plain
Content-range: bytes 0-1/10

[ 2 Bytes object content]
--63ce7776-c104-417f-8a65-ccaa3b17f428
Content-type: text/plain
Content-range: bytes 3-4/10

[ 2 Bytes object content]
--63ce7776-c104-417f-8a65-ccaa3b17f428
Content-type: text/plain
Content-range: bytes 5-6/10

[ 2 Bytes object content]
--63ce7776-c104-417f-8a65-ccaa3b17f428
Content-type: text/plain
Content-range: bytes 7-8/10

[ 2 Bytes object content]
--63ce7776-c104-417f-8a65-ccaa3b17f428--
`


### Custom response headers


Request


`http
GET /oss.jpg?response-expires=Thu%2C%2001%20Feb%202012%2017%3A00%3A00%20GMT&response-cache-control=No-cache&response-content-disposition=attachment%253B%2520filename%253Dtesting.txt&response-content-encoding=utf-8&response-content-language=%E4%B8%AD%E6%96%87 HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com:
Date: Fri, 24 Feb 2012 06:09:48 GMT
`


Response


`http
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC75A644*
x-oss-object-type: Normal
Date: Fri, 24 Feb 2012 06:09:48 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
ETag: "5B3C1A2E053D1B002CC607*"
Content-Length: 344606
Connection: keep-alive
Content-disposition: attachment; filename=testing.txt
Content-language: Chinese
Content-type: jpg
Cache-control: no-cache
Expires: Fri, 24 Feb 2012 17:00:00 GMT
Server: AliyunOSS
[344606 bytes of object data]
`


### Symbolic link object


Request


`http
GET /link-to-oss.jpg HTTP/1.1
Accept-Encoding: identity
Date: Tue, 08 Nov 2016 03:17:58 GMT
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 08 Nov 2016 03:17:58 GMT
Content-Type: application/octet-stream
Content-Length: 20
Connection: keep-alive
x-oss-request-id: 582143E6A212AD*
Accept-Ranges: bytes
ETag: "8086265EFC021F9A2F09BF4"
Last-Modified: Tue, 08 Nov 2016 03:17:58 GMT
x-oss-object-type: Symlink
Content-MD5: gIYmXvwCEe0fmi8Jv0Y
`


### Archive object (restored)


Request


`http
GET /oss.jpg HTTP/1.1
Host: oss-archive-example.oss-cn-hangzhou.aliyuncs.com
Date: Sat, 15 Apr 2017 09:38:30 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 200 OK
x-oss-request-id: 58F723829F29F18D7F00*
x-oss-object-type: Normal
x-oss-restore: ongoing-request="false", expiry-date="Sun, 16 Apr 2017 08:12:33 GMT"
Date: Sat, 15 Apr 2017 09:38:30 GMT
Last-Modified: Sat, 15 Apr 2017 06:07:48 GMT
ETag: "5B3C1A2E0763E1B002CC607C*"
Content-Type: image/jpg
Content-Length: 344606
Server: AliyunOSS
[344606 bytes of object data]
`


### Versioning scenarios

#### Specify a version ID


Request


`http
GET /example?versionId=CAEQNhiBgMDJgZCA0BYiIDc4MGZjZGI2OTBjOTRmNTE5NmU5NmFhZjhjYmY0 HTTP/1.1
Host: versioning-get.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 02:58:06 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 200 OK
x-oss-request-id: 5CAC0A3EDE0170*
x-oss-version-id: CAEQNhiBgM0BYiIDc4MGZjZGI2OTBjOTRmNTE5NmU5NmFhZjhjYmY*
x-oss-object-type: Normal
Date: Tue, 17 Apr 2025 02:58:06 GMT
Last-Modified: Fri, 22 Mar 2018 08:07:50 GMT
ETag: "5B3C1A2E053D7002CC607C5A*"
Content-Type: text/html
Content-Length: 362149
Server: AliyunOSS
[362149 bytes of object data]
`


#### Current version is a delete marker


Request


`http
GET /example HTTP/1.1
Host: versioning-get.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 17 Apr 2025 03:22:33 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 404 Not Found
x-oss-request-id: 5CAC0FEADE0170*
x-oss-delete-marker: true
x-oss-version-id: CAEQNxiBgyA0BYiIDc4ZDdmNTA2MGViZTRiNjE5NzZlZWM4OWM5OT*
Date: Tue, 17 Apr 2025 03:22:33 GMT
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>NoSuchKey</Code>
  <Message>The specified key does not exist.</Message>
  <RequestId>5CAC0FEADE0170*</RequestId>
  <HostId>versioning-get.oss-cn-hangzhou.aliyun*</HostId>
  <Key>example</Key>
</Error>
`


#### Specify the version ID of a delete marker


Request


`http
GET /example?versionId=CAEQMxiBgMCfqaWA0BYiIDliMWI4MGQ0MTVmMjQ3MmE5MDNlMmY4YmFkYTk3 HTTP/1.1
Host: versioning-get.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 17 Apr 2025 03:09:44 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response


`http
HTTP/1.1 405 Method Not Allowed
x-oss-request-id: 5CAC0CF8DE01700*
x-oss-delete-marker: true
x-oss-version-id: CAEQMxiBgMCfqaWADliMWI4MGQ0MTVmMjQ3MmE5MDNlMmY4YmFkYTk*
Allow: DELETE
Date: Tue, 17 Apr 2025 03:09:44 GMT
Content-Type: application/xml
Content-Length: 318
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>MethodNotAllowed</Code>
  <Message>The specified method is not allowed against this resource.</Message>
  <RequestId>5CAC0CF8DE0170*</RequestId>
  <HostId>versioning-get.oss-cn-hangzhou.aliyunc*</HostId>
  <Method>GET</Method>
  <ResourceType>DeleteMarker</ResourceType>
</Error>
`


## Error codes


If a request fails, OSS returns a response body that contains an error code. The following table lists the error codes specific to this operation.























| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchKey | 404 | The specified object does not exist. |
| SymlinkTargetNotExist | 404 | The object is a symbolic link, and the target object that the link points to does not exist. |
| InvalidTargetType | 400 | The object is a symbolic link, and the target object is also a symbolic link. |
| InvalidObjectState | 403 | The object is in the Archive storage class, and either a RestoreObject request was not submitted, the most recent RestoreObject request has timed out, or the restore operation is still in progress. |
| Not Modified | 304 | Returned when either of the following conditions is true: (1) The If-Modified-Since header is specified and the object has not been modified since the specified time. (2) The If-None-Match header is specified and the ETag of the object matches the provided ETag. |
| Precondition Failed | 412 | Returned when either of the following conditions is true: (1) The If-Unmodified-Since header is specified and the specified time is earlier than the actual last-modified time of the object. (2) The If-Match header is specified and the ETag of the object does not match the provided ETag. |
| Not Found | 404 | The versionId parameter was not specified in the request and the current version of the object is a delete marker. |
| Method Not Allowed | 405 | The versionId parameter was specified in the request and the specified version is a delete marker. |


## Integration methods

### SDK


The following SDKs support the GetObject operation.


(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-10/#concept-32014-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/download-file-using-oss-sdk-for-python-v2/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/download-file-using-oss-sdk-for-php-v2/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/v2-download-objects-as-files)


(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-30#concept-32137-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-69#concept-32137-zh)


(https://www.alibabacloud.com/help/en/oss/overview-42#concept-32091-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-5#concept-32048-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-47#concept-32061-zh)


(https://www.alibabacloud.com/help/en/oss/overview-45#concept-32073-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/preview-or-download-an-object#concept-64052-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-35#concept-32118-zh)


(https://www.alibabacloud.com/help/en/oss/developer-reference/download-object-using-oss-harmony-sdk/)


| Java | Python V2 | PHP V2 | Go V2 | C |
| --- | --- | --- | --- | --- |
| C++ | .NET | Android | iOS | Node.js |
| Browser.js | Ruby | Harmony |  |  |


### ossutil


For information about the ossutil command that corresponds to the GetObject operation, see [get-object](https://www.alibabacloud.com/help/en/oss/developer-reference/get-object).

Thank you! We've received your  feedback.