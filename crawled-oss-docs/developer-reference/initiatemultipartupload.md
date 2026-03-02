# api operation to initiate a multipart upload

You can call the InitiateMultipartUpload operation to initialize a multipart upload event before you upload data in parts to Object Storage Service (OSS).

## Notes


-

When you call the InitiateMultipartUpload operation, OSS creates and returns a globally unique upload ID for the multipart upload event. Use this ID to perform related operations, such as aborting or querying the multipart upload.

-

Initializing a multipart upload does not affect an existing object that has the same name.

-

When you calculate a signature to authenticate the InitiateMultipartUpload operation, add `?uploads` to `CanonicalizedResource`.

-

To initialize a multipart upload event, you must have the `oss:PutObject` permission. For more information, see [Grant custom permissions to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).























| API | Action | Definition |
| --- | --- | --- |
| InitiateMultipartUpload | oss:PutObject | Initializes multipart upload tasks. |
| oss:PutObjectTagging | When initializing a multipart upload task, if you specify object tags through x-oss-tagging, this permission is required. |
| kms:GenerateDataKey | When uploading an object, if the object metadata contains X-Oss-Server-Side-Encryption: KMS, these two permissions are required. |
| kms:Decrypt |


## Request syntax


`plaintext
POST /ObjectName?uploads HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT date
Authorization: SignatureValue
`


## Request headers


InitiateMultipartUpload requests support standard HTTP request headers such as Cache-Control, Content-Disposition, Content-Encoding, Content-Type, and Expires, and custom headers that start with `x-oss-meta-`. For more information, see [PutObject](https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb).











