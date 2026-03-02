# Accelerate access to OSS with Alibaba Cloud CDN

When you distribute static resources such as images, audio, videos, and documents from Object Storage Service (OSS), you can configure Alibaba Cloud CDN to improve access speed, reduce latency, and lower traffic costs.

## How it works


Alibaba Cloud CDN accelerates access to OSS using a distributed caching architecture. It proactively distributes and caches static content from an OSS bucket (the origin) to Alibaba Cloud CDN points of presence (POPs) located worldwide. This architecture serves content from a location closer to your users.


-

When a user requests a resource for the first time, a smart DNS routes the request to the nearest CDN POP with the best network conditions.

-

The CDN POP checks its local cache. If the resource is not found, the POP sends an origin fetch request to the OSS origin to retrieve the content.

-

After receiving the content from OSS, the CDN POP caches the resource according to the configured cache rules and serves it to the user.

-

When subsequent users request the same resource, the CDN POP serves it directly from its local cache without contacting the origin. This process shortens the access path, reduces network latency, lowers the origin load, and accelerates access.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9800585671/CAEQThiBgIDFrvjqyxkiIGRmNzVmNDcwYzE0OTQyNzRiMzliNDYyMGEzOWFlZjY25588027_20250814153520.055.svg)


## Configure CDN acceleration


Before you begin, ensure that you have a registered domain name or [register a new one](https://wanwang.aliyun.com/domain). You can also use a domain name that is not registered with Alibaba Cloud. If the acceleration region is in the Chinese mainland, the accelerated domain name must have an [ICP filing](https://beian.aliyun.com/).

#### Step 1: Add a CDN-accelerated domain name and configure the origin server


-

Go to the [CDN console](https://cdnnext.console.aliyun.com/domain/list) and click Add Domain Name.

-

Select an Acceleration Region and a Business Type, and then enter the Accelerated Domain Name. You can use a primary domain name (such as `example.cn`) or a custom subdomain (such as `oss.example.cn`). Using a subdomain simplifies management and expansion.

-

Add the origin server information as shown in the figure below. Set the origin URL to the domain name of the OSS bucket, and then click Next to add the domain name.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p993713.png)

#### Step 2: Configure a CNAME record


Use a DNS CNAME record to point your accelerated domain name to the CNAME address assigned by Alibaba Cloud CDN. This routes DNS queries for your domain to CDN POPs.


-

On the Recommended Configuration page, click Open Configuration Guide. Alternatively, on the Domain Names page, hover over Pending Configuration to the right of the domain name, and click Open Configuration Guide in the tooltip that appears.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p993725.png)

-

Copy the CNAME record value, such as `example.cn.w.kunlunap.com`. You will use this address for your DNS configuration.

-

Go to the [Alibaba Cloud DNS console](https://dnsnext.console.alibabacloud.com/). Find the domain name and click Settings in the Actions column.

-

Click Add Record and enter the record information as described below. Keep the default settings for other parameters. If a CNAME record already exists, click Edit in the Actions column and update the value to the CNAME you copied.


-

Record Type: Select CNAME.

-

Hostname: If you are using a primary domain name such as `example.cn`, enter `@`. If you are using a subdomain such as `oss.example.cn`, enter the subdomain prefix, which is `oss`.

-

Record Value: Paste the CNAME record value you copied.

-

Click OK. In the Confirm DNS Record Change pop-up window, click OK again to complete the domain name resolution configuration.


The propagation time for DNS changes depends on the record's Time to Live (TTL) setting. It typically takes a few minutes to a few hours for the changes to fully propagate. The domain may be temporarily inaccessible after configuration. Wait for the changes to propagate, or try clearing your local DNS cache.

#### Step 3: Configure origin fetch for a private bucket


By default, new buckets are private. To allow Alibaba Cloud CDN to access a private bucket, you must authorize it by enabling private bucket access. If your bucket is public-read, this step is not necessary.


-

Go to the [CDN console](https://cdnnext.console.aliyun.com/domain/list), click the target domain name, then click Origin Fetch in the navigation pane on the left.

-

In the Alibaba Cloud OSS Private Bucket Access section, enable private bucket access as shown in the following figure.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p993821.png)


> IMPORTANT:

> NOTE: 


> NOTE: Important 

After you enable private bucket access, CDN is authorized to access the private bucket and automatically adds a signature to origin fetch requests. Therefore, the client must use a URL without signature parameters, such as `http://example.cn/dest.jpg`. If the URL includes signature parameters such as `Expires` and `Signature`, this causes a double-signing conflict, leading to a 403 error from OSS.


#### Step 4: Verify the acceleration effect


After completing the configuration, run a comparison test to verify the performance improvement of the accelerated domain name.


-

Upload a file to the bucket


On the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click your bucket name. On the Objects page, click Upload Object. Select a static resource to upload, such as [dest.jpg](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/en-US/20250808/trnpcq/dest.jpg), and follow the on-screen prompts to complete the upload.

-

Obtain the file access URL


-

Default OSS access URL: On the Objects page, click View Details in the Actions column for the desired object. On the details page that appears, click Copy Object URL.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994938.png)

