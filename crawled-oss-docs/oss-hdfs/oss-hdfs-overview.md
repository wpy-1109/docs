# What is the OSS-HDFS service?

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs-overview

OSS-HDFS (also known as JindoFS) is a cloud-native data lake storage capability built on Object Storage Service (OSS). It is fully compatible with the Hadoop Distributed File System (HDFS) interface and provides unified metadata management for big data and AI computing scenarios.

OSS-HDFS is not a separate storage service. Instead, it is a set of capabilities that you enable on your existing OSS bucket. After a simple configuration process, you can manage and access data in the same way as you would with native HDFS, while benefiting from the scalability, reliability, and cost-efficiency of OSS.

## Usage notes

> **Warning**
> After OSS-HDFS is enabled for a bucket, data that is written by using OSS-HDFS is stored in the `.dlsdata/` directory. To ensure the availability of OSS-HDFS and prevent data loss, do not perform write operations on the `.dlsdata/` directory or objects within by using methods that are not supported by OSS-HDFS. For example, do not perform the following write operations: rename the directory, delete the directory, and delete objects in the directory.
>
> Using other OSS features to perform write operations on the `.dlsdata/` directory can cause data loss, data contamination, or data access failures. For more information, see Usage notes.

## Billing rules

### Data storage fees

When you use OSS-HDFS, data blocks are stored in Objects Storage Service (OSS). Therefore, the billing method of OSS applies to data blocks in OSS-HDFS. For more information, see Billing overview.

## Benefits

OSS-HDFS brings the following key capabilities to your OSS bucket:

- **HDFS-compatible access**: Use the standard Hadoop FileSystem API with no modifications to your existing Hadoop and Spark applications.
- **Hierarchical namespace**: Organize objects into a true directory hierarchy with support for atomic directory operations such as rename and delete.
- **Unified storage**: Data is stored in the underlying OSS bucket. You benefit from unlimited capacity, elastic scaling, and high security, reliability, and availability.
- **Broad ecosystem support**: Works with Spark, Hive, Flink, Presto, HBase, and other big data frameworks.
- **Enterprise security**: Supports file and directory permissions, access control lists (ACLs), and extended attributes (XAttrs).
- **Cost-efficiency**: The billing method of OSS applies to stored data. No separate storage service fees.

## Hierarchical namespace

The hierarchical namespace is a core feature of OSS-HDFS. In addition to the flat namespace of standard object storage, OSS-HDFS provides a directory hierarchy that lets you organize objects into directories and nested subdirectories. Its unified metadata management capability enables automatic internal conversion.

## Metadata management

OSS-HDFS uses a multi-node, active-active redundancy mechanism for metadata management. Compared to the active/standby NameNode architecture in traditional HDFS, this design provides superior data redundancy. OSS-HDFS can manage exabytes of data and hundreds of millions of files, and deliver terabytes of throughput.

For Hadoop users, this means you can access data as efficiently as you would access a local HDFS, without requiring data replication or conversion. This greatly improves overall job performance and reduces maintenance costs.

## Scenarios

OSS-HDFS supports a broad range of big data and AI use cases:

- Offline data warehousing with Hive and Spark
- Online analytical processing (OLAP)
- Compute-storage decoupled HBase
- Real-time computing
- Data migration

OSS-HDFS supports file and directory semantics and operations, including directory permissions, directory atomicity, millisecond-level rename operations, the setTimes operation, extended attributes (XAttrs), access control lists (ACLs), and local read cache acceleration. These features make it well-suited for open-source Hive and Spark offline data warehouses. In extract, transform, and load (ETL) scenarios, OSS-HDFS provides significant performance advantages over standard OSS buckets.

## Supported engines

### Open-source ecosystem

| Engine | References |
|--------|------------|
| Flink | Use open source Flink with JindoSDK to process data in OSS-HDFS |
| Flume | Use JindoSDK with Flume to write data to OSS-HDFS |
| Hadoop | Use JindoSDK with Hadoop to access OSS-HDFS |
| HBase | Use OSS-HDFS as the underlying storage for HBase |
| Hive | Use JindoSDK with Hive to process data in OSS-HDFS |
| Impala | Use JindoSDK with Impala to query data in OSS-HDFS |
| Presto | Use JindoSDK with Trino to query data in OSS-HDFS |
| Spark | Use JindoSDK with Spark to query data in OSS-HDFS |

### Alibaba Cloud ecosystem

| Engine/Platform | References |
|----------------|------------|
| EMR (Hive/Spark) | Access OSS-HDFS from EMR Hive or Spark |
| EMR Flink | Use Apache Flink on an EMR cluster to recoverably write data to OSS-HDFS; Use Realtime Compute for Apache Flink to read data from or write data to OSS or OSS-HDFS |
| EMR Flume | Use Flume to synchronize data from an EMR Kafka cluster to OSS-HDFS |
| EMR HBase | Use OSS-HDFS as the underlying storage of HBase on an EMR cluster |
| EMR Hive | Use Hive on an EMR cluster to process data in OSS-HDFS |
| EMR Impala | Use Impala on an EMR cluster to query data in OSS-HDFS |
| EMR Presto | Use Trino on an EMR cluster to query data in OSS-HDFS |
| EMR Spark | Use Spark on an EMR cluster to process data in OSS-HDFS |
| EMR Sqoop | Use Sqoop on an EMR cluster to read data from and write data to OSS-HDFS |

## Features

| Feature | Description | References |
|---------|-------------|------------|
| RootPolicy | Set a custom prefix for OSS-HDFS. This allows jobs to run directly on OSS-HDFS without modifying the original hdfs:// access prefix. | Access data using RootPolicy |
| ProxyUser | Authorize a user to perform file system operations on behalf of other users. This is useful for accessing sensitive data where only specific authorized users should operate on the data. | ProxyUser (Configure a proxy user) |
| UserGroupsMapping | Configure mappings between users and user groups. | UserGroupsMapping (Manage user and group mappings) |
