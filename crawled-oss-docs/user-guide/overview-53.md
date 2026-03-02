# What are the storage classes of OSS

Object Storage Service (OSS) offers several storage classes, including Standard, Infrequent Access, Archive, Cold Archive, and Deep Cold Archive. These classes are designed for various data storage scenarios, from hot to cold data.


> NOTE:

> NOTE: 


> NOTE: Note 

For information about the pricing of each storage class, see [OSS Pricing](https://www.alibabacloud.com/product/oss/pricing). For information about the billing methods for each storage class, see [Storage fees](https://www.alibabacloud.com/help/en/oss/storage-fees).


## Standard


Standard provides highly reliable, highly available, and high-performance object storage for data that is frequently accessed. Standard is suitable for various business applications, such as social networking applications, image, audio, and video resource sharing applications, large websites, and big data analytics. ZRS (Zone-redundant storage) and LRS (Locally redundant storage) are supported for Standard objects.


-

Standard - Zone-redundant storage (Recommended)


For regions with three or more zones, ZRS uses a multi-zone mechanism to store your data redundantly across at least three zones in the same region. If one zone becomes unavailable, your data remains accessible. For regions with two zones, ZRS uses a dual-zone mechanism to store your data across both zones in the same region. If one zone becomes unavailable, your data also remains accessible. Currently, dual-zone ZRS is supported only for the Standard storage class.


> NOTE:

> NOTE: 


> NOTE: Note 

The China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), Germany (Frankfurt), and Malaysia (Kuala Lumpur) regions use a multi-zone data redundancy mechanism for data in the Standard storage class. The US (Silicon Valley), Philippines (Manila), Thailand (Bangkok), South Korea (Seoul), UAE (Dubai), and UK (London) regions use a dual-zone data redundancy mechanism for data in the Standard storage class. To use the dual-zone data redundancy mechanism in the US (Virginia) region, contact [Technical Support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex) to request activation.


-

Standard - Locally redundant storage


LRS stores multiple copies of your data on multiple devices of different facilities in the same zone. LRS provides data durability and availability even if hardware failures occur.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

LRS stores multiple data copies in a single zone. If the zone becomes unavailable, data in the zone is inaccessible. If your business application requires higher availability, we recommend that you use ZRS.


## Infrequent Access (IA)


IA provides highly durable storage at lower prices compared with Standard. IA has a minimum billable size of 64 KB and a minimum billable storage duration of 30 days. IA is suitable for data that is infrequently accessed, such as data accessed once or twice a month. You can access IA objects in real time. You are charged data retrieval fees when you access IA objects. ZRS and LRS are supported for IA objects.


> NOTE:

> NOTE: 


> NOTE: Note 

A minimum billable object size of 64 KB means that files smaller than 64 KB are billed as 64 KB. A minimum storage duration of 30 days means that if you store an object in the IA storage class for less than 30 days, you are charged an early deletion fee. For more information, see [Storage fees](https://www.alibabacloud.com/help/en/oss/storage-fees).


-

Infrequent Access Zone-Redundant Storage (Recommended)


ZRS stores multiple copies of your data across multiple zones in the same region. Your data is still accessible even if a zone becomes unavailable.


> NOTE:

> NOTE: 


> NOTE: Note 

The China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), Germany (Frankfurt), and Malaysia (Kuala Lumpur) regions use a multi-zone data redundancy mechanism for data in the IA storage class.


-

Infrequent Access - locally redundant storage


LRS stores multiple copies of your data on multiple devices of different facilities in the same zone. LRS provides data durability and availability even if hardware failures occur.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

LRS stores multiple data copies in a single zone. If the zone becomes unavailable, data in the zone is inaccessible. If your business application requires higher availability, we recommend that you use ZRS.


## Archive Storage


Archive provides high-durability storage at lower prices compared with Standard and IA. Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 60 days. You can access an Archive object after it is restored or real-time access of Archive objects is enabled. The amount of time that is required to restore an Archive object is approximately 1 minute. You are charged data retrieval fees if you restore an Archive object. If you access an Archive object after real-time access of Archive objects is enabled, you are charged Archive data retrieval fees based on the size of the Archive object. Archive is suitable for data that needs to be stored for a long period of time and is rarely accessed, such as archival data, medical images, scientific materials, and video footage. ZRS and LRS are supported for Archive objects


> NOTE:

> NOTE: 


> NOTE: Note 

A minimum billable object size of 64 KB means that files smaller than 64 KB are billed as 64 KB. A minimum storage duration of 60 days means that if you store an object in the Archive Storage class for less than 60 days, you are charged an early deletion fee. For more information, see [Storage fees](https://www.alibabacloud.com/help/en/oss/storage-fees).


-

Archive Storage - Zone-redundant storage (Recommended)


ZRS stores multiple copies of your data across multiple zones in the same region. Your data is still accessible even if a zone becomes unavailable.


> NOTE:

> NOTE: 


> NOTE: Note 

The China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), Germany (Frankfurt), and Malaysia (Kuala Lumpur) regions use a multi-zone data redundancy mechanism for data in the Archive Storage class.


-

Archive Storage - Locally redundant storage


LRS stores multiple copies of your data on multiple devices of different facilities in the same zone. LRS provides data durability and availability even if hardware failures occur.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

LRS stores multiple data copies in a single zone. If the zone becomes unavailable, data in the zone is inaccessible. If your business application requires higher availability, we recommend that you use ZRS.


## Cold Archive


