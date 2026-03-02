# GetBucketRequestPayment

You can call this operation to obtain pay-by-requester configurations for a bucket.

Request syntax
 
GET /? requestPayment HTTP/1.1
Date: GMT Date
Host: BucketName.oss.aliyuncs.com
Authorization: authorization string
Response elements

Element

	

Type

	

Description




RequestPaymentConfiguration

	

Container

	

Indicates the container for the payer.

Child: Payer




Payer

	

String

	

Indicates who pays the download and request fees.

Valid values: BucketOwner and Requester

Parent: RequestPaymentConfiguration

Examples

Request sample

 
GET /? requestPayment
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 23 Jul 2019 01:23:20 GMT
Authorization: OSS qn6q**************:77Dv****************

Response sample

 
200 (OK)
content-length: 129
server: AliyunOSS
x-oss-request-id: 5D366188B007B79097EC****
date: Tue, 23 Jul 2019 01:23:20 GMT
content-type: application/xml
<? xml version="1.0" encoding="UTF-8"? >
<RequestPaymentConfiguration>
  <Payer>BucketOwner</Payer>
</RequestPaymentConfiguration>
OSS SDK

You can use OSS SDKs for the following programming languages to call GetBucketRequestPayment:

Java

Python

Go V2

Node.js

C++

PHP

.Net

ossutil

For information about the ossutil command that corresponds to the GetBucketRequestPayment operation, see get-bucket-request-payment.

Error codes

Error code

	

HTTP status code

	

Description




NoSuchBucket

	

404

	

The error message returned because the specified bucket does not exist.