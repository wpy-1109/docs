# Call PutBucket to create a bucket

You can call the PutBucket operation to create a bucket.

## Notes


-

An Alibaba Cloud account can create a maximum of 100 buckets in each region.

-

Each region has a corresponding endpoint. For more information about regions and endpoints, see [Endpoints and data centers](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db).

-

If you use an Alibaba Cloud account to send multiple PutBucket requests for the same bucket, the first request creates the bucket and subsequent requests modify the bucket metadata, such as the bucket access control list (ACL). Sending multiple PutBucket requests may overwrite the bucket metadata. Proceed with caution.

-

From 10:00 (UTC+8) on October 13, 2025, OSS will implement a phased adjustment across all regions to enable Block Public Access by default for new buckets created using the API, OSS SDKs, or ossutil. For details about the exact times when the adjustment will take effect in each region, see [[Official Announcement] Adjustment to the Public Access Blocking Configurations for Newly Created Buckets](https://www.alibabacloud.com/en/notice/block_public_access_enabled_by_default_for_buckets_created_by_calling_api_operations_using_oss_sdks_482). Once Block Public Access is enabled, you cannot configure public access permissions, including public ACLs (public read and public read/write) and bucket policies that allows public access. You can disable this feature after the bucket is created if your business requires public access.

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).

















| API | Action | Definition |
| --- | --- | --- |
| PutBucket | oss:PutBucket | Creates a bucket. |
| oss:PutBucketAcl | After creating a bucket, this permission is required to modify the bucket ACL. |


## Request syntax


`http
PUT / HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
x-oss-acl: Permission
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
</CreateBucketConfiguration>
`


## Request headers

















-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-acl#concept-fnt-4z1-5db)


-


-


