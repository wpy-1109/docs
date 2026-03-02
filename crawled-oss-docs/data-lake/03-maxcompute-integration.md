# OSS Integration with MaxCompute

Source: https://help.aliyun.com/zh/oss/user-guide/connect-oss-to-data-lake-ecosystems/

## Overview

MaxCompute (formerly ODPS) is Alibaba Cloud's fully managed big data processing platform. It integrates deeply with OSS for data lake scenarios, supporting direct SQL queries on OSS data without ETL.

## External Tables

### Creating OSS External Tables

```sql
-- CSV format
CREATE EXTERNAL TABLE IF NOT EXISTS oss_csv_table (
    id STRING,
    name STRING,
    value DOUBLE
)
STORED BY 'com.aliyun.odps.CsvStorageHandler'
WITH SERDEPROPERTIES (
    'odps.text.option.delimiter'=',',
    'odps.text.option.header.lines.count'='1'
)
LOCATION 'oss://my-bucket/data/csv/';

-- Parquet format (recommended)
CREATE EXTERNAL TABLE IF NOT EXISTS oss_parquet_table (
    id STRING,
    name STRING,
    value DOUBLE,
    event_date STRING
)
STORED AS PARQUET
LOCATION 'oss://my-bucket/data/parquet/';

-- ORC format
CREATE EXTERNAL TABLE IF NOT EXISTS oss_orc_table (
    id STRING,
    name STRING,
    value DOUBLE
)
STORED AS ORC
LOCATION 'oss://my-bucket/data/orc/';
```

### Partitioned External Tables

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS oss_partitioned_table (
    id STRING,
    name STRING,
    value DOUBLE
)
PARTITIONED BY (dt STRING, region STRING)
STORED AS PARQUET
LOCATION 'oss://my-bucket/data/partitioned/';

-- Add partitions
ALTER TABLE oss_partitioned_table ADD PARTITION (dt='2024-07-19', region='cn');
```

## Data Import from OSS

### LOAD Command
```sql
-- Load data from OSS into MaxCompute internal table
LOAD OVERWRITE TABLE internal_table
FROM LOCATION 'oss://my-bucket/data/import/'
STORED AS PARQUET;
```

### INSERT with External Table
```sql
-- Read from OSS external table and insert into internal table
INSERT OVERWRITE TABLE internal_table
SELECT * FROM oss_external_table
WHERE dt >= '2024-01-01';
```

## Data Export to OSS

### UNLOAD Command
```sql
-- Export query results to OSS
UNLOAD FROM (
    SELECT id, name, SUM(value) as total_value
    FROM internal_table
    GROUP BY id, name
)
INTO LOCATION 'oss://my-bucket/output/results/'
STORED AS PARQUET;
```

### INSERT OVERWRITE External Table
```sql
-- Write to OSS via external table
INSERT OVERWRITE TABLE oss_external_table
SELECT * FROM internal_table
WHERE dt = '2024-07-19';
```

## Lake-Warehouse Integration

### Delta Lake on OSS
```sql
-- Read Delta Lake table from OSS
CREATE EXTERNAL TABLE delta_table
STORED BY 'com.aliyun.odps.DeltaStorageHandler'
LOCATION 'oss://my-bucket/delta/events/';
```

### Apache Iceberg on OSS
```sql
-- Read Iceberg table from OSS
CREATE EXTERNAL TABLE iceberg_table
STORED BY 'com.aliyun.odps.IcebergStorageHandler'
LOCATION 'oss://my-bucket/iceberg/events/';
```

## Authentication

MaxCompute accesses OSS using RAM role authorization:
1. Create a RAM role with OSS read permissions
2. Grant MaxCompute the role assumption permission
3. External tables automatically use the role for OSS access

## Performance Optimization

1. **Use Parquet/ORC**: Columnar formats reduce I/O for analytical queries
2. **Partition data**: Use date/category partitions to prune data scans
3. **Use compression**: Snappy or ZSTD compression for Parquet/ORC
4. **Same-region access**: Keep MaxCompute project and OSS Bucket in the same region
5. **Predicate pushdown**: Filters on partition columns skip irrelevant data
