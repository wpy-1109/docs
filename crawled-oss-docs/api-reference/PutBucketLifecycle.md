# PutBucketLifecycle

Creates a lifecycle rule based on the last modification time or last access time of files to periodically change the storage class of multiple files in a bucket to a specified value or to periodically delete expired objects and parts. This reduces storage costs. This topic describes how to call the PutBucketLifecycle operation to configure a lifecycle rule for a bucket.

Notes

The PutBucketLifecycle operation overwrites the existing configurations of a lifecycle rule that is configured for a bucket. For example, if a lifecycle rule named Rule1 is configured for a bucket and you want to configure a lifecycle rule named Rule2 for the bucket based on Rule1, perform the following operations:

Call the GetBucketLifecycle operation to query the configurations of Rule1.

Configure Rule2 for the bucket based on Rule1.

Call the PutBucketLifecycle operation to update the lifecycle rule configurations of the bucket. Rule1 and Rule2 are configured for the bucket.

You can use lifecycle rules to specify the expiration time of objects and parts that are uploaded in incomplete multipart upload tasks.

You can configure a lifecycle rule for objects based on their last access time or last modified time.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM Policy or Bucket Policy.

API

	

Action

	

Definition




PutBucketLifecycle

	

oss:PutBucketLifecycle

	

Configures lifecycle rules for a bucket.

Request syntax
 
PUT /?lifecycle HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Authorization: SignatureValue 
Host: BucketName.oss.aliyuncs.com
<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration>
  <Rule>
    <ID>RuleID</ID>
    <Prefix>Prefix</Prefix>
    <Status>Status</Status>
    <Expiration>
      <Days>Days</Days>
    </Expiration>
    <Transition>
      <Days>Days</Days>
      <StorageClass>StorageClass</StorageClass>
    </Transition>
    <AbortMultipartUpload>
      <Days>Days</Days>
    </AbortMultipartUpload>
  </Rule>
</LifecycleConfiguration>
Request headers

Header

	

Type

	

Required

	

Example

	

Description




x-oss-allow-same-action-overlap

	

String

	

No

	

true

	

Specifies whether to allow overlapped prefixes. Valid values:

true: Overlapped prefixes are allowed.

false: Overlapped prefixes are not allowed.

This request contains other common request headers, such as Date and Authorization. For more information, see the "Common request headers" section of the Common HTTP headers topic.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




LifecycleConfiguration

	

Container

	

Yes

	

N/A

	

The container that stores lifecycle configurations. The container can store the configurations of up to 1,000 lifecycle rules.

Child nodes: Rule

Parent nodes: none




Rule

	

Container

	

Yes

	

N/A

	

The container that stores lifecycle rules. The period of time from when the objects expire to when the objects are deleted must be longer than the period of time from when the objects expire to when the storage class of the objects is changed to Infrequent Access (IA) or Archive.

Child nodes: ID, Prefix, Status, and Expiration

Parent nodes: LifecycleConfiguration




ID

	

String

	

No

	

rule1

	

The ID of the lifecycle rule. The ID can be up to 255 characters in length. If you do not specify this element or if you leave this element empty, OSS automatically generates a unique ID for the lifecycle rule.

Child nodes: none

Parent nodes: Rule




Prefix

	

String

	

No

	

tmp/

	

The prefix in the names of the objects to which the rule applies. The prefixes specified by different rules cannot overlap.

If you specify the Prefix element, the rule applies only to objects whose names contain the specified prefix in the bucket.

If you do not specify the Prefix element, this rule applies to all objects in the bucket.

Child nodes: none

Parent nodes: Rule




Status

	

String

	

Yes

	

Enabled

	

Specifies whether to enable the rule. Valid values:

Enabled: enables the rule. OSS periodically executes the rule.

Disabled: does not enable the rule. OSS ignores the rule.

Parent nodes: Rule




Expiration

	

Container

	

No

	

N/A

	

The delete operation that you want OSS to perform on objects that match the lifecycle rule when the objects expire. For objects in a versioned bucket, the delete operation specified by this element is performed only on the current versions of the objects.

The period of time from when the objects expire to when the objects are deleted must be longer than the period of time from when the objects expire to when the storage class of the objects is changed to IA or Archive.

