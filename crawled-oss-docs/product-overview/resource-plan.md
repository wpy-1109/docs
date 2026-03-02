# Resource plans

By default, OSS uses the pay-as-you-go billing method. For better value, you can purchase an OSS resource plan to offset fees for resources such as storage and traffic. If a resource plan expires or its quota is exhausted, any excess usage is automatically billed on a pay-as-you-go basis.


> NOTE:

> NOTE: 


> NOTE: Note 

OSS offers free trial resource plans for some features. For more information, see [View OSS trial resource plans](https://free.aliyun.com/?searchKey=oss&spm=a311a.7996332.0.0.3e9930807zHxhz&scm=20140722.M_9553144.P_154.MO_1802-ID_9553144-MID_9553144-CID_20080-ST_7663-V_1).


## Resource plan types

















| Resource plan | Description |
| --- | --- |
| Storage plan | Deducts storage fees for OSS files |
| Standard zone-redundant storage package | Deducts storage fees for OSS files of the standard zone-redundant storage class |
| Standard LRS plan | Deducts storage fees for OSS files of the Standard LRS class |
| Locally Redundant Infrequent Access Storage Package | Deducts storage fees for OSS files of the IA LRS class |
| Archive ZRS plan | Deducts storage fees for OSS files of the Archive ZRS class |
| Cold Archive LRS plan | Deducts storage fees for OSS files of the Cold Archive LRS class |
| Data transfer plan | Deducts fees for traffic generated during OSS usage |
| Outbound data transfer plan | Deducts fees for traffic generated when data is transferred from OSS to a client over the Internet |
| Transfer acceleration plan | Deducts fees for acceleration traffic generated when users access OSS through an acceleration endpoint |
| Anti-DDoS basic plan | Deducts fees for reserved Anti-DDoS instance resources |


## Purchase recommendations

### Recommendation 1: Choose a resource plan based on your scenario


A common combination is a storage plan and an outbound data transfer plan. The storage plan offsets storage fees for OSS. The outbound data transfer plan offsets traffic fees for accessing OSS files over the Internet.








| Scenario | Resource plan for deduction |
| --- | --- |
| Store files such as text, images, audio, and video in OSS using the Standard LRS storage class | Standard LRS plan |
| Browse or download files from OSS over the Internet | Outbound data transfer plan |


For information about the scenarios for all resource plan types, see [Resource plan types].

### Recommendation 2: Choose a resource plan based on the billable items in your bill


If you have an OSS bill, you can select a resource plan type based on the billable items in your [detailed bills](https://usercenter2-intl.console.alibabacloud.com/finance/expense-report/expense-detail-by-instance).


For example, if a billable item is Standard LRS Capacity, you can purchase a Standard LRS plan to offset this fee.


![计费项](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1823391661/p480255.png)

### Recommendation 3: Choose a resource plan size based on the usage in your bill


If you already have an OSS bill, we recommend that you choose the resource plan specifications based on the usage shown in your [Detailed Bills](https://usercenter2-intl.console.alibabacloud.com/finance/expense-report/expense-detail-by-instance).


For example, if your hourly usage for Standard LRS Capacity is 40 GB, you can purchase a 40 GB Standard LRS plan to offset this fee.

### Recommendation 4: How to troubleshoot hourly charges after purchasing a resource plan


-

On the [Billing Details](https://usercenter2-intl.console.alibabacloud.com/finance/expense-report/expense-detail-by-instance) page, view the type, usage, and usage time of the billable items.

-

On the [Resource Plans](https://usercenter2-intl.console.alibabacloud.com/ri/summary?commodityCode=) page, view the type, total quota, and effective period of your active resource plans.

-

Compare the billable item with the resource plan.








| Example issue | Solution |
| --- | --- |
| The bill includes a billable item for outbound traffic over Internet (NetworkOut), but you do not have an active outbound data transfer plan. | Purchase an outbound data transfer plan. |
| The bill includes a billable item for Standard LRS capacity, but you do not have an active Standard LRS plan. | Purchase a Standard LRS plan. |
| The bill shows 100 GB of hourly usage for the Standard LRS capacity billable item, but your active Standard LRS plan has a total quota of only 40 GB. | Upgrade the Standard LRS plan to 100 GB. |
| The bill was generated before the resource plan was purchased. | None |


## Deduction limits


-

OSS resource plans can only offset fees incurred by the current Alibaba Cloud account. They cannot be shared across different accounts.

-

OSS resource plans are specific to the OSS service and cannot be used to offset fees for other products.

-

OSS resource plans can only offset fees generated after the plan is purchased. They cannot be used to offset fees incurred before the purchase.

-

A resource plan of a specific type can only offset fees for its corresponding billable items, not all fees. For more information, see [Resource plan types].

-

Region-specific OSS resource plans can only offset fees for corresponding billable items in that region. Resource plans that are applicable to all regions in the Chinese mainland can offset fees for corresponding billable items across multiple regions in the Chinese mainland. For more information, see [Deduction regions].

## Deduction methods











-


-





-


-


-


-


-


-


-


-











| Deduction method | Resource plan | Example |
| --- | --- | --- |
| Fixed total amount | Storage planAnti-DDoS basic plan | Provides a fixed hourly quota. Unused quota from one hour cannot be carried over to the next. Storage planFor example, a 10 TB storage plan can deduct up to 10 TB of storage capacity per hour.If your storage usage is 9 TB in the first hour, the fee is fully covered by the plan.If your usage is 10 TB in the second hour, the fee is fully covered by the plan.If your usage is 11 TB in the third hour, the plan covers 10 TB, and the excess 1 TB is billed on a pay-as-you-go basis.Anti-DDoS basic planFor example, if you purchase two single-instance Anti-DDoS basic plans with a six-month duration, the plans can deduct the reserved resource fees and early release fees for up to two Anti-DDoS instances per hour.If you have only one Anti-DDoS instance in the first hour, the fee is fully covered by the plan.If you have two instances in the second hour, the fees are fully covered by the plan.If you have three instances in the third hour, the plan covers the fees for two instances, and the excess instance is billed on a pay-as-you-go basis. |
| Monthly subscription | Outbound data transfer plan | Provides a fixed monthly quota. The quota resets on the first day of the next month. Unused quota from the current month cannot be carried over.For example, if you purchase a 100 GB outbound data transfer plan for one month on the 18th of the current month, the plan can deduct up to 100 GB of outbound traffic over the Internet from the 18th to the end of the month. Any excess traffic is billed on a pay-as-you-go basis. On the first day of the next month, the quota resets, and the plan can again deduct up to 100 GB of traffic from the 1st to the 18th of that month. Any excess traffic is billed on a pay-as-you-go basis. |
| Decreasing Total Type | Transfer acceleration plan | Deducts usage from the total quota until the quota is depleted or the plan expires.For example, if you purchase a 5 TB transfer acceleration plan with a three-month duration, you have a total quota of 5 TB for transfer acceleration traffic deduction over the three months. Any excess traffic is billed on a pay-as-you-go basis. |


## Deduction regions


When you purchase an OSS resource plan, you must specify a region. The only exception is Anti-DDoS basic plans, which do not require a region to be specified. A region-specific resource plan can only offset fees in the specified region.


> NOTE:

> NOTE: 


> NOTE: Note 

An Anti-DDoS basic plan can offset usage fees in any region where Anti-DDoS instances can be enabled. However, within the same hour, it can only offset usage for a single instance in a single region. If you have Anti-DDoS usage in multiple regions within the same hour, you must purchase multiple Anti-DDoS basic plans to offset the fees.








| Region type | Description |
| --- | --- |
| Global Regions | Deducts usage fees for corresponding resources in all regions. The quota can be shared across regions. |
| Region-specific① | Deducts usage fees for corresponding resources in a specific region. The quota cannot be shared across regions.② |
| Chinese mainland general-purpose① | Deducts usage fees for corresponding resources in multiple regions within the Chinese mainland. The quota can be shared across regions.③ |
| Transfer acceleration region | Deducts fees for upload and download acceleration traffic generated when you use an acceleration endpoint to access OSS from one region to another. |
| Transfer acceleration M2M | Deducts fees for upload and download acceleration traffic (AccM2MIn, AccM2MOut) generated when you use an acceleration endpoint to access OSS within the Chinese mainland. |
| Transfer acceleration M2O_O2M | Deducts fees for upload and download acceleration traffic (AccM2OIn, AccM2OOut, AccO2MIn, AccO2MOut) generated when you use an acceleration endpoint to access OSS between the Chinese mainland and regions outside the Chinese mainland. |
| Transfer acceleration O2O | Deducts fees for upload and download acceleration traffic (AccO2OIn, AccO2OOut) generated when you use an acceleration endpoint to access OSS between regions outside the Chinese mainland. |


①You can purchase both a Chinese mainland general-purpose resource plan and a region-specific resource plan for a region in the Chinese mainland. When fees are offset, the region-specific plan is applied first. If its quota is exhausted, the general-purpose plan is applied. Any remaining excess usage is billed on a pay-as-you-go basis.


②For example, a resource plan for China (Qingdao) can only offset usage fees for corresponding resources in China (Qingdao). It cannot be used for resources in other regions.


③For information about the Chinese mainland regions supported by the Chinese mainland general-purpose resource plans, see [Supported regions for Chinese mainland general-purpose resource plans].

### Supported regions for Chinese mainland general-purpose resource plans








| Resource Plan | Region |
| --- | --- |
| standard zone-redundant storage package | China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Nanjing - Local Region - Decommissioning), China (Fuzhou - Local Region - Decommissioning) |
| Outbound data transfer plan |


## Supported operations


> NOTE:

> NOTE: 


> NOTE: Note 

✓ indicates that the operation is supported for the resource plan. × indicates that the operation is not supported.





(https://www.alibabacloud.com/help/en/oss/purchase-resource-plans#task-2190990)


(https://www.alibabacloud.com/help/en/oss/upgrade-resource-plans#concept-pw3-wvm-tdb)


(https://www.alibabacloud.com/help/en/oss/renew-resource-plans#task-ohy-w4m-tdb)


(https://www.alibabacloud.com/help/en/oss/purchase-resource-plans#task-2190990)


(https://www.alibabacloud.com/help/en/oss/view-the-usage-details-of-a-resource-plan#task-2191203)


| Resource plan | Purchase | Upgrade | Renew | Stack① | Details |
| --- | --- | --- | --- | --- | --- |
| Standard Zone-Redundant Storage Package | ✓ | ✓ | ✓ | ✓ | ✓ |
| Standard LRS plan | ✓ | ✓ | ✓ | × | ✓ |
| Infrequent Access Locally Redundant Storage Package | ✓ | ✓ | ✓ | × | ✓ |
| Cold Archive LRS plan | ✓ | ✓ | ✓ | ✓ | ✓ |
| Outbound data transfer plan | ✓ | × | ✓ | ✓ | ✓ |
| Transfer acceleration plan | ✓ | × | × | ✓ | ✓ |
| Anti-DDoS basic plan | ✓ | × | ✓ | ✓ | ✓ |


①You can purchase multiple resource plans of the same type. When you stack multiple resource plans of the same type, the one that expires first is applied first. For example, you purchase a 1 TB Chinese mainland general-purpose outbound data transfer plan with a one-year duration on February 1, 2022. You then purchase another 1 TB Chinese mainland general-purpose outbound data transfer plan with a three-month duration on March 1, 2022. In this case, the outbound data transfer plan purchased on March 1, 2022 is applied first.

## References


-

[Resource plan purchase guide](https://www.alibabacloud.com/help/en/oss/purchase-resource-plans)

-

[Resource plan upgrade guide](https://www.alibabacloud.com/help/en/oss/upgrade-resource-plans)

-

[Resource plan renewal guide](https://www.alibabacloud.com/help/en/oss/renew-resource-plans)

-

[Resource Plan Usage Details](https://www.alibabacloud.com/help/en/oss/view-the-usage-details-of-a-resource-plan)

-

[Resource plan refund guide](https://www.alibabacloud.com/help/en/oss/refund-resource-plans)

-

[Resource plans](https://www.alibabacloud.com/help/en/oss/package-faq/)


Thank you! We've received your  feedback.