# GetBucketArchiveDirectRead

Queries whether real-time access of Archive objects is enabled for a bucket.

## Usage notes


-

To check whether real-time access of Archive objects is enabled for a bucket, you must have the `oss:GetBucketArchiveDirectRead` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Each region has its own Object Storage Service (OSS) endpoints. For more information about regions and their endpoints, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

## Request syntax


`http
GET /?bucketArchiveDirectRead HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a GetBucketArchiveDirectRead request are common request headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a GetBucketArchiveDirectRead request are common response headers. For more information about common response headers, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

















-


-


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| ArchiveDirectReadConfiguration | Container | Yes | N/A | The container that stores the configurations for real-time access of Archive objects. |
| Enabled | Boolean | Yes | true | Indicates whether real-time access of Archive objects is enabled for the bucket. Valid values:true false |


## Examples


-

Sample request


`http
GET /?bucketArchiveDirectRead HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Mon, 24 Apr 2023 15:56:37 GMT
Authorization: OSS qn6q:77Dv
`


-

Sample response


`http
GET /?bucketArchiveDirectRead HTTP/1.1
Date: Mon, 24 Apr 2023 15:56:37 GMT
Content-Length: 60
Content-Type: application/xml
Authorization: OSS qn6q:77Dv
Host: oss-example.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<ArchiveDirectReadConfiguration>
    <Enabled>true</Enabled>
</ArchiveDirectReadConfiguration>
`


## ossutil


For information about the ossutil command that corresponds to the GetBucketArchiveDirectRead operation, see [get-bucket-archive-direct-read](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-archive-direct-read).

Thank you! We've received your  feedback.