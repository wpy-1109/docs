# OSS accelerator

As workloads such as AI, data warehousing, and big data analytics evolve, the demands for lower access latency, higher queries per second (QPS), and greater throughput for data stored on OSS have significantly increased. To meet these stringent requirements, OSS accelerator caches frequently accessed objects on high-performance NVMe SSDs co-located with your compute services in the same Availability Zone, delivering a data access service characterized by low, millisecond-level latency and high QPS.

## Benefits


-

Low latency


The NVMe SSD media of an accelerator can provide millisecond-level download latency for business. The accelerator provides better performance for hot data query in data warehouses and inference model download.

-

High IOPS


The accelerator can provide high throughput for a small amount of data and meet the burst read requirements for a small amount of hot data.

-

Increased throughput


The bandwidth of an accelerator increases linearly together with the cache capacity of the accelerator and provides burst throughput of up to hundreds of Gbit/s.

-

Automatic scaling


In most cases, computing tasks are periodic tasks that have different requirements for the amount of required resources. You can scale up or scale down the cache capacity of the accelerator based on your requirements without interrupting your business. This helps reduce resource waste and costs. The accelerator supports at least 50 GB of cache capacity and up to 100 TB of cache capacity. The accelerator inherits the advantages of OSS massive data storage and can directly cache multiple tables or partitions in a data warehouse.

-

Decoupled storage and computing


Compared with the cache capacity of the computing server, the accelerator can be independent of the computing server and you can change the cache capacity and performance of the accelerator online without interrupting your business.

-

Data consistency


Compared with conventional cache solutions, the OSS accelerator feature ensures data consistency. When you update objects in OSS buckets, the accelerator automatically identifies and caches the latest versions of the objects to ensure that the computing engines can read the latest versions of the objects.

-

Multiple warmup policies


The accelerator can automatically identify objects that are updated on OSS to ensure that the engine can read the latest data. The accelerator provides the following warmup policies:


-

Warmup during read: If the data that you request does not hit the cache, the accelerator automatically retrieves data from the bucket in which the data is stored and caches the data to the accelerator.

-

Synchronous warmup: When data is written to OSS, data is synchronized and cached on the accelerator.

-

Asynchronous warmup: You can configure parameters to batch cache data in OSS to the OSS accelerator.


> NOTE:

> NOTE: 


> NOTE: Note 

-

By default, warmup during read is enabled and cannot be configured.

-

If you want to enable synchronous warmup or asynchronous warmup, you must manually enable it. Synchronous warmup and asynchronous warmup can be enabled at the same time.


## How it works


After an accelerator is created, it has an internal accelerated endpoint that is dedicated to the region. You can access the resources cached in the accelerator only over an internal network. For example, the accelerated endpoint for the China (Beijing) region is `http://cn-beijing-internal.oss-data-acc.aliyuncs.com`. If you are located in the same virtual private cloud (VPC) as the accelerator, you can use the accelerated endpoint to access the resources that are cached on the accelerator. The following figure shows how the accelerated endpoint is used to access the resources that are cached on the accelerator.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7277915671/CAEQMhiBgIDWgoiUoRkiIGM3ZTA5MTI5ZjI1ZDQxODI4YjZkNDdmMTA1YzQ1MmY13963382_20230830144006.372.svg)

-

Write requests


-

Warmup during read: Write requests that are sent from a client to the accelerated endpoint of the accelerator are forwarded to OSS buckets. This process is similar to the process in which the default domain names of OSS buckets are used.

-

Synchronous warmup: Write requests that are sent from a client to the accelerated endpoint are forwarded to OSS buckets and the OSS accelerator.

-

Asynchronous warmup: Data that needs to be warmed up is written to the OSS accelerator in advance before read requests are forwarded.

-

Synchronous warmup + asynchronous warmup: Requests are forwarded to OSS buckets and the OSS accelerator. The hot data is written to the OSS accelerator in advance before read requests are forwarded.

-

Read requests


> NOTE:

> NOTE: 


> NOTE: Note 

Read requests are handled in the same manner in different warmup policies.


-

Read requests that are sent from a client to the accelerated endpoint are forwarded to the accelerator.

-

When the accelerator receives the read requests, the accelerator searches for the requested objects in the cache.


-

If the requested objects are cached on the accelerator, the objects are returned to the client.

