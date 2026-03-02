# Performance acceleration and management overview

Use transfer acceleration, CDN acceleration, Global Accelerator, and the OSS accelerator to quickly access resources. Optimize bandwidth usage and resource allocation with single-connection bandwidth throttling and resource pool Quality of Service (QoS) features to improve overall performance.

## Performance acceleration


(https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration)


(https://www.alibabacloud.com/help/en/oss/user-guide/user-global-accelerated-access-to-oss)


(https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-77/)


| Solution | Principle | Scenarios |
| --- | --- | --- |
| Accelerate OSS access using CDN | CDN caches static data from OSS on its globally distributed edge nodes. This accelerates access by allowing clients to retrieve data directly from the edge nodes. | This solution accelerates the download of static hot spot files and on-demand video/audio streaming. It is suitable for users on the Internet who access small and medium-sized files on websites or applications. |
| Global Accelerator access | A globally deployed smart routing system selects the optimal path based on the request's source and directs the request to the nearest access point. The Alibaba Cloud Global Accelerator network then provides a low-latency, high-bandwidth transmission path from the user to the OSS Bucket. This improves the speed and stability of data transfer. | Enterprise cross-border data sharing, global media content delivery, software updates, and cross-region real-time interactions, such as video conferencing, online education, and real-time data synchronization. This solution is suitable for cross-region applications on the Internet. |
| Accelerate OSS access using transfer acceleration | This solution uses globally distributed cloud data centers and smart routing to direct user requests to the nearest access point. It uses an optimized network and protocols to provide end-to-end acceleration for uploads and downloads over the Internet. | Accelerates long-distance data transfers for uploading and downloading large files (GBs or TBs) over the Internet. This solution is also used for the fast delivery of dynamic or non-hot spot data. |
| OSS accelerator | Hot spot files from OSS are cached on high-performance NVMe SSD storage. This provides a data access service with millisecond-level latency and high throughput. It supports three prefetch policies: read-time prefetch, synchronous prefetch, and asynchronous prefetch. | AI reasoning model downloads, hot data queries in data warehouses, big data analytics, and low-latency data sharing for internal network data access. |
| Accelerate OSS access using Elastic File Client (EFC) | Elastic File Client (EFC) mounts an OSS Bucket as a local file system and uses the memory and disks of compute nodes to build a distributed cache. Data is first read from the local cache with millisecond-level latency. On a cache miss, data is pulled from OSS and then cached. Multiple nodes share cached data over a P2P network to avoid repeated downloads. A single machine can reach 15 GB/s throughput and 200,000 input/output operations per second (IOPS). Performance scales linearly with the number of nodes. Active prefetching is supported, which loads data into the cache before a task starts. | This solution is suitable for scenarios with frequent reads of OSS data. For AI training, it accelerates the reading of large volumes of samples to improve GPU utilization. For AI reasoning, multiple nodes share model files over a P2P network to shorten cold start times. For big data analytics, it accelerates hot data queries for engines such as Spark and Presto. |


## Performance management


(https://www.alibabacloud.com/help/en/oss/user-guide/single-connection-bandwidth-throttling-4)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-resource-pool-qos)


| Solution | Principle | Scenarios |
| --- | --- | --- |
| Single-connection bandwidth throttling | Add the x-oss-traffic-limit parameter to a request and specify a speed limit value to throttle the upload or download speed of a single connection. The speed limit value ranges from 819,200 to 838,860,800 bit/s. This feature is supported in PutObject, AppendObject, PostObject, CopyObject, UploadPart, UploadPartCopy, and GetObject requests. | Preventing clients from using too much bandwidth, which can affect other applications. Also for multi-user shared environments, public resource access, and ensuring Quality of Service (QoS). |
| Resource pool QoS | Create resource pools and assign different resource quotas to various services for fine-grained management of OSS access. This feature supports bandwidth limits for Buckets, Bucket requesters, BucketGroups, and resource pool requesters. It also lets you set corresponding service quality guarantees. | Multiple services sharing OSS resources, guaranteeing performance for critical services, differentiated Quality of Service management, and large-scale multi-tenant environments. |


Thank you! We've received your  feedback.