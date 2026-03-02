# PutBucketInventory

You can call the PutBucketInventory API to configure inventory rules for a bucket.

Notes

An inventory provides information about objects in a bucket, such as their quantity, size, storage class, and encryption status. Note the following when you configure inventory rules:

Before you configure an inventory for a bucket, you must create a RAM role. The RAM role must have permissions to read all objects from the source bucket and write objects to the destination bucket. If you are using the bucket inventory feature for the first time, we recommend that you configure an inventory in the OSS console. After you configure the inventory, you can obtain a RAM role that has the permissions to perform all operations on OSS resources. For more information about the permissions required for the RAM role when you configure an inventory rule, see Bucket inventory.

A bucket supports a maximum of 1,000 inventory rules.

The source bucket for the inventory and the destination bucket for the exported inventory files must be in the same region.

To use the incremental inventory feature, contact technical support to apply. This feature is currently available only in the Mexico (Mexico City) region.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM policies or Bucket policies.

API

	

Action

	

Description




PutBucketInventory

	

oss:PutBucketInventory

	

Configures inventories for a bucket.

Request syntax
Important

The `inventoryId` parameter in the request header is required. Its value must match the `Id` request parameter.

Only the China (Qingdao), China (Hohhot), and Germany (Frankfurt) regions support the LastModifyBeginTimeStamp, LastModifyEndTimeStamp, LowerSizeBound, UpperSizeBound, and StorageClass options.

 
  PUT /?inventory&inventoryId=report1 HTTP/1.1
  Host: BucketName.oss-cn-hangzhou.aliyuncs.com
  Date: Mon, 31 Oct 2016 12:00:00 GMT
  Authorization: authorization string
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
           <Bucket>acs:oss:::destination-bucket</Bucket>
           <Prefix>prefix1</Prefix>
           <Encryption>
              <SSE-KMS>
                 <KeyId>keyId</KeyId>
              </SSE-KMS>
           </Encryption>
        </OSSBucketDestination>
     </Destination>
     <Schedule>
        <Frequency>Daily</Frequency>
     </Schedule>
     <IncludedObjectVersions>All</IncludedObjectVersions>
     <OptionalFields>
        <Field>Size</Field>
        <Field>LastModifiedDate</Field>
        <Field>TransistionTime</Field>        
        <Field>ETag</Field>
        <Field>StorageClass</Field>
        <Field>IsMultipartUploaded</Field>
        <Field>EncryptionStatus</Field>
     </OptionalFields>
     <IncrementalInventory>
      <IsEnabled>true</IsEnabled>
      <Schedule>
        <Frequency>600</Frequency>
      </Schedule>
      <OptionalFields>
        <Field>SequenceNumber</Field>
        <Field>RecordType</Field>
        <Field>RecordTimestamp</Field>
        <Field>Requester</Field>
        <Field>RequestId</Field>
        <Field>SourceIp</Field>
        <Field>Size</Field>
        <Field>StorageClass</Field>
        <Field>LastModifiedDate</Field>
        <Field>ETag</Field>
        <Field>IsMultipartUploaded</Field>
        <Field>ObjectType</Field>
        <Field>ObjectAcl</Field>
        <Field>Crc64</Field>
        <Field>EncryptionStatus</Field>
      </OptionalFields>
    </IncrementalInventory>
  </InventoryConfiguration>
Request elements

Name

	

Type

	

Required

	

Example

	

Description




Id

	

string

	

Yes

	

report1

	

The custom inventory name. It must meet the following requirements:

The inventory name must be globally unique within the current bucket.

The inventory name cannot exceed 192 characters.




IsEnabled

	

Boolean

	

Yes

	

true

	

Indicates whether the inventory feature is enabled.

Valid values:

true: Enable the inventory feature.

false: Disable the inventory feature.




Filter

	

container

	

No

	

N/A

	

The prefix for filtering objects in the inventory. After you specify a prefix, the inventory filters objects that match the prefix.




Prefix

	

string

	

No

	

Pics/

	

The prefix for filtering rules.

Parent node: Filter




LastModifyBeginTimeStamp

	

string

	

No

	

1637883649

	

The start UNIX timestamp of the last modified time for filtered files, in seconds.

Valid range: [1262275200, 253402271999]




LastModifyEndTimeStamp

	

string

	

No

	

1638347592

	

The end UNIX timestamp of the last modified time for filtered files, in seconds.

