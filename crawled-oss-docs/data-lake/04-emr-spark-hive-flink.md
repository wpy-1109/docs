# OSS Integration with EMR (Spark, Hive, Flink)

Source: https://help.aliyun.com/zh/oss/user-guide/connect-oss-to-data-lake-ecosystems/

## Overview

Alibaba Cloud E-MapReduce (EMR) provides a managed Hadoop/Spark ecosystem that uses OSS as its primary storage layer instead of HDFS. This storage-compute separation architecture enables independent scaling and cost optimization.

## Spark Integration

### Reading from OSS
```python
# Read Parquet files
df = spark.read.parquet("oss://my-data-lake/data/events/")

# Read CSV files
df = spark.read.option("header", "true").csv("oss://my-data-lake/data/sales.csv")

# Read JSON files
df = spark.read.json("oss://my-data-lake/data/logs/")

# Read with schema
from pyspark.sql.types import *
schema = StructType([
    StructField("id", StringType(), True),
    StructField("value", DoubleType(), True),
    StructField("timestamp", TimestampType(), True)
])
df = spark.read.schema(schema).parquet("oss://my-data-lake/data/events/")
```

### Writing to OSS
```python
# Write as Parquet (recommended)
df.write.mode("overwrite").parquet("oss://my-data-lake/output/results/")

# Write partitioned data
df.write.partitionBy("date", "region") \
    .mode("append") \
    .parquet("oss://my-data-lake/output/partitioned/")

# Write as CSV
df.write.option("header", "true").csv("oss://my-data-lake/output/csv/")
```

### Delta Lake on OSS
```python
# Write Delta Lake table
df.write.format("delta").mode("overwrite") \
    .save("oss://my-data-lake/delta/events/")

# Read Delta Lake table
df = spark.read.format("delta").load("oss://my-data-lake/delta/events/")

# Time travel
df = spark.read.format("delta") \
    .option("versionAsOf", 5) \
    .load("oss://my-data-lake/delta/events/")
```

### Iceberg on OSS
```python
# Write Iceberg table
df.writeTo("catalog.db.events") \
    .using("iceberg") \
    .create()

# Read Iceberg table
df = spark.read.format("iceberg") \
    .load("oss://my-data-lake/iceberg/events/")
```

## Hive Integration

### External Tables on OSS
```sql
-- Create database
CREATE DATABASE IF NOT EXISTS data_lake;

-- Create external table
CREATE EXTERNAL TABLE data_lake.events (
    event_id STRING,
    user_id STRING,
    event_type STRING,
    event_value DOUBLE
)
PARTITIONED BY (dt STRING)
STORED AS PARQUET
LOCATION 'oss://my-data-lake/hive/events/';

-- Add partition
ALTER TABLE data_lake.events ADD PARTITION (dt='2024-07-19')
LOCATION 'oss://my-data-lake/hive/events/dt=2024-07-19/';

-- Query
SELECT event_type, COUNT(*) as cnt
FROM data_lake.events
WHERE dt = '2024-07-19'
GROUP BY event_type;
```

## Flink Integration

### Streaming to OSS
```java
// Configure OSS sink
StreamingFileSink<String> sink = StreamingFileSink
    .forRowFormat(
        new Path("oss://my-data-lake/streaming/events/"),
        new SimpleStringEncoder<String>("UTF-8"))
    .withRollingPolicy(
        DefaultRollingPolicy.builder()
            .withRolloverInterval(Duration.ofMinutes(5))
            .withMaxPartSize(MemorySize.ofMebiBytes(128))
            .build())
    .withBucketAssigner(
        new DateTimeBucketAssigner<>("yyyy-MM-dd--HH"))
    .build();

stream.addSink(sink);
```

### Flink SQL with OSS
```sql
-- Create table backed by OSS
CREATE TABLE oss_events (
    event_id STRING,
    user_id STRING,
    event_time TIMESTAMP(3),
    WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
) WITH (
    'connector' = 'filesystem',
    'path' = 'oss://my-data-lake/flink/events/',
    'format' = 'parquet'
);
```

## JindoFS/JindoSDK Configuration

### EMR Configuration
EMR clusters automatically configure JindoSDK for optimized OSS access. Key configurations:

```xml
<!-- core-site.xml -->
<property>
    <name>fs.oss.impl</name>
    <value>com.aliyun.jindodata.oss.JindoOssFileSystem</value>
</property>
<property>
    <name>fs.oss.endpoint</name>
    <value>oss-cn-hangzhou-internal.aliyuncs.com</value>
</property>
```

### Local Cache Configuration
```xml
<property>
    <name>fs.oss.data.cache.enable</name>
    <value>true</value>
</property>
<property>
    <name>fs.oss.data.cache.dir</name>
    <value>/mnt/disk1/jindo-cache</value>
</property>
<property>
    <name>fs.oss.data.cache.size</name>
    <value>100GB</value>
</property>
```

## Performance Best Practices

1. **Use internal endpoints**: EMR and OSS in same region for free, fast access
2. **Enable JindoFS caching**: Cache hot data on local SSD for repeated reads
3. **Use Parquet/ORC**: Columnar formats with predicate pushdown
4. **Partition wisely**: By date for time-series, by key for lookup patterns
5. **Tune parallelism**: Match Spark/Hive partition count to data volume
6. **Use compression**: Snappy (speed) or ZSTD (ratio) for Parquet files
7. **Avoid small files**: Merge small files to reduce metadata overhead
