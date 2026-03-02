# View the resource usage of a bucket

This topic describes how to view the resource usage of a bucket. The resource usage of a bucket in the Object Storage Service (OSS) console is provided only for reference.

## Background information


You can view the following statistics about resource usage of a bucket in the OSS console:


-

Basic Data: includes storage usage, bandwidth usage, traffic usage, the number of requests, the size of processed images, and the number of image processing requests.

-

Ranking Statistics: includes page views (PVs), unique visitors (UVs), and the top 10 Referers or IP addresses that access the bucket. The number of failed requests for the top 10 IP address rankings is calculated based on requests with HTTP status codes 4XX (excluding 499) and 5XX.

-

Region and Operator Statistics: includes visitor distribution by region and Internet service provider (ISP).

-

API Statistics: includes statistics of HTTP methods and status codes.

-

Object Access Statistics: includes the statistics about object access.


> NOTE:

> NOTE: 


> NOTE: Note Ranking Statistics, Region and Operator Statistics, API Statistics, and Object Access Statistics are supported only in the following regions: the Chinese mainland, China (Hong Kong), US (Virginia), US (Silicon Valley), Germany (Frankfurt), and Singapore.


In this topic, Basic Data is used as an example to show how to view resource usage.

## Procedure


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left-side navigation tree, choose Data Usage > Basic Data.


On the Basic Data tab, the following charts are displayed: Buckets, Used Bandwidth, Traffic Usage, Requests, Image Processing Capacity, and Image Processing Requests.


-

Buckets: This chart displays the storage usage of the bucket for a given period of time.








| Basic data | Description |
| --- | --- |
| Standard-Actual Storage Usage | The size of Standard objects in the bucket. |
| Billed storage usage | The billed storage capacity of the bucket. |


-

Used Bandwidth: This chart displays the bandwidth usage for a given period of time.








| Basic data | Description |
| --- | --- |
| VPC Inbound | The bandwidth that is used when data is uploaded to OSS over Alibaba Cloud Virtual Private Cloud (VPC). |
| VPC Outbound | The bandwidth that is used when OSS data is accessed or downloaded over Alibaba Cloud VPC. |
| CDN Origin Inbound | The bandwidth that is used when data is uploaded to OSS by using Alibaba Cloud CDN (CDN). |
| CDN Origin Outbound | The bandwidth that is used when OSS data is accessed or downloaded by using CDN. |
| CRR Inbound | The bandwidth that is used when data is replicated to the bucket by using cross-region replication (CRR) over the Internet. |
| CRR Outbound | The bandwidth that is used when data is replicated from the bucket to another bucket by using CRR over the Internet. |
| Inbound over the Internet | The bandwidth that is used when data is uploaded to the bucket over the Internet. |
| Outbound over the Internet | The bandwidth that is used when data in the bucket is accessed or downloaded over the Internet. |
| Outbound over Internal Networks | The bandwidth that is used when data in the bucket is accessed or downloaded over internal networks. |
| Inbound over Internal Networks | The bandwidth that is used when data is uploaded to the bucket over internal networks. |


-

Traffic Usage: This chart displays the traffic usage of the bucket for a given period of time.








| Basic data | Description |
| --- | --- |
| VPC Inbound | The traffic that is generated when data is uploaded to the bucket over Alibaba Cloud VPC. |
| VPC Outbound | The traffic that is generated when data in the bucket is accessed or downloaded over Alibaba Cloud VPC. |
| CDN Origin Inbound | The traffic that is generated when data is uploaded to the bucket by using CDN. |
| CDN Origin Outbound | The traffic that is generated when data in the bucket is accessed or downloaded by using CDN. |
| CRR Inbound | The traffic that is generated when data is replicated to the bucket by using CRR over the Internet. |
| CRR Outbound | The traffic that is generated when data is replicated from the bucket to another bucket by using CRR over the Internet. |
| Inbound over the Internet | The traffic that is generated when data is uploaded to the bucket over the Internet. |
| Outbound over the Internet | The traffic that is generated when data in the bucket is accessed or downloaded over the Internet. |
| Outbound over Internal Networks | The traffic that is generated when data in the bucket is accessed or downloaded over internal networks. |
| Inbound over Internal Networks | The traffic that is generated when data is uploaded to the bucket over internal networks. |


