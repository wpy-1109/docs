# Object-level operations

Creates a symbolic link that points to a destination object. Use the symbolic link as an alias to access the destination object.

Use cases

PutSymlink is unique to Object Storage Service (OSS). Use symbolic links to:

Create shorter, human-readable aliases for objects with long or complex keys.

Maintain backward-compatible paths when reorganizing your object key structure.

Point multiple logical paths to a single physical object to save storage.

Usage notes

OSS does not validate the destination object when creating a symbolic link. OSS does not check whether the destination object exists, whether its storage class is valid, or whether you have access to it.

The destination object cannot be a symbolic link.

By default, if an object with the same name already exists and you have the required permissions, PutSymlink overwrites the existing object and returns 200 OK.

When API operations such as GetObject access the destination object through a symbolic link, OSS checks both the access control list (ACL) of the symbolic link and the ACL of the destination object.

Request headers prefixed with x-oss-meta- are treated as user metadata of the symbolic link. Example: x-oss-meta-location. An object can have multiple user metadata parameters, but the total size of all user metadata cannot exceed 8 KB.

Versioning

A symbolic link can point to the current version of a destination object. Each version of a symbolic link can point to a different object.

When versioning is enabled on the bucket, PutSymlink generates a new version ID for the symbolic link and returns it in the x-oss-version-id response header.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account have no permissions by default. Grant permissions through RAM Policy or Bucket Policy.

API	Action	Definition
PutSymlink	oss:PutObject	Creates a symbolic link for an object.
	oss:PutObjectTagging	Required only when specifying object tags through x-oss-tagging.
Request syntax
 
PUT /ObjectName?symlink HTTP/1.1
Host: BucketName.oss-<RegionId>.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
x-oss-symlink-target: TargetObjectName
Request headers
Header	Type	Required	Description
x-oss-symlink-target	String	Yes	The destination object that the symbolic link points to. Naming conventions follow regular object rules. The value must be URL-encoded, similar to ObjectName. The destination object cannot be a symbolic link.
x-oss-forbid-overwrite	String	No	Controls whether PutSymlink overwrites an existing object with the same name. If not specified or set to false, the existing object is overwritten. If set to true, the existing object is not overwritten and OSS returns a FileAlreadyExists error. This header may degrade queries per second (QPS) performance. If you need to use this header in a large number of requests (QPS greater than 1,000), contact technical support.
Note

This header does not take effect when versioning is enabled or suspended for the destination bucket. In that case, PutSymlink always overwrites the existing object.


x-oss-object-acl	String	No	The ACL of the symbolic link object. Default value: default. Valid values: default (inherits the bucket ACL), private (only the owner and authorized users have read and write permissions), public-read (owner and authorized users have read and write permissions; other users have read-only permissions), public-read-write (all users have read and write permissions). For more information, see Object ACLs.
x-oss-storage-class	String	No	The storage class of the object. This value overrides the bucket storage class when specified. Valid values: Standard, IA, Archive. Infrequent Access (IA) and Archive objects have a minimum billable size of 64 KB. Do not set the storage class to IA or Archive in PutSymlink requests. For more information, see Overview.

For more information about common request headers such as Host and Date, see Common request headers.

Response headers

The response contains only common response headers. For more information, see Common response headers.

Examples
Example 1: Create a basic symbolic link

Sample request:

 
PUT /link-to-oss.jpg?symlink HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Cache-control: no-cache
Content-Disposition: attachment;filename=oss_download.jpg
Date: Tue, 08 Nov 2016 02:00:25 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-disposition,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-symlink-target: oss****
x-oss-storage-class: Standard

Sample response:

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 08 Nov 2016 02:00:25 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 582131B9109F4EE66CDE56A5
ETag: "0A477B89B4602AA8DECB8E19BFD4****"
Example 2: Create a symbolic link in a versioned bucket

Sample request:

 
PUT /link-to-oss.jpg?symlink HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:50:48 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-symlink-target: oss.jpg

Sample response:

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 09 Apr 2019 06:50:48 GMT
Content-Length: 0
Connection: keep-alive
x-oss-version-id: CAEQNRiBgMClj7qD0BYiIDQ5Y2QyMjc3NGZkODRlMTU5M2VkY2U3MWRiNGRh****
x-oss-request-id: 5CAC40C8B7AEADE01700064B
ETag: "136A5E127272200EDAB170DD84DE****"
OSS SDKs

Use OSS SDKs for the following programming languages to call the PutSymlink operation:

Java

Go V2

C

C++

.NET

Android

iOS

Node.js

Browser.js

ossutil

For the ossutil command that corresponds to PutSymlink, see put-symlink.

Error codes

The following table lists error codes specific to PutSymlink.

Error code	HTTP status code	Description
InvalidArgument	400	The value of StorageClass is invalid.
FileAlreadyExists	409	An object with the same name already exists and x-oss-forbid-overwrite is set to true.
FileImmutable	409	The data is protected by a retention policy and cannot be deleted or modified.

For common error codes that apply to all OSS operations, see Common error codes.