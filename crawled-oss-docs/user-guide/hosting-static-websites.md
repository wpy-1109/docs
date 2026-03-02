# Static website hosting

Static website hosting of Object Storage Service (OSS) enables you to publish static files, such as HTML, CSS, and JavaScript, stored in a bucket as a publicly accessible website. This feature eliminates the need for traditional servers, letting you deploy highly available websites while significantly reducing maintenance costs and required technical expertise.

## Host a standard static website


Use static website hosting to deploy traditional multi-page static websites, such as corporate websites or product showcases, for stable online access.
For security reasons, when you access an HTML file using the domain name of an OSS bucket, browsers force a download instead of displaying the page online. To enable normal web browsing, you must map a custom domain name. For more information, see [Access OSS using a custom domain name](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names). An [ICP filing](https://www.alibabacloud.com/zh/product/icp-filing) is required if your bucket is located in the Chinese mainland.
#### Step 1: Configure static website hosting


Configure a default index page and an error page to set basic access rules for your website. This ensures that users can browse the site and receive a direct-viewing error message when an access error occurs.


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket, then click Data Management > Static Pages in the left-side navigation pane.

-

Click Settings and configure the following parameters:


-

Set Default Homepage to `index.html`.

-

For Subfolder Homepage, choose whether to enable a separate index page for subdirectories based on your website structure.


-

Disabled (Default): This option is suitable for simple websites without separate index pages for subdirectories. With this option, all URL paths ending with a forward slash (`/`) return the default index page from the root directory.

-

Enabled: This option is suitable for complex websites that contain multiple independent content sections (such as `/blog/` or `/docs/`), each with its own index page. When a separate index page is enabled, you must also configure the Subfolder 404 Rule, which defines how the system responds when a user requests a file that does not exist.


-

Redirect (Default): Redirects to the directory. When the requested file is not found, the system checks whether an index page exists in the corresponding directory.  If an index page exists, the system returns a `302` redirect, and the browser's address bar updates to the directory path (for example, `.../subdir`becomes `.../subdir/`).

-

Index: Returns the content of the index page directly. Similar to Redirect, but if an index page is found in the corresponding directory, the system returns the content of that page with a `200`status code. The browser's address bar remains unchanged.

-

NoSuchKey: Returns a 404 error directly. If the requested file does not exist, the system returns a `404` error, regardless of whether an index page exists in the corresponding directory.


Detailed description of the Subfolder 404 Rule


When Subfolder Homepage is enabled, this rule defines the system's response when a request points to an object that does not exist. This ensures that website routing is handled correctly.

#### Core mechanism: Differentiating between object requests and directory requests


The rule's behavior depends on the structure of the request URL, specifically whether it ends with a forward slash (`/`).


-

Object request: The URL does not end with a `/`, such as `.../subdir`. The system interprets this as a request for the `subdir` object.

-

Directory request: The URL ends with a `/`, such as `.../subdir/`. The system interprets this as a request for the default homepage within the `subdir` directory.


The Subfolder 404 Rule is triggered only when an object request fails, that is, the object does not exist.

#### Detailed rule behavior


The following table details how each rule behaves when a request is made for a non-existent object (for example, `http://example.com/subdir`).




















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







| Rule | Core behavior | Procedure | Effect (depending on whether subdir/index.html exists) |
| --- | --- | --- | --- |
| Redirect (Default) | Redirects to the directory URL: Checks whether an index page exists in the corresponding directory. If it does, a 302 redirect response is returned. | The subdir object is not found, triggering the rule.The system checks whether subdir/index.html exists.If it exists, 302 Found with the Location header pointing to .../subdir/ is returned. If it does not exist, 404 Not Found is returned. | If it exists: The index page content is displayed, and the browser's address bar updates to .../subdir/.If it does not exist: The 404 error page is displayed. |
| Index | Returns the index page content directly: Checks whether an index page exists in the corresponding directory. If it does, its content with a 200 status code is returned. | The subdir object is not found, triggering the rule.The system checks whether subdir/index.html exists.If it exists, its content is returned with a 200 OK status code. If it does not exist, 404 Not Found is returned. | If it exists: The index page content is displayed, and the browser's address bar remains .../subdir.If it does not exist: The 404 error page is displayed. |
| NoSuchKey | Returns a 404 error directly: Does not perform any additional directory or index page checks. | The subdir object is not found, triggering the rule.404 Not Found is immediately returned. | The 404 error page is always displayed, regardless of whether subdir/index.html exists. |


-

Set Default 404 Page to `error.html`.

-

For Error Page Status Code, select 404.

-

Click Save.

#### Step 2: Upload website files


Upload your prepared HTML files for your website to the bucket.


-

Download and decompress the sample file [html.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/en-US/20250920/kizngb/html_en.zip), or use your own project files.

-

In the left-side navigation pane, choose Object Management > Objects.

-

Drag your sample files or existing project files into the upload window. After the files are added to the upload list, click Upload.

#### Step 3: Set access permissions for a bucket


Configure public-read permissions so that users can access your website.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Granting public-read permission makes all objects in the bucket publicly accessible over the Internet. Any user who has the object URL can download the object directly. Therefore, you should only store publicly required resources, such as HTML, CSS, and JavaScript, in this bucket. Store any sensitive data in a separate bucket with stricter access control settings.


-

By default, Block Public Access is enabled when you create an OSS bucket. This feature prevents you from setting the bucket's access control list (ACL) to public-read or public-read-write. You must first disable this feature.


-

In the left-side navigation pane, click Access Control > Block Public Access.

-

Click the Block Public Access switch. In the dialog box that appears, enter I confirm that I want to disable Block Public Access, then click OK.

-

Set the bucket ACL to public-read.


-

Switch to the Access Control List tab and click Configure.

-

Set Bucket ACL to Public Read. In the dialog box that appears, click Continue.

-

Click Save.

#### Step 4: Verify the website configuration


Perform an access test to confirm that website hosting is working.


-

Verify homepage access: In a browser, navigate to your custom domain name (example: `http://example.com`). The result should appear as follows.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1643268571/p1008969.png)

