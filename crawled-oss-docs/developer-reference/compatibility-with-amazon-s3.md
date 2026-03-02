# S3-compatible APIs of OSS and differences between OSS and S3

This topic describes the API operations in Amazon Simple Storage Service (Amazon S3) that are compatible with Object Storage Service (OSS) and the differences between OSS and S3.

## Compatible S3 API operations


The following table describes the bucket, object, and multipart API operations in S3 that are compatible with OSS.


> NOTE:

> NOTE: 


> NOTE: Note 

For API calls using the S3 protocol, the `x-oss-process` parameter is limited to `image/` and `style/` types. Other processing types, such as `video/`, are not supported.








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


| Operation type | Operation |
| --- | --- |
| Bucket operations | PutBucketDeleteBucketGetBucket (ListObjects)GetBucketV2 (ListObjectsV2)GetBucketACLGetBucketLifecycleGetBucketLocationGetBucketLoggingHeadBucketPutBucketACLPutBucketLifecyclePutBucketLogging |
| Object operations | DeleteObjectDeleteObjectsGetObjectGetObjectACLHeadObjectPostObjectPutObjectPutObjectCopyPutObjectACL |
| Multipart operations | InitiateMultipartUploadAbortMultipartUploadCompleteMultipartUploadListPartsUploadPartUploadPartCopy |


## Differences between OSS and S3


The following section describes the differences between OSS and S3:


-

Request style


Amazon S3 supports two request addressing styles: virtual-hosted and path-style. Virtual-hosted style requests use the bucket name as a subdomain in the endpoint, while path-style requests place the bucket name in the URL path. For security reasons, OSS supports only the virtual-hosted style. Therefore, after being migrated from S3 to OSS, all client applications and S3-compatible tools must be configured to use virtual-hosted style requests. Failure to do so will result in access being denied.

-

Definitions of access control lists (ACLs)


The definition of ACL is different in OSS and S3. The following table describes the differences.














-


-


-


| Level | Permission | S3 | OSS |
| --- | --- | --- | --- |
| Bucket | READ | The permissions to list buckets. | If no object permissions are configured for an object in a bucket, you can perform only read operations on the object. |
| WRITE | The permissions to write or overwrite objects in a bucket. | If the object that you want to write does not exist in the specified bucket, the object is created in the bucket. If the object that you want to write exists in the specified bucket and no permissions are configured for the existing object, the existing object can be overwritten. Use InitiateMultipartUpload to upload objects. |
| READ_ACP | The permissions to read the ACL of a bucket. | Only the bucket owner and authorized RAM users have the permissions to read the ACL of a bucket. |
| WRITE_ACP | The permissions to configure the ACL of a bucket. | Only the bucket owner and authorized RAM users have the permissions to configure the ACL of a bucket. |
| Object | READ | The permissions to read an object. | The permissions to read an object. |
| WRITE | N/A | The permissions to overwrite an object. |
| READ_ACP | The permissions to read the ACL of an object. | Only the bucket owner and authorized RAM users have the permissions to read the ACL of an object. |
| WRITE_ACP | The permissions to configure the ACL of an object. | Only the bucket owner and authorized RAM users have the permissions to configure the ACL of an object. |


> NOTE:

> NOTE: 


> NOTE: Important 

OSS supports only the following ACL modes in S3: private, public-read, and public-read-write.


-

Storage class


In Amazon S3, the Standard storage class is referred to as STANDARD, the Infrequent Access (IA) storage class is referred to as STANDARD_IA, and the Archive storage class is referred to as GLACIER. You can convert the storage class of OSS objects based on your requirements.


If real-time access to Archive objects is not enabled for a bucket, you must first restore the Archive objects in the bucket before you can access them. OSS ignores the duration of the restored state configured for objects in S3 API operations. By default, the restored state lasts for one day and can be extended up to seven days. Then, the object enters the frozen state.

-

ETag


-

If objects are uploaded by using the PUT method, the ETag of an OSS object and the ETag of an Amazon S3 object have different case sensitivities. The ETag of an OSS object is in uppercase letters, and the ETag of an Amazon S3 object is in lowercase letters. If your client uses ETag to validate content, configure your client to ignore the case sensitivity to prevent errors.

-

If objects are uploaded by using the multipart upload method, OSS calculates ETag values by using a different method from that of S3.

Thank you! We've received your  feedback.