# Call GetBucketPolicyStatus to check whether the current bucket policy allows public access

Checks whether the current bucket policy allows public access.

## Note


By default, an Alibaba Cloud account has the permissions to check whether the current bucket policy allows public access. If you want to check whether the current bucket policy allows public access by using a RAM user or the access credentials provided by Security Token Service (STS), you must have the `oss:GetBucketPolicyStatus` permission.

## Request syntax


`http
GET /?policyStatus HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a GetBucketPolicyStatus request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers


The response to a GetBucketPolicyStatus request contains only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| PolicyStatus | Container | N/A | The container that stores public access information. Parent nodes: noneChild nodes: IsPublic |
| IsPublic | Boolean | true | Indicates whether the current bucket policy allows public access. true false |


## Example


-

Sample request


`http
GET /?policyStatus HTTP/1.1
Date: Mon, 19 Feb 2024 08:40:17 GMT
Content-Length: 0
Content-Type: application/xml
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Authorization:  OSS qn6q:77Dv
`


-

Sample success response


`http
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Mon, 19 Feb 2024 08:40:17 GMT
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<PolicyStatus>
   <IsPublic>true</IsPublic>
</PolicyStatus>
`


## OSS SDKs


You can use OSS SDKs for the following programming languages to call the GetBucketPolicyStatus operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-and-manage-bucket-policies)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-using-oss-sdk-for-python-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-bucket-policies)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-policies)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/php-v2-configure-and-manage-bucket-policies)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-1)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policies-2)

## ossutil


For information about the ossutil command that corresponds to the GetBucketPolicyStatus operation, see [get-bucket-policy-status](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-policy-status).

Thank you! We've received your  feedback.