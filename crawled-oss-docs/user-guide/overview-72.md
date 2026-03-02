# Monitoring service

The monitoring service of OSS provides metrics to measure the running status and performance of the system. The monitoring service also provides a custom alert service to help you track requests, analyze usage, collect statistics on business trends, and discover and diagnose system problems in a timely manner.


Metrics of the OSS monitoring service are classified into basic service metrics, performance metrics, and billable usage metrics. For more information, see [Metrics](https://www.alibabacloud.com/help/en/oss/user-guide/metrics#concept-ux3-yhk-5db).

## High real-time performance


Real-time monitoring can reveal potential traffic fluctuations during various periods. This facilitates the analysis and evaluation of business scenarios. Real-time monitoring metrics (except for billable usage metrics) allow for minute-level metric data to be collected and aggregated with an output delay of less than a minute. User information that is collected every minute is aggregated into a single value and displayed within one minute to represent the overall monitoring for the minute.

## Billable usage metrics


In line with the billing policies, billable usage metrics are collected and presented based on the following criteria:


-

Billable usage metric data is collected each hour. Resource metering data for each hour is aggregated into a single value that represents the overall monitoring for that hour.

-

Billable usage metric data is displayed with a delay of nearly 30 minutes.

-

The statistics collection time is the start time of the relevant statistical period.

-

The statistics collection deadline is the end time of the last statistical period of the current month. If no metric data is produced in the current month, the statistics collection deadline is 00:00:00 on the first day of the current month.

-

A maximum amount of metric data is pushed for presentation. For precise metric data, go to the Billing Management console and click [Usage Records](https://billingnew.console.alibabacloud.com/#/expense/outline).


For example, you only use PutObject requests to upload data and perform the operation an average of 10 times per minute. Then in the hour from 08:00:00 to 09:00:00 on May 10, 2018, the metric value of the number of PUT requests is 600 (10 × 60 minutes), the statistics collection time is 08:00:00 on May 10, 2018, and the data is displayed at around 09:30:00 on May 10, 2018. If the data is the last metric data from 00:00 on May 01, 2018, the statistics collection deadline for the current month is 09:00:00 on May 10, 2018. If you have not produced any metric data in May 2018, the statistics collection deadline will be 00:00:00 on May 1, 2018.

## OSS alert service


You can use an account to set up to 1,000 alert rules. You can configure alert rules for other monitoring metrics in addition to billable usage metrics and statistical metrics. You can also configure multiple alert rules for a single metric.


-

For more information about the alert service, see [Alert service overview](https://www.alibabacloud.com/help/en/cms/cloudmonitor-1-0/user-guide/overview-2)

-

For more information about how to use the OSS alert service, see [Alert service](https://www.alibabacloud.com/help/en/oss/user-guide/use-the-alert-service#concept-opj-kzj-5db).

-

For more information about the metrics of the OSS monitoring service, see [Metrics](https://www.alibabacloud.com/help/en/oss/user-guide/metrics#concept-ux3-yhk-5db).

## Metric data retention policy


Metric data is retained for 31 days before being automatically cleared upon expiration. To store or perform offline analysis on metric data that is over 31 days old, you can use tools or write code to read the CloudMonitor data storage. For more information, see [Access metric data by using the CloudMonitor API].


The OSS console displays metric data from the last seven days. To query metric data that is older than seven days, we recommend that you use CloudMonitor SDKs. For more information, see [Access metric data by using the CloudMonitor OpenAPI].

## Access metric data by using the CloudMonitor OpenAPI


The CloudMonitor API allows you to access OSS metric data. For more information, see the following topics:



-

[CloudMonitor SDK reference](https://www.alibabacloud.com/help/en/cms/cloudmonitor-1-0/developer-reference/cloudmonitor-sdk-for-java/#concept-llz-kz4-zdb)

-

[Metric item reference](https://www.alibabacloud.com/help/en/oss/user-guide/access-monitoring-data#concept-ij1-rfk-5db)

## Monitoring, diagnosis, and troubleshooting


The [Service monitoring, diagnosis, and troubleshooting](https://www.alibabacloud.com/help/en/oss/user-guide/monitoring-diagnosis-and-troubleshooting#concept-ths-hjk-5db) topic describes how to monitor the running status of OSS and perform diagnosis and troubleshooting. This topic provides an overview of the following aspects:


-

[OSS monitoring](https://www.alibabacloud.com/help/en/oss/user-guide/monitoring-diagnosis-and-troubleshooting#section-k51-nlk-5db)


Describes how to use the OSS monitoring service to monitor the running status and performance of OSS.

-

[Tracking and diagnosis](https://www.alibabacloud.com/help/en/oss/user-guide/monitoring-diagnosis-and-troubleshooting#section-ixw-f4k-5db)


Describes how to use the OSS monitoring service and logging function to diagnose problems as well as how to associate the relevant information in log files for tracking and diagnosis.

-

[Troubleshooting](https://www.alibabacloud.com/help/en/oss/user-guide/monitoring-diagnosis-and-troubleshooting#section-hmn-1pk-5db)


Describes typical problems and methods to troubleshoot the problems.

## Precautions


Bucket names must be globally unique in OSS. If you delete a bucket and then create a bucket with the same name as the deleted bucket, the monitoring and alert rules set for the deleted bucket will be applied to the new bucket.

Thank you! We've received your  feedback.