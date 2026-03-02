# Object-level operations

You can use the CopyObject operation to copy an object between the same or different buckets in the same region.

Versioning

By default, x-oss-copy-source copies the current version of an object. To copy a specific version, include the version ID in x-oss-copy-source. If the specified source version is a delete marker, OSS returns a 404 error, which indicates that the object does not exist.

You can restore an earlier version of an object as the current version by copying the earlier version to the same bucket. OSS then sets that earlier version as the current version.

If versioning is enabled for the destination bucket, OSS automatically generates a unique version ID for the newly copied object. This version ID is returned in the x-oss-version-id response header. If versioning is disabled or suspended for the destination bucket, OSS generates a version with a null version ID for the new object. This new version overwrites any existing version that has a null version ID.

Limits

Object size limits

If the source and destination buckets are the same, and you do not change the encryption method or storage class of the object during the copy operation, the object can be larger than 5 GB.

If the source and destination buckets are different, and you do not change the encryption method or storage class of the object during the copy operation, the object cannot be larger than 5 GB.

If you change the encryption method or storage class of the object during the copy operation, the object cannot be larger than 1 GB. If the object is larger than 1 GB, you must use the UploadPartCopy operation.

Permissions

Both the CopyObject and UploadPartCopy operations require read permissions on the source object.

If you use the CopyObject operation in a bucket where versioning is disabled and the source and destination objects are the same:

If the encryption method or storage class is not changed, OSS modifies only the metadata of the object and does not copy its content.

If the encryption method or storage class is changed, OSS modifies the metadata and also copies the content of the object.

Source object is a symbolic link

If you use the CopyObject operation on a symbolic link, only the symbolic link is copied. The content of the file to which the symbolic link points is not copied.

Hierarchical namespace is enabled for the bucket

If hierarchical namespace is enabled for the bucket, you cannot copy directories.

Preventing file overwrite conflicts

If you enable Prevent File Overwrite, you cannot use CopyObject to change a file's storage class, such as from Standard to Archive Storage. Instead, use automatic lifecycle conversion.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM policies or Bucket Policy.

API

	

Action

	

Definition




CopyObject

	

oss:GetObject

	

Copies objects within a bucket or between buckets in the same region.




oss:PutObject




oss:GetObjectVersion

	

If you specify the source object version through versionId, this permission is also required.




oss:GetObjectTagging

	

If you copy object tags through x-oss-tagging, these permissions are required.




oss:PutObjectTagging




oss:GetObjectVersionTagging

	

If you specify the tags of a specific version of the source object through versionId, this permission is also required.




kms:GenerateDataKey

	

When copying an object, if the destination object metadata contains X-Oss-Server-Side-Encryption: KMS, these two permissions are required.




kms:Decrypt

Billing

Each call to the CopyObject operation counts as one PUT request for the destination bucket.

The CopyObject operation increases the storage usage of the destination bucket.

Changing the storage class of an object using the CopyObject operation involves data overwrites. For example, if an Infrequent Access (IA) object is overwritten and its storage class is changed to Standard within 10 days of its creation, a fee is charged for 20 days of IA storage because the minimum storage duration was not met. For more information about storage fees, see Storage fees.

When you call the CopyObject operation, if the source object is an IA object, a data retrieval fee for IA storage is incurred. If the source object is an Archive Storage object that has not been restored using RestoreObject and real-time access of Archive objects is enabled for the bucket, a data retrieval fee for real-time access is incurred. These fees are charged to the account that owns the source bucket. For more information about billing, see Data processing fees.

Request syntax
 
PUT /DestObjectName HTTP/1.1
Host: DestBucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
x-oss-copy-source: /SourceBucketName/SourceObjectName
Request headers

All request headers for a copy operation start with x-oss-. Therefore, you must add all these request headers to the signature string.

Name

	

Type

	

Required

	

Value

	

Description




x-oss-forbid-overwrite

	

String

	

No

	

true

	

Specifies whether to overwrite an existing destination object that has the same name. If versioning is enabled or suspended for the destination bucket, the x-oss-forbid-overwrite request header is invalid. This means that overwriting an object with the same name is allowed.