(https://www.ietf.org/rfc/rfc2616.txt)


(https://www.ietf.org/rfc/rfc2616.txt)


(https://www.ietf.org/rfc/rfc2616.txt)


(https://www.ietf.org/rfc/rfc2616.txt)


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


> IMPORTANT:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/product/oss/pricing?spm=a2c63.p38356.0.0.a44f4307NWVVe9)(https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#concept-y2g-szy-5db)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb)


> NOTE:

> NOTE: 


> NOTE: 




| Name | Type | Description |
| --- | --- | --- |
| Cache-Control | String | Specifies the caching behavior of the web page when the object is downloaded. For more information, see RFC 2616. Default value: none |
| Content-Disposition | String | Specifies the name of the object when it is downloaded. For more information, see RFC 2616. Default value: none |
| Content-Encoding | String | Specifies the content encoding format of the object when it is downloaded. For more information, see RFC 2616. Default value: none |
| Expires | String | The expiration time. For more information, see RFC 2616.Default value: none |
| x-oss-forbid-overwrite | String | Specifies whether to overwrite an object that has the same name when you call the InitiateMultipartUpload operation. If versioning is enabled or suspended for the destination bucket, the x-oss-forbid-overwrite request header is invalid. In this case, the object that has the same name is overwritten. If you do not specify the x-oss-forbid-overwrite header or set the x-oss-forbid-overwrite header to false, the object that has the same name is overwritten.If you set the x-oss-forbid-overwrite header to true, the object that has the same name cannot be overwritten.Setting the x-oss-forbid-overwrite request header decreases the queries per second (QPS) performance. If you want to use the x-oss-forbid-overwrite request header for many operations (QPS > 1,000), contact technical support to prevent business interruptions. |
| x-oss-server-side-encryption | String | The server-side encryption method that is used to encrypt each part of the object.Valid values: AES256, KMSImportant To use the KMS encryption algorithm, first activate Key Management Service (KMS).If you specify this header in the request, this header is included in the response. OSS encrypts each uploaded part using the specified method. When you download the object, the x-oss-server-side-encryption header is included in the response and its value is the encryption algorithm of the object. |
| x-oss-server-side-encryption-key-id | String | The ID of the customer master key (CMK) that is managed by KMS. This header is valid only when x-oss-server-side-encryption is set to KMS. |
| x-oss-storage-class | String | The storage class of the object. If you specify this header when you upload an object, the object is stored in the specified storage class, regardless of the storage class of the bucket. For example, if you set x-oss-storage-class to Standard when you upload an object to an Infrequent Access (IA) bucket, the object is stored as a Standard object.Valid values:StandardIA (Infrequent Access)Archive (Archive Storage)ColdArchive: Cold ArchiveDeepColdArchive: Deep Cold ArchiveImportant Setting the storage class to Deep Cold Archive during upload incurs higher PUT request fees. We recommend that you set the storage classes of the objects to Standard when you upload the objects, and configure lifecycle rules to convert the storage classes of the Standard objects to Deep Cold Archive. This reduces PUT request fees. For more information, see Storage classes. |
| x-oss-tagging | String | The tag of the object. You can specify multiple tags for an object. Example: TagA=A&TagB=B Note The tag key and value must be URL-encoded. If a tag does not contain an equal sign (=), the tag value is considered an empty string. |


## Request parameters


You can specify the encoding-type parameter in the request to encode the object name in the response.











| Name | Type | Description |
| --- | --- | --- |
| encoding-type | String | The method used to encode the object name in the response. Object names are encoded in UTF-8. However, the XML 1.0 standard does not support some control characters, such as characters with ASCII values from 0 to 10. For object names that contain control characters not supported by XML 1.0, specify the encoding-type parameter to encode the object names in the response. Default value: noneValid value: url |


## Response elements


After OSS receives an InitiateMultipartUpload request, it returns a response in the XML format. The response body contains the Bucket, Key, and UploadID elements.











| Name | Type | Description |
| --- | --- | --- |
| InitiateMultipartUploadResult | Container | The container for the results of the InitiateMultipartUpload request. Child nodes: Bucket, Key, UploadId, and EncodingType Parent node: None |
| Bucket | String | The name of the bucket for the multipart upload event. Parent node: InitiateMultipartUploadResult |
| Key | String | The name of the object for the multipart upload event. Parent node: InitiateMultipartUploadResult |
| UploadId | String | The unique ID for the multipart upload event. Use this ID in subsequent UploadPart and CompleteMultipartUpload calls.Parent node: InitiateMultipartUploadResult |
| EncodingType | String | The encoding type of the object name in the response. If the encoding-type parameter is specified in the request, the object name in the response is encoded. Parent node: InitiateMultipartUploadResult |


This operation also includes common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`plaintext
POST /multipart.data?uploads HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 22 Feb 2012 08:32:21 GMT
x-oss-storage-class: Archive
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`plaintext
HTTP/1.1 200 OK
Content-Length: 230
Server: AliyunOSS
Connection: keep-alive
x-oss-request-id: 42c25703-7503-fbd8-670a-bda01eae
Date: Wed, 22 Feb 2012 08:32:21 GMT
Content-Type: application/xml

<?xml version="1.0" encoding="UTF-8"?>
<InitiateMultipartUploadResult xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
    <Bucket>oss-example</Bucket>
    <Key>multipart.data</Key>
    <UploadId>0004B9894A22E5B1888A1E29F823</UploadId>
</InitiateMultipartUploadResult>
`


## SDK


The following SDKs are available for this operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/java-multipart-upload#concept-84786-zh)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-multipart-upload)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-9#concept-90222-zh)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-sdk-for-php-v2)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-8#concept-90222-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-10#concept-91103-zh)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-3#concept-hgg-3vb-dhb)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/overview-2#section-snl-fxt-4fb)

-

[Harmony](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-harmony-sdk)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-6)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-7)

## ossutil command-line tool


For the ossutil command that corresponds to this operation, see [initiate-multipart-upload](https://www.alibabacloud.com/help/en/oss/developer-reference/initiate-multipart-upload).

## Error codes











-



-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidEncryptionAlgorithmError | 400 | A server-side encryption method other than AES256, KMS is specified. |
| InvalidArgument | 400 | The x-oss-server-side-encryption request header is added when each part is uploaded. |
| InvalidArgument | 400 | The specified storage class is invalid. |
| KmsServiceNotEnabled | 403 | The KMS encryption algorithm is used, but KMS is not activated in the console. |
| FileAlreadyExists | 409 | The possible causes for this fault are as follows:The request includes the x-oss-forbid-overwrite=true header to prevent overwriting an object that has the same name, but an object with the same name already exists in the bucket.The hierarchical namespace feature is enabled for the bucket, and the object specified for the multipart upload event is a directory. |


Thank you! We've received your  feedback.