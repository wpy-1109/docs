# Call GetBucketAccessMonitor to query the access tracking status of a bucket

Queries the access tracking status of a bucket. You must first enable access tracking for a bucket if you want to configure a lifecycle rule based on last access time to, for example, monitor access patterns and move cold data to a more cost-effective storage class.

## Note


To query the access tracking status of a bucket, you must have the `oss:GetBucketAccessMonitor` permission. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`http
GET /?accessmonitor HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| AccessMonitorConfiguration | Container | N/A | The access tracking configurations of the bucket. Child nodes: Status |
| Status | String | Enabled | The access tracking status of the bucket. Valid values:Enabled: Access tracking is enabled.Disabled: Access tracking is disabled.Parent nodes: AccessMonitorConfiguration |


## Example


Sample request


`http
GET /?accessmonitor HTTP/1.1
Host: oss-example.oss.aliyuncs.com
Date: Thu, 17 Apr 2025 13:08:38 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`http
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D
Date: Mon, 26 Jul 2021 13:08:38 GMT
Content-Length: 125
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<AccessMonitorConfiguration>
  <Status>Enabled</Status>
</AccessMonitorConfiguration>
`


## References


-

For more information about lifecycle rules based on last access time, see [Lifecycle rules based on last access time](https://www.alibabacloud.com/help/en/oss/user-guide/lifecycle-rules-based-on-the-last-access-time).

-

After access tracking is enabled, you can call the PutBucketLifecycle operation to configure a lifecycle rule based on last access time. For more information, see [PutBucketLifecycle](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlifecycle).

## OSS SDKs


You can use OSS SDKs for the following programming languages to call GetBucketAccessMonitor:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/access-tracking-2)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/access-monitor-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-access-tracking)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-access-tracking)

## ossutil


For information about the ossutil command that corresponds to the GetBucketAccessMonitor operation, see [get-bucket-access-monitor](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-access-monitor).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | You are not authorized to access the bucket. |
| NoSuchBucket | 404 | The bucket does not exist. |


Thank you! We've received your  feedback.