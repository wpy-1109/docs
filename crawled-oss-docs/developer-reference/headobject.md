# Get the metadata of an object

The HeadObject operation retrieves the metadata of an object. This operation does not return the object content.

## Versioning


-

If you call the HeadObject operation without specifying a versionId, the metadata of the current object version is returned. If the current object version is a delete marker, 404 NoSuchKey is returned.

-

If you call the HeadObject operation and specify a versionId, the metadata of the specified object version is returned. Do not specify the versionId of a delete marker. Otherwise, 405 MethodNotAllowed is returned.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).














| API | Action | Definition |
| --- | --- | --- |
| HeadObject | oss:GetObject | Queries the metadata of an object. |


## Request syntax


`xml
HEAD /ObjectName HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers














| Name | Type | Required | Description |
| --- | --- | --- | --- |
| If-Modified-Since | String | No | If the time specified is earlier than the object's actual modification time, 200 OK and the object metadata are returned. Otherwise, 304 Not Modified is returned.Default value: None |
| If-Unmodified-Since | String | No | If the time specified is the same as or later than the actual modification time of the object, 200 OK and the object metadata are returned. Otherwise, 412 Precondition Failed is returned.Default value: None |
| If-Match | String | No | If the specified ETag matches the ETag of the object, 200 OK and the object metadata are returned. Otherwise, 412 Precondition Failed is returned.Default value: None |
| If-None-Match | String | No | If the specified ETag does not match the ETag of the object, 200 OK and the object metadata are returned. Otherwise, 304 Not Modified is returned.Default value: None |


This operation also includes common request headers, such as Host and Date. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


If the requested object is a symbolic link, the response headers are described as follows:


-

Content-Length, ETag, x-oss-storage-class, and Content-Md5 are the metadata of the object file.

-

Last-Modified is the last modification time of the symbolic link or the object file, whichever is later.

-

Other response headers indicate the metadata of the symbolic link.











(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb)


-


-


-


> NOTE:

> NOTE: 


> NOTE: 

-


-




-


-


-


-


-


-


-


-


-


-


-


> NOTE:

> NOTE: 


> NOTE: 

-


-


| Name | Type | Description |
| --- | --- | --- |
| x-oss-meta-* | String | Parameters prefixed with x-oss-meta- are user-defined metadata headers. If you set custom metadata prefixed with x-oss-meta- when you call the PutObject operation, these custom metadata headers are included in the response. |
| Custom headers that do not start with x-oss-meta- | String | If you specify custom headers that do not start with x-oss-meta-, such as x-oss-persistent-headers:key1:base64_encode(value1),key2:base64_encode(value2)..., when you call the PutObject operation, the corresponding custom headers are added to the response. |
| x-oss-server-side-encryption | String | If the object is stored with server-side encryption, this header is returned in the response. The value of this header indicates the server-side encryption algorithm used for the object. |
| x-oss-server-side-encryption-key-id | String | If server-side encryption is used when the object is created and the encryption method is KMS, this header is included in the response. This header indicates the ID of the user's KMS key. |
| x-oss-storage-class | String | The storage class of the object. Valid values: Standard, IA, Archive, ColdArchive, and DeepColdArchive.For more information, see Storage classes. |
| x-oss-object-type | String | The type of the object.Objects that are uploaded by calling PutObject or created by calling CreateDirectory are of the Normal type.Objects that are uploaded by calling AppendObject are of the Appendable type.Objects that are uploaded by calling MultipartUpload are of the Multipart type. |
| x-oss-next-append-position | String | This header is returned for Appendable objects to specify the position from which the next append operation must start. |
| x-oss-hash-crc64ecma | String | The 64-bit cyclic redundancy check (CRC-64) value of the object. The value is calculated based on the CRC-64/XZ algorithm.This response header may not be returned when you call the HeadObject operation for objects that were created before OSS supported CRC-64. |
| x-oss-sealed-time | String | This header is returned for Appendable objects that are sealed. The value of this header indicates the time when the object was sealed. The time is in the GMT format specified in HTTP 1.1, such as Sat, 11 Oct 2025 06:41:42 GMT. |
| x-oss-transition-time | String | The time when the object was converted to the Cold Archive or Deep Cold Archive storage class by a lifecycle rule.Note If you delete a Cold Archive or Deep Cold Archive object more than 180 days after its storage class was converted, you are not charged an early deletion fee. If you delete the object within 180 days of the conversion, an early deletion fee is charged.You cannot use this header to query the time when the storage class of the object is converted to Infrequent Access or Archive based on lifecycle rules. You can determine whether the object is stored for more than the minimum storage duration based on the Last-Modified time. |
| x-oss-expiration | String | The expiration time of an object in a bucket for which a lifecycle rule is configured.Versioning is enabled for the bucketA request is sent without a versionId.If the requested object matches a delete rule in the lifecycle configuration, the x-oss-expiration header is returned in the response to indicate the expiration time of the current version of the object.A request is sent with a versionId.The x-oss-expiration header is not returned in the response, regardless of whether the requested object matches a delete rule in the lifecycle configuration.Versioning is disabled for the bucketIf the requested object matches a delete rule in the lifecycle configuration, the x-oss-expiration header is returned in the response.If the requested object does not match a delete rule in the lifecycle configuration, the x-oss-expiration header is not returned in the response. |
| x-oss-restore | String | If the storage class of the object is Archive, ColdArchive, or DeepColdArchive, and you have submitted a Restore request, the restore status of the object is returned in the x-oss-restore response header. The following cases may occur:If no Restore request is submitted or the restored object has expired, this header is not returned.If a Restore request is submitted but the restore task is not complete, the value of x-oss-restore is ongoing-request="true".If a Restore request is submitted and the restore task is complete, the value of x-oss-restore is ongoing-request="false", expiry-date="Sun, 16 Apr 2017 08:12:33 GMT". expiry-date indicates the expiration time of the restored object. |
| x-oss-process-status | String | After you create an OSS event notification using Simple Message Queue (SMQ), if a matching event notification rule exists when you perform a related OSS operation, this header is included in the response. The value is the Base64-encoded event notification result in the JSON format. |
| x-oss-request-charged | String | If the bucket to which the object belongs is set to the pay-by-requester mode and the requester is not the bucket owner, this header is included in the response. The value of this header is requester. |
| Content-Md5 | String | For Normal objects, the 128-bit MD5 value of the message content (excluding headers) is calculated based on RFC 1864. This value is then Base64-encoded to obtain the Content-Md5 value.This header is not returned for Multipart or Appendable objects. |
| Last-Modified | String | The date when the object was last modified. The format is the GMT time specified in HTTP 1.1.Note The minimum storage duration for Infrequent Access (IA) objects is 30 days, calculated from the object's Last-Modified time. If you delete an IA object more than 30 days after its last modification, you are not charged an early deletion fee.The minimum storage duration for Archive Storage objects is 60 days, calculated from the object's Last-Modified time. If you delete an Archive Storage object more than 60 days after its last modification, you are not charged an early deletion fee. |
| Access-Control-Allow-Origin | String | If a cross-origin resource sharing (CORS) rule is configured for the bucket to which the object belongs and the origin of the request meets the specified CORS rule, this origin is included in the response. |
| Access-Control-Allow-Methods | String | If a CORS rule is configured for the bucket to which the object belongs and the Access-Control-Request-Method of the request meets the specified CORS rule, the allowed methods are included in the response. |
| Access-Control-Max-Age | String | If a CORS rule is configured for the bucket to which the object belongs and the request meets the CORS rule, MaxAgeSeconds is included in the response. |
| Access-Control-Allow-Headers | String | If a CORS rule is configured for the bucket to which the object belongs and the request meets the specified CORS rule, these headers are included in the response. |
| Access-Control-Expose-Headers | String | The list of headers that client-side JavaScript programs are allowed to access. If a CORS rule is configured for the bucket to which the object belongs and the request meets the specified CORS rule, ExposeHeader is included in the response. |
| x-oss-tagging-count | String | The number of tags associated with the object. This header is returned only if you have the permission to read tags. |


This operation also includes common response headers, such as ETag and x-oss-request-id. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Versioning is disabled


Request example


`xml
HEAD /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 07:32:52 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example (The object is a file)