-

If the requested objects are not cached on the accelerator, the accelerator requests the objects from the OSS buckets that are mapped to the accelerator. After OSS receives the requests, OSS caches the requested objects in the accelerator. Then, the accelerator returns the objects to the client.

-

If the cache capacity of the accelerator is exhausted, the accelerator prioritizes the cached objects that are accessed with relatively high frequency.

## Scenarios


The OSS accelerator feature is suitable for scenarios in which high bandwidth is required and data is repeatedly read. Examples:

### Low-latency data sharing


-

Background information


When a customer purchases goods from a vending machine, the customer uses a mobile app to scan the goods in the container, take a picture, and upload the picture. After the application backend receives the picture, the accelerator stores the picture. The background subsystem then performs content moderation analysis and barcode recognition on the picture, and the results of barcode recognition are returned to the application backend for fee deduction and other operations. The picture must be downloaded within milliseconds.

-

Solution


Use the synchronous warmup policy of the accelerator. The accelerator can effectively reduce the latency of loading pictures to the analysis system and shorten transaction links. The OSS accelerator feature is suitable for business that is sensitive to latency and in which data is repeatedly read.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7277915671/CAEQMhiBgMDVxMyToRkiIDYxYzEwYTMxZmYxYzQ1ODc5ZmM1ZmZlYTAwNTcwNWZm3963382_20230830144006.372.svg)
### Model inference


-

Background information


The inference server needs to pull and load model objects for AI-generated content (AIGC) model inference. During inference and debugging, the inference server also needs to constantly switch between new model objects. As the size of the model objects increases, a longer period of time is required to allow the inference server to pull and load the model objects.

-

Solution


Use the asynchronous warmup policy or the warmup during read policy of the OSS accelerator feature. The asynchronous warmup policy of the OSS accelerator feature is suitable for scenarios in which you can determine the list of hot model objects. The warmup during read policy is suitable for scenarios in which you cannot determine the list of hot model objects. If you can determine the list of hot model objects, you can configure an accelerator of a specific cache capacity and use the accelerator SDK to store the objects in the accelerator in advance. You can also configure an accelerator of a specific cache capacity based on previous experience. The accelerator automatically caches model objects to the high-performance media of the accelerator when data is read for quick access in subsequent reads. The cache capacity of the accelerator can be scaled at any time based on your acceleration requirements. If your inference server needs to access OSS from a local directory, you must deploy [ossfs](https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs).
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7277915671/CAEQMhiBgMCxxsyToRkiIDI0YWQzNTZkY2NkZjQ5ZDViMWI4Y2NmNWNjYTk1YTdj3963382_20230830144006.372.svg)
### Big data analysis


-

Background information


The company's business data is partitioned by day and stored in OSS for a long period of time. Analysts use computing engines, such as Hive or Spark, to analyze data, but they are not sure about the query range. The analysts are required to reduce the amount of time that is required for query and analysis.

-

Solution


Use the warmup during read policy of the OSS accelerator feature. This policy is suitable for offline query scenarios in which a large amount of data is stored, the data query range is uncertain, and the data cannot be accurately warmed up. For example, the data queried by Analyst A is cached in an acceleration cluster. If the data queried by Analyst B contains the data queried by Analyst A, data analysis is accelerated.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7277915671/CAEQMhiBgMCv1oiUoRkiIDBiZjcyNGJiZDMwNTQ4YzI4NjA5MjY3NWE1MzliODM13963382_20230830144006.372.svg)
### Multi-level acceleration


-

Background information


No conflict exists between client-side caching and server-side acceleration. You want to achieve multi-level acceleration based on your business requirements.

-

Solution


Use the OSS accelerator together with the client-side cache. We recommend that you deploy Alluxio together with computing clusters. If the data that you want to read does not match data in the Alluxio cache, the data is read from the backend storage. The OSS accelerator uses the warmup during read policy and warms up data the first time the data is read. Time to live (TTL) is configured for each object and directory in Alluxio due to the limits of the cache capacity of the client host. When the TTL period ends, the cache is deleted to save storage space. In this case, data in the OSS accelerator is not immediately deleted, and its cache capacity can store hundreds of TB of data. When data that does not match data in the Alluxio cache is read again, the data can be directly loaded from the OSS accelerator to implement two-level acceleration.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7277915671/CAEQMhiBgMC3gouUoRkiIDhlNDVmYmIzYjU3ZTRkYjk5NWRhNTlhN2YwZjFlNTc03963382_20230830144006.372.svg)
## Metric description


