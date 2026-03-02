# Data lake overview

A data lake is a centralized repository that stores semi-structured and unstructured data at any scale. In a data lake, data is stored in its raw format. You can use various analytics engines, such as big data processing frameworks, real-time analytics tools, and machine learning, to easily extract valuable insights from your data.

## Architecture diagram


![组 850@4x](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5642186471/p952015.png)


This architecture diagram illustrates a comprehensive data management and analytics platform, covering the end-to-end flow from data collection to application.


-

Supports data uploads in multiple formats, such as Parquet, CSV, JSON, multimedia files, and database and application data.

-

Is compatible with public cloud, Apsara Stack, hybrid cloud, and edge devices, which ensures broad and flexible data sourcing.

-

Stores data for big data and AI services in BucketGroups. You can adjust BucketGroup bandwidth using resource pool Quality of Service (QoS) and use Object Storage Service (OSS) as the data lake storage solution. This approach ensures efficient data access and management.

-

Provides a rich set of programming interfaces, such as software development kits (SDKs), a POSIX file system, and a Hadoop Distributed File System (HDFS) compatible layer for flexible data access and processing.

-

Allows you to perform complex data exploration, train machine learning models, and run real-time stream computing by integrating data analytics and AI features. You can use visualization tools to better understand and present data insights.

## Why build a data lake on Alibaba Cloud OSS


Alibaba Cloud OSS provides virtually unlimited, cost-effective, and elastic storage, making it an ideal data storage service for building data lake solutions on Alibaba Cloud. OSS has powerful data management features to efficiently process and organize massive amounts of data. Its wide range of clients allows for easy integration with compute engines.


Building a data lake on OSS provides the following core advantages:


-

