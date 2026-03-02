# Migrate data from HDFS to OSS

This topic describes how to use Jindo DistCp to migrate data in an EMR Hadoop cluster from Hadoop Distributed File System (HDFS) to Object Storage Service (OSS). Jindo DistCp is a data copy tool provided by Alibaba Cloud.

## Background information


HDFS is used as the underlying storage for a large amount of data in traditional big data architectures. The DistCp tool provided by Hadoop is used to migrate or copy data in HDFS. However, this tool cannot take advantage of the features of OSS, which results in low efficiency and poor data consistency. In addition, DistCp provides only simple features, which cannot meet user requirements.


Jindo DistCp can be used to copy files in a distributed file system. You can use Jindo DistCp to copy files within or between large-scale clusters. Jindo DistCp uses MapReduce to distribute files, handle errors, and restore data. The lists of files and directories are used as the input of the MapReduce jobs. Each task copies specific files and directories in the input list. Jindo DistCp allows you to copy data between HDFS DataNodes, between HDFS and OSS, and between OSS buckets. It also provides various custom parameters and policies for data copy.


Compared with Hadoop DistCp, Jindo DistCp has the following advantages in data migration from HDFS to OSS:


-

High efficiency. The data migration speed of Jindo DistCp is 1.59 times faster than that of Hadoop DistCp.

-

Rich basic features. Jindo DistCp provides multiple copy methods and various scenario-based optimization policies.

-

Deep integration with OSS. Jindo DistCp takes advantage of OSS features so that you can perform various operations on data, including compressing data and converting the data storage class to Archive.

-

File copy without changing file names. This ensures data consistency.

-

High compatibility. Jindo DistCp is applicable to various scenarios and can be used to replace Hadoop DistCp. Jindo DistCp supports Hadoop 2.7.x and Hadoop 3.x.

## Prerequisites


