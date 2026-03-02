# OSS performance best practices

This topic describes how to use the distributed architecture of Alibaba Cloud Object Storage Service (OSS) to accelerate data processing, reduce data latency, and shorten application response time. This topic aims to help you optimize OSS performance.

## Change sequential prefixes to random prefixes


To optimize data distribution and improve processing efficiency, we recommend that you use random prefixes instead of traditional sequential prefixes to name your objects. OSS automatically partitions data based on the UTF-8 encoding order of the key of the object to support large-scale object management and high-concurrency requests. However, if you use sequential prefixes, such as timestamps and alphabetical strings, a large number of objects are stored in a few partitions.


For example, if you perform operations more than 2,000 times per second, the following issues may occur. An operation performed on a single object, such as downloading, uploading, deleting, and copying of an object, or querying the metadata of an object, is counted as a request, whereas an operation performed on multiple objects, such as downloading and listing multiple objects, is counted as multiple requests.


-

Generation of hotspot partitions: Requests are frequently initiated for objects in specific partitions, which turns these partitions into hotspot partitions. As a result, the I/O capacity of the partitions is exhausted or the system automatically limits the request rate.

-

Limited request rate: OSS continuously partitions data in hotspot partitions to balance the distribution of the data among partitions. This process may increase the request processing time.


> NOTE:

> NOTE: 


> NOTE: Note 

The even distribution of data is performed based on the analysis result of system status and processing capability. Objects that use sequential prefixes in their keys may be stored in hotspot partitions after the preceding operation is performed.


To resolve these issues, you can change the sequential prefixes in the keys of the object to random prefixes to achieve the even distribution of object indexes and I/O loads among different partitions.


-

Specify a hexadecimal hash as the prefix in the key of an object


If you use dates and customer IDs to generate keys, sequential prefixes that use timestamps are included in the keys as shown in the following examples:


`java
sample-bucket-01/2024-07-19/customer-1/file1
sample-bucket-01/2024-07-19/customer-2/file2
sample-bucket-01/2024-07-19/customer-3/file3
...
sample-bucket-01/2024-07-20/customer-2/file4
sample-bucket-01/2024-07-20/customer-5/file5
sample-bucket-01/2024-07-20/customer-7/file6
...
`


In this case, you can use an MD5 hash of multiple characters of the customer ID as the object name prefix. If you use an MD5 hash of four characters of the customer ID as the object name prefix, the names of the objects are changed as shown in the following examples:


`java
sample-bucket-01/9b11/2024-07-19/customer-1/file1
sample-bucket-01/9fc2/2024-07-19/customer-2/file2
sample-bucket-01/d1b3/2024-07-19/customer-3/file3
...
sample-bucket-01/9fc2/2024-07-20/customer-2/file4
sample-bucket-01/f1ed/2024-07-20/customer-5/file5
sample-bucket-01/0ddc/2024-07-20/customer-7/file6
...
`


If you use a hexadecimal hash of four characters of the customer ID as the object name prefix, each character can be one of the 16 values (0-9 and a-f). This way, the total number of combinations of the four characters is 65,536 (16 4). In OSS, data can be continuously distributed to up to 65,536 partitions. You can perform up to 2,000 operations per second on each partition based on the performance bottleneck. You can use the request rate to determine whether the number of the hash of four characters that you use as the object name prefix meets your business requirements.


If you want to list the objects whose names contain a specific date, such as the objects whose names contain the 2024-07-19 string in a bucket named sample-bucket-01, you need to only call the ListObject operation multiple times to list the objects in the sample-bucket-01 bucket in batches, and then group the objects whose names contain the specified date.

-

Reverse the order of digits that indicate milliseconds in object names


If you use the UNIX timestamps which are accurate to milliseconds to generate object names, sequential prefixes are included in object names as shown in the following examples:


`java
sample-bucket-02/1513160001245.log
sample-bucket-02/1513160001722.log
sample-bucket-02/1513160001836.log
sample-bucket-02/1513160001956.log
...
sample-bucket-02/1513160002153.log
sample-bucket-02/1513160002556.log
sample-bucket-02/1513160002859.log
...
`


