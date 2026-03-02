# Use the PutBucketReplication operation to specify a data replication rule for a bucket

Use the PutBucketReplication operation to specify a data replication rule for a bucket. OSS supports cross-region replication (CRR) and same-region replication (SRR).

## Usage notes


Data replication asynchronously copies objects from a source bucket to a destination bucket. This includes operations such as creating, updating, and deleting objects. Note the following when you use data replication:


-

Data replication is asynchronous. The time required to replicate data to the destination bucket depends on the size of the data and can range from several minutes to several hours.

-

The source bucket and the destination bucket cannot have the same name.

-

When you use cross-region replication, the source bucket and the destination bucket must be in different data centers. When you use same-region replication, the source bucket and the destination bucket must be in the same data center.


For more information about data replication, see [Introduction to cross-region replication](https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication-overview/#concept-zjp-31z-5db) and [Introduction to same-region replication](https://www.alibabacloud.com/help/en/oss/user-guide/srr/#concept-2067125).

## Request syntax


`javascript
POST /?replication&comp=add HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Authorization: SignatureValue
Host: BucketName.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<ReplicationConfiguration>
   <Rule>
        <RTC>
            <Status>enabled or disabled</Status>
        </RTC>
        <PrefixSet>
            <Prefix>prefix_1</Prefix>
            <Prefix>prefix_2</Prefix>
        </PrefixSet>
        <Action>ALL or PUT</Action>
        <Destination>
            <Bucket>destbucket</Bucket>
            <Location>oss-cn-hangzhou</Location>
            <TransferType>oss_acc</TransferType>
        </Destination>
        <HistoricalObjectReplication>enabled or disabled</HistoricalObjectReplication>
        <SyncRole>aliyunramrole</SyncRole>
   </Rule>
</ReplicationConfiguration>
`


## Request elements


-


-


-


> IMPORTANT:

> NOTE: 


> NOTE: 


-


> IMPORTANT:

> NOTE: 


> NOTE: 


-


-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/introduction-to-data-replication-permissions)


-


-


-


-


> NOTE:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/user-guide/rtc#section-52f-hyg-geu)


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| ReplicationConfiguration | Container | Yes | N/A | The container for the data replication rules of a bucket.Parent node: NoneChild node: Rule |
| Rule | Container | Yes | N/A | The container for a data replication rule.Parent node: ReplicationConfigurationChild nodes: Destination, HistoricalObjectReplication, ID, and more |
| ID | String | No | first | The unique ID of the data replication rule.Parent node: RuleChild nodes: None |
| PrefixSet | Container | No | N/A | The container for prefixes. You can specify a maximum of 10 prefixes in each data replication rule.Parent node: RuleChild node: Prefix |
| Prefix | String | No | source1 | The prefix of the objects to replicate. Only objects that match the prefix are replicated to the destination bucket.The prefix can be up to 1,023 characters in length.If you configure a prefix, both newly written data and historical data are replicated based on the prefix.Parent node: PrefixSetChild nodes: None |
| Action | String | No | ALL | The operations to replicate to the destination bucket. If you configure an action, both newly written data and historical data are replicated based on the specified action.You can specify one or more of the following valid values.Valid values:ALL (default): Replicates PUT, DELETE, and ABORT operations to the destination bucket.Important Besides replication of newly uploaded and updated objects, this replication policy includes replication of deletion, which ensures the consistency of data. This policy is applicable to scenarios in which multiple users or applications need to share and access the same dataset. Objects deleted from the source bucket, either manually or through lifecycle policies, will also be deleted from the destination bucket. Objects cannot be recovered after they are deleted.PUT: Replicates write operations to the destination bucket. These operations include PutObject, PostObject, AppendObject, CopyObject, PutObjectACL, InitiateMultipartUpload, UploadPart, UploadPartCopy, and CompleteMultipartUpload.Important If this replication policy is applied, only objects that are uploaded or updated after the policy takes effect will be replicated to the destination bucket, and objects deleted from the source bucket will not be deleted from the destination bucket. This policy effectively prevents data loss in the destination bucket resulting from manual deletion or automated deletion triggered by lifecycle policies in the source bucket.Parent node: RuleChild nodes: None |
| Destination | Container | Yes | N/A | The container for information about the destination bucket.Parent node: RuleChild nodes: Bucket and Location |
| Bucket | String | Yes | destbucket | The destination bucket for data replication.Parent node: DestinationChild nodes: None |
| Location | String | Yes | oss-cn-hangzhou | The region where the destination bucket is located.Parent node: DestinationChild nodes: None |
| TransferType | String | Yes | oss_acc | The data transmission link used for data replication.Valid values:internal (default): The default OSS transmission link.oss_acc: The transfer acceleration link. You can use the transfer acceleration link only when you create a cross-region replication rule.Parent node: DestinationChild nodes: None |
| HistoricalObjectReplication | String | No | disabled | Specifies whether to replicate historical data. This determines if data in the source bucket before data replication is enabled is replicated to the destination bucket.Valid values:enabled (default): Replicates historical data.disabled: Does not replicate historical data. Only data written after the data replication rule is created is replicated.Parent node: RuleChild nodes: None |
| SyncRole | String | Yes | aliyunramrole | The RAM role that you authorize OSS to use for data replication. Data replication can be performed within the same account or across different accounts. For both scenarios, you must grant the RAM role the required replication permissions. Otherwise, the replication task cannot be completed. For more information, see Data replication permissions.Parent node: RuleChild nodes: None |
| SourceSelectionCriteria | Container | No | N/A | The container for other filter conditions that identify the source objects to replicate. OSS currently supports specifying filter conditions only for source objects encrypted with SSE-KMS.Parent node: RuleChild node: SseKmsEncryptedObjects |
| SseKmsEncryptedObjects | Container | No | N/A | The container for filtering objects encrypted with SSE-KMS. If you specify SourceSelectionCriteria in the data replication rule, you must specify this element.Parent node: SourceSelectionCriteriaChild node: Status |
| Status | String | No | Enabled | Specifies whether OSS replicates objects created with SSE-KMS encryption. Valid values:Enabled: Replicates objects created with SSE-KMS encryption.Disabled (default): Does not replicate objects created with SSE-KMS encryption.Parent node: SseKmsEncryptedObjectsChild nodes: None |
| EncryptionConfiguration | Container | No | N/A | The encryption configuration for destination objects. If you set Status to Enabled, you must specify this element.Parent node: RuleChild node: ReplicaKmsKeyID |
| ReplicaKmsKeyID | String | No | c4d49f85-ee30-426b-a5ed-95e9139d | The ID of the SSE-KMS key. If you set Status to Enabled, you must specify this element.Parent node: EncryptionConfigurationChild nodes: None |
| RTC | Container | No | N/A | The status of the replication time control (RTC) feature.Parent node: RuleChild node: Status |
| Status | String | No | Enabled | Enables or disables the RTC feature. You can configure the RTC feature only for cross-region replication.Valid values:enabled: Enables the RTC feature.disabled (default): Disables the RTC feature.Parent node: RTCChild nodes: NoneNote For more information about the regions that support the RTC feature, see Regions that support RTC. |


