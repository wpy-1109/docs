# Overview of access domains and network connectivity

OSS provides a variety of network access solutions that cover domain configuration, performance optimization, security protection, and proxy access. You can use these features to build an efficient, stable, and secure storage access architecture.

## Domain selection


You can access your data using either bucket domain names or custom domain names, depending on your use case.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Due to a [policy change](https://www.alibabacloud.com/en/notice/oss_update_notice_policy_change_in_calling_data_api_operations_via_the_default_public_domain_name_45a) to improve compliance and security, starting March 20, 2025, new OSS users must [use a custom domain name](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names) (CNAME) to perform data API operations on OSS buckets located in Chinese mainland regions. Default public endpoints are restricted for these operations. Refer to the [official announcement](https://www.alibabacloud.com/en/notice/oss_update_notice_policy_change_in_calling_data_api_operations_via_the_default_public_domain_name_45a) for a complete list of the affected operations. If you access your data via HTTPS, you must [bind a valid SSL Certificate](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-by-https-protocol) to your custom domain. This is mandatory for OSS Console access, as the console enforces HTTPS.














(https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-via-bucket-domain-name)





-



-



-




-



-



-




(https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names)





-



-



-




-



-




| Domain Name Type | Description | Pros | Cons |
| --- | --- | --- | --- |
| Bucket domain name | Default domain name for OSS | Ready to use: Available immediately after bucket creation, with no need to wait for DNS resolution configuration.Full-featured: Supports multiple access modes, including Internet, internal network, and transfer acceleration.Maintenance-free: OSS manages and updates the domain name and its SSL certificate. | Browser behavior: When you access objects such as HTML files or images, the browser forces a download instead of displaying them online.Lacks brand identity: The URL contains the .aliyuncs.com suffix and does not reflect your corporate brand.Long URL: Difficult to remember, share, and promote. |
| Custom domain name | Your own domain name, mapped to a CNAME domain (recommended) or to a bucket domain that supports Internet access, to deliver a branded access experience. | Brand consistency: Use your own domain name, such as example.com, to maintain a consistent brand identity.Flexible architecture: The URL remains unchanged even if you switch the underlying storage service, which reduces migration costs.SEO-friendly: Beneficial for search engine optimization and improving your website's authority. | Operational overhead: You manage DNS resolution and SSL certificate renewals.ICP filing requirement: When you map a domain name to a bucket in the Chinese mainland, your domain name must have an ICP filing. |


## Performance optimization

### CDN acceleration


You can configure [Alibaba Cloud CDN (CDN)](https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration) to distribute static assets such as images, videos, and documents from your OSS buckets. This service uses a global network of edge nodes to serve user requests from the nearest point of presence. This significantly improves access speed, reduces network latency, and helps control costs by minimizing direct traffic to OSS.

### Transfer acceleration


For long-distance, cross-region data transfers, such as accessing a bucket in an overseas region from the Chinese mainland or vice versa, enabling [transfer acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration) significantly boosts performance. Transfer acceleration uses Alibaba Cloud's globally distributed data centers and intelligent routing to route user requests to the nearest access point, which accelerates both uploads and downloads from end to end.

## Security enhancement

### HTTPS Security Protocol


The HTTP protocol transmits data in plaintext. This creates risks of data leaks and tampering, and often fails to meet corporate data protection or compliance requirements. You can configure an SSL certificate to [enable HTTPS access to OSS](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-by-https-protocol) to achieve end-to-end encryption for data in transit. This prevents security threats such as man-in-the-middle attacks and data eavesdropping, and helps you meet the strict compliance standards of industries such as finance and healthcare.

### Private connection with PrivateLink


[PrivateLink](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-via-privatelink-network) establishes a dedicated, private connection between your Virtual Private Cloud (VPC) and OSS, which provides traffic isolation at the network layer. This solution eliminates the security risks of data transmission over the public network, prevents potential network address conflicts, and simplifies O&M complexity. This lets you build a secure and controllable cloud storage access architecture that meets  requirements.

## Proxy access

### Reverse proxy on an ECS instance


OSS relies on DNS to resolve its service endpoints to a dynamic set of IP addresses. Consequently, you may encounter access restrictions or failures when you configure firewall allowlists or integrate with systems that require a fixed IP address. To address this issue, you can [configure a reverse proxy](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-through-ecs-reverse-proxy) on an Elastic Compute Service (ECS) instance with a dedicated static public IP. Forwarding requests through this instance ensures that all access to your resources originates from a single, stable IP address.

## FAQ

### How do I generate a long-lived, unsigned URL to access an OSS object?


You can generate a long-lived, unsigned URL in two ways:


-

[Set the object to public-read](https://www.alibabacloud.com/help/en/oss/user-guide/object-acl#concept-blw-yqm-2gb): Anyone can access the object without restriction. To prevent malicious hotlinking and unexpected charges, configure [hotlink protection](https://www.alibabacloud.com/help/en/oss/user-guide/hotlink-protection) in OSS to restrict allowed referrers.

-

[Use CDN to access OSS](https://www.alibabacloud.com/help/en/cdn/use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console): Keep the object permissions private and enable the private bucket origin fetch feature of CDN to provide public-read access. CDN delivers better access performance and caching. To prevent hotlinking, configure [hotlink protection](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection) at the CDN layer.

### Which ports does OSS support?


-

Port 80: HTTP protocol

-

Port 443: HTTPS protocol

-

Port 1935: RTMP ingest (used only for RTMP ingest)

### My OSS upload or download is slow. How do I fix it?


OSS transfer speed depends on client bandwidth, network path quality, and transfer settings.


-

General troubleshooting: First, confirm that your current bandwidth usage has not reached the bucket’s [bandwidth limit](https://www.alibabacloud.com/help/en/oss/user-guide/limits). Next, [use the MTR tool to analyze your network path](https://www.alibabacloud.com/help/en/ecs/user-guide/use-mtr-tool-for-network-analysis#fb02c53042ekt) for packet loss, high latency, or routing anomalies. For cross-border or long-distance transfers, it is strongly recommended that you [enable transfer acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/transfer-acceleration#section-gtt-hyd-vba) to optimize the network path.

-

Tool optimization: Use [ossutil 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/) to transfer large or numerous files. Run the `probe` command to check your current network status.

-

SDK optimization: For large files, always use [multipart upload](https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload) and [resumable upload](https://www.alibabacloud.com/help/en/oss/user-guide/resumable-upload). Set appropriate values for part_size and `num_threads`. When network conditions are good, increase `part_size` to reduce the number of requests. Also, disable CRC64 checksums during SDK initialization, for example, set `enable_crc=False` in Python, and add `Content-MD5` to request headers for data integrity verification. This improves performance while it maintains data security.

### How do I troubleshoot network errors such as DNS resolution failure or connection timeout?


If OSS returns a response, retrieve the [Request ID](https://www.alibabacloud.com/help/en/oss/user-guide/obtain-request-ids) and run the [OSS self-diagnostic tool](https://oss.console.alibabacloud.com/tools/diagnose) to identify the issue.


If the request fails before it reaches OSS, and the `Request ID` is empty, follow these steps:


-

Connection refused: This error usually indicates that the client and OSS are in the same region but the port is blocked, or you used an internal endpoint across regions. Verify that you are using the correct public endpoint. Then, use `ping` and `telnet` to test firewall rules and network connectivity.

-

ConnectionTimeout: This error typically occurs due to poor network conditions or short timeout settings. Increase the connection and read timeout values in your SDK and enable retry logic. For large file transfers, use [multipart upload](https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload) and [resumable upload](https://www.alibabacloud.com/help/en/oss/user-guide/resumable-upload) to improve stability. If the issue is network-related, consider using CDN or OSS transfer acceleration.

-

Socket timeout or Socket closed: The connection to OSS timed out or was closed unexpectedly. Increase the socket timeout value in your SDK. For example, use the `ClientConfiguration.setSocketTimeout` method in the Java SDK.

-

Connection reset: A connection reset can have many causes, such as incorrect endpoint configuration or security-based access restrictions on the bucket. Troubleshoot the issue step by step:


-

Use `ping` or the [Ali Kunlun diagnostic tool](https://cdn.dns-detect.alicdn.com/https/doc.html) to verify client network connectivity.

-

Confirm that the endpoint in your code is correct and includes the proper protocol prefix (`http://` or `https://`).

-

Confirm that the bucket is not in [OSS sandbox](https://www.alibabacloud.com/help/en/oss/user-guide/oss-sandbox) mode due to security attacks or policy violations.

-

If the issue persists, capture packets using Wireshark and contact technical support for further analysis.

Thank you! We've received your  feedback.