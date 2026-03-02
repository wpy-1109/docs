# What is OSS on CloudBox?

Object Storage Service (OSS) on CloudBox provides local storage, local access, and local data processing of unstructured data for CloudBox. You can create a bucket in OSS on CloudBox and use the same OSS API operations and OSS SDKs as Alibaba Cloud public cloud to access data in OSS on CloudBox.

## Benefits


CloudBox is a fully managed cloud service provided by Alibaba Cloud. The hardware and software of Alibaba Cloud public cloud are integrated into your data center to meet specific requirements, such as data security, local data processing, and low latency. You can have the same user experience that you have on the public cloud in your data center. You can use CloudBox out of the box. This helps you better focus on business logic and reduce the O&M workloads on hardware and the cloud platform. For more information about CloudBox, see [What is CloudBox?](https://www.alibabacloud.com/help/en/cloud-box/product-overview/what-is-cloudbox#concept-2035794)


Compared with Alibaba Cloud public cloud, CloudBox provides advantages, such as data security, local data processing, and low latency.


-

Data security: Data is stored in data centers under your control, which meets the regulatory requirements for locally storing data.

-

Local data processing: You do not need to upload data to Alibaba Cloud public cloud, which reduces the cost of uploading large amounts of data to Alibaba Cloud public cloud.

-

Low latency: Your cloud box is geographically close to your local devices and can interact with local devices and applications in near real time.

-

Exclusive resources: You do not need to share storage with other customers in the Alibaba Cloud public cloud. In this case, you can store sensitive data with ease.

## Billing rules


For more information about the billing methods, scale up rules, and billing cases of OSS on CloudBox, see [OSS resources](https://www.alibabacloud.com/help/en/cloud-box/product-overview/oss-resources#concept-2203995).

## Limits


-

Each Alibaba Cloud account can create up to 100 region-specific buckets in OSS on CloudBox.

-

You can set the storage class of OSS on CloudBox buckets and objects in OSS on CloudBox buckets only to Standard.

-

The server-side encryption method of OSS on CloudBox can only be SSE-OSS. SSE-KMS is not supported.

-

OSS on CloudBox can only be accessed by using internal endpoints. Public endpoints are not supported. If you want to transfer OSS data between CloudBox and Alibaba Cloud public cloud, establish a network connection between CloudBox and Alibaba Cloud public cloud, and use [ossimport](https://www.alibabacloud.com/help/en/oss/overview-36#concept-rc2-t1h-wdb) to transfer data.

## OSS on CloudBox endpoints


You can use a CloudBox VPC to access an OSS on CloudBox bucket. Access endpoints are divided into control endpoints and data endpoints.


-

Control endpoints


Control endpoints are used only for operations on OSS on CloudBox buckets. For more information about the API operations supported by control endpoints, see [API operations supported by control endpoints].


Control endpoints are in the following format: `<Cloudbox-Id>.<Region>.oss-cloudbox-control.aliyuncs.com`. Example: `cb-f8z7yvzgwfkl9q0h.cn-shenzhen.oss-cloudbox-control.aliyuncs.com`.

-

Data endpoints


Data endpoints can be used to perform operations on OSS on CloudBox buckets and data in OSS on CloudBox buckets. For more information about the API operations supported by data endpoints, see [API operations supported by data endpoints].


Data endpoints are in the following format: `<Cloudbox-Id>.<Region>.oss-cloudbox.aliyuncs.com`. Example: `cb-f8z7yvzgwfkl9q0h.cn-shenzhen.oss-cloudbox.aliyuncs.com`.


If you create a VPC in CloudBox and need to use OSS in the VPC environment, contact [technical support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex) to enable the endpoints.

## API operations supported by control endpoints


The following table describes the bucket-level API operations supported by OSS on CloudBox control endpoints.











(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#reference-wdh-fj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucket#reference-o1j-rrw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketinfo#reference-rwk-bwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlocation#reference-e11-qtv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketacl#reference-zzr-hk5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketacl#reference-hgp-psv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlifecycle#reference-xlw-dbv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlifecycle#reference-zq5-grw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlifecycle#reference-wl1-xsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketversioning#reference-w2w-nm3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketversioning#reference-fhn-kt3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy#reference-2424532)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicy#reference-2424982)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpolicy#reference-2424995)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketwebsite#reference-hwb-yr5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketwebsite#reference-wvy-s4w-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketwebsite#reference-zrl-msw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketreferer#reference-prc-ys5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreferer#reference-bs5-rpw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketencryption#concept-262214)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketencryption#concept-262215)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketencryption#concept-262216)


| Category | API | Description |
| --- | --- | --- |
| Basic operations | PutBucket | Creates an OSS on CloudBox bucket. |
| DeleteBucket | Deletes an OSS on CloudBox bucket. |
| GetBucketInfo | Queries information about an OSS on CloudBox bucket. |
| GetBucketLocation | Queries the region in which an OSS on CloudBox bucket is located. |
| ACL | PutBucketAcl | Specifies the access control list (ACL) of an OSS on CloudBox bucket. |
| GetBucketAcl | Queries the ACL of an OSS on CloudBox bucket. |
| Lifecycle | PutBucketLifecycle | Configures lifecycle rules for an OSS on CloudBox bucket. |
| GetBucketLifecycle | Queries the lifecycle rules of an OSS on CloudBox bucket. |
| DeleteBucketLifecycle | Deletes the lifecycle rules of an OSS on CloudBox bucket. |
| Versioning | PutBucketVersioning | Specifies the versioning status of an OSS on CloudBox bucket. |
| GetBucketVersioning | Queries the versioning status of an OSS on CloudBox bucket. |
| Bucket policy | PutBucketPolicy | Configures a bucket policy for an OSS on CloudBox bucket. |
| GetBucketPolicy | Queries the bucket policies of an OSS on CloudBox bucket. |
| DeleteBucketPolicy | Deletes a bucket policy of an OSS on CloudBox bucket. |
| Logging | PutBucketLogging | Enables logging for an OSS on CloudBox bucket. |
| GetBucketLogging | Queries the logging configurations of an OSS on CloudBox bucket. |
| DeleteBucketLogging | Disables logging for an OSS on CloudBox bucket. |
| Static website hosting | PutBucketWebsite | Enables static website hosting for an OSS on CloudBox bucket. |
| GetBucketWebsite | Queries the static website hosting configurations of an OSS on CloudBox bucket. |
| DeleteBucketWebsite | Disables static website hosting for an OSS on CloudBox bucket. |
| Hotlink protection | PutBucketReferer | Configures hotlink protection for an OSS on CloudBox bucket. |
| GetBucketReferer | Queries the hotlink protection configurations of an OSS on CloudBox bucket. |
| Encryption | PutBucketEncryption | Configures encryption rules for an OSS on CloudBox bucket. |
| GetBucketEncryption | Queries the encryption rules of an OSS on CloudBox bucket. |
| DeleteBucketEncryption | Deletes the encryption rules of an OSS on CloudBox bucket. |


## API operations supported by data endpoints


The following tables describe the API operations supported by the data endpoints of OSS on CloudBox.

### Service-level operation








(https://www.alibabacloud.com/help/en/oss/developer-reference/listbuckets#reference-ahf-k4t-tdb)


| API | Description |
| --- | --- |
| ListBuckets (GetService) | Lists all buckets that are owned by the requester. |


### Bucket-level operations











(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#reference-wdh-fj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucket#reference-o1j-rrw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects-v2#reference-2520881)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketinfo#reference-rwk-bwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlocation#reference-e11-qtv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketacl#reference-zzr-hk5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketacl#reference-hgp-psv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlifecycle#reference-xlw-dbv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlifecycle#reference-zq5-grw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlifecycle#reference-wl1-xsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketversioning#reference-w2w-nm3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketversioning#reference-fhn-kt3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjectversions#reference-n2s-xy3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy#reference-2424532)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicy#reference-2424982)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpolicy#reference-2424995)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketwebsite#reference-hwb-yr5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketwebsite#reference-wvy-s4w-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketwebsite#reference-zrl-msw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketreferer#reference-prc-ys5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreferer#reference-bs5-rpw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketencryption#concept-262214)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketencryption#concept-262215)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketencryption#concept-262216)


| Category | API | Description |
| --- | --- | --- |
| Basic operations | PutBucket | Creates an OSS on CloudBox bucket. |
| DeleteBucket | Deletes an OSS on CloudBox bucket. |
| GetBucket(ListObjects) | Queries information about all objects in an OSS on CloudBox bucket. |
| ListObjectsV2 (GetBucketV2) | Queries information about all objects in an OSS on CloudBox bucket. |
| GetBucketInfo | Queries information about an OSS on CloudBox bucket. |
| GetBucketLocation | Queries the region in which an OSS on CloudBox bucket is located. |
| ACL | PutBucketAcl | Specifies the ACL of an OSS on CloudBox bucket. |
| GetBucketAcl | Queries the ACL of an OSS on CloudBox bucket. |
| Lifecycle | PutBucketLifecycle | Configures lifecycle rules for an OSS on CloudBox bucket. |
| GetBucketLifecycle | Queries the lifecycle rules of an OSS on CloudBox bucket. |
| DeleteBucketLifecycle | Deletes the lifecycle rules of an OSS on CloudBox bucket. |
| Versioning | PutBucketVersioning | Specifies the versioning status of an OSS on CloudBox bucket. |
| GetBucketVersioning | Queries the versioning status of an OSS on CloudBox bucket. |
| ListObjectVersions (GetBucketVersions) | Lists the versions of all objects in an OSS on CloudBox bucket. |
| Bucket policy | PutBucketPolicy | Configures a bucket policy for an OSS on CloudBox bucket. |
| GetBucketPolicy | Queries the bucket policies of an OSS on CloudBox bucket. |
| DeleteBucketPolicy | Deletes a bucket policy of an OSS on CloudBox bucket. |
| Logging | PutBucketLogging | Enables logging for an OSS on CloudBox bucket. |
| GetBucketLogging | Queries the logging configurations of an OSS on CloudBox bucket. |
| DeleteBucketLogging | Disables logging for an OSS on CloudBox bucket. |
| Static website hosting | PutBucketWebsite | Enables static website hosting for an OSS on CloudBox bucket. |
| GetBucketWebsite | Queries the static website hosting configurations of an OSS on CloudBox bucket. |
| DeleteBucketWebsite | Disables static website hosting for an OSS on CloudBox bucket. |
| Hotlink protection | PutBucketReferer | Configures hotlink protection for an OSS on CloudBox bucket. |
| GetBucketReferer | Queries the hotlink protection configurations of an OSS on CloudBox bucket. |
| Encryption | PutBucketEncryption | Configures encryption rules for an OSS on CloudBox bucket. |
| GetBucketEncryption | Queries the encryption rules of an OSS on CloudBox bucket. |
| DeleteBucketEncryption | Deletes the encryption rules of an OSS on CloudBox bucket. |


### Object-level operations











(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobject#reference-ccf-rgd-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject#reference-mvx-xxc-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/appendobject#reference-fvf-xld-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject#reference-iqc-mqv-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletemultipleobjects#reference-ydg-25v-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/headobject#reference-bgh-cbw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectmeta#reference-sg4-k2w-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpartcopy#reference-t4b-vpx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listmultipartuploads#reference-hj2-3wx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listparts#reference-hzm-1zx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjectacl#reference-fs3-gfw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectacl#reference-lzc-24w-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putsymlink#reference-qzz-qzw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getsymlink#reference-s3d-s1x-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjecttagging#reference-185784)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjecttagging#concept-185787)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobjecttagging#reference-185788)


| Category | APi | Description |
| --- | --- | --- |
| Basic operations | PutObject | Uploads an object. |
| GetObject | Queries an object. |
| CopyObject | Copies an object. |
| AppendObject | Uploads an object by using append upload. |
| DeleteObject | Deletes an object. |
| DeleteMultipleObjects | Deletes multiple objects at a time. |
| HeadObject | Queries only the metadata of an object. |
| GetObjectMeta | Queries only the basic metadata of an object, including the ETag, size, and last modified time. |
| Multipart upload | InitiateMultipartUpload | Initiates a multipart upload task. |
| UploadPart | Uploads an object by part based on a specific object name and upload ID. |
| UploadPartCopy | Copies data from an existing object to upload a part by adding the x-oss-copy-source request header to an UploadPart request. |
| CompleteMultipartUpload | Completes the multipart upload task of an object. |
| AbortMultipartUpload | Cancels a multipart upload task and deletes the uploaded parts. |
| ListMultipartUploads | Lists all ongoing multipart upload tasks, which include tasks that are initiated but are not completed or canceled. |
| ListParts | Lists all parts uploaded by a multipart upload task that has a specific upload ID. |
| ACL | PutObjectACL | Modifies the ACL of an object. |
| GetObjectACL | Queries the ACL of an object. |
| Symbolic link | PutSymlink | Creates a symbolic link. |
| GetSymlink | Queries a symbolic link. |
| Tagging | PutObjectTagging | Adds tags to or modifies the tags of an object. |
| GetObjectTagging | Queries the tags of an object. |
| DeleteObjectTagging | Deletes the tags of an object. |


## References


-

[Get started with OSS on CloudBox](https://www.alibabacloud.com/help/en/oss/user-guide/getting-started-with-oss-deployed-in-cloudbox)

-

[Bucket operations supported by OSS on CloudBox](https://www.alibabacloud.com/help/en/oss/user-guide/bucket-operations-supported-by-oss-deployed-in-cloudbox/)

-

[Object operations supported by OSS on CloudBox](https://www.alibabacloud.com/help/en/oss/user-guide/object-operations-supported-by-oss-deployed-in-cloudbox/)

Thank you! We've received your  feedback.