Child nodes: Days, CreatedBeforeDate, or ExpiredObjectDeleteMarker

Parent nodes: Rule




Days

	

Positive integer

	

Either Days or CreatedBeforeDate is required

	

1

	

The number of days from when the objects were last modified to when the lifecycle rule takes effect.

If the IsAccessTime element is set to true, the value of the Days element specifies that the lifecycle rule takes effect based on the specified days after the object is last accessed.

Parent nodes: Expiration or AbortMultipartUpload




CreatedBeforeDate

	

String

	

Either Days or CreatedBeforeDate is required

	

2002-10-11T00:00:00.000Z

	

The date based on which the lifecycle rule takes effect. OSS performs the specified operation on data whose last modified date is earlier than this date. The value of this element is in the yyyy-MM-ddT00:00:00.000Z format.

Specify the time in the ISO 8601 standard. The time must be 00:00:00 in UTC.

Parent nodes: Expiration or AbortMultipartUpload




ExpiredObjectDeleteMarker

	

String

	

No

	

true

	

Specifies whether to automatically remove expired delete markers. Valid values:

true: Expired delete markers are automatically removed. If you set this element to true, you cannot specify the Days or CreatedBeforeDate element.

false: Expired delete markers are not automatically removed. If you set this element to false, you must specify the Days or CreatedBeforeDate element.

Parent nodes: Expiration




Transition

	

Container

	

No

	

N/A

	

The change of the storage class of objects that match the lifecycle rule when the objects expire.

The storage class of Standard objects can be changed to IA, Archive, or Cold Archive. The period of time from when the objects expire to when the storage class of the objects is changed to Archive must be longer than the period of time from when the objects expire to when the storage class of the objects is changed to IA. For example, if the validity period is set to 30 for objects whose storage class is changed to IA after the validity period, the validity period must be set to a value greater than 30 for objects whose storage class is changed to Archive.

Parent nodes: Rule

Child nodes: Days, CreatedBeforeDate, and StorageClass

Important
Important

Either Days or CreatedBeforeDate is required.




StorageClass

	

String

	

Yes if Transition or NoncurrentVersionTransition is specified

	

IA

	

The storage class to which objects are changed. Valid values:

IA

Archive

ColdArchive

DeepColdArchive

Important

You can convert the storage class of objects in an IA bucket to only Archive or Cold Archive.

Parent nodes: Transition




AbortMultipartUpload

	

Container

	

No

	

N/A

	

The delete operation that you want OSS to perform on the parts that are uploaded in incomplete multipart upload tasks when the parts expire.

Child nodes: Days or CreatedBeforeDate

Parent nodes: Rule




Tag

	

Container

	

No

	

N/A

	

The tag of the objects to which the lifecycle rule applies. You can specify multiple tags.

Parent nodes: Rule

Child nodes: Key and Value




Key

	

String

	

Yes if the Tag element is specified

	

TagKey1

	

The key of the tag that is specified for the objects.

Parent nodes: Tag




Value

	

String

	

Yes if the Tag element is specified

	

TagValue1

	

The value of the tag that is specified for the objects.

Parent nodes: Tag




NoncurrentVersionExpiration

	

Container

	

No

	

N/A

	

The delete operation that you want OSS to perform on the previous versions of the objects that match the lifecycle rule when the previous versions expire.

Child nodes: NoncurrentDays




NoncurrentVersionTransition

	

Container

	

No

	

N/A

	

The change of the storage class of previous versions of the objects that match the lifecycle rule when the previous versions expire. The storage class of the previous versions can be changed to IA or Archive.

The period of time from when the previous versions expire to when the storage class of the previous versions is changed to Archive must be longer than the period of time from when the previous versions expire to when the storage class of the previous versions is changed to IA.

Child nodes: NoncurrentDays and StorageClass




NoncurrentDays

	

String

	

Yes if NoncurrentVersionExpiration or NoncurrentVersionTransition is specified

	

10

	

The number of days from when the objects became previous versions to when the lifecycle rule takes effect.

If the IsAccessTime element is set to true, the NoncurrentDays element takes effect based on the specified days after the objects are last accessed.

Parent nodes: NoncurrentVersionTransition and NoncurrentVersionExpiration




IsAccessTime

	