`xml
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A6448
x-oss-object-type: Normal
x-oss-storage-class: Archive
Date: Fri, 7 Aug 2020 07:32:52 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
ETag: "fba9dede5f27731c9771645a3986"
Content-Length: 344606
Content-Type: image/jpg
Connection: keep-alive
Server: AliyunOSS
`


Response example (The object is a folder)


`xml
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A6448
x-oss-object-type: Normal
x-oss-storage-class: Standard
Date: Wed, 31 Mar 2021 07:32:52 GMT
Last-Modified: Tue, 30 Mar 2021 06:07:48 GMT
ETag: "null"
Content-Length: 0
Content-Type: application/x-directory
Connection: keep-alive
Server: AliyunOSS
`


Response example (The object is a sealed Appendable object)


`
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A6448
x-oss-object-type: Appendable
x-oss-storage-class: Standard
x-oss-sealed-time: Sat, 11 Oct 2025 06:41:42 GMT
Date: Wed, 31 Mar 2021 07:32:52 GMT
Last-Modified: Tue, 30 Mar 2021 06:07:48 GMT
ETag: "fba9dede5f27731c9771645a3986"
Content-Length: 100
Content-Type: text/plain
Connection: keep-alive
Server: AliyunOSS
`


-

Requesting a specific version of an object (versioning is enabled)


Request example


