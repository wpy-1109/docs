# Billable items, billing methods, and pricing

Object Storage Service (OSS) bills based on actual usage.


After data is stored in OSS, you will incur storage fees based on the duration of storage; request fees for each data upload, download, or access; and outbound data transfer fees for data distributed over the public internet. Additionally, enabling value-added services such as CDN Acceleration, Image Processing, Transfer Acceleration, and DDoS Protection will incur corresponding charges.
If your business has a stable access pattern with predictable storage volume, request volume, and outbound data transfer, we recommend purchasing resource packages to offset specific billing items and reduce costs. Resource packages must correspond precisely to their intended billing item (for example, an Outbound Data Transfer Package can only be used to offset outbound data transfer fees). Purchasing the wrong package type will result in a failure to apply the deduction.

## Unit price


For pricing details of OSS, see [OSS Fees](https://www.alibabacloud.com/product/oss/pricing).

## Billable items


The billable items of OSS are classified into the following types:


-

Basic billable items: Fees that most users incur when using OSS, including [storage fees](https://www.alibabacloud.com/help/en/oss/storage-fees) for data storage, [traffic fees](https://www.alibabacloud.com/help/en/oss/traffic-fees) for downloading objects from OSS buckets or delivering objects by using Alibaba Cloud CDN, and [API operation calling fees](https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees) for read and write requests.

-

Billable items for value-added features: Fees incurred by a minority of users who enable and use value-added features. To improve data processing efficiency or enhance user experience, the value-added features, such as image processing (IMG), transfer acceleration, and DDoS protection, are provided. For more information, see [Billable items for value-added features](https://www.alibabacloud.com/help/en/oss/value-added-billing-item/).

#### Billable items


The following figure shows the billable items of OSS.


![oss费用组成-cn-zh](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0192025471/p686969.png)

## Billing methods


OSS supports the following billing methods:


-

[Pay-as-you-go](https://www.alibabacloud.com/help/en/oss/pay-as-you-go-1#concept-2247263): By default, the pay-as-you-go billing method applies to all billable items. You are charged based on the actual usage of each billable item after you use resources. This billing method is ideal for scenarios in which resource usage fluctuates.

-

[Subscription (resource plans)](https://www.alibabacloud.com/help/en/oss/resource-plan/#concept-l43-j4h-tdb): OSS provides resource plans to offset fees of specific billable items, such as storage and traffic fees. You can purchase resource plans that cover specific billable items at favorable prices. Resources are consumed before fees are offset by resource plans. If the resource plans are exhausted, you are charged for excess resource usage on a pay-as-you-go basis. This billing method is suitable for scenarios in which resource usage is stable.


SCUs to offset storage fees


You can use [storage capacity units (SCUs)](https://www.alibabacloud.com/help/en/oss/scu#concept-2005963) to offset storage fees that are generated for using OSS and other Alibaba Cloud storage services.

## Free tier


New users activating OSS for the first time are eligible for our [Free tier](https://www.alibabacloud.com/help/en/oss/free-quota-for-new-users), which includes a free allowance of Standard (LRS) storage.

## Billing cycle


OSS calculates all resource usage by hour and charges you based on your actual usage.


> NOTE:

> NOTE: 


> NOTE: Note 

Storage fees are calculated in `USD per GB-month`, as indicated on the OSS pricing page. When you use the pay-as-you-go billing method, storage fees are calculated based on the following formula: `Storage fees = Actual storage usage (GB) × Unit price per hour`. Therefore, when you calculate storage fees charged based on actual storage usage, convert GB-month to GB-hour based on the following formula: `Unit price in USD per GB-hour` = Unit price in USD per GB-month/30/24. For example, the unit price for the storage usage of Standard locally redundant storage (LRS) objects is `USD 0.0173 per GB-month`, and the hourly pricing is approximately `USD 0.000024 per GB-hour (0.0173/30/24)`.


## References


-

[Billable items](https://www.alibabacloud.com/help/en/oss/billable-items/)

-

[Billing method](https://www.alibabacloud.com/help/en/oss/billing-method/)

-

[Hourly data of OSS](https://www.alibabacloud.com/help/en/oss/query-oss-billing-data-generated-on-an-hourly-basis)

-

[Query resource usage of an Alibaba Cloud account](https://www.alibabacloud.com/help/en/oss/query-resource-usage-of-an-alibaba-cloud-account)

-

[Query bills](https://www.alibabacloud.com/help/en/oss/query-bills)

-

[Cost optimization](https://www.alibabacloud.com/help/en/oss/faq-6/)

-

[Overdue payments](https://www.alibabacloud.com/help/en/oss/overdue-payments)

Thank you! We've received your  feedback.