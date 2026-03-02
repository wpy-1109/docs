# FAQ about OSS

This topic provides answers to some commonly asked questions about Object Storage Service (OSS).

## General FAQ


-

What is Alibaba Cloud OSS?


Alibaba Cloud OSS is a secure, cost-effective, highly durable, and scalable storage service that allows you to store a large volume of data. OSS is designed to provide data durability of at least 99.9999999999% (twelve 9's) and service availability of at least 99.995%.

-

What are the features of OSS?


OSS supports RESTful API operations that do not need to be performed in the OSS console. You can store and access data from all applications anytime and anywhere. OSS is highly scalable. You are charged only for the resources that you use. You can scale OSS resources based on your business requirements without compromising performance or durability.


Aside from the API operations, OSS provides OSS SDKs and migration tools that you can use to easily transfer large amounts of data to and from OSS. OSS provides storage classes that are intended for different storage scenarios. For example, you can store images, audio files, and video files used in your apps and websites as Standard objects for frequent access and store infrequently accessed data as Infrequent Access (IA), Archive, Cold Archive, or Deep Cold Archive objects to reduce the total costs of storage over time.


For more information, see [Functions and features](https://www.alibabacloud.com/help/en/oss/functions-and-features#concept-ilc-x31-tdb).

-

Who are the intended users of OSS?


OSS is suitable for users who need to store large volumes of data. These users include app and software developers, game development enterprises, and webmasters of online communities, media sharing sites, and e-commerce websites.


-

Audio, video, and image applications: You can use the OSS API to implement a large number of distributed data storage solutions, such as short video storage, live video recording, video on demand, photo-sharing social networking, and video albums.

-

Education: Online education platforms, such as K12, can store their large volumes of data in OSS and use Alibaba Cloud CDN for content delivery.

-

AI and IoT: In the autonomous driving field, you can migrate collected training data to OSS by using Data Transport. For IoT-powered video surveillance systems, such as systems used for residential or community security, the video data captured by cameras is directly uploaded to OSS to allow real-time viewing by using mobile apps and tiered data storage based on lifecycle rules. This reduces storage costs while maintaining compliance.

-

Cinematic rendering: OSS offers large and scalable storage for filmmaking and media assets. OSS can be used together with Intelligent Media Management (IMM) to enable storage and intelligent data processing.

-

Genomics: OSS provides a scalable storage solution for data generated across upstream and downstream applications such as gene sequencing, delivery, and diagnostics. With OSS, you can store raw genomic data cost-effectively and leverage integrated cloud compute services to run complex analytics and machine learning models.

-

What data does OSS store?


OSS is suitable for storing attachments, high-definition images, audio and video objects, and backup objects for forums, websites, and software applications, as well as objects for various applications, file synchronization software, and online storage systems.

-

What are the advantages of OSS compared with local storage solutions?


OSS allows developers to fully use the economy of scale provided by Alibaba Cloud at minimal cost without additional investments or performance degradation. Developers can focus on their own innovations without performance bottlenecks and security risks that may occur due to business growth. OSS is cost-effective and easy to use.

-

What is the upper limit of the data volume that OSS can support?


OSS does not impose limits on the total storage capacity and the storage capacity of a bucket. You can upload an object whose size is up to 5 GB by using the OSS console. To upload an object whose size is larger than 5 GB, you can use [multipart upload](https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload#concept-wzs-2gb-5db), [Graphical management tool ossbrowser 1.0](https://www.alibabacloud.com/help/en/oss/developer-reference/graphical-management-tools-ossbrowser-1-0/), or [ossutil command line interface 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/).

-

What are the storage classes of OSS?


OSS provides the following storage classes to cover various data storage scenarios from hot data storage to cold data storage: Standard, Infrequent Access (IA), Archive, Cold Archive, and Deep Cold Archive. For more information, see [Storage classes](https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#concept-fcn-3xt-tdb).

-

How do I select an appropriate storage class for my data in OSS?


The billable size, storage duration, restoration time, and data retrieval vary with the storage class. You can store data in different storage classes based on the data access frequency and application scenarios to reduce storage costs.


For example, if 70% of your data is not accessed for more than 30 days, this portion of data is considered cold data. We recommend that you store cold data in the IA or Archive storage class. You can also configure lifecycle rules. This allows OSS to automatically change the storage class of cold data to IA or Archive based on the rules. In most cases, data that is accessed less frequently incurs lower storage costs.


If you want to access Archive or Cold Archive data, the data must be restored first, which requires minutes or even hours to complete. Data retrieval fees are generated when you restore data.

-

Does Alibaba Cloud use data that is stored in OSS?


Alibaba Cloud does not use or disclose your data without your authorization. Alibaba Cloud processes user data only based on your service requirements or requirements of laws and regulations. For more information, see [Alibaba Cloud International Website Product Terms of Service](https://www.alibabacloud.com/help/en/legal/latest/alibaba-cloud-international-website-product-terms-of-service-v-3-8-0).

-

Does Alibaba Cloud use OSS to store their own data?


Yes, Alibaba Cloud developers use OSS to store authorized data for various projects. These projects rely on OSS to perform key business operations.

-

How does OSS ensure service availability when traffic spikes occur?


OSS is designed to handle traffic spikes that may occur due to traffic that is sent from Internet applications. Pay-as-you-go pricing and unlimited capacity ensure that your service is not interrupted due to traffic spikes. OSS balances loads to prevent applications from being affected by traffic spikes.

-

How is data organized in OSS?


OSS is a distributed object storage service that stores data in the key-value pair format. When you store an object, you must specify an object name (key). The key can then be used to obtain the content of the object.


Keys can also be used to simulate features of directories. OSS uses a flat structure for objects instead of a hierarchical structure. All elements are stored as objects in buckets. However, OSS supports directories as a concept to group objects and simplify management. When you use API operations or OSS SDKs to configure an object, you can specify the key value, which is a full name that includes a prefix for the object to manage other objects. For example, if you set the key of an object to `dir/example.jpg`, a directory named `dir` is created in the current bucket and an object named `example.jpg` is created in the dir directory. If you delete the `dir/example.jpg` object, the `dir` directory is also deleted.

-

What are the intelligent features of OSS?


OSS seamlessly integrates with various computing frameworks, including Hadoop, Spark, MaxCompute, Batch Compute, High Performance Computing (HPC), and E-MapReduce (EMR). To simplify and facilitate user operations, OSS provides easy-to-use SaaS services, including image processing and content detection. In addition, OSS can work with IMM to improve the efficiency of media management and distribution by using various media processing algorithms.

-

How do I get started with OSS?


-

Before you use OSS, make sure that you have created an Alibaba Cloud account. For more information, see [Create an Alibaba Cloud account](https://account.alibabacloud.com/register/intl_register.htm?spm=a2c45.11132027.495866.3.121a5455M9EN53).

-

After you register an Alibaba Cloud account, click [Activate OSS](https://www.alibabacloud.com/help/en/oss/getting-started/activate-oss#task-njz-hf4-tdb) to go to the activation page.

-

Optional. After you activate OSS, the default billing method is pay-as-you-go. If you want to reduce OSS fees, we recommend that you purchase resource plans. For more information, see [Purchase resource plans](https://www.alibabacloud.com/help/en/oss/purchase-resource-plans#task-2190990).

-

You can get started with OSS by using the OSS console, ossbrowser, ossutil, or OSS SDKs for various programming languages. For more information, see [Quick start](https://www.alibabacloud.com/help/en/oss/user-guide/get-started-with-oss/#concept-ptc-g24-tdb).

-

What are the qualifications and certifications of OSS?


Alibaba Cloud has a variety of major compliance certifications in Asia, Europe, and other countries or regions, and passed major assessments and security reviews in China. Alibaba Cloud is the first company in the world that obtains the ISO 22301 and CSA STAR gold certifications and meets the C5 additional requirements, the first in Asia Pacific to be C5 and ISO27001 certified, and the first in China to be MTCS Level 3 and ISO20000 certified. Alibaba Cloud is also the first cloud security service provider in China to receive the ISO 27001 certification from British Standards Institution (BSI) in 2012. Alibaba Cloud OSS has met the compliance requirements of the Securities and Exchange Commission (SEC) and the Financial Industry Regulatory Authority (FINRA). In addition, Alibaba Cloud is the first cloud service provider in China that has passed the audit and examination of Cohasset Associates, following AWS, Azure, Google Cloud, and IBM. For more information, see [Compliance certifications](https://www.alibabacloud.com/help/en/oss/user-guide/compliance-certifications).

-

Why is data restoration required?


Data restoration is required when you need to access data that is stored in OSS for long-term preservation at a low cost. You can access cold data only after you restore the data. Cold data storage significantly reduces storage costs but sacrifices the convenience of real-time access.

## FAQ about Alibaba Cloud regions


-

Where is my data stored?


When you create an OSS bucket, you can specify an Alibaba Cloud region in which the bucket is located. By default, OSS backs up your data to one zone in the specified region. If you enable zone-redundant storage (ZRS), ZRS stores multiple copies of your data across multiple zones in the same region. Your data remains accessible even if a zone becomes unavailable.

-

What is an Alibaba Cloud region?


An Alibaba Cloud region is a geographical region that contains multiple geographically isolated zones. These zones are connected to each other over networks that feature low latency, high throughput, and high redundancy.

-

What is a zone?


An Alibaba Cloud region is a geographical region that contains multiple geographically isolated zones. These zones are connected to each other over networks that feature low latency, high throughput, and high redundancy. The network latency between instances that are deployed in the same zone is lower than the network latency between instances that are deployed in different zones. Zones in the same region are connected over the internal network. When a zone becomes unavailable, other zones are not affected.

-

How do I determine in which region to store my data?


When you select a region, we recommend that you consider factors such as physical locations, relationships between cloud services, and resource prices. For more information, see [Choose an OSS region](https://www.alibabacloud.com/help/en/oss/choose-an-oss-region#concept-2465513).

## FAQ about billing


-

How are users charged fees?


OSS supports the pay-as-you-go billing method to allow you to pay for the resources that you use. You are not charged a minimum usage fee when you use OSS. You can also purchase resource plans. Resource plans are used to offset fees incurred due to resource usage. In most cases, resource plans are more cost-effective. For more information about the pricing of OSS, visit the [OSS pricing page](https://www.alibabacloud.com/product/oss/pricing?spm=a3c0i.7950270.1834322160.1.7bf3ab915anLR3).

-

How am I charged fees when other accounts are used to access my OSS resources?


When other accounts access your OSS resources, you are charged fees based on the standard pricing. You can enable the pay-by-requester mode for your bucket so that requesters are charged fees that are generated when the requesters send requests and download OSS data. For more information, see [Pay-by-requester](https://www.alibabacloud.com/help/en/oss/user-guide/enable-pay-by-requester-1#concept-yls-jm2-2fb).

-

How do I deactivate OSS?


If you deactivate OSS, your business may be affected. Therefore, OSS does not provide the deactivation feature. However, you can use other methods to delete your OSS resources and stop being charged for these resources. For more information, see [How do I deactivate OSS or stop OSS charging my resources?](https://www.alibabacloud.com/help/en/oss/product-overview/how-do-i-deactivate-oss-or-stop-oss-charging-my-resources#concept-4937)

## FAQ about data security and protection


-

Is data stored in OSS in a secure manner?


OSS ensures the security of the data that is stored. By default, only the resource owner can access resources within a bucket. OSS provides user identity verification to manage access to data. You can use various access control policies at the bucket level or object level, such as access control lists (ACLs), to grant specific permissions to specific users and user groups. The OSS console displays the buckets that are available for public access. You can set the bucket ACL to private if you do not want other users to access your bucket or object. If you set the ACL of a private bucket or object to public-read or public-read write, OSS sends you a warning. For more information, see [Security and compliance](https://www.alibabacloud.com/help/en/oss/user-guide/security-and-compliance-overview#concept-1322552).

-

How do I perform access control on my OSS data?


OSS provides multiple access control methods, including ACLs, RAM policies, and bucket policies, to allow users to access objects stored in buckets. For more information, see [Access control](https://www.alibabacloud.com/help/en/oss/user-guide/permissions-and-access-control-overview#concept-e4s-mhv-tdb).

-

What data encryption methods does OSS provide?


Server-side encryption: OSS encrypts objects uploaded to a bucket for which server-side encryption is configured and stores the encrypted objects. When you download an object, OSS decrypts and returns the object. The x-oss-server-side-encryption header is included in the response to declare that the object is encrypted on the server side. For more information, see [Server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db).


Client-side encryption: Objects are encrypted on the local client before they are uploaded to OSS. For more information, see [Client-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/client-side-encryption#concept-2323737).

-

How do I prevent data stored in buckets from being accidentally deleted or overwritten?


Versioning is a bucket-level data protection feature that you can use to protect objects in a bucket against unintended operations. After versioning is enabled for a bucket, existing objects in the bucket are stored as previous versions when they are overwritten or deleted. Versioning allows you to recover accidentally overwritten or deleted objects to any previous versions. For more information, see [Versioning](https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/#concept-jdg-4rx-bgb).

-

What is a retention policy?


OSS supports the Write Once Read Many (WORM) strategy that prevents an object from being deleted or overwritten for a specified period of time. You can configure time-based retention policies for buckets. After a retention policy is configured and locked for a bucket, you can read objects from or upload objects to the bucket. However, objects in the bucket or the retention policy cannot be deleted within the retention period specified in the retention policy. You can delete the objects only after the retention period ends.


You can configure retention policies for infrequently accessed important data that you do not want to be modified or deleted. Such data includes medical records, technical documents, and contracts. You can store the data in a specified bucket and configure a retention policy for the bucket.

-

Does OSS support online object modification?


OSS does not allow you to modify objects online. If you want to modify objects, you can download the object to your local computer, modify the file, and then upload the file.

-

Does OSS use the triplicate mechanism?


No, OSS uses erasure coding (EC), which also ensures storage performance and reliability.

-

How is the 99.995% uptime calculated?


The uptime defined in the OSS SLA is calculated by using the following formulas:


-

Error rate per 5 minutes = Failed requests per 5 minutes/Total valid requests per 5 minutes x 100%

-

Uptime = (1 - Error rate per 5 minutes during the service period/Total number of errors in 5 minutes during the service period) × 100%


For more information, see the [Alibaba Cloud International Website Object Storage Service Service Level Agreement](https://terms.aliyun.com/legal-agreement/terms/suit_bu1_ali_cloud/suit_bu1_ali_cloud201803021527_93160.html?spm=a2c4g.11186623.0.0.47a350f9jxxAM0)

## FAQ about data replication


-

How do I replicate data from a bucket to another bucket in a different region?


Multiple cross-region replication (CRR) rules can be configured for a bucket to store multiple copies of data in different regions. CRR provides automatic and asynchronous (near real-time) replication of objects across buckets in different OSS regions. Operations such as creating, overwriting, and deleting objects can be replicated from a source bucket to a destination bucket.

-

What are the advantages of CRR?


- Compliance requirements: Although OSS stores multiple replicas of each object in physical disks, replicas must be stored at a distance from each other to comply with regulations. CRR allows you to replicate data between geographically distant data centers to comply with regulations.
- Minimum latency: You have users who are located in two geographical locations. To minimize the latency when the users access objects, you can store replicas of objects in OSS data centers that are geographically closer to these users.
- Data backup and disaster recovery: You have high requirements for data security and availability, and want to explicitly maintain replicas of all written data in a second data center. If one OSS data center is damaged in a disaster, such as an earthquake or a tsunami, you can use backup data from the other data center.
- Data replication: To ensure the availability of your business, you may need to migrate data across different data centers.
- Operational reasons: You have compute clusters deployed in two different data centers that need to analyze the same group of objects. You can store object replicas in the two regions.
-

How am I charged fees when I use CRR?


After CRR is enabled, cross-region traffic is generated when you replicate objects across buckets in the source and destination regions. You are charged for the traffic that is generated when you use CRR. Each time an object is synchronized, OSS calculates the number of requests and the requests are charged on a pay-as-you-go basis. The traffic that is generated when you use CRR can be charged only on a pay-as-you-go basis. Resource plans are unavailable for CRR.

## FAQ about data query


How do I query data in OSS?


OSS supports the SelectObject operation that allows you to use SQL statements to query specific data in a CSV or JSON object instead of querying the entire object. The SelectObject operation simplifies the process used to query data and filter the data into smaller and more specific data sets. This operation is suitable for the multipart query of large objects, query of JSON objects, and analysis of log objects. For more information, see [Query objects](https://www.alibabacloud.com/help/en/oss/user-guide/query-objects#concept-ghk-xz2-4gb).

## FAQ about storage management


-

What is OSS lifecycle management? How do I use lifecycle management to minimize OSS storage costs?


You can configure a lifecycle rule to regularly delete objects that are no longer accessed or convert the storage class of cold data to IA, Archive, Cold Archive, or Deep Cold Archive. This makes data management easier and reduces storage costs. For example, you can configure lifecycle rules in the following scenarios:


-

A medical institution stores medical records in OSS. The objects are occasionally accessed within six months after they are uploaded, and almost never after that. In this case, you can configure a lifecycle rule to convert the storage class of the objects to Archive 180 days after they are uploaded.

-

A company stores the call records of its customer service hotline in OSS. These objects are frequently accessed within the first two months, occasionally after two months, and almost never after six months. After two years, the objects no longer need to be stored. In this case, you can configure a lifecycle rule to convert the storage class of the objects to IA 60 days after they are uploaded and to Archive 180 days after they are uploaded, and delete the objects 730 days after they are uploaded.

-

A bucket contains a large number of objects, and you want to delete all objects from the bucket. You may need to perform several manual deletion operations because OSS allows you to manually delete up to 1,000 objects at a time. In this case, you can configure a lifecycle rule to delete all objects in the bucket one day later. This way, all objects in the bucket can be deleted the next day.


For more information, see [Lifecycle rules based on the last modified time](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#concept-y2g-szy-5db).

-

How do I periodically obtain information about objects stored in a bucket?


You can use the bucket inventory feature to export information about specific objects in a bucket on a daily or weekly basis. Exported object information includes the number, sizes, storage classes, and encryption status of the objects. For more information, see [Bucket inventory](https://www.alibabacloud.com/help/en/oss/user-guide/bucket-inventory#concept-2381539).


Thank you! We've received your  feedback.