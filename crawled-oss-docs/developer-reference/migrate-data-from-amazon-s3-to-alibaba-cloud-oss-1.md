# Migrate data from Amazon S3 to Alibaba Cloud OSS

Alibaba Cloud Object Storage Service (OSS) is compatible with the Amazon Simple Storage Service (Amazon S3) API operations to allow you to seamlessly migrate data from S3 to OSS.

## Usage notes


-

Limits


OSS is compatible with the S3 protocol. You can use S3 SDKs or S3-compatible tools to create Buckets and upload Objects. During these operations, limits on bandwidth, queries per second (QPS), and other factors are subject to OSS performance metrics. For more information, see [Limits](https://www.alibabacloud.com/help/en/oss/user-guide/limits#concept-pzk-crg-tdb).

-

Client configurations


After migrating from Amazon S3 to OSS, you can continue to use the S3 API to access OSS. You only need to make the following changes to your S3 client:


-

Configure your client or SDK with the AccessKey ID and AccessKey secret from your Alibaba Cloud account or RAM user.

-

Set the connection endpoint in your client to the appropriate OSS endpoint. For a list of OSS endpoints, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db).

## Migration tutorial


Use [Data Online Migration](https://mgw.console.alibabacloud.com/job?_k=r90z7u#/job?_k=xdgp8r) to migrate data from Amazon S3 to OSS. For more information, see [Migrate data from AWS S3 to Alibaba Cloud OSS](https://www.alibabacloud.com/help/en/data-online-migration/user-guide/tutorial-for-data-migration-from-aws-s3-to-oss/).

Thank you! We've received your  feedback.