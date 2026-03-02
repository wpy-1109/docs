# Overview of OSS error codes

When an Object Storage Service (OSS) request fails, OSS returns an HTTP status code, a fine-grained error code (EC), and an XML body with diagnostic details. Use this information to identify the root cause and resolve the issue.

## Diagnose an error

### Step 1: Read the error response


Every error response contains fields that help you pinpoint the issue. Start with the `Message` field for a human-readable description, then check the remaining fields:


`xml
HTTP/1.1 400 Bad Request
Server: AliyunOSS
Date: Thu, 11 Aug 2019 01:44:54 GMT
Content-Type: application/xml
Content-Length: 322
Connection: keep-alive
x-oss-request-id: 57ABD896CCB80C366955
x-oss-server-time: 0
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>MissingArgument</Code>
  <Message>Missing Some Required Arguments.</Message>
  <RequestId>57ABD896CCB80C366955</RequestId>
  <HostId>oss-example.oss-cn-hangzhou.aliyuncs.com</HostId>
  <EC>0016-00000502</EC>
  <RecommendDoc>https://api.aliyun.com/troubleshoot?q=0016-00000502</RecommendDoc>
</Error>
`



| Field | Description |
| --- | --- |
| RecommendDoc | A direct link to the troubleshooting guide for this error in OpenAPI Explorer. Start here. |
| EC | A fine-grained error code that identifies the exact cause. More precise than the general Code field. |
| HTTP status code (e.g., 400 Bad Request) | The broad error category: 4xx indicates a client-side issue, 5xx indicates a server-side issue. |
| RequestId | The unique identifier for this request. Always provide this value when you contact technical support. |


### Step 2: Find a solution


-

Follow the `RecommendDoc` link. The link opens an interactive troubleshooting guide in OpenAPI Explorer tailored to the error.

-

Look up the `EC` in the error code list. If the response does not contain a `RecommendDoc` link, search for the `EC` value in the [error code reference](https://www.alibabacloud.com/help/en/oss/user-guide/error-codes/).


If neither approach resolves the issue, contact technical support with the full `RequestId`. For instructions on retrieving the request ID from different clients, see [Obtain request IDs](https://www.alibabacloud.com/help/en/oss/user-guide/obtain-request-ids).

## Error response structure


An error response consists of HTTP headers and an XML body. Both carry diagnostic information.

### Response headers


| Header | Description |
| --- | --- |
| x-oss-ec | The fine-grained error code. Each error condition maps to a unique EC, making it more precise than the Code element in the body for identifying the root cause. |
| x-oss-request-id | The unique identifier of the request. Provide this value when you contact technical support. |


> IMPORTANT:

> NOTE: 


> NOTE: Important 

The `x-oss-ec` header is for diagnostic purposes only. Its value may change without notice, and backward compatibility is not guaranteed. Do not write application logic that depends on specific EC values.


Example:


`http
HTTP/1.1 403 Forbidden
Server: AliyunOSS
Date: Wed, 09 Nov 2022 08:45:46 GMT
Content-Type: application/xml
Content-Length: 471
Connection: keep-alive
x-oss-request-id: 636B68BA80DA8539399F
x-oss-server-time: 0
x-oss-ec: 0003-00000001
`


For the full list of headers, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers).

### Response body


The XML body contains the following elements:


| Element | Description |
| --- | --- |
| Code | A general-purpose error code string defined by OSS. Use this value to detect and handle errors programmatically by type. |
| Message | A detailed description of the error. |
| RequestId | The unique identifier of the request. Provide this value when you contact technical support. |
| HostId | The OSS cluster that handled the request. This value corresponds to the host specified in the request. |
| EC | The fine-grained error code, identical to the x-oss-ec response header. |
| RecommendDoc | A link to an interactive troubleshooting guide in OpenAPI Explorer for this error. |


Example:


`xml
<?xml version="1.0" ?>
<Error xmlns="http://doc.oss-cn-hangzhou.aliyuncs.com">
  <Code>MalformedXML</Code>
  <Message>The XML you provided was not well-formed or did not validate against our published schema.</Message>
  <RequestId>57ABD896CCB80C366955</RequestId>
  <HostId>oss-cn-hangzhou.aliyuncs.com</HostId>
  <EC>0031-00000001</EC>
  <RecommendDoc>https://api.aliyun.com/troubleshoot?q=0031-00000001</RecommendDoc>
</Error>
`


## Handle errors in your application


Follow these practices to handle OSS errors in your application:


-

Use the error code, not the HTTP status code, for branching logic. Multiple distinct errors can map to the same HTTP status code. For example, both missing-bucket and missing-object errors return `404 Not Found`. The `Code` element provides the granularity needed to distinguish between them.

-

Retry on `InternalError`. An `InternalError` indicates the service is busy or an internal error occurred. Wait for a while and send the request again. If the issue persists, submit a ticket for technical support.

-

Back off on rate-limiting errors. If requests return HTTP `429` (such as `QpsLimitExceeded`) or HTTP `503` errors (such as `TotalQpsLimitExceeded` or `DownloadTrafficRateLimitExceeded`), reduce the request rate.

-

Always log the `RequestId`. Capture the `RequestId` (or `x-oss-request-id` header) in your application logs. This value is required for troubleshooting with technical support.

## References


-

[Obtain request IDs](https://www.alibabacloud.com/help/en/oss/user-guide/obtain-request-ids)

-

[Error codes](https://www.alibabacloud.com/help/en/oss/user-guide/error-codes/)

-

[HTTP status code](https://www.alibabacloud.com/help/en/oss/user-guide/http-status-code/)

Thank you! We've received your  feedback.