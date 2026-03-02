# PutBucketEncryption

You can call this operation to configure encryption rules for a bucket.

## Notes


The `oss:PutBucketEncryption` permission is required for configuring encryption rules for a bucket. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).


> NOTE:

> NOTE: 


> NOTE: Note 

Only the bucket owner or authorized RAM users can configure encryption rules for a bucket. Otherwise, OSS returns the 403 error. For more information about bucket encryption, see [Server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db).


## Request structure


`plaintext
PUT /? encryption HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
<? xml version="1.0" encoding="UTF-8"? >
<ServerSideEncryptionRule>
  <ApplyServerSideEncryptionByDefault>
    <SSEAlgorithm>AES256</SSEAlgorithm>
    <KMSMasterKeyID></KMSMasterKeyID>
  </ApplyServerSideEncryptionByDefault>
</ServerSideEncryptionRule>
`


## Request elements

















> NOTE:

> NOTE: 


> NOTE: 


(https://www.alibabacloud.com/help/en/kms/key-management-service/support/billing-of-kms#section-br1-k3j-kfb)


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/crr-in-specific-scenarios#section-qkp-d1h-2dr)


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| ServerSideEncryptionRule | Container | Yes | N/A | The container that stores server-side encryption rules. Child node: ApplyServerSideEncryptionByDefault |
| ApplyServerSideEncryptionByDefault | Container | Yes | N/A | The container that stores the default server-side encryption method. Child nodes: SSEAlgorithm and KMSMasterKeyID |
| SSEAlgorithm | String | Yes | AES256 | The default server-side encryption method. Valid values: KMS, AES256.Note If you use OSS on CloudBox, only AES-256 is supported.You are charged for calling API operations when you use CMKs to encrypt or decrypt data. For more information about the fees, see KMS pricing.In cross-region replications, if the default server-side encryption method is configured for the destination bucket and ReplicaCMKID is configured in the replication rule:If objects in the source bucket are not encrypted, they are encrypted using the default encryption method of the destination bucket after they are replicated.If objects in the source bucket are encrypted using SSE-KMS or SSE-OSS, they are encrypted using the same method after they are replicated.For more information, see Use cross-region replication with server-side encryption. |
| KMSDataEncryption | String | No | SM4 | The algorithm used to encrypt objects. If this element is not specified, objects are encrypted by using AES256. This element is valid only when the value of SSEAlgorithm is set to KMS.Valid value: SM4.If you use OSS on CloudBox, this parameter is not supported. |
| KMSMasterKeyID | String | No | 9468da86-3509-4f8d-a61e-6eab1eac | The CMK ID that must be specified when SSEAlgorithm is set to KMS and a specified CMK is used for encryption. In other cases, this element must be set to null.If you use OSS on CloudBox, this parameter is not supported. |


For more information about other common request headers included in PutBucketEncryption requests, such as Host and Date, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample requests


-

Set the encryption method to SSE-KMS


The following sample request can be sent to configure the encryption method of the bucket named oss-example to SSE-KMS:


`plaintext
PUT /? encryption HTTP/1.1
Date: Thu, 17 Apr 2025 11:09:13 GMT
Content-Length: ContentLength
Content-Type: application/xml
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<? xml version="1.0" encoding="UTF-8"? >
<ServerSideEncryptionRule>
  <ApplyServerSideEncryptionByDefault>
    <SSEAlgorithm>KMS</SSEAlgorithm>
    <KMSMasterKeyID>9468da86-3509-4f8d-a61e-6eab1eac</KMSMasterKeyID>
  </ApplyServerSideEncryptionByDefault>
</ServerSideEncryptionRule>
`


-

Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D
Date: Thur, 5 Nov 2020 11:09:13 GMT
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the PutBucketEncryption operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-6#concept-266387)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-server-side-encryption)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-server-side-encryption)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-1#concept-2311158)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-4#concept-2482290)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/server-side-encryption-7#concept-2382981)

## ossutil


For information about the ossutil command that corresponds to the PutBucketEncryption operation, see [put-bucket-encryption](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-encryption).

## Errors codes

















| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidEncryptionAlgorithmError | 400 | The error returned because the value of SSEAlgorithm is not KMS or AES256. The following error message is returned: The Encryption request you specified is not valid. Supported value: AES256/KMS. |
| InvalidArgument | 400 | The error returned because the value of SSEAlgorithm is AES256 but KMSMasterKeyID is specified. The following error message is returned: KMSMasterKeyID is not applicable if the default sse algorithm is not KMS. |


Thank you! We've received your  feedback.