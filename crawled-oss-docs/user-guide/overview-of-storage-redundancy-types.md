# OSS storage redundancy types

Object Storage Service (OSS) provides two storage redundancy types: zone-redundant storage (ZRS) and locally redundant storage (LRS). Each type distributes data copies across different scopes to protect against failures.

## Choose a redundancy type


| Factor | ZRS | LRS |
| --- | --- | --- |
| Scope | Multiple availability zones (AZs) in a region | Single AZ |
| Data durability | 99.9999999999% (12 nines) | 99.999999999% (11 nines) |
| Service availability | Up to 99.995% (Standard) | Up to 99.99% (Standard) |
| Failure protection | Survives a full AZ outage | Survives hardware failures within an AZ |
| Storage classes | Standard, Infrequent Access, Archive Storage | Standard, Infrequent Access, Archive Storage, Cold Archive, Deep Cold Archive |
| Region coverage | Select regions | All public cloud regions |


Choose ZRS for production workloads that require high availability and protection against AZ-level failures.


Choose LRS when Cold Archive or Deep Cold Archive storage classes are required, as these classes support only LRS.

## Zone-redundant storage (ZRS)


ZRS distributes data copies across multiple availability zones in a region. In regions with three or more zones, copies are stored across at least three AZs. In regions with two zones, copies are stored across both AZs. Data remains accessible even if one AZ becomes unavailable.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

ZRS stores data within a single region. If the entire region becomes unavailable, the data is inaccessible. To protect against region-level failures, use [cross-region replication](https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication-overview/) to back up data to a different region.


## Locally redundant storage (LRS)


LRS stores redundant copies on multiple devices across multiple facilities within a single availability zone (AZ). This protects data against hardware failures.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

LRS stores data within a single AZ. If that AZ becomes unavailable, the data is inaccessible. For higher availability, use [zone-redundant storage (ZRS)].


## Durability and availability by storage class

### ZRS


| Storage class | Region | Data durability | Service availability |
| --- | --- | --- | --- |
| Standard | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), Malaysia (Kuala Lumpur), Germany (Frankfurt) | 99.9999999999% (12 nines) | 99.995% |
| Standard | US (Silicon Valley), US (Virginia), Philippines (Manila), Thailand (Bangkok), South Korea (Seoul), UAE (Dubai), UK (London) | 99.9999999999% (12 nines) | 99.99% |
| Infrequent Access | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), Malaysia (Kuala Lumpur), Germany (Frankfurt) | 99.9999999999% (12 nines) | 99.50% |
| Archive Storage | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), China (Hong Kong), Japan (Tokyo), Singapore, Indonesia (Jakarta), Malaysia (Kuala Lumpur), Germany (Frankfurt) | 99.9999999999% (12 nines) | 99.50% |


> NOTE:

> NOTE: 


> NOTE: Note 

To enable ZRS in the US (Virginia) region, contact [Technical Support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex).


### LRS


| Storage class | Region | Data durability | Service availability |
| --- | --- | --- | --- |
| Standard | All public cloud regions | 99.999999999% (11 nines) | 99.99% |
| Infrequent Access | All public cloud regions | 99.999999999% (11 nines) | 99.00% |
| Archive Storage | All public cloud regions | 99.999999999% (11 nines) | 99.00% |
| Cold Archive | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Mexico, Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Germany (Frankfurt), UK (London), UAE (Dubai) | 99.999999999% (11 nines) | 99.00% |
| Deep Cold Archive | China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), China (Ulanqab), China (Shenzhen), Singapore | 99.999999999% (11 nines) | 99.00% |


## Related operations


-

[Create a zone-redundant storage bucket](https://www.alibabacloud.com/help/en/oss/user-guide/zrs)

-

[Convert the storage redundancy type of a bucket](https://www.alibabacloud.com/help/en/oss/user-guide/converting-storage-redundancy-types) (LRS to ZRS)

Thank you! We've received your  feedback.