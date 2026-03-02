# How to schedule backups for OSS data for recovery

Accidental deletions, overwrites, and modifications can cause permanent data loss. Scheduled backup uses Cloud Backup to periodically back up objects in a bucket, so they can be restored at any time.

## Prerequisites


Before you begin, make sure that you have:


-

Activated [Cloud Backup](https://www.alibabacloud.com/zh/products/hybrid-backup-recovery)

-

Authorized Cloud Backup to read data from OSS. Log on to the [Cloud Backup console](https://hbr.console.alibabacloud.com), click OSS Backup, and follow the on-screen instructions

## Billing


Cloud Backup charges for storage capacity and OSS requests. For details, see [Billing](https://www.alibabacloud.com/help/en/cloud-backup/user-guide/oss-backup-overview#section-gbp-k0w-479).

## Limitations


-

Only Standard and Infrequent Access buckets and objects are supported. Archive, Cold Archive, and Deep Cold Archive buckets and objects are not supported.

-

Object access control lists (ACLs) are not backed up or restored.

-

Scheduled backup is available in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Chengdu), Hong Kong (China), Germany (Frankfurt), UK (London), US (Virginia), Japan (Tokyo), South Korea (Seoul), Singapore, Indonesia (Jakarta), Malaysia (Kuala Lumpur), Philippines (Manila), Thailand (Bangkok), US (Silicon Valley), UAE (Dubai), and Saudi Arabia (Riyadh).

## Create a backup plan for an existing bucket


-

Log on to the [OSS](https://oss.console.alibabacloud.com/) console.

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the navigation pane on the left, choose Data Management > Scheduled Backup.

-

In the Scheduled Backup panel, create a free or paid backup plan.

### Free backup plan


Cloud Backup offers a 30-day free trial. No Cloud Backup fees are incurred during the trial period.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

In a free backup plan, the source path and backup cycle cannot be edited. Each free plan uses an independent backup vault. After converting to a paid plan, the backup vault cannot be changed. To back up all data to the same backup vault, use a paid plan instead.


-

On the Backup Plan tab, click Create Backup Plan.

-

In the Create Backup Plan panel, keep the default settings.

-

Click OK.

### Paid backup plan


A paid plan provides full control over the backup interval, retention period, and which objects to back up.


-

On the Backup Plan tab, click Create Backup Plan.

-

In the Create Backup Plan panel, click Switch To Paid Plan.

-

In the dialog box, click Confirm.

-

Configure the following parameters.














(https://www.alibabacloud.com/help/en/cloud-backup/user-guide/manage-backup-policies)





(https://www.alibabacloud.com/help/en/cloud-backup/user-guide/use-an-oss-inventory-list-to-create-a-backup-plan-for-a-large-amount-of-oss-data#task-2092823)


| Parameter | Description |
| --- | --- |
| Backup Bucket Prefix | The prefix of the objects to back up. Leave blank to back up all objects in the bucket. |
| Backup Policy | Select Create Policy. For more information, see Manage backup policies. |
| Use OSS Inventory | Use the OSS inventory feature to improve incremental backup performance for large datasets. For details, see Back up large amounts of OSS data using the inventory feature. |


-

Click OK.


Cloud Backup runs backup jobs based on the schedule and interval specified in the plan.

## Enable scheduled backup when creating a bucket


-

Log on to the [OSS](https://oss.console.alibabacloud.com/) console.

-

Click Buckets, and then click Create Bucket.

-

In the Create Bucket panel, turn on Scheduled Backup. For other parameters, see [Create a bucket](https://www.alibabacloud.com/help/en/oss/manage-buckets-create-buckets#concept-bcz-sbz-5db).

-

Click OK.


After the bucket is created, a backup plan is automatically created with the following defaults:


-

Backs up data once per day

-

Retains backups for one week

-

Includes a 30-day free trial


To view or modify the plan, choose Data Management > Scheduled Backup.

## References


Restore backed-up files to OSS by creating restore jobs. For details, see [Create an OSS restore job](https://www.alibabacloud.com/help/en/cloud-backup/user-guide/create-an-oss-restore-job#task-2092826).


Thank you! We've received your  feedback.