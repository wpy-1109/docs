# Overview of buckets

A bucket is the basic container that holds objects in Object Storage Service (OSS). A bucket has a flat structure where all objects are stored directly within it, and it does not have a directory hierarchy like a traditional file system.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/2010339571/CAEQThiBgICKtuKrzBkiIDBjMzRjODNiNWI4NTRkZDE5YjliNGFlYjhkNDJiZTQ54730938_20241025180808.849.svg)

Although the structure is flat, you can simulate folders in graphical tools, such as the OSS console and OSS Browser, using a forward slash (`/`) as a delimiter in object names. For example, `folder/file.jpg`.

## Key concepts


The key properties of a bucket are defined by the following concepts.

### Region


The region specifies the physical location of the data center where the bucket resides. The region of a bucket cannot be changed after it is created.

### Storage class


Select a storage class based on how frequently you access your data. This choice directly affects storage costs. If you are unsure, select Standard. You can later use [lifecycle](https://www.alibabacloud.com/help/en/oss/user-guide/overview-54/) rules to automatically move data to a more cost-effective storage class.























| Storage class | Key features | Typical scenarios |
| --- | --- | --- |
| Standard | Supports frequent read and write access. No minimum storage duration is required. | Dynamic business data for websites and applications. |
| Infrequent Access | For data with a lower access frequency. The minimum storage duration is 30 days. | Monitoring data, logs, and enterprise backups. |
| Archive Storage | For rarely accessed data, such as once a year. The minimum storage duration is 60 days. | Long-term archiving and medical imaging. |
| Cold Archive/Deep Cold Archive | For data that is almost never accessed. The minimum storage duration is 180 days. Data must be restored before it can be accessed. | Compliance data and historical image archives. |


For more information, see [Storage classes](https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#section-tbz-dt6-bg2) and [OSS Pricing](https://www.alibabacloud.com/product/oss/pricing).

### Storage redundancy type


The redundancy type determines the number of data replicas and the level of data reliability. For more information, see [Data redundancy types](https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/). You can upgrade a bucket from Locally Redundant Storage (LRS) to zone-redundant storage (ZRS), but you cannot downgrade a bucket from ZRS to LRS.

















| Redundancy type | Data reliability | Scenarios |
| --- | --- | --- |
| LRS (locally redundant storage) | 99.999999999% (11 nines) | Development and testing environments |
| ZRS (zone-redundant storage) | 99.9999999999% (12 nines) | Production environments |


## Basic operations 


> NOTE:

> NOTE: 


> NOTE: Note 

An Alibaba Cloud account can create a maximum of 100 buckets per region. A single bucket has no capacity limit.


-

[Create buckets](https://www.alibabacloud.com/help/en/oss/user-guide/create-a-bucket-4): Create a new bucket to store your objects.

-

[List buckets](https://www.alibabacloud.com/help/en/oss/user-guide/list-buckets-11): View a list of the buckets that you created.

-

[Get the region of a bucket](https://www.alibabacloud.com/help/en/oss/user-guide/query-the-regions-of-buckets-2): View the region where a bucket is located.

-

[Delete buckets](https://www.alibabacloud.com/help/en/oss/user-guide/delete-buckets): Delete a bucket that you no longer need.

-

[Bucket FAQ](https://www.alibabacloud.com/help/en/oss/ossfs-faq/): Find solutions to common problems.

## Access control


OSS provides a multi-layered access control model. The policies are enforced in the following order of precedence, from highest to lowest:


-

[Block Public Access](https://www.alibabacloud.com/help/en/oss/user-guide/block-public-access): A bucket-level setting that provides a simple way to block all public access. When enabled, it blocks all forms of public access by overriding any other permissions, such as access control lists (ACLs) or bucket policies, that might otherwise grant public access. This setting is enabled by default for all new buckets created in the console.

-

[Bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/): A resource-based authorization policy that grants fine-grained access permissions to your bucket and the objects within it to other accounts or anonymous users.

-

[RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/): A user-based authorization policy that controls which OSS resources Resource Access Management (RAM) users under your Alibaba Cloud account can access.

-

[Bucket ACL](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-acl): A simplified permission management method that provides three preset bucket-level permissions: private, public-read, and public-read-write.

## Scenario-specific configurations

### Ensure data security and compliance


To protect your data from unauthorized access and accidental leaks, use a combined strategy:


-

Keep [Block Public Access](https://www.alibabacloud.com/help/en/oss/user-guide/block-public-access) enabled as a fundamental security measure.

-

Use a [RAM policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) to grant least privilege access to internal users and applications.

-

Use [server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8) to protect static data.

-

Enable [log storage](https://www.alibabacloud.com/help/en/oss/user-guide/logging) to record all access requests for security audits and troubleshooting.

### Implement data disaster recovery and backup


To prevent data loss from accidental deletion or regional failures, you can configure the following features:


-

Prevent accidental deletion: Enable [versioning](https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/) to keep historical versions of objects. You can restore them at any time.

-

Automate backups: Use the [scheduled backup](https://www.alibabacloud.com/help/en/oss/user-guide/configure-scheduled-backup) feature to automatically back up your data every day.

### Reduce long-term storage costs


For data that is accessed less frequently over time, such as logs and backup files, you can use the [Lifecycle](https://www.alibabacloud.com/help/en/oss/user-guide/overview-54/) management feature. By setting rules, you can automatically transform data from Standard to Infrequent Access or Archive Storage, and then automatically delete the data after it expires. This process continuously optimizes your storage costs without manual intervention.

### Accelerate global user access


If your business serves a global user base, you can enable [transfer acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration) to improve upload and download speeds. This feature uses a global network of access points and optimized routes to accelerate data transfers across countries and regions. For static websites or distributing popular small files, you can use it with [CDN](https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration) to improve the access experience.

### Automate data processing and analytics


To automatically trigger downstream workflows after data is uploaded to OSS, you can use the [event notification](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-processing-file-changes-oss-event-notifications) feature. This feature sends notifications to a destination, such as Message Service (MNS) or Function Compute (FC), when events such as object creation or deletion occur. This lets you build event-driven data processing pipelines for tasks such as automated [image processing](https://www.alibabacloud.com/help/en/oss/user-guide/overview-17/), [video and audio processing](https://www.alibabacloud.com/help/en/oss/user-guide/introduction-2/), or data analytics.

Thank you! We've received your  feedback.