If x-oss-forbid-overwrite is not specified or x-oss-forbid-overwrite is set to false, you can overwrite a destination Object with the same name.

If you set x-oss-forbid-overwrite to true, an existing destination object with the same name is not overwritten.

Setting the x-oss-forbid-overwrite request header degrades QPS processing performance. To use the x-oss-forbid-overwrite request header for many operations (QPS > 1000), contact technical support to avoid affecting your business.

Default value: false




x-oss-copy-source

	

String

	

Yes

	

/oss-example/oss.jpg

	

Specifies the source address for the copy operation.

Default value: none




x-oss-copy-source-if-match

	

String

	

No

	

5B3C1A2E053D763E1B002CC607C5****

	

The copy operation is performed and 200 OK is returned only if the ETag of the source object matches the ETag you provide.

Default value: none




x-oss-copy-source-if-none-match

	

String

	

No

	

5B3C1A2E053D763E1B002CC607C5****

	

The copy operation is performed and 200 OK is returned only if the ETag of the source object does not match the ETag you provide.

Default value: none




x-oss-copy-source-if-unmodified-since

	

String

	

No

	

Mon, 11 May 2020 08:16:23 GMT

	

The object is copied and 200 OK is returned only if the time you specify is the same as or later than the actual modification time of the object.

Default value: none




x-oss-copy-source-if-modified-since

	

String

	

No

	

Mon, 11 May 2020 08:16:23 GMT

	

The object is copied and 200 OK is returned only if the time you specify is earlier than the actual modification time of the object.

Default value: none




x-oss-metadata-directive

	

String

	

No

	

COPY

	

Specifies how to set the metadata of the destination object.

COPY (default): Copies the metadata from the source object to the destination object.

OSS does not copy the x-oss-server-side-encryption property from the source object to the destination object. The server-side encryption method for the destination object depends on whether x-oss-server-side-encryption is specified in the copy operation.

REPLACE: Ignores the metadata of the source object and uses the metadata specified in the request.

Important

If the source and destination objects are the same and versioning is not enabled, the metadata of the source object is ignored regardless of the value of x-oss-metadata-directive. The destination object uses the metadata specified in the request.




x-oss-server-side-encryption

	

String

	

No

	

AES256

	

Specifies the server-side encryption algorithm that OSS uses to create the destination object.

Valid values: AES256 and KMS

Important

You cannot specify x-oss-server-side-encryption when you copy a symbolic link object.

You can use the KMS encryption algorithm only after you purchase a KMS suite. Otherwise, OSS returns the KmsServiceNotEnabled error.

If x-oss-server-side-encryption is not specified in the copy operation, the destination object is not server-side encrypted, regardless of whether the source object was encrypted.

If x-oss-server-side-encryption is specified in the copy operation, the destination object is server-side encrypted, regardless of whether the source object was encrypted. The response header for the copy operation includes x-oss-server-side-encryption, and its value is the encryption algorithm of the destination object.

When the destination object is downloaded, the response header also includes x-oss-server-side-encryption, and its value is the encryption algorithm of the object.




x-oss-server-side-encryption-key-id

	

String

	

No

	

9468da86-3509-4f8d-a61e-6eab1eac****

	

Specifies the customer master key (CMK) that is managed by KMS.

This parameter is valid only when x-oss-server-side-encryption is set to KMS.




x-oss-object-acl

	

String

	

No

	

private

	

Specifies the access permissions of the destination object when it is created in OSS.

Valid values:

default (default): The object inherits the permissions of the bucket.

private: The object is a private resource. Only the object owner and authorized users have read and write permissions on the object. Other users cannot access the object.

public-read: The object is a public-read resource. Only the object owner and authorized users have read and write permissions on the object. Other users have only read permissions. Use this permission with caution.

public-read-write: The object is a public-read-write resource. All users have read and write permissions on the object. Use this permission with caution.

For more information about access permissions, see Object ACL.




x-oss-storage-class

	

String

	

No

	

Standard

	

Specifies the storage class of the object.

