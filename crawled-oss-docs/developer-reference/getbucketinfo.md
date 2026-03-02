# Call GetBucketInfo to view bucket information

Call the GetBucketInfo operation to view information about a bucket.

## Usage notes


-

You can send this request from any Object Storage Service (OSS) endpoint.

-

By default, an Alibaba Cloud account has the permission to view bucket information. If you want to use a Resource Access Management (RAM) user or Security Token Service (STS) to view bucket information, you must have the `oss:GetBucketInfo` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /?bucketInfo HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-acl#concept-fnt-4z1-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketversioning#reference-w2w-nm3-fhb)


(https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db)


-


-


| Name | Type | Example | Description |
| --- | --- | --- | --- |
| BucketInfo | Container | N/A | The container for bucket information.Child node: BucketParent node: None |
| Bucket | Container | N/A | The container for bucket information.Parent node: BucketInfo |
| CreationDate | Time | 2013-07-31T10:56:21.000Z | The time when the bucket was created. The time is in UTC.Parent node: BucketInfo.Bucket |
| ExtranetEndpoint | String | oss-cn-hangzhou.aliyuncs.com | The public endpoint.Parent node: BucketInfo.Bucket |
| IntranetEndpoint | String | oss-cn-hangzhou-internal.aliyuncs.com | The internal endpoint.Parent node: BucketInfo.Bucket |
| Location | String | oss-cn-hangzhou | The region where the bucket is located. The value is the region ID for OSS.Parent node: BucketInfo.Bucket |
| StorageClass | String | Standard | The storage class of the bucket.Valid values: Standard, IA, Archive, and ColdArchive.For more information about storage classes, see Storage classes. |
| Name | String | oss-example | The name of the bucket.Parent node: BucketInfo.Bucket |
| ResourceGroupId | String | rg-aek27tc | The ID of the resource group to which the bucket belongs.If the bucket belongs to the default resource group, the value of this parameter is rg-default-id.Parent node: BucketInfo.Bucket |
| Owner | Container | N/A | The container for information about the bucket owner.Parent node: BucketInfo.Bucket |
| ID | String | 27183473914 | The user ID of the bucket owner.Parent node: BucketInfo.Bucket.Owner |
| DisplayName | String | username | The name of the bucket owner. This parameter has the same value as the ID.Parent node: BucketInfo.Bucket.Owner |
| AccessControlList | Container | N/A | The container for the access control list (ACL) of the bucket.For more information about bucket ACLs, see Bucket ACL.Parent node: BucketInfo.Bucket |
| Grant | Enumeration | private | The ACL of the bucket.Valid values: private, public-read, and public-read-write.Parent node: BucketInfo.Bucket.AccessControlList |
| DataRedundancyType | Enumeration | LRS | The data redundancy type of the bucket.Valid values: LRS and ZRS.Parent node: BucketInfo.Bucket |
| Versioning | String | Enabled | The versioning state of the bucket.Valid values: Enabled and Suspended.For more information about versioning states, see PutBucketVersioning.Parent node: BucketInfo.Bucket |
| ServerSideEncryptionRule | Container | N/A | The container for server-side encryption rules.For more information about server-side encryption, see Server-side encryption.Parent node: BucketInfo.Bucket |
| SSEAlgorithm | String | KMS | The default server-side encryption method.Valid values: KMS and AES256.Parent node: BucketInfo.Bucket.ServerSideEncryptionRule |
| KMSMasterKeyID | String |  | The ID of the KMS key in use. This parameter is returned only if `SSEAlgorithm` is set to `KMS` and a key ID is specified. Otherwise, this parameter is empty.Parent node: BucketInfo.Bucket.ServerSideEncryptionRule |
| KMSDataEncryption | String | SM4 | The encryption algorithm for the object. If this parameter is not specified, AES-256 is used. This parameter is valid only when `SSEAlgorithm` is set to `KMS`.Parent node: BucketInfo.Bucket.ServerSideEncryptionRule |
| CrossRegionReplication | String | Disabled | The cross-region replication (CRR) status of the bucket.Valid values: Enabled and Disabled.Parent node: BucketInfo.Bucket |
| TransferAcceleration | String | Disabled | The transfer acceleration status of the bucket.Valid values: Enabled and Disabled.Parent node: BucketInfo.Bucket |
| HierarchicalNamespace | String | Enabled | The hierarchical namespace status of the bucket.Valid value: Enabled.Parent node: BucketInfo.Bucket |
| AccessMonitor | String | Enabled | The access tracking status of the bucket.Valid values: Enabled and Disabled.Parent node: BucketInfo.Bucket |
| BucketPolicy | Container | N/A | The container for log information.Parent node: BucketInfo.Bucket |
| LogBucket | String | examplebucket | The name of the bucket that stores log records.Parent node: BucketInfo.Bucket.BucketPolicy |
| LogPrefix | String | log/ | The directory where log files are stored.Parent node: BucketInfo.Bucket.BucketPolicy |
| BlockPublicAccess | Boolean | true | The configuration of Block Public Access for the bucket.true: Block Public Access is enabled.false: Block Public Access is disabled. |


