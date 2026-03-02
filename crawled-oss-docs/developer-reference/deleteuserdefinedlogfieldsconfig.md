# Call the DeleteUserDefinedLogFieldsConfig operation to delete custom field configurations

Deletes custom field settings from the `user_defined_log_fields` element.

## Notes


The permission of `oss:DeleteUserDefinedLogFieldsConfig` is required to delete the custom settings of `user_defined_log_fields` in the real-time logs of the bucket by calling DeleteUserDefinedLogFieldsConfig operation. For more information, see [Attach a custom policy to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

## Request syntax


`plaintext
DELETE /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
`


### Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

### Response headers


All headers in the response to a DescribeRegions request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


Sample request


`plaintext
DELETE /?userDefinedLogFieldsConfig HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss.aliyuncs.com
Authorization: SignatureValue
`


Sample response


`plaintext
HTTP/1.1 204 OK
x-oss-request-id: 534B371674125A4D8906008B
Date: Date
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call DeleteUserDefinedLogFieldsConfig operation:


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

## ossutil


For information about the ossutil command that corresponds to the DeleteUserDefinedLogFieldsConfig operation, see [delete-user-defined-log-fields-config](https://www.alibabacloud.com/help/en/oss/developer-reference/delete-user-defined-log-fields-config).

Thank you! We've received your  feedback.