-


-


(https://smartservice.console.alibabacloud.com/#/ticket/createIndex)


(https://www.alibabacloud.com/help/en/oss/user-guide/limits)


-


-


(https://smartservice.console.alibabacloud.com/#/ticket/createIndex)


| Metric | Description |
| --- | --- |
| Cache capacity | After public preview: up to 100 TBDuring public preview: up to 500 GBIf your business requires a greater cache capacity, submit a ticket. |
| Accelerator throughput | The accelerator provides throughput bandwidth for data cached on the accelerator based on the configured cache capacity. The accelerator provides a throughput of up to 2.4 Gbit/s for 1 TB of cache capacity of the accelerator. The throughput provided by the accelerator is not limited by the standard throughput provided by OSS. For more information about the standard bandwidth limits of OSS, see Limits and performance metrics. For example, OSS provides a standard bandwidth of 100 Gbit/s in the China (Shenzhen) region. After you enable the OSS accelerator feature and create an accelerator that has a cache capacity of 10 TB, you can obtain an additional 24 Gbit/s of low-latency throughput provided by the accelerator if you use the accelerated endpoint of the accelerator to access data cached on the accelerator. For batch offline computing applications, you can take advantage of the 100 Gbit/s of standard throughput for large-scale concurrent block read if you use an OSS internal endpoint. For hot data query service, you can obtain an additional 24 Gbit/s of low-latency throughput if you use the accelerated endpoint of the accelerator to access data cached on the NVMe SSD media of the accelerator. |
| Peak read bandwidth | Formula: MAX[600,300 × Cache capacity (TB)] MB/sMAXindicates that the larger value within the brackets is used. The basic bandwidth is 600 MB/s, which indicates that at least 600 MB/s of bandwidth is provided regardless of the cache capacity. 300 x Cache capacity (TB) is the bandwidth that increases linearly together with the cache capacity. For example, if an accelerator provides a cache capacity of 2,048 GB (2 TB), the read bandwidth is 600 MB/s. |
| Maximum read bandwidth | 40 GB/sIf your business requires a greater read bandwidth, submit a ticket. |
| Minimum latency for reading 128 KB of data in a single request | <10 ms |
| Scale-up or scale-down interval | Once per hour |
| Scale-up or scale-down method | Manually scale up or scale down in the OSS console |
| Cache deletion policy | The cache is deleted based on the Least Recently Used (LRU) algorithm. The LRU algorithm is used to ensure that frequently accessed data is retained, and data that is not accessed for a long period of time is preferentially deleted. In this case, the cache capacity is efficiently used. |


## Billing rules


-

The OSS accelerator feature is in public preview. During the public preview, up to 100 GB of cache capacity is provided free of charge. After the public preview ends, you are charged for the actual cache capacity of the accelerator based on the pay-as-you-go billing method.

-

When you use the accelerated endpoint of the accelerator to read data from and write data to OSS, you are charged OSS API operation calling fees even if origin fetch requests are not sent.


> NOTE:

> NOTE: 


> NOTE: Note 

For more information about how to query OSS billing data generated on an hourly basis, see [Hourly data of OSS](https://www.alibabacloud.com/help/en/oss/query-oss-billing-data-generated-on-an-hourly-basis#reference-2093072) and [Query bills](https://www.alibabacloud.com/help/en/oss/query-bills#task-2191459).


## What to do next


-

For more information about how to create an accelerator and modify the cache capacity of an accelerator, see [Create, modify, and delete accelerators](https://www.alibabacloud.com/help/en/oss/user-guide/create-accelerator#ff268bae99ix6).

-

For more information about how to configure and use the OSS accelerator feature together with OSS tools and OSS SDKs, see [Use OSS accelerator](https://www.alibabacloud.com/help/en/oss/user-guide/use-accelerator/#0607066e0cu7d).

-

For more information about the differences in performance when you access resources by using an OSS internal endpoint and an accelerator in specific business scenarios, see [Performance metrics](https://www.alibabacloud.com/help/en/oss/user-guide/performance-index).

Thank you! We've received your  feedback.