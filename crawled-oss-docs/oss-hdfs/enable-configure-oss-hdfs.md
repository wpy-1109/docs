# Enable and Configure OSS-HDFS with JindoSDK

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/enable-oss-hdfs-service

## Overview

OSS-HDFS (also known as JindoFS DLS - Data Lake Storage) is Alibaba Cloud's HDFS-compatible layer on top of OSS. JindoSDK is the client SDK used to access OSS-HDFS from big data ecosystems like Hadoop, Spark, Hive, etc.

## Prerequisites

1. **ECS Instance**: An Alibaba Cloud Elastic Compute Service (ECS) instance must be created and accessible, ideally in the **same region** as the target OSS bucket.
2. **OSS-HDFS Service Enabled**: The OSS-HDFS service (Data Lake Storage feature) must be explicitly enabled for the specific OSS bucket through the OSS console.
3. **JindoSDK Deployed**: JindoSDK JARs (e.g., `jindo-sdk-x.x.x.jar` and `jindo-core-x.x.x.jar`) must be placed in your Hadoop classpath (e.g., `$HADOOP_HOME/lib/` or `$HADOOP_HOME/share/hadoop/common/lib/`).

## Enable OSS-HDFS on a Bucket

1. Log in to the **OSS Console** at https://oss.console.aliyun.com
2. Select the target bucket
3. Navigate to **Data Lake Storage** or **OSS-HDFS** settings
4. Click **Enable** to activate the OSS-HDFS service for the bucket

## Configure JindoSDK in core-site.xml

Add the following configurations to your Hadoop `core-site.xml` file:

### 1. Set the FileSystem Implementation

```xml
<property>
    <name>fs.AbstractFileSystem.oss.impl</name>
    <value>com.aliyun.jindodata.oss.JindoOSS</value>
</property>

<property>
    <name>fs.oss.impl</name>
    <value>com.aliyun.jindodata.oss.JindoOssFileSystem</value>
</property>
```

### 2. Configure the OSS-HDFS Endpoint

```xml
<property>
    <name>fs.oss.endpoint</name>
    <value><YOUR_OSS_HDFS_ENDPOINT></value>
    <!-- Example: cn-hangzhou.oss-dls.aliyuncs.com -->
</property>
```

> **Note:** The OSS-HDFS endpoint uses a special domain format: `<region>.oss-dls.aliyuncs.com` (note the `oss-dls` subdomain, which differs from the standard OSS endpoint).

### 3. Configure Access Credentials

```xml
<property>
    <name>fs.oss.accessKeyId</name>
    <value><YOUR_ACCESS_KEY_ID></value>
</property>

<property>
    <name>fs.oss.accessKeySecret</name>
    <value><YOUR_ACCESS_KEY_SECRET></value>
</property>
```

### 4. Access Path Format

Once configured, access data using:

```
oss://<bucket-name>/<path>
```

## RootPolicy Configuration

RootPolicy allows you to set a custom prefix for OSS-HDFS. This allows jobs to run directly on OSS-HDFS without modifying the original `hdfs://` access prefix.

```xml
<property>
    <name>fs.oss.hdfs.root.policy</name>
    <value>{policy_value}</value>
</property>
```

## ProxyUser Configuration (Impersonation)

ProxyUser enables user impersonation, allowing a trusted super user to perform operations on behalf of other users. This is critical for multi-tenant environments (e.g., Hive Server, Oozie).

```xml
<!-- Allow the super user (e.g., 'hadoop') to impersonate any user -->
<property>
    <name>fs.oss.hdfs.proxy.user.hadoop.hosts</name>
    <value>*</value>
</property>

<property>
    <name>fs.oss.hdfs.proxy.user.hadoop.groups</name>
    <value>*</value>
</property>

<!-- Or restrict to specific users/groups -->
<property>
    <name>fs.oss.hdfs.proxy.user.hadoop.users</name>
    <value>user1,user2</value>
</property>
```

## UserGroupsMapping

Configure mappings between users and user groups for fine-grained access control.

## Key Considerations

| Feature | Detail |
|---------|--------|
| **Authentication** | RAM user, RAM role, STS token, or instance role |
| **RootPolicy** | Defines superuser privileges at the namespace level |
| **ProxyUser** | Enables impersonation for multi-tenant services |
| **SDK Version** | Use JindoSDK 4.x+ (recommended 6.x for latest features) |
| **Compatibility** | Compatible with Hadoop 2.x/3.x APIs |
| **Endpoint** | Use `oss-dls.aliyuncs.com` (not standard OSS endpoint) |

## Notes

- For **EMR clusters**, JindoSDK is typically pre-installed.
- For **self-managed Hadoop clusters**, you need to manually download and deploy the JindoSDK.
- You can use **STS tokens** or **credential providers** instead of hardcoding AccessKey credentials for better security.
