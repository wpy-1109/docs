# How to migrate data to OSS or OSS-HDFS

Business data is often scattered across on-premises data centers, third-party cloud storage, or Alibaba Cloud Object Storage Service (OSS) buckets in different regions and under different accounts. Managing this scattered data can be complex and costly. Migrating this data to a destination OSS bucket simplifies management. Alibaba Cloud offers several solutions to meet your business needs, including Data Online Migration, command line tools, and offline migration with Data Transport.

## Migrating between Alibaba Cloud OSS buckets


When you migrate data between Alibaba Cloud OSS buckets, you can choose a migration method based on the regions of the source and destination buckets to ensure an efficient and straightforward migration.

### Same-region migration


When the source and destination buckets are in the same region, you can select a migration method based on your scenario:


-

For small to medium amounts of data in buckets under the same account, you can use the [cp (copy file)](https://www.alibabacloud.com/help/en/oss/developer-reference/cp-1) command of the ossutil command line tool. This command supports batch file copying and resumable transfers.

-

For large-scale data migration or migration between buckets under different accounts, you can use the [Same-region replication (SRR)](https://www.alibabacloud.com/help/en/oss/user-guide/srr/) feature. Data is automatically synchronized to the destination bucket when it is added, modified, or deleted in the source bucket. This process eliminates the need for intermediate downloads and extra network transfers. SRR is ideal for data centralization and sharing between different teams or subsidiaries.

### Cross-region migration


When the source and destination buckets are in different regions, such as migrating from China (Hangzhou) to China (Beijing), you can use the [cross-region replication](https://www.alibabacloud.com/help/en/oss/user-guide/cross-region-replication-overview/) feature. This feature uses the Alibaba Cloud internal network for secure and reliable data transfer. Data is automatically synchronized to the destination bucket when it is added, modified, or deleted in the source bucket. This method is ideal for multi-site collaboration and real-time backups.

## Migrating from third-party storage to OSS


When your data is stored with other cloud providers and you need to migrate it to Alibaba Cloud OSS, you can use [Alibaba Cloud Data Online Migration](https://www.alibabacloud.com/help/en/data-online-migration/product-overview/what-is-data-online-migration). This service supports various storage services, including AWS S3, Tencent Cloud COS, Huawei Cloud OBS, Volcano Engine TOS, Google Cloud Storage (GCS), and Microsoft Azure Blob. It also supports self-managed object storage services that are compatible with the S3 protocol. You do not need to set up a migration environment. You can submit migration tasks online and monitor the process at any time. You can select the appropriate [online migration tutorial](https://www.alibabacloud.com/help/en/data-online-migration/user-guide/migration-tutorials/) for your business scenario for a smooth data migration.

## Migrating from a local file system to OSS

### Small-scale data migration


For small amounts of data (less than 5 GB), you can upload the data directly using the [Object Storage Service (OSS) console](https://oss.console.alibabacloud.com/overview). This method is simple and does not require extra tools or complex configurations. It is suitable for temporary file uploads, test data migration, or infrequent migration tasks. You can quickly upload files through the browser interface, making it ideal for moving individual files or small datasets to the cloud.

### Medium-scale data migration


For medium-scale data migration, you can choose one of the following two methods based on your needs:


-

To efficiently transfer regular business data, log files, and backup data, you can use the [cp (upload file)](https://www.alibabacloud.com/help/en/oss/developer-reference/cp-upload-file) command of the ossutil command line tool. This tool supports batch file uploads, resumable transfers, and concurrent acceleration.

-

If your on-premises network environment is complex, or if you want to centrally schedule and manage migration tasks from the cloud, you can use [Alibaba Cloud Data Online Migration](https://www.alibabacloud.com/help/en/data-online-migration/product-overview/what-is-data-online-migration) to [migrate data from a local file system to OSS](https://www.alibabacloud.com/help/en/data-online-migration/user-guide/migration-tutorial-from-localfs-to-oss/). This service provides a managed data migration solution that supports task creation, monitoring, and management. It simplifies operations and maintenance (O&M) complexity and is suitable for enterprise customers who need centralized control over the migration process.

### Large-scale data migration


For very large-scale data migration, you can choose one of the following two methods based on your needs:


-

You can use [Alibaba Cloud Data Online Migration](https://www.alibabacloud.com/help/en/data-online-migration/product-overview/what-is-data-online-migration). You can use this service without setting up a migration environment. You can submit migration tasks online and monitor the progress in real time. This method is suitable for business scenarios that require flexible scheduling and can be performed over the Internet.

-

If your data transfer is limited by public bandwidth or you need to migrate from an on-premises data center, you can use [offline migration (Data Transport)](https://www.alibabacloud.com/help/en/data-transport/product-overview/what-is-data-transport). This method is ideal for scenarios such as migrating an entire data center to the cloud or moving large corporate archives and historical image data. Data Transport is designed for large-scale data migration from the terabyte to the petabyte level. It uses physical devices for data collection and transfer, avoiding public bandwidth bottlenecks and significantly improving migration efficiency.

## Migrating from an HTTP/HTTPS source to OSS


If your data is stored on an HTTP/HTTPS source, you can use [Alibaba Cloud Data Online Migration](https://www.alibabacloud.com/help/en/data-online-migration/product-overview/what-is-data-online-migration) to efficiently and smoothly [migrate the data from the HTTP/HTTPS source to OSS](https://www.alibabacloud.com/help/en/data-online-migration/user-guide/tutorial-for-data-migration-from-http-or-https-servers-to-oss/). You do not need to set up an additional environment for the migration. You can simply submit the migration task online and monitor its progress and status in real time to ensure a secure and reliable data transfer.

## Migrating from big data storage to OSS

### Migrating HDFS data to OSS


For large-scale data in a Hadoop Distributed File System (HDFS), you can use [Alibaba Cloud Jindo DistCp to migrate HDFS data to OSS](https://www.alibabacloud.com/help/en/oss/user-guide/migrate-data-from-hdfs-to-oss#task-1938603). Jindo DistCp is a MapReduce-based distributed file copy tool that can efficiently transfer files within a large-scale cluster or between different clusters. It takes a list of files and directories as input for MapReduce tasks, which it then splits and distributes for parallel execution. Each task copies a portion of the data from the source list. This process improves transfer efficiency and supports fault tolerance, resumable transfers, and error recovery, ensuring stability and data integrity during terabyte- or petabyte-scale big data migrations. This method is suitable for big data computing and data lake construction scenarios.

### Migrating OSS external table (gpossext) data to OSS


When data is stored as an OSS external table (gpossext) and needs to be efficiently imported or exported between OSS and a data warehouse, you can use [cloud-native data warehouse AnalyticDB for PostgreSQL to export data to OSS in parallel](https://www.alibabacloud.com/help/en/analyticdb/analyticdb-for-postgresql/user-guide/use-oss-external-tables-to-export-data-to-oss#task-2100743). This service supports the gpossext feature to import data from OSS to AnalyticDB for PostgreSQL in parallel or export data to OSS in parallel. Because the migration process is based on a distributed architecture, it offers high concurrency and high throughput. This greatly reduces data transfer time while ensuring data security and integrity. This method is suitable for business scenarios such as large-scale data analytics, historical data archiving, and cross-system data exchange.

## Migrating from big data storage to OSS-HDFS


The OSS-HDFS service, also known as the JindoFS service, is a cloud-native data lake storage product. It provides unified metadata management capabilities and is fully compatible with the HDFS file system interface while offering full POSIX support. This makes it well-suited for data lake scenarios such as big data computing and AI training. You can migrate existing data to OSS-HDFS or efficiently migrate data between different OSS-HDFS buckets.

### Migrating HDFS data to OSS-HDFS


For data migration from traditional HDFS clusters, you can use the [Alibaba Cloud Jindo DistCp tool to migrate HDFS data to OSS-HDFS](https://www.alibabacloud.com/help/en/oss/user-guide/migrate-data-from-hdfs-to-oss-hdfs). This tool enables large-scale file distribution within a cluster or across clusters. It supports automatic error detection, retries, and task recovery, improving the stability and efficiency of migration tasks. It works by taking a list of files and directories as input for MapReduce tasks, and each task copies a portion of the files. This is ideal for batch processing of massive data migration. With Jindo DistCp, you can achieve a smooth migration, quickly import data into OSS-HDFS, and help transition your big data platform to a cloud-native architecture.

### Migrating data between OSS-HDFS buckets



If you have deployed the OSS-HDFS service, you can also use the [Alibaba Cloud Jindo DistCp tool to migrate data between different buckets in the OSS-HDFS service](https://www.alibabacloud.com/help/en/oss/user-guide/migrate-data-across-multiple-buckets-in-oss-hdfs#task-2218900). This is suitable for adjusting data partitions, optimizing storage resources, or scheduling data across regions, ensuring that business data remains consistent and highly available.

### Migrating data from a semi-managed JindoFS cluster to OSS-HDFS



When using a semi-managed JindoFS cluster, you can use the [JindoDistJob tool to migrate data from the semi-managed JindoFS cluster to the OSS-HDFS service](https://www.alibabacloud.com/help/en/oss/user-guide/migrate-data-from-a-semi-hosted-jindofs-cluster-to-oss-hdfs#task-2231351). This tool supports full and incremental migration and lets you smoothly switch to the JindoFS service solution without migrating data blocks. This ensures a seamless transition for your business and is suitable for scenarios that require a rapid change in storage architecture.

### Migrating Hive table and partition data to OSS-HDFS



To migrate structured data, you can use the [JindoTable MoveTo command to migrate Hive table and partition data to the OSS-HDFS service](https://www.alibabacloud.com/help/en/oss/user-guide/use-the-jindotable-moveto-command-to-migrate-hive-tables-and-partitions-to-oss-hdfs#task-2231743). After copying the underlying data, this command automatically updates the metadata, ensuring that tables and partitions are completely migrated to the new path. It supports filtering by conditions, allowing you to migrate many partitions at once. It also uses multiple data validation mechanisms to ensure data integrity and security, making it ideal for migrating large structured datasets.

## Configuring zero-downtime migrationNote: First, determine the migration method. Then, configure mirroring-based back-to-origin as needed to achieve a zero-downtime migration.


To maintain business continuity and achieve a zero-downtime migration, you can configure [mirroring-based back-to-origin](https://www.alibabacloud.com/help/en/oss/back-to-origin-configuration-overview#concept-n34-q1z-5db). After you switch your service to OSS, any requests for data that has not yet been migrated are automatically retrieved from the source site. This ensures a smooth, seamless transition for users. The typical migration flow is as follows: first, complete the historical data migration and switch the business entry point to OSS. Then, mirroring-based back-to-origin automatically fetches any non-migrated data, gradually backfilling it until the migration to the cloud is complete.


For example, a business is initially deployed on another cloud storage platform. Because of business growth, it needs to migrate to OSS without interrupting online services. In this case, you can configure a mirroring-based back-to-origin rule to automatically fetch and synchronize non-migrated data to OSS during the migration process. This ensures the service remains stable and continuously available.

Thank you! We've received your  feedback.