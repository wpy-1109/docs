# Options

Before a cross-origin request is sent, the browser sends a preflight (OPTIONS) request that includes a specific origin, HTTP method, and header information to Object Storage Service (OSS) to determine whether to send the cross-origin request. The browser automatically determines whether to send the preflight request based on whether the actual request is a cross-origin request.

## Request structure


`plaintext
OPTIONS /ObjectName HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Origin:Origin
Access-Control-Request-Method:HTTP method
Access-Control-Request-Headers:Request Headers
`


## Request headers

















| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| Origin | String | Yes | http://www.example.com | The origin of the request, which is used to identify a cross-origin request. You can specify only one Origin header in a cross-origin request. Default value: null |
| Access-Control-Request-Method | String | Yes | PUT | The method to use in the actual cross-origin request. You can specify only one Access-Control-Request-Method header in a cross-origin request. Default value: null |
| Access-Control-Request-Headers | String | No | x-oss-test1,x-oss-test2 | The custom headers to be sent in the actual cross-origin request. You can configure multiple custom headers in a cross-origin request. Custom headers are separated by commas (,). Default value: null |


## Response headers














| Header | Type | Example | Description |
| --- | --- | --- | --- |
| Access-Control-Allow-Origin | String | http://www.example.com | The origin that is included in the request. If the request is denied, the response does not contain the header. |
| Access-Control-Allow-Methods | String | PUT | The HTTP method of the request. If the request is denied, the response does not contain the header. |
| Access-Control-Allow-Headers | String | x-oss-test,x-oss-test1 | The list of headers included in the request. If the request includes headers that are not allowed, the response does not contain the headers and the request is denied. |
| Access-Control-Expose-Headers | String | x-oss-test1,x-oss-test2 | The list of headers that can be accessed by JavaScript applications on a client. |
| Access-Control-Max-Age | Integer | 60 | The maximum duration for the browser to cache preflight results. Unit: seconds. |


## Examples


Sample requests


`plaintext
OPTIONS /testobject HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 05:45:34 GMT
Origin:http://www.example.com
Access-Control-Request-Method:PUT
Access-Control-Request-Headers:x-oss-test1,x-oss-test2
`


Sample responses


`plaintext
HTTP/1.1 200 OK
x-oss-request-id: 5051845BC4689A033D00
Date: Fri, 24 Feb 2012 05:45:34 GMT
Access-Control-Allow-Origin: http://www.example.com
Access-Control-Allow-Methods: PUT
Access-Control-Expose-Headers: x-oss-test1,x-oss-test2
Connection: keep-alive
Content-Length: 0
Server: AliyunOSS
`


## ossutil


For information about the ossutil command that corresponds to this operation, see [option-object](https://www.alibabacloud.com/help/en/oss/developer-reference/option-object).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessForbidden | 403 | The error message returned because OSS does not allow the cross-origin request or cross-origin resource sharing (CORS) is disabled for the bucket. You can call PutBucketCORS to enable CORS for the bucket. After CORS is enabled for the bucket and a preflight request is sent from the browser, OSS determines whether to allow the actual cross-origin request based on the specified CORS rules. |


Thank you! We've received your  feedback.