# Transport Layer Security

You can call the GetBucketHttpsConfig operation to query the TLS version and cipher suite configurations of a bucket.

Usage notes

To query the TLS version and cipher suite configurations of a bucket, you must have the oss:GetBucketHttpsConfig permission. For more information, see Grant custom permissions to a RAM user.

Each region has its endpoints that you can use to access OSS in the region. For more information about the mappings between regions and endpoints, see Endpoints and data centers.

Request syntax
 
GET /?httpsConfig HTTP/1.1
Host: BucketName.oss.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Request headers

All headers in a GetBucketHttpsConfig request are common request headers. For more information, see Common Request Headers.

Response headers

All headers in the response to a GetBucketHttpsConfig request are common response headers. For more information, see Common Response Headers.

Response elements

Name

	

Type

	

Example

	

Description




HttpsConfiguration

	

The container

	

None

	

The container that stores HTTPS configurations.




TLS

	

The container

	

None

	

The container that stores TLS version configurations.




Enable

	

Boolean

	

true

	

Indicates whether TLS version control is enabled for the bucket.

true

false




TLSVersion

	

string

	

TLSv1.2

	

The TLS version number. For more information about the scenarios and descriptions of TLS versions, see TLS version guide.




CipherSuite

	

The container

	

None

	

The container that stores cipher suites.




Enable

	

Boolean

	

true

	

Configures TLS cipher suites.

true: strong cipher suites or custom cipher suites.

false: all cipher suites (default).




StrongCipherSuite

	

Boolean

	

true

	

Indicates whether strong cipher suites are used.

true: Strong cipher suites are used.

false: Custom cipher suites are used.




CustomCipherSuite

	

string

	

ECDHE-ECDSA-AES128-SHA256

	

The custom cipher suite for TLS 1.2.




TLS13CustomCipherSuite

	

string

	

ECDHE-ECDSA-AES256-CCM8

	

The custom cipher suite for TLS 1.3.

Examples

Sample requests

 
GET /?httpsConfig HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com 
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Sample command output:

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Sat, 8 May 2021 07:51:28 GMT
Connection: keep-alive
Content-Length: 154
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<HttpsConfiguration>
  <TLS>
    <Enable>true</Enable>
    <TLSVersion>TLSv1.2</TLSVersion>
    <TLSVersion>TLSv1.3</TLSVersion>
  </TLS>
  <CipherSuite>
    <Enable>true/false</Enable>
    <StrongCipherSuite>true/false</StrongCipherSuite>
    <CustomCipherSuite>ECDHE-ECDSA-AES128-SHA256</CustomCipherSuite>
    <CustomCipherSuite>ECDHE-RSA-AES128-GCM-SHA256</CustomCipherSuite>
    <CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
  </CipherSuite>
</HttpsConfiguration>
Command-line tool ossutil

For more information about the ossutil command that corresponds to the GetBucketHttpsConfig operation, see get-bucket-https-config.