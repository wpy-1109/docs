# Migrate data from a semi-hosted JindoFS cluster to OSS-HDFS

This topic describes how to migrate data from a semi-hosted JindoFS cluster to the OSS-HDFS service.

## Prerequisites


-

The bucket that stores the data of the semi-hosted JindoFS cluster has OSS-HDFS enabled.

-

The semi-hosted JindoFS cluster has audit logging enabled.

-

The latest jindosdk is installed and configured. For more information, visit [GitHub](https://github.com/aliyun/alibabacloud-jindodata/blob/latest/docs/user/en/jindosdk/jindosdk_download.md).

## Step 1: Migrate full data


In full data migration mode, you can migrate the metadata in a directory from the semi-hosted JindoFS cluster to a directory in OSS-HDFS at a time. You can migrate data to only first-level subdirectories in OSS-HDFS.


-

Command syntax


`plaintext
jindo distjob -migrateImport -srcPath <srcPath> -destPath <destPath> -backendLoc <backendLoc>
`


The following table describes the parameters in the command syntax.








| Parameter | Description |
| --- | --- |
| -srcPath | The source path that stores the data of the semi-hosted JindoFS cluster before migration. |
| -destPath | The destination path in OSS-HDFS that stores the data of the semi-hosted JindoFS cluster after migration. |
| -backendLoc | The Object Storage Service (OSS) path that stores the source data of the semi-hosted JindoFS cluster. |


-

Example


Migrate full data from the jfs://mycluster/foo directory in the semi-hosted JindoFS cluster to the bar directory in OSS-HDFS. Data of OSS-HDFS is stored in the examplebucket bucket.


`plaintext
jindo distjob -migrateImport -srcPath jfs://mycluster/foo -destPath oss://examplebucket/bar/
`


## Step 2: (Optional) Migrate incremental data


-

Convert the audit logs of the semi-hosted JindoFS cluster into change logs.


To migrate incremental data of the semi-hosted JindoFS cluster to OSS-HDFS, you must use a Jindo tool to convert the audit logs of the semi-hosted JindoFS cluster into change logs.


-

Command syntax


`plaintext
jindo distjob -mkchangelog -auditLogDir <auditLogDir> -changeLogDir <changeLogDir> -startTime <startTime>
`


The following table describes the parameters in the command syntax.








| Parameter | Description |
| --- | --- |
| -auditLogDir | The path that stores the audit logs of the semi-hosted JindoFS cluster. |
| -changeLogDir | The path that stores the generated change logs. |
| -startTime | The time to start converting audit logs. |


-

Example


Convert audit logs of the semi-hosted JindoFS cluster in the oss://examplebucket/sysinfo/auditlog path into change logs and store the change logs in the oss://examplebucket/sysinfo/changelog path. In this example, only audit logs that are generated as of June 1, 2022 are converted.


`plaintext
jindo distjob -mkchangelog -auditLogDir oss://examplebucket/sysinfo/auditlog -changeLogDir oss://examplebucket/sysinfo/changelog -startTime 2022-06-01T12:00:00Z
`


-

Migrate incremental data for one time.


You can migrate incremental metadata updates from the semi-hosted JindoFS cluster to OSS-HDFS as audit logs are converted into change logs.


-

Command syntax


`plaintext
jindo distjob -migrateImport -srcPath <srcPath> -destPath <destPath> -changeLogDir <changeLogDir> -backendLoc <backendLoc> -update
`


The following table describes the parameters in the command syntax.








| Parameter | Description |
| --- | --- |
| -srcPath | The source path that stores the data of the semi-hosted JindoFS cluster before migration. |
| -destPath | The destination path in OSS-HDFS that stores the data of the semi-hosted JindoFS cluster after migration. |
| -changeLogDir | The path that stores the generated change logs. |
| -backendLoc | The OSS path that stores the source data of the semi-hosted JindoFS cluster. |
| -update | Enables the incremental data migration mode. |


-

Example


Migrate incremental data from the jfs://mycluster/foo directory in the semi-hosted JindoFS cluster to the bar directory in OSS-HDFS. In this example, data of OSS-HDFS is stored in the examplebucket bucket. The generated change logs are stored in the oss://logbucket/logdir/ path.


`plaintext
jindo distjob -migrateImport -srcPath jfs://mycluster/foo -destPath oss://examplebucket/bar/ -changeLogDir oss://logbucket/logdir/ -backendLoc oss://examplebucket/jfsdataDir -update
`


-

Optional: Migrate incremental data multiple times.


To migrate incremental data from the semi-hosted JindoFS cluster to OSS-HDFS multiple times, you can set the -startTime parameter to customize the time range to convert audit logs. Then, repeat [Step 1] and [Step 2].

Thank you! We've received your  feedback.