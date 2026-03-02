# OSS limits and performance metrics

This topic describes the limits and performance metrics for Object Storage Service (OSS).

## Bandwidth


The following table lists the maximum bandwidth for a single Alibaba Cloud account in each region.

















| Region | Total download bandwidth (internal and public) | Public download bandwidth | Total upload bandwidth (internal and public) | Public upload bandwidth |
| --- | --- | --- | --- | --- |
| China (Shanghai) | 100 Gbps | 10 Gbps | 20 Gbps | 10 Gbps |
| China (Shenzhen) | 100 Gbps | 10 Gbps | 20 Gbps | 10 Gbps |
| China (Beijing) | 100 Gbps | 10 Gbps | 20 Gbps | 10 Gbps |
| China (Hangzhou) | 100 Gbps | 20 Gbps | 20 Gbps | 20 Gbps |
| Singapore | 100 Gbps | 5 Gbps | 20 Gbps | 5 Gbps |
| China (Zhangjiakou) | 20 Gbps | No separate limit. This is constrained by the total download bandwidth. | 20 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| China (Nanjing - Local Region) (Closing Down) | 2 Gbps | No separate limit. This is constrained by the total download bandwidth. | 2 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| China (Fuzhou - Local Region) (Closing Down) | 2 Gbps | No separate limit. This is constrained by the total download bandwidth. | 2 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| China (Wuhan - Local Region) | 2 Gbps | No separate limit. This is constrained by the total download bandwidth. | 2 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| South Korea (Seoul) | 2 Gbps | No separate limit. This is constrained by the total download bandwidth. | 2 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| Thailand (Bangkok) | 2 Gbps | No separate limit. This is constrained by the total download bandwidth. | 2 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| Other regions in the Chinese mainland | 10 Gbps | No separate limit. This is constrained by the total download bandwidth. | 10 Gbps | No separate limit. This is constrained by the total upload bandwidth. |
| Other regions outside the Chinese mainland | 5 Gbps | No separate limit. This is constrained by the total download bandwidth. | 5 Gbps | No separate limit. This is constrained by the total upload bandwidth. |


If the threshold is reached, requests are throttled. When a request is throttled, the response header contains `x-oss-qos-delay-time: number`. In this header, `number` indicates the throttling duration in milliseconds. For upload requests, the header returns the exact throttling duration. For download requests, the header returns an estimated throttling duration based on the throttling level and file size.


Requests from OSS background tasks, such as lifecycle rules, cross-region replication, Same-region replication (SRR), and last access time updates, do not consume your account's QPS and bandwidth quotas. Only read, write, and delete operations initiated using temporary credentials from AssumeRole are counted. For example, the automatic deletion of expired objects by a lifecycle policy does not use your account's QPS quota for delete operations. The cross-region replication feature has a separate QPS quota that is independent of your account's QPS quota.

## Queries per second (QPS)


A single Alibaba Cloud account supports up to 10,000 queries per second (QPS). The actual maximum QPS varies based on the read and write mode:








| Read/write mode | QPS |
| --- | --- |
| Sequential read/write | 2,000 |
| Non-sequential read/write | 10,000 |


The maximum total QPS for single-file uploads and downloads is 2,000, and the peak bandwidth cannot exceed 10 Gbps. These operations are also subject to the bandwidth and QPS limits of your Alibaba Cloud account in each region and for the specific bucket.


