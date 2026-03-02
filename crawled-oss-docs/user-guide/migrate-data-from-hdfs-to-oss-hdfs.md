# Migrate data from HDFS to OSS-HDFS for data backup and disaster recovery

If you want to back up data or scale out storage space in Hadoop Distributed File System (HDFS), you can migrate data from HDFS to OSS-HDFS by using the Jindo DistCp tool that is automatically deployed in an Alibaba Cloud E-MapReduce (EMR) cluster. OSS-HDFS is compatible with the Hadoop ecosystem. After migrating data from HDFS to OSS-HDFS, you can use various tools and frameworks of the Hadoop ecosystem to process and analyze data.

## Prerequisites


-

A cluster of Alibaba Cloud EMR-5.6.0 or later versions or a cluster of EMR-3.40.0 or later versions is created. For more information, see [Create a cluster](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/create-a-cluster-on-the-emr-on-ecs-page#task-2136630).

-

An environment of Hadoop 2.7.0 or later or Hadoop 3.x is prepared in your self-managed Elastic Compute Service (ECS) cluster. The cluster must be able to run MapReduce jobs. You must deploy [JindoData](https://github.com/aliyun/alibabacloud-jindodata/blob/master/docs/user/4.x/jindodata_download.md) on your own before completing the migration in the ECS cluster. JindoData includes JindoSDK and JindoFSx. We recommend that you download the latest version.

-

OSS-HDFS is enabled for a bucket and permissions are granted to access OSS-HDFS. For more information, see [Enable OSS-HDFS](https://www.alibabacloud.com/help/en/oss/user-guide/enable-oss-hdfs-service#task-2201339).

## Background information


You can use Jindo DistCp to copy files within or between large-scale clusters. Jindo DistCp uses MapReduce to distribute files, handle errors, and restore data. The lists of files and directories are used as the input of the MapReduce tasks. Each task copies specific files and directories in the input list. Jindo DistCp supports full data copy between directories in HDFS, between HDFS and Object Storage Service (OSS), between HDFS and OSS-HDFS, and between buckets in OSS-HDFS. Jindo DistCp also provides various custom copy parameters and copy policies.


Jindo DistCp provides the following benefits:


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

## Procedure


-

Log on to the EMR cluster.


-

Log on to the EMR console. In the left-side navigation pane, click [EMR on ECS](https://emr.console.alibabacloud.com/#/region/cn-hangzhou/resource/all/ecs/list).

-

Click the EMR cluster that you created.

-

Click the Nodes tab, and then click the ![+.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/2676424071/p747238.jpg) icon on the left side of the node group.

-

Click the ID of the ECS instance. On the Instances page, click Connect next to the instance ID.


For more information about how to log on to a cluster in Windows or Linux by using an SSH key pair or SSH password, see [Log on to a cluster](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/log-on-to-an-emr-cluster#task-2508490).

-

Migrate data from a specified path in HDFS to OSS-HDFS.


-

Run the following command to view the data in HDFS:


`shell
hdfs dfs -ls /
`


Sample response:


`shell
Found 8 items
drwxrwxrwx - admin supergroup 0 2023-10-26 10:55 /.sysinfo
drwxrwxrwx - hadoop supergroup 0 2023-10-26 10:55 /apps
drwxrwxrwx - root supergroup 0 2022-08-03 15:54 /data
-rw-r----- 1 root supergroup 13 2022-08-25 11:45 /examplefile.txt
drwxrwxrwx - spark supergroup 0 2023-10-26 14:49 /spark-history
drwx-wx-wx - hive supergroup 0 2023-10-26 13:35 /tmp
drwxrwxrwx - hive supergroup 0 2023-10-26 14:48 /user
drwxrwxrwx - hadoop supergroup 0 2023-10-26 14:48 /yarn
`


-

Switch to the directory where the jindo-distcp-tool-${version}.jar package is located.


`shell
cd /opt/apps/JINDOSDK/jindosdk-current/tools
`


-

View the jindo-distcp-tool version that is automatically deployed in the EMR cluster.


`shell
ls
`


-

Migrate data from HDFS to OSS-HDFS.

#### Migrate or copy full data


Migrate or copy data in the specified directory, such as /tmp, of HDFS to the destination OSS-HDFS path, such as oss://examplebucket/dir. In the example of this topic, jindo-distcp-tool-6.1.0.jar is used. You must replace the version number with the actual version number.


`shell
hadoop jar jindo-distcp-tool-6.1.0.jar --src /tmp/ --dest oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/dir/ --hadoopConf fs.oss.accessKeyId=LTAI  --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --parallelism 10
`


The following table describes the parameters and options in the command.











-


`shell

`


-


`shell

`


| Parameter/Option | Description | Example |
| --- | --- | --- |
| --src | The source path of the data in HDFS that you want to migrate or copy. | /tmp/ |
| --dest | The destination path in OSS-HDFS to which the migrated or copied data is saved. | oss://destbucket.cn-hangzhou.oss-dls.aliyuncs.com/dir/ |
| --hadoopConf | The AccessKey pair that is used to access OSS-HDFS. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. | AccessKey IDLTAI AccessKey SecretyourAccessKeySecret |
| --parallelism | The number of data migration threads or data copying threads that can be concurrently run based on the number of resources in your cluster. | 10 |


#### Migrate or copy incremental data


If you want to migrate or copy only incremental data from the source path after a full data migration or copy, you can use the --update option.


The following sample code shows how to migrate or copy incremental data from data/ in HDFS to oss://destbucket/dir in OSS-HDFS.


`shell
hadoop jar jindo-distcp-tool-6.1.0.jar --src /data/ --dest oss://destbucket.cn-hangzhou.oss-dls.aliyuncs.com/dir/ --hadoopConf fs.oss.accessKeyId=LTAI  --hadoopConf fs.oss.accessKeySecret=yourAccessKeySecret --update --parallelism 10
`


## References


-

If you do not want to manually add the endpoint and AccessKey pair each time you run the migration command, you can pre-configure the endpoint and AccessKey pair in the Hadoop configuration file core-site.xml. For more information, see [Connect non-EMR clusters to OSS-HDFS](https://www.alibabacloud.com/help/en/oss/user-guide/connect-non-emr-clusters-to-oss-hdfs).

-

For more information about other usage scenarios of Jindo DistCp, see [Use Jindo DistCp](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/use-jindo-distcp-7#task-2526637).


Thank you! We've received your  feedback.