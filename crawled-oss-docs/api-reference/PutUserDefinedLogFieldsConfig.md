# PutUserDefinedLogFieldsConfig

Customizes fields in the user_defined_log_fields element for bucket logging to log request headers and query parameters.

Usage notes

The oss:PutUserDefinedLogFieldsConfig permission is required to customize the user_defined_log_fields field in real-time logs by calling the PutUserDefinedLogFieldsConfig operation. For more information, see Attach a custom policy to a RAM user.

Your logging configuration information is encoded and populated in the user_defined_log_fields field. The value of the user_defined_log_fields field is Base64-encoded JSON data. The JSON data includes the "truncated" field that indicates whether the JSON data was truncated, the "headers" field that contains the specified request headers, and the "querys" field that contains the specified query parameters.

You can specify a total of six custom request headers and query parameters in a logging configuration.

The total key and value length of all custom fields for request headers and query parameters in a logging configuration is limited to 1024 bytes. Trailing characters beyond the length limit are truncated.

Custom field keys for request headers can contain hyphens (-) but cannot contain underscores (_). Custom field keys for query parameters can contain underscores (_).

Custom field keys for request headers must comply with the HTTP protocol and can contain only ASCII printable characters (from 33 to 126) except for underscores (_) and colons (:).

Request syntax
 
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
Request headers

All headers in a PutUserDefinedLogFieldsConfig request are common request headers. For more information, see Common request headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




UserDefinedLogFieldsConfiguration

	

Container

	

Yes

	

N/A

	

The container for the user-defined logging configuration.

Child elements: HeaderSet and ParamSet

Parent elements: none




HeaderSet

	

Container

	

No

	

N/A

	

The container for custom request headers.

Child elements: header

Parent elements: UserDefinedLogFieldsConfiguration




header

	

String

	

No

	

header1

	

The custom request header.

Child elements: none

Parent elements: HeaderSet




ParamSet

	

Container

	

No

	

N/A

	

The container for custom query parameters.

Child elements: parameter

Parent elements: UserDefinedLogFieldsConfiguration




parameter

	

String

	

No

	

param1

	

The custom query parameter.

Child elements: none

Parent elements: ParamSet

Response headers

All headers in the response to a PutUserDefinedLogFieldsConfig request are common response headers. For more information, see Common response headers.

Examples

Sample request

 
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

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674125A4D8906008B
Date: Date
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call PutUserDefinedLogFieldsConfig operation:

Java

Python V2

PHP V2

Go V2

C

.NET

Node.js

Ruby