# API overview

This topic outlines the Object Storage Service (OSS) APIs. It helps you understand the core concepts and resource model of OSS and quickly find the APIs that you need. For custom development, use software development kits (SDKs) in your production environment. SDKs encapsulate complex logic, such as signing, retries, and concurrency. This topic serves as a reference for the underlying implementation of SDKs and is useful for advanced customization or for understanding the communication mechanism.

Before you begin, take note of the following:

API calls must comply with the Limits.

Before you use the APIs, make sure that you understand the billing methods of OSS. For more information about pricing, see OSS Pricing.

Quick start: Call your first API

This section uses the creation of a bucket (PutBucket) as an example to describe the complete process of making an API call.

1. Preparations

Before you start, obtain the following information:

AccessKey: For security, all OSS API requests except for anonymous access requests must be signed for authentication. OSS uses a signature mechanism that is based on an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, to verify requests. The signature information must be included in the Authorization field of the HTTP request header. For more information about how to calculate a signature, see Signature V4 (recommended).

Endpoint: API requests must be sent to the endpoint of the region where the destination bucket is located. An endpoint is the access address of an OSS service. For more information about the endpoints of different regions, see Regions and endpoints.

2. Construct and send a request
 
PUT / HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 03:15:40 GMT
x-oss-acl: private
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
    <DataRedundancyType>LRS</DataRedundancyType>    
</CreateBucketConfiguration>
3. Understand the response

Successful response: If the request is successful, the server returns a 2xx status code. For operations that return content, the response body is in XML format.

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Fri, 24 Feb 2017 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
Location: /oss-example

Error handling: If the request fails, the server returns a 4xx or 5xx status code. The response body is also in XML format and contains a specific error code (Code) and an error message (Message). For more information, see Error codes to troubleshoot the issue.

API list
Service operations

API

	

Description




ListBuckets (GetService)

	

Returns all buckets that are owned by the requester.




ListUserDataRedundancyTransition

	

Lists all data redundancy transition tasks of the requester.

Region operations

API

	

Description




DescribeRegions

	

Queries the endpoints of all supported regions or a specified region.

Bucket operations

Classification

	

API

	

Description




Basic operations

	

PutBucket

	

Creates a bucket.




DeleteBucket

	

Deletes a bucket.




ListObjects (GetBucket)

	

Lists information about all objects in a bucket.




ListObjectsV2 (GetBucketV2)




GetBucketInfo

	

Queries bucket information.




GetBucketLocation

	

Queries the location of a bucket.




GetBucketStat

	

Queries the storage usage and the number of objects in a bucket.




Retention policy

	

InitiateBucketWorm

	

Creates a retention policy.




AbortBucketWorm

	

Deletes an unlocked retention policy.




CompleteBucketWorm

	

Locks a retention policy.




ExtendBucketWorm

	

Extends the retention period of objects in a bucket for which a retention policy is locked.




GetBucketWorm

	

Queries the retention policy of a bucket.




Access control

	

PutBucketAcl

	

Sets the access permissions of a bucket.




GetBucketAcl

	

Queries the access permissions of a bucket.




Lifecycle

	

PutBucketLifecycle

	

Sets lifecycle rules for objects in a bucket.




GetBucketLifecycle

	

Queries the lifecycle rules for objects in a bucket.




DeleteBucketLifecycle

	

Deletes the lifecycle rules for objects in a bucket.




Transfer acceleration

	

PutBucketTransferAcceleration

	

Configures transfer acceleration for a bucket.




GetBucketTransferAcceleration

	

Queries the transfer acceleration configuration of a bucket.




Versioning

	

PutBucketVersioning

	

Sets the versioning state of a bucket.




GetBucketVersioning

	

Queries the versioning state of a bucket.




ListObjectVersions (GetBucketVersions)

	

Lists the versions of all objects in a bucket.




Cross-region replication

	

PutBucketReplication

	

Sets data replication rules for a bucket.




PutBucketRTC

	

Enables or disables replication time control (RTC) for existing cross-region replication rules.




GetBucketReplication

	

Queries the data replication rules that are set for a bucket.




GetBucketReplicationLocation

	

Queries the destination regions to which data can be replicated.




GetBucketReplicationProgress

	

Queries the data replication progress of a bucket.




DeleteBucketReplication

	

Stops data replication tasks and deletes the replication configuration of a bucket.




Authorization policy

	

PutBucketPolicy

	

Sets a bucket policy.




GetBucketPolicy

	

