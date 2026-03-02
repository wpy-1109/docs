# Object Storage Service ListObjectsV2 (GetBucketV2) API

The ListObjectsV2 (GetBucketV2) operation lists information about objects in a bucket.

## Request syntax


`http
GET /?list-type=2 HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Usage notes


The ListObjectsV2 (GetBucketV2) request does not return custom object metadata. By default, a single response returns a maximum of 100 objects. To retrieve all objects, you must retrieve them in segments using parameters such as NextContinuationToken and continuationToken.


-

To list all objects in a bucket, you must have the `oss:ListObjects` permission.

-

If you enable [log storage](https://www.alibabacloud.com/help/en/oss/user-guide/logging#concept-t3h-4hd-5db) or [real-time log query](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/#concept-eyb-1n5-1gb), the value of the operation field in the access logs generated for this operation is `GetBucket`.

-

If versioning is enabled for a bucket, overwrite or accidental delete operations create many delete markers and previous versions. [Configure a lifecycle rule](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time) to periodically clean up delete markers and unneeded previous versions to prevent a decrease in list performance.

-

Calls to the ListObjectsV2 (GetBucketV2) operation are billed as PUT requests. For more information, see [PUT requests](https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees#section-0h5-sdd-8t2).

## Request parameters

















-



-




-


-


-


-


-


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| list-type | Number | Yes | 2 | The value is fixed to 2. |
| delimiter | String | No | / | A character for grouping object names. All object names that contain the specified prefix and appear before the first occurrence of the delimiter are grouped as an element (CommonPrefixes).Default value: none |
| start-after | String | No | b | Specifies that the list of objects is returned starting from the object that alphabetically follows the start-after value. This parameter is used for pagination. The parameter must be less than 1024 bytes in length.For a conditional query, even if the start-after value does not exist in the list, the response starts from the next object that follows the start-after value in alphabetical order.Default value: none |
| continuation-token | String | No | test1.txt | Specifies the token from which the list operation starts. You can obtain this token from the NextContinuationToken value in the response of a previous ListObjectsV2 (GetBucketV2) operation. |
| max-keys | Number | No | 100 | Specifies the maximum number of objects to return.The value must be greater than 0 and less than or equal to 1000.Default value: 100If not all objects can be listed in a single response due to the max-keys setting, the response includes NextContinuationToken. Use this token as the continuation-token for the next request.The number of returned objects is not guaranteed to reach the specified max-keys value. If this occurs, get the NextContinuationToken from the response and use it as the continuation-token for the next request. |
| prefix | String | No | a | Limits the response to keys that begin with the specified prefix. If you set prefix to a folder name, the operation lists all files and subfolders recursively within that folder.If you use the prefix parameter with the delimiter parameter set to a forward slash (/), the operation lists only the direct files in that folder. Subfolder names are returned in CommonPrefixes, and the contents of the subfolders are not listed.For example, a bucket contains three objects: fun/test.jpg, fun/movie/001.avi, and fun/movie/007.avi. If you set prefix to fun/, all three objects are returned. If you set prefix to fun/ and delimiter to a forward slash (/), the fun/test.jpg file and the fun/movie/ folder are returned.The parameter must be less than 1024 bytes in length.The prefix parameter cannot start with a forward slash (/). If the prefix parameter is empty, all objects in the bucket are listed by default.When you query using prefix, the returned keys still include the prefix.Default value: none |
| encoding-type | String | No | url | Encodes the response and specifies the encoding type.Default value: noneValid value: urlIf `delimiter`, `start-after`, `prefix`, `NextContinuationToken`, or `Key` contains control characters that are not supported by XML 1.0, you can specify the `encoding-type` parameter to URL-encode these elements in the response.The `delimiter`, `start-after`, `prefix`, `NextContinuationToken`, and `Key` parameters use UTF-8 character encoding. |
| fetch-owner | Boolean | No | false | Specifies whether to include owner information in the response.Valid values: true, falsetrue: The response includes owner information.false: The response does not include owner information.Default value: false |


## Response parameters














-


-


-


-


-


-


-



-




| Name | Type | Example | Description |
| --- | --- | --- | --- |
| Contents | Container | N/A | A container for the metadata of each returned object.Parent node: ListBucketResult |
| CommonPrefixes | Container | N/A | If the request specifies the Delimiter parameter, the response includes the CommonPrefixes element. This element indicates a collection of object names that end with the delimiter and share a common prefix.Parent node: ListBucketResultChild node: Prefix |
| Delimiter | String | / | The character used to group object names. All object names that contain the specified prefix and appear before the first occurrence of the delimiter are grouped as a CommonPrefixes element.Parent node: ListBucketResult |
| EncodingType | String | N/A | The encoding type used in the response. If `encoding-type` is specified in the request, the `Delimiter`, `StartAfter`, `Prefix`, `NextContinuationToken`, and `Key` elements in the response are encoded.Parent node: ListBucketResult |
| DisplayName | String | user_example | The display name of the object owner.Parent node: ListBucketResult.Contents.Owner |
| ETag | String | 5B3C1A2E053D763E1B002CC607C5A0FE1 | The ETag is created when an object is generated and uniquely identifies the content of the object.Parent node: ListBucketResult.ContentsFor an object created by a PutObject request, the ETag value is the MD5 hash of its content.For an object created in other ways, the ETag value is a unique value generated based on a specific calculation rule, but it is not the MD5 hash of its content.The ETag value can be used to check if the object content has changed. Do not use the ETag value as the basis for MD5 validation to ensure data integrity. |
| ID | String | 0022012 | The user ID of the bucket owner.Parent node: ListBucketResult.Contents.Owner |
| IsTruncated | Enumerated string | false | Indicates whether the returned results are truncated.Return values: true, falsetrue indicates that not all results are returned.false indicates that all results are returned.Parent node: ListBucketResult |
| Key | String | fun/test.jpg | The name of the object key.Parent node: ListBucketResult.Contents |
| LastModified | Time | 2012-02-24T08:42:32.000Z | The time when the object was last modified.Parent node: ListBucketResult.Contents |
| ListBucketResult | Container | N/A | A container for the results of the GetBucket request.Child nodes: Name, Prefix, StartAfter, MaxKeys, Delimiter, IsTruncated, NextContinuationToken, ContentsParent node: None |
| StartAfter | String | test1.txt | If the request specifies the StartAfter parameter, the response includes the StartAfter element. |
| MaxKeys | Number | 100 | The maximum number of results returned in the response.Parent node: ListBucketResult |
| Name | String | examplebucket | The name of the bucket.Parent node: ListBucketResult |
| Owner | Container | N/A | A container for the bucket owner's information.Child nodes: DisplayName, IDParent node: ListBucketResult.Contents |
| Prefix | String | fun/ | The prefix of the query results.Parent node: ListBucketResult |
| Type | String | Normal | File typeValid values: Normal, Multipart, Appendable, and Symlink.Parent node: ListBucketResult.Contents |
| Size | Number | 344606 | The size of the object in bytes.Parent node: ListBucketResult.Contents |
| StorageClass | String | Standard | The storage class of the object.Parent node: ListBucketResult.Contents |
| SealedTime | Time | 2020-05-21T12:07:15.000Z | The time when the Seal operation was performed on the object. This field is returned when you access an Appendable Object that is in the Sealed state.Parent node: ListBucketResult.Contents |
| ContinuationToken | String | test1.txt | If the request specifies the ContinuationToken parameter, the response includes the ContinuationToken element.Parent node: ListBucketResult |
| KeyCount | Number | 6 | The number of keys returned in this request. If the Delimiter parameter is specified, KeyCount is the sum of the number of Key and CommonPrefixes elements.Parent node: ListBucketResult |
| NextContinuationToken | String | CgJiYw-- | Indicates that the ListObjectsV2 (GetBucketV2) request has more results. To get the next set of results, specify the NextContinuationToken value as the ContinuationToken for the next request.Parent node: ListBucketResult |
| RestoreInfo | String | ongoing-request="true" | The restored state of the object.This field is not returned if no RestoreObject request is submitted or the RestoreObject request has expired.If a RestoreObject request is submitted but the restore operation is not complete, the value of RestoreInfo is ongoing-request="true".If a RestoreObject request is submitted and the restore operation is complete, the value of RestoreInfo is ongoing-request="false", expiry-date="Thu, 24 Sep 2020 12:40:33 GMT". The expiry-date field indicates the expiration time of the restored object.Parent node: ListBucketResult.Contents |


## Examples

### Simple request


-

Sample request


`http
GET /?list-type=2 HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Thu, 17 Apr 2025 08:43:27 GMT
Content-Type: application/xml
Content-Length: 1866
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Name>examplebucket</Name>
    <Prefix></Prefix>
    <MaxKeys>100</MaxKeys>
    <EncodingType>url</EncodingType>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>a</Key>
        <LastModified>2020-05-18T05:45:43.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>a/b</Key>
        <LastModified>2020-05-18T05:45:47.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>b</Key>
        <LastModified>2020-05-18T05:45:50.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>b/c</Key>
        <LastModified>2020-05-18T05:45:54.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>bc</Key>
        <LastModified>2020-05-18T05:45:59.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>c</Key>
        <LastModified>2020-05-18T05:45:57.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <KeyCount>6</KeyCount>
