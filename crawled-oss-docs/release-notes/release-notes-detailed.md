# Release Notes for OSS Features

> Source: https://www.alibabacloud.com/help/en/oss/product-overview/release-notes

This topic describes the release notes for Object Storage Service (OSS) and provides links to the relevant references.

## September 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Vector bucket | Vector buckets provide a simple, scalable, and cost-effective foundation for your AI applications. By delivering dedicated vector storage and query capabilities, vector buckets empower you to develop sophisticated solutions for multimodal retrieval, knowledge bases, Retrieval-Augmented Generation (RAG), and AI Agents. | 2025-09-24 | China (Shenzhen), China (Beijing) | Overview of vector buckets |
| Dual-AZ support for Standard (ZRS) expands to more regions | For regions with two Availability Zones, the dual-AZ redundancy storage mechanism is implemented for Standard (ZRS) objects. Copies of your data are redundantly stored across the two zones within the same region, which ensures uninterrupted access even if one AZ becomes unavailable. Standard(ZRS) provides 99.9999999999% (twelve 9s) of data durability and 99.99% service availability. | 2025-09-11 | UK (London), Thailand (Bangkok), UAE (Dubai) | Storage redundancy |
| Multi-AZ support for Standard (ZRS) expands to Malaysia (Kuala Lumpur) | Standard (ZRS) is available in regions with multiple AZs and redundantly stores your data across these AZs within a single region, ensuring continued data access even if one AZ becomes unavailable. Standard (ZRS) provides 99.9999999999% (twelve 9s) data durability and 99.995% service availability. | 2025-09-11 | Malaysia (Kuala Lumpur) | Storage redundancy |
| Multi-AZ support for IA (ZRS) expands to Malaysia (Kuala Lumpur) | IA (ZRS) is available in regions with multiple AZs and redundantly stores your data across these AZs within a single region. | 2025-09-11 | Malaysia (Kuala Lumpur) | Storage redundancy |
| Multi-AZ support for Archive (ZRS) expands to Malaysia (Kuala Lumpur) | Archive (ZRS) is available in regions with multiple AZs. | 2025-09-11 | Malaysia (Kuala Lumpur) | Storage redundancy |

## August 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| OSS SDK for Java 2.0 | OSS SDK for Java 2.0 is a major rewrite of the OSS SDK for Java 1.0 code repository. It simplifies underlying operations such as identity authentication, automatic request retry, and error handling. Provides flexible parameter configuration methods and rich advanced operations, such as paginator, transmission managers, and File-like operations. | 2025-08-29 | All regions | OSS Java SDK V2 (Preview) |
| OSS accelerator available for commercial use | OSS accelerator is officially available for commercial use with pricing determined by provisioned capacity and usage duration. It also supports deployment at the Availability Zone level. | 2025-08-18 | China (Hangzhou), China (Shanghai), China (Beijing), China (Ulanqab), China (Shenzhen), Singapore | OSS accelerator fees, OSS accelerator |

## July 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Singapore Region bandwidth upgrade to 20 Gbps | The default aggregate upload bandwidth for OSS under a single Alibaba Cloud account in the Singapore Region has been increased from 5 Gbps to 20 Gbps for both internal and external networks. | 2025-07-04 | Singapore | Limits and performance metrics |

## June 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| OSS SDK for C# 2.0 | OSS SDK for C# 2.0 is a major rewrite of the OSS SDK for C# 1.0 code repository. It simplifies underlying operations such as identity authentication, automatic request retry, and error handling. Provides flexible parameter configuration and rich advanced operations. | 2025-06-06 | All regions | Get started with OSS SDK for C# 2.0 |