-

Verify the 404 page: In a browser, navigate to a non-existent file (example: `http://example.com/missing-object`). The result should appear as follows.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1643268571/p1008970.png)

## Host a single-page application (SPA)


This specialized hosting solution for SPAs supports front-end routing and page refreshes, meeting the deployment needs of modern web applications.
For security reasons, when you access an HTML file using the domain name of an OSS bucket, browsers force a download instead of displaying the page online. To enable normal web browsing, you must map a custom domain name. For more information, see [Access OSS using a custom domain name](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names). An [ICP filing](https://www.alibabacloud.com/zh/product/icp-filing) is required if your bucket is located in the Chinese mainland.
#### Step 1: Configure SPA hosting


Configure the hosting parameters and optimize the settings for the routing characteristics of SPAs to ensure that frontend routing works correctly.


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket, then click Data Management > Static Pages in the left-side navigation pane.

-

Click Settings and configure the following parameters:


-

Set Default Homepage to `index.html`.

-

Set Subfolder Homepage to Disabled. With this setting, any request to the static website domain or any URL under that domain ending with a forward slash (`/`) returns the root directory's default homepage.

-

Set Default 404 Page to `index.html` (This critical setting redirects all routes to the application's entry point).

-

For Error Page Status Code, select 200 (to ensure that route transitions return the correct status code).

-

Click Save.

#### Step 2: Upload application files


Upload your prepared SPA files to the bucket to complete the application deployment.


-

Download and decompress the sample application [demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/en-US/20250920/tbuoqg/demo.zip), or use your own application files.

-

In the left-side navigation pane, click Object Management > Objects.

-

Drag all files from the `demo` directory or your own application files into the upload window. After all files are added to the upload list, click Upload.

#### Step 3: Set access permissions for a bucket


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Granting public-read permission makes all objects in the bucket publicly accessible over the Internet. Any user who has the object URL can download the object directly. Therefore, you should only store publicly required resources, such as HTML, CSS, and JavaScript, in this bucket. Store any sensitive data in a separate bucket with stricter access control settings.


Configure public access permissions so that users can access the SPA.


-

Disable Block Public Access for the bucket.


-

In the left-side navigation pane, click Access Control > Block Public Access.

-

Click the Block Public Access switch. In the dialog box that appears, enter I confirm that I want to disable Block Public Access, then click OK.

-

Set the bucket ACL to public-read.


-

Switch to the Access Control List tab and click Configure.

-

Set Bucket ACL to Public Read. In the dialog box that appears, click Continue.

-

Click Save.

#### Step 4: Verify the application deployment


Perform an access test to confirm that the SPA is deployed and can handle route transitions correctly.


-

Verify homepage access: In a browser, navigate to your custom domain name (example: `http://example.com`). The result should appear as follows.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1643268571/p1009194.png)

-

Verify the 404 page: In a browser, navigate to a non-existent file (example: `http://example.com/missing-object`). The request is redirected to the application's entry point and returns `200 OK`. The result should appear as follows.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1643268571/p1009196.png)

## Apply in production


To ensure your static website runs stably and provides a good user experience in a production environment, implement security and performance optimizations.

#### Best practices


-

Secure transmission: Enable HTTPS access


Modern browsers display a "Not Secure" warning for HTTP websites, and search engines give higher SEO scores to HTTPS-enabled websites. Enforce HTTPS access for your attached custom domain name to [access OSS over the HTTPS protocol](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-by-https-protocol). The HTTPS protocol uses TLS/SSL to encrypt data in transit, preventing data theft or tampering while enhancing website security and user trust.

-

Performance optimization: Configure CDN acceleration


If your static website serves a global audience or experiences high concurrent traffic, [configure CDN acceleration](https://www.alibabacloud.com/help/en/oss/user-guide/cdn-acceleration). This approach caches your content on edge nodes worldwide, significantly improving access speed and reducing OSS traffic costs.

-

Cross-domain access: Configure CORS rules


SPAs often need to call back-end APIs or access third-party resources, which the browser's same-origin policy can restrict. By [configuring CORS rules](https://www.alibabacloud.com/help/en/oss/user-guide/cors-settings), you can specify allowed origins, methods, and headers to ensure your front-end application can access the necessary API services and external resources.

-

Version management: Implement releases and rollbacks


A production environment requires the ability to quickly release new versions and perform emergency rollbacks. Enable [versioning](https://www.alibabacloud.com/help/en/oss/user-guide/overview-78/) and integrate it with automation tools such as Jenkins to create a complete continuous integration and continuous deployment (CI/CD) Pipeline. This improves release efficiency and system stability.

#### Risk prevention


-

Traffic theft protection: Configure hotlink protection


Static resources that are directly referenced by other websites cause extra traffic costs and server load. [Configure hotlink protection](https://www.alibabacloud.com/help/en/oss/user-guide/hotlink-protection) and set up a domain allowlist to prevent bandwidth theft from other websites hotlinking your assets and to control operational costs.

-

Access monitoring: Enable access logs


Production environments require complete access records for security audits, performance analysis, and troubleshooting. Enable [Real-time Log Query](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/) to record detailed information for all access requests. This helps you identify abnormal access patterns, analyze user behavior, and optimize website performance.

## FAQ

#### How do I fix the 404 error that appears when I refresh a page in my deployed SPA?


In a single-page application, front-end JavaScript handles all routes. When you directly access or refresh a non-home page route, the server cannot find a corresponding file. To resolve this issue, set the Default 404 Page to `index.html` and the Error Page Status Code to `200`. This redirects all "non-existent" paths to the application's entry point, allowing the frontend router to handle them correctly.

#### How do I disable static website hosting?


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket, then click Data Management > Static Pages in the left-side navigation pane.

-

Click Settings, clear the Default Homepage and Default 404 Page configurations, then click Save to disable static website hosting.

#### Does static website hosting support dynamic content?


Static website hosting only supports client-side static content, including HTML, CSS, and JavaScript. It does not support server-side dynamic languages such as PHP, Python, or Java. If you need dynamic functionality, you can use client-side rendering techniques with frontend frameworks or call backend APIs through serverless services such as Alibaba Cloud Function Compute.

Thank you! We've received your  feedback.