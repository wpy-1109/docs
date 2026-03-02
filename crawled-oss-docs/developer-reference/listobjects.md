# List file information by using the GetBucket (ListObjects) API

You can call the GetBucket (ListObjects) operation to list information about all objects in a bucket. This information includes the object name, size, and last modified time.

## Usage notes


-

The GetBucket (ListObjects) operation has been updated to GetBucketV2 (ListObjectsV2). We recommend that you use the newer GetBucketV2 (ListObjectsV2) version when you develop applications. For backward compatibility, OSS continues to support GetBucket (ListObjects). For more information about GetBucketV2 (ListObjectsV2), see [ListObjectsV2 (GetBucketV2)](https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects-v2#reference-2520881).

-

Custom object metadata is not returned in the response to a GetBucket (ListObjects) request.

-

The GetBucket (ListObjects) operation is a bucket-level operation. Each time you call this operation, you are charged a fee equivalent to one PUT request. The fee is based on the storage class of the bucket. For more information, see [PUT API requests](https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees#section-0h5-sdd-8t2).

-

If versioning is enabled for a bucket, overwriting or deleting objects creates many delete markers and previous versions. We recommend that you [configure lifecycle rules](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time) to periodically remove delete markers and previous versions that are no longer needed. This helps avoid performance degradation when you list objects.

## Request syntax


`plaintext
GET / HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


This operation uses only common request headers, such as `Authorization` and `Host`. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request parameters

















-


-


> IMPORTANT:

> NOTE: 


> NOTE: 


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| delimiter | String | No | / | A character for grouping object names. All object names that contain the same string from the prefix to the first occurrence of the delimiter are grouped as a single element named CommonPrefixes.Default value: none. |
| marker | String | No | test1.txt | The object from which the listing operation begins. Objects are returned in alphabetical order after the specified marker.The marker is used for pagination. The value of this parameter must be less than 1,024 bytes in length.For a conditional query, even if the specified marker does not exist, the listing starts from the object that alphabetically follows the marker.Default value: none. |
| max-keys | String | No | 200 | The maximum number of objects to return. If the listing is not complete because of this limit, the response includes the NextMarker element to use as the marker for the next request.Valid values: 1 to 1000.Default value: 100. |
| prefix | String | No | fun | The prefix that the names of objects to be listed must contain.The prefix must be less than 1,024 bytes in length.When you use a prefix for a query, the returned keys also contain the prefix.If you set prefix to a directory name, all objects and subdirectories that recursively exist in the directory are listed.If you set delimiter to a forward slash (/) based on the prefix, only the objects in the directory are listed. The names of the subdirectories in the directory are returned in CommonPrefixes. The objects and directories that recursively exist in the subdirectories are not listed.For example, a bucket contains three objects: fun/test.jpg, fun/movie/001.avi, and fun/movie/007.avi. If you set prefix to fun/, the three objects are returned. If you set prefix to fun/ and delimiter to a forward slash (/), fun/test.jpg and fun/movie/ are returned.Default value: none. |
| encoding-type | String | No | url | The encoding type of the content in the response.Default value: none.Valid value: urlImportant The values of delimiter, marker, prefix, NextMarker, and Key are UTF-8 encoded. If the value of delimiter, marker, prefix, NextMarker, or Key contains control characters that are not supported by XML 1.0, you can specify the encoding-type parameter to encode these values in the response. |


## Response elements














-


-


> NOTE:

> NOTE: 


> NOTE: 

-


-




> NOTE:

> NOTE: 


> NOTE: 


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

(https://www.alibabacloud.com/help/en/oss/developer-reference/putsymlink)


-


-



-




| Name | Type | Example | Description |
| --- | --- | --- | --- |
| ListBucketResult | Container | N/A | The container for the results of a GetBucket request.Child nodes: Name, Prefix, Marker, MaxKeys, Delimiter, IsTruncated, Nextmarker, and ContentsParent node: None |
| Name | String | oss-example | The bucket name.Parent node: ListBucketResult |
| Prefix | String | fun/ | The prefix of the query results.Parent nodes: ListBucketResult or CommonPrefixes |
| Marker | String | test1.txt | The start position of this GetBucket (ListObjects) operation.Parent node: ListBucketResult |
| MaxKeys | String | 100 | The maximum number of results returned in the response.Parent node: ListBucketResult |
| Delimiter | String | / | The character used to group object names. All object names that contain the same string from the prefix to the first occurrence of the Delimiter character are grouped as a single element named CommonPrefixes.Parent node: ListBucketResult |
| EncodingType | String | url | The encoding type used for the returned results. If you specify the encoding-type parameter in the request, the Delimiter, Marker, Prefix, NextMarker, and Key elements in the response are encoded.Parent node: ListBucketResult |
| IsTruncated | Enumerated string | false | Indicates whether the results returned in the request are truncated.Valid values: true and falsetrue: Not all results are returned.false: All results are returned.Parent node: ListBucketResult |
| NextMarker | String | test100.txt | The start position of the next listing.Parent node: ListBucketResult |
| Contents | Container | N/A | The container for the metadata of each returned object.Parent node: ListBucketResult |
| Key | String | fun/test.jpg | The key of the object.Parent node: ListBucketResult.Contents |
| TransitionTime | Time | 2024-04-23T07:21:42.000Z | The time when the object was transitioned to the Cold Archive or Deep Cold Archive storage class based on a lifecycle rule.Note If the object is stored for more than 180 days after the storage class of the object is converted, you are not charged for the storage usage of the Cold Archive or Deep Cold Archive object that is stored for less than the minimum storage duration. If the object is stored for less than 180 days after the storage class of the object is converted, you are charged for the storage usage of the Cold Archive or Deep Cold Archive object that is stored for less than the minimum storage duration. You cannot use this header to query the time when the storage class of the object is converted to Infrequent Access (IA) or Archive based on lifecycle rules. You can determine whether the object is stored for more than the minimum storage duration based on the value of the Last-Modified header. Parent node: ListBucketResult.Contents |
| SealedTime | Time | 2020-05-21T12:07:15.000Z | The time when the seal operation was performed on the object.Note This field is returned only for an appendable object that is created using the AppendObject operation and has been sealed.Parent node: ListBucketResult.Contents |
| LastModified | Time | 2012-02-24T08:42:32.000Z | The time when the object was last modified.Note The minimum storage duration (30 days) of IA objects is calculated based on the last modified time of the objects. If the value of the Last-Modified header is 30 days earlier than the current time, you are not charged for the storage usage of the IA object that is stored for less than the minimum storage duration. The minimum storage duration (60 days) of Archive objects is calculated based on the last modified time of the objects. If the value of the Last-Modified header is 60 days earlier than the current time, you are not charged for the storage usage of the Archive object that is stored for less than the minimum storage duration. Parent node: ListBucketResult.Contents |
| ETag | String | 5B3C1A2E053D763E1B002CC607C5A0FE1 | The entity tag (ETag). An ETag is created when an object is created to identify the content of the object.For an object created by a PutObject request, the ETag value is the MD5 hash of the object content.For an object created by other methods, the ETag value is a unique value calculated based on a specific rule. The ETag value is not the MD5 hash of the object content.The ETag value can be used to check whether the object content has changed. Do not use the ETag value to verify the data integrity of an object.Parent node: ListBucketResult.Contents |
| Type | String | Normal | The type of the object. Valid values:Normal: The object is created by a simple upload.Multipart: The object is created by a multipart upload.Appendable: The object is created by an append upload.Symlink: The symbolic link is created by the PutSymlink operation. |
| Size | String | 344606 | The size of the returned object in bytes.Parent node: ListBucketResult.Contents |
| StorageClass | String | Standard | The storage class of the object.Parent node: ListBucketResult.Contents |
| RestoreInfo | String | ongoing-request="true” | The restored state of the object.This field is not returned if no RestoreObject request is submitted or the RestoreObject request has expired.If a RestoreObject request is submitted but the restore operation is not complete, the value of RestoreInfo is ongoing-request="true".If a RestoreObject request is submitted and the restore operation is complete, the value of RestoreInfo is ongoing-request="false", expiry-date="Thu, 24 Sep 2020 12:40:33 GMT". The expiry-date field indicates the expiration time of the restored object. |
| Owner | Container | N/A | The container for the information about the bucket owner.Child nodes: DisplayName and IDParent node: ListBucketResult.Contents |
| ID | String | 0022012 | The user ID of the bucket owner.Parent node: ListBucketResult.Contents.Owner |
| DisplayName | String | user_example | The name of the object owner.Parent node: ListBucketResult.Contents.Owner |
| CommonPrefixes | Container | N/A | If you specify the Delimiter parameter in the request, the response contains the CommonPrefixes element. This element indicates a collection of object names that have a common prefix and end with the delimiter.Parent node: ListBucketResult |


For more information about other common response headers, such as `x-oss-request-id` and `Content-Type`, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Simple request


`plaintext
GET / HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 08:43:27 GMT
Content-Type: application/xml
Content-Length: 1866
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
<Name>examplebucket</Name>
<Prefix></Prefix>
<Marker></Marker>
<MaxKeys>100</MaxKeys>
<Delimiter></Delimiter>
<IsTruncated>false</IsTruncated>
<Contents>
      <Key>fun/movie/001.avi</Key>
      <TransitionTime>2024-04-23T07:21:42.000Z</TransitionTime>
      <LastModified>2012-02-24T08:43:07.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user-example</DisplayName>
      </Owner>
</Contents>
<Contents>
      <Key>fun/movie/007.avi</Key>
      <LastModified>2012-02-24T08:43:27.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user-example</DisplayName>
      </Owner>
</Contents>
<Contents>
      <Key>fun/test.jpg</Key>
      <LastModified>2012-02-24T08:42:32.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user-example</DisplayName>
      </Owner>
</Contents>
<Contents>
      <Key>oss.jpg</Key>
      <LastModified>2012-02-24T06:07:48.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user-example</DisplayName>
      </Owner>
</Contents>
</ListBucketResult>
`


-

Request with the prefix parameter


`plaintext
GET /?prefix=fun HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 08:43:27 GMT
Content-Type: application/xml
Content-Length: 1464
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
<Name>examplebucket</Name>
<Prefix>fun</Prefix>
<Marker></Marker>
<MaxKeys>100</MaxKeys>
<Delimiter></Delimiter>
<IsTruncated>false</IsTruncated>
<Contents>
      <Key>fun/movie/001.avi</Key>
      <LastModified>2012-02-24T08:43:07.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user_example</DisplayName>
      </Owner>
</Contents>
<Contents>
      <Key>fun/movie/007.avi</Key>
      <LastModified>2012-02-24T08:43:27.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user_example</DisplayName>
      </Owner>
</Contents>
<Contents>
      <Key>fun/test.jpg</Key>
      <LastModified>2012-02-24T08:42:32.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user_example</DisplayName>
      </Owner>
</Contents>
</ListBucketResult>
`


-

Request with the prefix and delimiter parameters


`plaintext
GET /?prefix=fun/&delimiter=/ HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2012 08:43:27 GMT
Content-Type: application/xml
Content-Length: 712
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
<Name>examplebucket</Name>
<Prefix>fun/</Prefix>
<Marker></Marker>
<MaxKeys>100</MaxKeys>
<Delimiter>/</Delimiter>
<IsTruncated>false</IsTruncated>
<Contents>
      <Key>fun/test.jpg</Key>
      <LastModified>2012-02-24T08:42:32.000Z</LastModified>
      <ETag>"5B3C1A2E053D763E1B002CC607C5A0FE1"</ETag>
      <Type>Normal</Type>
      <Size>344606</Size>
      <StorageClass>Standard</StorageClass>
      <Owner>
          <ID>0022012</ID>
          <DisplayName>user_example</DisplayName>
      </Owner>
</Contents>
<CommonPrefixes>
      <Prefix>fun/movie/</Prefix>
</CommonPrefixes>
</ListBucketResult>
`


-

Paginated request that specifies the marker parameter


In this example, max-keys is set to 2, which indicates that a maximum of two objects are returned.


`plaintext
GET /?max-keys=2&marker=test1.txt HTTP/1.1
Host: examplebucket.oss-cn-shenzhen.aliyuncs.com
Accept-Encoding: identity
Accept: */*
Connection: keep-alive
User-Agent: aliyun-sdk-python/2.11.0(Darwin/18.2.0/x86_64;3.4.1)
date: Tue, 26 May 2020 08:39:48 GMT
authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


The NextMarker element in the response can be used as the marker for the next request.


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 26 May 2020 08:39:48 GMT
Content-Type: application/xml
Content-Length: 1032
Connection: keep-alive
x-oss-request-id: 5ECCD5D4881816373582xxx
x-oss-server-time: 3

<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult>
  <Name>examplebucket</Name>
  <Prefix></Prefix>
  <Marker>test1.txt</Marker>
  <MaxKeys>2</MaxKeys>
  <Delimiter></Delimiter>
  <EncodingType>url</EncodingType>
  <IsTruncated>true</IsTruncated>
  <NextMarker>test100.txt</NextMarker>
  <Contents>
    <Key>test10.txt</Key>
    <LastModified>2020-05-26T07:50:18.000Z</LastModified>
    <ETag>"C4CA4238A0B923820DCC509A6F75"</ETag>
    <Type>Normal</Type>
    <Size>1</Size>
    <StorageClass>Standard</StorageClass>
    <Owner>
      <ID>1305433xxx</ID>
      <DisplayName>1305433xxx</DisplayName>
    </Owner>
  </Contents>
  <Contents>
    <Key>test100.txt</Key>
    <LastModified>2020-05-26T07:50:20.000Z</LastModified>
    <ETag>"C4CA4238A0B923820DCC509A6F75"</ETag>
    <Type>Normal</Type>
    <Size>1</Size>
    <StorageClass>Standard</StorageClass>
    <Owner>
      <ID>1305433xxx</ID>
      <DisplayName>1305433xxx</DisplayName>
    </Owner>
  </Contents>
</ListBucketResult>
`


-

Request for a bucket that contains Archive or Cold Archive objects


Assume that the examplebucket bucket contains the exampleobject1.txt, exampleobject2.txt, and exampleobject3.txt objects. All three objects are in the Cold Archive storage class. The states of the three objects are as follows:


-

For exampleobject1.txt, a RestoreObject request has not been submitted, or the submitted RestoreObject request has expired.

-

For exampleobject2.txt, a RestoreObject request has been submitted, and the restore operation is in progress.

-

For exampleobject3.txt, a RestoreObject request has been submitted and the restore operation is complete.


Sample request


`plaintext
GET / HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 08:43:27 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Date: Fri, 24 Feb 2012 08:43:27 GMT
Content-Type: application/xml
Content-Length: 1866
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
  <Name>examplebucket</Name>
  <Prefix></Prefix>
  <Marker></Marker>
  <MaxKeys></MaxKeys>
  <Delimiter></Delimiter>
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


## SDK


You can use the SDKs for the following programming languages to call this operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-list-buckets)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-list-buckets)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-9)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-using-oss-sdk-for-csharp-v1)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-4)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-8)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/list-buckets-7)

## ossutil command-line tool


For more information about the ossutil command that corresponds to the GetBucket operation, see [list-objects (get-bucket)](https://www.alibabacloud.com/help/en/oss/developer-reference/list-objects-get-bucket).

## Error codes














-


-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The specified bucket does not exist. Check whether the bucket name is valid. |
| AccessDenied | 403 | You do not have the required permissions to access the bucket. Only the bucket owner and users who are granted the oss:ListObjects permission can access the bucket. |
| InvalidArgument | 400 | The value of max-keys is less than 0 or greater than 1,000.The length of the prefix, marker, or delimiter parameter is invalid. |


Thank you! We've received your  feedback.