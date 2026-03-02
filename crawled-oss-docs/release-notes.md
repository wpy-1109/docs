# Release notes for OSS features

This topic describes the release notes for Object Storage Service (OSS) and provides links to the relevant references.

## September 2025


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-vector-bucket)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/)


| Feature | Description | Release date | Supported regions | References |
| --- | --- | --- | --- | --- |
| Vector bucket | Vector buckets provide a simple, scalable, and cost-effective foundation for your AI applications. By delivering dedicated vector storage and query capabilities, vector buckets empower you to develop sophisticated solutions for multimodal retrieval, knowledge bases, Retrieval-Augmented Generation (RAG), and AI Agents. | 2025-09-24 | China (Shenzhen), China (Beijing) | Overview of vector buckets |
| Dual-AZ support for Standard (ZRS) expands to more regions | For regions with two Availability Zones, the dual-AZ redundancy storage mechanism is implemented for Standard (ZRS) objects. Copies of your data are redundantly stored across the two zones within the same region, which ensures uninterrupted access even if one AZ becomes unavailable. By redundantly storing data across two distinct AZs, Standard(ZRS) provides 99.9999999999% (twelve 9s) of data durability and 99.99% service availability. | 2025-09-11 | UK (London, Thailand (Bangkok), UAE (Dubai) | Storage redundancy |
| Multi-AZ support for Standard (ZRS) expands to Malaysia (Kuala Lumpur) | Standard (ZRS) is available in regions with multiple AZs and redundantly stores your data across these AZs within a single region, ensuring continued data access even if one AZ becomes unavailable. Standard (ZRS) provides 99.9999999999% (twelve 9s) data durability and 99.995% service availability. | 2025-09-11 | Malaysia (Kuala Lumpur) | Storage redundancy |
| Multi-AZ support for IA (ZRS) expands to Malaysia (Kuala Lumpur) | IA (ZRS) is available in regions with multiple AZs and redundantly stores your data across these AZs within a single region, ensuring continued data access even if one AZ becomes unavailable. IA (ZRS) provides 99.9999999999% (twelve 9s) data durability and 99.50% service availability. | 2025-09-11 | Malaysia (Kuala Lumpur) | Storage redundancy |
| Multi-AZ support for Archive (ZRS) expands to Malaysia (Kuala Lumpur) | Archive (ZRS) is available in regions with multiple AZs and redundantly stores your data across these AZs within a single region, ensuring continued data access even if one AZ becomes unavailable. Archive (ZRS) provides 99.9999999999% (twelve 9s) data durability and 99.50% service availability. | 2025-09-11 | Malaysia (Kuala Lumpur) | Storage redundancy |


## August 2025


(https://www.alibabacloud.com/help/en/oss/developer-reference/oss-sdk-for-java-2-0/)


-

(https://www.alibabacloud.com/help/en/oss/oss-accelerator-fees)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/overview-77/)


| Feature | Description | Release date | Supported regions | References |
| --- | --- | --- | --- | --- |
| OSS SDK for Java 2.0 | OSS SDK for Java 2.0 a major rewrite of the OSS SDK for Java 1.0 code repository. OSS SDK for Java 2.0 is a new version that simplifies underlying operations such as identity authentication, automatic request retry, and error handling. You can access OSS by calling API operations without complex programming.OSS SDK for Java 2.0 provides flexible parameter configuration methods and rich advanced operations, such as paginator, transmission managers, and File-like operations. This comprehensively improves development efficiency and experience. | 2025-08-29 | All regions | OSS Java SDK V2 (Preview) |
| OSS accelerator available for commercial use | OSS accelerator is officially available for commercial use with pricing determined by provisioned capacity and usage duration. It also supports deployment at the Availability Zone level. | 2025-08-18 | China (Hangzhou), China (Shanghai), China (Beijing), China (Ulanqab), China (Shenzhen), Singapore | OSS accelerator feesOSS accelerator |


## July 2025


(https://www.alibabacloud.com/help/en/oss/user-guide/limits)


| Feature | Description | Release date | Supported regions | References |
| --- | --- | --- | --- | --- |
| The aggregate upload bandwidth for internal and external networks in the Singapore Region has been upgraded to 20 Gbps. | The default aggregate upload bandwidth for OSS under a single Alibaba Cloud account in the Singapore Region has been increased from 5 Gbps to 20 Gbps for both internal and external networks. | 2025-07-04 | Singapore | Limits and performance metrics |


## June 2025


(https://www.alibabacloud.com/help/en/oss/developer-reference/quick-start-using-oss-sdk-for-c-v2#9457e799ce9jn)


| Feature | Description | Release date | Supported regions | References |
| --- | --- | --- | --- | --- |
| OSS SDK for C# 2.0 | OSS SDK for C# 2.0 is a major rewrite of the OSS SDK for C# 1.0 code repository.OSS SDK for C# 2.0 is a new version that simplifies underlying operations such as identity authentication, automatic request retry, and error handling. You can access OSS by calling API operations without complex programming.OSS SDK for C# 2.0 provides flexible parameter configuration methods and rich advanced operations, such as the paginator. This comprehensively improves development efficiency and experience. | 2025-06-06 | All regions | Get started with OSS SDK for C# 2.0 |


## April 2025


(https://www.alibabacloud.com/help/en/oss/user-guide/limits)


-

(https://www.alibabacloud.com/help/en/oss/user-guide/use-cloudmonitor-to-monitor-oss#20395328edqbj)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/use-cloudmonitor-to-monitor-oss-throttling-information-in-real-time)


(https://www.alibabacloud.com/help/en/oss/user-guide/use-cases-of-resource-pool-qos)


(https://www.alibabacloud.com/help/en/oss/resource-plan/)


(https://www.alibabacloud.com/help/en/oss/resource-plan/)


(https://www.alibabacloud.com/help/en/oss/user-guide/set-tls-version)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| The total download bandwidth over internal networks and the Internet is increased to 100 Gbit/s in the Singapore region. | The maximum download bandwidth (over internal networks and the Internet) of a single Alibaba Cloud account is increased from 5 Gbit/s to 100 Gbit/s, thereby improving the efficiency of data analysis and computation. | 2025-04-29 | Singapore | Limits and performance metrics |
| Monitoring bucket groups in the resource pool | You can use CloudMonitor to monitor bucket groups in the resource pool and obtain information about the performance thresholds and metrics. You can also configure threshold-triggered alerts. | 2025-04-27 | All regions | View the bandwidth usage of the resource poolUse CloudMonitor to monitor OSS throttling information in real time |
| Throttling configurations for a bucket group in a resource pool | In a resource pool, you can add multiple buckets that are used for same business to a bucket group and configure the bandwidth of the bucket group. This simplifies configurations and maximizes bandwidth utilization based on time-sharing scheduling. | 2025-04-10 | All regions | Examples of resource pool QoS configuration |
| Standard (ZRS) storage plan | A Standard (ZRS) storage plan can be used to offset the storage fees of Standard zone-redundant storage (ZRS) objects. | 2025-04-09 | Regions in the Chinese mainland, China (Hong Kong), China (Macao), China (Taiwan), and regions outside the Chinese mainland | Resource plans |
| Cold Archive (LRS) storage plan | A Cold Archive (LRS) storage plan can be used to offset the storage fees of Cold Archive locally redundant storage (LRS) objects. | 2025-04-09 | China (Hong Kong) and Singapore | Resource plans |
| TLS version and cipher suite management | The Transport Layer Security (TLS) version and a cipher suite can be configured to ensure data encryption, authentication, and data integrity. After you configure the TLS version and the cipher suite, clients can use only the configured TLS version and cipher suite to send requests to and receive requests from OSS to meet the security requirements of the communication link. | 2025-04-03 | UK (London) | Configure the TLS version |


## March 2025


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-2-0/#fbd0fa1fc1w0w)


(https://www.alibabacloud.com/help/en/oss/developer-reference/harmony/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/2-0-manual-preview-version/)


(https://www.alibabacloud.com/help/en/oss/get-started-with-oss-sdk-for-python-v2)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Standard ZRS for dual zones in a region | Standard (ZRS) stores multiple data copies across two zones in a region if a region has two zones. If one zone becomes unavailable, you can still access the data that is stored in the other zone. Standard ZRS provides 99.9999999999% (twelve 9's) data durability and 99.99% service availability. | 2025-03-31 | Malaysia (Kuala Lumpur) | Storage redundancy |
| ossfs 2.0 | ossfs 2.0 is released as an upgraded version of ossfs 1.0, designed for new forms of compute-intensive use cases. Certain limits are applied to POSIX semantics based on actual business requirements to allow ossfs 2.0 to deliver comprehensive performance upgrade. ossfs 2.0 is suitable for scenarios such as AI-powered model training, inference model retrieval, and autonomous driving simulation. | 2025-03-25 | All regions | ossfs 2.0 |
| OSS SDK for Harmony | OSS SDK for Harmony is a software development kit especially designed for Huawei HarmonyOS developers to easily access Alibaba Cloud OSS. | 2025-03-13 | All regions | OSS SDK for Harmony (preview) |
| Python SDK V2.0 | OSS SDK for Python 2.0 is a major rewrite of the OSS SDK for Python 1.0 code repository. OSS SDK for Python 2.0 is a new version that simplifies underlying operations such as identity authentication, automatic request retry, and error handling. You can access OSS by calling API operations without complex programming. OSS SDK for Python 2.0 provides flexible parameter configuration methods and rich advanced operations, such as paginator, transmission managers, and File-like operations. This comprehensively improves development efficiency and experience. | 2025-03-07 | All regions | OSS SDK for Python 2.0Get Started |


## January 2025


-

(https://www.alibabacloud.com/help/en/oss/user-guide/use-cloudmonitor-to-monitor-oss#20395328edqbj)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/use-cloudmonitor-to-monitor-oss-throttling-information-in-real-time)


(https://www.alibabacloud.com/help/en/oss/user-guide/monitoring-information-for-accelerators#356baf1424yv8)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Integration of resource pool QoS into CloudMonitor | After you enable resource pool QoS, you can use CloudMonitor to monitor each bucket in the resource pool and obtain information about the performance thresholds and actual performance of the requesters to the resource pool. You can also configure threshold-triggered alerts. | 2025-01-16 | All regions | View the bandwidth usage of the resource poolUse CloudMonitor to monitor OSS throttling information in real time |
| OSS accelerator monitoring | After you enable an OSS accelerator, you can use the OSS accelerator monitoring feature to obtain the cache status of the OSS accelerator by using the Bandwidth Usage, QPS Usage, Hit Rate, and Latency monitoring items. This helps ensure efficient and smooth data transfer. | 2025-01-06 | All regions | Monitor accelerators |


## November 2024

















(https://www.alibabacloud.com/help/en/oss/user-guide/oss-resource-pool-qos)


(https://www.alibabacloud.com/help/en/oss/developer-reference/manual-for-go-sdk-v2/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/quick-start-for-oss-go-sdk-v2)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Resource pool QoS | After you add multiple buckets in your Alibaba Cloud account to the same resource pool, you are allowed to dynamically change the bandwidth of each bucket based on their usage. This ensures that resources are preferentially allocated to key services and compute-intensive tasks during peak hours and prevents bottlenecks caused by uneven resource allocation. | 2024-11-29 | All regions | Quality of service (QoS) policy of resource pools |
| Go SDK V2.0 | OSS SDK for Go 2.0 is a major rewrite of the OSS SDK for Go 1.0 code repository. OSS SDK for Go 2.0 is a new version that simplifies underlying operations such as identity authentication, automatic request retry, and error handling. You can access OSS by calling API operations without complex programming. OSS SDK for Go 2.0 provides flexible parameter configuration methods and rich advanced operations, such as paginator, transmission managers, and File-like operations. This comprehensively improves development efficiency and experience. | 2024-11-26 | All regions | OSS SDK for Go 2.0Get Started |


## September 2024


-

(https://www.alibabacloud.com/help/en/oss/user-guide/data-indexing-overview/)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/vector-retrieval/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/oss-connector-for-ai-ml)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Data indexing-AISearch | AISearch is available. AISearch allows you to quickly search for specific objects among a large number of objects based on object information conditions of documents, images, videos, and audio files, such as semantic content, multimedia metadata, and custom metadata. AISearch improves search efficiency based on object content and multimedia attributes. | 2024-09-25 | China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hangzhou), China (Shanghai), China (Shenzhen), China (Guangzhou), China (Chengdu), China (Hong Kong), Singapore, Indonesia (Jakarta), Germany (Frankfurt), US (Silicon Valley), and US (Virginia) | Data indexingVector search |
| OSS Connector for AI/ML | OSS Connector for AI/ML is a Python library that is used to efficiently access and store OSS data in PyTorch training jobs. You can build map-style and iterable-style datasets that are suitable for random data access and sequential streaming data access by using data in OSS. OSS Connector for AI/ML allows you to create an OssCheckpoint object. This object allows you to directly load checkpoints from OSS during model training and save checkpoints to OSS after periodic model training. This way, workflow is simplified. | 2024-09-02 | All regions | OSS Connector for AI/ML |


## July 2024


(https://www.alibabacloud.com/help/en/oss/developer-reference/command-line-tool-ossutil-version-2)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| ossutil 2.0 | Compared with ossutil 1.0, ossutil 2.0 is comprehensively and significantly optimized and improved in the following aspects: the structure and supported types of configuration files, the uniformity of commands in different operating systems, the functions and rules of various types of commands, the matching mode and supported values of options, the default parameter configurations, and the default status of resumable upload. | 2024-07-31 | All regions | ossutil 2.0 (preview) |


## June 2024


(https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-via-privatelink-network)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Access to OSS by using PrivateLink | PrivateLink can be used to establish private, stable, and secure connections between virtual private clouds (VPCs) and other Alibaba Cloud services. PrivateLink simplifies network architectures and prevents risks that may arise from accessing services over the Internet. | 2024-06-13 | China (Hangzhou), China (Shanghai), China (Beijing), China (Ulanqab), China (Shenzhen), China (Hong Kong), Singapore, and Indonesia (Jakarta) | Access OSS over PrivateLink |


## May 2024


(https://www.alibabacloud.com/help/en/oss/user-guide/limits#481f9cdaa9cxq)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bandwidth increase in the China (Hangzhou) region | The total download bandwidth over internal networks and the Internet is increased to 100 Gbit/s in the China (Hangzhou) region. | 2024-05-10 | China (Hangzhou) | Limits and performance metrics of OSS |


## April 2024


(https://www.alibabacloud.com/help/en/oss/user-guide/block-public-access)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Block Public Access | You can allow public access to OSS resources by configuring bucket policies and access control lists (ACLs). Public access specifies access to OSS resources without specific permissions or authentication. Public access can cause data breaches and generate a large amount of outbound traffic over the Internet due to malicious access. To prevent risks caused by public access, OSS allows you to enable Block Public Access with a few steps for OSS, a bucket, an access point, and an Object FC Access Point. If you enable Block Public Access, existing public access permissions are ignored and you cannot configure public access permissions. This disables public data access channels and ensures data security. | 2024-04-11 | All regions | Block Public Access |


## December 2023





(https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#3ad07983293bf)





(https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#ef1d329d4e7gm)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Permissions to activate OSS | The oss:ActivateProduct permission is required for a RAM user or RAM role to activate OSS. | 2023-12-25 | All regions | Example 14: Authorize a RAM user to activate OSS |
| Permissions to purchase OSS resource plans | The oss:CreateOrder permission is required for a RAM user or RAM role to purchase OSS resource plans. | 2023-12-20 | All regions | Example 13: Authorize a RAM user to place an order for an OSS resource plan |


## October 2023


(https://www.alibabacloud.com/help/en/oss/user-guide/limits)


-

(https://www.alibabacloud.com/help/en/oss/user-guide/create-object-fc-access-point)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/use-function-compute-to-process-get-object-requests)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/use-object-fc-access-point)


-

(https://www.alibabacloud.com/help/en/oss/user-guide/cross-account-cross-region-replication)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/copy-across-accounts-in-the-same-region)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/introduction-to-data-replication-permissions)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bandwidth increase in the China (Shanghai) and China (Shenzhen) regions | The total download bandwidth over the internal network and the Internet is increased from 10 Gbit/s to 100 Gbit/s in the China (Shanghai) and China (Shenzhen) regions. | 2023-10-31 | China (Shanghai) and China (Shenzhen) | Limits and performance metrics of OSS |
| Object FC Access Point | If you want OSS to automatically trigger Function Compute when you initiate a GetObject request and return the transformed result of the retrieved data to the application, you must initiate the request by using an Object FC Access Point. You can initiate requests by using Object FC Access Points to seamlessly modify or filter the content of objects without the need to change object storage semantics or modify the client. | 2023-10-31 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Shenzhen), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), South Korea (Seoul), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Germany (Frankfurt), and UK (London) | Create Object FC Access PointsCompile a function that is used to process GetObject requestsUse Object FC Access Points |
| CRR | Cross-region replication (CRR) across accounts and same-region replication (SRR) across accounts allow the automatic and asynchronous (near real-time) replication of OSS objects from a bucket within an Alibaba Cloud account to another bucket within another Alibaba Cloud account. CRR across accounts requires that the source and destination buckets be located in different regions, and SRR across accounts requires that the source and destination buckets be located in the same region. CRR across accounts and SRR across accounts replicate operations, such as the creation, overwriting, and deletion of objects, from a source bucket to a destination bucket. | 2023-10-17 | All regions | Cross-account and cross-region data replicationSRR across accountsData replication permissions |


## September 2023


(https://www.alibabacloud.com/help/en/oss/user-guide/set-tls-version)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| TLS version management | Communication between client applications and OSS is encrypted by using the transport layer security (TLS) protocol. TLS is a standard cryptographic protocol that ensures privacy and data integrity between clients and servers that communicate over the Internet. You can use an OSS server to configure the TLS version. After you configure the TLS version, clients can use only the configured TLS version to send requests to and receive requests from OSS to meet the security requirements of the communication link. | 2023-09-19 | All regions | Configure the TLS version |


## June 2023


-

(https://www.alibabacloud.com/help/en/oss/user-guide/archive-direct-reading)

-

(https://www.alibabacloud.com/help/en/oss/data-processing-fees)


-

(https://www.alibabacloud.com/help/en/oss/user-guide/overview-of-storage-redundancy-types/)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/converting-storage-redundancy-types)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Real-time access to Archive objects | Real-time access of Archive objects is supported. This feature allows you to access Archive objects in real time without the need to restore them. Compared with accessing restored objects, real-time access of Archive objects requires less time to retrieve data but generates higher data retrieval fees. This feature is suitable for occasional access to rarely accessed data. | 2023-06-30 | All regions | Real-time access of Archive objectsData processing fees |
| Change of the storage redundancy type | The storage redundancy type of a bucket can be changed from locally redundant storage (LRS) to zone-redundant storage (ZRS) to withstand zone-level failures. | 2023-06-28 | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), and Germany (Frankfurt). | Storage redundancyChange the storage redundancy type of a bucket |


## May 2023


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#96a15b20da0qc)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Deep Cold Archive | Deep Cold Archive provides highly durable storage at lower prices compared with Cold Archive. Deep Cold Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 180 days. You must restore a Deep Cold Archive object before you can access it. The amount of time that is required to restore a Deep Cold Archive object varies based on the object size and restoration priority. You are charged data retrieval fees and API operation calling fees when you restore Deep Cold Archive objects. Deep Cold Archive is suitable for extremely cold data that must be stored for an extremely long period of time, including raw data that is accumulated over an extended period of time in the big data and AI fields, retained media resources, regulatory and compliance documents, and data that needs to be migrated from tapes to the cloud for long-term storage. Deep Cold Archive supports only LRS. | 2023-05-07 | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), and Singapore | Deep Cold Archive |


## March 2023


(https://www.alibabacloud.com/help/en/oss/user-guide/limits)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bandwidth increase in the China (Beijing) region | The total download bandwidth over internal and external networks is increased from 10 Gbit/s to 100 Gbit/s in the China (Beijing) region. | 2023-03-12 | China (Beijing) | Limits and performance metrics of OSS |


## February 2023

















-


-


-


-

(https://www.alibabacloud.com/help/en/oss/developer-reference/signature-in-authorization-header#concept-2286713)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/postobject-policy-signature#concept-2286714)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/signed-urls#concept-2286716)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Signature tools | The OSS console provides the following signature tools: Signature in Authorization HeaderAfter you use the signature tool to specify parameters, the system automatically generates a request signature and verifies the request signature. PostObject Policy SignatureAfter you use the signature tool to specify parameters, the system automatically generates a request signature for the upload task by using an HTML form and verifies the request signature. URL SignatureYou can use the signature tool to generate a signed object URL for temporary access. When you generate a signed object URL, you can specify the validity period of the URL to limit the period in which visitors can use the URL to access resources. | 2023-02-03 | All regions | Signature in Authorization HeaderPostObject Policy SignatureURL Signature |


## December 2022

















(https://www.alibabacloud.com/help/en/oss/user-guide/configure-a-resource-group#concept-2074860)


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/rtc#task-2257877)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Resource group | A resource group is a resource-based access control method. You can group your buckets based on your business requirements and configure different permissions for each resource group. This way, you can manage access to your buckets by group. | 2022-12-16 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Germany (Frankfurt), UK (London), and UAE (Dubai) | Grant the same permissions on multiple buckets by using a resource group |
| RTC | The Replication Time Control (RTC) feature provided by OSS can meet your compliance requirements or business requirements for CRR. After the RTC feature is enabled, OSS replicates most of the objects that you uploaded to OSS within a few seconds and replicates 99.99% of the objects within 10 minutes. In addition, the RTC feature provides near real-time monitoring of data replication. After you enable the RTC feature, you can view various metrics of replication tasks. | 2022-12-01 | The Chinese mainlandIn the Chinese mainland, RTC can be enabled for cross-region replication tasks only between the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), and China (Shenzhen).outside the Chinese mainlandRTC supports cross-region replication only between the following regions outside the Chinese mainland: US (Silicon Valley) and US (Virginia). | Use Replication Time Control (RTC) |


## October 2022





(https://www.alibabacloud.com/help/en/oss/how-to-ensure-an-object-is-previewed-when-you-access-the-object)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Response header adjustment for object access | The Content-Disposition: attachment header is automatically added to the response that is returned when you access an OSS object from a browser by using the default domain name of a bucket created after October 9, 2022. The browser detects the value of the response header and downloads the object as an attachment instead of providing a preview of the object. This response header is not added if you access objects by using a custom domain name. | 2022-10-09 | All regions | What do I do if an object cannot be previewed when I access the object? |


## August 2022

















(https://www.alibabacloud.com/help/en/oss/user-guide/enable-the-automatic-storage-tiering-feature-for-the-oss-hdfs-service#task-2224842)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Automatic storage tiering of OSS-HDFS | The automatic storage tiering feature of OSS-HDFS is available. Some data stored in OSS-HDFS does not need to be frequently accessed. However, due to data compliance or archiving requirements, the data still needs to be retained. To meet your business requirements, OSS-HDFS provides the automatic storage tiering feature. Data that is frequently accessed is stored as Standard objects, whereas data that is infrequently accessed is stored as Archive objects. This helps reduce the total storage costs. | 2022-08-16 | China (Hangzhou), China (Shanghai), China (Shenzhen), China (Beijing), China (Zhangjiakou), and Singapore | Automatic storage tiering of OSS-HDFS |


## March 2022

















-

(https://www.alibabacloud.com/help/en/oss/user-guide/data-indexing-overview/)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/scalar-retrieval/#concept-2136292)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Data indexing-MetaSearch | Object Storage Service (OSS) provides MetaSearch to allow you to quickly search for specific objects among a large number of objects based on object metadata conditions. The metadata of objects can be specified as index conditions to query objects. This way, you can efficiently manage and learn about data structures, perform queries, collect statistics, and manage objects. | 2022-03-21 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Shenzhen), China (Guangzhou), China (Chengdu), China (Hong Kong), Singapore, Indonesia (Jakarta), Germany (Frankfurt), US (Silicon Valley), US (Virginia), and UK (London) | Data indexingScalar retrieval |


## January 2022

















(https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs-overview#concept-2176950)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| OSS-HDFS | OSS-HDFS is compatible with Hadoop Distributed File System (HDFS) API operations and supports directory-level operations. This facilitates the use of OSS resources in open source ecosystems. | 2022-01-27 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Ulanqab), China (Shenzhen), China (Guangzhou), China (Zhangjiakou), China (Hong Kong), Japan (Tokyo), Singapore, Germany (Frankfurt), US (Silicon Valley), US (Virginia), Indonesia (Jakarta), and Thailand (Bangkok) | What is OSS-HDFS? |


## October 2021

















(https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-access-time#concept-2116588)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Lifecycle rules based on the last access time | You can configure lifecycle rules based on the last access time of objects in a bucket. After you configure a lifecycle rule based on the last access time of objects, OSS monitors the access patterns of objects in the bucket, identifies cold data, and then converts the storage class of cold data. This way, cold data is stored by using storage classes that are different from the storage classes of hot data, which helps you reduce storage costs. | 2021-10-19 | All regions | Lifecycle rules based on the last access time |


## September 2021

















(https://www.alibabacloud.com/help/en/oss/user-guide/srr/#concept-2067125)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| SRR | SRR replicates objects across buckets within the same region in an automatic and asynchronous (near real-time) manner. Operations, such as the creation, overwriting, and deletion of objects, can be replicated from a source bucket to a destination bucket. | 2021-09-06 | All regions | SRR |


## August 2021

















(https://www.alibabacloud.com/help/en/oss/user-guide/oss-ddos-protection#concept-1955178)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#section-lfu-pgj-2yn)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| OSS DDoS protection for custom domain names | DDoS protection is supported for custom domain names of buckets. If you want to access a bucket by using the custom domain names that are mapped to the bucket when the bucket is under attack, add the custom domain names to the protection lists of Anti-DDoS instances in the OSS console. Up to five custom domain names can be added for each bucket. | 2021-08-13 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Shenzhen), and China (Hong Kong) | OSS DDoS protection |
| Cold Archive | Cold Archive is suitable for cold data that needs to be stored for a long period of time. Cold Archive objects have a minimum billable size of 64 KB and a minimum billable storage period of 180 days. The unit price of Cold Archive is lower than that of Archive. | 2021-08-01 | The single-zone redundancy storage mechanism is implemented for Cold Archive objects in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Germany (Frankfurt), UK (London), and UAE (Dubai). | Cold Archive |


## July 2021

















(https://www.alibabacloud.com/help/en/oss/upload-download-and-manage-objects-configure-object-tagging#task-1796814)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Object tagging for different versions of an object | After versioning is enabled for a bucket, object tagging can be configured for different versions of objects stored in the bucket. | 2021-07-15 | All regions | Configure object tagging |


## April 2021

















(https://www.alibabacloud.com/help/en/oss/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources#concept-ahc-tx4-j2b)


(https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication-overview/#concept-zjp-31z-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bucket Policy | Bucket policies can be configured by using graphical user interfaces (GUIs) and policy syntax. | 2021-04-16 | All regions | Configure bucket policies to authorize other users to access OSS resources |
| CRR improvement | CRR automatically and asynchronously (in near real time) replicates objects across buckets in different OSS regions. CRR can help you meet compliance requirements for cross-region disaster recovery and minimize the latency that occurs when customers from different regions access the data in the bucket. | 2021-04-23 | All regions | CRR |


## January 2021

















(https://www.alibabacloud.com/help/en/oss/user-guide/share-objects-by-url#task-2025983)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-ddos-protection#concept-1955178)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Export of multiple object URLs at a time | The URLs of multiple objects can be exported at a time. This makes it easier to export object URLs and share the URLs with third parties for object downloads or previews. | 2021-01-18 | All regions | Use object URLs |
| OSS DDoS protection | OSS DDoS protection can be used to protect buckets from DDoS attacks and maintain normal access to the buckets in the face of DDoS attacks. | 2021-01-07 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Shenzhen), and China (Hong Kong) | OSS DDoS protection |


## December 2020

















(https://www.alibabacloud.com/help/en/oss/back-to-origin-rules-overview#concept-ukn-3tf-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/zip-package-decompression#concept-x1g-cyg-4gb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Mirroring-based back-to-origin rules for objects in private buckets | Mirroring-based back-to-origin rules can be configured to obtain private objects in other buckets owned by the same Alibaba Cloud account. | 2020-12-17 | All regions | Overview |
| Decompression of a ZIP package to a subdirectory with the same name as the package | A ZIP package can be decompressed to a subdirectory that has the same name as the package. This way, files decompressed from different ZIP packages can be easily classified. | 2020-12-01 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Shenzhen), China (Chengdu), China (Hong Kong), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Japan (Tokyo), Germany (Frankfurt), UK (London), US (Virginia), and US (Silicon Valley) | Upload a ZIP package and automatically decompress it |


## November 2020

















-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb)


(https://www.alibabacloud.com/help/en/oss/configure-crr#concept-h3r-shf-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Service availability improvement of the Standard storage class | The service availability of the Standard storage class is improved: Standard ZRS: provides 99.995% service availability. Standard LRS: provides 99.99% service availability. | 2020-11-12 | All regions | Storage classes |
| CRR for encrypted objects | CRR supports replicating objects that are encrypted by using server-side encryption based on KMS-managed CMKs (SSE-KMS) or server-side encryption based on OSS-managed keys (SSE-OSS). | 2020-11-01 | All regions | Configure CRR |


## September 2020

















(https://www.alibabacloud.com/help/en/oss/delete-directories#concept-v5p-b4m-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Display of the list of directory deletion tasks in the OSS console | The progress of directory deletion tasks is displayed, and ongoing deletion tasks in the task list can be paused at any time. | 2020-09-28 | All regions | Delete directories |


## August 2020

















(https://www.alibabacloud.com/help/en/oss/configure-crr#concept-h3r-shf-vdb)


(https://www.alibabacloud.com/help/en/oss/configure-crr#concept-h3r-shf-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| CRR for objects with specific tags | When versioning is enabled for both the source and destination buckets and the Replication Policy parameter is set to Add/Change, a CRR rule can be configured to replicate objects that have specific tags to the destination bucket. | 2020-08-28 | If the source region is China (Hangzhou), the destination region can be a region other than China (Hangzhou) | Configure CRR |
| Transfer acceleration for CRR | Transfer acceleration is supported for CRR tasks. | 2020-08-28 | Between regions inside and outside the Chinese mainland | Configure CRR |


## July 2020




















(https://www.alibabacloud.com/help/en/oss/map-an-acceleration-endpoint#task-2347343)


(https://www.alibabacloud.com/help/en/oss/redundancy-for-fault-tolerance-configure-versioning#task-2326148)


(https://www.alibabacloud.com/help/en/oss/back-to-origin-rules-overview#concept-ukn-3tf-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Acceleration endpoint of regions outside the Chinese mainland for transfer acceleration | The following acceleration endpoint of regions outside the Chinese mainland is supported for transfer acceleration: oss-accelerate-overseas.aliyuncs.com. If you want to use a custom domain name that is not filed at the Ministry of Industry and Information Technology (MIIT) to enable transfer acceleration for a bucket outside the Chinese mainland, map the custom domain name to this endpoint. In other scenarios, we recommend that you use the global acceleration endpoint. | 2020-07-28 | All regions outside the Chinese mainland | Map a custom domain to an OSS-accelerated domain |
| Recovery and batch deletion of previous versions of objects in the OSS console | Specified previous versions of an object in a versioning-enabled bucket can be recovered, and multiple previous versions of objects can be deleted at a time by using the OSS console. | 2020-07-24 | All regions | Configure versioning |
| Mirroring-based back-to-origin with a forward slash (/) retained in the name of the origin file | If the name of the requested file in the origin starts with a forward slash (/), the forward slash is retained in the origin URL of the file. | 2020-07-20 | US (Silicon Valley), US (Virginia), and China (Hangzhou) | Overview |


## June 2020

















(https://www.alibabacloud.com/help/en/oss/map-accelerated-domain-names#concept-eyf-fvh-wfb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Auto CDN cache update supported for specified operations | Operations, such as PutObject and DeleteObject, can be specified to trigger auto CDN cache updates. When the specified operations are performed on objects, the CDN cache is automatically updated. | 2020-06-05 | All regions | Map accelerated domain names |


## May 2020

















-


-


(https://www.alibabacloud.com/help/en/oss/back-to-origin-rules-overview#concept-ukn-3tf-vdb)


(https://www.alibabacloud.com/help/en/oss/upload-download-and-manage-objects-upload-objects#task-zx1-4p4-tdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| MD5 verification and object name prefix replacement for mirroring-based back-to-origin | MD5 verification is supported for mirroring-based back-to-origin. When the response contains the Content-MD5 header, OSS checks whether the MD5 hash of the returned object matches the value of Content-MD5. If the MD5 hash matches the value of Content-MD5, the object is stored in OSS. Otherwise, the object is discarded. Replacement of object name prefixes is supported for mirroring-based back-to-origin. When OSS sends a request to the origin, the prefix in the object name is replaced with the specified prefix. | 2020-05-22 | All regions | Overview |
| Retention of directories uploaded by using drag upload | When a directory is uploaded to OSS by using drag upload in the OSS console, all subdirectories in the directory are retained. | 2020-05-22 | All regions | Upload objects |


## April 2020

















(https://www.alibabacloud.com/help/en/oss/user-guide/bucket-inventory#concept-2381539)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#section-lfu-pgj-2yn)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bucket inventories | You can use the bucket inventory feature to export information about specific objects in a bucket, such as the number, size, storage class, and encryption status. To list a large number of objects, we recommend that you use the bucket inventory feature instead of the GetBucket (ListObjects) operation. | 2020-04-30 | All regions | Bucket inventory |
| Improvement in OSS SLA-guaranteed availability | The SLA-guaranteed availability of Standard LRS objects is improved from 99.9% to 99.99%. The SLA-guaranteed availability of Standard ZRS objects is improved from 99.95% to 99.995%. | 2020-04-30 | All regions | Storage classes |
| Cold Archive | The Cold Archive storage class is available. Cold Archive is suitable for cold data that must be stored for a long period of time. Cold Archive objects have a minimum storage size of 64 KB and a minimum storage period of 180 days. The unit price of Cold Archive is lower than that of Archive. | 2020-04-22 (invitational preview) | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Germany (Frankfurt), UK (London), and UAE (Dubai) | Cold Archive |


## March 2020

















(https://www.alibabacloud.com/help/en/oss/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources#concept-ahc-tx4-j2b)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Temporary access authorization by using bucket policies | Bucket policies can be used to grant users temporary access permissions. | 2020-03-13 | All regions | Configure bucket policies to authorize other users to access OSS resources |


## December 2019

















(https://www.alibabacloud.com/help/en/oss/user-guide/limits#concept-pzk-crg-tdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Increase in the maximum number of buckets that can be created | The maximum number of buckets that can be created by using an Alibaba Cloud account in a region is increased to 100. | 2019-12-13 | All regions | Limits and performance metrics of OSS |


## November 2019

















(https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/#concept-jdg-4rx-bgb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Versioning | Versioning protects data at the bucket level. When versioning is enabled for a bucket, data that is overwritten or deleted in the bucket is saved as a previous version. After you enable versioning for a bucket, you can recover objects in the bucket to a previous version to protect your data from being accidentally overwritten or deleted. | 2019-11-15 | All regions | Overview |


## September 2019

















-

(https://www.alibabacloud.com/help/en/oss/manage-a-domain-map-custom-domain-names#concept-ozw-m2r-5fb)


(https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration#concept-1813960)


(https://www.alibabacloud.com/help/en/oss/user-guide/zrs#concept-ufs-g5m-cfb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Changes to the image preview feature | If OSS domain names are used in a browser to access image objects in buckets that are created on or after September 23, 2019, the objects are downloaded as attachments. To preview an image when you access the image from a browser, you must use a custom domain name. Buckets that are created before 00:00:00 September 23, 2019 are not affected. | 2019-09-23 | All regions | Map custom domain names |
| Transfer acceleration | Transfer acceleration is available. Transfer acceleration is implemented by using data centers that are distributed around the globe. When a data transfer request is sent, the request is resolved and routed over the optimal network path and protocol to the data center in which your bucket is located. Transfer acceleration improves user experience and reduces the amount of time needed for your business to deliver services to users. | 2019-09-10 | All regions | Access OSS using transfer acceleration |
| ZRS | ZRS stores multiple copies of your data across multiple zones in the same region. If a zone becomes unavailable, you can continue to access the data that is stored in other zones. ZRS provides 99.9999999999% (twelve 9's) data durability and 99.995% service availability. | 2019-09-09 (available for commercial use) | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), and Germany (Frankfurt) | Create a zone-redundant storage bucket |


## August 2019

















(https://www.alibabacloud.com/help/en/oss/user-guide/manage-bucket-tags#concept-1925905)


(https://www.alibabacloud.com/help/en/oss/user-guide/object-tagging-8#concept-zxf-jpy-pgb)


(https://www.alibabacloud.com/help/en/oss/user-guide/single-connection-bandwidth-throttling-4#concept-1013170)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bucket tagging | Bucket tags can be configured to classify and manage buckets. For example, you can list buckets that have specific tags and configure ACLs for buckets that have specific tags. | 2019-08-29 | All regions | Manage bucket tagging |
| Object tagging | Object tags can be configured to classify objects. You can configure lifecycle rules and ACLs for objects that have specific object tags. | 2019-08-29 | All regions | Tag objects |
| Single-connection bandwidth throttling | Bandwidth throttling for upload, download, and copy operations is supported to ensure sufficient bandwidth for other applications. | 2019-08-17 | All regions | Single-connection bandwidth throttling |


## June 2019

















(https://www.alibabacloud.com/help/en/oss/configure-server-side-encryption#concept-r55-np5-xgb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Server-side encryption | Server-side encryption of uploaded data is supported. When you upload data, OSS encrypts the received data and stores the encrypted data. When you download the data, OSS automatically decrypts the encrypted data. OSS returns the original data and declares that the data has been encrypted on the server in the returned HTTP header. | 2019-06-18 | All regions | Configure server-side encryption |


## January 2019

















(https://www.alibabacloud.com/help/en/oss/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources#concept-ahc-tx4-j2b)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Bucket Policy | A bucket policy is a resource-based authorization policy. Bucket policies can be configured by using GUIs in the OSS console. The bucket owner can grant other users the permissions to access the OSS resources that are stored in the bucket. | 2019-01-21 | All regions | Configure bucket policies to authorize other users to access OSS resources |


## December 2018

















(https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/#concept-eyb-1n5-1gb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Real-time log query | The real-time log query feature is supported. Real-time log query is based on the integration of Simple Log Service and OSS. This feature allows you to query and collect statistics about OSS access logs and audit access to OSS by using the OSS console, track exceptions, and troubleshoot problems. | 2018-12-26 | All regions | Real-time log query |


## November 2018

















-

(https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/convert-storage-classes#concept-p13-zmz-5db)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject#reference-mvx-xxc-5db)


-

(https://www.alibabacloud.com/help/en/oss/developer-reference/terraform-overview/#concept-qhs-4ms-zfb)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/use-terraform-to-manage-oss#concept-nqx-wps-zfb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Object storage class configuration and conversion | The storage class of an object can be set to Standard, IA, or Archive when you upload the object. The configuration of the storage class takes effect in real time. The CopyObject operation can be called to convert the storage class of an object. The amount of time required for the conversion is reduced from days to seconds. | 2018-11-10 | All regions | Storage classesConvert storage classesCopyObject |
| Terraform | The Terraform module is supported. The versions of OSS resources can be managed by using the Terraform module. For example, you can use Terraform to create buckets and manage objects. | 2018-11-07 | All regions | TerraformCreate a bucket by using Terraform |


## October 2018

















(https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| KMS-based server-side encryption | KMS-based server-side encryption is supported for objects. | 2018-10-20 | All regions | Configure server-side encryption |


## September 2018

















(https://www.alibabacloud.com/help/en/oss/developer-reference/selectobject#reference-lz1-r1x-b2b)


-

(https://www.alibabacloud.com/help/en/oss/user-guide/oss-retention-policies#concept-lnj-4rl-cfb)

-

(https://www.alibabacloud.com/help/en/oss/configure-retention-policies#concept-lnq-csm-cfb)


(https://www.alibabacloud.com/help/en/oss/user-guide/zrs#concept-ufs-g5m-cfb)


(https://www.alibabacloud.com/help/en/oss/user-guide/enable-pay-by-requester-1#concept-yls-jm2-2fb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| OSS Select | OSS Select is supported. The content of an object can be selected and obtained by using simple SQL statements. The amount of data that is transmitted from OSS can be reduced by using OSS Select to improve data retrieval efficiency. | 2018-09-28 | All regions | SelectObject |
| Retention policies | Retention policies for buckets are supported. A retention policy helps prevent objects in a bucket from being deleted or overwritten within a specific period of time. | 2018-09-28 | All regions | Retention policiesConfigure retention policies |
| ZRS | ZRS stores multiple copies of your data across multiple zones in the same region. If a zone becomes unavailable, you can continue to access the data that is stored in other zones. ZRS provides 99.9999999999% (twelve 9's) data durability and 99.995% service availability. | 2018-09-28 (public preview) | China (Shenzhen), China (Beijing), China (Hangzhou), China (Shanghai), and Singapore | Create a zone-redundant storage bucket |
| Pay-by-requester | Pay-by-requester is supported. When pay-by-requester is enabled for a bucket, the requester pays the request and traffic fees, and the bucket owner pays the storage costs. | 2018-09-27 | All regions | Pay-by-requester |


## August 2018

















(https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| SSE-KMS | Server-side encryption based on SSE-KMS is supported. A CMK ID is required to use KMS for server-side encryption. This allows you to implement bring your own key (BYOK) for server-side encryption in OSS. | 2018-08-14 | All regions | Configure server-side encryption |


## June 2018

















(https://www.alibabacloud.com/help/en/oss/developer-reference/client-side-encryption-1#concept-74371-zh)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Client-side encryption by using OSS SDK for Python | Client-side encryption by using OSS SDK for Python is supported. Data on the client can be encrypted locally by using OSS SDK for Python before the data is uploaded to OSS. However, in this scenario, you must manage the encryption process and the encryption key. | 2018-06-05 | All regions | Client-side encryption |


## May 2018

















(https://www.alibabacloud.com/help/en/data-lake-analytics/latest/read-and-write-oss-data-background-and-preparations)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Combination of OSS and DLA | Interactive queries and analysis of data in OSS can be performed by using the serverless architecture in the Data Lake Analytics (DLA) console. | 2018-05-31 | All regions | Background information and preparations |


## March 2018

















-

(https://www.alibabacloud.com/help/en/oss/developer-reference/resumable-upload-5)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/resumable-upload-9)


-

(https://www.alibabacloud.com/help/en/oss/manage-a-domain-map-custom-domain-names#concept-ozw-m2r-5fb)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-by-https-protocol#concept-b2m-5mq-5fb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Resumable upload by using OSS SDKs for Browser.js and Node.js | Resumable upload is supported by using OSS SDK for Browser.js and OSS SDK for Node.js. An object can be split into several parts that can be simultaneously uploaded. After all parts are uploaded, the parts are combined into a complete object. | 2018-03-07 | All regions | Resumable uploadResumable upload |
| SSL certificate hosting | To use a custom domain name to access OSS resources over HTTPS, you can host an SSL certificate in OSS. | 2018-03-05 | All regions | Map custom domain namesAccess OSS over HTTPS |


## January 2018

















(https://github.com/aliyun/aliyun-oss-ios-sdk/tree/master/OSSSwiftDemo)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Swift-based mobile apps by using OSS SDK for iOS | OSS SDK for iOS can be used by users who use Swift-based mobile apps. | 2018-01-18 | All regions | OSSSwiftDemo |


## December 2017

















-

(https://www.alibabacloud.com/help/en/oss/developer-reference/data-verification-3#concept-iyw-wmp-mfb)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/data-security-7#concept-cmk-hgg-4fb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| CRC-64 data verification by using OSS SDKs for iOS 2.8 and Android 2.5 | CRC-64 data verification is supported by using OSS SDKs for iOS 2.8 and Android 2.5. After CRC-64 is enabled and an object is uploaded or downloaded, the system checks whether the calculated CRC-64 value is the same as the CRC-64 value of the source data to ensure the integrity of the transmitted data. | 2017-12-21 | All regions | OSS SDK for Android: Data verificationOSS SDK for iOS: Data security |


## October 2017

















-

(https://www.alibabacloud.com/help/en/oss/standalone-deployment#concept-py5-2hh-wdb)

-

(https://www.alibabacloud.com/help/en/oss/distributed-deployment#concept-axx-n3h-wdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| ossimport | You can use ossimport to migrate data to OSS buckets. | 2017-10-23 | All regions | Standalone deploymentDistributed deployment |


## September 2017

















(https://www.alibabacloud.com/help/en/oss/configure-crr#concept-h3r-shf-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| CRR | CRR automatically and asynchronously (in near real time) replicates objects across buckets in different regions. CRR can also synchronize operations, such as the creation, overwriting, and deletion of objects, from a source bucket to a destination bucket. | 2017-09-15 | Regions in the Chinese mainland, US (Virginia), and US (Silicon Valley) | Configure CRR |


## July 2017

















-

(https://www.alibabacloud.com/help/en/oss/billing-overview#concept-n4t-mwg-tdb)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/restoreobject#reference-mfr-5bx-wdb)


-


-


-


(https://www.alibabacloud.com/help/en/oss/use-alibaba-cloud-accounts-to-log-on-to-the-oss-console#task-zx1-4p4-tdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Decrease in the unit price of the Archive storage class | The unit price of the Archive storage class is reduced by 45%. The minimum billable storage duration for Archive objects is changed to 60 days. | 2017-07-21 | All regions | Billing overviewRestoreObject |
| Official release of the new version of the OSS console | The new OSS console is available. The web page layouts and navigation system are optimized. Information aggregation on the Overview page is improved. The configuration and management of buckets and objects are improved. | 2017-07-01 | All regions | Use Alibaba Cloud accounts to log on to the OSS console |


## April 2017

















(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-59/#concept-cnr-3d4-vdb)


-

(https://www.alibabacloud.com/help/en/oss/user-guide/limits#concept-pzk-crg-tdb)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#reference-wdh-fj5-tdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| ossutil | The command line tool ossutil is available on Windows, Linux, and macOS. ossutil allows you to manage buckets and objects by using a rich set of commands. | 2017-04-26 | All regions | Overview |
| Increase in the maximum number of buckets that can be created | The maximum number of buckets that can be created by using an Alibaba Cloud account in a region is increased to 30. | 2017-04-24 | All regions | Limits and performance metrics of OSSPutBucket |


## December 2016

















(https://www.alibabacloud.com/help/en/oss/developer-reference/installation-8#concept-32056-zh)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| iOS SDK 2.6.0 | The HTTPS request access specifications of App Store are supported by OSS SDK for iOS 2.6.0. | 2016-12-16 | All regions | Installation |


## March 2016

















(https://www.alibabacloud.com/help/en/oss/user-guide/delete-parts#concept-r3h-c1y-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Part management | Lifecycle rules can be configured to periodically delete the parts that you no longer need. | 2016-03-10 | All regions | Delete parts |


## January 2016

















(https://www.alibabacloud.com/help/en/oss/back-to-origin-configuration-overview#concept-n34-q1z-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Back-to-origin | Data that is requested from the origin can be retrieved in multiple ways by configuring back-to-origin rules based on your requirements for specific operations, such as hot data migration and specific request redirection. | 2016-01-14 | All regions | Back-to-origin configurations |


## November 2015

















(https://www.alibabacloud.com/help/en/oss/developer-reference/installation-5#concept-32114-zh)


(https://www.alibabacloud.com/help/en/oss/user-guide/img-implementation-modes#concept-m4f-dcn-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Ruby SDK | OSS SDK for Ruby is officially released. | 2015-11-26 | All regions | Installation |
| IMG | By default, image processing (IMG) is enabled for buckets. | 2015-11-10 | All regions | IMG implementation modes |


## July 2015

















(https://www.alibabacloud.com/help/en/oss/user-guide/append-upload-11#concept-ls5-yhb-5db)


(https://www.alibabacloud.com/help/en/oss/user-guide/set-up-upload-callbacks-for-mobile-apps#concept-jqr-s1y-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Append upload | Content can be appended to appendable objects by calling the AppendObject operation. | 2015-07-18 | All regions | Append upload |
| Upload callbacks for application servers | An OSS-based direct data transfer service for mobile apps can be built, and upload callbacks can be configured. | 2015-07-08 | All regions | Set up upload callbacks for mobile apps |


## April 2015

















-

(https://www.alibabacloud.com/help/en/oss/ram-policy-overview/#concept-y5r-5rm-2gb)

-

(https://www.alibabacloud.com/help/en/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#concept-xzh-nzk-2gb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| RAM-based access | You can use Security Token Service (STS) to generate temporary access credentials to authorize a RAM user to access your OSS resources within a specific period of time. | 2015-04-26 | All regions | RAM PolicyUse temporary access credentials provided by STS to access OSS |


## October 2014

















(https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#concept-y2g-szy-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Lifecycle rule | The lifecycle rule feature is supported. The PutBucketLifecycle operation can be called to create a lifecycle rule that automatically deletes expired objects and parts to reduce storage costs. | 2014-10-20 | All regions | Lifecycle rules based on the last modified time |


## March 2014

















(https://www.alibabacloud.com/help/en/oss/user-guide/cors-settings#concept-bwn-tjd-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| CORS | Cross-origin access is supported by using cross-origin resource sharing (CORS), which is a standard cross-origin solution that is provided by HTML5. | 2014-03-15 | All regions | CORS |


## February 2014

















(https://www.alibabacloud.com/help/en/oss/user-guide/form-upload#concept-uln-lcb-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Form upload | Form upload is supported by calling the PostObject operation to upload an object of up to 5 GB in size. | 2014-02-12 | All regions | Form upload |


## November 2012

















(https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Server-side encryption | Server-side encryption for uploaded data is supported. When you upload data, OSS encrypts the received data and stores the encrypted data. When you download the data, OSS automatically decrypts the encrypted data. Then, OSS returns the data and declares that the data has been encrypted on the server in the returned HTTP header. | 2012-11-4 | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), South Korea (Seoul), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Thailand (Bangkok), Germany (Frankfurt), UK (London), and UAE (Dubai) | Configure server-side encryption |


## September 2012

















(https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names#concept-rz2-xg5-tdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| CNAME | A custom domain name can be mapped to a bucket. To map a custom domain name to a bucket, add a CNAME record that maps the custom domain name to the public domain name of the bucket. This way, you can use the custom domain name to access objects in the bucket. | 2012-09-04 | All regions | Access OSS through a custom domain name |


## August 2012

















(https://www.alibabacloud.com/help/en/oss/user-guide/logging#concept-t3h-4hd-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Logging | Logging can be configured for a bucket. A large number of logs are generated over time when OSS resources are accessed. Access logs that are generated by OSS on an hourly basis are written to a specified bucket as objects based on a predefined naming rule. | 2012-08-09 | All regions | Log storage |


## June 2012

















(https://www.alibabacloud.com/help/en/oss/user-guide/hosting-static-websites#concept-ynd-phc-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Static website hosting | Static website hosting can be configured for a bucket by calling the PutBucketWebsite operation. This way, the static website can be accessed by using the domain name of the bucket. | 2012-06-20 | All regions | Overview |


## March 2012

















(https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload#concept-wzs-2gb-5db)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Multipart upload | An object can be split into several parts that can be simultaneously uploaded. After all parts are uploaded, you can combine the parts into a complete object. | 2012-03-29 | All regions | Multipart upload |


## December 2011

















(https://www.alibabacloud.com/help/en/oss/user-guide/copy-objects-16#concept-lbg-2zy-5db)


(https://www.alibabacloud.com/help/en/oss/user-guide/hotlink-protection#concept-s5b-gjd-5db)


(https://www.alibabacloud.com/help/en/oss/configure-object-metadata#concept-pk1-sxl-vdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Object copy | Objects can be copied from a bucket to another bucket without modifying the object content. | 2011-12-16 | All regions | Copy objects |
| Hotlink protection | Hotlink protection can be configured for a bucket by calling the PutBucketReferer operation to configure the Referer whitelist and prevent unauthorized users from accessing data in OSS. | 2011-12-16 | All regions | Hotlink protection |
| HTTP header | HTTP headers can be configured to specify HTTP request policies, such as the cache policy and the forced object download policy. | 2011-12-16 | All regions | Configure object metadata |


## October 2011

















(https://www.alibabacloud.com/help/en/oss/user-guide/what-is-oss#concept-ybr-fg1-tdb)


| Feature | Description | Release date | Supported region | References |
| --- | --- | --- | --- | --- |
| Official release of OSS | Alibaba Cloud OSS is available for commercial use. | 2011-10-22 | All regions | What is OSS? |


Thank you! We've received your  feedback.