-

Requests: This chart displays the number of requests to access the bucket per hour:


-

Requests with HTTP 403 status code

-

Requests with HTTP 4xx status codes

-

Requests with HTTP 4xx status codes other than 403, 404, 408, and 499

-

Requests with HTTP 5xx status codes


This curve records the number of requests for which an HTTP 5xx status code (such as 501, 502, or 503) is returned.

-

PUT requests








> NOTE:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees#section-0h5-sdd-8t2)


| Request | Description |
| --- | --- |
| PutBucket | Creates a bucket. |
| ListObjects (GetBucket) and ListObjectsV2 (GetBucketV2) | Lists all objects. Note You are billed for ListObjects (GetBucket) and ListObjectsV2 (GetBucketV2) in the PUT request category. ListObjects (GetBucket) and ListObjectsV2 (GetBucketV2) usage is included in the PUT request usage. For more information, see API operation calling fees. |
| PutBucketACL | Configures an access control list (ACL) for a bucket. |
| PutBucketInventory | Configures inventories for a bucket. |
| DeleteBucketInventory | Deletes inventories that are configured for a bucket. |
| PutBucketLogging | Enables logging for a bucket. |
| DeleteBucketLogging | Disables logging for a bucket. |
| PutBucketWebsite | Enables static website hosting for a bucket and configures redirection rules for the bucket. |
| DeleteBucketWebsite | Disables static website hosting for a bucket and deletes the redirection rules configured for the bucket. |
| PutBucketReferer | Configures the Referer whitelist and specifies whether requests with empty Referer fields are allowed. |
| PutBucketLifecycle | Configures lifecycle rules for a bucket. |
| CommitTransition | Converts the storage class of objects to IA, Archive, Cold Archive, or Deep Cold Archive based on lifecycle rules. |
| ExpireObject | Deletes an object based on lifecycle rules. |
| DeleteBucketLifecycle | Deletes lifecycle rules that are configured for a bucket. |
| DeleteBucket | Deletes a bucket. |
| PutObject | Uploads an object. |
| CopyObject | Copies objects to the same bucket or to another bucket within the same region. |
| AppendObject | Uploads an object by appending the content of the object to an existing object. |
| DeleteObject | Deletes a single object. |
| DeleteMultipleObjects | Deletes multiple objects. |
| PutObjectACL | Configures an ACL for an object. |
| PostObject | Uploads an object by using an HTML form. |
| PutSymlink | Creates a symbolic link. |
| RestoreObject | Restores Archive, Cold Archive, or Deep Cold Archive objects. |
| InitiateMultipartUpload | Initiates a multipart upload task. |
| UploadPart | Uploads an object by part based on the specified object name and the upload ID. |
| AbortMultipartUpload | Cancels a multipart upload task and deletes uploaded parts. |
| UploadPartCopy | Copies an object by part. |
| PutBucketReplication | Configures data replication rules for a bucket. |
| DeleteBucketReplication | Stops a data replication task for a bucket and deletes the data replication rules configured for the bucket. |
| PutBucketCors | Configures cross-origin resource sharing (CORS) for a bucket. |
| DeleteBucketCors | Deletes CORS configurations of a bucket. |
| CompleteMultipartUpload | Completes a multipart upload task. |
| InitiateBucketWorm | Creates a retention policy for a bucket. |
| AbortBucketWorm | Deletes an unlocked retention policy. |
| CompleteBucketWorm | Locks a retention policy. |
| ExtendBucketWorm | Extends the retention period (days) of objects in a bucket for which a retention policy is locked. |
| PutBucketVersioning | Enables versioning for a bucket. |
| PutBucketPolicy | Configures a bucket policy. |
| DeleteBucketPolicy | Deletes a bucket policy. |
| PutBucketTags | Adds tags to or modifies the tags of a bucket. |
| DeleteBucketTags | Deletes tags of a bucket. |
| PutBucketEncryption | Configures a data encryption rule for a bucket. |
| DeleteBucketEncryption | Deletes a data encryption rule configured for a bucket. |
| PutBucketRequestPayment | Configures request payment settings for a bucket. |
| PutObjectTagging | Adds tags to or modifies tags of an object. |
| DeleteObjectTagging | Deletes tags of an object. |
| PutLiveChannel | Creates a LiveChannel. |
| DeleteLiveChannel | Deletes a LiveChannel. |
| PutLiveChannelStatus | Changes the status of a LiveChannel. |
| PostVodPlaylist | Generates a playlist that is used for video on demand (VOD) for a LiveChannel. |