An EMR cluster 3.28.0 or later is created. For more information, see [Create a cluster](https://www.alibabacloud.com/help/en/emr/create-a-cluster).


For the EMR cluster 3.28.0 or later, you can use Jindo DistCp by running Shell commands. For more information, see [Use Jindo DistCp](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/use-jindo-distcp-7#task-2526637). For an EMR cluster earlier than 3.28.0, you may encounter compatibility issues. In that case, [submit a ticket](https://smartservice.console.alibabacloud.com/#/ticket/createIndex) to reach technical support.


If a self-managed Elastic Compute Service (ECS) cluster is used, a Hadoop 2.7.x or Hadoop 3.x environment is deployed and MapReduce jobs can be run in the environment.

## Step 1: Download the JAR package of Jindo DistCp


-

Connect to the EMR cluster.


-

Log on to the EMR console. In the left-side navigation pane, click [EMR on ECS](https://emr.console.alibabacloud.com/#/region/cn-hangzhou/resource/all/ecs/list).

-

Click the EMR cluster that you created.

-

Click the Nodes tab, and then click the plus icon (![p480359.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/4113499961/p731861.jpg)) on the left side of the node group.

-

Click the ID of the ECS instance. On the Instances page, click Connect next to the instance ID.


For more information about how to log on to a cluster in Windows or Linux by using an SSH key pair or SSH password, see [Log on to a cluster](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/log-on-to-an-emr-cluster#task-2508490).

-

Download and decompress the latest version of `Jindosdk-${version}.tar.gz`. For more information, see [Download JindoData](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/download-jindodata#main-2325134).

## Step 2: Configure the AccessKey pair used to access OSS


You can use one of the following methods to configure an AccessKey pair:

### Configure the AccessKey pair by using the sample command


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --parallelism 10
`


### Configure the AccessKey pair by using a configuration file


-

Go to the directory in which the core-site.xml Hadoop configuration file is located.


`shell
cd /etc/emr/hadoop-conf/
`


For more information, see [Paths of frequently used files](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/paths-of-frequently-used-files).

-

Run the following command to open the core-site.xml configuration file:


`shell
vim core-site.xml
`


-

Add the following configurations to the core-site.xml configuration file:


`json
<configuration>
    <property>
        <name>fs.oss.accessKeyId</name>
        <value>LTAI</value>
    </property>

    <property>
        <name>fs.oss.accessKeySecret</name>
        <value>YourAccessKeySecret</value>
    </property>

    <property>
        <name>fs.oss.endpoint</name>
        <!-- If you access OSS from an ECS instance, we recommend that you use an internal endpoint of OSS in the oss-cn-xxx-internal.aliyuncs.com format. -->
        <value>oss-cn-xxx.aliyuncs.com</value>
    </property>
</configuration>
`


## Use the password-free feature of JindoFS SDK


If you use the password-free feature of JindoFS SDK, we recommend that you do not store your AccessKey pairs in plaintext. This improves data security. For more information, see [Use the password-free feature of JindoFS SDK](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/use-the-password-free-feature-of-jindofs-sdk-6#task-2435437).

## Step 3: Migrate or copy data


-

Run the following command to view data in HDFS:


`shell
hdfs dfs -ls /
`


Sample response:


`shell
Found 8 items
drwxrwxrwx   - admin  supergroup          0 2023-10-26 10:55 /.sysinfo
drwxrwxrwx   - hadoop supergroup          0 2023-10-26 10:55 /apps
drwxrwxrwx   - root   supergroup          0 2022-08-03 15:54 /data
-rw-r-----   1 root   supergroup         13 2022-08-25 11:45 /examplefile.txt
drwxrwxrwx   - spark  supergroup          0 2023-10-26 14:49 /spark-history
drwx-wx-wx   - hive   supergroup          0 2023-10-26 13:35 /tmp
drwxrwxrwx   - hive   supergroup          0 2023-10-26 14:48 /user
drwxrwxrwx   - hadoop supergroup          0 2023-10-26 14:48 /yarn
`


-

Run the following command to switch to the directory in which the jindo-distjob-tool-${version}.jar package is located:


`shell
cd /opt/apps/JINDOSDK/jindosdk-current/tools
`


-

Migrate data from HDFS to OSS.

### Migrate or copy full data


Run the following command to migrate or copy full data from the /tmp directory in HDFS to oss://examplebucket in OSS:


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --parallelism 10
`


The following table describes the parameters and options in the command.











-

(https://www.alibabacloud.com/help/en/cloud-migration-guide-for-beginners/latest/obtain-an-accesskey-pair#task968)

-

(https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)


> NOTE:

> NOTE: 


> NOTE: 


| Parameter/Option | Description | Example |
| --- | --- | --- |
| --src | The source path of the data that you want to migrate or copy from HDFS. | /tmp/ |
| --dest | The destination path of the data that you want to migrate or copy to OSS. | oss://examplebucket/ |
| --hadoopConf | The AccessKey ID, AccessKey secret, and endpoint that you can use to access OSS. For more information about how to obtain the AccessKey ID and AccessKey secret, see Obtain an AccessKey pair. For more information about regions and endpoints supported by OSS, see OSS regions and endpoints.Important If you access OSS from an ECS instance, we recommend that you use an internal endpoint of OSS in the oss-cn-xxx-internal.aliyuncs.com format. | --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com |
| --parallelism | The number of data migration tasks or data copy tasks that can be run in parallel based on the number of resources in your cluster. | 10 |


### Migrate or copy incremental data


If you want to migrate or copy only the incremental data from the source path after a full data migration or copy, you can specify the --update option.


Run the following command to migrate or copy only incremental data from the /tmp directory in HDFS to oss://examplebucket in OSS:


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --update --parallelism 10
`


By default, checksum is enabled when you specify the --update option. This way, Jindo DistCp compares file names, file sizes, and the checksums of files in the source path and the destination path. If data inconsistency is detected in the preceding items, an incremental data migration or copy is automatically started.


To disable Jindo DistCp from comparing the checksums of files in the source path and the destination path, add the --disableChecksum option to the command. Example:


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --update --disableChecksum --parallelism 10
`


## Appendix 1: Parameters and options supported by Jindo DistCp


Jindo DistCp provides various parameters and options. You can run the following command to obtain information about the parameters and options:


`shell
hadoop jar jindo-distcp-tool-${version}.jar --help
`


The following table describes the parameters and options.











-


-


> NOTE:

> NOTE: 


> NOTE: 


-


-


-


> NOTE:

> NOTE: 


> NOTE: 


| Parameter/Option | Description | Example |
| --- | --- | --- |
| --src | The source path of the data that you want to copy from HDFS. | --src oss://examplebucket/sourcedir |
| --dest | The destination path of the data that you want to copy to OSS. | --dest oss://examplebucket/destdir |
| --bandWidth | The bandwidth for the data copy task. Unit: MB. | --bandWidth 6 |
| --codec | The compression method of the files that you want to copy. Supported compression codecs: gzip, gz, lzo, lzop, and snappy. Supported keywords: none and keep. Descriptions of none and keep:none: The files are saved as uncompressed files. If the files are compressed, Jindo DistCp decompresses the files. keep (default): The files remain compressed. Note If you want to use the Lempel–Ziv–Oberhumer (LZO) compression algorithm in an open source Hadoop cluster, you must install the native library of gplcompression and the Hadoop-LZO package. If you do not want to install the native library and the package, we recommend that you use other compression methods. | --codec gz |
| --policy | The storage class of the files after they are copied to OSS. Valid values:ia: Infrequent Access (IA)archive: ArchiveColdArchive: Cold Archive | --policy coldArchive |
| --filters | The path of a file. Data in each line in the file contains a regular expression, which corresponds to files that do not need to be copied or compared. | --filters test.txt |
| --srcPrefixesFile | The files that you want to copy. The files are prefixed with the path specified by the src parameter. | --srcPrefixesFile prefixes.txt |
| --parallelism | The number of data copy tasks that can be run in parallel. You can set this parameter based on your available cluster resources. Note Default value: 7. | --parallelism 20 |
| --tmp | The directory in which you want to store temporary files when you use Jindo DistCp. | --tmp /tmp |
| --hadoopConf | The AccessKey ID, AccessKey secret, and endpoint that you can use to access OSS. | --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-xxx.aliyuncs.com |
| --disableChecksum | Specifies that checksum verification is disabled. | --disableChecksum |
| --deleteOnSuccess | Specifies that the files that you want to copy from the source path are deleted after they are copied to the destination path. | --deleteOnSuccess |
| --enableTransaction | By default, Jindo DistCp ensures data consistency between tasks. To ensure job-level data integrity and transaction support among jobs, you can use the --enableTransaction parameter. | --enableTransaction |
| --ignore | Specifies that exceptions are ignored during data migration to ensure uninterrupted migration. Errors are reported in the form of Jindo DistCp counters. If you use the --enableCMS parameter, you receive notifications in the specified form. | -ignore |
| --diff | This parameter is used to check whether all files are copied and generate a list of files that fail to be copied. | --diff |
| --update | Specifies that only incremental data is migrated to the destination path. Incremental data refers to data that is added to the source path after the last full data migration or copy. | --update |
| --preserveMeta | When data is migrated, metadata including Owner, Group, Permission, Atime, Mtime, Replication, BlockSize, XAttrs, and ACL is migrated. | --preserveMeta |
| --jobBatch | The number of files processed by each data copy task. Default value: 1000. | --jobBatch 1000 |
| --taskBatch | The number of files processed by each data copy subtask. Default value: 10. | --taskBatch 10 |


## Appendix 2: Sample scenarios

### Scenario 1: How do I check data integrity after data is transmitted to OSS by using Jindo DistCp?


You can use one of the following methods to check data integrity:


-

Method 1: Use Jindo DistCp counters


Parameters included in the information about DistCp counters, such as BYTES_EXPECTED and FILES_EXPECTED, can be used to check data integrity.


`shell
Example
    JindoDistcpCounter
        BYTES_COPIED=10000
        BYTES_EXPECTED=10000
        FILES_COPIED=11
        FILES_EXPECTED=11
        ...
    Shuffle Errors
        BAD_ID=0
        CONNECTION=0
        IO_ERROR=0
        WRONG_LENGTH=0
        WRONG_MAP=0
        WRONG_REDUCE=0
`


The following table describes the parameters that may be included in the Jindo DistCp counters in the preceding example.








| Parameter | Description |
| --- | --- |
| BYTES_COPIED | The number of bytes that have been copied. |
| BYTES_EXPECTED | The number of bytes to be copied. |
| FILES_COPIED | The number of files that have been copied. |
| FILES_EXPECTED | The number of files to be copied. |
| FILES_SKIPPED | The number of files that are skipped when only incremental data is copied. |
| BYTES_SKIPPED | The number of bytes that are skipped when only incremental data is copied. |
| COPY_FAILED | The number of files that fail to be copied. An alert is triggered when the value is not 0. |
| BYTES_FAILED | The number of bytes that fail to be copied. |
| DIFF_FILES | The number of files that are different in the source path and the destination path. An alert is triggered when the value is not 0. |
| DIFF_FAILED | The number of files that are not properly compared. The number is added to the DIFF_FILES value. |
| SRC_MISS | The number of files that do not exist in the source path. The number is added to the DIFF_FILES value. |
| DST_MISS | The number of files that do not exist in the destination path. The number is added to the DIFF_FILES value. |
| LENGTH_DIFF | The number of files that have identical names but different sizes in the source path and the destination path. The number is added to the DIFF_FILES value. |
| CHECKSUM_DIFF | The number of files that fail to pass checksum verification. The number is added to the COPY_FAILED value. |
| SAME_FILES | The number of files that are identical in the source path and the destination path. |


-

Method 2: Use the --diff option


You can use the --diff option to compare the names and the sizes of files in the source path and the destination path. Example:


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --diff
`


### Scenario 2: Which parameters can I use to set the storage class of files that are migrated to OSS to IA, Archive, or Cold Archive?


You can use the --policy option to set the storage class of files that are migrated to OSS to IA, Archive, or Cold Archive. The following code provides an example on how to set the storage class of the migrated files to IA:


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --policy ia --parallelism 10
`


To set the storage class of the migrated files to Archive, replace --policy ia with --policy archive. To set the storage class of the migrated files to Cold Archive, replace --policy ia with --policy coldArchive. Cold Archive is supported only in specific regions. For more information, see [Cold Archive](https://www.alibabacloud.com/help/en/oss/user-guide/overview-53/#section-lfu-pgj-2yn).

### Scenario 3: After data is migrated or copied, which parameters can I configure to delete specific data from the source path?


You can use the --deleteOnSuccess option to delete specific data from the source path after the data is migrated or copied to the destination path.


`shell
hadoop jar jindo-distcp-tool-${version}.jar --src /tmp/ --dest oss://examplebucket/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --hadoopConf fs.oss.endpoint=oss-cn-hangzhou.aliyuncs.com --deleteOnSuccess --parallelism 10
`


Thank you! We've received your  feedback.