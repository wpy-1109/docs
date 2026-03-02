# WriteGetObjectResponse

Specifies the return data and response headers for a GetObject request.

## Prerequisites


The `oss:WriteGetObjectResponse` permission is granted to the default role (AliyunFCDefaultRole) of the service you created in the Function Compute console. Sample permission policy:


`json
{
  "Statement": [
    {
      "Action": "oss:WriteGetObjectResponse",
      "Effect": "Allow",
      "Resource": "*"
    }
  ],
  "Version": "1"
}
`


For more information, see [Grant permissions to a RAM role](https://www.alibabacloud.com/help/en/ram/user-guide/grant-permissions-to-a-ram-role).

## Request headers


`xml
POST /?x-oss-write-get-object-response HTTP/1.1
Host: RouteFromFcEvent
Date: GMT Date
Authorization: SignatureValue
x-oss-request-route: RouteFromFcEvent
x-oss-request-token: TokenFromFcEvent
x-oss-fwd-status: StatusCode
x-oss-fwd-header-Accept-Ranges: AcceptRanges
x-oss-fwd-header-Cache-Control: CacheControl
x-oss-fwd-header-Content-Disposition: ContentDisposition
x-oss-fwd-header-Content-Encoding: ContentEncoding
x-oss-fwd-header-Content-Language: ContentLanguage
Content-Length: ContentLength
x-oss-fwd-header-Content-Range: ContentRange
x-oss-fwd-header-Content-Type: ContentType
x-oss-fwd-header-ETag: ETag
x-oss-fwd-header-Expires: Expires
x-oss-fwd-header-Last-Modified: LastModified
`


## Request headers


(https://www.alibabacloud.com/help/en/oss/developer-reference/include-signatures-in-the-authorization-header#concept-aml-vv2-xdb)


-


-


-


-


-


-



-



-




-


-


-


-


-


| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Host | String | Yes | -opap.oss-cn-qingdao-internal.oss-object-process.aliyuncs.com | The router forwarding address obtained from the event parameter of Function Compute. |
| Date | String | Yes | Tue, 31 Oct 2023 03:17:58 GMT | The time when the request was initiated. The time is in GMT specified by HTTP 1.1. |
| Authorization | String | Yes | OSS lkojgn8y1exic6e:6+BuuEqzI1tAMW0wgIyl | The authentication information used to verify the validity of the request. For more information about how to calculate the Authorization header, see Include signatures in the Authorization header. |
| x-oss-request-route | String | Yes | -opap.oss-cn-qingdao-internal.oss-object-process.aliyuncs.com | The router forwarding address obtained from the event parameter of Function Compute. |
| x-oss-request-token | String | Yes | OSSV1#ZvBDC3XPm3g | The unique forwarding token obtained from the event parameter of Function Compute. |
| x-oss-fwd-status | String | Yes | 200 | The HTTP status code returned by the backend server. Valid values: 200, 206, 301, 302, 303, 304, 400, 401, 403, 404, 405, 409, 411, 412, 416, 500, and 503. |
| x-oss-fwd-header-Accept-Ranges | String | No | bytes | The HTTP response header returned by the backend server. It is used to specify the scope of the resources that you want to query. |
| x-oss-fwd-header-Cache-Control | String | No | no-cache | The HTTP response header returned by the backend server. It is used to specify the resource cache method that the client uses. Valid values:no-cache: Each time you access a cached object, the server checks whether the object is updated. If the object is updated, the cache expires. The object must be downloaded from the server again. If the object is not updated, the cache does not expire, and you can directly use the cached object. no-store: All content of the object is not cached. public: All content of the object is cached. private: All content of the object is cached only on the client. max-age=<seconds>: the validity period of the cached content. Unit: seconds. This option is available only in HTTP 1.1. |
| x-oss-fwd-header-Content-Disposition | String | No | attachment | The HTTP response header returned by the backend server. It is used to specify the name of the object to download and whether and how the object is downloaded. Valid values:Content-Disposition:inline: The object is previewed. Content-Disposition:attachment: The object is downloaded to the specified path in the browser with the original object name. Content-Disposition:attachment; filename="yourFileName": The object is downloaded to the specified path in the browser with a custom name. yourFileName specifies the custom name of the downloaded object, such as example.jpg. |
| x-oss-fwd-header-Content-Encoding | String | No | gzip | The HTTP response header returned by the backend server. It is used to specify the compression and encoding method of the downloaded object. Valid values:identity (default): OSS does not compress or encode the object. gzip: OSS uses the LZ77 compression algorithm created by Lempel and Ziv in 1977 and 32-bit cyclic redundancy check (CRC) to encode the object. compress: OSS uses the Lempel–Ziv–Welch (LZW) compression algorithm to encode the object. deflate: OSS uses the zlib library and the deflate algorithm to encode the object. br: OSS uses the Brotli algorithm to encode the object. |
| x-oss-fwd-header-Content-Language | String | No | en | The HTTP response header returned by the backend server. It is used to specify the language of the downloaded object. |
| Content-Length | String | Yes | 67589 | The HTTP response header returned by the backend server. It is used to specify the size of the HTTP message body. Unit: bytes. |
| x-oss-fwd-header-Content-Range | String | No | bytes 0-9/67589 | The HTTP response header returned by the backend server. It is used to specify the range of the object that you want to query. For example, if the Content-Range header is set to bytes 0-9/67589, the size of the entire object is 67589 and the content of the first 10 bytes (0 to 9) is returned. |
| x-oss-fwd-header-Content-Type | String | No | text/html; charset=utf-8 | The HTTP response header returned by the backend server. It is used to specify the type of the received or sent data. |
| x-oss-fwd-header-ETag | String | No | D41D8CD98F00B204E9800998ECF8 | The HTTP response header returned by the backend server. It uniquely identifies the object. |
| x-oss-fwd-header-Expires | String | No | Fri, 10 Nov 2023 03:17:58 GMT | The HTTP response header returned by the backend server. It specifies the absolute expiration time of the cache. |
| x-oss-fwd-header-Last-Modified | String | No | Tue, 10 Oct 2023 03:17:58 GMT | The HTTP response header returned by the backend server. It specifies the time when the requested resource was last modified. |


## Response headers


The response to a WriteGetObjectResponse request contains only common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Examples


-

Sample request


`xml
POST /?x-oss-write-get-object-response HTTP/1.1
Host: RouteFromFcEvent
Date: Tue, 31 Oct 2023 03:17:58 GMT
Authorization: SignatureValue
x-oss-request-route: RouteFromFcEvent
x-oss-request-token: TokenFromFcEvent
x-oss-fwd-status: 200
x-oss-fwd-header-Accept-Ranges: bytes
x-oss-fwd-header-Cache-Control: no-cache
x-oss-fwd-header-Content-Disposition: attachment
x-oss-fwd-header-Content-Encoding: gzip
x-oss-fwd-header-Content-Language: en
Content-Length: 67589
x-oss-fwd-header-Content-Range: bytes 0-9/67589
x-oss-fwd-header-Content-Type: text/html; charset=utf-8
x-oss-fwd-header-ETag: D41D8CD98F00B204E9800998ECF8
x-oss-fwd-header-Expires: Fri, 10 Nov 2023 03:17:58 GMT
x-oss-fwd-header-Last-Modified: Tue, 10 Oct 2023 03:17:58 GMT
`


-

Sample response


`xml
HTTP/1.1 200 OK
x-oss-request-id: 6540CF0DCB24453133A
Date: Tue, 31 Oct 2023 03:17:58 GMT
Content-Length: 0
`


Thank you! We've received your  feedback.