-

GET requests








| Request | Description |
| --- | --- |
| GetBucketAcl | Queries the ACL of a bucket. |
| GetBucketLocation | Queries the data center in which a bucket is located. |
| GetBucketInfo | Queries information about a bucket. |
| GetBucketLogging | Queries the logging configurations of a bucket. |
| GetBucketWebsite | Queries the static website hosting configurations of a bucket. |
| GetBucketReferer | Queries the Referer configurations of a bucket. |
| GetBucketLifecycle | Queries the lifecycle rules that are configured for a bucket. |
| GetBucketReplication | Queries the data replication rules that are configured for a bucket. |
| GetBucketReplicationLocation | Queries the regions of the destination bucket to which data can be replicated. |
| GetBucketReplicationProgress | Queries the data replication progress. |
| GetBucketInventory | Queries an inventory of a bucket. |
| ListBucketInventory | Queries all inventories that are configured for a bucket. |
| GetObject | Downloads an object. |
| HeadObject | Queries all metadata of an object. |
| GetObjectMeta | Queries some metadata information of an object. |
| GetObjectACL | Queries the ACL of an object. |
| GetSymlink | Queries symbolic links. |
| ListMultipartUploads | Lists all ongoing multipart upload tasks. |
| ListParts | Lists the uploaded parts. |
| UploadPartCopy | Copies an object by part. |
| GetBucketCors | Queries the CORS rules that are configured for a bucket. |
| GetBucketWorm | Queries the retention policies that are configured for a bucket. |
| GetBucketVersioning | Queries the versioning status of a bucket. |
| ListObjectVersions (GetBucketVersions) | Queries the versions of all objects in a bucket. |
| GetBucketPolicy | Queries the bucket policies that are configured for a bucket. |
| GetBucketReferer | Queries Referer configurations of a bucket. |
| GetBucketTags | Queries the tags of a bucket. |
| GetBucketEncryption | Queries the encryption configurations of a bucket. |
| GetBucketRequestPayment | Queries the pay-by-requester configurations of a bucket. |
| SelectObject | Scans an object. |
| GetObjectTagging | Queries the tags of an object. |
| ListLiveChannel | Queries the list of LiveChannels. |
| GetLiveChannelInfo | Queries the configurations of a specific LiveChannel. |
| GetLiveChannelStat | Queries the stream ingest status of a specific LiveChannel. |
| GetLiveChannelHistory | Queries the stream ingest history of a specific LiveChannel. |
| GetVodPlaylist | Queries the playlist that is generated by the streams ingested to a specific LiveChannel within a specific time range. |


-

Image Processing Capacity: the size of image data that is processed in the bucket.

-

Image Processing Requests: the number of image processing requests sent to the bucket.

-

Specify a time range at the top of the charts.

-

View the data in the charts. In the following example, the Requests chart is used to show how to view the basic data items in a chart.


By default, the Requests chart displays requests with HTTP 5xx status codes, HTTP 4xx status codes, PUT requests, and GET requests. You can click a data item to hide the curve of the item in the chart. The names of hidden data items are displayed in gray. For example, if you click Requests with HTTP Status Code 5XX to hide the curve for this type of requests, only the Requests with HTTP Status Code 4XX, PUT Requests, and GET Requests curves are displayed in the chart.


Thank you! We've received your  feedback.