# PutBucketCors

Configures cross-origin resource sharing (CORS) rules for a bucket. CORS is disabled by default, and all cross-origin requests are rejected until you configure rules with this operation.

## Usage notes


-

Overwrite semantics: PutBucketCors replaces all existing CORS rules. The configuration you submit completely overwrites the previous one.

-

Enable CORS in your application: To allow cross-origin access from a browser (for example, using `XMLHttpRequest` from `example.com` to access OSS), call PutBucketCors with the appropriate rules before making cross-origin requests.

-

Disable CORS: To remove all CORS rules and disable CORS for a bucket, call [DeleteBucketCors](https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketcors).

### How rule matching works


When OSS receives a cross-origin request or an OPTIONS request, it evaluates the CORS rules in order and applies the first match. If no rule matches, OSS does not include any CORS-related headers in the response.


A rule matches only when all three conditions are met:


-

The request origin matches an `AllowedOrigin` value.

-

The request method (such as GET or PUT), or the method in the `Access-Control-Request-Method` header for an OPTIONS preflight request, matches an `AllowedMethod` value.

-

Every header listed in the `Access-Control-Request-Headers` header of the OPTIONS preflight request matches an `AllowedHeader` value.

### Limits


| Constraint | Limit |
| --- | --- |
| Maximum CORS rules per bucket | 20 |
| Maximum XML body size | 16 KB |
| Wildcard character (*) in AllowedOrigin | One per element |
| Wildcard character (*) in AllowedHeader | One per element |
| Wildcard character (*) in ExposeHeader | Not supported |
| MaxAgeSeconds per CORS rule | One per rule |


Characters not allowed in `AllowedHeader`: `<>&'"`


Characters not allowed in `ExposeHeader`: `*<>&'"`

## Permissions


By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles have no permissions by default. Grant permissions through [RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/) or [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).


| API | Action | Description |
| --- | --- | --- |
| PutBucketCors | oss:PutBucketCors | Configure CORS rules for a bucket |


## Request syntax


`plaintext
PUT /?cors HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration>
    <CORSRule>
      <AllowedOrigin>the origin to allow</AllowedOrigin>
      <AllowedMethod>the HTTP method to allow</AllowedMethod>
      <AllowedHeader>the request header to allow</AllowedHeader>
      <ExposeHeader>the response header to expose</ExposeHeader>
      <MaxAgeSeconds>preflight cache duration in seconds</MaxAgeSeconds>
    </CORSRule>
    <ResponseVary>false</ResponseVary>
</CORSConfiguration>
`


## Request elements


| Name | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| CORSConfiguration | Container | Yes | N/A | Root container for the CORS configuration. |
| CORSRule | Container | Yes | N/A | A single CORS rule. A bucket supports up to 20 rules, and the XML body must not exceed 16 KB. Parent node: CORSConfiguration. |
| AllowedOrigin | String | Yes | * | An origin allowed to make cross-origin requests. Specify multiple origins with multiple AllowedOrigin elements. A single asterisk (*) matches all origins. Only one wildcard character is allowed per element. Include the protocol and port for non-default ports (for example, https://example.com:8443). Parent node: CORSRule. |
| AllowedMethod | Enumeration | Yes | GET | An HTTP method allowed for cross-origin requests. Valid values: GET, PUT, DELETE, POST, HEAD. Parent node: CORSRule. |
| AllowedHeader | String | No | Authorization | A request header allowed in cross-origin requests. Each header in the Access-Control-Request-Headers header of an OPTIONS preflight request must match an AllowedHeader value. Set to * to allow all headers. Only one wildcard character is allowed per element. Characters not allowed: < > & ' ". Parent node: CORSRule. |
| ExposeHeader | String | No | x-oss-test | A response header that client applications (such as JavaScript XMLHttpRequest) can access. Wildcards (*) are not supported. Characters not allowed: * < > & ' ". Parent node: CORSRule. |
| MaxAgeSeconds | Integer | No | 100 | How long (in seconds) the browser caches the response to an OPTIONS preflight request. Only one MaxAgeSeconds element is allowed per CORS rule. Parent node: CORSRule. |
| ResponseVary | Boolean | No | false | Whether to return the Vary: Origin header. true: always returns Vary: Origin, regardless of whether the request is cross-origin or whether CORS matching succeeds. false (default): never returns Vary: Origin. This element takes effect only when at least one CORS rule is configured. Parent node: CORSConfiguration. |


For more information about common request headers such as `Host` and `Authorization`, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers).

## Response headers


This operation returns only common response headers. For more information, see [Common response headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers).

## Examples

### Allow all origins with specific methods


This example configures a rule that allows GET and PUT requests from any origin with the `Authorization` header.


Request


`plaintext
PUT /?cors HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Content-Length: 186
Date: Fri, 04 May 2012 03:21:12 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration>
    <CORSRule>
      <AllowedOrigin>*</AllowedOrigin>
      <AllowedMethod>PUT</AllowedMethod>
      <AllowedMethod>GET</AllowedMethod>
      <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    <CORSRule>
      <AllowedOrigin>http://example.com</AllowedOrigin>
      <AllowedOrigin>http://example.net</AllowedOrigin>
      <AllowedMethod>GET</AllowedMethod>
      <AllowedHeader> Authorization</AllowedHeader>
      <ExposeHeader>x-oss-test</ExposeHeader>
      <ExposeHeader>x-oss-test1</ExposeHeader>
      <MaxAgeSeconds>100</MaxAgeSeconds>
    </CORSRule>
    <ResponseVary>false</ResponseVary>
</CORSConfiguration>
`


The first rule allows PUT and GET requests from any origin with the `Authorization` header. The second rule restricts GET access to `http://example.com` and `http://example.net`, exposes custom headers `x-oss-test` and `x-oss-test1`, and caches preflight responses for 100 seconds.


Response


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 50519080C4689A033D0*
Date: Fri, 04 May 2012 03:21:12 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
x-oss-server-time: 94
`


## Error codes


| Error code | HTTP status code | Description |
| --- | --- | --- |
| InvalidDigest | 400 | The Content-MD5 value in the request header does not match the MD5 digest calculated from the request body. |


## SDK references


SDKs for the following languages support this operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-1#undefined)

-

[Python V2](https://www.alibabacloud.com/help/en/oss/developer-reference/cross-domain-resource-sharing-using-oss-sdk-for-python-v2)

-

[PHP V2](https://www.alibabacloud.com/help/en/oss/developer-reference/cross-domain-resource-sharing-for-php-sdk-v2)

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/cross-domain-resource-sharing-for-go-sdk-v2)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-10#undefined)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-3#undefined)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-9#undefined)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-8#section-jfv-uw1-ua4)

-

[Ruby](https://www.alibabacloud.com/help/en/oss/developer-reference/cors-6#undefined)

## ossutil command-line interface


For the ossutil command, see [put-bucket-cors](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-cors).

## Related operations


-

[GetBucketCors](https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketcors) -- Query the CORS rules configured for a bucket.

-

[DeleteBucketCors](https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketcors) -- Delete all CORS rules and disable CORS for a bucket.

-

[OptionObject](https://www.alibabacloud.com/help/en/oss/developer-reference/optionobject) -- Send an OPTIONS preflight request to check whether a cross-origin request is allowed.

Thank you! We've received your  feedback.