Queries a bucket policy.




GetBucketPolicyStatus

	

Checks whether the current bucket policy allows public access.




DeleteBucketPolicy

	

Deletes a bucket policy.




Inventory

	

PutBucketInventory

	

Sets an inventory rule for a bucket.




GetBucketInventory

	

Queries a specified inventory task in a bucket.




ListBucketInventory

	

Queries all inventory tasks in a bucket.




DeleteBucketInventory

	

Deletes a specified inventory task from a bucket.




Log Management

	

PutBucketLogging

	

Enables the access log recording feature for a bucket.




GetBucketLogging

	

Queries the access log configuration of a bucket.




DeleteBucketLogging

	

Disables the access log recording feature for a bucket.




PutUserDefinedLogFieldsConfig

	

Configures the user_defined_log_fields field in the real-time logs of a bucket.




GetUserDefinedLogFieldsConfig

	

Queries the configuration of the user_defined_log_fields field in the real-time logs of a bucket.




DeleteUserDefinedLogFieldsConfig

	

Deletes the configuration of the user_defined_log_fields field in the real-time logs of a bucket.




Static website

	

PutBucketWebsite

	

Sets a bucket to the static website hosting mode.




GetBucketWebsite

	

Queries the static website hosting status of a bucket.




DeleteBucketWebsite

	

Disables the static website hosting mode for a bucket.




Hotlink protection

	

PutBucketReferer

	

Sets a hotlink protection rule for a bucket.




GetBucketReferer

	

Queries the hotlink protection rule of a bucket.




Tags

	

PutBucketTags

	

Adds or modifies bucket tags.




GetBucketTags

	

Queries bucket tags.




DeleteBucketTags

	

Deletes bucket tags.




Encryption

	

PutBucketEncryption

	

Configures encryption rules for a bucket.




GetBucketEncryption

	

Queries the encryption rules of a bucket.




DeleteBucketEncryption

	

Deletes the encryption rules of a bucket.




Pay by requester

	

PutBucketRequestPayment

	

Sets a bucket to the pay-by-requester mode.




GetBucketRequestPayment

	

Queries the pay-by-requester configuration of a bucket.




Cross-origin resource sharing

	

PutBucketCors

	

Sets cross-origin resource sharing (CORS) rules for a specified bucket.




GetBucketCors

	

Queries the current CORS rules of a specified bucket.




DeleteBucketCors

	

Disables the CORS feature and clears all CORS rules for a specified bucket.




Options

	

Before a browser sends a cross-origin request, it sends a preflight request (OPTIONS) that carries information such as the source origin, HTTP method, and headers to OSS to determine whether to send the actual request.




Access tracking

	

PutBucketAccessMonitor

	

Configures the access tracking state of a bucket.




GetBucketAccessMonitor

	

Queries the access tracking state of a bucket.




Data Indexing

	

OpenMetaQuery

	

Enables the metadata management feature for a bucket.




GetMetaQueryStatus

	

Queries the metadata index library of a specified bucket.




DoMetaQuery

	

Queries objects that meet specified conditions and lists object information based on specified fields and sorting methods.




CloseMetaQuery

	

Disables the metadata management feature for a bucket.




DDoS Protection

	

InitUserAntiDDosInfo

	

Creates an Anti-DDoS for OSS instance.




UpdateUserAntiDDosInfo

	

Changes the status of an Anti-DDoS for OSS instance.




GetUserAntiDDosInfo

	

Queries information about the Anti-DDoS for OSS instances that belong to a specified account.




InitBucketAntiDDosInfo

	

Initializes protection for a bucket.




UpdateBucketAntiDDosInfo

	

Updates the protection status of a bucket.




ListBucketAntiDDosInfo

	

Queries the list of protection information for a bucket.




Resource group

	

PutBucketResourceGroup

	

Configures a resource group for a bucket.




GetBucketResourceGroup

	

Queries the ID of the resource group to which a bucket belongs.




Custom domain name

	

CreateCnameToken

	

Creates a CNAME token that is required to verify the ownership of a domain name.




GetCnameToken

	

Queries a created CNAME token.




PutCname

	

Binds a CNAME record to a bucket.




ListCname

	

Queries the list of all CNAME records that are bound to a bucket.




DeleteCname

	

Deletes a bound CNAME record.




Image style

	

PutStyle

	

Adds an image style.




GetStyle

	

Queries information about a specified image style in a bucket.




ListStyle

	

