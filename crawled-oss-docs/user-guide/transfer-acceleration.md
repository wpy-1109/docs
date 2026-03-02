# Access OSS using transfer acceleration

When transferring data over long distances, transfer acceleration uses globally distributed cloud data centers and intelligent routing to provide an end-to-end acceleration solution for uploads and downloads. It optimizes for high latency and unstable transmission during cross-region access, improving transfer speed and user experience.

## How it works


When you access a bucket through an acceleration endpoint, the system intelligently routes your request to the nearest Alibaba Cloud access point. Data then travels at high speed over Alibaba Cloud’s internal backbone network to the region where the target bucket resides. This avoids long-distance transmission over the public internet.


For example, if a user in Beijing accesses a bucket in Chengdu. Using a standard public endpoint, the request must traverse multiple hops across the public internet. With transfer acceleration, the request enters Alibaba Cloud’s network at a local access point in Beijing and travels directly to Chengdu via the internal backbone network. This reduces the public internet transmission distance and improves speed and stability.


> NOTE:

> NOTE: 


> NOTE: Note 

Transfer acceleration improves speed and stability by optimizing the transmission path, but it cannot fully eliminate the effects of public internet fluctuations or cross-border network instability. Actual performance depends on factors such as the user’s location, ISP link quality, and network congestion. This is especially noticeable in cross-border scenarios.


## Enable access through transfer acceleration

### Step 1: Enable transfer acceleration


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the target bucket.

-

In the left navigation pane, click Bucket Settings > Transfer Acceleration.

-

Click the toggle next to Transfer Acceleration. Read the prompt in the dialog box carefully, then click OK.


> NOTE:

> NOTE: 


> NOTE: Note 

It takes about 30 minutes for transfer acceleration to take effect globally. Wait until it is fully active before running verification tests.


After enabling transfer acceleration, your bucket’s original endpoints (such as the public endpoint) remain fully functional. Your application can choose the optimal access method based on user location and network conditions.

### Step 2: Use the acceleration endpoint to access OSS


To benefit from acceleration, replace the endpoint in your request with the acceleration endpoint (`oss-accelerate.aliyuncs.com`).


> NOTE:

> NOTE: 


> NOTE: Note 

Domains without ICP filing cannot resolve to IP addresses in the Chinese mainland. If you want to use a custom domain without ICP filing and enable transfer acceleration via CNAME, you must point the CNAME to the acceleration endpoint for regions outside the Chinese mainland (`oss-accelerate-overseas.aliyuncs.com`).


## Public-read and public-read-write buckets


You can access objects directly through a URL in your browser. For example, `https://example-bucket.oss-accelerate.aliyuncs.com/example.jpg` accesses the file `example.jpg` in the bucket `example-bucket`.

## Private buckets


