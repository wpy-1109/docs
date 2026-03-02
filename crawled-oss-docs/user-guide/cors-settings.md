# OSS configure cross-origin resource sharing CORS

When a website attempts to load a resource from Object Storage Service (OSS), the browser may report a "blocked by CORS policy" error. This happens because of the browser's same-origin policy, which restricts a web page to accessing resources only from its own protocol, domain, and port. For example, a page at `https://www.example.com` cannot directly access an OSS resource from a different domain, such as `https://example-bucket.oss-cn-hangzhou.aliyuncs.com/test.jpg`.![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8104597571/p1007027.png)By configuring cross-origin resource sharing (CORS) rules for your OSS bucket, you can securely authorize specific websites to access your OSS resources, allowing web pages to interact with objects directly.

## How it works


CORS requests are categorized into two types: simple requests and preflight requests. Simple requests are sent directly. Preflight requests, however, require a preliminary authorization check before the main request can be sent.


A preflight request is required if any of the following conditions are met:


-

The request uses a method other than `GET`, `HEAD`, or `POST`.

-

The request uses the `POST` method with a `Content-Type` other than `text/plain`, `application/x-www-form-urlencoded`, or `multipart/form-data`.

-

The request includes custom headers, such as `x-oss-*`.


When a browser sends a simple request to OSS, the following process occurs:


-

The browser adds an `Origin` header to the request. The `Origin` header specifies the origin of the calling page, for example, `Origin: https://www.example.com`.

-

OSS checks the request's HTTP method and `Origin` header against the bucket's CORS rules to find a matching rule. If a match is found, OSS includes the `Access-Control-Allow-Origin` header in the response. The value of this header is the value of the `Origin` header from the initial request.

-

The browser receives the response. It allows the request to proceed only if the `Access-Control-Allow-Origin` header is present and its value matches the page's domain. Otherwise, the request fails.


A preflight request first performs the following steps. If successful, it then proceeds with the same process as a simple request:


-

The browser sends an `OPTIONS` request that includes the method (`Access-Control-Request-Method`) and headers (`Access-Control-Request-Headers`) of the intended main request.

-

OSS checks if the method and headers in the request are allowed based on the CORS configuration. If the preflight request includes any method or header not allowed by the rules, the request fails, and the main request is not sent.

## Load static website resources


A website at `https://www.example.com` needs to load images, CSS, and JS files stored in an OSS bucket.


Step 1: Configure a CORS rule


