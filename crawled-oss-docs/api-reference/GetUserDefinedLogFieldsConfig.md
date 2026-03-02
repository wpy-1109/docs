# GetUserDefinedLogFieldsConfig

Queries custom fields in the user_defined_log_fields element for bucket logging.

Notes

The permission of oss:GetUserDefinedLogFieldsConfig is required to get the custom settings of user_defined_log_fields in the real-time logs of the bucket by calling GetUserDefinedLogFieldsConfig operation. For more information, see Attach a custom policy to a RAM user.

Request syntax
 
GET /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a GetUserDefinedLogFieldsConfig request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a GetUserDefinedLogFieldsConfig request are common response headers. For more information, see Common response headers.

Response elements

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

Parent element: HeaderSet




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

Examples

Sample request

 
GET /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue

Sample response

 
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

OSS SDKs

You can use OSS SDKs for the following programming languages to call GetUserDefinedLogFieldsConfig operation:

Java

Python V2

PHP V2

Go V2

C

.NET

Node.js

Ruby