-

CDN-accelerated access URL: Construct an access URL without a signature using the CDN-accelerated domain name and the file name. For example, `http://example.cn/dest.jpg`, where `example.cn` is the CDN-accelerated domain name.

-

Verify the acceleration effect


Use a professional speed testing platform or tool, such as the [CloudMonitor Synthetic Tests](https://cloudmonitor.console.alibabacloud.com/disposableTest), to compare the loading times of the same file using the default OSS access URL and the CDN-accelerated access URL.


> NOTE:

> NOTE: 


> NOTE: Note 

The test data is for reference only. The improvement in access speed may vary due to different network environments, geographical locations, and other factors. During the first test, the acceleration effect may not be obvious because CDN POPs have not yet cached the resource and must perform an origin fetch to retrieve it. After the first test, wait for the CDN to cache the resource, and then test again to see the acceleration effect.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p995067.png)

-

Check the cache hit status


Use your browser's developer tools (F12) to check the value of the `X-Cache` field in the response headers. This value indicates whether the request hit the CDN cache.


-

If the value starts with `HIT`, the request successfully hit the CDN cache, and the acceleration was effective.

-

If the value starts with `MISS`, the request missed the CDN cache, and an origin fetch was sent to OSS to retrieve the resource.

## Configure origin fetch to multiple buckets


When your architecture relies on multiple OSS buckets to store different types or categories of resources, use one of the following two multi-origin configurations.

#### Method 1: Independent subdomain architecture


Assign independent, semantic subdomains to buckets for different functions or resource types, and configure separate CDN acceleration for each subdomain. For example, use the subdomain `img.example.cn` for image resources and `video.example.cn` for audio and video resources. Semantic subdomains make resources easier to identify and maintain. They also enable DNS traffic distribution, which helps avoid single-domain concurrent connection limits.


This architecture completely isolates different types of resources, allowing you to set and optimize cache policies, security configurations, and monitoring for each bucket independently:


-

Configure a long-term cache policy for image resources to improve access speed.

-

Enable range origin fetch for video resources to support resumable downloads.

-

Enable URL signing for sensitive documents to ensure security.


An independent monitoring system accurately locates performance bottlenecks and unusual traffic. This enables fine-grained operational management and reduces the risk of interference between different services.

#### Method 2: Unified domain with path-based routing


If you have multiple buckets for different services or applications but want to provide a single, unified access point, you can configure a single CDN-accelerated domain name. Use the [rules engine](https://www.alibabacloud.com/help/en/cdn/user-guide/rules-engine) to route requests with different access paths to specific buckets. This approach unifies your brand image, simplifies domain name and SSL certificate maintenance, and reduces O&M complexity. The following example uses two buckets, `cdn-bucket1` and `cdn-bucket2`, to explain the configuration.


-

Add path rules


First, in the [CDN console](https://cdnnext.console.aliyun.com/), click the target accelerated domain name. Then, click Rules Engine > Add Rule. Add two URL path rules to match `http://example.cn/bucket1/*` and `http://example.cn/bucket2/*` respectively, as shown in the following figure. In this example, `example.cn` is the accelerated domain name. `bucket1` and `bucket2` are virtual paths that point to `cdn-bucket1` and `cdn-bucket2` respectively. `*` represents the actual path of the object within the bucket.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994622.png)

-

Configure conditional origins


In the Basic Information section for the accelerated domain name, configure two conditional origins. Attach the created path rules to their respective target bucket origin addresses. This ensures that requests are automatically routed to the correct origin based on the matching path rule.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994624.png)

-

Specify the origin host


After you configure conditional origin routing, you must also specify the origin host for each origin server in the Origin Fetch configuration of the accelerated domain name. This ensures that origin requests are routed to the correct target bucket.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994626.png)

-

Rewrite the origin URL


To ensure that the origin can correctly locate resources, you must rewrite the origin URL in the Origin Fetch configuration of the accelerated domain name. This rewrite automatically removes the virtual path used for routing (such as `/bucket1`) during origin fetch, so that the origin request path matches the actual storage path of the object in the bucket.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994628.png)