Queries all image styles that are created in a bucket.




DeleteStyle

	

Deletes a specified image style from a bucket.




Transport-layer security

	

PutBucketHttpsConfig

	

Enables or disables TLS version settings for a bucket.




GetBucketHttpsConfig

	

Queries the TLS version settings of a bucket.




Redundancy transition

	

CreateBucketDataRedundancyTransition

	

Creates a data redundancy transition task.




GetBucketDataRedundancyTransition

	

Queries a data redundancy transition task.




DeleteBucketDataRedundancyTransition

	

Deletes a data redundancy transition task.




ListUserDataRedundancyTransition

	

Lists all data redundancy transition tasks of the requester.




ListBucketDataRedundancyTransition

	

Lists all data redundancy transition tasks in a bucket.




Access point

	

CreateAccessPoint

	

Creates an access point.




GetAccessPoint

	

Queries the information about an access point.




DeleteAccessPoint

	

Deletes an access point.




ListAccessPoints

	

Queries the information about user-level or bucket-level access points.




PutAccessPointPolicy

	

Configures an access point policy.




GetAccessPointPolicy

	

Queries the configuration of an access point policy.




DeleteAccessPointPolicy

	

Deletes an access point policy.




Object FC access point

	

CreateAccessPointForObjectProcess

	

Creates an Object FC access point.




GetAccessPointForObjectProcess

	

Queries basic information about an Object FC access point.




DeleteAccessPointForObjectProcess

	

Deletes an Object FC access point.




ListAccessPointsForObjectProcess

	

Queries information about user-level Object FC access points.




PutAccessPointConfigForObjectProcess

	

Modifies the configuration of an Object FC access point.




GetAccessPointConfigForObjectProcess

	

Queries the configuration of an Object FC access point.




PutAccessPointPolicyForObjectProcess

	

Configures an access policy for an Object FC access point.




GetAccessPointPolicyForObjectProcess

	

Queries the access policy configuration of an Object FC access point.




DeleteAccessPointPolicyForObjectProcess

	

Deletes the access policy of an Object FC access point.




WriteGetObjectResponse

	

Customizes returned data and response headers.




Block Public Access

	

PutPublicAccessBlock

	

Globally enables Block Public Access for OSS.




GetPublicAccessBlock

	

Queries the global Block Public Access configuration for OSS.




DeletePublicAccessBlock

	

Deletes the global Block Public Access configuration for OSS.




PutBucketPublicAccessBlock

	

Enables Block Public Access for a bucket.




GetBucketPublicAccessBlock

	

Queries the Block Public Access configuration of a specified bucket.




DeleteBucketPublicAccessBlock

	

Deletes the Block Public Access configuration of a specified bucket.




PutAccessPointPublicAccessBlock

	

Enables Block Public Access for an access point.




GetAccessPointPublicAccessBlock

	

Queries the Block Public Access configuration of a specified access point.




DeleteAccessPointPublicAccessBlock

	

Deletes the Block Public Access configuration of a specified access point.




Real-time access of Archive objects

	

PutBucketArchiveDirectRead

	

Enables or disables real-time access of Archive objects.




GetBucketArchiveDirectRead

	

Queries whether real-time access of Archive objects is enabled.




OSS accelerator

	

PutBucketDataAccelerator

	

Creates an OSS accelerator or modifies its configuration.




GetBucketDataAccelerator

	

Queries the information about an OSS accelerator.




DeleteBucketDataAccelerator

	

Deletes an OSS accelerator.

Object operations

Classification

	

API

	

Description




Basic operations

	

PutObject

	

Uploads an object.




GetObject

	

Queries an object.




CopyObject

	

Copies an object.




AppendObject

	

Uploads an object using append upload.




SealAppendObject

	

Prevents data from being appended to an Appendable object.




DeleteObject

	

Deletes a single object.




DeleteMultipleObjects

	

Deletes multiple objects.




HeadObject

	

Returns only the metadata of an object, not the content of the object.




GetObjectMeta

	

Returns the basic metadata of an object, such as the ETag, size, and last modified time of the object, but does not return the content of the object.




PostObject

	

Uploads an object using an HTML form.




Callback

	

You can implement a callback by including the callback parameters in a request that you send to OSS.




RestoreObject

	

Restores an Archive Storage, Cold Archive, or Deep Cold Archive object.




CleanRestoredObject

	

Ends the restored state of an object in advance.




SelectObject

	

Executes an SQL statement on an object file and returns the execution resul