## April 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Singapore download bandwidth increased to 100 Gbit/s | Maximum download bandwidth (over internal networks and the Internet) of a single account is increased from 5 Gbit/s to 100 Gbit/s. | 2025-04-29 | Singapore | Limits and performance metrics |
| Monitoring bucket groups in the resource pool | Use CloudMonitor to monitor bucket groups in the resource pool and obtain information about performance thresholds and metrics. Configure threshold-triggered alerts. | 2025-04-27 | All regions | View the bandwidth usage of the resource pool |
| Throttling configurations for bucket group in resource pool | In a resource pool, add multiple buckets to a bucket group and configure bandwidth. Simplifies configurations and maximizes bandwidth utilization. | 2025-04-10 | All regions | Examples of resource pool QoS configuration |
| Standard (ZRS) storage plan | Can be used to offset the storage fees of Standard zone-redundant storage (ZRS) objects. | 2025-04-09 | Regions in the Chinese mainland, China (Hong Kong), China (Macao), China (Taiwan), and regions outside the Chinese mainland | Resource plans |
| Cold Archive (LRS) storage plan | Can be used to offset the storage fees of Cold Archive locally redundant storage (LRS) objects. | 2025-04-09 | China (Hong Kong) and Singapore | Resource plans |
| TLS version and cipher suite management | Configure TLS version and cipher suite to ensure data encryption, authentication, and data integrity. | 2025-04-03 | UK (London) | Configure the TLS version |

## March 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Standard ZRS for dual zones in a region | Standard (ZRS) stores multiple data copies across two zones in a region. Provides 99.9999999999% data durability and 99.99% service availability. | 2025-03-31 | Malaysia (Kuala Lumpur) | Storage redundancy |
| ossfs 2.0 | Upgraded version of ossfs 1.0, designed for compute-intensive use cases. Suitable for AI-powered model training, inference model retrieval, and autonomous driving simulation. | 2025-03-25 | All regions | ossfs 2.0 |
| OSS SDK for Harmony | SDK designed for Huawei HarmonyOS developers to easily access Alibaba Cloud OSS. | 2025-03-13 | All regions | OSS SDK for Harmony (preview) |
| Python SDK V2.0 | Major rewrite of OSS SDK for Python 1.0 with simplified operations and rich advanced features including paginator, transmission managers, and File-like operations. | 2025-03-07 | All regions | OSS SDK for Python 2.0 |

## January 2025

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Integration of resource pool QoS into CloudMonitor | Monitor each bucket in the resource pool and obtain information about performance thresholds and actual performance. | 2025-01-16 | All regions | View the bandwidth usage of the resource pool |
| OSS accelerator monitoring | Obtain cache status of OSS accelerator including Bandwidth Usage, QPS Usage, Hit Rate, and Latency monitoring items. | 2025-01-06 | All regions | Monitor accelerators |

## November 2024

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Resource pool QoS | Dynamically change bandwidth of buckets in a resource pool to prioritize key services during peak hours. | 2024-11-29 | All regions | Quality of service (QoS) policy of resource pools |
| Go SDK V2.0 | Major rewrite with simplified operations including paginator, transmission managers, and File-like operations. | 2024-11-26 | All regions | OSS SDK for Go 2.0 |

## September 2024

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Data indexing - AISearch | Quickly search for specific objects based on semantic content, multimedia metadata, and custom metadata. | 2024-09-25 | Multiple regions including China and international | Data indexing, Vector search |
| OSS Connector for AI/ML | Python library for efficient OSS data access in PyTorch training jobs. Supports map-style and iterable-style datasets and OssCheckpoint for model training. | 2024-09-02 | All regions | OSS Connector for AI/ML |

## July 2024

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| ossutil 2.0 | Comprehensive optimization including configuration files, command uniformity, function improvements, and default parameter configurations. | 2024-07-31 | All regions | ossutil 2.0 (preview) |

## June 2024

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Access to OSS by using PrivateLink | Establish private, stable, and secure connections between VPCs and OSS. Simplifies network architectures. | 2024-06-13 | Multiple regions | Access OSS over PrivateLink |

## May 2024

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Bandwidth increase in China (Hangzhou) region | Total download bandwidth increased to 100 Gbit/s. | 2024-05-10 | China (Hangzhou) | Limits and performance metrics |

## April 2024

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Block Public Access | Enable Block Public Access for OSS buckets to prevent data breaches. Existing public access permissions are ignored when enabled. | 2024-04-11 | All regions | Block Public Access |

## December 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Permissions to activate OSS | The oss:ActivateProduct permission is required for a RAM user or RAM role to activate OSS. | 2023-12-25 | All regions | Example 14: Authorize a RAM user to activate OSS |
| Permissions to purchase OSS resource plans | The oss:CreateOrder permission is required for a RAM user or RAM role to purchase OSS resource plans. | 2023-12-20 | All regions | Example 13: Authorize a RAM user to place an order for an OSS resource plan |

