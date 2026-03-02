# DeleteUserDefinedLogFieldsConfig

Deletes custom field settings from the user_defined_log_fields element.

Notes

The permission of oss:DeleteUserDefinedLogFieldsConfig is required to delete the custom settings of user_defined_log_fields in the real-time logs of the bucket by calling DeleteUserDefinedLogFieldsConfig operation. For more information, see Attach a custom policy to a RAM user.

Request syntax
 
DELETE /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Examples

Sample request

 
DELETE /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue

Sample response

 
HTTP/1.1 204 OK
x-oss-request-id: 534B371674125A4D8906008B
Date: Date
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS

OSS SDKs

You can use OSS SDKs for the following programming languages to call DeleteUserDefinedLogFieldsConfig operation:

Java

Python V2

PHP V2

Go V2

C

.NET

Node.js

Ruby

ossutil

For information about the ossutil command that corresponds to the DeleteUserDefinedLogFieldsConfig operation, see delete-user-defined-log-fields-config.