To access a private bucket, include signature information in the object URL. The following steps show how to obtain a signed URL from the console. For details on signatures and how to generate them, see [Signature Version 4 (recommended)](https://www.alibabacloud.com/help/en/oss/developer-reference/add-signatures-to-urls).


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the target bucket.

-

In the Actions column for the target object, click Details.

-

Click Copy Object URL and replace the public endpoint in the URL (for example, `oss-cn-hangzhou.aliyuncs.com`) with the acceleration endpoint (`oss-accelerate.aliyuncs.com`).

-

You can access the modified URL in your browser.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

When using SDKs, ossutil, ossbrowser, or other tools to access OSS, set the endpoint to `oss-accelerate.aliyuncs.com`. Do not include the bucket name. If you mistakenly configure the endpoint as `<BucketName>.oss-accelerate.aliyuncs.com`, domain resolution will fail.


## Test acceleration performance


The following test compares download speeds from a bucket in the China (Hangzhou) region to an ECS instance in the Japan (Tokyo) region using [ossutil](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/) to verify the real-world impact of transfer acceleration.

## Without acceleration


`shell
ossutil cp oss://example-bucket/ossutil-2.1.2-mac-arm64.zip ossutil-2.1.2-mac-arm64.zip -e oss-cn-hangzhou.aliyuncs.com
`


Download time:


`shell
Success: Total 1 object, size 9281195 B, Download done:(1 files, 9281195 B), avg 8.733 MiB/s

1.013983(s) elapsed
`


## Enable Acceleration


`shell
ossutil cp oss://example-bucket/ossutil-2.1.2-mac-arm64.zip ossutil-2.1.2-mac-arm64.zip -e oss-accelerate.aliyuncs.com
`


Download time:


`shell
Success: Total 1 object, size 9281195 B, Download done:(1 files, 9281195 B), avg 20.155 MiB/s

0.440160(s) elapsed
`


## Apply in production

#### Best practices


-

Combine CDN with transfer acceleration: A multilayer acceleration architecture


You can enable both [CDN acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration) and transfer acceleration. Configure your CDN origin to point to the acceleration endpoint to build a dual-layer system: “CDN edge caching + OSS transfer acceleration.” CDN serves requests from the nearest cache, while transfer acceleration optimizes the CDN’s origin-fetch path. This setup is ideal for globally distributed static resources and delivers full-path optimization for both cache hits and origin fetches.

-

Optimize large file transfers: Combine multipart operations with acceleration


For gigabyte- or terabyte-scale file transfers, combine transfer acceleration with [multipart upload](https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload) and [resumable download](https://www.alibabacloud.com/help/en/oss/user-guide/oss-resumable-download) to create a complete long-distance large-file transfer solution. Transfer acceleration improves network path quality, while multipart operations increase concurrency and fault tolerance. Together, they significantly reduce timeout risk and boost overall transfer efficiency.

-

Cost Optimization: An Intelligent Strategy for Domain Name Selection


You can apply different endpoint strategies based on user groups and access scenarios. For users in the same region or with good network conditions, use the public endpoint to avoid transfer acceleration costs. For cross-region users or those with poor network quality, use the acceleration endpoint to improve their experience. Build your endpoint strategy based on user geography, business criticality, and cost budget.

#### Fault tolerance strategies


-

Domain Name Downgrade Mechanism


If the acceleration endpoint becomes unavailable, your application should automatically fall back to the public endpoint to ensure business continuity. Transfer acceleration and the public endpoint operate independently—failure in one does not affect the other. This provides dual protection for your service.

## Quotas and limitations








| Limitation | Description |
| --- | --- |
| Protocol support | The acceleration endpoint supports API access only over HTTP and HTTPS. Non-HTTP/HTTPS protocols such as RTMP are not supported. |
| Effective time | Enabling or disabling transfer acceleration takes about 30 minutes to take effect globally. |
| Access mode | The acceleration endpoint supports only third-level domain access that includes the bucket name. It cannot be used for management operations such as listing buckets. Use the public endpoint for all management operations. |
| Secure transmission | The backend may use HTTPS for internal data transmission. If a client accesses data over HTTP, the access log might still show HTTPS. |


## Billing


Enabling transfer acceleration is free. You only incur charges for accelerated upload traffic and accelerated download traffic when you access OSS through the acceleration endpoint. For details, see [Transfer acceleration fees](https://www.alibabacloud.com/help/en/oss/transfer-acceleration-fees).

## FAQ

### What should I do if I get a `502` or `504` error when accessing through the acceleration endpoint?


This is usually normal behavior, caused by OSS transfer acceleration’s automatic path switching mechanism. To handle network fluctuations and changing link quality during long-distance transfers, the service dynamically selects the best transmission path. During path switches, a small number of requests may be interrupted and return `502/504` errors. This situation cannot be fully avoided. You should implement exponential backoff retry logic in your client code to improve success rates.

### Why don’t I see acceleration after enabling the feature?


After enabling transfer acceleration, you must also replace the endpoint in your request with the acceleration endpoint (`oss-accelerate.aliyuncs.com`) to obtain the benefit. If you keep using the standard public endpoint, acceleration will not apply.

### Why do I get errors immediately after enabling transfer acceleration?


It takes about 30 minutes for transfer acceleration to take effect globally. If you try to use the acceleration endpoint right after enabling it, you may receive errors because the change has not propagated yet. You should wait and retry after some time.

### Why is cross-border access still slow even with the acceleration endpoint?


Transfer acceleration improves cross-region access by optimizing the transmission path, but actual performance in cross-border scenarios depends on ISP link quality. Speed may drop if cross-border links become congested or unstable. We recommend:


-

You should verify that your endpoint is correctly configured as `oss-accelerate.aliyuncs.com`. Do not include the bucket name.

-

For large files, you can combine [multipart upload](https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload) and [resumable download](https://www.alibabacloud.com/help/en/oss/user-guide/oss-resumable-download) to improve reliability.

-

You should implement an endpoint fallback mechanism in your application layer to automatically switch to the public endpoint if the acceleration endpoint becomes unstable. This ensures business continuity.

### How is transfer acceleration billed? Is it added on top of public internet traffic fees?


Transfer acceleration fees are billed separately from public internet outbound traffic fees.


-

When you use the acceleration endpoint, you incur both transfer acceleration traffic fees and public internet outbound traffic fees.

-

When you use the standard public endpoint, you only pay for public internet outbound traffic—no transfer acceleration fees apply.


Enabling the transfer acceleration feature itself is free. Charges apply only when you actually transfer data through the acceleration endpoint.


Thank you! We've received your  feedback.