## October 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Bandwidth increase in China (Shanghai) and China (Shenzhen) | Total download bandwidth increased from 10 Gbit/s to 100 Gbit/s. | 2023-10-31 | China (Shanghai), China (Shenzhen) | Limits and performance metrics |
| Object FC Access Point | Initiate GetObject requests that automatically trigger Function Compute to transform object content. | 2023-10-31 | Multiple regions | Create Object FC Access Points |
| CRR across accounts | Cross-region and same-region replication across accounts for automatic and asynchronous replication. | 2023-10-17 | All regions | Cross-account and cross-region data replication |

## September 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| TLS version management | Configure TLS version for encrypted communication between client applications and OSS. | 2023-09-19 | All regions | Configure the TLS version |

## June 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Real-time access to Archive objects | Access Archive objects in real time without restoration. Higher data retrieval fees but no waiting time. | 2023-06-30 | All regions | Real-time access of Archive objects |
| Change of storage redundancy type | Storage redundancy type of a bucket can be changed from LRS to ZRS. | 2023-06-28 | Multiple regions | Storage redundancy |

## May 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Deep Cold Archive | Highly durable storage at lower prices than Cold Archive. Minimum billable size of 64 KB and minimum storage duration of 180 days. Suitable for extremely cold data. | 2023-05-07 | Multiple regions including China and Singapore | Deep Cold Archive |

## March 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Bandwidth increase in China (Beijing) | Total download bandwidth increased from 10 Gbit/s to 100 Gbit/s. | 2023-03-12 | China (Beijing) | Limits and performance metrics |

## February 2023

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Signature tools | OSS console provides signature tools including Signature in Authorization Header, PostObject Policy Signature, and URL Signature. | 2023-02-03 | All regions | Signature in Authorization Header, PostObject Policy Signature, URL Signature |

## December 2022

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Resource group | Group buckets based on business requirements and configure different permissions for each resource group. | 2022-12-16 | Multiple regions | Grant the same permissions on multiple buckets by using a resource group |
| RTC (Replication Time Control) | Meet compliance requirements with replication of 99.99% of objects within 10 minutes. Near real-time monitoring. | 2022-12-01 | Chinese mainland regions, US regions | Use Replication Time Control (RTC) |

## October 2022

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Response header adjustment | Content-Disposition: attachment header automatically added when accessing objects from browser via default domain name for buckets created after October 9, 2022. | 2022-10-09 | All regions | What do I do if an object cannot be previewed? |

## August 2022

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Automatic storage tiering of OSS-HDFS | Data frequently accessed stored as Standard objects, infrequently accessed stored as Archive objects. Reduces total storage costs. | 2022-08-16 | Multiple regions | Automatic storage tiering of OSS-HDFS |

## March 2022

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Data indexing - MetaSearch | Quickly search for specific objects based on object metadata conditions. Efficiently manage data structures and perform queries. | 2022-03-21 | Multiple regions | Data indexing, Scalar retrieval |

## January 2022

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| OSS-HDFS | Compatible with HDFS API operations and supports directory-level operations. Facilitates use of OSS resources in open source ecosystems. | 2022-01-27 | Multiple regions | What is OSS-HDFS? |

## October 2021

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Lifecycle rules based on last access time | Configure lifecycle rules based on last access time to identify and transition cold data, reducing storage costs. | 2021-10-19 | All regions | Lifecycle rules based on the last access time |

## September 2021

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| SRR (Same-Region Replication) | Replicates objects across buckets within the same region in an automatic and asynchronous manner. | 2021-09-06 | All regions | SRR |

## August 2021

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| OSS DDoS protection for custom domain names | DDoS protection supported for custom domain names of buckets. Up to five custom domain names per bucket. | 2021-08-13 | Multiple China regions | OSS DDoS protection |
| Cold Archive | Storage class suitable for cold data with long-term retention. Minimum billable size of 64 KB, minimum storage period of 180 days. Unit price lower than Archive. | 2021-08-01 | Multiple regions worldwide | Cold Archive |

## July 2021

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Object tagging for different versions | Object tagging can be configured for different versions of objects in versioning-enabled buckets. | 2021-07-15 | All regions | Configure object tagging |

## April 2021

| Feature | Description | Release date | Supported regions | References |
|---------|-------------|--------------|-------------------|------------|
| Bucket Policy | Bucket policies can be configured by using graphical user interfaces (GUIs) and policy syntax. | 2021-04-16 | All regions | Configure bucket policies |
