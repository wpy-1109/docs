# Call GetObjectMeta to obtain the metadata of an object

Call the GetObjectMeta operation to obtain the metadata of an object. The metadata includes the ETag, size, and last-modified time of the object. The content of the object is not returned.

## Notes


> NOTE:

> NOTE: 


> NOTE: Note 

If the object is a symbolic link, information about the symbolic link is returned.


If versioning is disabled for a bucket, you must have the `oss:GetObject` permission to obtain the metadata of an object. If versioning is enabled for a bucket, you must have the `oss:GetObjectVersion` permission to obtain the metadata of a specific version of an object. To specify a version, use the x-oss-version-id request header. For more information, see [Grant custom permissions to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Versioning


By default, the GetObjectMeta operation retrieves the metadata of the current version of an object. If the current version of the object is a delete marker, a 404 Not Found error is returned. If you specify a versionId in the request, the metadata of the specified version is returned.

## Request syntax


`plaintext
HEAD /ObjectName?objectMeta HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers














> NOTE:

> NOTE: 


> NOTE: 

-


-




> IMPORTANT:

> NOTE: 


> NOTE: 


> NOTE:

> NOTE: 


> NOTE: 

-


-


| Response header | Type | Example | Description |
| --- | --- | --- | --- |
| Content-Length | String | 344606 | The size of the object in bytes. |
| ETag | String | 5B3C1A2E053D763E1B002CC607C5 | When an object is created, an ETag (entity tag) is generated to identify the content of the object.For an object created by a PutObject request, the ETag is the MD5 hash of its content. For objects created by other methods, the ETag is a unique value but not the MD5 hash of the content. You can use the ETag to check whether the object content has changed. Do not use the ETag for MD5 validation to verify data integrity.Default value: None |
| x-oss-transition-time | String | Tue, 23 Apr 2024 07:21:42 GMT | The time when the object was converted to the Cold Archive or Deep Cold Archive storage class by a lifecycle rule.Note If you delete a Cold Archive or Deep Cold Archive object more than 180 days after it is converted, no early deletion fee is charged. If you delete the object within 180 days after it is converted, an early deletion fee is charged.This field cannot be used to determine the time when an object is converted to the IA or Archive storage class by a lifecycle rule. Whether an IA or Archive object meets the minimum storage duration requirement depends on the Last-Modified time. |
| x-oss-last-access-time | String | Tue, 30 Mar 2021 06:07:48 GMT | The last access time of the object. The time is in GMT format as specified in HTTP 1.1. If access tracking is enabled, the value of this field is updated when the object is accessed. If access tracking is disabled, this field is not returned.Important The last access time of an object is updated asynchronously. OSS typically updates the last access time of an object within 24 hours. If an object is accessed multiple times within 24 hours, OSS updates only the earliest access time. |
| Last-Modified | String | Fri, 24 Feb 2012 06:07:48 GMT | The time when the object was last modified. The time is in GMT format as specified in HTTP 1.1.Note The minimum storage duration for objects in the Infrequent Access storage class is 30 days. The duration is calculated from the Last-Modified time of the object. If you delete an object more than 30 days after its Last-Modified time, no early deletion fee is charged.The minimum storage duration for objects in the Archive Storage class is 60 days. The duration is calculated from the Last-Modified time of the object. If you delete an object more than 60 days after its Last-Modified time, no early deletion fee is charged. |
| x-oss-version-id | String | CAEQNRiBgIDMh4mD0BYiIDUzNDA4OGNmZjBjYTQ0YmI4Y2I4ZmVlYzJlNGVk | The version ID of the object. This field is returned only when you obtain the metadata of a specific version of an object. |
| x-oss-sealed-time | String | Sat, 11 Oct 2025 06:41:42 GMT | The time when the seal operation was performed on an appendable object that is in the Sealed state. The time is in GMT format as specified in HTTP 1.1. This field is returned only when you access a sealed appendable object. |


This operation also uses common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Versioning disabled


Request example


`plaintext
HEAD /oss.jpg?objectMeta HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 29 Apr 2015 05:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


> IMPORTANT:

> NOTE: 


> NOTE: Important 

If you enable hierarchical namespace for a bucket and then create a folder by calling the CreateDirectory operation, the ETag is returned as "null" when you call the GetObjectMeta operation to obtain the metadata of the folder.


-

Access tracking disabled


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A6448
Date: Wed, 29 Apr 2015 05:21:12 GMT
ETag: "5B3C1A2E053D763E1B002CC607C5"
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
Content-Length: 344606
Connection: keep-alive
Server: AliyunOSS
`


-

Access tracking enabled


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A6448
Date: Wed, 29 Apr 2015 05:21:12 GMT
ETag: "5B3C1A2E053D763E1B002CC607C5"
x-oss-transition-time: Tue, 23 Apr 2024 07:21:42 GMT
x-oss-last-access-time: Thu, 14 Oct 2021 11:49:05 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
Content-Length: 344606
Connection: keep-alive
Server: AliyunOSS
`


-

Versioning enabled


Request example


`plaintext
GET /example?objectMeta&versionId=CAEQNRiBgIDMh4mD0BYiIDUzNDA4OGNmZjBjYTQ0YmI4Y2I4ZmVlYzJlNGVk HTTP/1.1
Host: versioning-test.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:24:00 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Response example


-

Access tracking disabled


`plaintext
HTTP/1.1 200 OK
x-oss-version-id: CAEQNRiBgIDMh4mD0BYiIDUzNDA4OGNmZjBjYTQ0YmI4Y2I4ZmVlYzJlNGVk
x-oss-request-id: 5CAC3A80B7AEADE0170005F6
Date: Tue, 09 Apr 2019 06:24:00 GMT
ETag: "1CF5A685959CA2ED8DE6E5F8ACC2"
Last-Modified: Tue, 09 Apr 2019 06:24:00 GMT
Content-Length: 119914
Connection: keep-alive
Server: AliyunOSS
`


-

Access tracking enabled


`plaintext
HTTP/1.1 200 OK
x-oss-version-id: CAEQNRiBgIDMh4mD0BYiIDUzNDA4OGNmZjBjYTQ0YmI4Y2I4ZmVlYzJlNGVk
x-oss-request-id: 5CAC3A80B7AEADE0170005F6
Date: Tue, 09 Apr 2019 06:24:00 GMT
ETag: "1CF5A685959CA2ED8DE6E5F8ACC2"
x-oss-last-access-time: Thu, 14 Oct 2021 11:49:05 GMT
Last-Modified: Tue, 09 Apr 2019 06:24:00 GMT
Content-Length: 119914
Connection: keep-alive
Server: AliyunOSS
`


## SDK


You can call this operation using the following software development kits (SDKs):


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-2#concept-84840-zh)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-using-oss-sdk-for-php-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-object-metadata)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-7#concept-90504-zh)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-5#concept-90504-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-8#concept-91920-zh)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/query-object-metadata-5#concept-vp1-dnp-mfb)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/query-object-metadata-6#concept-qcf-zhg-4fb)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-4#concept-ukc-wc3-dhb)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-3#concept-2166880)

-

[Harmony](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata-using-harmony-sdk)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-object-metadata)

## Command line interface ossutil


For the ossutil command that corresponds to the GetObjectMeta operation, see [get-object-meta](https://www.alibabacloud.com/help/en/oss/developer-reference/get-object-meta).

## References


For more information about object metadata, see [Manage object metadata](https://www.alibabacloud.com/help/en/oss/user-guide/manage-object-metadata-10/).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| Not Found | 404 | The specified object does not exist. |


Thank you! We've received your  feedback.