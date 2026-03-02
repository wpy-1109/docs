# How OSS DDoS protection works and how to configure it

Object Storage Service (OSS) DDoS protection is a proxy-based service that mitigates DDoS attacks by integrating OSS with Anti-DDoS Pro and Anti-DDoS Premium. When a protected bucket is under a volumetric attack, OSS DDoS protection diverts the attack traffic to an Anti-DDoS instance for scrubbing. The service then redirects non-malicious traffic to the destination bucket to ensure business continuity.

## Scenarios


DDoS attacks are one of the most harmful types of attacks against enterprises. When an enterprise experiences a DDoS attack, its services may be interrupted. This can damage the corporate image, cause customer churn, and lead to financial loss, all of which severely affect business operations.


To mitigate these problems, OSS is deeply integrated with [Anti-DDoS Pro and Anti-DDoS Premium](https://www.alibabacloud.com/help/en/anti-ddos/anti-ddos-pro-and-premium/product-overview/what-are-anti-ddos-pro-and-anti-ddos-premium#concept-2417452). This integration provides a DDoS mitigation capability of hundreds of Gbps, protection for millions of queries per second (QPS), and attack switching in seconds. These features can effectively defend against DDoS flood attacks of hundreds of Gbps and other attacks, such as SYN Flood, ACK Flood, ICMP Flood, UDP Flood, NTP Flood, SSDP Flood, DNS Flood, and HTTP Flood. This ensures that your services remain available during an attack.

## Usage notes


-

OSS DDoS protection does not handle low-volume fraudulent traffic that mimics normal requests. To prevent this type of traffic, you can configure access control using policies or access control lists (ACLs), or configure Web Application Firewall (WAF) protection. For more information, see [How do I prevent fraudulent traffic from accessing OSS?](https://www.alibabacloud.com/help/en/oss/how-to-prevent-high-qps-and-traffic-generated-by-unauthorized-access).

-

OSS DDoS protection cannot effectively mitigate medium-scale CC attacks.

## How it works


The following figure shows how OSS DDoS protection works.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/6880422771/CAEQFhiBgID.l6_56RgiIDI2ZTdmOTc1ZDQ5ODQ5ZjRhOTE1OThiMDJkMDMwYzZj3963382_20230830144006.372.svg)

By default, OSS uses [Anti-DDoS Origin](https://www.alibabacloud.com/help/en/anti-ddos/anti-ddos-origin/product-overview/what-is-anti-ddos-origin#concept-63643-zh) to protect your buckets. However, if the attack traffic exceeds the protection threshold of Anti-DDoS Origin, the service cannot provide effective protection. This may disrupt access to your buckets.


After you enable OSS DDoS protection, if the attack traffic exceeds the protection threshold of Anti-DDoS Origin, OSS automatically diverts all traffic destined for the attacked bucket to an Anti-DDoS instance. Malicious traffic is scrubbed and filtered in scrubbing centers. Non-malicious traffic is then forwarded to the destination bucket through port and protocol forwarding. This ensures stable access to the bucket during an attack.


After the attack ends, traffic to the bucket is switched back to Anti-DDoS Origin for protection.

## Limits


-

OSS DDoS protection is supported in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Shenzhen), and China (Hong Kong).

-

OSS DDoS protection protects only the public endpoints of buckets, such as `oss-cn-hangzhou.aliyuncs.com`. It does not protect the following types of domain names:


-

Acceleration endpoints, such as `oss-accelerate.aliyuncs.com` and `oss-accelerate-overseas.aliyuncs.com`

-

Access point endpoints, such as `ap-01-3b00521f653d2b3223680ec39dbbe2-ossalias.oss-cn-hangzhou.aliyuncs.com`

-

Object FC Access Point endpoints, such as `fc-ap-01-3b00521f653d2b3223680ec39dbbe2-opapalias.oss-cn-hangzhou.aliyuncs.com`

-

Endpoints accessed over IPv6, such as `cn-hangzhou.oss.aliyuncs.com`

-

Amazon S3 endpoints, such as `s3.oss-cn-hongkong.aliyuncs.com`

-

An Anti-DDoS instance has a minimum usage period of seven days after it is created. If you delete the instance within this period, you are charged the basic resource fee for the remainder of the seven-day period. For more information about billing, see [DDoS protection fees](https://www.alibabacloud.com/help/en/oss/oss-ddos-protection-fees#concept-2025393).

-

You can create only one Anti-DDoS instance in a region. Each instance can be attached to a maximum of 10 buckets in the same region.

-

After you attach a bucket to an Anti-DDoS instance, you cannot preview resources in the bucket using a browser. In addition, OSS does not protect custom domain names that are associated with the bucket by default. Therefore, when the bucket is under attack, you cannot access it using the custom domain names. If you want to access the bucket using a custom domain name during an attack, you must add the custom domain name to the protection list in the OSS DDoS protection console. You can add a maximum of five custom domain names to the protection list for each bucket.


If a custom domain name that you want to protect for the bucket (such as `www.example.com`) matches an exact domain name (such as `www.example.com`) or a wildcard domain name (such as `*.example.com`) that is configured in a forwarding rule of Anti-DDoS Pro and Anti-DDoS Premium, you must go to the [Anti-DDoS Pro console](https://yundun.console.alibabacloud.com/?p=ddoscoo) and detach the exact or wildcard domain name. Otherwise, you cannot access OSS through the custom domain name when the bucket is under attack.


For more information about forwarding rules for exact or wildcard domain names, see [Add a website configuration](https://www.alibabacloud.com/help/en/anti-ddos/anti-ddos-pro-and-premium/user-guide/add-websites#task-2325689).

## Use the OSS console


-

Create an Anti-DDoS instance.


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the navigation pane on the left, choose Data Service > Anti-DDoS Pro.

-

Optional: If this is the first time you are using OSS DDoS protection, on the Anti-DDoS Pro page, click Activate Now.

-

On the Anti-DDoS Pro page, click Create Anti-DDoS Instance and then select a Region.

-

Click OK.

-

Attach a bucket.


-

In the Actions column of the destination instance, click View and Attach Buckets.

-

In the View and Attach Buckets panel, click Attach Protected Buckets.

-

In the Attach Protected Buckets dialog box, from the Bucket drop-down list, select the bucket that you want to attach.


Buckets that are already attached to an Anti-DDoS instance do not appear in the Protected Bucket drop-down list.

-

Click OK.


After you attach the bucket, its status is Initializing. When the status changes to Protecting, the Anti-DDoS instance starts protecting the bucket's domain name.

-

To protect custom domain names, add the custom domain names to the protection list.


> NOTE:

> NOTE: 


> NOTE: Important 

OSS does not protect custom domain names that are associated with a bucket by default. Therefore, you cannot access the bucket using its custom domain names during an attack. If you want to access the bucket using its custom domain names during an attack, you must add the custom domain names to the protection list. You can add a maximum of five custom domain names to the protection list for each bucket. The custom domain names can belong to a maximum of four different sites. For example, `a.mycname.com` and `b.mycname.com` belong to the same site, but `c.othercname.com` belongs to a different site.


-

If a custom domain name is not attached to the bucket, you must first attach one. For more information, see [Attach a custom domain name](https://www.alibabacloud.com/help/en/oss/manage-a-domain-map-custom-domain-names#concept-ozw-m2r-5fb).

-

If a custom domain name is already attached to the bucket, perform the following steps to add the custom domain name to the protection list:


-

In the Actions column of the protected bucket, click Modify Custom Domain Name.

-

Select the custom domain names that you want to protect.

-

Click OK.


The Anti-DDoS instance starts protecting the selected custom domain names.


Thank you! We've received your  feedback.