Valid range: [1262275200, 253402271999]




LowerSizeBound

	

string

	

No

	

1024

	

The minimum size of filtered files, in bytes.

Valid range: 0 B to 48.8 TB.




UpperSizeBound

	

string

	

No

	

1048576

	

The maximum size of filtered files, in bytes.

Valid range: greater than 0 B and up to 48.8 TB.




StorageClass

	

string

	

No

	

Standard,IA

	

The storage class of filtered files. You can specify multiple storage classes.

Valid values:

Standard: Standard storage

IA: Infrequent Access

Archive: Archive Storage

ColdArchive: Cold Archive

All (default): All storage classes




Destination

	

container

	

Yes

	

N/A

	

Stores the checklist results.




OSSBucketDestination

	

container

	

Yes

	

N/A

	

Information about the bucket where exported inventory results are stored.

Parent node: Destination




Format

	

string

	

Yes

	

CSV

	

The file format of the inventory file. Exported inventory files are CSV files compressed with GZIP.

Valid value: CSV

Parent node: OSSBucketDestination




AccountId

	

string

	

Yes

	

100000000000000

	

The AccountId granted by the bucket owner.

Parent node: OSSBucketDestination




RoleArn

	

string

	

Yes

	

acs:ram::100000000000000:role/AliyunOSSRole

	

The name of the role with permissions to read all files from the source bucket and write files to the destination bucket. Format: acs:ram::uid:role/rolename.

Parent node: OSSBucketDestination




Bucket

	

string

	

Yes

	

acs:oss:::bucket_0001

	

The bucket where exported inventory files are stored.

Parent node: OSSBucketDestination




Prefix

	

string

	

No

	

prefix1/

	

The prefix of the storage path for inventory files.

Parent node: OSSBucketDestination




Encryption

	

container

	

No

	

N/A

	

The encryption method for inventory files.

Valid values:

SSE-OSS: Use OSS-managed keys for encryption and decryption.

SSE-KMS: Use a default customer master key (CMK) managed by KMS or a specified CMK for encryption and decryption.

Parent node: OSSBucketDestination

For more information, see Server-side encryption.




SSE-OSS

	

container

	

No

	

N/A

	

The container for the SSE-OSS encryption method.

Parent node: Encryption




SSE-KMS

	

container

	

No

	

N/A

	

The container for the SSE-KMS encryption key.

Parent node: Encryption




KeyId

	

string

	

No

	

keyId

	

The KMS key ID.

Parent node: SSE-KMS




Schedule

	

container

	

Yes

	

N/A

	

The container for inventory export frequency information.




Frequency

	

string

	

Yes

	

Daily

	

The frequency of inventory file exports.

Valid values:

Daily: Export inventory files daily.

Weekly: Export inventory files weekly.

Parent node: Schedule




IncludedObjectVersions

	

string

	

Yes

	

All

	

Specifies whether to include object version information in the inventory.

Valid values:

All: Export all object version information.

Current: Export only the current object version information.




OptionalFields

	

container

	

No

	

N/A

	

Configure the items included in the inventory results.




Field

	

string

	

No

	

Size

	

The configuration items included in the inventory results.

Key: The object name in the bucket, URL-encoded.

VersionId: The object version ID. This field appears only when the inventory rule is configured to export all versions.

If versioning is not enabled for the bucket where inventory rules are configured, this field is empty.

If versioning is enabled for the bucket where inventory rules are configured, this field displays the object's VersionId.

IsDeleteMarker: Indicates whether the object version is a delete marker. This field appears only when the inventory rule is configured to export all versions.

If versioning is not enabled for the bucket where inventory rules are configured, this field defaults to false.

If versioning is enabled for the bucket where inventory rules are configured and the object is a delete marker, this field displays true. If the object is not a delete marker, this field displays false.

Size: The object size.

StorageClass: The object storage class.

TransitionTime: The time when the object's storage class changed to Cold Archive or Deep Cold Archive due to lifecycle rules.

LastModifiedDate: The object's last modified time.

ETag: The object's ETag value, which identifies the object's content. An ETag is created when an object is generated to identify its content.

For objects created using the PutObject API, the ETag value is the MD5 hash of its content.

For objects created by other methods, the ETag value is a unique value generated based on specific calculation rules, but it is not the MD5 hash of its content.

