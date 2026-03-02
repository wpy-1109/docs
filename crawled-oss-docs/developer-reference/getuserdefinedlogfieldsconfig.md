# Call the GetUserDefinedLogFieldsConfig operation to query custom logging fields

Queries custom fields in the `user_defined_log_fields` element for bucket logging.

## Notes


The permission of `oss:GetUserDefinedLogFieldsConfig` is required to get the custom settings of `user_defined_log_fields` in the real-time logs of the bucket by calling GetUserDefinedLogFieldsConfig operation. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
GET /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a GetUserDefinedLogFieldsConfig request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


All headers in the response to a GetUserDefinedLogFieldsConfig request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| UserDefinedLogFieldsConfiguration | Container | Yes | N/A | The container for the user-defined logging configuration. Child elements: HeaderSet and ParamSetParent elements: none |
| HeaderSet | Container | No | N/A | The container for custom request headers. Child elements: headerParent elements: UserDefinedLogFieldsConfiguration |
| header | String | No | header1 | The custom request header. Child elements: noneParent element: HeaderSet |
| ParamSet | Container | No | N/A | The container for custom query parameters. Child elements: parameterParent elements: UserDefinedLogFieldsConfiguration |
| parameter | String | No | param1 | The custom query parameter. Child elements: noneParent elements: ParamSet |


## Examples


Sample request


`plaintext
GET /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
`


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674125A4D8906008B
Date: Date
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<UserDefinedLogFieldsConfiguration>
	<HeaderSet>
		<header>header1</header>
		<header>header2</header>
		<header>header3</header>
	</HeaderSet>
	<ParamSet>
		<parameter>param1</parameter>
		<parameter>param2</parameter>
	</ParamSet>
</UserDefinedLogFieldsConfiguration>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call GetUserDefinedLogFieldsConfig operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-1#undefined)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-logging-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-logging-2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-logging-5)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-12#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-2#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-8#undefined)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/logging-6#undefined)

Thank you! We've received your  feedback.