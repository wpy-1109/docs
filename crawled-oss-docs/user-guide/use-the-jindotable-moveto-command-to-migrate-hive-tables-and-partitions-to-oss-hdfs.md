# Migrate Hive tables and partitions to OSS-HDFS using the JindoTable MoveTo command

This topic describes how to use the JindoTable MoveTo command to migrate Hive tables and partitions to OSS-HDFS.

## Prerequisites


-

An E-MapReduce (EMR) cluster of version 3.36.0 or later is created. Alternatively, an EMR cluster of version 5.2.0 is created. EMR V3.39.X and EMR V5.5.X are not supported.

-

A partitioned table is created by using the Hive command and data is written to the table. In this example, the table name is set to test_table, the partition name is set to dt, and the partition value is set to value.

-

OSS-HDFS is enabled and permissions are granted to access OSS-HDFS. For more information, see [Connect non-EMR clusters to OSS-HDFS](https://www.alibabacloud.com/help/en/oss/user-guide/connect-non-emr-clusters-to-oss-hdfs#task-2128488).

## Background information


The MoveTo command can automatically update metadata after the command copies the underlying data. This way, data in a table or partitions can be fully migrated to the destination path. You can configure filter conditions for the MoveTo command to migrate a large number of partitions at the same time. JindoTable also provides some protective measures to ensure data integrity and security when the MoveTo command is used to migrate data.

## Procedure


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Only one MoveTo process can run at a time on an EMR cluster. If you attempt to start a MoveTo process on an EMR cluster in which another MoveTo process is running, your request is rejected because the configuration lock is unavailable. A message that contains information about the running MoveTo process is also displayed. In this case, you can terminate the running MoveTo process and start a new MoveTo process, or wait for the running MoveTo process to end.


- Log on to your cluster in SSH mode. For more information, see [Log on to a cluster](https://www.alibabacloud.com/help/en/emr/emr-on-ecs/user-guide/log-on-to-a-cluster#task-2508490).
-

Run the following command to obtain help information:


`plaintext
sudo jindo table -help moveTo
`


The following output is returned:


`plaintext
<dbName.tableName>      The table to move.
<destination path>      The destination base directory which is always at the
                          same level of a 'table location', where the moved
                          partitions or un-partitioned data would located in.
<condition>/-fullTable  A filter condition to determine which partitions should
                          be moved, supporting common operators (like '>') and
                          built-in UDFs (like to_date) (UDFs not supported
                          yet...), while -fullTable means that all partitions (or
                          a whole un-partitioned table) should be moved. One but
                          only one option must be specified among -c
                          "<condition>" and -fullTable.
<before days>           Optional, saying that table/partitions should be moved
                          only when they are created (not updated or modified)
                          more than some days before from now.
<parallelism>           The maximum concurrency when copying partitions, 1 by
                          default.
<OSS storage policy>    Storage policy for OSS destination, which can be Standard
                          (by default), IA, Archive, or ColdArchive. Not applicable for destinations other
                          than OSS. NOTE: if you are willing to use ColdArchive storage policy, please
                          make sure that Cold Archive has been enabled for your OSS bucket.

-o/-overWrite           Overwriting the final paths where the data would be moved.
                          For partitioned tables this overwrites partitions locations
                          which are subdirectories of <destination path>; for
                          un-partitioned table this overwrites the <destination path>
                          itself.
-r/-removeSource        Let the source data be removed when the corresponding
                          table/partition is successfully moved to the new destination.
                          Otherwise (by default), the source data would be left as it
                          was.
-skipTrash              Applicable only when [-r/-removeSource] is enabled. If
                          present, source data would be immediately deleted from the
                          file system, bypassing the trash.
-e/-explain             If present, the command would not really move data, but only
                          prints the table/partitions that would be moved for given
                          conditions.
<log directory>         A directory to locate log files, '/tmp/<current user>/' by
                          default.
`


-

Command syntax


`plaintext
sudo jindo table -moveTo \
  -t <dbName.tableName> \
  -d <destination path> \
  [-c "<condition>" | -fullTable] \
  [-b/-before <before days>] \
  [-p/-parallel <parallelism>] \
  [-s/-storagePolicy <OSS storage policy>] \
  [-o/-overWrite] \
  [-r/-removeSource] \
  [-skipTrash] \
  [-e/-explain] \
  [-l/-logDir <log directory>]
`


-

Command description




















- 
- 




> NOTE:

> NOTE: 


> NOTE: 


| Parameter | Required | Description |
| --- | --- | --- |
| -t <dbName.tableName> | Yes | The name of the table that you want to migrate. Specify this parameter in the Database name.Table name format. Separate the database name and the table name with a period (.). The table can be a partitioned table or a non-partitioned table. |
| -d <destination path> | Yes | The destination path to which you want to migrate the table. This parameter specifies a table-level path regardless of whether you migrate a specific partition or an entire non-partitioned table. If you migrate a partition, the full path of the partition consists of the destination path and the name of the partition. Example: <destination path>/p1=v1/p2=v2/. |
| -c "<condition>" | -fullTable | No | You must specify one of the -c "<condition>" and -fullTable variables. If you specify -fullTable, the entire partitioned or non-partitioned table is archived. If you specify -c "<condition>", only the partitions that meet the filter condition are archived. Common operators, such as greater-than signs (>), are supported. For example, if the partition key column is the ds column whose data type is String and you want to archive partitions whose partition names are greater than 'd', use -c " ds > 'd' ". |
| -b/before <before days> | No | Only tables or partitions that were created at least a specific number of days ago can be migrated. |
| -p/-parallel <parallelism> | No | The maximum number of partitions or tables that can be migrated in parallel. |
| -s/-storagePolicy <OSS storage policy> | No | This parameter is not supported by OSS-HDFS. |
| -o/-overWrite | No | Specifies whether to forcefully overwrite the destination path. For a partitioned table, only the destination path of the partition that you want to migrate is overwritten. |
| -r/-removeSource | No | Specifies whether to clear the source path after data is migrated and metadata is updated. For a partitioned table, only the source path of the partition that is migrated is cleared. |
| -skipTrash | No | Specifies whether to skip the Trash directory when the source path is cleared. Note You must use this parameter together with the -r/-removeSource parameter. |
| -e/-explain | No | The explain mode. In explain mode, the list of partitions that you want to migrate is displayed, but no data is migrated. |
| -l/-logDir <log directory> | No | The directory in which log files are stored. Default value: /tmp/<current user>/. |


-

Migrate partitions to OSS-HDFS.


-

Query the partitions that you want to migrate.


Commands that contain the -e option only list the partitions that you want to migrate, but no data is migrated.


`plaintext
sudo jindotable -moveTo -t tdb.test_table -d oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/data/tdb.test_table -c " dt > 'v' " -e
`


Command output:


`plaintext
Found 1 partitions to move:
      dt=value-2
MoveTo finished for table tdb.test_table to destination oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/data/tdb.test_table with condition " dt > 'v' " (explain only).
`


-

Migrate the partition to OSS-HDFS.


`plaintext
sudo jindotable -moveTo -t tdb.test_table -d oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/data/tdb.test_table  -c " dt > 'v' "
`


Command output:


`plaintext
Found 1 partitions in total, and all are successfully moved.
Successfully moved partitions:
    dt=value-2
No failed partition.
MoveTo finished for table tdb.test_table to destination oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/data/tdb.test_table with condition " dt > 'v' ".
`


-

Query the location of the partition to check whether the partition is migrated.


`plaintext
sudo hive> desc formatted test_table partition (dt='value-2');
`


Command output:


`plaintext
OK
# col_name              data_type               comment
id                      int
content                 string

# Partition Information
# col_name              data_type               comment
dt                      string

# Detailed Partition Information
Partition Value:        [value-2]
Database:               tdb
Table:                  test_table
CreateTime:             UNKNOWN
LastAccessTime:         UNKNOWN
Location:               oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/data/tdb.test_table/dt=value-2
`


-

Optional: Migrate the partition from OSS-HDFS to Hadoop Distributed File System (HDFS).


`plaintext
sudo jindotable -moveTo -t tdb.test_table -d hdfs://<hdfs-path>/user/hive/warehouse/tdb.db/test_table  -c " dt > 'v' "
`


Command output:


`plaintext
No successfully moved partition.
Failed partitions:
    dt=value-2    New location is not empty but -overWrite is not enabled.
MoveTo finished for table tdb.test_table to destination hdfs://<hdfs-path>/user/hive/warehouse/tdb.db/test_table with condition -c " dt > 'v' ".
`


The No successfully moved partition. error message is returned because the destination directory in HDFS is not empty. If you want to clear the destination directory, use the -overWrite parameter to forcefully overwrite it. This way, the partition can be migrated from OSS-HDFS to HDFS.


`plaintext
sudo jindotable -moveTo -t tdb.test_table -d hdfs://<hdfs-path>/user/hive/warehouse/tdb.db/test_table  -c " dt > 'v' "
`


If the partition is migrated, the following command output is returned:


`plaintext
Found 1 partitions in total, and all are successfully moved.
Successfully moved partitions:
    dt=value-2
No failed partition.
MoveTo finished for table tdb.test_table to destination hdfs:///user/hive/warehouse/tdb.db/test_table with condition " dt > 'v' ", overwriting new locations.
`


## Exception handling


If the migration fails with a Conflicts found error, perform the following operations to handle the issue:


-

Make sure that no commands other than the JindoTable MoveTo command are run to migrate data to the destination path, such as DistCp and JindoDistCp.

-

Delete the destination directory. For non-partitioned tables, delete the table-level directory. For partitioned tables, delete the partition-level directory that conflicts.

-

Do not delete the source directory.

Thank you! We've received your  feedback.