# Data Lake Integration Overview

Source: https://help.aliyun.com/zh/oss/user-guide/connect-oss-to-data-lake-ecosystems/
Source: https://help.aliyun.com/zh/oss/user-guide/data-lake

## Overview

Alibaba Cloud OSS serves as the storage foundation for building data lakes. It provides EB-scale storage capacity with 12 nines (99.9999999999%) data durability at significantly lower cost than traditional HDFS. OSS integrates with major Alibaba Cloud big data services and open-source data lake technologies.

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Application & BI Layer                      │
├────────────────┬──────────────┬───────────────┬──────────────┤
│   MaxCompute   │     EMR      │   DLA / DLF   │    Flink     │
│ (Offline SQL)  │(Spark/Hive)  │ (Serverless)  │ (Streaming)  │
├────────────────┴──────────────┴───────────────┴──────────────┤
│              Data Lake Management (Data Lake Formation)       │
├──────────────────────────────────────────────────────────────┤
│                   OSS Object Storage (Data Lake)              │
│          Parquet / ORC / Avro / Delta Lake / Iceberg          │
└──────────────────────────────────────────────────────────────┘
```

## OSS as Data Lake Storage

### Advantages Over HDFS
| Feature | OSS | HDFS |
|---|---|---|
| Storage cost | ~60% lower | Higher (3x replication) |
| Scalability | EB-scale, unlimited | Limited by cluster size |
| Durability | 12 nines | Depends on replication |
| Maintenance | Zero (managed service) | Requires NameNode/DataNode ops |
| Compute coupling | Decoupled (elastic) | Tightly coupled |
| Multi-engine access | Any engine concurrently | Primarily Hadoop stack |

### Storage Classes for Data Lake
- **Standard**: Hot data, frequent queries, real-time analytics
- **IA**: Warm data, periodic batch processing
- **Archive**: Historical data, compliance retention
- Use lifecycle rules to automatically tier data

## Integration with MaxCompute

### External Tables
MaxCompute can directly read/write data in OSS via external tables:

```sql
-- Create external table over OSS data
CREATE EXTERNAL TABLE oss_sales (
    order_id STRING,
    customer_id STRING,
    amount DOUBLE,
    order_date STRING
)
STORED BY 'com.aliyun.odps.CsvStorageHandler'
WITH SERDEPROPERTIES (
    'odps.text.option.delimiter'=','
)
LOCATION 'oss://my-data-lake/sales/';

-- Query directly
SELECT customer_id, SUM(amount) as total
FROM oss_sales
WHERE order_date >= '2024-01-01'
GROUP BY customer_id;
```

### Supported Formats
- CSV, TSV
- Parquet (recommended for analytics)
- ORC
- Avro
- JSON

### Lake-Warehouse Integration
MaxCompute supports direct access to open table formats on OSS:
- **Delta Lake**: ACID transactions on OSS
- **Apache Hudi**: Incremental data processing
- **Apache Iceberg**: Schema evolution, time travel

## Integration with EMR (Elastic MapReduce)

### Storage-Compute Separation
EMR uses OSS as primary storage instead of HDFS:

```python
# Spark reading from OSS
df = spark.read.parquet("oss://my-data-lake/processed/events/")

# Spark writing to OSS
df.write.mode("overwrite").parquet("oss://my-data-lake/output/results/")
```

### JindoFS / JindoSDK
Alibaba Cloud's accelerated OSS access layer for big data:
- **Caching**: Local SSD cache for frequently accessed data
- **HDFS compatibility**: Full HDFS API compatibility via `oss://` schema
- **Performance**: 2-5x read performance improvement with caching
- **POSIX support**: Full POSIX file system interface

### Supported Components
All EMR components can access OSS directly:
- **Apache Spark**: `oss://` path support
- **Apache Hive**: External tables and managed tables on OSS
- **Presto/Trino**: Direct OSS query support
- **Apache Flink**: OSS as source and sink
- **HBase**: OSS as backup storage

## Integration with Data Lake Formation (DLF)

### Capabilities
- **Unified metadata management**: Central catalog for OSS data
- **Schema management**: Track schema evolution across datasets
- **Data discovery**: Search and browse data lake contents
- **Access control**: Fine-grained column-level permissions
- **Data quality**: Automated data quality monitoring

### Serverless SQL Analytics
Use Data Lake Analytics (DLA) for serverless SQL queries on OSS data:
```sql
-- No cluster management needed
SELECT * FROM oss_table
WHERE event_date = '2024-07-19'
LIMIT 100;
```

## Integration with Flink

### Real-Time Data Ingestion
Use Flink to stream data into OSS data lake:

```java
// Flink sink to OSS (Parquet format)
StreamingFileSink<Row> sink = StreamingFileSink
    .forBulkFormat(
        new Path("oss://my-data-lake/streaming/"),
        ParquetAvroWriters.forReflectRecord(EventRecord.class))
    .withBucketAssigner(new DateTimeBucketAssigner<>("yyyy-MM-dd--HH"))
    .build();

stream.addSink(sink);
```

### Lambda Architecture
```
Real-time (Flink) ──> OSS (streaming layer)
                                │
Batch (Spark/MaxCompute) ──> OSS (batch layer)
                                │
                         Serving Layer (query engines)
```

## OSS-HDFS Service (JindoFS)

Cloud-native data lake storage with full HDFS and POSIX compatibility:

### Features
- **HDFS-compatible**: Drop-in replacement for HDFS
- **POSIX support**: Mount as local file system
- **Atomic operations**: Directory rename, consistent listing
- **Performance**: Optimized for big data workloads
- **AI/ML support**: Compatible with training frameworks

### Migration from HDFS
Use **Jindo DistCp** for migrating HDFS data to OSS-HDFS:
```bash
hadoop jar jindo-distcp-*.jar \
  --src hdfs://namenode:8020/data/ \
  --dest oss://my-data-lake/data/ \
  --parallelism 20
```

## OSS Select for Ad-Hoc Queries

Push SQL-like queries to OSS for server-side processing:
```sql
SELECT s.name, s.revenue
FROM ossobject s
WHERE s.revenue > 1000000
```

Benefits:
- Reduce data transfer (only return matching rows)
- Faster than downloading and processing locally
- Supports CSV and JSON formats

## Best Practices

1. **Use Parquet or ORC** format for analytical workloads (columnar, compressed)
2. **Partition data** by date/region/category for efficient queries
3. **Use lifecycle rules** to tier cold data to IA/Archive storage
4. **Enable JindoFS caching** for frequently accessed datasets
5. **Use internal endpoints** for big data services in same region
6. **Separate storage from compute** for independent scaling
7. **Use Delta Lake/Iceberg** for ACID transactions and schema evolution
8. **Monitor with CloudLens** for storage usage and access patterns
