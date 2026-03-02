# Call the ListParts operation to list all uploaded parts that belong to a specific upload ID

Lists all parts that are uploaded by using a specific upload ID.

## Usage notes


-

The results returned by Object Storage Service (OSS) are listed in ascending order of part numbers.

-

We recommend that you generate a part list by using locally recorded data instead of using the part number and ETags in the response to a ListParts request. Parts uploaded by using a specific upload ID may be accidentally overwritten. In this case. you may need to delete some unnecessary parts before you call the CompleteMultipartUpload operation, or the part data received by OSS may not meet expectations due to errors during network transmission. If the part number and ETag that correspond to each part are not recorded locally, the part data that meets expectations cannot be found in the response to a ListParts request. As a result, the consistency and integrity of the part data uploaded to OSS and the original content cannot be verified.

## Permissions


By default, an Alibaba Cloud account has full permissions on resources in the account. In contrast, RAM users and RAM roles associated with an Alibaba Cloud account initially have no permissions. To manage resources by using a RAM user or role, you must grant the required permissions via [RAM policies](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).














| API | Action | Description |
| --- | --- | --- |
| ListParts | oss:ListParts | Lists all parts that are uploaded by using a specified upload ID. |


## Request syntax


`plaintext
Get  /ObjectName?uploadId=UploadId HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: Signature
`


## Request headers


All headers in a ListParts request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request parameters














| Parameter | Type | Example | Description |
| --- | --- | --- | --- |
| uploadId | String | 0004B999EF5A239BB9138C6227D6 | The ID of the multipart upload task. By default, this parameter is left empty. |
| max-parts | Integer | 1000 | The maximum number of parts that can be returned by OSS. Default value: 1000.Maximum value: 1000. |
| part-number-marker | Integer | 100 | The position from which the list starts. All parts whose part numbers are greater than the value of this parameter are listed. By default, this parameter is left empty. |
| encoding-type | String | url | The encoding type of the object name in the response. The object name can contain characters that are encoded in UTF-8. However, the XML 1.0 standard cannot be used to parse certain control characters such as characters with an ASCII value from 0 to 10. You can configure this parameter to encode the object names in the response. By default, this parameter is left empty.Valid value: url. |


## Response headers


All headers in the response to a ListParts request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














| Element | Type | Example | Description |
| --- | --- | --- | --- |
| ListPartsResult | Container | N/A | The container that stores the response of the ListParts request. Child nodes: Bucket, Key, UploadId, PartNumberMarker, NextPartNumberMarker, MaxParts, IsTruncated, and Part Parent nodes: none |
| Bucket | String | multipart_upload | The name of the bucket. Parent nodes: ListPartsResult |
| EncodingType | String | url | The encoding type of the object name in the response. If the encoding-type parameter is specified in the request, the object name in the response is encoded. Parent nodes: ListPartsResult |
| Key | String | multipart.data | The name of the object. Parent nodes: ListPartsResult |
| UploadId | String | 0004B999EF5A239BB9138C6227D69F95 | The ID of the upload task. Parent nodes: ListPartsResult |
| PartNumberMarker | Integer | 10 | The position from which the list starts. All parts whose part numbers are greater than the value of this parameter are listed. Parent nodes: ListPartsResult |
| NextPartNumberMarker | Integer | 5 | The NextPartNumberMarker value that is used for the PartNumberMarker value in a subsequent request when the response does not contain all required results. Parent nodes: ListPartsResult |
| MaxParts | Integer | 1000 | The maximum number of parts in the response. Parent nodes: ListPartsResult |
| IsTruncated | Enumerated string | false | Indicates whether the list of parts returned in the response has been truncated. A value of true indicates that the response does not contain all required results. A value of false indicates that the response contains all required results. Valid values: true and false.Parent nodes: ListPartsResult |
| Part | Container | N/A | The container that stores the information about parts. Child nodes: PartNumber, LastModified, ETag, and Size Parent nodes: ListPartsResult |
| PartNumber | Integer | 1 | The number that identifies a part. Parent nodes: ListPartsResult.Part |
| LastModified | Date | 2012-02-23T07:01:34.000Z | The time when the part was uploaded. Parent nodes: ListPartsResult.Part |
| ETag | String | 3349DC700140D7F86A0784842780 | The ETag of the uploaded part. Parent nodes: ListPartsResult.Part |
| Size | Integer | 6291456 | The size of the uploaded parts. Parent nodes: ListPartsResult.Part |


## Examples


Sample request


`plaintext
Get  /multipart.data?uploadId=0004B999EF5A239BB9138C6227D6  HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 23 Feb 2012 07:13:28 GMT
Authorization: OSS qn6q:77Dv
`


Sample success response


`plaintext
HTTP/1.1 200
Server: AliyunOSS
Connection: keep-alive
Content-length: 1221
Content-type: application/xml
x-oss-request-id: 106452c8-10ff-812d-736e-c865294afc1c
Date: Thu, 23 Feb 2012 07:13:28 GMT

<?xml version="1.0" encoding="UTF-8"?>
<ListPartsResult xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
    <Bucket>multipart_upload</Bucket>
    <Key>multipart.data</Key>
    <UploadId>0004B999EF5A239BB9138C6227D6</UploadId>
    <NextPartNumberMarker>5</NextPartNumberMarker>
    <MaxParts>1000</MaxParts>
    <IsTruncated>false</IsTruncated>
    <Part>
        <PartNumber>1</PartNumber>
        <LastModified>2012-02-23T07:01:34.000Z</LastModified>
        <ETag>"3349DC700140D7F86A0784842780"</ETag>
        <Size>6291456</Size>
    </Part>
    <Part>
        <PartNumber>2</PartNumber>
        <LastModified>2012-02-23T07:01:12.000Z</LastModified>
        <ETag>"3349DC700140D7F86A0784842780"</ETag>
        <Size>6291456</Size>
    </Part>
    <Part>
        <PartNumber>5</PartNumber>
        <LastModified>2012-02-23T07:02:03.000Z</LastModified>
        <ETag>"7265F4D211B56873A381D321F586"</ETag>
        <Size>1024</Size>
    </Part>
</ListPartsResult>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the ListParts operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/java-multipart-upload#section-emy-ep5-dlm)

-

[PHP](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload#section-ke5-fgm-wj8)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/use-oss-python-sdk-to-multipart-upload#section-gza-kj0-fb6)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-3#section-jo5-fg1-yua)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-11#section-ftg-q6l-k62)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-6#section-5mg-qgm-s1a)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-7#section-fdc-mgg-4fb)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-multipart-upload)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-9#section-alv-2zy-zgb)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/multipart-upload-10#section-62b-vc5-24z)

## ossutil


For information about the ossutil command that corresponds to the ListParts operation, see [list-parts](https://www.alibabacloud.com/help/en/oss/developer-reference/list-parts).

Thank you! We've received your  feedback.