For a bucket of any storage class, if you specify this header when you upload an object, the uploaded object is stored in the specified storage class. For example, if you set x-oss-storage-class to Standard when you upload an object to an IA bucket, the object is stored as a Standard object.

Valid values:

Standard (default): Standard

IA: Infrequent Access

Archive: Archive Storage

ColdArchive: Cold Archive

DeepColdArchive: Deep Cold Archive

Important

To copy many files, directly specifying Deep Cold Archive as the storage class for the copied files results in high fees for PUT requests. We recommend that you use a lifecycle rule to transition the files to the Deep Cold Archive storage class to reduce PUT request fees.

For more information about storage classes, see Storage classes.




x-oss-tagging

	

String

	

No

	

a:1

	

Specifies the tags of the object. You can specify multiple tags at the same time, for example, TagA=A&TagB=B.

Note

The key and value must be URL-encoded. If an item does not contain an equal sign (=), the value is considered an empty string.




x-oss-tagging-directive

	

String

	

No

	

Copy

	

Specifies how to set the tags of the destination object. Valid values:

Copy (default): Copies the tags from the source object to the destination object.

Replace: Ignores the tags of the source object and uses the tags specified in the request.

This operation also uses common request headers, such as Host and Date. For more information, see Common request headers.

Response headers

This operation uses only common response headers. For more information, see Common response headers.

Response elements

Name

	

Type

	

Example

	

Description




CopyObjectResult

	

Container

	

N/A

	

A container for the results of the CopyObject operation.

Default value: none




ETag

	

String

	

5B3C1A2E053D763E1B002CC607C5****

	

The ETag of the destination object.

Parent element: CopyObjectResult




LastModified

	

String

	

Fri, 24 Feb 2012 07:18:48 GMT

	

The time when the destination object was last updated.

Parent element: CopyObjectResult

Examples

Versioning is disabled

Sample request

 
PUT /test%2FAK.txt HTTP/1.1
Host: tesx.oss-cn-zhangjiakou.aliyuncs.com
Accept-Encoding: identity
User-Agent: aliyun-sdk-python/2.6.0(Windows/7/AMD64;3.7.0)
Accept: text/html
Connection: keep-alive
x-oss-copy-source: /test/AK.txt
date: Fri, 28 Dec 2018 09:41:55 GMT
authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Content-Length: 0

Sample response

x-oss-hash-crc64ecma indicates the 64-bit CRC value of the object. This 64-bit CRC value is calculated based on the CRC-64/XZ standard. The CopyObject operation does not guarantee that the generated object has a 64-bit CRC value.

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 28 Dec 2018 09:41:56 GMT
Content-Type: application/xml
Content-Length: 184
Connection: keep-alive
x-oss-request-id: 5C25EFE4462CE00EC6D87156
ETag: "F2064A169EE92E9775EE5324D0B1****"
x-oss-hash-crc64ecma: 12753002859196105360
x-oss-server-time: 150
<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
  <ETag>"F2064A169EE92E9775EE5324D0B1****"</ETag>
  <LastModified>2018-12-28T09:41:56.000Z</LastModified>
</CopyObjectResult>

Copy an object without specifying a version ID

Sample request

 
PUT /dest-object-example HTTP/1.1
Host: versioning-copy.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 03:45:32 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-copy-source: /versioning-copy-source/source-object

Sample response

In this example, x-oss-copy-source-version-id is the version ID of the source object, which in this case is the current version. x-oss-version-id is the version ID of the newly copied object.

 
HTTP/1.1 200 OK
x-oss-copy-source-version-id: CAEQNRiBgIC28uaA0BYiIDY5OGIwNmNlNjYyMTRjNTc4N2M2OGNiMjZkZTQ2****
x-oss-version-id: CAEQNxiBgIDG8uaA0BYiIGZhZDRkZTk5Zjg3YzRhNzdiMWEwZGViNDM1NTFh****
x-oss-request-id: 5CAC155CB7AEADE01700****
Content-Type: application/xml
Content-Length: 184
Connection: keep-alive
Date: Tue, 09 Apr 2019 03:45:32 GM