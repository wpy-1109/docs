# Data Lake Storage and Analytics Integration

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/data-lake-storage

## Overview

Alibaba Cloud Object Storage Service (OSS) serves as the unified storage layer for building data lakes on Alibaba Cloud. It provides 99.9999999999% (12 nines) data durability, massive scalability with no upper limit on storage, and native integration with analytics compute engines.

## OSS as a Data Lake Foundation

### Key Capabilities

- **Unlimited storage capacity** with elastic scaling
- **Multiple storage classes** (Standard, IA, Archive, Cold Archive, Deep Cold Archive) for cost optimization
- **HDFS-compatible access** via OSS-HDFS (JindoFS) for big data workloads
- **Open format support** (Parquet, ORC, Avro, CSV, JSON) for interoperability
- **Compute-storage separation** enabling independent scaling

## Integration with Analytics Services

### 1. E-MapReduce (EMR)

EMR clusters can directly read/write data stored in OSS using the `oss://` protocol.

**Supported Frameworks:**
- Hadoop
- Spark
- Hive
- Presto/Trino
- Flink
- HBase

**Key Features:**
- OSS acts as a decoupled storage layer, separating compute from storage
- Enables elastic scaling of compute without data migration
- JindoFS/JindoSDK optimizes OSS access performance for EMR workloads
- Works seamlessly with EMR's autoscaling capabilities

**Access Pattern:**
```
oss://<bucket-name>/<path-to-data>
```

### 2. MaxCompute (formerly ODPS)

MaxCompute can create external tables pointing to OSS data for SQL-based analytics.

**Supported Formats:**
- CSV
- Parquet
- ORC
- JSON
- Avro

**Key Features:**
- Create external tables for seamless access to OSS data without data movement
- Use `LOAD` commands for batch data ingestion
- Ideal for large-scale batch processing and data warehousing
- Supports SQL-based analytics on data stored in OSS

**Example:**
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS oss_table (
  id BIGINT,
  name STRING,
  created_at DATETIME
)
STORED BY 'com.aliyun.odps.CsvStorageHandler'
LOCATION 'oss://<endpoint>/<bucket>/<path>/';
```

### 3. Data Lake Analytics (DLA) / Data Lake Formation (DLF)

DLA is a serverless interactive query service that directly queries data in OSS.

**Key Features:**
- **Serverless** - no infrastructure management required
- Supports standard SQL for querying structured/semi-structured data
- Can federate queries across OSS, ApsaraDB (RDS), and TableStore
- Built-in schema discovery and metadata management via DLA Meta (Catalog)
- No data movement required

> **Note:** Data Lake Analytics (DLA) has been transitioning to Data Lake Formation (DLF) for metadata management and governance. Serverless SQL capabilities have been integrated into other services.

## Architecture

```
+---------------------------------------------+
|            Compute Layer                     |
|  +-------+  +-----------+  +-------------+  |
|  |  EMR  |  | MaxCompute|  |     DLA     |  |
|  +---+---+  +-----+-----+  +------+------+  |
|      |            |               |          |
|      +------------+---------------+          |
|                   |                          |
|           +-------v--------+                 |
|           |   OSS (oss://) |                 |
|           |  Data Lake     |                 |
|           |  Storage       |                 |
|           +----------------+                 |
|  Standard | IA | Archive | Cold Archive      |
+---------------------------------------------+
```

## Benefits

| Feature | Benefit |
|---------|---------|
| **Compute-Storage Separation** | Scale compute and storage independently |
| **Cost Optimization** | Use OSS lifecycle policies and storage tiers |
| **Multi-Engine Access** | Same data accessible by EMR, MaxCompute, DLA simultaneously |
| **Open Formats** | Parquet, ORC, Avro ensure interoperability |
| **Security** | RAM policies, STS tokens, SSE encryption, VPC access |
| **Performance** | OSS acceleration + caching (JindoFS) for high throughput |

## Use Cases

1. **Offline Data Warehousing** - Use Hive/Spark on EMR with OSS for ETL and analytics
2. **Real-time Analytics** - Flink streaming jobs reading from and writing to OSS
3. **Machine Learning** - Store training data in OSS, access from EMR or PAI
4. **Log Analytics** - Centralize log data in OSS, query with DLA or MaxCompute
5. **Data Archival** - Use lifecycle rules to transition data to cheaper storage tiers

## Related Services

- **EMR Documentation**: https://www.alibabacloud.com/help/en/emr/
- **MaxCompute Documentation**: https://www.alibabacloud.com/help/en/maxcompute/
- **Data Lake Formation**: https://www.alibabacloud.com/help/en/dlf/
