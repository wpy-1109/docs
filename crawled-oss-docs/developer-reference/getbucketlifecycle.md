# GetBucketLifecycle

Queries the lifecycle rules that are configured for a bucket.

## Usage notes


To query the lifecycle rules that are configured for a bucket, you must have the `oss:GetBucketLifecycle` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /?lifecycle HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Examples


Sample requests


`plaintext
Get /?lifecycle HTTP/1.1
Host: oss-example.oss.aliyuncs.com
Date: Mon, 14 Apr 2014 01:17:29 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=host,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample responses


-

Lifecycle rules that are configured based on the last modification time


`plaintext
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 14 Apr 2014 01:17:29 GMT
Connection: keep-alive
Content-Length: 255
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration>
  <Rule>
    <ID>delete after one day</ID>
    <Prefix>logs1/</Prefix>
    <Status>Enabled</Status>
    <Expiration>
      <Days>1</Days>
    </Expiration>
  </Rule>
  <Rule>
    <ID>mtime transition1</ID>
    <Prefix>logs2/</Prefix>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>IA</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>mtime transition2</ID>
    <Prefix>logs3/</Prefix>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>IA</StorageClass>
      <IsAccessTime>false</IsAccessTime>
    </Transition>
  </Rule>
</LifecycleConfiguration>
`


-

Lifecycle rules that are configured based on the last access time


> NOTE:

> NOTE: 


> NOTE: Note 

If a lifecycle rule is configured for a bucket based on the last access time, the AtimeBase element is included in the sample response. This element indicates that the timestamp of the last access time (the time since 1970-01-01 00:00:00 UTC) is the timestamp when access tracking is enabled for the bucket.


`plaintext
HTTP/1.1 200
x-oss-request-id: 
Date: Mon, 26 Jul 2021 01:17:29 GMT
Connection: keep-alive
Content-Length: length
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration>
  <Rule>
    <ID>atime transition1</ID>
    <Prefix>logs1/</Prefix>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>IA</StorageClass>
      <IsAccessTime>true</IsAccessTime>
      <ReturnToStdWhenVisit>false</ReturnToStdWhenVisit>
    </Transition>
    <AtimeBase>1631698332</AtimeBase>
  </Rule>
  <Rule>
    <ID>atime transition2</ID>
    <Prefix>logs2/</Prefix>
    <Status>Enabled</Status>
    <NoncurrentVersionTransition>
      <NoncurrentDays>10</NoncurrentDays>
      <StorageClass>IA</StorageClass>
      <IsAccessTime>true</IsAccessTime>
      <ReturnToStdWhenVisit>false</ReturnToStdWhenVisit>
    </NoncurrentVersionTransition>
    <AtimeBase>1631698332</AtimeBase>
  </Rule>
</LifecycleConfiguration>
`


-

No lifecycle rules configured


`plaintext
HTTP/1.1 404
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 14 Apr 2014 01:17:29 GMT
Connection: keep-alive
Content-Length: 278
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <BucketName>oss-example</BucketName>
  <Code>NoSuchLifecycle</Code>
  <Message>No Row found in Lifecycle Table.</Message>
  <RequestId>534B372974E88A4D8906</RequestId>
  <HostId> BucketName.oss.example.com</HostId>
</Error>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the GetBucketLifecycle operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/lifecycle-1#undefined)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-lifecycle-management)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-lifecycle)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules#undefined)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/lifecycle-5#concept-32140-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/lifecycle-rules-2#undefined)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules-4#concept-2071421)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules-3#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-lifecycle-rules-1#undefined)

## ossutil


For information about the ossutil command that corresponds to the GetBucketLifecycle operation, see [get-bucket-lifecycle](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-lifecycle).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 Forbidden | The error message returned because you do not have the permissions to query the lifecycle rules that are configured for a bucket. Only the bucket owner has the permissions to query the lifecycle rules that are configured for a bucket. |
| NoSuchBucket or NoSuchLifecycle | 404 Not Found | The error message returned because the bucket does not exist or no lifecycle rules are configured for the bucket. |


Thank you! We've received your  feedback.