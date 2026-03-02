# Call GetBucketInventory to view a specified inventory task in a bucket

GetBucketInventory retrieves the configuration of a specified inventory task for a bucket.

## Usage notes


By default, an Alibaba Cloud account has permission to retrieve inventory task configurations for a bucket. If you use a RAM user or Security Token Service (STS) to retrieve inventory task configurations, you must have the `oss:GetBucketInventory` permission.

## Request syntax


`plaintext
GET /?inventory&inventoryId=inventoryId HTTP/1.1
`


## Request parameters














| Name | Type | Required | Description |
| --- | --- | --- | --- |
| inventoryId | String | Yes | The ID of the inventory task to query. |


## Response parameters











-


-


-


-


-


-


-


-


-


-


-



-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-

(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb)

-


-


-


-


-


-


| Name | Type | Description |
| --- | --- | --- |
| Id | String | The inventory name that you specify. The name must be globally unique in the bucket. |
| IsEnabled | Boolean | Indicates whether the inventory feature is enabled.Valid values: true and falseIf set to true, the inventory feature is enabled.If set to false, no inventory list is generated. |
| Filter | Container | The prefix used to filter objects. Only objects whose names contain the specified prefix are included in the inventory list. |
| Prefix | String | The prefix used in the filter rule.Parent node: Filter |
| Destination | Container | Details of the checklist results. |
| OSSBucketDestination | Container | Information about the bucket that stores exported inventory lists.Parent node: Destination |
| Format | String | The format of exported inventory lists.Valid value: CSVParent node: OSSBucketDestination |
| AccountId | String | The account ID granted by the bucket owner.Parent node: OSSBucketDestination |
| RoleArn | String | The role name to which the bucket owner grants permissions.Format: acs:ram::uid:role/rolenameParent node: OSSBucketDestination |
| Bucket | String | The bucket that stores exported inventory lists.Parent node: OSSBucketDestination |
| Prefix | String | The prefix in the path where exported inventory lists are stored.Parent node: OSSBucketDestination |
| Encryption | Container | The encryption method used for exported inventory lists.Valid values: SSE-OSS, SSE-KMS, and nullParent node: OSSBucketDestination |
| SSE-OSS | Container | The container for the SSE-OSS encryption method.Parent node: Encryption |
| SSE-KMS | Container | The container that stores the customer master key (CMK) used in the SSE-KMS encryption method.Parent node: Encryption |
| KeyId | String | The ID of the key managed by Key Management Service (KMS).Parent node: SSE-KMS |
| Schedule | Container | The container that stores information about how often inventory lists are exported. |
| Frequency | String | How often inventory lists are exported.Valid values: Daily and WeeklyParent node: Schedule |
| IncludedObjectVersions | String | Indicates whether to include version information for objects in inventory lists.Valid values: All and CurrentIf set to All, all versions of objects are exported.If set to Current, only the current versions of objects are exported. |
| OptionalFields | Container | The configuration fields to include in inventory lists. |
| Field | String | The configuration fields to include in inventory lists.Valid values: Size, LastModifiedDate, TransitionTime, ETag, StorageClass, IsMultipartUploaded, EncryptionStatus, ObjectAcl, TaggingCount, ObjectType, and CRC64Parent node: OptionalFields |
| IncrementalInventory | Container | Configuration information for incremental inventories. |
| IsEnabled | Boolean | Indicates whether to enable incremental inventories.Valid values:true: Enablefalse: DisableIf set to true, the incremental inventory feature is enabled regardless of whether the top-level IsEnabled parameter is set to false.Parent node: IncrementalInventory |
| Schedule | Container | The export frequency for incremental inventories.Parent node: IncrementalInventory |
| Frequency | Positive integer | The export frequency for incremental inventories, in seconds.The system uses a fixed interval of 600 seconds. For each interval, the system automatically creates a directory prefix and generates a manifest file and multiple CSV files for objects created during that interval. Custom frequencies are not supported.Parent node: Schedule |
| OptionalFields | Container | The configuration fields to include in incremental inventories.Parent node: IncrementalInventory |
| Field | String | The configuration fields to include in incremental inventories.Parent node: OptionalFieldsSequenceNumber: The sequence number. Each record has a unique SequenceNumber. Records for the same bucket and object can be sorted by SequenceNumber, which usually follows chronological order.RecordType: The event type: CREATE, UPDATE_METADATA, or DELETE.CREATE: All upload operations under the selected prefix, such as PutObject, PostObject, AppendObject, MultipartUpload, and CopyObject.UPDATE_METADATA: All metadata updates under the selected prefix.DELETE: All deletion operations under the selected prefix, such as DeleteObject and DeleteMultipleObjects. When versioning is enabled, this includes delete markers. Lifecycle-based deletions are also included. Permanent deletions record only these core fields: Bucket, Key, SequenceNumber, RecordType, RecordTimestamp, and VersionId. All other columns are null.RecordTimestamp: A timestamp in ISO 8601 format, such as "2024-08-25 18:08:01.024". Uses Greenwich Mean Time (GMT) with millisecond precision.Requester: The Alibaba Cloud ID or principal ID of the requester.RequestId: The unique ID of the request.SourceIp: The source IP address of the requester.Key: The name of the object in the bucket, URL-encoded.VersionId: The version ID of the object. This field appears only when the inventory rule is configured to export all versions.If versioning is disabled for the bucket, this field is empty.If versioning is enabled for the bucket, this field shows the object's VersionId.IsDeleteMarker: Indicates whether the object version is a delete marker. This field appears only when the inventory rule is configured to export all versions.If versioning is disabled for the bucket, this field defaults to false.If versioning is enabled for the bucket and the object is a delete marker, this field shows true. If the object is not a delete marker, this field shows false.Size: The size of the object.StorageClass: The storage class of the object.LastModifiedDate: The last modified time of the object.ETag: The ETag value of the object, used to identify its content. An ETag is generated when the object is created.For objects created using the PutObject operation, the ETag is the MD5 hash of the object's content.For objects created using other methods, the ETag is a unique value generated by a specific algorithm, but it is not the MD5 hash of the content.IsMultipartUploaded: Indicates whether the object was uploaded using multipart upload.ObjectType: The type of the object.ObjectAcl: The access control list (ACL) of the object.CRC64: The CRC-64 checksum of the object.EncryptionStatus: Indicates whether the object is encrypted. |


