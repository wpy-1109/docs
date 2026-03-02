# How do I troubleshoot signature errors?

This topic describes how to troubleshoot Object Storage Service (OSS) signature errors.

## Error message


`
<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>SignatureDoesNotMatch</Code>
  <Message>The request signature we calculated does not match the signature you provided. Check your key and signing method.</Message>
  <RequestId>646DCB189AE2D1333018</RequestId>
  <HostId>bucket.oss-cn-hangzhou.aliyuncs.com</HostId>
  <OSSAccessKeyId>LTAI</OSSAccessKeyId>
  <SignatureProvided>tPN3LTAI </SignatureProvided>
  <StringToSign>PUT\n\n\nTue, 23 May 2023 15:24:55 GMT\n/bucket/?acl</StringToSign>
  <StringToSignBytes>50 55 54 0A 0A 0A 54 75 65 2C 20 32 33 20 4D 61 79 20 32 30 32 33 20 31 35 3A 32 34 3A 35 35 20 47 4D 54 0A 2F 64 69 6E 61 72 79 2F 3F 61 63 6C </StringToSignBytes>
  <EC>0002-00000040</EC>
</Error>
`


When you call an API operation or use an OSS SDK to access OSS, the client must include a signature for the OSS server to perform identity authentication. If the server returns the preceding error message, the signature that you provided in the request is inconsistent with the signature calculated by the server. As a result, the request is rejected.

## Troubleshooting


If a signature error occurs in your request, perform the following steps to troubleshoot the error:


-

Check whether the AccessKey ID and AccessKey secret are valid.


You can use the AccessKey ID and AccessKey secret to log on to ossbrowser to check whether the AccessKey ID and AccessKey secret are valid. For more information, see [Install and log on to ossbrowser](https://www.alibabacloud.com/help/en/oss/developer-reference/install-ossbrowser-1-0).

-

Check whether the signature algorithm is valid.


OSS provides two request methods that can include signatures. For more information, see [Include signatures in the Authorization header](https://www.alibabacloud.com/help/en/oss/developer-reference/include-signatures-in-the-authorization-header) and [Add signatures to URLs](https://www.alibabacloud.com/help/en/oss/developer-reference/ddd-signatures-to-urls). The following items describe the algorithms for the two signature methods:


-

Include signatures in the Authorization header


`plaintext
StringToSign = VERB + "\n"
              + Content-MD5 + "\n"
              + Content-Type + "\n"
              + Date + "\n"
              + CanonicalizedOSSHeaders
              + CanonicalizedResource
Signature = base64(hmac-sha1(AccessKeySecret, StringToSign)
`


-

Add signatures to URLs


`plaintext
StringToSign = VERB + "\n"
              + CONTENT-MD5 + "\n"
              + CONTENT-TYPE + "\n"
              + EXPIRES + "\n"
              + CanonicalizedOSSHeaders
              + CanonicalizedResource
Signature = urlencode(base64(hmac-sha1(AccessKeySecret, StringToSign)))
`


We recommend that you use OSS SDKs to access OSS. This eliminates the need to manually calculate the signature. For more information, see [Use Alibaba Cloud SDKs to initiate requests](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-63/).

-

Check whether the value of the `StringToSign` field in the response body is consistent with that in the request.


The `StringToSign` field specifies the string to be signed, which is the content that needs to be encrypted by using the AccessKey secret in the signature algorithm.


Examples:


`plaintext
PUT /bucket/abc?acl
Date: Wed, 24 May 2023 02:12:30 GMT
Authorization: OSS qn6q:77Dv
x-oss-abc: mymeta
`


The string to be signed calculated by using the preceding method:


`plaintext
PUT\n\n\nWed, 24 May 2023 02:12:30 GMT\nx-oss-abc:mymeta\n/bucket/abc?acl
`


Thank you! We've received your  feedback.