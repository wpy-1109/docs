# GetBucketVersioning

You can call this operation to query the versioning state of a bucket.

## Request syntax


`plaintext
GET /? versioning HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














-


-


> NOTE:

> NOTE: 


> NOTE: 


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| VersioningConfiguration | Container | N/A | The container that stores the versioning state of the bucket. Child nodes: StatusParent nodes: none |
| Status | String | Enabled | The versioning state of the bucket.Parent nodes: VersioningConfigurationValid values: Enabled: indicates that versioning is enabled for the bucket.Suspended: indicates that versioning is suspended for the bucket.Note If versioning is not enabled for a bucket, the Status element is not contained in the response elements. |


## Examples


Sample request


`plaintext
GET /?versioning HTTP/1.1
Host: bucket-versioning.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 02:28:18 GMT
Authorization: OSS qn6q:77Dv
`


Sample responses


-

 Sample response for a bucket for which versioning is enabled


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 5CAC0342B7AEADE01700
Date: Tue, 09 Apr 2019 02:28:18 GMT
Content-Length: 121
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<? xml version="1.0" encoding="UTF-8"? >
<VersioningConfiguration>
    <Status>Enabled</Status>
</VersioningConfiguration>
`


-

Sample response for a bucket for which versioning is disabled


If versioning is disabled for the requested bucket, the versioning state of the bucket is not contained in the XML body of the response.


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 5CAC015CB7AEADE01700
Date: Tue, 09 Apr 2019 02:20:12 GMT
Content-Length: 74
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<VersioningConfiguration xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com"/>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the GetBucketVersioning operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/versioning-8#concept-265070)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-versioning-2#concept-265070)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-versioning-3)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-versioning#concept-2331567)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/versioning-4#concept-2486979)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/versioning-9#concept-2435967)

## ossutil


For information about the ossutil command that corresponds to the GetBucketVersioning operation, see [get-bucket-versioning](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-versioning).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | The error message returned because you do not have permissions to query the versioning state of the bucket.Only the bucket owner or RAM users that have the GetBucketVersioning permission can query the versioning state of a bucket. |
| NoSuchBucket | 404 | The error message returned because the specified bucket does not exist. |


Thank you! We've received your  feedback.