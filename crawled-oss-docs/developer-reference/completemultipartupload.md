# call CompleteMultipartUpload to complete multipart upload

Completes the multipart upload task of an object after all parts of the object are uploaded.

## Notes


When you call the CompleteMultipartUpload operation, you must provide a complete list of all valid parts, including the part number and entity tag (ETag) of each part. After Object Storage Service (OSS) receives the list of parts, OSS verifies the validity of each part one after another. After all parts are validated, OSS combines these parts into a complete object.


-

Confirm the size of each part


When you call the CompleteMultipartUpload operation, OSS checks whether each part except the last part is larger than or equal to 100 KB in size and verifies the part number and ETag of each part provided in the part list. Therefore, when a part is uploaded, the client must record not only the part number of the part but also the ETag value of the part returned from the server.

-

Handle requests


It may take a period of time for OSS to process a CompleteMultipartUpload request. If the client is disconnected from OSS during the period, OSS continues to process the request.

-

PartNumber


OSS verifies the value of PartNumber when you call the CompleteMultipartUpload operation.


The value of PartNumber ranges from 1 to 10000. The part numbers listed in the request can be non-consecutive but must be sorted in ascending order. For example, if the part number of the first part is 1, the part number of the second part can be 5.

-

UploadId


An object can be uploaded by multiple upload tasks that have independent upload IDs. When one upload task is completed, its upload ID becomes invalid but the upload IDs of other upload tasks are not affected.

-

x-oss-server-side-encryption


If the x-oss-server-side-encryption header is specified in an InitiateMultipartUpload request, this header is returned in the response to the CompleteMultipartUpload request. The value of the x-oss-server-side-encryption header in the response indicates the method that is used to encrypt the object on the OSS server.

## Versioning


You can call the CompleteMultipartUpload operation to complete the multipart upload task of an object when versioning is enabled for the bucket to which the object is uploaded. In this case, OSS generates a unique version ID for the object, and returns the version ID as the x-oss-version-id header in the response.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).

















| API | Action | Definition |
| --- | --- | --- |
| CompleteMultipartUpload | oss:PutObject | Merges parts into an object. |
| oss:PutObjectTagging | When merging parts into an object, if you specify object tags through x-oss-tagging, this permission is required. |


## Request syntax


`plaintext
POST /ObjectName?uploadId=UploadId HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Content-Length: Size
Authorization: Signature
<CompleteMultipartUpload>
<Part>
<PartNumber>PartNumber</PartNumber>
<ETag>ETag</ETag>
</Part>
...
</CompleteMultipartUpload>
`


## Request parameters


You can configure the encoding-type parameter in a CompleteMultipartUpload request. OSS uses the specified encoding type to encode the object name in the response.











| Parameter | Type | Description |
| --- | --- | --- |
| encoding-type | String | The encoding type of the object name in the response. Only URL encoding is supported. The object name can contain characters that are encoded in UTF-8. However, the XML 1.0 standard cannot be used to parse control characters, such as characters with an ASCII value from 0 to 10. You can configure this parameter to encode the object name in the response. By default, this header is left empty.Valid value: url. |


## Request headers














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


| Header | Type | Required | Description |
| --- | --- | --- | --- |
| x-oss-forbid-overwrite | String | No | Specifies whether the object with the same object name is overwritten when you call the CompleteMultipartUpload operation. If x-oss-forbid-overwrite is not specified or set to false, existing objects can be overwritten by objects that have the same names. If x-oss-forbid-overwrite is set to true, existing objects cannot be overwritten by objects that have the same names. Note The x-oss-forbid-overwrite request header is invalid if versioning is enabled or suspended for the bucket. In this case, the CompleteMultipartUpload operation overwrites the object that has the same name. If you specify the x-oss-forbid-overwrite request header, the queries per second (QPS) performance of OSS may degrade. If you want to configure the x-oss-forbid-overwrite header in a large number of requests (more than 1,000 QPS), submit a ticket. |
| x-oss-complete-all | String | No | Specifies whether to list all parts that are uploaded by using the current upload ID. Valid value: yes.If x-oss-complete-all is set to yes in the request, OSS lists all parts that are uploaded by using the current upload ID, sorts the parts by part number, and then performs the CompleteMultipartUpload operation. When OSS performs the CompleteMultipartUpload operation, OSS cannot detect the parts that are not uploaded or currently being uploaded. Before you call the CompleteMultipartUpload operation, make sure that all parts are uploaded. If x-oss-complete-all is specified in the request, the request body cannot be specified. Otherwise, an error occurs. If x-oss-complete-all is specified in the request, the format of the response remains unchanged. |


For more information about the common request headers contained in CompleteMultipartUpload requests such as Host and Date, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#reference-mhp-zdy-wdb).

## Request elements











| Element | Type | Description |
| --- | --- | --- |
| CompleteMultipartUpload | Container | The container that stores the content of the CompleteMultipartUpload request. Child nodes: Part.Parent nodes: none. |
| ETag | String | The ETag values that are returned by OSS after parts are uploaded. Parent nodes: Part. |
| Part | Container | The container that stores the uploaded parts. Child nodes: ETag and PartNumber.Parent nodes: CompleteMultipartUpload. |
| PartNumber | Integer | The number of parts. Parent nodes: Part. |


## Response elements