</ListBucketResult>
`


### Request with the prefix parameter


-

Sample request


`http
GET /?list-type=2&prefix=a HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Thu, 17 Apr 2025 08:43:27 GMT
Content-Type: application/xml
Content-Length: 1464
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Name>examplebucket</Name>
    <Prefix>a</Prefix>
    <MaxKeys>100</MaxKeys>
    <EncodingType>url</EncodingType>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>a</Key>
        <LastModified>2020-05-18T05:45:43.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>a/b</Key>
        <LastModified>2020-05-18T05:45:47.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <KeyCount>2</KeyCount>
</ListBucketResult>
`


### Request with the prefix and delimiter parameters


-

Sample request


`http
GET /?list-type=2&prefix=a/&delimiter=/ HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Thu, 17 Apr 2025 08:43:27 GMT
Content-Type: application/xml
Content-Length: 712
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Name>examplebucket</Name>
    <Prefix>a/</Prefix>
    <MaxKeys>100</MaxKeys>
    <Delimiter>/</Delimiter>
    <EncodingType>url</EncodingType>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>a/b</Key>
        <LastModified>2020-05-18T05:45:47.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <CommonPrefixes>
        <Prefix>a/b/</Prefix>
    </CommonPrefixes>
    <KeyCount>2</KeyCount>