String

	

No

	

true

	

Specifies whether the lifecycle rule applies to objects based on their last access time. Valid values:

true: The rule applies to objects based on their last access time.

false (default): The rule applies to objects based on their last modification time.

Parent nodes: Transition or NoncurrentVersionTransition




ReturnToStdWhenVisit

	

String

	

No

	

false

	

Specifies whether to change the storage class of non-Standard objects back to Standard after the objects are accessed. This element takes effect only when the IsAccessTime element is set to true. Valid values:

true: changes the storage class of the objects to Standard.

false: does not change the storage class of the objects to Standard.

Parent nodes: Transition or NoncurrentVersionTransition




AllowSmallFile

	

String

	

No

	

false

	

Specifies whether to change the storage class of objects whose sizes are less than 64 KB to IA, Archive, or Cold Archive based on their last access time. Valid values:

true: changes the storage class of objects that are smaller than 64 KB to IA, Archive, or Cold Archive. The minimum billable size of objects is 64 KB. Objects that are smaller than 64 KB are charged as 64 KB. Objects whose sizes are greater than or equal to 64 KB are charged based on their actual sizes. If you set this element to true, the storage fees may increase.

false: does not change the storage class of objects that are smaller than 64 KB.

Parent nodes: Transition or NoncurrentVersionTransition




Filter

	

Container

	

No

	

N/A

	

The container that stores the Not element that is used to filter objects. You can leave this element empty or specify only a single Not node.

Parent nodes: Rule

Child nodes: Not




Not

	

Container

	

No

	

N/A

	

The condition that is matched by objects to which the lifecycle rule does not apply. If you specify a value for the Filter element, you must specify only a single Not node.

Parent nodes: Filter

Child nodes: Prefix and Tag




Prefix

	

String

	

Yes

	

tmp/not/

	

The prefix in the names of the objects to which the lifecycle rule does not apply. You cannot leave this element empty.

If you specify a value for the Prefix element on the Rule node, the value of the Prefix element that is specified on the Not node must be prefixed with the value of the Prefix element that is specified on the Rule node. For example, if the value of the Prefix element that is specified on the Rule node is dir, the value of the Prefix element that is specified on the Not node must be prefixed with dir. Examples: dir1 and dir2.

If no tag is specified on the Not node, the value of the Prefix element that is specified on the Not node must be different from the value of the Prefix element that is specified on the Rule node.

Parent nodes: Not

Child nodes: none




Tag

	

Container

	

No

	

N/A

	

The tag of the objects to which the lifecycle rule does not apply. You can specify only a single tag or leave this element empty.




ObjectSizeGreaterThan

	

Positive integer

	

No

	

500

	

The minimum object size to which this rule applies. You can specify only one value or leave this element empty. If both this parameter and the ObjectSizeLessThan parameter are set, the system will verify that the object size falls within the specified range-greater than the minimum size and less than the maximum size.

This parameter and the AllowSmallFile parameter are mutually exclusive.

Parent node: Filter

Child node: none




ObjectSizeLessThan

	

Positive integer

	

No

	

64000

	

The minimum object size to which this rule applies. You can specify only one value or leave this element empty. If both this parameter and the ObjectSizeGreaterThan parameter are set, the system will verify that the object size falls within the specified range-greater than the minimum size and less than the maximum size.

This parameter and the AllowSmallFile parameter are mutually exclusive.

Parent node: Filter

Child node: none

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples
Sample requests
Example 1: Configure a lifecycle rule based on the last modified time to only convert the storage class of objects
Example 2: Configure a lifecycle rule based on the last modified time to only delete objects
Example 3: Configure a lifecycle rule based on the last modified time to convert the storage class of objects and delete objects
Example 4: Configure a lifecycle rule based on the last modified time to delete previous versions of objects and remove delete markers
Example 5: Configure a lifecycle rule based on the last modified time to convert the storage class of objects and delete objects, excluding objects whose names contain specific prefixes or objects that have specific tags
Example 6: Configure a lifecycle rule based on the last access time to convert the storage class of objects
Example 7: Configure a lifecycle rule based on the last modified time to delete parts
Example 8: Configure a lifecycle rule based on the last modified time to delete objects whose names contain overlapping prefixes
S