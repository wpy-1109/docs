# Use Alibaba Cloud Jindo DistCp to migrate data across multiple buckets in OSS-HDFS

This topic describes how to use Alibaba Cloud Jindo DistCp to migrate data across multiple buckets in OSS-HDFS.

## Prerequisites


-

A cluster of Alibaba Cloud EMR-5.6.0 or later versions or a cluster of EMR-3.40.0 or later versions is created. For more information, see [Create a cluster](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/create-a-cluster-on-the-emr-on-ecs-page#task-2136630).

-

An environment of Hadoop 2.7.0 or later or Hadoop 3.x is prepared in your self-managed Elastic Compute Service (ECS) cluster. The cluster must be able to run MapReduce jobs. You must deploy [JindoData](https://github.com/aliyun/alibabacloud-jindodata/blob/master/docs/user/4.x/jindodata_download.md) on your own before completing the migration in the ECS cluster. JindoData includes JindoSDK and JindoFSx. We recommend that you download the latest version.

-

OSS-HDFS is enabled for a bucket and permissions are granted to access OSS-HDFS. For more information, see [Enable OSS-HDFS and grant access permissions](https://www.alibabacloud.com/help/en/oss/user-guide/enable-oss-hdfs-service#task-2201339).

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

## Step 1: Download the JAR package of Jindo DistCp


[GitHub](https://github.com/aliyun/alibabacloud-jindodata/blob/latest/docs/user/en/jindosdk/jindosdk_download.md)

## Step 2: Configure the AccessKey pair that is used to access OSS-HDFS


You can use one of the following methods to configure the AccessKey pair that is used to access OSS-HDFS:


-

Configure the AccessKey pair by using the sample command


Configure the AccessKey pair by specifying the --hadoopConf option in the sample command that is used to migrate data from srcbucket to destbucket in OSS-HDFS.


`plaintext
hadoop jar jindo-distcp-tool-${version}.jar --src oss://srcbucket.cn-hangzhou.oss-dls.aliyuncs.com/ --dest oss://destbucket.cn-hangzhou.oss-dls.aliyuncs.com/ --hadoopConf fs.oss.accessKeyId=yourkey --hadoopConf fs.oss.accessKeySecret=yoursecret --parallelism 10
`


-

Configure the AccessKey pair by using a configuration file


Configure the AccessKey pair that is used to access OSS-HDFS by specifying fs.oss.accessKeyId and fs.oss.accessKeySecret in the core-site.xml file of Hadoop. Sample command:


`plaintext
<configuration>
    <property>
        <name>fs.oss.accessKeyId</name>
        <value>LTAI</value>
    </property>

    <property>
        <name>fs.oss.accessKeySecret</name>
        <value>KZo1</value>
    </property>
</configuration>
`


## Step 3: Configure the endpoint of OSS-HDFS


You must configure the endpoint of OSS-HDFS when you use OSS-HDFS to access buckets in OSS. We recommend that you specify the access path in the `oss://<Bucket>.<Endpoint>/<Object>` format. Example: `oss://examplebucket.cn-shanghai.oss-dls.aliyuncs.com/exampleobject.txt`. After you configure the access path, JindoSDK calls the corresponding OSS-HDFS operation based on the specified endpoint in the access path.


You can also configure the endpoint of OSS-HDFS by using other methods. The endpoints that are configured by using different methods have different priorities. For more information, see [Appendix 1: Other methods used to configure the endpoint of OSS-HDFS](https://www.alibabacloud.com/help/en/oss/user-guide/connect-non-emr-clusters-to-oss-hdfs#section-tbb-w3j-rnq).

## Step 4: Migrate full data across multiple buckets in OSS-HDFS


In this example, Jindo DistCp 4.4.0 is used. Replace the version number with your actual version number.

### Use the same AccessKey pair to migrate data from Bucket A to Bucket B in the same region


-

Command syntax


`plaintext
hadoop jar jindo-distcp-tool-${version}.jar --src oss://bucketname.region.oss-dls.aliyuncs.com/ --dest oss://bucketname.region.oss-dls.aliyuncs.com/ --hadoopConf fs.oss.accessKeyId=yourkey --hadoopConf fs.oss.accessKeySecret=yoursecret --parallelism 10
`


The following table describes the parameters and options in the preceding command.











-


`plaintext

`


-


`plaintext

`


| Parameter/Option | Description | Example |
| --- | --- | --- |
| --src | The full path of the source bucket in OSS-HDFS from which data is migrated or copied. | oss://srcbucket.cn-hangzhou.oss-dls.aliyuncs.com/ |
| --dest | The full path of the destination bucket in OSS-HDFS to which the migrated or copied data is saved. | oss://destbucket.cn-hangzhou.oss-dls.aliyuncs.com/ |
| --hadoopConf | The AccessKey pair that is used to access OSS-HDFS. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. | AccessKey IDLTAIAccessKey SecretKZo1 |
| --parallelism | The number of data migration tasks or data copy tasks that can be run in parallel based on the number of resources in your cluster. | 10 |


-

Example


Run the following command to migrate data from srcbucket in the China (Hangzhou) region to destbucket by using the same AccessKey pair:


`plaintext
hadoop jar jindo-distcp-tool-4.4.0.jar --src oss://srcbucket.cn-hangzhou.oss-dls.aliyuncs.com/ --dest oss://destbucket.cn-hangzhou.oss-dls.aliyuncs.com/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=KZo1 --parallelism 10
`


## (Optional) Migrate incremental data across multiple buckets in OSS-HDFS


If you want to migrate or copy only incremental data from the source path after a full data migration or copy, you can use the --update option.


For example, you can run the following command to migrate incremental data from srcbucket in the China (Hangzhou) region to destbucket by using the same AccessKey pair:


`plaintext
hadoop jar jindo-distcp-tool-4.4.0.jar --src oss://srcbucket.cn-hangzhou.oss-dls.aliyuncs.com/ --dest oss://destbucket.cn-hangzhou.oss-dls.aliyuncs.com/ --hadoopConf fs.oss.accessKeyId=LTAI --hadoopConf fs.oss.accessKeySecret=KZo1 --update --parallelism 10
`


## References


For more information about other scenarios of Jindo DistCp, see [Use Jindo DistCp](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/use-jindo-distcp-7#task-2526637).


Thank you! We've received your  feedback.