If you upload many files with names that have sequential prefixes, such as timestamps or alphabetical characters, the indexes for these files may be concentrated in a specific partition of the bucket. If the request rate is too high, performance may degrade. We recommend that you avoid using sequential prefixes for file names when you upload many files. For more information about how to change sequential prefixes to random prefixes, see [OSS performance best practices](https://www.alibabacloud.com/help/en/oss/user-guide/oss-performance-best-practices/#concept-xtt-pln-vdb).

## Bucket


-

An Alibaba Cloud account can have up to 100 buckets in a single region. If your business requires more buckets, you can submit a request in [Quota Center](https://quotas.console.alibabacloud.com/products/oss/quotas).

-

Bucket names must be globally unique within OSS. For more information about naming conventions, see [Bucket naming conventions](https://www.alibabacloud.com/help/en/oss/user-guide/bucket-naming-conventions#concept-2085565).

-

After a bucket is created, you cannot change its name, region, or storage class.

-

There is no limit on the capacity of a single bucket.

## Object


-

Object size for uploads


The size of a single object uploaded using [simple upload](https://www.alibabacloud.com/help/en/oss/user-guide/simple-upload#concept-bws-3bb-5db), [form upload](https://www.alibabacloud.com/help/en/oss/user-guide/form-upload#concept-uln-lcb-5db), or [append upload](https://www.alibabacloud.com/help/en/oss/user-guide/append-upload-11#concept-ls5-yhb-5db) cannot exceed 5 GB.


The size of a single object uploaded using [multipart upload](https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload#section-k5c-lgp-mgb) cannot exceed 48.8 TB.

-

Renamed file size


In the OSS console, you can rename only objects that are 1 GB or smaller. To rename objects larger than 1 GB, use an SDK or the ossutil command line interface. For more information, see [Rename objects](https://www.alibabacloud.com/help/en/oss/user-guide/rename-objects#task-mn1-cdj-1fb).

-

Number of files to delete


You can delete up to 100 objects at a time in the OSS console or up to 1,000 objects using an SDK. There is no limit on the number of objects that you can delete at a time when using the ossutil command line interface or the ossbrowser graphical tool.


> WARNING:

> NOTE: 


> NOTE: Warning 

Deleted objects cannot be recovered. Proceed with caution.


-

Files with the same name will be overwritten.


By default, if you upload an object with the same name as an existing object, the existing object is overwritten.


> WARNING:

> NOTE: 


> NOTE: Warning 

Overwritten objects cannot be recovered. Proceed with caution. To prevent objects from being accidentally overwritten, you can enable versioning for the bucket where the objects are stored, or include the x-oss-forbid-overwrite header in the upload request and set its value to true.


## Restoring Data


To access data in the Archive Storage (if real-time access of Archive objects is not enabled), Cold Archive, or Deep Cold Archive storage classes, you must first restore the data. A higher restoration priority results in a shorter restoration time and higher data retrieval fees. For more information, see [Data retrieval fees](https://www.alibabacloud.com/product/oss/pricing).











-


-


-


-


-


| Storage Class | Restoration time | Restore quota |
| --- | --- | --- |
| Archive | Typically 1 minute. | Not applicable |
| Cold Archive | Expedited: Restoration is typically complete within 1 hour.Standard: Restoration is typically complete within 2 to 5 hours.Bulk: Restoration is typically complete within 5 to 12 hours. | For a single Alibaba Cloud account in a single region, the reference restoration quota for Cold Archive objects is an average of 500 objects per second. The total daily restoration quota across all three priorities is 100 TB to 120 TB. |
| Deep Cold Archive | Expedited: Restoration is typically complete within 12 hours.Standard: Restoration is typically complete within 48 hours. | For a single Alibaba Cloud account in a single region, the reference restoration quota for Deep Cold Archive objects is an average of 100 objects per second. The total daily restoration quota across both priorities is 10 TB to 15 TB. |


If you exceed the reference restoration quotas for Cold Archive and Deep Cold Archive, you can still submit restoration requests. The requests are queued, and the restoration may take longer than the time specified for the chosen priority.

## Domain name binding


-

Domain names bound to buckets in regions in the Chinese mainland must have an ICP filing from the MIIT. This is not required for buckets in other regions.

-

A domain name can be bound to only one bucket. A bucket can have up to 100 domain names bound to it.

-

You can attach an unlimited number of domain names to a single account.

## Lifecycle rules


-

You can configure up to 1,000 lifecycle rules for a bucket.

-

Completion time:


-

After a rule takes effect, lifecycle operations such as object deletion, storage class transition, and expiration of multipart upload parts are typically completed within 24 hours for up to 1 billion objects in the China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), and Singapore regions. In other regions, these operations are typically completed within 24 hours for up to 100 million objects.

-

Execution may take longer than 24 hours, and in some cases several days or weeks, if there are many objects to scan, many objects to which the lifecycle rule applies, numerous tags, multiple versions for a single object, or a high volume of new objects being uploaded while the lifecycle task is running.


> NOTE:

> NOTE: 


> NOTE: Note 

If versioning is enabled for the bucket, an operation on each version of an object is counted as a separate operation.


## Back-to-origin rules


-

You can configure up to 20 back-to-origin rules for a bucket.

-

For mirroring-based back-to-origin, the default QPS is 2,000 and the default bandwidth is 2 Gbps in regions in the Chinese mainland and the China (Hong Kong) region. In other regions, the default QPS is 1,000 and the default bandwidth is 1 Gbps.

## Image processing


-

Image limits


-

Source images


-

Supported formats are JPG, PNG, BMP, GIF, WebP, TIFF, HEIC, and AVIF.

-

The source image cannot exceed 20 MB.

-

For rotation, the height or width of the source image cannot exceed 4,096 pixels. For other operations, the height or width cannot exceed 30,000 pixels, and the total number of pixels cannot exceed 250 million.


The total number of pixels for a dynamic image, such as a GIF image, is calculated as `Width × Height × Number of frames`. The total number of pixels for a static image, such as a PNG image, is calculated as `Width × Height`.

-

Scaled image


Neither the width nor the height can exceed 16,384 pixels, and the total number of pixels cannot exceed 16,777,216.

-

Style limits


You can create up to 50 styles for each bucket.

-

Processing capacity limits


-

Image processing throughput per second (by source image size)


-

China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), and China (Shenzhen): 20 MB/s.

-

Other regions: 2 MB/s.

-

Queries per second (QPS)


-

China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), and China (Shenzhen): 50.

-

Other regions: 5.

## Resource plans


-

Region-specific resource plans can offset fees only in the region for which they are purchased.

-

You cannot change the region of a purchased resource plan.

-

You cannot use multiple storage plans concurrently. However, you can [upgrade](https://www.alibabacloud.com/help/en/oss/resource-plan/#section-nnt-zug-lsv) your purchased storage plan.

-

You can use multiple transfer acceleration plans concurrently. However, these plans cannot be upgraded or renewed.

-

You can use and renew multiple outbound data transfer plans and Anti-DDoS Basic plans concurrently. However, these plans cannot be upgraded.

-

[Request fees](https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees#concept-2558398), [Data processing fees](https://www.alibabacloud.com/help/en/oss/data-processing-fees#concept-2558464), and [Traffic fees](https://www.alibabacloud.com/help/en/oss/traffic-fees#concept-2558367) for cross-region replication traffic do not have a corresponding resource plan. Therefore, these fees are available only on a pay-as-you-go basis and do not support subscription.

Thank you! We've received your  feedback.