# GetBucketInfo

Call the GetBucketInfo operation to view information about a bucket.

## Usage notes

- You can send this request from any Object Storage Service (OSS) endpoint.
- By default, an Alibaba Cloud account has the permission to view bucket information. If you want to use a RAM user or STS to view bucket information, you must have the `oss:GetBucketInfo` permission.

## Request syntax

```
GET /?bucketInfo HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
```

## Request headers

All headers in a GetBucketInfo request are common request headers. For more information, see Common request headers.

## Response headers

All headers in the response to a GetBucketInfo request are common response headers. For more information, see Common response headers.

## Response elements

| Name | Type | Example | Description |
| --- | --- | --- | --- |
| BucketInfo | Container | N/A | The container for bucket information. Child node: Bucket. Parent node: None |
| Bucket | Container | N/A | The container for bucket information. Parent node: BucketInfo |
| CreationDate | Time | 2013-07-31T10:56:21.000Z | The time when the bucket was created (UTC). Parent node: BucketInfo.Bucket |
| ExtranetEndpoint | String | oss-cn-hangzhou.aliyuncs.com | The public endpoint. Parent node: BucketInfo.Bucket |
| IntranetEndpoint | String | oss-cn-hangzhou-internal.aliyuncs.com | The internal endpoint. Parent node: BucketInfo.Bucket |
| Location | String | oss-cn-hangzhou | The region where the bucket is located. Parent node: BucketInfo.Bucket |
| StorageClass | String | Standard | The storage class. Valid values: Standard, IA, Archive, ColdArchive. Parent node: BucketInfo.Bucket |
| Name | String | oss-example | The name of the bucket. Parent node: BucketInfo.Bucket |
| ResourceGroupId | String | rg-aek27tc******** | The ID of the resource group. Parent node: BucketInfo.Bucket |
| Owner | Container | N/A | The container for bucket owner info. Parent node: BucketInfo.Bucket |
| ID | String | 27183473914**** | The user ID of the bucket owner. Parent node: BucketInfo.Bucket.Owner |
| DisplayName | String | username | The name of the bucket owner (same as ID). Parent node: BucketInfo.Bucket.Owner |
| AccessControlList | Container | N/A | The container for bucket ACL. Parent node: BucketInfo.Bucket |
| Grant | Enumeration | private | The ACL. Valid values: private, public-read, public-read-write. Parent node: BucketInfo.Bucket.AccessControlList |
| DataRedundancyType | Enumeration | LRS | The data redundancy type. Valid values: LRS, ZRS. Parent node: BucketInfo.Bucket |
| Versioning | String | Enabled | The versioning state. Valid values: Enabled, Suspended. Parent node: BucketInfo.Bucket |
| ServerSideEncryptionRule | Container | N/A | The container for server-side encryption rules. Parent node: BucketInfo.Bucket |
| SSEAlgorithm | String | KMS | The default server-side encryption method. Valid values: KMS, AES256. |
| KMSMasterKeyID | String | ****** | The ID of the KMS key in use. |
| KMSDataEncryption | String | SM4 | The encryption algorithm. |
| CrossRegionReplication | String | Disabled | CRR status. Valid values: Enabled, Disabled. |
| TransferAcceleration | String | Disabled | Transfer acceleration status. Valid values: Enabled, Disabled. |
| HierarchicalNamespace | String | Enabled | Hierarchical namespace status. Valid value: Enabled. |
| AccessMonitor | String | Enabled | Access tracking status. Valid values: Enabled, Disabled. |
| BlockPublicAccess | Boolean | true | Block Public Access configuration. true: enabled, false: disabled. |

## Examples

### Sample request

```http
Get /?bucketInfo HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 07:51:28 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=...
```

### Sample success response

```xml
HTTP/1.1 200
x-oss-request-id: 534B371674E88A4D8906****
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
    <ResourceGroupId>rg-aek27tc********</ResourceGroupId>
    <Owner>
      <DisplayName>username</DisplayName>
      <ID>27183473914****</ID>
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
```

## Error codes

| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The specified bucket does not exist. |
| AccessDenied | 403 | You do not have the permissions to view the bucket information. Only the bucket owner can view the bucket information. |
