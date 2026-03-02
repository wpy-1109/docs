# GetBucketRequestPayment

You can call this operation to obtain pay-by-requester configurations for a bucket.

## Request syntax


`plaintext
GET /? requestPayment HTTP/1.1
Date: GMT Date
Host: BucketName.oss.aliyuncs.com
Authorization: authorization string
`


## Response elements











| Element | Type | Description |
| --- | --- | --- |
| RequestPaymentConfiguration | Container | Indicates the container for the payer. Child: Payer |
| Payer | String | Indicates who pays the download and request fees. Valid values: BucketOwner and RequesterParent: RequestPaymentConfiguration |


## Examples


Request sample



`plaintext
GET /? requestPayment
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 23 Jul 2019 01:23:20 GMT
Authorization: OSS qn6q:77Dv
`


Response sample



`plaintext
200 (OK)
content-length: 129
server: AliyunOSS
x-oss-request-id: 5D366188B007B79097EC
date: Tue, 23 Jul 2019 01:23:20 GMT
content-type: application/xml
<? xml version="1.0" encoding="UTF-8"? >
<RequestPaymentConfiguration>
  <Payer>BucketOwner</Payer>
</RequestPaymentConfiguration>
`


## OSS SDK


You can use OSS SDKs for the following programming languages to call GetBucketRequestPayment:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/pay-by-requester-4#concept-943914)

-

[Python](https://www.alibabacloud.com/help/en/oss/developer-reference/pay-by-requester-1#concept-944152)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-pay-by-requester)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/pay-by-requester-5)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/pay-by-requester-2#concept-944152)

-

[PHP](https://www.alibabacloud.com/help/en/oss/developer-reference/pay-by-requester-5)

-

[.Net](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-pay-by-requester-via-oss-sdk-for-csharp)

## ossutil


For information about the ossutil command that corresponds to the GetBucketRequestPayment operation, see [get-bucket-request-payment](https://www.alibabacloud.com/help/en/oss/developer-reference/get-bucket-request-payment).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchBucket | 404 | The error message returned because the specified bucket does not exist. |


Thank you! We've received your  feedback.