## Examples


-

Sample request


`plaintext
GET /?inventory&inventoryId=list1 HTTP/1.1
`


-

Sample response


`plaintext
  HTTP/1.1 200 OK
  x-oss-request-id: 56594298207FB304438516F9
  Date: Mon, 31 Oct 2016 12:00:00 GMT
  Server: AliyunOSS
  Content-Length: length

  <?xml version="1.0" encoding="UTF-8"?>
  <InventoryConfiguration>
     <Id>report1</Id>
     <IsEnabled>true</IsEnabled>
     <Destination>
        <OSSBucketDestination>
           <Format>CSV</Format>
           <AccountId>1000000000000000</AccountId>
           <RoleArn>acs:ram::1000000000000000:role/AliyunOSSRole</RoleArn>
           <Bucket>acs:oss:::bucket_0001</Bucket>
           <Prefix>prefix1</Prefix>
           <Encryption>
              <SSE-OSS/>
           </Encryption>
        </OSSBucketDestination>
     </Destination>
     <Schedule>
        <Frequency>Daily</Frequency>
     </Schedule>
     <Filter>
       <Prefix>myprefix/</Prefix>
     </Filter>
     <IncludedObjectVersions>All</IncludedObjectVersions>
     <OptionalFields>
        <Field>Size</Field>
        <Field>LastModifiedDate</Field>
        <Field>ETag</Field>
        <Field>StorageClass</Field>
        <Field>IsMultipartUploaded</Field>
        <Field>EncryptionStatus</Field>
     </OptionalFields>
  </InventoryConfiguration>
`


## SDK


The SDKs for this API are available in the following programming languages:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-inventory-5)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-inventory-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-bucket-inventory)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-inventory-1)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-inventory-4#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-inventory-2)

## ossutil


For information about the ossutil command that corresponds to the GetBucketInventory operation, see [get-bucket-inventory](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-inventory).


Thank you! We've received your  feedback.