Cold Archive provides highly durable storage at lower prices compared with Archive. Cold Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 180 days. You must restore a Cold Archive object before you can access it. The amount of time required to restore a Cold Archive object varies based on the object size and restoration priority. You are charged data retrieval fees and API operation calling fees when you restore Cold Archive objects. Cold Archive is suitable for cold data that needs to be stored for an extended period of time, including data that must be retained for an extended period of time to meet compliance requirements, raw data that is accumulated over an extended period of time in the big data and AI fields, retained media resources in the film and television industries, and archived videos in the online education industry. Only LRS is supported for Cold Archive objects.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

LRS data is stored in a specific zone. If the zone fails, the data stored within becomes inaccessible. If your business application requires higher availability, we recommend that you use ZRS (supported for Standard, IA and Archive objects).


> NOTE:

> NOTE: 


> NOTE: Note 

-

The single-zone redundancy storage mechanism is implemented for Cold Archive objects in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Germany (Frankfurt), UK (London), and UAE (Dubai).

-

A minimum billable object size of 64 KB means that files smaller than 64 KB are billed as 64 KB. A minimum storage duration of 180 days means that if you store an object in the Cold Archive storage class for less than 180 days, you are charged an early deletion fee. For more information, see [Storage fees](https://www.alibabacloud.com/help/en/oss/storage-fees).


## Deep Cold Archive


Deep Cold Archive provides highly durable storage at lower prices compared with Cold Archive. Deep Cold Archive has a minimum billable size of 64 KB and a minimum billable storage duration of 180 days. You must restore a Deep Cold Archive object before you can access it. The amount of time that is required to restore a Deep Cold Archive object varies based on the object size and restoration priority. You are charged data retrieval fees and API operation calling fees when you restore Deep Cold Archive objects. Deep Cold Archive is suitable for extremely cold data that needs to be stored for an extremely long period of time, including raw data that is accumulated over an extended period of time in the big data and AI fields, retained media resources, regulatory and compliance documents, and data that is archived by using tapes. Only LRS is supported for Deep Cold Archive objects.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

LRS data is stored in a specific zone. If the zone fails, the data stored within becomes inaccessible. If your business application requires higher availability, we recommend that you use ZRS (supported for Standard, IA and Archive objects).


> NOTE:

> NOTE: 


> NOTE: Note 

-

The single-zone redundancy storage mechanism is implemented for Deep Cold Archive objects in the following regions: China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), and Singapore.

-

A minimum billable object size of 64 KB means that files smaller than 64 KB are billed as 64 KB. A minimum storage duration of 180 days means that if you store an object in the Deep Cold Archive storage class for less than 180 days, you are charged an early deletion fee. For more information, see [Storage fees](https://www.alibabacloud.com/help/en/oss/storage-fees).


## Comparison of storage classes


























| Storage class | Storage redundancy type | Data durability | Service availability | Minimum metering unit | Minimum storage duration | Data access characteristics | Access latency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Standard | Zone-redundant (2 AZs) | 99.9999999999% (12 nines) | 99.99% | Billed based on actual object size | None | More than one access per object per month | Real-time access |
| Standard | Zone-redundant (Multi-AZ) | 99.9999999999% (12 nines) | 99.995% | Billed based on actual object size | None | More than one access per object per month | Real-time access |
| Infrequent Access | 99.50% | 64 KB | 30 days | Less than one access per object per month | Real-time access |
| Archive Storage | 99.50% | 64 KB | 60 days | Less than one access per object per 90 days | It supports both real-time access through direct reads and access only after restoration.Restoration time: 1 minute |
| Standard | Locally redundant | 99.999999999% (11 nines) | 99.99% | Billed based on actual object size | None | More than one access per object per month | Real-time access |
| Infrequent Access | 99.00% | 64 KB | 30 days | A single file is accessed less than once a month. | Real-time access |
| Archive Storage | 99.00% | 64 KB | 60 days | Less than one access per object per 90 days | It supports both real-time access of Archive objects and reading restored objects.Restoration time: 1 minute |
| Cold Archive | 99.00% | 64 KB | 180 days | A single file is accessed less than once a year. | It can be read only after it is restored.Restoration time: 1 to 12 hours |
| Deep Cold Archive | 99.00% | 64 KB | 180 days | Less than one access per object per year | Data must be restored before it can be read.Restoration time: 12 or 48 hours |


## References


-

By default, objects that you upload to a bucket are assigned the Standard storage class. The Standard storage class is suitable for scenarios that require frequent access and low latency. If you find that some objects no longer require frequent access, or if you want to reduce storage costs, you can convert the objects from the Standard storage class to a more cost-effective storage class, such as Infrequent Access or Archive Storage. For more information, see [Convert storage classes](https://www.alibabacloud.com/help/en/oss/user-guide/convert-storage-classes).

-

The Deep Cold Archive storage class provides a highly durable, low-cost storage service that is suitable for extremely cold data that requires ultra long-term retention. For more information, see [Best practices for using Deep Cold Archive](https://www.alibabacloud.com/help/en/oss/user-guide/deep-cold-archive-storage-usage-best-practices).

-

To understand why the storage capacity of the source storage class does not decrease after you convert an object's storage class and how to resolve this issue, see [Why does the capacity of the source storage class remain unchanged after a storage class conversion?](https://www.alibabacloud.com/help/en/oss/why-does-the-storage-capacity-of-the-source-object-remain-unchanged-after-the-storage-type-conversion).

Thank you! We've received your  feedback.