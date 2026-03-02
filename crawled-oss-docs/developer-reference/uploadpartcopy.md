# Call the UploadPartCopy operation to copy data from an existing object to upload a part

You can call the UploadPartCopy operation by adding the x-oss-copy-source request header to an UploadPart request. This operation copies data from an existing object to upload as a part.

## Usage notes


You must use UploadPartCopy to copy a file larger than 1 GB. To copy a file smaller than 1 GB in a single operation, see [CopyObject](https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject#reference-mvx-xxc-5db).


Note the following when you use the UploadPartCopy operation:


-

The source bucket and the destination bucket for the UploadPartCopy operation must be in the same region.

-

Before you call this operation to upload a part, you must call the InitiateMultipartUpload operation to obtain an upload ID issued by OSS.

-

If you specify the x-oss-server-side-encryption request header when you call the InitiateMultipartUpload operation, the uploaded part is encrypted. The x-oss-server-side-encryption header is returned in the response to the UploadPart operation. The value of this header indicates the server-side encryption algorithm used for the part. For more information, see [InitiateMultipartUpload](https://www.alibabacloud.com/help/en/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb).

-

For a multipart upload, all parts except the last one must be larger than 100 KB. The UploadPart operation does not immediately check the size of the uploaded part because it cannot determine if it is the last part. The size is checked only when the CompleteMultipartUpload operation is called.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).




















| API | Action | Definition |
| --- | --- | --- |
| UploadPartCopy | oss:GetObject | Reads data in the source object when you upload a part by copying data from an existing object. |
| oss:PutObject | Writes data to the destination object when you upload a part by copying data from an existing object. |
| oss:GetObjectVersion | When uploading a part by copying data from an existing object, if you specify the object version through versionId, this permission is required to read the specified version of the source object. |


## Versioning


By default, the UploadPartCopy operation copies data from the current version of an existing object to upload as a part. You can copy data from a specific version of an object by including the versionId sub-resource in the x-oss-copy-source request header. For example: x-oss-copy-source : /SourceBucketName/SourceObjectName?versionId=111111.


> NOTE:

> NOTE: 


> NOTE: Note 

SourceObjectName must be URL-encoded. The response returns the versionId of the copied object in the x-oss-copy-source-version-id header.


If you do not specify a versionId and the current version of the object to copy is a delete marker, OSS returns 404 Not Found. If you specify a versionId to copy a delete marker, OSS returns 400 Bad Request.

## Metering and billing


When you call the UploadPartCopy operation, if the source object is an Infrequent Access (IA) object, data retrieval fees for IA objects are incurred. If the source object is an Archive object that has not been restored using the RestoreObject operation and real-time access of Archive objects is enabled for the bucket, data retrieval fees for real-time access of Archive objects are incurred when you access the object. The fees are charged to the source bucket. For more information about billing, see [Data processing fees](https://www.alibabacloud.com/help/en/oss/data-processing-fees).

## Request syntax


`plaintext
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId  HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Content-Length: Size
Authorization: SignatureValue
x-oss-copy-source: /SourceBucketName/SourceObjectName
x-oss-copy-source-range: bytes=first-last
`


## Request headers


In addition to common request headers, the UploadPartCopy request uses the following request headers to specify the source object and the copy range.











-


-


-


| Name | Type | Description |
| --- | --- | --- |
| x-oss-copy-source | String | The source object to copy. You must have read permissions on this object.Default value: None |
| x-oss-copy-source-range | String | The range of the source object to copy. For example, if you set this header to bytes=0-9, the first 10 bytes of the object are copied. Default value: NoneIf you do not specify this header, the entire source object is copied.If you specify this header, the response includes the total length of the file and the range of the current copy. For example, `Content-Range: bytes 0-9/44` indicates that the total file length is 44 bytes and the copied range is from byte 0 to byte 9.If the specified range is invalid, the entire source object is copied, and the response does not include Content-Range. |


The following request headers apply to the source object specified by x-oss-copy-source.














| Name | Type | Description |
| --- | --- | --- |
| x-oss-copy-source-if-match | String | The copy operation is performed only if the ETag of the source object matches the specified ETag. Otherwise, the 412 Precondition Failed error is returned. Default value: None |
| x-oss-copy-source-if-none-match | String | If the provided ETag value does not match the Object's ETag, the file is transferred and a 200 OK response is returned. Otherwise, a 304 Not Modified response is returned.Default value: None |
| x-oss-copy-source-if-unmodified-since | String | The file is copied and 200 OK is returned only if the time specified in this header is the same as or later than the actual modification time of the file. Otherwise, the 412 Precondition Failed error is returned. Default value: None |
| x-oss-copy-source-if-modified-since | String | The file is copied and 200 OK is returned only if the specified time is earlier than the actual modification time of the file. Otherwise, 304 Not Modified is returned. Default value: NoneFormat: GMT. Example: Fri, 13 Nov 2015 14:47:53 GMT |


## Examples


-

Request example


`plaintext
PUT /multipart.data?partNumber=1&uploadId=0004B9895DBBB6EC98E36  HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Length: 6291456
Date: Wed, 22 Feb 2012 08:32:21 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-copy-source: /oss-example/src-object
x-oss-copy-source-range: bytes=100-6291756
`


Response example


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Connection: keep-alive
x-oss-request-id: 3e6aba62-1eae-d246-6118-8ff42cd0
Date: Thu, 17 Jul 2014 06:27:54 GMT

<?xml version="1.0" encoding="UTF-8"?>
<CopyPartResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <LastModified>2014-07-17T06:27:54.000Z </LastModified>
    <ETag>"5B3C1A2E053D763E1B002CC607C5"</ETag>
</CopyPartResult>
`


-

Request example with a specified versionId


`plaintext
PUT /multipart.data?partNumber=2&uploadId=63C06A5CFF6F4AE4A6BB3AD7F01C  HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 07:01:56 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-copy-source: /oss-example/src-object?versionId=CAEQMxiBgMC0vs6D0BYiIGJiZWRjOTRjNTg0NzQ1MTRiN2Y1OTYxMTdkYjQ0
`


Response example


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Connection: keep-alive
x-oss-copy-source-version-id: CAEQMxiBgMC0vs6D0BYiIGJiZWRjOTRjNTg0NzQ1MTRiN2Y1OTYxMTdkYjQ0
x-oss-request-id: 5CAC4364B7AEADE017000660
Date: Tue, 09 Apr 2019 07:01:56 GMT

<?xml version="1.0" encoding="UTF-8"?>
<CopyPartResult>
  <LastModified>2019-04-09T07:01:56.000Z</LastModified>
  <ETag>"25A9F4ABFCC05743DF6E2C886C56"</ETag>
</CopyPartResult>
`


## SDK


The following software development kits (SDKs) are available for this operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/java-copy-objects#section-aq6-vel-1iq)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/fragment-copy-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-upload-part-copy)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/copy-objects-10#section-rnf-xnz-xgb)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/fragment-copy-using-oss-sdk-for-php-v2)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/copy-an-object-2#section-z4i-elj-3z1)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/copy-objects-using-oss-sdk-for-csharp-v1#section-9mg-n07-bi9)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/copy-objects-5#section-38u-k9j-c7j)

## ossutil command line interface


For the ossutil command that corresponds to the UploadPartCopy operation, see [upload-part-copy](https://www.alibabacloud.com/help/en/oss/developer-reference/upload-part-copy).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| OperationNotSupported | 400 | The UploadPartCopy operation is called for a bucket of the Archive storage class. |


Thank you! We've received your  feedback.