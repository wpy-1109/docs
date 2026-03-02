# Directly read archived objects in real time without restoring them

The Archive Direct Read feature lets you directly access files in the Archive storage class in scenarios such as data lakes and cloud photo albums without having to [restore](https://www.alibabacloud.com/help/en/oss/user-guide/restore-objects-for-access) them in advance. This feature helps you maintain low storage costs while enabling real-time access to infrequently accessed data, providing a balance between storage costs and access efficiency.

## Restoring and reading vs. direct reading


The following table compares the differences before and after you enable Archive Direct Read.











| Item | Archive Direct Read disabled (Default) | Archive Direct Read enabled |
| --- | --- | --- |
| Retrieval method | Restore and then read | Direct read |
| Retrieval fee① | Low | High |
| Retrieval time | Minutes | Milliseconds |


①For more information about retrieval fees, see [OSS Pricing](https://www.alibabacloud.com/zh/product/oss/pricing).

## Enable Archive Direct Read

## OSS console


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left navigation pane, choose Data Management > Archive Direct Read.

-

On the Archive Direct Read page, enable Archive Direct Read.

-

In the message that appears, click OK.

## ossutil


Before you use ossutil, you must [install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


-

The following command enables Archive Direct Read for a bucket named `examplebucket`.


`bash
ossutil api put-bucket-archive-direct-read --bucket examplebucket --archive-direct-read-configuration "{\"Enabled\":\"true\"}"
`


For more information about this command, see [put-bucket-archive-direct-read](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-archive-direct-read).

-

The following command queries whether Archive Direct Read is enabled for a bucket named `examplebucket`.


`bash
ossutil api get-bucket-archive-direct-read --bucket examplebucket
`


For more information about this command, see [get-bucket-archive-direct-read](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-archive-direct-read).

## API


If your program has high customization requirements, you can call REST API operations directly. To do this, you must manually write code to calculate signatures. For more information, see [PutBucketArchiveDirectRead](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketarchivedirectread) and [GetBucketArchiveDirectRead](https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketarchivedirectread).

## Read operations


After you enable Archive Direct Read, you can perform the following read operations directly on files in the Archive storage class in the bucket without restoring them:


-

[GetObject](https://www.alibabacloud.com/help/en/oss/developer-reference/getobject)

-

[CopyObject](https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject#reference-mvx-xxc-5db)

-

[UploadPartCopy](https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpartcopy)

-

[ProcessImage](https://www.alibabacloud.com/help/en/oss/user-guide/img-implementation-modes)

-

[PostProcessTask](https://www.alibabacloud.com/help/en/oss/user-guide/save-processed-images#t4800.html)

## Query the access records of objects that are generated using Archive Direct Read


-

If you have not enabled the field index for `archive_direct_read_size` in Simple Log Service, run the following command to query in scan mode:


`sql
* and __topic__: oss_access_log and bucket: bucketname | set session mode=scan; select object where archive_direct_read_size not like '-'
`


-

If you have enabled the field index for `archive_direct_read_size` in [Simple Log Service](https://sls.console.alibabacloud.com/), run the following command to query in index mode:


`sql
* and __topic__: oss_access_log and bucket: bucketname |select object where archive_direct_read_size not like '-'
`


## Query the traffic that is generated using Archive Direct Read


-

If you have not enabled the field index for `archive_direct_read_size` in Simple Log Service, run the following command to perform a query in scan mode:


`sql
* and __topic__: oss_access_log and bucket: bucketname | set session mode=scan; select sum(cast(archive_direct_read_size as bigint)) as total_size where archive_direct_read_size != '-'
`


-

If you have enabled the field index for `archive_direct_read_size` in [Simple Log Service](https://sls.console.alibabacloud.com/), run the following command to perform a query in index mode:


`sql
* and __topic__: oss_access_log and bucket: bucketname | select sum(cast(archive_direct_read_size as bigint)) as total_size where archive_direct_read_size != '-'
`


## Permissions


A Resource Access Management (RAM) user must have the following permissions: `oss:PutBucketArchiveDirectRead` and `oss:GetBucketArchiveDirectRead`. For more information, see [Grant custom permissions to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Limits


-

Archive Direct Read applies only to files in the Archive storage class in a bucket. It does not apply to files in the Cold Archive or Deep Cold Archive storage classes.

-

If Archive Direct Read is enabled for a bucket and you set the default index page or default error page for static website hosting to an unrestored archived object in the same bucket, access to the page fails and a 403 error is returned. To ensure that the page can be accessed, we recommend that you set the default index page and default error page to files in the Standard storage class.

## Billing


-

After you enable Archive Direct Read for a bucket, you are charged for the volume of data retrieved using Archive Direct Read (RetrievalDataArchiveDirect) when you directly read unrestored files in the Archive storage class. The volume of retrieved data for a request is indicated by the `archive_direct_read_size` log field. If you read files that have already been restored from the Archive storage class, no retrieval fees are incurred. For more information, see [Data processing fees](https://www.alibabacloud.com/help/en/oss/data-processing-fees).

-

The volume of data retrieved using Archive Direct Read depends on the data read range specified in the request header when an HTTP connection is established. Terminating a data transfer early does not affect the billable volume of retrieved data for the request. For example, if you request a range of 100 MB to 200 MB but the connection is terminated after only 1 byte is read, you are still charged for the entire 100 MB to 200 MB range.

-

If you use the Archive Direct Read feature to perform image scaling operations on archived images, OSS calculates the volume of data retrieved using Archive Direct Read based on the size of the source image, not the size of the processed image. This means that you are charged for data retrieval based on the source image size, even if the actual bandwidth used for the transfer is significantly lower because the image was scaled down. For example, if the source image is 1 GB and is scaled to 100 KB, the billable volume of data retrieved using Archive Direct Read is 1 GB.

Thank you! We've received your  feedback.