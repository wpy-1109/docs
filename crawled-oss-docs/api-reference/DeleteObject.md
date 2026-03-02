# Object-level operations

Call DeleteObject to delete an object.

Usage notes

If a bucket has a data replication rule with the replication policy set to Sync Additions, Deletions, And Modifications, when you call DeleteObject to delete an object from the bucket, the corresponding object in the destination bucket specified in the replication policy is also deleted. The deleted object cannot be recovered. If versioning is enabled for the bucket, when you call DeleteObject, not only is a delete marker created for the deleted object in the bucket, but this action is also replicated to the destination bucket, which means a corresponding delete marker is also generated in the destination bucket.

Deleted objects cannot be recovered. Exercise caution when you delete objects. For more information about deleting objects, see Delete objects.

HTTP status code 204 is returned when the DeleteObject operation succeeds, regardless of whether the object exists.

If the object type is a symbolic link, the DeleteObject operation deletes only the symbolic link.

If the hierarchical namespace feature is enabled for a bucket, you cannot use the DeleteObject operation to delete a directory from the bucket.

Versioning

When you call DeleteObject to delete an object from a versioned bucket, you must determine whether to specify a version ID in the request.

Delete an object without specifying a version ID (temporary deletion)

By default, if you do not specify the version ID of the object that you want to delete in the request, OSS does not delete the current version of the object but adds a delete marker to the object as the new version. In addition, OSS includes the header: x-oss-delete-marker = true and the version ID of the created delete marker x-oss-version-id in the response.

The value of x-oss-delete-marker is true, which indicates that the version corresponding to the returned x-oss-version-id is a delete marker.

Note

If versioning is suspended for a bucket and an object has a previous version whose ID is null, a delete marker whose version ID is null is added to the object and the previous version whose ID is null is overwritten when you perform the DeleteObject operation without specifying a version ID in the request. An object can have up to one version whose version ID is null.

Delete an object by specifying a version ID (permanent deletion)

If you specify the version ID of the object that you want to delete in the DeleteObject request, OSS permanently deletes the version specified by the params parameter versionId. To delete a version whose ID is null, add params['versionId'] = "null" to the params parameter. OSS identifies the string "null" as the null version ID and deletes the object version whose ID is null.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM Policy or Bucket Policy.

API

	

Action

	

Description




DeleteObject

	

oss:DeleteObject

	

Deletes an object.




oss:DeleteObjectVersion

	

Deletes a specified version of an object.

Request syntax
 
DELETE /ObjectName HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response headers

Name

	

Type

	

Example value

	

Description




x-oss-delete-marker

	

Boolean

	

true

	

Indicates whether the object is a delete marker.

If you do not specify the version ID of the object that you want to delete in the DeleteObject request, OSS creates a delete marker as the current version of the object and includes this header with a value of true in the response.

If you specify the version ID of the object you want to delete in the DeleteObject request and the specified version is a delete marker, OSS includes this header with a value of true in the response.

Valid value: true




x-oss-version-id

	

string

	

CAEQMxiBgIDh3ZCB0BYiIGE4YjIyMjExZDhhYjQxNzZiNGUyZTI4ZjljZDcz****

	

The version ID of the object.

If you do not specify the version ID of the object that you want to delete in the DeleteObject request, OSS creates a delete marker as the current version of the object and includes this header in the response to indicate the version ID of the created delete marker.

If you specify the version ID of the object you want to delete in the DeleteObject request, OSS includes this header in the response to indicate the ID of the deleted object version.

The response to this request contains common response headers. For more information about common response headers, see Common Response Headers.

Examples

Delete an object from an unversioned bucket

Sample request

 
DELETE /AK.txt HTTP/1.1
Host: test.oss-cn-zhangjiakou.aliyuncs.com
Accept-Encoding: identity
User-Agent: aliyun-sdk-python/2.6.0(Windows/7/AMD64;3.7.0)
Accept: text/html
Connection: keep-alive
Date: Wed, 02 Jan 2019 13:28:38 GMT
authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Content-Length: 0

Sample response

 
HTTP/1.1 204 No Content
Server: AliyunOSS
Date: Wed, 02 Jan 2019 13:28:38 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5C2CBC8653718B5511EF4535
x-oss-server-time: 134

Delete an object from a versioned bucket without specifying a version ID

In this case, OSS adds a delete marker to the object and includes x-oss-delete-marker=true in the response.

Sample request

 
DELETE /example HTTP/1.1
Host: versioning-delete.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 04:08:23 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204 NoContent
x-oss-delete-marker: true
x-oss-version-id: CAEQMxiBgIDh3ZCB0BYiIGE4YjIyMjExZDhhYjQxNzZiNGUyZTI4ZjljZDcz****
x-oss-request-id: 5CAC1AB7B7AEADE01700****
Date: Tue, 09 Apr 2019 04:08:23 GMT
Connection: keep-alive
Server: AliyunOSS

Delete a version of the object from a versioned bucket by specifying the version ID

In this case, the specified version of the object is permanently deleted.

Sample request

 
DELETE /example?versionId=CAEQOBiBgIDNlJeB0BYiIDAwYjJlNDQ4YjJkMzQxMmY5NTM5N2UzZWNiZTQ2**** HTTP/1.1
Host: versioning-delete.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 04:11:54 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204 No Content
x-oss-version-id: CAEQOBiBgIDNlJeB0BYiIDAwYjJlNDQ4YjJkMzQxMmY5NTM5N2UzZWNiZTQ2****
x-oss-request-id: 5CAC1B8AB7AEADE01700****
Date: Tue, 09 Apr 2019 04:11:54 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS

Delete a delete marker by specifying its version ID

If the specified version is a delete marker, OSS includes x-oss-delete-marker=true in the response.

Sample request

 
DELETE /example?versionId=CAEQOBiBgIDNlJeB0BYiIDAwYjJlNDQ4YjJkMzQxMmY5NTM5N2UzZWNiZTQ2**** HTTP/1.1
Host: versioning-delete.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 04:16:25 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample response

 
HTTP/1.1 204 No Content
x-oss-delete-marker: true
x-oss-version-id: CAEQNhiBgIDFtp.B0BYiIDk4NzgwMmU4NDMyOTQyM2NiMDQxOTcxYWNhMjc1****
x-oss-request-id: 5CAC1C99B7AEADE01700****
Date: Tue, 09 Apr 2019 04:16:25 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
SDK

The following SDKs provide the DeleteObject operation:

Java

Python V2

PHP

Go V2

C

.NET

Android

iOS

Node.js

Browser.js

Command-line tool ossutil

For information about the ossutil command that corresponds to the DeleteObject operation, see delete-object.

References

To delete multiple objects, see DeleteMultipleObjects.

To automatically delete objects, see Lifecycle.

Error codes

Error code

	

HTTP status code

	

Description




FileImmutable

	

409

	

You attempt to delete or modify protected data. During the protection period, data in the bucket cannot be deleted or modified.




FileAlreadyExists

	

409

	

The error message returned because the object that you want to delete is a directory in a bucket for which the hierarchical namespace feature is enabled.