## Examples


Sample request


`plaintext
Get /?bucketInfo HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 07:51:28 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample responses


-

Sample response for a successful request


`plaintext
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906
Date: Sat, 12 Sep 2015 07:51:28 GMT
Connection: keep-alive
Content-Length: 531
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<BucketInfo>
  <Bucket>
    <CreationDate>2013-07-31T10:56:21.000Z</CreationDate>
    <ExtranetEndpoint>oss-cn-hangzhou.aliyuncs.com</ExtranetEndpoint>
    <IntranetEndpoint>oss-cn-hangzhou-internal.aliyuncs.com</IntranetEndpoint>
    <Location>oss-cn-hangzhou</Location>
    <StorageClass>Standard</StorageClass>
    <TransferAcceleration>Disabled</TransferAcceleration>
    <CrossRegionReplication>Disabled</CrossRegionReplication>
    <HierarchicalNamespace>Enabled</HierarchicalNamespace>
    <Name>oss-example</Name>
    <ResourceGroupId>rg-aek27tc</ResourceGroupId>
    <Owner>
      <DisplayName>username</DisplayName>
      <ID>27183473914</ID>
    </Owner>
    <AccessControlList>
      <Grant>private</Grant>
    </AccessControlList>
    <Comment>test</Comment>
    <BucketPolicy>
      <LogBucket>examplebucket</LogBucket>
      <LogPrefix>log/</LogPrefix>
    </BucketPolicy>
  </Bucket>
</BucketInfo>
`


-

Sample response for a bucket that does not exist


`plaintext
HTTP/1.1 404
x-oss-request-id: 534B371674E88A4D8906
Date: Sat, 12 Sep 2015 07:51:28 GMT
Connection: keep-alive
Content-Length: 308
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>NoSuchBucket</Code>
  <Message>The specified bucket does not exist.</Message>
  <RequestId>568D547F31243C673BA1</RequestId>
  <HostId>nosuchbucket.oss.aliyuncs.com</HostId>
  <BucketName>nosuchbucket</BucketName>
  <EC>0015-00000101</EC>
</Error>
`


-

Sample response for an access denied error


`plaintext
HTTP/1.1 403
x-oss-request-id: 534B371674E88A4D8906
Date: Sat, 12 Sep 2015 07:51:28 GMT
Connection: keep-alive
Content-Length: 209
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>AccessDenied</Code>
  <Message>AccessDenied</Message>
  <RequestId>568D5566F2D0F89F5C0E</RequestId>
  <HostId>test.oss.aliyuncs.com</HostId>
</Error>
`


## SDK


You can use the SDKs for the following programming languages to call this operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information#concept-2348421)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/obtain-bucket-information-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-query-bucket-information)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-query-information-about-a-bucket)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-4#concept-2365066)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-2#concept-2351981)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-using-oss-sdk-for-csharp-v1#topic-2591171)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-3#concept-2382429)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/query-information-about-a-bucket#concept-2056671)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/query-bucket-information-5#concept-2502726)

## ossutil command-line tool


For more information about the ossutil command that corresponds to this operation, see [get-bucket-info](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-info).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The specified bucket does not exist. |
| AccessDenied | 403 | You do not have the permissions to view the bucket information. Only the bucket owner can view the bucket information. |


Thank you! We've received your  feedback.