</ListBucketResult>
`


### Request with the start-after, max-keys, and fetch-owner parameters


-

Sample request


`http
GET /?list-type=2&start-after=b&max-keys=3&fetch-owner=true HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Thu, 17 Apr 2025 08:43:27 GMT
Content-Type: application/xml
Content-Length: 712
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Name>examplebucket</Name>
    <Prefix></Prefix>
    <StartAfter>b</StartAfter>
    <MaxKeys>3</MaxKeys>
    <EncodingType>url</EncodingType>
    <IsTruncated>true</IsTruncated>
    <NextContinuationToken>CgJiYw--</NextContinuationToken>
    <Contents>
        <Key>b/c</Key>
        <LastModified>2020-05-18T05:45:54.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>1686240967192623</ID>
            <DisplayName>1686240967192623</DisplayName>
        </Owner>
    </Contents>
    <Contents>
        <Key>ba</Key>
        <LastModified>2020-05-18T11:17:58.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>1686240967192623</ID>
            <DisplayName>1686240967192623</DisplayName>
        </Owner>
    </Contents>
    <Contents>
        <Key>bc</Key>
        <LastModified>2020-05-18T05:45:59.000Z</LastModified>
        <ETag>"35A27C2B9EAEEB6F48FD7FB5861D"</ETag>
        <Size>25</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>1686240967192623</ID>
            <DisplayName>1686240967192623</DisplayName>
        </Owner>
    </Contents>
    <KeyCount>3</KeyCount>