-

Verify the effect


After the configuration is complete, you can use a single CDN-accelerated domain name to access resources in different OSS buckets based on different paths. This provides a unified entry point for multi-origin access.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p995076.png)

## Going live

#### Best practices


-

Secure transmission: Enable HTTPS


For more information, see [Configure an HTTPS certificate](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-an-ssl-certificate) for your accelerated domain name and enable forced HTTPS redirection to encrypt data transmitted between clients and CDN POPs. HTTPS prevents data from being stolen or tampered with during transmission and avoids "Not Secure" warnings in browser address bars, enhancing user trust, brand image, and compliance with modern web security standards.

-

Performance optimization: Configure comprehensive cache policies


Cache policies are at the core of CDN performance. A well-designed cache policy should address both the cache duration and parameter handling to achieve optimal performance and functional compatibility.


-

Set TTL: By [setting a reasonable cache period](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-the-cdn-cache-expiration-time), you can maximize the cache hit ratio and significantly reduce the frequency of origin fetch requests and bandwidth costs.


-

Static files that are not updated frequently: For files such as images, audio, videos, and application installation packages, set a long cache period, such as one month or more, to reduce unnecessary origin requests.

-

Frequently updated static files: For files such as JS and CSS, set the cache period to several hours or days based on your business update frequency. Use versioning (for example, `style.v1.1.css`) for release management.

-

Dynamic files or APIs: For files such as PHP and JSP, set the cache time to 0 seconds (no caching) to ensure that every request fetches the latest content.

-