In this case, you can reverse the order of the digits in the UNIX timestamp. This way, the object names do not contain sequential prefixes. After you reverse the order of the digits, the object names are displayed as shown in the following examples:


`java
sample-bucket-02/5421000613151.log
sample-bucket-02/2271000613151.log
sample-bucket-02/6381000613151.log
sample-bucket-02/6591000613151.log
...
sample-bucket-02/3512000613151.log
sample-bucket-02/6552000613151.log
sample-bucket-02/9582000613151.log
...
`


The first three digits indicate milliseconds and 1,000 values are available. The fourth digit changes at an interval of 1 second. The fifth digit changes at an interval of 10 seconds. The reverse operation increases the randomness of prefixes. This way, requests are evenly distributed among each partition to prevent performance bottleneck issues.

## Initiate an HTTP Range request to obtain part of an object


When you download a large object whose size is greater than 100 MB from OSS, the download operation may fail due to an unstable network environment. If you want to download only part of the object, you can initiate an HTTP Range request. Example:


`javascript
Get /ObjectName HTTP/1.1
Host:examplebucket.oss-cn-hangzhou.aliyuncs.com
Date:Fri, 19 Jul 2024 17:27:45 GMT
Authorization:SignatureValue
Range:bytes=[$ByteRange]
`


According to the HTTP protocol specification, you can configure the Range request header to specify the range of the object that you want to download. The range must be within [0, `content-length - 1`]. For more information, see [How to Obtain OSS Resources by Segmenting HTTP Range Requests](https://www.alibabacloud.com/help/en/oss/how-to-obtain-oss-resources-by-segmenting-http-range-requests).

## Use transfer acceleration


You can enable transfer acceleration to speed up the upload and download of objects in a bucket over long distances. For example, if you are located in the Chinese mainland, you can enable transfer acceleration when you upload objects to or download objects from a bucket that is located outside the Chinese mainland. This way, the upload and download of gigabyte-size and terabyte-size objects are accelerated. The transfer acceleration feature provides an optimized end-to-end solution with data centers distributed across the world to accelerate access to OSS over the Internet. When the feature is enabled, requests destined for your bucket are routed to the data center nearest to users over the optimal network path and protocol. For more information, see [Transfer acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration).

## Cache frequently-accessed content


To accelerate access to frequently accessed objects in OSS, we recommend that you use Alibaba Cloud CDN. Alibaba Cloud CDN caches static content on points of presence (POPs) around the world. You can retrieve static content from the nearest POPs. This improves website access speed and stability.


When you request an object in OSS, Alibaba Cloud CDN first checks whether the object is cached on a POP. If the object is not cached or is expired, the object is requested from OSS and cached on a nearby POP. When the object in OSS changes, Alibaba Cloud CDN automatically updates the cache on the POP to ensure data consistency between OSS and the POP.


If you use the preceding solution, Alibaba Cloud CDN can effectively reduce the load on OSS and improve the website access speed and stability. This solution is especially suitable for enterprises whose users are located around the world. For more information, see [Access acceleration by using Alibaba Cloud CDN](https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration).

## Use the latest OSS SDKs


OSS SDKs provide built-in support for optimizing OSS performance. The following items describe how the latest OSS SDKs improve OSS performance:


-

Support for new features: In most cases, the latest OSS SDKs support the latest features and improvements. It can take advantage of the new features of OSS, such as the latest API operations, optimized algorithms, and more efficient coding methods to improve performance.

-

Error handling and retry mechanism: The latest OSS SDKs include a more complete error handling and retry mechanism that can automatically handle common errors, such as errors with HTTP status code 503 returned, to reduce the number of failed operations caused by network issues and improve the success rate.

-

Transmission management: The latest OSS SDKs provide a higher level of transmission management, which supports automatic scaling and properly uses range requests for efficient throughput.

-

Support for parallel threads: The latest OSS SDKs support a multi-thread programming model, which can process parallel requests and improve data processing speed.

-

Memory management optimization: To effectively use memory resources, the latest OSS SDKs have deeply optimized memory management to reduce unnecessary memory overheads and improve memory usage efficiency.

-

Compatibility improvement: The latest OSS SDKs are dedicated to resolving the historical issues and continuously improving compatibility with various third-party software libraries and operating systems.


For more information about how to obtain the latest OSS SDKs, see [Overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21).

## Use OSS and ECS in the same region


To take full advantage of OSS and Elastic Compute Service (ECS), we recommend that you deploy your ECS instances and OSS buckets within the same region. This deployment strategy can significantly reduce the latency of the data transmission and improve the data reading speed, thereby enhancing the overall performance of the application.
If your ECS instances and OSS buckets are located in the same region and communicate with each other by using internal endpoints, you are not charged internal network traffic fees. In this case, when you transfer large amounts of data between ECS instances and OSS buckets, you are not charged high network bandwidth fees, which reduces the overall costs.
For more information, see [Access to OSS resources from an ECS instance by using an internal endpoint of OSS](https://www.alibabacloud.com/help/en/oss/access-to-oss-resources-from-ecs-instances-by-using-an-internal-endpoint-of-oss).

## Configure latency-sensitive applications to automatically retry timeout requests


OSS throttles the queries per second (QPS) of management-related API operations, such as GetService (ListBuckets), PutBucket, and GetBucketLifecycle. If your application initiates a large number of requests at the same time, HTTP status code 503 may be returned to indicate that request throttling is triggered. In this case, we recommend that you retry the requests after a few seconds.


The total QPS of a single Alibaba Cloud account is 10,000. If you require a higher QPS, contact [technical support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex). Take note that if the overall QPS does not exceed 10,000 and the requests are sent to a specific partition, the server may automatically limit the request rate and return HTTP status code 503 because the I/O capacity of the partition is exhausted. If random prefixes in object names are used for even distribution of object indexes and I/O loads among different partitions, OSS automatically increases the number of partitions to support higher QPS. You need to only wait until the process is complete. For more information, see [OSS performance and scalability best practices](https://www.alibabacloud.com/help/en/oss/user-guide/oss-performance-best-practices/#concept-xtt-pln-vdb).


When you initiate a large number of requests for objects of different sizes, such as objects that are more than 128 MB in size, we recommend that you measure throughput and retry the slowest 5% of requests. In most cases, the responses to requests for objects that are smaller than 512 KB in size are returned within tens of milliseconds. If you need to retry GET or PUT requests, we recommend that you retry the requests 2 seconds after the requests are sent. If a request fails multiple times, we recommend that you close the program and retry the request. For example, you can retry a request 2 seconds after the request is sent and then retry the request after 4 seconds.


If the requests are sent by your application for objects of the same size and you want the response time of all requests to be consistent, we recommend that you identify and retry the slowest 1% requests. In this case, the response time of the requests can be reduced when the requests are retried.

## Send requests in a distributed and concurrent manner for high throughput


OSS is a large-scale distributed storage system. To fully utilize the throughput of OSS, we recommend that you send concurrent requests to OSS and distribute the requests across multiple OSS service nodes. This way, workloads can be distributed by using multiple network paths.


To increase throughput during data transmission, we recommend that you create multiple threads or instances and initiate multiple requests in the threads or instances to concurrently upload and download data. For specific applications, you can initiate multiple requests in different threads or instances to concurrently access OSS. You can determine how to distribute requests based on the architecture of your application and the structure of objects that you want to access.


Before you change the number of concurrent requests, you need to check the performance metrics. We recommend that you first check the bandwidth usage and other resources that are consumed by a single request. This helps you identify resources with the highest usage and determine the maximum number of concurrent requests that can be processed based on the resource upper limit. For example, if 10% CPU resources are required to process a request, you can send up to 10 concurrent requests.

## Distribute requests to multiple connections


It is common to distribute requests to multiple connections for high performance in the design of applications. When you develop a high-performance application, you can use OSS as a large-scale distributed storage system instead of a single storage node such as a traditional storage server. You can send multiple concurrent requests to OSS to improve application performance. You can distribute requests to multiple connections to fully use the bandwidth provided by OSS. OSS does not impose limits on the number of connections to a bucket.

## Increase allowed number of retries


The first time a request is sent, OSS may require an extended period of time to respond to the request due to its large scale. In this case, you can resend the request. You can use OSS SDKs to configure a timeout period and the allowed number of retries for requests based on your business requirements.


Thank you! We've received your  feedback.