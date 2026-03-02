# Functions and features

## Data management


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/)


(https://www.alibabacloud.com/help/en/oss/back-to-origin-configuration-overview)


(https://www.alibabacloud.com/help/en/oss/user-guide/static-website-hosting-8)


(https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration)


(https://www.alibabacloud.com/help/en/oss/user-guide/create-a-bucket-4)


(https://www.alibabacloud.com/help/en/oss/user-guide/bucket-inventory#concept-2381539)


(https://www.alibabacloud.com/help/en/oss/user-guide/configure-a-resource-group)


(https://www.alibabacloud.com/help/en/oss/user-guide/enable-pay-by-requester-1)


(https://www.alibabacloud.com/help/en/oss/user-guide/delete-buckets)


(https://www.alibabacloud.com/help/en/oss/user-guide/manage-bucket-tags)


(https://www.alibabacloud.com/help/en/oss/user-guide/object-tagging-8)


(https://www.alibabacloud.com/help/en/oss/user-guide/upload-objects-to-oss/)


(https://www.alibabacloud.com/help/en/oss/user-guide/download-files/)


(https://www.alibabacloud.com/help/en/oss/user-guide/list-objects-18)


(https://www.alibabacloud.com/help/en/oss/user-guide/delete-objects-18)


(https://www.alibabacloud.com/help/en/oss/user-guide/copy-objects-16)


(https://www.alibabacloud.com/help/en/oss/user-guide/restore-objects-for-access)


(https://www.alibabacloud.com/help/en/oss/user-guide/rename-objects)


(https://www.alibabacloud.com/help/en/oss/user-guide/share-objects-by-url)


(https://www.alibabacloud.com/help/en/oss/user-guide/search-for-objects)


(https://www.alibabacloud.com/help/en/oss/user-guide/configure-symbolic-links)


(https://www.alibabacloud.com/help/en/oss/user-guide/manage-object-metadata-10/)


(https://www.alibabacloud.com/help/en/oss/user-guide/manage-directories)


(https://www.alibabacloud.com/help/en/oss/user-guide/scalar-retrieval/)


(https://www.alibabacloud.com/help/en/oss/user-guide/use-csg-to-attach-oss-buckets-to-ecs-instances)

| Category | Feature | Description | Reference |
| --- | --- | --- | --- |
| Storage classes | Standard | Standard provides highly reliable, highly available, and high-performance storage for frequently accessed data. | Standard |
| IA | Infrequent Access (IA) provides highly durable storage at lower prices compared with Standard. IA has a minimum billable size of 64 KB and a minimum billable storage duration of 30 days. IA is suitable for data that is infrequently accessed, such as data accessed once or twice a month. You can access IA objects in real time. You are charged data retrieval fees when you access IA objects. | IA |
| Archive | Archive provides highly durable storage at lower prices compared with Standard and IA. Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 60 days. You can access an Archive object after it is restored or real-time access of Archive objects is enabled. The amount of time that is required to restore an Archive object is approximately 1 minute. Archive is suitable for data that needs to be stored for a long period of time, such as archival data, medical images, scientific materials, and video footage. | Archive |
| Cold Archive | Cold Archive provides highly durable storage at lower prices compared with Archive. Cold Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 180 days. You must restore a Cold Archive object before you can access it. The amount of time that is required to restore a Cold Archive object varies based on the object size and the restoration mode. You are charged data retrieval fees and API operation calling fees when you restore a Cold Archive object. Cold Archive is suitable for cold data that needs to be stored for an extended period of time. | Cold Archive |
| Deep Cold Archive | Deep Cold Archive provides highly durable storage at lower prices compared with Cold Archive. Deep Cold Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 180 days. You must restore a Deep Cold Archive object before you can access it. The amount of time that is required to restore a Deep Cold Archive object varies based on the object size and restoration mode. You are charged data retrieval fees and API operation calling fees when you restore Deep Cold Archive objects. The storage cost of Deep Cold Archive is the lowest, but it takes a long period of time to restore Deep Cold Archive objects. | Deep Cold Archive |
| Bucket management | Mirroring-based back-to-origin | After you configure mirroring-based back-to-origin rules for a bucket, if a requested object does not exist in the bucket, Object Storage Service (OSS) retrieves the object from the origin specified by the back-to-origin rules. OSS returns the object retrieved from the origin to the requester and stores the object in the bucket. | Mirroring-based back-to-origin |
| Static website hosting | You can host a static website on your bucket and access the static website by using the domain name of the bucket. | Static website hosting |
| Transfer acceleration | OSS supports the transfer acceleration feature. The feature selects the optimal route and uses tuned protocol stacks to deliver content across geographical regions. This improves the access speed and reliability. | Transfer Acceleration |
| Create a bucket | A bucket is a container for objects in OSS. Before you upload an object to OSS, you must first create a bucket to store the object. You can configure various attributes for a bucket, including the region, access control list (ACL), and storage class. You can create buckets of different storage classes and store data in them based on your business requirements. | Create a bucket |
| Bucket inventory | You can configure inventories for buckets to export the metadata of specific objects, including the object sizes and encryption status. | Bucket inventory |
| Resource group | A resource group is a resource-based access control method. You can group your buckets based on your business requirements and configure different permissions for each resource group. This way, you can manage access to your buckets by group. | Use resource groups |
| Pay-by-requester | You can enable pay-by-requester for buckets. If pay-by-requester is enabled for a bucket, the requester is charged the request and traffic fees when the requester accesses objects in the bucket. The bucket owner is charged only the storage fees of the objects. You can enable pay-by-requester to share your data in OSS without additional fees. | Enable pay-by-requester |
| Delete a bucket | You can delete a bucket that you no longer use to reduce costs. | Delete buckets |
| Bucket tagging | You can classify and manage your buckets by using tags. You can use the bucket tagging feature to configure tags for buckets that are used for different purposes and configure ACLs for buckets that have specific tags. | Manage bucket tags |
| Object management | Object tagging | You can configure object tags to classify objects. Tags allow you to configure lifecycle rules and ACLs for objects that have the same tag. | Add tags to an object |
| Upload objects | Alibaba Cloud provides various methods to upload objects to OSS buckets. | Upload objects |
| Download objects | Alibaba Cloud provides various methods to download objects stored in OSS buckets. You can download objects to the default download path of your browser, or specify a directory to store the downloaded objects. | Download objects |
| List objects | By default, when you list objects in a bucket, the objects are returned in alphabetical order. You can list all objects, objects whose names contain a specific prefix, or a specific number of objects in a bucket. | List objects |
| Delete objects | You can delete one or more objects and parts at a time. You can also configure lifecycle rules to periodically delete expired objects to reduce storage costs. | Delete objects |
| Copy objects | You can copy an object from a source bucket to a destination bucket within the same region without modifying the content of the object. | Copy objects |
| Restore objects | You must restore an Archive, Cold Archive, or Deep Cold Archive object before you can access it. | Restore objects |
| Rename objects | You cannot rename objects by simply changing their keys. To rename an object in the bucket, you can call the CopyObject operation to copy the source object to the destination object and call the DeleteObject operation to delete the source object. | Rename objects |
| Share objects | You can share the URL of an object with third parties. This way, the third parties can download or preview the object. | Use object URLs |
| Search for objects | You can search for objects and directories that you want to access in a bucket. | Search for objects |
| Symbolic links | You can use symbolic links to access objects that are frequently accessed. A symbolic link points to an object and allows you to quickly access the object. Symbolic links are similar to shortcuts in Windows. | Create symbolic links |
| Manage object metadata | Information about objects stored in OSS includes keys, data, and object metadata. Object metadata describes object attributes. Object metadata includes standard HTTP headers and user metadata. You can use standard HTTP headers to specify HTTP request policies for an object, such as caching and forced download. You can also configure user metadata to identify the purposes or attributes of objects. | Manage object metadata |
| Manage directories | Compared with traditional file systems that use a hierarchical structure, data in OSS is stored as objects in a flat structure. All objects in OSS are stored in buckets. You can create simulated directories in OSS to help you categorize objects and manage access to your objects in a simplified manner. You can delete directories that you no longer need. | Manage directories |
| Data indexing | OSS provides the data indexing feature to allow you to query objects that match specific metadata conditions, such as the name, Etag, storage class, size, and last modified time of objects. The data indexing feature sorts and aggregates the query results based on your business requirements. This improves the efficiency of querying specific objects from a large number of objects. | Data indexing |
| Use CSG to attach OSS buckets to ECS instances | To allow multiple users to access data in an OSS bucket in different locations by using different devices as they access local files, you can use Cloud Storage Gateway (CSG) to attach the OSS bucket to an Elastic Compute Service (ECS) instance and then map the bucket to a local directory. This way, you can manage OSS objects in the same manner as you manage local files and share objects. | Use CSG to attach OSS bucket to ECS instance |


## Data security and protection


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-acl)


(https://www.alibabacloud.com/help/en/oss/user-guide/object-acl)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/)


(https://www.alibabacloud.com/help/en/oss/user-guide/hotlink-protection)


(https://www.alibabacloud.com/help/en/oss/user-guide/cors-settings)


(https://www.alibabacloud.com/help/en/oss/user-guide/zrs)


(https://www.alibabacloud.com/help/en/oss/user-guide/crr)


(https://www.alibabacloud.com/help/en/oss/user-guide/srr/)


(https://www.alibabacloud.com/help/en/oss/versioning-6)


(https://www.alibabacloud.com/help/en/oss/user-guide/rtc)


(https://www.alibabacloud.com/help/en/oss/user-guide/configure-scheduled-backup)


(https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8)


(https://www.alibabacloud.com/help/en/oss/user-guide/client-side-encryption)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-retention-policies)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-ddos-protection)


(https://www.alibabacloud.com/help/en/oss/user-guide/logging)


(https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/)

| Category | Feature | Description | Reference |
| --- | --- | --- | --- |
| Access control | Bucket ACL | To implement coarse-grained access control on a bucket, such as the same read/write permissions on all objects in the bucket, configure the ACL of the bucket. The ACL of a bucket can be public-read, public-read-write, or private. You can configure the ACL of a bucket when you create the bucket or modify the ACL of an existing bucket based on your business requirements. | Bucket ACLs |
| Object ACL | You can grant the read and write permissions on a specific object in a bucket by configuring the ACL of the object. An object ACL allows you to control permissions on a specific object without affecting access permissions on other objects in the bucket. The ACL of an object can be public-read, public-read-write, or private. You can configure the ACL of an object when you create the object or modify the ACL of an existing object based on your business requirements. | Object ACLs |
| Bucket policy | You can configure bucket policies to authorize access to resources in a bucket. You can use bucket policies to authorize one or more RAM users or RAM roles that belong to the current Alibaba Cloud account or other Alibaba Cloud accounts to access specific resources in a bucket. You can use the GUI or specify policy statements in the code editor to configure bucket policies for the bucket to accelerate authorization based on your business scenarios. | Bucket Policy |
| Hotlink protection | OSS allows you to configure a Referer-based filtering policy to block requests that contain specific Referers from accessing data in your bucket. This way, you can prevent unauthorized access and unexpected traffic fees. | Hotlink protection |
| CORS | Browsers enforce the same-origin policy, which allows JavaScript code executed on a web page to access resources only from the same origin and denies cross-origin requests. Cross-origin resource sharing (CORS) allows web browsers to initiate requests from a domain or an origin to a different domain or origin. CORS allows JavaScript code loaded on your websites to successfully request objects that have a different origin. | CORS |
| Data protection | ZRS | Zone-redundant storage (ZRS) stores multiple copies of your data across multiple zones in the same region. If one zone becomes unavailable, you can access the data that is stored in other zones. ZRS provides 99.9999999999% (12 nines) data durability. | Create a ZRS bucket |
| CRR | Cross-region replication (CRR) allows you to automatically and asynchronously (in near real-time) replicate objects from a bucket in one region to a bucket in a different region within the same account or a different account. CRR synchronizes operations such as object creation, overwriting, and deletion to help meet compliance, latency, security, and availability requirements. | CRR |
| SRR | SRR replicates objects across buckets within the same region in an automatic and asynchronous (near real-time) manner. Operations, such as the creation, overwriting, and deletion of objects, can be replicated from a source bucket to a destination bucket. | SRR overview |
| Versioning | OSS allows you to enable versioning for a bucket to protect objects that are stored in the bucket. After you enable versioning for a bucket, existing objects in the bucket are stored as previous versions when they are overwritten or deleted. If you accidentally delete or overwrite an object, you can recover the object to a previous version. | Versioning |
| RTC | The Replication Time Control (RTC) feature provided by OSS can meet your compliance requirements or business requirements for CRR. After the RTC feature is enabled, OSS replicates most of the objects that you uploaded to OSS within a few seconds and replicates 99.99% of the objects within 10 minutes. In addition, the RTC feature provides near real-time monitoring of data replication. After you enable the RTC feature, you can view various metrics of replication tasks. | RTC |
| Scheduled backup | To prevent data loss and data damage caused by accidental deletion, modification, and overwriting, you can use the scheduled backup feature to periodically back up objects in a bucket to Cloud Backup. In cases of accidental object loss, you can restore lost objects from Cloud Backup. Cloud Backup allows you to configure flexible backup policies to back up data to the cloud. You can view your backups and use them to restore data at any time. | Configure scheduled backup |
| Security and compliance | Server-side encryption | OSS encrypts objects uploaded to a bucket for which server-side encryption is configured and stores the encrypted objects. When you call the GetObject operation to download an object, OSS decrypts and returns the object. The x-oss-server-side-encryption header is contained in the response to indicate that the object is encrypted on the server side. | Server-side encryption |
| Client-side encryption | If client-side encryption is enabled, objects are locally encrypted before they are uploaded to OSS. Only the owner of the customer master key (CMK) can decrypt the objects. This improves data security during data transmission and storage. | Client-side encryption |
| Retention policies | The Write Once Read Many (WORM) feature of retention policies in OSS allows you to prevent users from modifying or deleting data. If you do not want anyone, including resource owners, to modify or delete objects in a bucket within a specific period of time, you can configure a retention policy for the bucket. After you configure a retention policy, users can only read the objects in or upload objects to the bucket until the retention period ends. You can modify or delete objects after the retention period ends. | Retention policies |
| OSS DDoS protection | OSS DDoS protection is a proxy-based attack mitigation service that integrates OSS with Anti-DDoS Proxy. When a bucket for which OSS DDoS protection is enabled suffers a DDoS attack, OSS DDoS protection diverts incoming traffic to an Anti-DDoS instance for scrubbing and then redirects normal traffic to the bucket. This ensures the continuity of your business in the event of DDoS attacks. | OSS DDoS protection |
| Logging | OSS generates access logs to record access to resources stored in OSS buckets. After you enable and configure logging for a bucket, OSS generates logs on an hourly basis based on predefined naming conventions and then stores the logs in a specific bucket. You can use Simple Log Service or build a Spark cluster to analyze the logs. | Logging |
| Real-time log query | OSS generates access logs to record access to resources stored in OSS buckets. OSS uses Simple Log Service to help you query and collect statistics for OSS access logs and audit access to OSS in the OSS console, track exception events, and troubleshoot problems. This helps you improve work efficiency and make informed decisions. | Real-time log query |


## Data processing


(https://www.alibabacloud.com/help/en/oss/user-guide/query-objects)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs/)


(https://www.alibabacloud.com/help/en/oss/user-guide/latest-version-of-img-guide)


(https://www.alibabacloud.com/help/en/oss/user-guide/zip-package-decompression)


(https://www.alibabacloud.com/help/en/oss/user-guide/event-notifications/)

| Category | Feature | Description | Reference |
| --- | --- | --- | --- |
| Data lake | OSS Select | You can call the SelectObject operation to execute SQL statements on an object and obtain the execution results. | Query objects |
| OSS-HDFS | OSS-HDFS (JindoFS) is a cloud-native data lake storage feature. OSS-HDFS provides centralized metadata management capabilities and is fully compatible with Hadoop Distributed File System (HDFS) API. You can use OSS-HDFS to manage data in data lake-based computing scenarios in the big data and AI fields. | OSS-HDFS |
| Data processing | IMG | You can add Image Processing (IMG) parameters to GetObject requests to process image objects stored in OSS. For example, you can add image watermarks to images or convert image formats. | IMG |
| ZIP package decompression | If you want to upload multiple objects at a time, upload objects with the original directory structure retained, upload a complete list of objects, or assign resources to objects, you can configure a ZIP package decompression rule and upload ZIP objects to the specified directory in an OSS bucket. Function Compute automatically decompresses ZIP objects based on the decompression rule and returns the decompressed data to the specified directory in OSS. | ZIP package decompression |
| Event notifications | You may want to monitor changes to objects in OSS for various reasons, such as real-time processing, synchronization, listening, business logic triggers, and logging. You can configure event notification rules to monitor objects and receive notifications so that you can act accordingly at the earliest opportunity. | Event notifications |


## Tools


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-1)


(https://www.alibabacloud.com/help/en/oss/developer-reference/graphical-management-tools-ossbrowser-1-0/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossftp)

| Category | Feature | Description | Reference |
| --- | --- | --- | --- |
| Client management | ossutil | ossutil allows you to manage OSS data by using command lines on Windows, Linux, and macOS operating systems. | ossutil |
| ossbrowser | ossbrowser is a graphical management tool that is provided by Alibaba Cloud to help you easily manage buckets and objects in OSS. For example, you can use ossbrowser to create buckets, delete buckets, upload objects, download objects, preview objects, copy objects, move objects, and share objects. | ossbrowser |
| Access by mounting and mapping | ossfs | ossfs allows you to mount an Object Storage Service (OSS) bucket to a local directory on a Linux system so that your application can access resources in the bucket as if they were local resources. The mount feature facilitates resource sharing. | ossfs |
| ossftp | ossftp is an FTP server tool based on Alibaba Cloud OSS. ossftp maps operations related to files and directories to those on OSS objects and directories. This way, you can manage objects stored in OSS over FTP. | ossftp |


Thank you! We've received your  feedback.