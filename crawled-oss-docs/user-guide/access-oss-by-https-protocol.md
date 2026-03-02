# Access OSS over HTTPS

Accessing Object Storage Service (OSS) resources over HTTP is insecure because it transmits data in plaintext. This practice exposes your data to significant security risks, such as interception and man-in-the-middle attacks, and may fail to meet data protection and compliance requirements 1. To protect your data, enable HTTPS by configuring an SSL certificate. HTTPS encrypts data in transit, ensuring data confidentiality and integrity.

## How it works


To enable HTTPS for OSS, you must configure a valid SSL certificate for a specific domain name in the correct location. HTTPS uses the TLS/SSL protocol to encrypt HTTP data packets from end to end. It also uses a certificate chain to verify the server's identity, ensuring the confidentiality, integrity, and authentication of data during transmission.


The location where you configure the SSL certificate depends on the domain name type you use. The specific configuration methods are as follows:


-

Bucket domain name


For example, `example.oss-cn-hangzhou.aliyuncs.com`. Alibaba Cloud manages and maintains the SSL certificates for these domain names. They natively support HTTPS, requiring no configuration. You can achieve secure access simply by using the `https://` prefix, which simplifies certificate management.

-

Custom domain name


When using a custom domain name to access OSS, the SSL certificate configuration location depends on whether CDN acceleration is enabled. This design ensures that the certificate configuration aligns with the traffic path.


-

CDN is not enabled: Traffic accesses OSS directly. You must configure certificate hosting for the mapped custom domain name in the OSS console. For more information, see [Enable HTTPS access by configuring certificate hosting in OSS].

-

CDN is enabled: Traffic passes through CDN points of presence (POPs) before it is forwarded to OSS. You must configure an HTTPS certificate for the CDN-accelerated domain name in the CDN console. For more information, see [Enable HTTPS access by configuring an HTTPS certificate in CDN].


How do I determine whether CDN acceleration is enabled?


To avoid configuration errors, first determine if CDN acceleration is enabled for your custom domain name. This ensures you configure the SSL certificate in the correct location. Use one of the following methods:


-

Method 1: Use the OSS console


Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the target bucket, and then in the left-side navigation pane, click Bucket Settings > Domain Names. The domain list shows all configured CDN-accelerated domain names for the bucket. The HTTPS certificates for these domains must be managed in the Alibaba Cloud CDN console.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p1010478.png)

-

Method 2: Use the CDN console


