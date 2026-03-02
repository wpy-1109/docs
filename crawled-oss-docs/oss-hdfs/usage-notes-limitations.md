# OSS-HDFS Usage Notes and Limitations

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/oss-hdfs-overview

## Supported Regions

OSS-HDFS (Data Lake Storage / DLS) is available in the following regions:

- China (Hangzhou)
- China (Shanghai)
- China (Qingdao)
- China (Beijing)
- China (Ulanqab)
- China (Zhangjiakou)
- China (Shenzhen)
- China (Chengdu)

> **Note:** The list of supported regions may expand over time. Check the latest official documentation for the most current list.

## Key Usage Notes

### Data Directory Warning

After OSS-HDFS is enabled for a bucket, data written by using OSS-HDFS is stored in the `.dlsdata/` directory. To ensure the availability of OSS-HDFS and prevent data loss:

- **Do NOT** perform write operations on the `.dlsdata/` directory or objects within it using methods not supported by OSS-HDFS
- **Do NOT** rename the directory, delete the directory, or delete objects in the directory using standard OSS APIs
- Using other OSS features to perform write operations on the `.dlsdata/` directory can cause **data loss, data contamination, or data access failures**

### General Limitations

1. **Bucket-Level Enablement**: OSS-HDFS must be enabled at the bucket level and **cannot be disabled** once turned on
2. **Region Restrictions**: Only buckets in supported regions can enable OSS-HDFS
3. **Separate Namespace**: OSS-HDFS uses a separate namespace (`.dlsdata/`) from the standard OSS object namespace. Data written via HDFS interfaces and standard OSS interfaces are not interchangeable by default
4. **No Versioning Support**: Buckets with OSS-HDFS enabled do not support OSS versioning for the HDFS data path
5. **Access Protocol**: You must use the `oss://` scheme with JindoSDK to access data through the HDFS-compatible interface

### Performance and Compatibility Notes

- **Rename Operations**: OSS-HDFS supports atomic rename, a major advantage over standard OSS for big data workloads (Spark, Hive)
- **Permission Model**: Supports POSIX-like permissions (owner, group, others) and ACLs for HDFS data
- **Symlinks**: Not supported
- **Truncate**: May have limited support depending on the SDK version
- **setTimes**: Supported for modifying file timestamps

### Endpoint Format

OSS-HDFS uses a dedicated endpoint format that differs from standard OSS:

| Type | Format |
|------|--------|
| **Standard OSS** | `oss-<region>.aliyuncs.com` |
| **OSS-HDFS** | `<region>.oss-dls.aliyuncs.com` |

Example: `cn-hangzhou.oss-dls.aliyuncs.com`

### Access Path Format

```
oss://<bucket-name>/<path>
```

or

```
dls://<bucket-name>.<endpoint>/<path>
```

### Integration Compatibility

| Service | Compatible |
|---------|-----------|
| EMR (E-MapReduce) | Yes |
| DataLake Analytics | Yes |
| MaxCompute | Yes |
| Open-source Hadoop | Yes (via JindoSDK) |
| Open-source Spark | Yes (via JindoSDK) |
| Open-source Hive | Yes (via JindoSDK) |
| Open-source Flink | Yes (via JindoSDK) |
| Open-source HBase | Yes (via JindoSDK) |
| Open-source Presto/Trino | Yes (via JindoSDK) |
