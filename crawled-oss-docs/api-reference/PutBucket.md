# PutBucket

You can call the PutBucket operation to create a bucket.

## Notes

- An Alibaba Cloud account can create a maximum of 100 buckets in each region.
- Each region has a corresponding endpoint. For more information about regions and endpoints, see Endpoints and data centers.
- If you use an Alibaba Cloud account to send multiple PutBucket requests for the same bucket, the first request creates the bucket and subsequent requests modify the bucket metadata, such as the bucket access control list (ACL).

## Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default.

| API | Action | Definition |
| --- | --- | --- |
| PutBucket | oss:PutBucket | Creates a bucket. |
| | oss:PutBucketAcl | After creating a bucket, this permission is required to modify the bucket ACL. |

## Request syntax

```
PUT / HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
x-oss-acl: Permission
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
</CreateBucketConfiguration>
```

## Request headers

| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-acl | String | No | private | The ACL of the bucket. Valid values: public-read-write, public-read, private (default). |
| x-oss-resource-group-id | String | No | rg-aek27tc**** | The ID of the resource group. |
| x-oss-bucket-tagging | String | No | k1=v1&k2=v2 | The tags of the bucket. |
| x-oss-hns-status | String | No | disabled | Whether to enable hierarchical namespace. Valid values: enabled, disabled (default). |
| x-oss-server-side-encryption | String | No | AES256 | Default server-side encryption method. Valid values: KMS, AES256. |
| x-oss-server-side-encryption-key-id | String | No | 9468da86-3509-4f8d-a61e-6eab1eac**** | The ID of the KMS key. Required when x-oss-server-side-encryption is set to KMS. |

## Request elements

| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| StorageClass | String | No | Standard | The storage class. Valid values: Standard (default), IA, Archive, ColdArchive, DeepColdArchive. |
| DataRedundancyType | String | No | LRS | The data redundancy type. Valid values: LRS (default), ZRS. |

## Response headers

| Header | Type | Example | Description |
| --- | --- | --- | --- |
| Location | String | /oss-example | The address of the bucket (forward slash + bucket name). |

## Examples

### Create a bucket in the default resource group

```http
PUT / HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 03:15:40 GMT
x-oss-acl: private
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=...
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
    <DataRedundancyType>LRS</DataRedundancyType>
</CreateBucketConfiguration>
```

**Response**

```http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Fri, 24 Feb 2017 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
Location: /oss-example
```

## Error codes

| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidBucketName | 400 | The specified bucket name does not follow the naming conventions. |
| AccessDenied | 403 | User authentication information is not included or you do not have the required permissions. |
| TooManyBuckets | 400 | The number of created buckets exceeds the upper limit (100 per region). |
| BucketAlreadyExists | 409 | A bucket with the same name exists or was recently deleted. Wait 4-8 hours before creating a bucket with the same name. |
