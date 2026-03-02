# DeleteStyle

Deletes a specific image style configured for a bucket.

Usage notes

By default, an Alibaba Cloud account has the permissions to delete a specific image style configured for a bucket. If you want to delete an image style as a RAM user or by using Security Token Service (STS), you must grant the RAM user the oss:DeleteStyle permission. For more information, see Common examples of RAM policies.

Request syntax
Note

When you delete a specified image style configured for a bucket, you must use the style parameter to specify the bucket name and use the styleName parameter to specify the image style name. Sample code: DELETE /?style=oss-example&styleName=imagestyle HTTP/1.1.

 
DELETE /?style=BucketName&styleName=styleName HTTP/1.1
Date:  GMT Date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a DeleteStyle request are common request headers. For more information, see Common HTTP headers.

Response headers

All headers in the response to a DeleteStyle request are common response headers. For more information about common response headers, see Common HTTP headers.

Examples

Sample requests

 
DELETE /?style=oss-example&styleName=imagestyle HTTP/1.1
Date: Thu, 17 Apr 2025 05:38:38 GMT
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample success responses

 
HTTP/1.1 204
Server: AliyunOSS
Date: Fri, 04 Mar 2022 05:38:38 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 6221A5DE5BEABE363779****
OSS SDK

You can use OSS SDK for Python to call the DeleteStyle operation.

ossutil

For information about the ossutil command that corresponds to the DeleteStyle operation, see delete-style.