`xml
HEAD /example?versionId=CAEQNRiBgICb8o6D0BYiIDNlNzk5NGE2M2Y3ZjRhZTViYTAxZGE0ZTEyMWYy
Host: versioning-test.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 06:27:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200 OK
x-oss-versionId: CAEQNRiBgICb8o6D0BYiIDNlNzk5NGE2M2Y3ZjRhZTViYTAxZGE0ZTEyMWYy
x-oss-request-id: 5CAC3B40B7AEADE01700
x-oss-object-type: Normal
x-oss-storage-class: Archive
Date: Fri, 7 Aug 2020 06:27:12 GMT
Last-Modified: Fri, 7 Aug 2020 06:27:12 GMT
ETag: "A082B659EF78733A5A042FA253B1"
Content-Length: 481827
Content-Type: text/html
Connection: keep-alive
Server: AliyunOSS
`


-

Requesting the latest version of an object (versioning is enabled)


Request example


`plaintext
HEAD /example HTTP/1.1
Host: versioning-test.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 06:27:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200 OK
x-oss-versionId: CAEQMxiBgMCZov2D0BYiIDY4MDllOTc2YmY5MjQxMzdiOGI3OTlhNTU0ODIx
x-oss-request-id: 5CAC3B40B7AEADE01700
x-oss-object-type: Normal
x-oss-storage-class: Archive
Date: Fri, 7 Aug 2020 06:27:12 GMT
Last-Modified: Fri, 7 Aug 2020 06:27:12 GMT
ETag: "3663F7B0B9D3153F884C821E7CF4"
Content-Length: 485859
Content-Type: text/html
Connection: keep-alive
Server: AliyunOSS
`


-

Restore task in progress


Request example


`plaintext
HEAD /oss.jpg HTTP/1.1
Host: oss-archive-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 07:32:52 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 58F71A164529F18D7F00
x-oss-object-type: Normal
x-oss-storage-class: Archive
x-oss-restore: ongoing-request="true"
Date: Fri, 7 Aug 2020 07:32:52 GMT
Last-Modified: Fri, 7 Aug 2020 06:07:48 GMT
ETag: "fba9dede5f27731c9771645a3986"
Content-Length: 344606
Content-Type: image/jpg
Connection: keep-alive
Server: AliyunOSS
`


-

Restore task complete


Request example


`plaintext
HEAD /oss.jpg HTTP/1.1
Host: oss-archive-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 09:35:51 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 58F725344529F18D7F00
x-oss-object-type: Normal
x-oss-storage-class: Archive
x-oss-restore: ongoing-request="false", expiry-date="Sun, 16 Apr 2017 08:12:33 GMT"
Date: Fri, 7 Aug 2020 09:35:51 GMT
Last-Modified: Fri, 7 Aug 2020 06:07:48 GMT
ETag: "fba9dede5f27731c9771645a3986"
Content-Length: 344606
`


-

Using server-side encryption with SSE-OSS


Request example


`plaintext
HEAD /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 07:32:52 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A6448
x-oss-object-type: Normal
x-oss-storage-class: Archive
x-oss-server-side-encryption: AES256
Date: Fri, 7 Aug 2020 07:32:52 GMT
Last-Modified: Fri, 7 Aug 2020 06:07:48 GMT
ETag: "fba9dede5f27731c9771645a3986"
Content-Length: 344606
Content-Type: image/jpg
Connection: keep-alive
Server: AliyunOSS
`


-

Using server-side encryption with SSE-KMS


Request example


`plaintext
HEAD /oss.jpg HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 7 Aug 2020 07:32:52 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A64485981
x-oss-object-type: Normal
x-oss-storage-class: Archive
x-oss-server-side-encryption: KMS
x-oss-server-side-encryption-key-id: 9468da86-3509-4f8d-a61e-6eab1eac
Date: Fri, 7 Aug 2020 07:32:52 GMT
Last-Modified: Fri, 7 Aug 2020 06:07:48 GMT
ETag: "fba9dede5f27731c9771645a3986"
Content-Length: 344606
Content-Type: image/jpg
Connection: keep-alive
Server: AliyunOSS
`


## SDKs


This operation is supported by the following SDKs:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-2)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-object-metadata)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-4)

-

[Harmony](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-using-harmony-sdk)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-using-oss-sdk-for-php-v2)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-8)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-3)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/query-object-metadata-5)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-5)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/query-object-metadata-6)

## ossutil


For the ossutil command that corresponds to the HeadObject operation, see [head-object](https://www.alibabacloud.com/help/en/oss/developer-reference/head-object).

## Error codes











-


-


-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchKey | 404 | The requested object does not exist. |
| SymlinkTargetNotExist | 404 | The requested file is a symbolic link. |
| InvalidTargetType | 400 | The requested object is a symbolic link, and its target object is also a symbolic link. |
| NotModified | 304 | This error is returned for one of the following reasons:The If-Modified-Since request header is specified, but the source object has not been modified since the specified time.The If-None-Match request header is specified, and the ETag of the source object is the same as the ETag that you provided. |
| PreconditionFailed | 412 | This error is returned for one of the following reasons:The If-Unmodified-Since request header is specified, but the specified time is earlier than the actual modification time of the object.The If-Match request header is specified, but the ETag of the source object is not the same as the ETag that you provided. |


Thank you! We've received your  feedback.