# Object-level operations

To modify an object's access control list (ACL), invoke the PutObjectACL operation. This action is restricted to the bucket owner, who must possess read and write permissions for the object.

Versioning

By default, the PutObjectACL operation configures the ACL for the current version of the object. To modify the ACL of a specific version, include the versionId parameter in your request.

If a versionId is specified and the object's version is a delete marker, OSS will return a 405 MethodNotAllowed error.

Without a versionId, if the latest object version is a delete marker, OSS will return a 404 NoSuchKey error.

ACL overview

The PutObjectACL operation uses the x-oss-object-acl header in the Put request to set the object's ACL. The table below details the four types of access permissions available for an object.

Name

	

Description




private

	

The object is a private resource. Only the owner of the object has permissions to read and write this object. Other users do not have permissions on the object.




public-read

	

The object is a public-read resource. The owner of the object has permissions to read and write this object. Other users can only read the object.




public-read-write

	

The object is a public-read-write resource. All users have permissions to read and write the object.




default

	

The ACL of the object is the same as the ACL of the bucket in which the object is stored.

Note

An object's ACL takes precedence over the bucket's ACL. For instance, an object with a public-read-write ACL in a private bucket will be accessible for reading and writing by all users, despite the bucket's private setting. The object's ACL defaults to the bucket's ACL if not set explicitly.

Reading operations include GetObject, HeadObject, CopyObject, and UploadPartCopy, where CopyObject and UploadPartCopy read the source object. Writing operations include PutObject, PostObject, AppendObject, DeleteObject, DeleteMultipleObjects, CompleteMultipartUpload, and CopyObject, where CopyObject writes to the destination object.

The x-oss-object-acl header can also be included in write operations to set an object's ACL, equivalent to invoking the PutObjectACL operation. For example, you can set the ACL for an uploaded object by including this header in a PutObject request.

Request syntax
 
PUT /ObjectName?acl HTTP/1.1
x-oss-object-acl: Permission
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

Name

	

Type

	

Required

	

Example

	

Description




x-oss-object-acl

	

String

	

Yes

	

public-read

	

Specifies the access control list (ACL) of the object when OSS creates the object.

Valid values:

default (default): The ACL of the object is the same as the ACL of the bucket in which the object is stored.

private: The object is a private resource. Only the owner of the object and authorized users have permissions to read and write the object. Other users do not have permissions on the object.

public-read: The object is a public-read resource. Only the owner of the object and authorized users have permissions to read and write the object. Other users can only read the object. Exercise caution when you use this permission.

public-read-write: The object is a public-read-write resource. All users have permissions to read and write the object. Exercise caution when you use this permission.

For more information about access permissions, see Configure object ACL.

This operation also requires common request headers, including Host and Date. For more information, see Common request headers.

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples

Unversioned Bucket

Sample Request

 
PUT /test-object?acl HTTP/1.1
x-oss-object-acl: public-read
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 29 Apr 2015 05:21:12 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample Response

 
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A64485981
Date: Wed, 29 Apr 2015 05:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS

Versioned Bucket

Sample Request

 
PUT /example?acl&versionId=CAEQMhiBgIC3rpSD0BYiIDBjYTk5MmIzN2JlNjQxZTFiNGIzM2E3OTliODA0**** HTTP/1.1
x-oss-object-acl: public-read
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:30:11 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample Response

 
HTTP/1.1 200 OK
x-oss-version-id: CAEQMhiBgIC3rpSD0BYiIDBjYTk5MmIzN2JlNjQxZTFiNGIzM2E3OTliODA0****
x-oss-request-id: 5CAC3BF3B7AEADE017000624
Date: Tue, 09 Apr 2019 06:30:11 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
SDKs

The PutObjectACL operation can be called using OSS SDKs for the following programming languages:

Java

Python

Go V2

PHP

Node.js

Browser.js

.NET

C++

C

Command line tool ossutil

For the ossutil command equivalent to the PutObjectACL operation, refer to put-object-acl.

Error codes

Error code

	

HTTP status code

	

Description




AccessDenied

	

403

	

You are not the bucket owner or do not have permissions to read and write the object whose ACL you want to modify.




InvalidArgument

	

400

	

The specified x-oss-object-acl value is invalid.




FileAlreadyExists

	

409

	

The object whose ACL you want to modify is a directory in a bucket for which the hierarchical namespace feature is enabled.