> NOTE:

> NOTE: 


> NOTE: 


| Element | Type | Description |
| --- | --- | --- |
| Bucket | String | The name of the bucket that contains the object you want to restore. Parent nodes: CompleteMultipartUploadResult. |
| CompleteMultipartUploadResult | Container | The container that stores the results of the CompleteMultipartUpload request. Child nodes: Bucket, Key, ETag, and Location.Parent nodes: none. |
| ETag | String | The ETag that is generated when an object is created. ETags are used to identify the content of objects. If an object is created by calling the CompleteMultipartUpload operation, the ETag value is not the MD5 hash of the object content but a unique value calculated based on a specific rule. Note The ETag of an object can be used to check whether the object content is modified. However, we recommend that you use the MD5 hash of an object rather than the ETag value of the object to verify data integrity. Parent nodes: CompleteMultipartUploadResult. |
| Location | String | The URL that is used to access the uploaded object. Parent nodes: CompleteMultipartUploadResult. |
| Key | String | The name of the uploaded object. Parent nodes: CompleteMultipartUploadResult. |
| EncodingType | String | The encoding type of the object name in the response. If this parameter is specified in the request, the object name is encoded in the response. Parent nodes: Container. |


## Examples


-

Complete the multipart upload task of an object in an unversioned bucket


Sample requests


`plaintext
POST /multipart.data?uploadId=0004B9B2D2F7815C432C9057C031&encoding-type=url HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Length: 1056
Date: Fri, 24 Feb 2012 10:19:18 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<CompleteMultipartUpload>
    <Part>
        <PartNumber>1</PartNumber>
        <ETag>"3349DC700140D7F86A0784842780"</ETag>
    </Part>
    <Part>
        <PartNumber>5</PartNumber>
        <ETag>"8EFDA8BE206636A695359836FE0A"</ETag>
    </Part>
    <Part>
        <PartNumber>8</PartNumber>
        <ETag>"8C315065167132444177411FDA14"</ETag>
    </Part>
</CompleteMultipartUpload>
`


Sample success responses


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Content-Length: 329
Content-Type: Application/xml
Connection: keep-alive
x-oss-request-id: 594f0751-3b1e-168f-4501-4ac71d21
Date: Fri, 24 Feb 2012 10:19:18 GMT
<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
    <EncodingType>url</EncodingType>
    <Location>http://oss-example.oss-cn-hangzhou.aliyuncs.com /multipart.data</Location>
    <Bucket>oss-example</Bucket>
    <Key>multipart.data</Key>
    <ETag>"B864DB6A936D376F9F8D3ED3BBE540"</ETag>
</CompleteMultipartUploadResult>
`


-

Complete the multipart upload task of an object in a versioned bucket


Sample requests


`plaintext
POST /multipart.data?uploadId=63C06A5CFF6F4AE4A6BB3AD7F01C  HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Length: 223
Date: Tue, 09 Apr 2019 07:01:56 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<CompleteMultipartUpload>
    <Part>
        <PartNumber>1</PartNumber>
        <ETag>"25A9F4ABFCC05743DF6E2C886C56"</ETag>
    </Part>
    <Part>
        <PartNumber>5</PartNumber>
        <ETag>"25A9F4ABFCC05743DF6E2C886C56"</ETag>
    </Part>
</CompleteMultipartUpload>
`


Sample success responses


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Content-Length: 314
Content-Type: Application/xml
Connection: keep-alive
x-oss-version-id: CAEQMxiBgID6v86D0BYiIDc3ZDI0YTBjZGQzYjQ2Mjk4OWVjYWNiMDljYzhlN
x-oss-request-id: 5CAC4364B7AEADE017000662
Date: Tue, 09 Apr 2019 07:01:56 GMT
<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult>
  <Location>http://oss-example.oss-cn-hangzhou.aliyuncs.com/multipart.data</Location>
  <Bucket>oss-example</Bucket>
  <Key>multipart.data</Key>
  <ETag>"097DE458AD02B5F89F9D0530231876"</ETag>
</CompleteMultipartUploadResult>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the CompleteMultipartUpload operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/java-multipart-upload#concept-84786-zh)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-multipart-upload)

-

[Harmony](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-harmony-sdk)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-using-oss-sdk-for-php-v2)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-9#concept-90222-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-10#concept-91103-zh)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-11)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-8#concept-90222-zh)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-3#concept-hgg-3vb-dhb)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-6#concept-1925841)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-7)

## ossutil


For information about the ossutil command that corresponds to the CompleteMultipartUpload operation, see [complete-multipart-upload](https://www.alibabacloud.com/help/en/oss/developer-reference/complete-multipart-upload).

## Error codes











-



-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidDigest | 400 | The Content-MD5 value in the request is different from the MD5 hash calculated by OSS. To prevent errors during data transmission, you can include the Content-MD5 value in the request. OSS calculates the MD5 hash of the uploaded data and compares it with the Content-MD5 value in the request. |
| FileAlreadyExists | 409 | Possible causes:The request contains the x-oss-forbid-overwrite=true header, and the bucket contains an object that has the same name as the object that you want to upload. The object on which you want to perform the CompleteMultipartUpload operation is a directory within a bucket for which the hierarchical namespace feature is enabled. |


Thank you! We've received your  feedback.