This operation also requires common request headers such as Host and Date. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#reference-mhp-zdy-wdb/section-eq1-b2y-wdb).

## Response headers


This operation returns only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#reference-mhp-zdy-wdb/section-hcd-m2y-wdb).

## Examples


-

Request example


`javascript
POST /?replication&comp=add HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Type: application/xml
Content-Length: 186
Date: Thu, 17 Apr 2025 15:39:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<ReplicationConfiguration>
  <Rule>
     <RTC>
        <Status>enabled</Status>
     </RTC>
     <PrefixSet>
        <Prefix>source1</Prefix>
        <Prefix>video</Prefix>
     </PrefixSet>
     <Action>PUT</Action>
     <Destination>
        <Bucket>destbucket</Bucket>
        <Location>oss-cn-beijing</Location>
        <TransferType>oss_acc</TransferType>
     </Destination>
     <HistoricalObjectReplication>enabled</HistoricalObjectReplication>
      <SyncRole>aliyunramrole</SyncRole>
      <SourceSelectionCriteria>
         <SseKmsEncryptedObjects>
           <Status>Enabled</Status>
         </SseKmsEncryptedObjects>
      </SourceSelectionCriteria>
      <EncryptionConfiguration>
           <ReplicaKmsKeyID>c4d49f85-ee30-426b-a5ed-95e9139d</ReplicaKmsKeyID>
      </EncryptionConfiguration>
  </Rule>
</ReplicationConfiguration>
`


-

Response example


`javascript
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Thu, 24 Sep 2025 15:39:12 GMT
Content-Length: 0
Connection: close
Server: AliyunOSS
`


## SDK


The SDKs for this operation in different languages are as follows:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/data-replication-1)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/data-replication-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-data-replication)

## ossutil command-line tool


For the ossutil command that corresponds to this operation, see [put-bucket-replication](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-replication).

## Error codes


-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)


(https://smartservice.console.alibabacloud.com/?spm=5176.2020520001.nav-right.ditem-sub.433c12d26HHFbc#/ticket/createIndex)


(https://smartservice.console.alibabacloud.com/?spm=5176.2020520001.nav-right.ditem-sub.433c12d26HHFbc#/ticket/createIndex)


(https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication-overview/#section-4f4-9mu-9t8)


| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidTargetBucket | 400 BadRequest | This error can occur for the following reasons:The name of the destination bucket is the same as the name of the source bucket.The destination bucket does not exist.The destination bucket and the source bucket do not belong to the same user. |
| InvalidTargetLocation | 400 BadRequest | The location of the destination bucket is different from the location specified in the request XML. |
| BucketReplicationAlreadyExist | 400 BadRequest | A replication relationship already exists from the source bucket to the destination bucket.To configure a new data replication rule, delete the existing rule first. |
| BadReplicationLocation | 400 BadRequest | The specified destination data center is invalid.You can call the GetBucketReplicationLocation operation to obtain valid destination data centers. |
| NoReplicationLocation | 400 BadRequest | When you use cross-region replication, the data center of the source bucket does not have a paired data center for cross-region replication.For more information about paired data centers for cross-region replication, see Endpoints and data centers. |
| TooManyReplicationRules | 400 BadRequest | More than one data replication rule is configured in the request.You can configure only one data replication rule in a single request. |
| TooManyIncomingReplication | 400 BadRequest | The number of data replication rules configured for the bucket has reached the limit of 100. Delete the data replication rules that are no longer used and try again.You can configure up to 100 data replication rules for a bucket. If your business requirements exceed this limit, please submit a ticket to contact us. |
| TooManyOutgoingReplication | 400 BadRequest | The number of data replication rules configured for the bucket has reached the limit of 100. Delete the data replication rules that are no longer used and try again.You can configure up to 100 data replication rules for a bucket. If your business requirements exceed this limit, please submit a ticket to contact us. |
| MissingArgument | 400 BadRequest | The data transmission link is not specified. |
| InvalidArgument | 400 BadRequest | The specified data transmission link is not supported. |
| ReplicationLocationNotSupportRtc | 400 BadRequest | The RTC feature cannot be enabled in this region. For more information about the regions that support the RTC feature, see RTC regions. |


Thank you! We've received your  feedback.