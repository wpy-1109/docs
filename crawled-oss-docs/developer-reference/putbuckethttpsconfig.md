# PutBucketHttpsConfig

You can call the PutBucketHttpsConfig operation to configure TLS versions and encryption algorithm suites for a bucket.

## Usage notes


-

To configure TLS versions and encryption algorithm suites for a bucket, you must have the `oss:PutBucketHttpsConfig` permission. For more information, see [Grant custom permissions to a RAM user](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip).

-

Each region has its endpoints that you can use to access OSS in the region. For more information about the mappings between regions and endpoints, see [Endpoints and data centers](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

## Request syntax


`xml
PUT /?httpsConfig HTTP/1.1
Date: GMT Date
Authorization: SignatureValue
Host: BucketName.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<HttpsConfiguration>
  <TLS>
    <Enable>true</Enable>
    <TLSVersion>TLSv1.2</TLSVersion>
    <TLSVersion>TLSv1.3</TLSVersion>
  </TLS>
  <CipherSuite>
    <Enable>true</Enable>
    <StrongCipherSuite>false</StrongCipherSuite>
    <CustomCipherSuite>ECDHE-ECDSA-AES128-SHA256</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
  </CipherSuite>
</HttpsConfiguration>
`


## Request headers


All headers in a PutBucketHttpsConfig request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements


-


-


-


-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/set-tls-version#e1ad05f03bvb8)


-


-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/set-tls-version#228cc44f2bhtw)


(https://www.alibabacloud.com/help/en/oss/user-guide/set-tls-version#32fcb427eb8ue)


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| HttpsConfiguration | The container | Yes | None | The container that stores HTTPS configurations.Parent nodes: none |
| TLS | The container | Yes | None | The container that stores TLS version configurations.Parent nodes: HttpsConfiguration |
| Enable | Boolean | Yes | true | Specifies whether to enable TLS version control for the bucket. Valid values:truefalseParent nodes: TLS |
| TLSVersion | string | Optional | TLSv1.2 | The TLS version. This element is required only when you set the Enable element to true. Valid values:TLSv1.0TLSv1.1TLSv1.2TLSv1.3For more information about the scenarios and descriptions of TLS versions, see TLS version description.Parent nodes: TLS |
| CipherSuite | The container | Optional | None | The container that stores encryption algorithm suites.Parent nodes: HttpsConfiguration |
| Enable | Boolean | Optional | true | Configures TLS encryption algorithm suites. Valid values:true: strong encryption algorithm suites or custom encryption algorithm suites.false: all encryption algorithm suites (default).Parent nodes: CipherSuite |
| StrongCipherSuite | Boolean | Optional | false | Specifies whether to use strong encryption algorithm suites. Valid values:true: uses strong encryption algorithm suites.false: uses custom encryption algorithm suites.Parent nodes: CipherSuite |
| CustomCipherSuite | string | Optional | ECDHE-ECDSA-AES128-SHA256 | Specifies custom encryption algorithm suites. You can specify multiple suites. This field is used to configure custom encryption algorithm suites for TLS 1.2.Parent nodes: CipherSuite |
| TLS13CustomCipherSuite | string | Optional | ECDHE-ECDSA-AES256-CCM8 | Specifies custom encryption algorithm suites. You can specify multiple suites. This field is used to configure custom encryption algorithm suites for TLS 1.3.Parent nodes: CipherSuite |


## Response headers


All headers in the response to a PutBucketHttpsConfig request are common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample requests


`xml
PUT /?httpsConfig HTTP/1.1
Date: Thu, 17 Apr 2025 08:40:17 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Host: oss-example.oss-cn-hangzhou.aliyuncs.com

<?xml version="1.0" encoding="UTF-8"?>
<HttpsConfiguration>
  <TLS>
    <Enable>true</Enable>
    <TLSVersion>TLSv1.2</TLSVersion>
    <TLSVersion>TLSv1.3</TLSVersion>
  </TLS>
  <CipherSuite>
    <Enable>true</Enable>
    <StrongCipherSuite>false</StrongCipherSuite>
    <CustomCipherSuite>ECDHE-ECDSA-AES128-SHA256</CustomCipherSuite>
    <CustomCipherSuite>ECDHE-RSA-AES128-GCM-SHA256</CustomCipherSuite>
    <CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
    <TLS13CustomCipherSuite>ECDHE-ECDSA-AES256-CCM8</CustomCipherSuite>
  </CipherSuite>
</HttpsConfiguration>
`


-

Sample command output:


`json
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Wed, 16 Aug 2023 15:56:37 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
`


## Command-line tool ossutil


For more information about the ossutil command that corresponds to the PutBucketHttpsConfig operation, see [put-bucket-https-config](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-https-config).

Thank you! We've received your  feedback.