Go to the [CDN Domain Name List](https://cdn.console.alibabacloud.com/domain/list) page to view the configured and active CDN-accelerated domain names and their origin bucket information. This method lets you directly check the CDN acceleration status and origin configuration details for your domains.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p1010671.png)

## Enable HTTPS access by configuring certificate hosting in OSS


This section shows how to enable secure HTTPS access for a custom domain name mapped to a bucket. HTTPS encrypts data in transit and provides authentication to secure access.
Before you begin, make sure that you have [mapped a custom domain name to an OSS bucket](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names). You must also have a valid SSL Certificate that matches the domain name in SSL Certificates Service. You can obtain a certificate by [purchasing a new certificate](https://www.aliyun.com/product/cas), [applying for a free certificate](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/free), or [uploading a third-party certificate](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/upload).
#### Step 1: Configure certificate hosting


Host an SSL Certificate in OSS to enable HTTPS encrypted access for a custom domain name.


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page. Click the target bucket. In the left-side navigation pane, click Bucket Settings > Domain Names.

-

In the Actions column for the target custom domain name, click Certificate Hosting. Select a certificate from the Certificate Name drop-down list. If you cannot select the desired certificate, go to the [SSL Certificate Management](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/buy) page and make sure that the certificate meets the following conditions:


-

The certificate is issued and valid.

-

The certificate is valid for the domain name that you are configuring.

-

Click Upload Certificate to finish configuring certificate hosting.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996557.png)

#### Step 2: Verify HTTPS access


After configuring Certificate Hosting and allowing time for it to take effect, verify the setup by accessing a resource in a browser. A successful configuration ensures secure, encrypted data transmission.


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the Actions column of the object file you want to access, click View Details.

-

Set Domain Name to Custom Domain Name. From the drop-down list, select the mapped custom domain name. Then, click Copy Object URL.

-

Access the URL in a browser to verify the HTTPS encrypted access. The browser's address bar should display a lock icon, which indicates that the connection is encrypted.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996895.png)

## Enable HTTPS access by configuring an HTTPS certificate in CDN


Enable secure HTTPS access for a custom domain name that has CDN acceleration enabled. This ensures secure data transmission while providing acceleration through CDN's global POPs.
Before you begin, make sure that you have [configured CDN acceleration for an OSS bucket](https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration) and are using the accelerated domain name as the endpoint. You must also have a valid SSL Certificate that matches the domain name in SSL Certificates Service. You can obtain a certificate by [purchasing a new certificate](https://www.aliyun.com/product/cas) or [applying for a free certificate](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/free). You can also [upload a third-party certificate](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/upload) or directly enter the third-party certificate content and private key in the following steps.
#### Step 1: Configure the CDN HTTPS certificate


Configure an SSL Certificate for the accelerated domain name in the CDN console to enable HTTPS secure acceleration.


-

Go to the [CDN console](https://cdn.console.alibabacloud.com/domain/list). Click the target accelerated domain name. Click HTTPS. Next to HTTPS Certificate, click Modify.

-

Select HTTPS Secure Acceleration. Read the billing reminder and click OK.

-

Based on the Certificate Source drop-down list, select an SSL Certificate or enter third-party certificate information.


-

SSL Certificates Service: From the Certificate Name drop-down list, select a certificate. If you cannot select the target certificate, go to the [SSL Certificate Management](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/buy) page and make sure the certificate meets the following conditions:


-

The certificate has been issued and is within its validity period.

-

The certificate is valid for the domain name that you are configuring.

-

Custom Certificate (Certificate + Private Key): Enter the Certificate Name, Certificate (Public Key), and Private Key.

-

Click OK to complete the HTTPS certificate configuration.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996491.png)

#### Step 2: Verify CDN HTTPS access


The HTTPS configuration for an accelerated domain name takes about one minute to deploy. After the configuration takes effect, verify it by accessing an OSS resource over HTTPS in a browser (for example, `https://example.com/dest.jpg`, where `example.com` is your accelerated domain name). A successful visit displays a lock icon in the browser's address bar, indicating that the data transmission is encrypted.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996685.png)

## Apply in production


In a production environment, your HTTPS configuration must account for security, reliability, and performance. Sound configuration strategies and risk mitigation measures ensure your services operate continuously and stably.

#### Best practices


-

Force HTTPS access: Configure an access control policy


In production, we recommend enforcing HTTPS for all clients. This prevents data from being intercepted or tampered with during transmission and helps you meet data protection compliance requirements.


-

For custom domain names, deny all HTTP requests by configuring a [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/).


Configuration example


Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page. Click the target bucket. In the navigation pane on the left, click Access Control > Bucket Policy. Select Add by Syntax to add the following bucket policy.
When adding the policy, replace bucketname in the sample configuration with your bucket name.

`json
{
	"Version": "1",
	"Statement": [{
		"Effect": "Deny",
		"Action": [
			"oss:*"
		],
		"Principal": [
			"*"
		],
		"Resource": [
			"acs:oss:*:*:bucketname",
			"acs:oss:*:*:bucketname/*"
		],
		"Condition": {
			"Bool": {
				"acs:SecureTransport": [
					"false"
				]
			}
		}
	}]
}
`


After you configure the bucket policy, all HTTP requests are denied.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996951.png)

-

For CDN-accelerated domain names, configure a [force redirect](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-url-redirection) or [enable HTTP Strict Transport Security (HSTS)](https://www.alibabacloud.com/help/en/cdn/user-guide/configure-hsts) to force clients to use HTTPS, enhancing the overall security level.


Configuration example


-

Configure a force redirect


Go to the [CDN console](https://cdn.console.alibabacloud.com/domain/list) page. Click the target accelerated domain name. Click HTTPS, and then next to HTTP/S Redirect, click Modify. Configure the redirection as shown in the following figure. After the configuration is complete, CDN uses a 301 redirect to change HTTP requests from clients to CDN nodes into HTTPS requests.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996730.png)

-

Enable HSTS


Go to the [CDN console](https://cdn.console.alibabacloud.com/domain/list) page. Click the target accelerated domain name. Click HTTPS, and then next to HSTS, click Modify. Enable HSTS as shown in the following figure. After the configuration is complete, client HTTP requests are forcibly converted to HTTPS requests.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996732.png)

-

Automatic renewal: Manage the certificate lifecycle


SSL certificates have a fixed validity period. An expired certificate will cause service interruptions and business losses. Monitor certificate expiration and set up alerts. Renew certificates 30 days in advance to allow sufficient time for testing and deployment. For Alibaba Cloud SSL certificates, [enable certificate hosting](https://www.alibabacloud.com/help/en/ssl-certificate/enable-certificate-hosting) reduces manual intervention. For third-party certificates, establish a regular update process and designate responsible personnel to ensure business continuity.

-

Performance optimization: Enable HTTP/2 and compression


Modern browsers and CDNs widely support the HTTP/2 protocol, which offers technical advantages over HTTP/1.1, such as multiplexing, header compression, and server push. These features significantly improve page load speeds. In your CDN configuration, enable the [HTTP/2 protocol](https://www.alibabacloud.com/help/en/cdn/user-guide/enable-http-or-2) and [Gzip compression](https://www.alibabacloud.com/help/en/cdn/user-guide/use-the-gzip-compression-feature) to optimize transmission efficiency, reduce bandwidth consumption, and improve user experience.

#### Risk mitigation


-

Certificate failure contingency: Establish a backup certificate mechanism


Prepare a backup SSL certificate for unexpected events, such as primary certificate failure, accidental deletion, or CA-related issues. For critical business systems, use certificates from multiple Certificate Authorities (CAs) as backups. If the primary certificate fails, quickly switch to a backup to minimize service downtime and ensure business continuity.

-

Access downgrade policy: Revert to HTTP in emergencies


Although HTTPS is a best practice, have an emergency plan to revert to HTTP if a severe, unresolvable certificate issue occurs. Have a standard emergency response procedure and an operations manual to temporarily allow HTTP access during troubleshooting. Enhance monitoring and logging to ensure prompt problem detection and quick service restoration.

## OSS root certificate upgrade


The root certificate is the foundation of the SSL/TLS trust chain and is used to verify the trustworthiness of server certificates. Browsers and operating systems have built-in root certificate stores. A server certificate is considered secure only when it is signed by a trusted root certificate.

#### Background


To ensure a continuously reliable network security environment, Mozilla implemented a new root certificate trust policy in early 2023. According to this policy, any root certificate used for server authentication with an issuance date of more than 15 years will no longer be trusted by Mozilla. Affected by this policy, GlobalSign issued a root certificate upgrade notice, stating that the GlobalSign Root R1 root certificate became invalid starting April 15, 2025. For more information, see [Mozilla's notice on updating the root certificate trust policy](https://wiki.mozilla.org/CA/Root_CA_Lifecycles) and [GlobalSign's root certificate upgrade notice](https://support.globalsign.com/ssl/general-ssl/removal-tls-trust-bit-roots-r1-and-r3-mozilla).

#### OSS response strategy


In response to the change in the root certificate trust policy, Alibaba Cloud Object Storage Service (OSS) has adopted the following strategies to ensure a smooth transition and continued service availability. For more information, see [Alibaba Cloud Object Storage Service HTTPS Root Certificate Upgrade Announcement](https://www.aliyun.com/noticelist/articleid/1075666827.html).


-

Certificate update plan


Starting from July 1, 2024, new certificates issued by OSS use GlobalSign Root R3 to ensure compatibility with the latest security standards and to prevent access interruptions caused by changes in the root certificate trust policy.

-

Cross-certificate compatibility solution


To ensure broad compatibility during the transition period, existing OSS certificates use a cross-certificate mechanism to smoothly migrate from GlobalSign Root R1 to GlobalSign Root R3. The cross-certificate based on GlobalSign Root R1 is valid until January 28, 2028. Considering that certificate applications must be submitted 13 months before expiration, complete all related root certificate update preparations by December 28, 2026.

-

Future plans and recommendations


For long-term development, although GlobalSign Root R3 is the current solution, it will also cease to be trusted by Mozilla starting April 15, 2027, and will finally expire on March 18, 2029. Therefore, update your root certificates in a timely manner and ensure that your root certificate list includes multiple authoritative root certificates such as GlobalSign R1, R3, R6, and R46 to meet future certificate rotation needs.

#### What you need to do


For most users, no action is required. Modern operating systems (such as Windows 7+, macOS 10.12.1+, and major Linux distributions from the last 5 years) and browsers (such as Chrome, Firefox, and Safari) automatically update their built-in root certificate libraries. They will automatically trust the new root certificates.


Follow the steps below only if you encounter certificate errors when accessing OSS over HTTPS on legacy operating systems, embedded devices, or outdated custom clients.

##### Step 1: Check for the 'GlobalSign Root CA - R3' root certificate

## Windows


-

Press Win+R, enter `certmgr.msc`, and press Enter to open Certificate Manager.

-

In the navigation pane on the left, expand Trusted Root Certification Authorities > Certificates.

-

In the list on the right, find the certificate where Issued To is GlobalSign and Friendly Name is GlobalSign Root CA - R3.

## Linux


Using Ubuntu as an example, open a terminal and run the following command to check if GlobalSign-related certificates exist in the system's certificate directory.


`shell
ls /etc/ssl/certs/ | grep GlobalSign
`


## macOS


-

Open Finder, search for Keychain Access, and double-click it to open.

-

Click System Roots. Enter GlobalSign in the search box in the upper-right corner. Double-click a certificate to view its details.

##### Step 2: Install the missing root certificate


If you have checked and confirmed that the root certificate is missing from your system, please follow the installation method corresponding to your operating system.


-

Windows: [How to install a root certificate or an intermediate certificate on a Windows system](https://www.alibabacloud.com/help/en/ssl-certificate/user-guide/how-to-install-root-and-intermediate-certificates-on-windows-systems)

-

macOS: [How to install a root certificate on a macOS system](https://www.alibabacloud.com/help/en/ssl-certificate/user-guide/install-a-root-certificate-on-macos)

-

Linux: [How to install a root certificate on a Linux system](https://www.alibabacloud.com/help/en/ssl-certificate/user-guide/how-to-install-a-root-certificate-in-a-linux-system)

## Billing


After you enable HTTPS in CDN, you are billed for the number of static HTTPS requests. For more information, see [Billing of HTTPS requests for static content](https://www.alibabacloud.com/help/en/cdn/product-overview/billing-of-https-requests-for-static-content).

## FAQ

#### How do I update a certificate that is replaced or has expired? 


The update procedure is the same as the initial configuration. Choose the update path corresponding to your domain name type.


-

OSS custom domain name: Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page, and in the Certificate Hosting section for the target bucket's domain management, select the new certificate.

-

CDN-accelerated domain name: Go to the [CDN console](https://cdn.console.alibabacloud.com/domain/list). In the HTTPS settings for the target accelerated domain name, select or upload the new certificate.

#### After I configure an SSL Certificate, why does my browser still show an 'insecure' or 'certificate error' message?


If a security warning persists after configuration, troubleshoot the issue as follows:


-

Check the configuration location: Confirm whether CDN acceleration is enabled for the access domain. If it is, you must configure HTTPS in the Alibaba Cloud CDN console for the accelerated domain name. The certificate hosting setting in the OSS console will not apply.

-

Clear the browser cache: Your browser may have cached the old certificate status. Try clearing your browser cache and accessing the site again.

-

Wait for the configuration to take effect: Certificate configurations can take time to deploy. Please wait a few minutes before re-testing.

-

Check the certificate chain integrity: Certificate files issued by intermediate CAs contain multiple certificates. Concatenate the server certificate with the intermediate certificate to form a complete certificate chain before uploading. The Certificate Authority usually provides instructions for this concatenation. Review the relevant documentation carefully.

#### How do I handle certificate exceptions when accessing OSS over HTTPS?


You can use the corresponding method based on the type of certificate exception.


-

Certificate not configured: The browser displays "Your connection is not private," with the error message: `NET::ERR_SSL_PROTOCOL_ERROR`. This error may indicate that the certificate is missing or configured in the wrong location (for example, using certificate hosting in OSS when CDN acceleration is enabled). Reconfigure HTTPS using the correct method.

-

Certificate expired: The browser displays "Your connection is not private," with the error message: `NET::ERR_CERT_DATE_INVALID`. The certificate bound to the domain has expired. View the expiration date in the browser. Purchase or apply for a new certificate, then update it following the configuration procedure.

-

Certificate mismatch: The browser displays "Your connection is not private," with the error message: `NET::ERR_CERT_COMMON_NAME_INVALID`. The domain in the access URL is not included in the certificate's domains. For example, the access domain is `cdn.example.com`, but the certificate is bound to `oss.example.com`. Configure the correct certificate for the access domain.

#### Why can't I find my target certificate in the drop-down list when selecting a certificate?


The certificate might not appear in the drop-down list for the following reasons:


-

Certificate and domain name mismatch: The system only lists certificates that match the domain you are currently configuring. For example, when configuring a certificate for `oss.example.com`, you cannot select a certificate issued to `cdn.example.com`.

-

Certificate is not under the current account: Confirm whether the certificate is under the current Alibaba Cloud account. If not, you need to upload the certificate on the [SSL Certificate Management](https://yundun.console.alibabacloud.com/?p=cas#/certExtend/upload) page.

-

Wildcard certificate level mismatch: A wildcard certificate only supports subdomains at the same level. For example, `*.example.com` can match `www.example.com` and `oss.example.com`, but not `cdn.oss.example.com`.

#### When I configure an HTTPS certificate in CDN, a message indicates that the certificate format is incorrect. How do I convert the format? 


CDN HTTPS configuration only supports certificates in PEM format. Different CAs have different requirements for uploading certificate content. If the certificate is not in PEM format, see [Certificate formats](https://www.alibabacloud.com/help/en/cdn/user-guide/certificate-formats#concept-grb-4pl-xdb). Follow the instructions in the document to convert the format before uploading.

#### How do I update a certificate using the command line or an API?


-

CDN-accelerated domain name: Use the Alibaba Cloud CLI to set the CDN domain certificate. For more information, see [Cloud Assistant CLI integration example](https://www.alibabacloud.com/help/en/cdn/developer-reference/cli-integration-example) and [SetDomainServerCertificate API](https://www.alibabacloud.com/help/en/cdn/developer-reference/api-cdn-2018-05-10-setcdndomainsslcertificate).

-

OSS custom domain name: Use ossutil to bind a certificate to a custom domain name. For more information, see [put-cname command](https://www.alibabacloud.com/help/en/oss/developer-reference/put-cname).

#### How do I disable HTTPS access?


-

Custom domain name


To disable HTTPS access, proceed with the following steps to delete the certificate.


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page. Click the target bucket. In the navigation pane on the left, click Bucket Settings > Domain Names.

-

Click the delete icon next to Certificate Details for the target domain name, and then click OK.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996963.png)

-

CDN-accelerated domain name


Proceed with the following steps to disable HTTPS.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

To avoid access interruptions, first restore the URL Redirection type to its default setting and disable the HSTS feature before disabling HTTPS.


-

Go to the [CDN console](https://cdn.console.alibabacloud.com/domain/list), click the target accelerated domain name, click HTTPS, then click Modify next to HTTPS Certificate.

-

Disable HTTPS Secure Acceleration as shown in the following figure, then click OK.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9387529571/p996766.png)


Thank you! We've received your  feedback.