</ListBucketResult>
`


### Request for a bucket that contains Archive or Cold Archive objects


-

Sample request


`http
GET /?list-type=2 HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Thu, 17 Apr 2025 08:43:27 GMT
Content-Type: application/xml
Content-Length: 1866
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
  <Name>examplebucket</Name>
  <Prefix></Prefix>
  <MaxKeys>100</MaxKeys>
  <EncodingType>url</EncodingType>
  <IsTruncated>false</IsTruncated>
  <Contents>
        <Key>exampleobject1.txt</Key>
        <LastModified>2020-06-22T11:42:32.000Z</LastModified>
        <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
        <Type>Normal</Type>
        <Size>344606</Size>
        <StorageClass>ColdArchive</StorageClass>
        <Owner>
            <ID>0022012</ID>
            <DisplayName>user-example</DisplayName>
        </Owner>
  </Contents>
  <Contents>
        <Key>exampleobject2.txt</Key>
        <LastModified>2020-06-22T11:42:32.000Z</LastModified>
        <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
        <Type>Normal</Type>
        <Size>344606</Size>
        <StorageClass>Standard</StorageClass>
        <RestoreInfo>ongoing-request="true"</RestoreInfo>
        <Owner>
            <ID>0022012</ID>
            <DisplayName>user-example</DisplayName>
        </Owner>
  </Contents>
  <Contents>
        <Key>exampleobject3.txt</Key>
        <LastModified>2020-06-22T11:42:32.000Z</LastModified>
        <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
        <Type>Normal</Type>
        <Size>344606</Size>
        <StorageClass>Standard</StorageClass>
        <RestoreInfo>ongoing-request="false", expiry-date="Thu, 24 Sep 2020 12:40:33 GMT"</RestoreInfo>
        <Owner>
            <ID>0022012</ID>
            <DisplayName>user-example</DisplayName>
        </Owner>
  </Contents>
</ListBucketResult>
`


The following describes the file states:


-

For exampleobject1.txt, a RestoreObject request has not been submitted or has expired.

-

For exampleobject2.txt, a RestoreObject request has been submitted, but the restore is not complete.

-

For exampleobject3.txt, a RestoreObject request has been submitted, and the restore is complete.

## Error codes





-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The specified bucket does not exist. Check whether the bucket name in the request complies with the naming conventions. |
| AccessDenied | 403 | You do not have permission to access the bucket. Only the bucket owner and users who are granted the oss:ListObjects permission can access the bucket. |
| InvalidArgument | 400 | The value of the max-keys parameter is less than 0 or greater than 1000.The length of the prefix, start-after, or delimiter parameter is invalid. |


## Integration methods


-

SDK


You can use SDKs for the following languages to call the ListObjectsV2 operation:


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-3)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-using-oss-sdk-for-python-v2)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-12)


(https://www.alibabacloud.com/help/en/oss/developer-reference/v2-list-objects)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-5)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-13)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-4)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-using-oss-sdk-for-php-v2)


(https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-15)


| Java | Python V2 | C | Go V2 | Node.js |
| --- | --- | --- | --- | --- |
| IOS | Android | Ruby | PHP V2 | .NET |


-

ossutil command line interface


For information about the ossutil command for the ListObjectsV2 operation, see [list-objects-v2 (get-bucket-v2)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-v2-get-bucket-v2).

Thank you! We've received your  feedback.