# How to save money with OSS

When you use OSS, you can reduce costs by planning storage classes based on your changing business data and using a combination of subscription and pay-as-you-go strategies.

## Notes


-

The unit prices in the following examples are based on the OSS pricing information published on the official Alibaba Cloud website on July 30, 2024. Prices are updated periodically, so the unit price for each billable item may vary. For the actual costs, refer to the [Pricing](https://www.alibabacloud.com/en/product/oss/pricing?_p_lc=1) page.

-

The following examples cover only common scenarios for data storage and data requests. If you use other OSS features, you may incur other billable items. For more information, see [Billable items](https://www.alibabacloud.com/help/en/oss/billable-items/).

## Confirm that bucket capacity growth meets expectations


When you store data in a bucket, you are charged storage fees based on the data storage capacity and storage class.


To obtain more detailed cost information, you can regularly query the OSS usage at the account level. You can export the CSV usage details to view the storage capacity data for each bucket in your account. This helps you determine whether the storage capacity growth meets your expectations. For more information, see [Query usage at the account level](https://www.alibabacloud.com/help/en/oss/query-resource-usage-of-an-alibaba-cloud-account).


If storage capacity grows unexpectedly, you can change the access control list (ACL) to private or configure a bucket policy. This prevents unauthorized operations on your OSS resources. Unauthorized operations include uploading many unexpected objects, which causes a sudden increase in storage capacity, or malicious access to objects, which results in high outbound traffic fees. For more information, see [Reduce the risk of unauthorized access due to account credential leaks](https://www.alibabacloud.com/help/en/oss/user-guide/reduce-the-risks-of-unauthorized-access-caused-by-accesskey-pair-leaks).

## Reduce outbound traffic and data retrieval costs for bucket owners


If a bucket owner authorizes other users to access data in the bucket over the internet and wants the requester to pay for the outbound traffic and data retrieval fees for Infrequent Access data, the owner can enable the pay-by-requester mode. For the specific steps, see [Pay-by-requester](https://www.alibabacloud.com/help/en/oss/user-guide/enable-pay-by-requester-1).


> IMPORTANT:

> NOTE: 


> NOTE: Important 

After the pay-by-requester mode is enabled, outbound data transfer plans cannot be used to offset outbound traffic over Internet fees that are generated when requesters download data from OSS to clients. In this mode, outbound traffic fees are charged based on actual usage.


## Configure lifecycle rules


To manage and reduce your OSS costs, you can use lifecycle rules to maximize cost-effectiveness.

### Transition storage classes based on data access frequency and response time


When you notice that a dataset is accessed less frequently or does not require real-time access, you can configure a lifecycle rule. The rule automatically transitions the data to a more cost-effective storage class without affecting access performance.











| Selection reference | Scenario description | Data access frequency |
| --- | --- | --- |
| Standard | Suitable for hot data that is frequently accessed and requires real-time reads. | A single file is accessed more than once per month. |
| Infrequent Access | Suitable for warm data that is accessed less frequently but requires real-time reads. | A single file is accessed less than once per month. |
| Archive Storage | Suitable for cold data that must be stored for a long time, is rarely accessed, but needs to be retrieved quickly. The restore time is about one minute. | A single file is accessed less than once per 90 days. |


> IMPORTANT:

> NOTE: 


> NOTE: Important 

If you set the data storage class to Archive Storage and do not enable real-time access of Archive objects, you cannot access the data in real time. You must restore the data before you can access it.


You can configure lifecycle rules for specific data using prefixes or tags to filter objects based on their characteristics and access frequency. You can automatically migrate cold data that is rarely accessed to the cost-effective Archive Storage class and keep frequently accessed hot data in the Standard storage class for faster read speeds. This practice helps optimize storage costs and improves data access efficiency.


The following example is provided to help you understand how to calculate storage costs and choose the best storage class for your needs.

### Clean up previous versions of objects


When you enable versioning for a bucket, objects that you overwrite or delete are saved as previous versions. If a bucket accumulates many previous versions, you can configure a lifecycle rule to delete the unnecessary versions and reduce storage costs.


Recommended action


You can configure a lifecycle rule to automatically delete previous versions of objects that reach a specified age.


![lifecycle.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3853175571/p825175.jpg)


The preceding configuration example shows that OSS automatically deletes previous versions of objects that are more than 200 days old. For the specific steps, see [Lifecycle rules based on last modification time](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time).

### Clean up expired parts to reduce storage costs


After a multipart upload, if you do not call the CompleteMultipartUpload operation to combine the parts, these parts remain in the bucket. They occupy storage space and incur storage fees.


Recommended action


You can configure a lifecycle rule to automatically delete parts after a specified number of days or on a specified date.


![碎片.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3853175571/p825218.jpg)


The preceding configuration example shows that OSS automatically deletes parts that were created more than two days ago. For the specific steps, see [Lifecycle rules based on last modification time](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time).

Thank you! We've received your  feedback.