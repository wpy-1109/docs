# What is OSS?

Alibaba Cloud Object Storage Service (OSS) is a secure, cost-effective, and highly reliable cloud storage service that allows you to store large amounts of data. OSS is designed to provide 99.9999999999% (twelve 9's) data durability and 99.995% data availability. OSS provides multiple storage classes to help you manage and reduce storage costs.


OSS provides platform-independent API operations, which allows you to upload and access your data from any application, anytime, and anywhere.


Aside from the API operations, OSS provides OSS SDKs and migration tools that you can use to easily transfer large amounts of data to and from OSS. OSS provides storage classes that are intended for different storage scenarios. For example, you can store images, audio files, and video files used in your apps and websites as Standard objects for frequent access and store infrequently accessed data as Infrequent Access (IA), Archive, Cold Archive, or Deep Cold Archive objects to reduce the total costs of storage over time.


OSS as a cloud data lake can provide high bandwidth to download objects. In specific regions, a single Alibaba Cloud account can provide up to 100 Gbit/s of total download bandwidth over the internal network and Internet to meet the requirements of AI and large-scale data analysis. For more information about the bandwidth of each region, see [Bandwidth](https://www.alibabacloud.com/help/en/oss/user-guide/limits#481f9cdaa9cxq).

## Get started with OSS


-

Video introduction


Watch the following video for a quick introduction to OSS.


-

FAQ


Browse the [FAQ](https://www.alibabacloud.com/help/en/oss/faq-15#concept-1698037) to obtain answers to frequently asked questions about OSS.

## Terms


OSS stores data as objects within buckets. To store data in OSS, you must first create a bucket within a region and specify the access control list (ACL) and storage class for the bucket. When you upload an object to OSS, you must specify the name of the object (also referred to as an object key or a key). This name is the unique identifier of the object within a bucket.


OSS provides region-specific endpoints through which you can access your data. Endpoints allow you to use OSS operations to manage your data. OSS authenticates a request by verifying the symmetric AccessKey pair (AccessKey ID and AccessKey secret) included in the request.


OSS ensures atomic updates to all objects and provides strong consistency for operations on all objects.


-

Bucket


A bucket is a container for objects that are stored in OSS. Every object in OSS is contained in a bucket. You can configure various properties for a bucket, including the region, access control list (ACL), and storage class. Storage classes are useful when you need to store data that have different access patterns.

-

Object


Objects are the smallest data unit in OSS. Files uploaded to OSS are called objects. Unlike typical file systems, objects in OSS are stored in a flat structure instead of a hierarchical structure. An object is composed of a key, metadata, and the data stored in the object. Each object in a bucket is uniquely identified by the key. Object metadata is a group of key-value pairs that define the properties of an object, such as the file type and encoding format. You can also specify custom user metadata for objects in OSS.

-

Object key


In OSS SDKs for different programming languages, object key, key, and object name indicate the full path of the object. You must specify the full path of an object when you perform operations on the object. For example, when you upload an object to a bucket, ObjectKey indicates the full path that includes the extension of the object, such as abc/efg/123.jpg.

-

Region


A region is a physical location from which OSS provides services. When you create a bucket, you can select a region based on the cost or location from which the bucket is most frequently accessed. In most cases, when you access OSS from a geographically closer location, the access speed is faster. For more information, see [Regions, endpoints and open ports](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db).

-

Endpoint


An endpoint is a domain name used to access OSS. OSS provides region-specific endpoints that you can use to access your data. You can manage your data in different regions by using OSS API operations. A region has different endpoints for access over the internal network and for access over the Internet. For example, the public endpoint used to access OSS data in the China (Hangzhou) region is oss-cn-hangzhou.aliyuncs.com, and the internal endpoint is oss-cn-hangzhou-internal.aliyuncs.com. For more information, see [Regions, endpoints and open ports](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db).

-

AccessKey pair


An AccessKey pair is used to authenticate a requester. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. OSS uses an AccessKey pair to implement symmetric encryption and verify the identity of a requester. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt and verify the signature string. The AccessKey secret must be kept confidential. OSS supports AccessKey pairs obtained by using the following methods:


-

AccessKey pairs applied for by the bucket owner.

-

AccessKey pairs granted by the bucket owner by using Resource Access Management (RAM).

-

AccessKey pairs granted by the bucket owner by using Security Token Service (STS).


For more information, see [Obtain an AccessKey pair](https://www.alibabacloud.com/help/en/cloud-migration-guide-for-beginners/latest/obtain-an-accesskey-pair#task968).

-

Atomicity and strong consistency


Object operations in OSS are atomic. Operations are either successful or failed without intermediate states. When an object is uploaded, you can get either the data before or after the upload. You cannot obtain partial or corrupted data.


Object operations in OSS are highly consistent. For example, when you receive an upload (PUT) success response, you can immediately read the uploaded object, and replicas of the object are created for redundancy. Therefore, there are no scenarios in which data is not obtained when you perform the read-after-write operation. Similarly, after you delete an object, the object and its replicas no longer exist.


For more information about the terms in OSS, see [Terms](https://www.alibabacloud.com/help/en/oss/terms-2#concept-izx-fmt-tdb).

## Features


-

Versioning


Versioning is a bucket-level data protection feature that you can use to protect objects in a bucket against unintended operations. After versioning is enabled for a bucket, existing objects in the bucket are stored as previous versions when they are overwritten or deleted. Versioning allows you to recover accidentally overwritten or deleted objects to any previous versions. For more information, see [Overview](https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/#concept-jdg-4rx-bgb).

-

Bucket policy


A bucket policy is an access policy that provides flexible and fine-grained permission management. The owner of a bucket can configure bucket policies to grant users access permissions on the bucket and the objects in the bucket. For example, you can configure bucket policies to authorize other Alibaba Cloud accounts or anonymous users to access or manage all or specific resources in your bucket. You can also configure bucket policies to grant read-only, read/write, or full permissions to different RAM users of the same Alibaba Cloud account. For more information about how to configure bucket policies, see [Configure bucket policies to authorize other users to access OSS resources](https://www.alibabacloud.com/help/en/oss/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources#concept-ahc-tx4-j2b).

-

CRR


Cross-region replication (CRR) allows you to automatically and asynchronously (in near real-time) replicate objects in a bucket from one region to a bucket in a different region within the same account or a different account. CRR replicates operations, such as the creation, overwriting, and deletion of objects, from a source bucket to a destination bucket. CRR can help you meet compliance requirements for cross-region disaster recovery and data replication. For more information, see [CRR overview](https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication-overview/#concept-zjp-31z-5db).

-

Data encryption


Server-side encryption: OSS encrypts objects uploaded to a bucket for which server-side encryption is configured and stores the encrypted objects. When you download an object, OSS decrypts and returns the object. The x-oss-server-side-encryption header is included in the response to declare that the object is encrypted on the server side. For more information, see [Server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db).


Client-side encryption: Objects are encrypted on the local client before they are uploaded to OSS. For more information, see [Client-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/client-side-encryption#concept-2323737).

-

Data durability


By default, OSS permanently stores objects uploaded to a bucket except in the following circumstances:


-

Objects are manually deleted by using the OSS console, OSS SDKs, API operations, or OSS tools such as ossutil and ossbrowser. For more information, see [Delete objects](https://www.alibabacloud.com/help/en/oss/user-guide/delete-objects-18#concept-g42-bhd-5db).

-

Objects are automatically deleted based on a lifecycle rule. For more information, see [Lifecycle rules based on the last modified time](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#concept-y2g-szy-5db).

-

Overdue fees are not paid within 15 days after service suspension. For more information, see [Service suspension](https://www.alibabacloud.com/help/en/oss/overdue-payments#section-h0t-eo4-6d4).


For more information about OSS features, see [Functions and features](https://www.alibabacloud.com/help/en/oss/functions-and-features#concept-ilc-x31-tdb).

## Methods


You can use the following methods to upload, download, and manage objects in OSS:


-

OSS console


The [OSS console](https://oss.console.alibabacloud.com/overview) is a web-based console that provides a GUI-based way to manage OSS resources. For more information, see [Overview page of the OSS console](https://www.alibabacloud.com/help/en/oss/overview-of-the-oss-console/#concept-znd-p1z-5db).

-

OSS API operations or OSS SDKs


OSS provides RESTful API operations and OSS SDKs for multiple programming languages to facilitate custom development. For more information, see [List of operations by function](https://www.alibabacloud.com/help/en/oss/developer-reference/list-of-operations-by-function#reference-wrz-l2q-tdb) and [Overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).

-

OSS tools


OSS provides multiple management tools, such as ossbrowser, ossutil, and ossftp. For more information, see [OSS tools](https://www.alibabacloud.com/help/en/oss/developer-reference/oss-tools#concept-owg-knn-vdb).

-

CSG


OSS uses a flat structure instead of a hierarchical structure to store objects. All elements are stored as objects in buckets. If you want to manage your resources in OSS in the same way you manage local directories and files on disks, use OSS with Cloud Storage Gateway (CSG). For more information, visit the [CSG product page](https://www.alibabacloud.com/product/cloud-storage-gateway).

## Billing


OSS supports the following billing methods:


-

Pay-as-you-go: By default, the pay-as-you-go billing method applies to all billable items. You are charged for the actual usage of each billable item. Fees are paid after you use resources. This billing method is ideal for scenarios in which resource usage is difficult to predict. For more information, see [Pay-as-you-go](https://www.alibabacloud.com/help/en/oss/pay-as-you-go-1#concept-2247263).

-

Subscription (resource plans): OSS provides resource plans to offset fees generated for specific billable items. You can purchase resource plans that cover specific billable items at favorable prices. Resources are consumed before fees are offset by resource plans. Resource plans are ideal for scenarios in which resource usage is easy to predict. For more information, see [Overview](https://www.alibabacloud.com/help/en/oss/resource-plan/#concept-l43-j4h-tdb).

-

Storage capacity units (SCUs): You can use SCUs to offset storage fees that are generated for using OSS and other Alibaba Cloud storage services. For more information, see [SCUs](https://www.alibabacloud.com/help/en/oss/scu#concept-2005963).


> NOTE:

> NOTE: 


> NOTE: Note 

-

Compared with the pay-as-you-go billing method, resource plans and SCUs are more cost-effective.

-

Each resource plan and SCU has a quota for resource usage. If your resource usage exceeds the quota, you are charged for the excess resource usage based on the pay-as-you-go billing method. We recommend that you purchase resource plans and SCUs based on your workloads and business scale.


## Related services


You can use other Alibaba Cloud services to process data uploaded to OSS.


The following services are commonly used with OSS:


-

Image processing (IMG): allows you to perform a variety of operations on images in OSS, such as format conversion, resizing, cropping, rotation, and watermarking. For more information, see [IMG implementation modes](https://www.alibabacloud.com/help/en/oss/user-guide/img-implementation-modes#concept-m4f-dcn-vdb).

-

Elastic Compute Service (ECS): a cloud computing service that offers elastic and efficient computing. For more information, visit the [ECS product page](https://www.alibabacloud.com/product/ecs).

-

Alibaba Cloud CDN: allows you to cache OSS resources to Alibaba Cloud points of presence (POPs) that are geographically closer to your users to improve their download experience. For more information, visit the [CDN product page](https://www.alibabacloud.com/product/cdn).

-

E-MapReduce (EMR): a big data processing solution built on ECS. EMR is developed based on open source Apache Hadoop and Apache Spark to facilitate data analysis and processing. For more information, visit the [EMR product page](https://www.alibabacloud.com/product/emapreduce).


-

Data Online Migration: allows you to migrate data from a third-party storage service such as AWS and Google Cloud to OSS with ease. For more information, see the [Data Online Migration documentation](https://www.alibabacloud.com/help/product/94157.htm).

-

Data Transport: helps you migrate large amounts of data to OSS under limited network conditions. For example, you can use Data Transport to migrate petabyte-scale data to OSS when upload speed is slow and hardware expansion costs are high. For more information, see [What is Data Transport?](https://www.alibabacloud.com/help/en/data-transport/product-overview/what-is-data-transport#topic574)

## Other Alibaba Cloud storage services


In addition to OSS, Alibaba Cloud provides other storage services, such as File Storage NAS (NAS) and Elastic Block Storage (EBS), that you can use to meet different business scenarios. For more information, see [Overview](https://www.alibabacloud.com/help/en/aibaba-cloud-storage-services/latest/alibaba-cloud-storage-service-overview-overview#concept-1305535).


For more information about Alibaba Cloud storage solutions and customer success stories, visit the [Alibaba Cloud storage page](https://www.alibabacloud.com/product/storage).

Thank you! We've received your  feedback.