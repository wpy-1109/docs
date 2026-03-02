# List of supported API operations

This topic describes the API operations supported when the hierarchical namespace feature is disabled or enabled for a bucket.

Note

In the following table, a check sign (√) indicates that the feature is supported. A cross sign (×) indicates that the feature is not supported.

Service operations

API

	

Hierarchical namespace disabled

	

Hierarchical namespace enabled




GetService (ListBuckets)

	

√

	

√

Bucket operations

API

	

Hierarchical namespace disabled

	

Hierarchical namespace enabled




Basic operation

	

PutBucket

	

√

	

√




DeleteBucket

	

√

	

√




GetBucket (ListObjects)

	

√

	

√




GetBucketV2 (ListObjectsV2)

	

√

	

√




GetBucketInfo

	

√

	

√




GetBucketLocation

	

√

	

√




Retention policy

	

InitiateBucketWorm

	

√

	

×




AbortBucketWorm

	

√

	

×




CompleteBucketWorm

	

√

	

×




ExtendBucketWorm

	

√

	

×




GetBucketWorm

	

√

	

×




Access control list (ACL)

	

PutBucketAcl

	

√

	

√




GetBucketAcl

	

√

	

√




Lifecycle

	

PutBucketLifecycle

	

√

	

×




GetBucketLifecycle

	

√

	

×




DeleteBucketLifecycle

	

√

	

×




Versioning

	

PutBucketVersioning

	

√

	

×




GetBucketVersioning

	

√

	

×




GetBucketVersions(ListObjectVersions)

	

√

	

×




Cross-region replication (CRR)

	

PutBucketReplication

	

√

	

×




GetBucketReplication

	

√

	

×




GetBucketReplicationLocation

	

√

	

×




GetBucketReplicationProgress

	

√

	

×




DeleteBucketReplication

	

√

	

×




Bucket policy

	

PutBucketPolicy

	

√

	

√




GetBucketPolicy

	

√

	

√




DeleteBucketPolicy

	

√

	

√




Inventory

	

PutBucketInventory

	

√

	

×




GetBucketInventory

	

√

	

×




ListBucketInventory

	

√

	

×




DeleteBucketInventory

	

√

	

×




Logging

	

PutBucketLogging

	

√

	

√




GetBucketLogging

	

√

	

√




DeleteBucketLogging

	

√

	

√




Static website hosting

	

PutBucketWebsite

	

√

	

×




GetBucketWebsite

	

√

	

×




DeleteBucketWebsite

	

√

	

×




Hotlink protection

	

PutBucketReferer

	

√

	

√




GetBucketReferer

	

√

	

√




Tagging

	

PutBucketTags

	

√

	

√




GetObjectTagging

	

√

	

√




DeleteBucketTags

	

√

	

√




Encryption

	

PutBucketEncryption

	

√

	

√




GetBucketEncryption

	

√

	

√




DeleteBucketEncryption

	

√

	

√




Pay-by-requester

	

PutBucketRequestPayment

	

√

	

√




GetBucketRequestPayment

	

√

	

√




Cross-origin resource sharing (CORS)

	

PutBucketCors

	

√

	

×




GetBucketCors

	

√

	

×




DeleteBucketCors

	

√

	

×




OptionObject

	

√

	

×

Object operations

API

	

Hierarchical namespace disabled

	

Hierarchical namespace enabled




Basic operation

	

PutObject

	

√

	

√




GetObject

	

√

	

√




CopyObject

	

√

	

√




AppendObject

	

√

	

×




DeleteObject

	

√

	

√




DeleteMultipleObjects

	

√

	

×




HeadObject

	

√

	

√




GetObjectMeta

	

√

	

√




PostObject

	

√

	

√




Callback

	

√

	

×




RestoreObject

	

√

	

×




SelectObject

	

√

	

×




Directory management

	

CreateDirectory

	

×

	

√




Rename

	

×

	

√




DeleteDirectory

	

×

	

√




Multipart upload

	

InitiateMultipartUpload

	

√

	

√




UploadPart

	

√

	

√




UploadPartCopy

	

√

	

√




CompleteMultipartUpload

	

√

	

√




AbortMultipartUpload

	

√

	

√




ListMultipartUploads

	

√

	

√




ListParts

	

√

	

√




ACL

	

PutObjectACL

	

√

	

√




GetObjectACL

	

√

	

√




Symbolic link

	

PutSymlink

	

√

	

×




GetSymlink

	

√

	

×




Tagging

	

PutObjectTagging

	

√

	

√




GetObjectTagging

	

√

	

√




DeleteObjectTagging

	

√

	

√

LiveChannel operations

API

	

Hierarchical namespace disabled

	

Hierarchical namespace enabled




PutLiveChannel

	

√

	

×




ListLiveChannel

	

√

	

×




DeleteLiveChannel

	

√

	

×




PutLiveChannelStatus

	

√

	

×




GetLiveChannelInfo

	

√

	

×




GetLiveChannelStat

	

√

	

×




GetLiveChannelHistory

	

√

	

×




PostVodPlaylist

	

√

	

×




GetVodPlaylist

	

√

	

×

For more information about the hierarchical namespace feature, see Hierarchical namespace.