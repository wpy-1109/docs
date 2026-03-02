# Call the PutUserDefinedLogFieldsConfig operation to customize log fields

Customizes fields in the `user_defined_log_fields` element for bucket logging to log request headers and query parameters.

## Usage notes


-

The `oss:PutUserDefinedLogFieldsConfig` permission is required to customize the `user_defined_log_fields` field in real-time logs by calling the PutUserDefinedLogFieldsConfig operation. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Your logging configuration information is encoded and populated in the `user_defined_log_fields` field. The value of the `user_defined_log_fields` field is Base64-encoded JSON data. The JSON data includes the "truncated" field that indicates whether the JSON data was truncated, the "headers" field that contains the specified request headers, and the "querys" field that contains the specified query parameters.

-

You can specify a total of six custom request headers and query parameters in a logging configuration.

-

The total key and value length of all custom fields for request headers and query parameters in a logging configuration is limited to 1024 bytes. Trailing characters beyond the length limit are truncated.

-

Custom field keys for request headers can contain hyphens (-) but cannot contain underscores (_). Custom field keys for query parameters can contain underscores (_).

-

Custom field keys for request headers must comply with the HTTP protocol and can contain only ASCII printable characters (from 33 to 126) except for underscores (_) and colons (:).

## Request syntax


`plaintext
PUT /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
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


## Request headers


All headers in a PutUserDefinedLogFieldsConfig request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| UserDefinedLogFieldsConfiguration | Container | Yes | N/A | The container for the user-defined logging configuration. Child elements: HeaderSet and ParamSetParent elements: none |
| HeaderSet | Container | No | N/A | The container for custom request headers. Child elements: headerParent elements: UserDefinedLogFieldsConfiguration |
| header | String | No | header1 | The custom request header. Child elements: noneParent elements: HeaderSet |
| ParamSet | Container | No | N/A | The container for custom query parameters. Child elements: parameterParent elements: UserDefinedLogFieldsConfiguration |
| parameter | String | No | param1 | The custom query parameter. Child elements: noneParent elements: ParamSet |


## Response headers


All headers in the response to a PutUserDefinedLogFieldsConfig request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Sample request


`http
PUT /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue

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


Sample response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 534B371674125A4D8906008B
Date: Date
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call PutUserDefinedLogFieldsConfig operation:


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