Low-cost storage: Offers a pay-as-you-go model and supports [tiered storage](https://www.alibabacloud.com/help/en/oss/user-guide/overview-54/) based on lifecycle rules (Standard, Infrequent Access, Archive, Cold Archive, and Deep Cold Archive) for flexible cost control.

-

Elastic scalability: Supports exabyte-scale data storage and eliminates the need for capacity provisioning, which makes it easy to handle data growth.

-

Ecosystem integration: Seamlessly integrates with Alibaba Cloud compute services, such as MaxCompute, EMR, and PAI, and open source analytics frameworks, such as Hadoop, Spark, RAY, and PyTorch.

-

Security and compliance: Provides [encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8), [access control](https://www.alibabacloud.com/help/en/oss/user-guide/permissions-and-access-control-overview#t4347.html), and  to meet enterprise-grade security requirements.

-

High availability and disaster recovery: Provides cross-zone redundant storage and supports cross-region replication to ensure data reliability.

## What to consider when building a data lake


When you build a data lake and analytics platform, you should consider several key aspects, including the following:

### Data collection and import


A data lake allows for the real-time import of any amount of data. It supports data collection from multiple sources and storage in its raw format. This process lets you scale to any amount of data and saves time on defining data structures, schemas, and transformations. OSS provides the following methods to import data:


-

You can directly upload data to OSS over the [internal network](https://www.alibabacloud.com/help/en/oss/user-guide/access-and-network-overview#section-r14-5vv-tdb).

-

You can upload data from your data center to OSS using [Express Connect](https://www.alibabacloud.com/help/en/express-connect/product-overview/what-is-express-connect/).

-

You can migrate petabyte-scale data to OSS using [Data Online Migration](https://www.alibabacloud.com/help/en/data-online-migration/product-overview/what-is-data-online-migration) or [Data Transport](https://www.alibabacloud.com/help/en/data-transport/product-overview/what-is-data-transport).

-

You can directly upload data to OSS over the [internet](https://www.alibabacloud.com/help/en/oss/user-guide/access-and-network-overview#section-sgf-k5v-tdb). Because this method introduces security risks, pay close attention to domain name management and access control. We recommend that you review the following documents:


-

[Bind a custom domain name to the default domain name of a bucket](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names)

-

[Block Public Access](https://www.alibabacloud.com/help/en/oss/user-guide/block-public-access)

-

[View the Referer of OSS requests from other websites](https://www.alibabacloud.com/help/en/oss/view-the-referers-of-oss-requests-from-other-websites)

### Secure and low-cost data storage


A data lake can store massive amounts of unstructured data from sources such as mobile applications, IoT devices, social media, and the Internet of vehicles. This data requires automatic cost optimization and must be kept secure at all times. OSS provides the following features to meet these requirements:


-

[Five storage classes](https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/) to accommodate data with different access frequencies, from hot to cold.

-

[Lifecycle rules](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-access-time) to automatically transition cold data to lower-cost storage classes.

-

[Versioning](https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/) to prevent accidental data deletion.

### Manage massive data


In a data lake, different business departments may store data under different prefixes in the same bucket, or in separate buckets. These scenarios require the ability to manage data separately within a single bucket and to facilitate data flow between different buckets. OSS provides a wide range of features to handle these complex scenarios:


-

[Access points](https://www.alibabacloud.com/help/en/oss/user-guide/access-point/) to configure data access permissions for different business teams.

-

[Bucket inventory](https://www.alibabacloud.com/help/en/oss/user-guide/bucket-inventory) to monitor the storage usage of different business teams within a bucket.

-

[Data replication](https://www.alibabacloud.com/help/en/oss/user-guide/data-replication-2/) to automatically synchronize data between buckets in the same region or across different regions.

### Manage and optimize performance for multi-service access


-

In typical data lake operations, concurrent data collection, pre-processing, AI training, and debugging can cause uneven resource allocation and resource contention between buckets and between Resource Access Management (RAM) users. OSS provides the [resource pool QoS](https://www.alibabacloud.com/help/en/oss/user-guide/oss-resource-pool-qos) feature, which lets you dynamically adjust throttling for buckets and their requesters. This ensures that key services and compute-intensive tasks receive priority access to resources during high-load periods, which maintains business stability.

-

For scenarios that require low latency and high performance, such as high queries per second (QPS) for data warehouses, low-latency responses for online business data, and repeated, low-latency model pulls for AI inference, OSS provides the [OSS accelerator](https://www.alibabacloud.com/help/en/oss/user-guide/overview-77/). The OSS accelerator caches hot files on high-performance NVMe SSDs to reduce data read latency and increase QPS. This capability significantly optimizes the performance of real-time computing jobs.

### Integrate with data analytics and AI frameworks


A data lake typically runs a variety of analytics and AI compute frameworks, and a complete production process in an enterprise may use several of them. Different compute frameworks have different interfaces and methods for accessing data. To facilitate easy connection to these ecosystems and reduce business transformation costs, OSS provides a rich set of clients, tools, and features:


-

OSS provides a rich set of SDKs for mainstream programming languages. If you have programming experience, you can use the [OSS SDK](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-63/) to achieve high-performance data access. For information about high-performance programming practices for OSS, see [Improve bandwidth significantly using Python's concurrency library for multi-threaded transformation](https://www.alibabacloud.com/help/en/oss/user-guide/bandwidth-of-100-gbit-s-in-vpcs#771389fbadu5q).

-

If you have experience running the Hadoop ecosystem on object storage in the cloud, you can use the [OSS connector for Hadoop](https://www.alibabacloud.com/help/en/oss/user-guide/use-oss-sdks-to-connect-to-the-open-source-ecosystem/) to read and write OSS data. This method lets you efficiently use the unlimited scalability and various enterprise-grade features of OSS.

-

If you currently use open source HDFS extensively and cannot transform your business in the short term, you can use the [OSS-HDFS service](https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs-overview#t2176950.html). This service provides standard interfaces that are fully compatible with HDFS. It also provides stronger performance and more elastic scalability than traditional HDFS. The OSS-HDFS service is seamlessly integrated with Alibaba Cloud EMR and open source ecosystem components such as Hadoop and Spark. This solution emphasizes strong compatibility with HDFS, which allows enterprises to smoothly migrate traditional HDFS services from on-premises data centers to the cloud without modifying existing HDFS-based big data applications. However, because of functional differences between open source HDFS and object storage, you may not be able to use some of OSS's native advanced data management features. For more information, see [Features of the OSS-HDFS service](https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs-service-function-support). Therefore, after you migrate to the cloud, we recommend that you gradually adapt and optimize your services to use the OSS Connector. This lets you take full advantage of the high performance and rich data management capabilities of OSS in cloud-native scenarios.

-

If some of your business applications need to access data using traditional file methods and cannot be modified, OSS provides the ossfs client to meet the data read and write requirements of these programs:


-

For modern applications such as AI training, AI inference, and autonomous driving simulation, the POSIX semantics requirements are relatively loose. You can use [ossfs 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-2-0/) for the best performance. If you are not sure about the specific access mode of your application, you can test with ossfs 2.0 first. If it does not work, you can downgrade to [ossfs 1.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-overview/).

-

For traditional applications, you can use [ossfs 1.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-overview/) to read and write data stored in OSS. However, because of the significant semantic differences between OSS and NAS, and the need for some traditional applications to have higher POSIX compatibility and performance, we do not recommend using ossfs 1.0 with OSS as a replacement for NAS. In these cases, to ensure the best compatibility and performance, we recommend that you choose [Alibaba Cloud File Storage NAS](https://www.alibabacloud.com/help/en/nas/product-overview/what-is-nas).

-

If you are familiar with the PyTorch dataset framework for loading AI datasets but are not familiar with using the OSS SDK, you can [use the OSS Connector for AI/ML to accelerate model training](https://www.alibabacloud.com/help/en/oss/developer-reference/oss-connector-overview/). This lets you obtain the best OSS dataset read performance without learning how to use the OSS SDK.

-

For the daily file upload and download needs of administrators and developers, OSS provides the following tools:


-

[Command-line tool ossutil 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/)

-

[Graphical management tool ossbrowser 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossbrowser-2-0-overview/)


Thank you! We've received your  feedback.