(https://www.alibabacloud.com/help/en/resource-management/resource-group/user-guide/view-basic-information-of-a-resource-group#task-2398293)(https://www.alibabacloud.com/help/en/resource-management/api-listresourcegroups#doc-api-ResourceManager-ListResourceGroups)


-


-


> NOTE:

> NOTE: 


> NOTE: 


(https://www.alibabacloud.com/help/en/kms/key-management-service/support/billing-of-kms#section-br1-k3j-kfb)


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/crr-in-specific-scenarios#section-qkp-d1h-2dr)


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-acl | String | No | private | The ACL of the bucket. Valid values:public-read-write: public-read-writepublic-read: public-readprivate (default): privateFor more information about bucket ACLs, see Set bucket ACLs. |
| x-oss-resource-group-id | String | No | rg-aek27tc | The ID of the resource group.If you include this header in the request and specify a resource group ID, the created bucket belongs to the specified resource group.If you set the resource group ID to rg-default-id, the created bucket belongs to the default resource group.If you do not include this header in the request, the created bucket belongs to the default resource group.You can obtain the resource group ID in the Resource Management console or by calling the ListResourceGroups operation. For more information, see View basic information of a resource group and ListResourceGroups. |
| x-oss-bucket-tagging | String | No | k1=v1&k2=v2 | The tags of the bucket. |
| x-oss-hns-status | String | No | disabled | Specifies whether to enable the hierarchical namespace feature for the bucket.You can enable the hierarchical namespace feature only when you create a bucket. You cannot change the hierarchical namespace status of an existing bucket.enabled: Enables the feature.After you enable the hierarchical namespace feature for a bucket, you can perform folder operations in the bucket, such as creating, deleting, and renaming folders.disabled (default): Disables the feature. |
| x-oss-server-side-encryption | String | No | AES256 | The default server-side encryption method.Valid values: KMS, AES256Note In OSS on CloudBox scenarios, only AES256 is supported.A small fee is charged for calling KMS API operations when you use KMS keys. For more information, see KMS pricing.When you use cross-region replication, if the destination bucket has default server-side encryption enabled and the replication rule has ReplicaCMKID configured, the following cases apply:If an object in the source bucket is not encrypted, the object replicated to the destination bucket is encrypted using the default encryption method of the destination bucket.If an object in the source bucket is encrypted using SSE-KMS or SSE-OSS, the object is encrypted using its original encryption method in the destination bucket.For more information, see Cross-region replication and server-side encryption. |
| x-oss-server-side-encryption-key-id | String | No | 9468da86-3509-4f8d-a61e-6eab1eac | The ID of the KMS key. This header is required when x-oss-server-side-encryption is set to KMS and you want to use a specified key for encryption. In other cases, this header must be empty.If you use OSS on CloudBox, this parameter is not supported. |


This operation also uses common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements

















-


-


-


-


-


-


-


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| StorageClass | String | No | Standard | The storage class of the bucket. Valid values:Standard (default): StandardIA: Infrequent AccessArchive: Archive StorageColdArchive: Cold ArchiveDeepColdArchive: Deep Cold ArchiveParent node: CreateBucketConfigurationChild nodes: none |
| DataRedundancyType | String | No | LRS | The data redundancy type of the bucket. Valid values:LRS (default)Locally redundant storage (LRS) stores redundant copies of your data on different storage devices in the same zone. This ensures data durability and availability even if two storage devices are damaged at the same time.ZRSZone-redundant storage (ZRS) uses a data redundancy mechanism across multiple zones. ZRS stores redundant copies of your data across multiple zones in the same region. This ensures that your data remains accessible even if a zone becomes unavailable.Parent node: CreateBucketConfigurationChild nodes: none |


## Response headers














| Header | Type | Example | Description |
| --- | --- | --- | --- |
| Location | String | /oss-example | The address of the bucket. It consists of a forward slash (/) and the bucket name.Default value: none |


This operation also uses common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Create a bucket in the default resource group


`http
PUT / HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 03:15:40 GMT
x-oss-acl: private
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
    <DataRedundancyType>LRS</DataRedundancyType>
</CreateBucketConfiguration>
`


-

Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2017 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
Location: /oss-example
`


-

Create a bucket in a specific resource group


Sample request


`http
PUT / HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 03:15:40 GMT
x-oss-acl: private
x-oss-resource-group-id: rg-aek27tc
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
</CreateBucketConfiguration>
`


Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2017 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
Location: /oss-example
`


## SDK


You can call the PutBucket operation using SDKs for the following programming languages:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket#concept-32012-zh)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/create-bucket-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-create-bucket)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-create-bucket)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-1#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#undefined)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-5#undefined)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/create-buckets-1#concept-2058317)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-4#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/create-a-bucket-2#undefined)

## ossutil


For more information about the ossutil command that corresponds to the PutBucket operation, see [put-bucket](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket).

## Error codes











-


-


-


-


-



-


| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidBucketName | 400 | The specified bucket name does not follow the naming conventions. |
| AccessDenied | 403 | Possible causes of the error:User authentication information is not included in the PutBucket request.You do not have the required permissions. |
| TooManyBuckets | 400 | The number of created buckets exceeds the upper limit. An Alibaba Cloud account can create a maximum of 100 buckets in a region. |
| BucketAlreadyExists | 409 | The request to create a Bucket with the same name as a deleted Bucket does not meet the time requirement.You try to create a bucket with the same name as a bucket that was recently deleted. After you delete a bucket, you must wait for several hours, typically 4 to 8 hours, before you can create another bucket with the same name.You use a RAM user or STS to call the PutBucket operation to create a bucket with the same name as an existing bucket.Only an Alibaba Cloud account can recreate a bucket with the same name.You do not have the permissions to call the PutBucketAcl operation. Make sure that the caller is granted the oss:PutBucketAcl permission using a bucket policy or a RAM policy.You try to change the hierarchical namespace status of an existing bucket. You can enable the hierarchical namespace feature only when you create a bucket. |


Thank you! We've received your  feedback.