Log on to the [OSS console](https://oss.console.alibabacloud.com/). Navigate to the Content Security> CORS page for the destination bucket and create a rule as follows:























-



-




| Parameter | Value | Description |
| --- | --- | --- |
| Origin | https://www.example.com | Restricts requests to this specific website to ensure resource security. |
| Allowed Methods | GET, HEAD | GET downloads resources, and HEAD validates caches. |
| Allowed Headers | Empty | This use case involves simple requests that do not trigger a preflight request, so this parameter is not required. |
| Exposed Headers | ETag, Content-Length | ETag lets browsers validate caches with HEAD requests. If an object is unchanged, the server returns a 304 Not Modified response to prevent re-downloading.Content-Length can be used to display resource loading progress on the frontend. |
| Cached Timeout (Seconds) | 86400 | Caches the preflight response for 24 hours to reduce potential future preflight requests. |
| Vary: Origin | Unchecked | Because the origin is single and specific, this option is not needed to handle multi-domain caching issues. |


Step 2: Verify the configuration


Visit `https://www.example.com` and confirm that OSS resources, such as images, load correctly and that there are no CORS errors in the browser console.

## Upload files directly from the frontend


A user on the web page `https://app.example.com` uploads files, such as avatars and documents, directly to OSS.


Step 1: Configure a CORS rule


Log on to the [OSS console](https://oss.console.alibabacloud.com/). Navigate to the Content Security> CORS page for the destination bucket and create a rule as follows:





























-



-




| Parameter | Value | Description |
| --- | --- | --- |
| Origin | https://app.example.com | Restricts uploads to this authorized application. |
| Allowed Methods | PUT, POST | PUT or POST are the required HTTP methods for performing upload operations. |
| Allowed Headers | * | Security for direct uploads relies on temporary signatures (e.g., Presigned URLs), not a fixed Authorization header. Using * accommodates various headers sent by the SDK (e.g., x-oss-meta-*), simplifying configuration without introducing security risks. |
| Exposed Headers | ETag, x-oss-request-id | ETag: A unique identifier for a successful file upload, used for subsequent verification.x-oss-request-id: If an upload fails, the frontend can capture this ID and provide it for technical support to quickly locate the problem. |
| Cached Timeout (Seconds) | 600 | Upload operations are less frequent, so a 10-minute cache reduces preflight requests while allowing configuration changes to take effect swiftly. |
| Vary: Origin | Checked | Prepares for potential future multi-domain deployments, such as a test environment, and prevents CDN cache pollution. |


Step 2: Verify the configuration


Perform an upload operation on the `https://app.example.com` page and confirm that the file is successfully uploaded to OSS and that there are no CORS errors in the browser console.

## Support for multiple environments


Multiple subdomains for development, testing, and production, such as `dev.example.com` and `app.example.com`, need to access the same OSS resources.


Step 1: Configure a CORS rule


Log on to the [OSS console](https://oss.console.alibabacloud.com/). Navigate to the Content Security> CORS page for the destination bucket and create a rule as follows:
































| Parameter | Value | Description |
| --- | --- | --- |
| Origin | https://*.example.com | Uses the * wildcard to authorize all subdomains under example.com that use the HTTPS protocol. |
| Allowed Methods | GET, PUT, POST | Allows both reading and uploading of resources to meet testing needs across multiple environments. |
| Allowed Headers | * | Different environments and features in development may introduce different custom headers. Using * avoids the need to frequently modify CORS rules. |
| Exposed Headers | ETag, x-oss-request-id | Supports both download validation and upload result feedback. |
| Cached Timeout (Seconds) | 3600 | A 1-hour cache provides flexibility for debugging across multiple environments. |
| Vary: Origin | Checked | Required. This instructs the CDN to cache responses based on the Origin header, preventing cache conflicts between environments. |


Step 2: Verify the configuration


Perform access or upload tests on both `https://dev.example.com` and `https://app.example.com` to confirm that all operations succeed.

## Make API-style calls with authentication


A frontend application at `https://api.example.com` needs to access protected OSS resources by including custom headers such as `Authorization`.


Step 1: Configure a CORS rule


Log on to the [OSS console](https://oss.console.alibabacloud.com/). In the destination bucket, navigate to the Content Security> CORS page and create a rule as follows:


























| Parameter | Value | Description |
| --- | --- | --- |
| Origin | https://api.example.com | For requests with authentication information, the origin must be a precise, trusted domain. |
| Allowed Methods | GET, PUT, DELETE | Supports full lifecycle management of private resources, including reading, updating, and deleting. |
| Allowed Headers | authorization, content-type, x-oss-* | Do not use *. Explicitly list all required headers. Follow the principle of least privilege to avoid exposing unnecessary header details. |
| Exposed Headers | ETag, x-oss-request-id | Provides a verification identifier for successful operations and an ID for troubleshooting. |
| Cached Timeout (Seconds) | 600 | For authenticated requests, a shorter preflight cache time (10 minutes) helps apply security policy changes more quickly. |
| Vary: Origin | Select | Instructs the CDN to cache responses separately for different origins to avoid confusion. |


Step 2: Verify the configuration


Initiate a request with an `Authorization` header from the `https://api.example.com` page and confirm that you can access the protected OSS resource.

## Apply in production

### Security best practices


Follow the principle of least privilege.


-

Configure `Origin (AllowedOrigin)` precisely: Avoid setting `*` for `Sources` unless your bucket is fully public. Specify exact domains, such as `https://www.example.com`.

-

Restrict `Allowed Methods`: Expose only the HTTP methods required for your business. For example, if your website only needs to read data, configure only `GET` and `HEAD`.

-

Specify `Allowed Headers` explicitly: For requests that carry authentication information (such as an `Authorization`header), do not use `*`. You must explicitly list all required request headers.

### Performance best practices


-

Optimize the preflight cache: A reasonable `MaxAgeSeconds` value, such as `86400` seconds (24 hours) can significantly reduce preflight requests, lowering latency and cost.

-

Evaluate the impact of `Vary: Origin`: Enabling the `Vary: Origin` response header solves cache poisoning issues, but it increases the complexity of CDN caching. This may lead to a lower cache hit ratio and increased back-to-origin traffic, resulting in additional costs and latency. Use this option only after a thorough evaluation.

### CDN acceleration


If your bucket is accelerated by Alibaba Cloud CDN and accessed via a CDN domain, cross-origin requests will first reach a CDN Point of Presence (PoP). You must configure CORS rules in the CDN console, not in the OSS console. The CORS configuration in OSS only applies to requests made directly to the OSS origin domain. For details, see [Configure CORS](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-cors).

## Parameters of CORS rules 


You can configure up to 20 CORS rules for each bucket. OSS evaluates rules sequentially from top to bottom and applies the first one that matches the request. Once a match is found, OSS does not check subsequent rules.











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







-




> IMPORTANT:

> NOTE: 


> NOTE: 


| Parameter | Required | Description |
| --- | --- | --- |
| Origin (AllowedOrigin) | Yes | Specifies the websites (origin domains) that are allowed to make cross-origin requests to OSS resources.The format is protocol://domain[:port]. Example: https://www.example.com.The * wildcard is supported, but you can use it only once in each origin.Valid examples: https://*.example.com or http://localhost:*Invalid examples: https://*.example.* or https://*Multiple origins are allowed, one per line. |
| Allowed Methods (AllowedMethod) | Yes | Specifies the allowed HTTP methods.Valid values: GET, PUT, POST, DELETE, HEAD.Multiple methods are allowed. |
| Allowed Headers (AllowedHeader) | No | Applies to preflight requests and determines which HTTP headers can be included in the actual request.The * wildcard character is supported, which allows all headers.Multiple headers are allowed, one per line. The headers are NOT case-insensitive. |
| Exposed Headers (ExposeHeader) | No | Specifies which OSS response headers are accessible to client-side JavaScript.The * wildcard character is not supported.Multiple headers are allowed, one per line.Use case: To get the ETag or x-oss-request-id of an uploaded file in JavaScript, add ETag and x-oss-request-id to this parameter. |
| Cached Timeout (MaxAgeSeconds) | No | Specifies the time in seconds that a browser can cache the result of a preflight OPTIONS request.Effect: Within the cache duration, subsequent identical cross-origin requests for the same resource will not trigger a new preflight request, which optimizes performance. |
| Vary: Origin | No | Determines whether to add the Vary: Origin HTTP response header. This header tells CDNs and other intermediate caches to cache different versions of the resource based on the request's Origin header. This prevents cache pollution when multiple origins access the same resource.Use case: To prevent cache pollution when you configure multiple domains or a wildcard for the Sources parameter, enable this option.Important Enabling this option may decrease the CDN cache hit ratio. |


## FAQ

### Error: `No 'Access-Control-Allow-Origin' header is present on the requested resource.`


This error typically means the browser has cached an old response without CORS headers, or no CORS rule matches the incoming request.


First, try clearing your browser cache and retesting. If the error persists, follow these steps to check if your CORS rules are set correctly:


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

Click Buckets, then click the name of the destination bucket.

-

In the navigation pane on the left, choose Content Security > CORS.

-

On the CORS page, click Create Rule.

-

In the Create CORS Rule panel, set Origin to `*`, select all Allowed Methods, set Allowed Headers to `*`, set Exposed Headers to `ETag` and `x-oss-request-id`, set Cache Timeout (Seconds) to 0, select Vary: Origin, and click OK.

-

If the issue persists, log on to any server and run the following command to view the cross-origin request headers.


`shell
curl -v -o output_file.txt -H 'Origin:[$URL2]' '[$URL1]'
`


> NOTE:

> NOTE: 


> NOTE: Note 

-

[URL1] is the URL of the requested OSS resource.

-

[URL2] is the origin address you configured in the CORS rule.


The system displays an output similar to the following.


!(https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5586716071/p512442.png)


-

If the response includes a matching CORS header, the problem is likely browser or network caching. Your first request might not have triggered a cross-origin check, and the response was cached locally. A subsequent cross-origin request might have fetched the data from the local cache instead of the server, causing the cross-origin check to fail. Try the following solutions:


-

Press Ctrl+F5 in your browser to clear the cache, then test if the issue persists.

-

Set Cached-Seconds for the CORS rule to 0. This prevents the preflight response from being cached on the client, forcing every request to re-fetch authorization information from the server.


> NOTE:

> NOTE: 


> NOTE: Note 

You can set the `cache-control`of an object to `no-cache` when you upload it. For objects that are already uploaded, you can ossutil to change this setting. For more information, see [set-meta](https://www.alibabacloud.com/help/en/oss/developer-reference/set-meta).


-

Use CDN to accelerate OSS. This ensures that all requests served by the CDN return a CORS header.

-

If the response contains two CORS headers or a header that does not match your OSS configuration, the issue is likely caused by using CDN to accelerate OSS:


-

Log on to the [CDN console](https://cdn.console.alibabacloud.com/domain/list) and temporarily disable CDN acceleration for the domain name to confirm that the cross-origin issue is resolved.

-

After confirmation, click the specific domain name, then navigate to Cache Configuration > Node HTTP Response Header.

-

Set custom HTTP response headers as needed.

-

If the CORS issue is still not resolved, see [Common errors and solutions for OSS CORS](https://www.alibabacloud.com/help/en/oss/cors-error-diagnosis) for further troubleshooting.

### Error: `The 'Access-Control-Allow-Origin' header has a value '...' that is not equal to the supplied origin.`


The server returned an `Access-Control-Allow-Origin` header, but its value does not match the current request's `Origin`. This is often a caching problem. When multiple domains access the same resource, a browser or CDN might cache the response for one domain and serve it incorrectly to another.


Enable the Vary: Origin option in your CORS rule to prevent cache conflicts between different websites, or clear your browser cache before retrying.

### Error: `Response to preflight request doesn't pass access control check: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'.`


This error occurs because the frontend code sent a request with credentials (`Access-Control-Allow-Credentials` is `True`), but the `Access-Control-Allow-Origin` was configured as the wildcard `*`. For security, browsers prohibit this combination to prevent any site from making credentialed requests and accessing sensitive data like cookies or `Authorization` tokens.


-

If you need to include credentials in the request, change the value of `Sources` from the wildcard `*` to a specific domain (e.g., `https://example.com`).

-

If you do not need to include credentials in the request, you can set `xhr.withCredentials` to `false` in your frontend code and ensure that `Access-Control-Allow-Credentials` is set to `false` on the server side.

### How to improve slow cross-origin loading from OSS?


A cross-origin request is a standard HTTP request that includes an `Origin` header. Loading speed depends on network latency between the client and the OSS bucket. For example, a request from a client in China (Hong Kong) to a bucket in the Chinese mainland is considered long-distance access. We recommend using a transfer acceleration endpoint in such cases to optimize the network path. For more information, see [Transfer Acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration).


> NOTE:

> NOTE: 


> NOTE: Note 

Transfer Acceleration uses an optimized network to improve data transfer speeds for users globally, enhancing the access experience for users in different regions.


Thank you! We've received your  feedback.