IsMultipartUploaded: Indicates whether the object was uploaded using multipart upload.

ObjectType: The object type.

ObjectAcl: The object's access control list (ACL).

Crc64: The object's CRC-64.

EncryptionStatus: Indicates whether the object is encrypted.

TaggingCount: The number of tags.




IncrementalInventory

	

container

	

No

	

N/A

	

The configuration container for incremental inventories.




IsEnabled

	

Boolean

	

Yes

	

true

	

Specifies whether to enable incremental inventories. Valid values:

true: Enable.

false: Disable.

If set to `true`, incremental inventories are enabled, even if `InventoryConfiguration/IsEnabled` is `false`.

Parent node: IncrementalInventory




Schedule

	

container

	

Yes

	

N/A

	

The container for incremental inventory export frequency information.

Parent node: IncrementalInventory




Frequency

	

Positive integer

	

Yes

	

600

	

The export frequency for incremental inventories, in seconds.

The system currently uses a fixed period of 600 seconds. For each period, it automatically creates a directory prefix and generates a manifest file and multiple CSV files for that period. Custom frequency settings are not supported.

Parent node: Schedule




OptionalFields

	

container

	

No

	

N/A

	

The configuration container for incremental inventory file properties.

Parent node: IncrementalInventory




Field

	

string

	

No

	

Size

	

The configuration items included in the incremental inventory.

Parent node: OptionalFields

SequenceNumber: The serial number. Each record has a unique SequenceNumber. Records under the same bucket and object can be sorted by SequenceNumber, which usually ensures a chronological order.

RecordType: The event type: CREATE, UPDATE_METADATA, DELETE.

CREATE: All upload methods that occur under the selected prefix, such as Put/Post/Append/MultipartUpload/Copy.

UPDATE_METADATA: All metadata updates under the selected prefix are recorded under this type.

DELETE: All deletion methods for files under the selected prefix, such as DeleteObject/DeleteMultipleObjects, DeleteMarker generation after enabling versioning, and lifecycle deletion. Deletions include DeleteMarker and permanent deletion. For permanent deletion records, only the core fields Bucket, Key, SequenceNumber, RecordType, RecordTimestamp, and VersionId are retained. All other columns are null.

RecordTimestamp: The timestamp (example: "2024-08-25 18:08:01.024"), in Greenwich Mean Time (GMT) with millisecond precision.

Requester: The requester's Alibaba Cloud ID or Principal ID.

RequestId: The unique ID of the request.

SourceIp: The requester's source IP address.

Key: The object name in the bucket, URL-encoded.

VersionId: The object version ID. This field appears only when the inventory rule is configured to export all versions.

If versioning is not enabled for the bucket where inventory rules are configured, this field is empty.

If versioning is enabled for the bucket where inventory rules are configured, this field displays the object's VersionId.

IsDeleteMarker: Indicates whether the object version is a delete marker. This field appears only when the inventory rule is configured to export all versions.

If versioning is not enabled for the bucket where inventory rules are configured, this field defaults to false.

If versioning is enabled for the bucket where inventory rules are configured and the object is a delete marker, this field displays true. If the object is not a delete marker, this field displays false.

Size: The object size.

StorageClass: The object storage class.

LastModifiedDate: The object's last modified time.

ETag: The object's ETag value, which identifies the object's content. An ETag is created when an object is generated to identify its content.

For objects created using the PutObject API, the ETag value is the MD5 hash of its content.

For objects created by other methods, the ETag value is a unique value generated based on specific calculation rules, but it is not the MD5 hash of its content.

IsMultipartUploaded: Indicates whether the object was uploaded using multipart upload.

ObjectType: The object type.

ObjectAcl: The object's access control list (ACL).

Crc64: The object's CRC-64.

EncryptionStatus: Indicates whether the object is encrypted.

Response Element

This operation returns only common response headers, such as Content-Length and Date. For more information, see Common response headers.

Examples
Configure inventory rules

Sample request

 
  PUT /?inventory&inventoryId=report1 HTTP/1.1
  Host: oss-example.oss-cn-hangzhou.aliyuncs.com
  Date: Mon, 31 Oct 2016 12:00:00 GMT
  Authorization: authorization string
  Content-Length: length

  <?xml version="1.0" encoding="UTF-8"?>
  <InventoryConfiguration>
     <Id>report1</Id>
     <IsEnabled>true</IsEnabled>
     <Filter>