Configure parameter handling to enable image processing: OSS provides image processing features, such as scaling, cropping, and watermarking. By default, CDN filters all parameters to maximize the cache hit ratio. This prevents image processing instructions, such as `?x-oss-process`, from working. To use these features, go to the [CDN console](https://cdnnext.console.aliyun.com/), navigate to Domain Names > your accelerated domain name > Performance Optimization, and modify the [Ignore Parameters](https://www.alibabacloud.com/help/en/cdn/user-guide/ignore-parameters) configuration.

-

Ensuring availability: Use resource prefetch and automatic cache updates


When caching is enabled, changes to origin files are not immediately propagated to CDN POPs. To ensure users can access the latest resources promptly and to maintain service stability during critical periods such as a version release, we recommend the following strategies.


-

Resource prefetch: Before a version release or an operational activity, use the [purge and prefetch resources](https://www.alibabacloud.com/help/en/cdn/user-guide/refresh-and-prefetch-resources) feature of Alibaba Cloud CDN to distribute hot spot resources to global nodes in advance. This prevents a surge of origin requests from impacting the origin server when the content is published and ensures a smooth experience for users during their first access.

-

Auto CDN cache update: On the Bucket Settings > Domain Names page of the OSS console, enable Auto CDN Cache Update for the domain name. When you update an OSS file through an API, OSS automatically triggers a CDN refresh task, ensuring users can promptly access the latest content.


> NOTE:

> NOTE: 


> NOTE: Note 

This feature is effective only when the CDN-accelerated domain name and the OSS bucket belong to the same Alibaba Cloud account. It does not guarantee absolute real-time updates. For use cases with extremely high timeliness requirements, actively use the CDN refresh feature after updating a file.


-

Cross-origin access: Configure a CORS policy


Configuring CORS rules only at the OSS origin is unreliable for cross-origin requests. The CDN may cache and serve a response that lacks the necessary CORS headers, causing the browser to block the request. The recommended solution is to configure the Access-Control-Allow-Origin and other required CORS headers directly on the CDN. This ensures they are included in every relevant response, regardless of the cache status.


-

On the [CDN console](https://cdn.console.alibabacloud.com/domain/list), click the accelerated domain name or Manage in the Actions column.

-

On the Cache > Modify HTTP Response Header page, configure the parameters and values for the response header as shown in the following figure.


> NOTE:

> NOTE: 


> NOTE: Note 

The parameter settings are for reference only. Adjust them as needed.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994907.png)


After the configuration is complete, when you access OSS resources through a CDN POP, the response consistently includes the specified CORS headers. This ensures that cross-origin requests pass browser validation.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p994916.png)

-

Performance optimization: Improve efficiency for large files and data transfer


-

Enable range origin fetch: For use cases such as on-demand video/audio streaming and large file distribution, it is crucial to [enable range origin fetch](https://www.alibabacloud.com/help/en/cdn/user-guide/object-chunking). This feature allows CDN POPs to request parts of large files on demand. It not only enables advanced features such as seeking during video playback, but also significantly reduces unnecessary back-to-origin traffic and initial load times.

-

Optimize data transfer: Enable [Gzip compression](https://www.alibabacloud.com/help/en/cdn/user-guide/use-the-gzip-compression-feature) or [HTML optimization](https://www.alibabacloud.com/help/en/cdn/user-guide/enable-html-optimization) in the CDN console to reduce the transfer size of text files, such as JS, CSS, and HTML, and improve transfer efficiency. Gzip compression compresses resources before they are returned, while HTML optimization automatically removes redundant content, such as comments and repeated whitespace characters, from HTML pages and embedded JavaScript and CSS.


> NOTE:

> NOTE: 


> NOTE: Note 

-

Enabling HTML optimization or Gzip compression changes the Content-Length and Content-MD5 values of files. If your business logic relies on these values for verification, enable these features with caution.

-

If both HTML optimization and Gzip compression are enabled, the HTML optimization feature is ineffective. CDN only performs Gzip compression on the files.


-

Seamless migration: Zero-downtime domain switch
When you migrate an existing service from an OSS bucket domain to an accelerated domain name, adopt a phased approach to ensure service continuity and stability.


-

Preparation phase: Complete all configurations for the CDN-accelerated domain name and fully verify its functionality and performance in a test environment.

-

Phased release phase (recommended during off-peak hours): Use a phased release approach to switch a portion of your service traffic to the CDN-accelerated domain name. Gradually increase the traffic to reduce switching risks.

-

Verification phase: Closely monitor service access logs and error rates. Analyze key metrics such as response time and success rate to ensure that the phased release service is normal and the business is running smoothly.

-

Full release phase: After thorough verification, switch all service traffic to the CDN-accelerated domain name to complete the domain name migration.

-

Rollback plan: If you encounter any issues, have a plan to immediately roll back traffic to the original bucket domain. Analyze the root cause of the problem in detail before you redeploy.

#### Risk prevention


-

Protecting against hotlinking and unauthorized access: Configure Referer-based hotlink protection and URL signing
To prevent resources from being used by unauthorized sites, which can cause unnecessary traffic fees and bandwidth consumption, you must configure security protection policies.


-

Hotlink protection: For more information, see [Configure a Referer blacklist or whitelist](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection) to enable hotlink protection. This method validates the Referer field in the HTTP request header to prevent hotlinking, allowing access only from specified domains.

-

URL signing: When you enable private origin fetch for an OSS bucket, you grant CDN POPs direct access, bypassing OSS's native signature verification. This means that private resources can be publicly accessed through the CDN domain. To secure these resources, enable [URL signing](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-url-signing) on the CDN. This feature requires requests to include a unique signature and timestamp, preventing unauthorized downloads and distribution.

-

Ensuring origin connection security: Configure origin SNI and the origin host



Ensuring stable and secure communication between Alibaba Cloud CDN and OSS is key to ensuring service availability.


-

Configure origin SNI: CDN origin requests that do not include SNI (Server Name Indication) can cause access issues for OSS. To prevent this, you must [configure origin SNI](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-sni) in CDN and set it to the same value as the origin HOST. The origin HOST defaults to the accelerated domain name. When an origin request includes SNI, OSS can accurately identify the business domain name during the TLS handshake and return the matching certificate to protect the domain name. If OSS receives a request that does not include SNI, it cannot accurately identify the business domain name and can only return the default certificate. During the TLS handshake, all requests without SNI are treated as the same class, which can trigger stricter traffic limits and in turn disrupt normal access.

-

Hide origin information


By default, CDN uses the bucket domain name for origin fetch. When an origin fetch error occurs (for example, the file does not exist), the error message may expose the OSS bucket domain name, which poses a security risk.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p993900.png)


To hide the origin information and enhance security, follow these steps to change the origin host to the CDN-accelerated domain name:


-

On the [Buckets](https://oss.console.alibabacloud.com/bucket/) page, click the target bucket name. Then go to Bucket Settings > Domain Names, and map the accelerated domain name to the bucket.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0646278571/p993895.png)

-

In the [CDN console](https://cdnnext.console.aliyun.com/domain/list), click the target accelerated domain name. Then go to Origin Fetch > Default Origin Host, click Modify and change the Domain Name Type to Accelerated Domain Name.

-

Auditing and troubleshooting: Enable access logs
For security auditing, performance analysis, and troubleshooting in a production environment, you must enable comprehensive logging. For more information, see [Configure real-time log delivery](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-real-time-log-delivery) in the CDN console to send access logs to Simple Log Service (SLS). With SLS, you can perform in-depth analysis and set up alerts on key metrics, including access behavior and traffic distribution, popular resources and content, and error rates and request failures. This data is essential for optimizing performance and enhancing security.

## Billing


-

CDN fees: Configuring CDN to accelerate access to OSS incurs CDN traffic fees. For more information, see [CDN billing overview](https://www.alibabacloud.com/help/en/cdn/product-overview/billing-overview).

-

OSS fees: When a CDN cache miss occurs, the CDN POP retrieves the resource from OSS, which incurs origin traffic fees. For more information, see [OSS traffic fees](https://www.alibabacloud.com/help/en/oss/traffic-fees).

## FAQ

#### Why do `5xx` errors occur during CDN origin fetch?


A `5xx` error indicates that CDN failed to retrieve the resource from the OSS origin. Check the following aspects to troubleshoot the issue:


-

Origin configuration: Check whether the OSS origin address configured in the [CDN console](https://cdnnext.console.aliyun.com/) is correct.

-

Origin protocol policy: If CDN is configured for HTTPS origin fetch or [origin protocol policy](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-the-origin-protocol-policy), ensure that the origin supports HTTPS access and the SSL certificate is configured correctly.

-

Network link: Test the network connectivity from the CDN POP or your local machine to the OSS origin. CDN POPs are on the Internet, so the origin configured for CDN must be accessible over the Internet. If the origin IP address is not reachable from the Internet, the port is closed, or the origin domain name is not resolved, CDN origin requests to the origin server fail.

-

Origin server pressure: On the [CDN real-time monitoring](https://cdnnext.console.aliyun.com/monitor/realTime) page, check for a sudden increase in bandwidth and traffic. Many back-to-origin requests can cause excessive origin server pressure, which leads to back-to-origin response timeouts. For hot spot resources, perform [resource prefetch](https://www.alibabacloud.com/help/en/cdn/user-guide/refresh-and-prefetch-resources) and [set a reasonable cache period](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-the-cdn-cache-expiration-time) when the resources are published.

#### Why do I get a `403 Forbidden` or `You are forbidden to list buckets` error when accessing a static page accelerated by CDN?Cause analysis: This issue usually occurs after you enable CDN acceleration for a private bucket that is configured for static website hosting. The root cause is a conflict between two access mechanisms:


-

CDN private origin fetch: When CDN performs an origin fetch to OSS, it carries signature information for identity verification.

-

OSS static website hosting: Its default index page feature (for example, automatically returning `index.html` when accessing `/`) requires that access requests must be anonymous.


When a user accesses the root directory of the accelerated domain name, CDN initiates a signed request to access the bucket's root directory. When OSS receives this signed request, it does not trigger the static website hosting logic because the request is not anonymous. Instead, it attempts to perform a `ListObjects` (list files) operation. Because access policies usually prohibit this type of operation, a `403 Forbidden` error is returned.


Solution: Bypass the static website hosting feature of OSS and achieve the same result by [configuring URL rewrite rules](https://www.alibabacloud.com/help/en/cdn/user-guide/create-an-access-url-rewrite-rule) directly on the CDN.


-

Path To Rewrite: `^/$` (matches root directory access)

-

Target Path: `/index.html` (or the actual file name of the index page)

-

Execution Rule: Select Redirect

#### Can I upload files to OSS through a CDN domain name?


For security reasons, do not upload files to OSS through a CDN domain name. If your CDN allows write methods (such as PUT and POST), anyone can upload files to OSS through CDN without identity verification or authorization. This makes your service vulnerable to malicious uploads and data tampering attacks. To follow the principle of least privilege, upload files using the OSS domain name.

#### Will OSS outbound traffic decrease after using CDN acceleration?


Yes, it will. When requests are served from the CDN cache instead of your OSS bucket, it reduces your OSS outbound traffic. This is most effective for frequently accessed content, such as popular images, downloads, or website assets.


Frequent hits on CDN cache files occur in business scenarios where specific data is accessed repeatedly, such as website access, image file downloads, and game distribution. A higher cache hit ratio results in lower back-to-origin traffic and greater cost savings.

#### How can I count the actual number of times a file is accessed?


After CDN acceleration is enabled, OSS access logs cannot record end-user access requests that are directly served by the CDN cache. You can count the actual number of file accesses in the following ways:


-

Log data within 30 days: You can download the CDN [offline logs](https://www.alibabacloud.com/help/en/cdn/user-guide/download-logs) to view and analyze them.

-

Log data older than 30 days: After you [configure real-time log delivery](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-real-time-log-delivery) in CDN, you can view and analyze the data on the [CDN Data Statistics](https://cdnnext.console.aliyun.com/log/realtime/pushData) page.


Thank you! We've received your  feedback.