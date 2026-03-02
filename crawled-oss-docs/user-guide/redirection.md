# Use redirection to fetch files that do not exist in a bucket from an origin server

When a client accesses OSS, a 404 error may occur if a file does not exist or during data migration, which can interrupt the connection. To prevent this, you can configure redirection rules. These rules allow OSS to return a 3xx redirect response when specific conditions are met. The response seamlessly guides the request to an origin server or another specified page. This ensures business continuity and a positive user experience.

## How it works


The core of the redirection feature is a client-side redirect. A client, such as a browser, accesses a bucket using its attached custom domain name. If the request triggers a rule, such as one for an HTTP 404 error, the OSS server returns an `HTTP 3xx` status code, such as 302, and a `Location` response header that contains a new address. When the client receives this response, it automatically sends a new request to the URL specified in the `Location` header. OSS does not proxy the content from the origin server during this process.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/7345600671/CAEQThiBgICmv6KwzhkiIDhkMjdiYmU2ZjE4NzRmZjU5YTc1ZTZkM2VlYzA4M2Y03963382_20230830144006.372.svg)
## Custom 404 page


When a specific error occurs for a path or file in OSS, you can redirect the request to a custom error page or another page for business processing. For example, if a client encounters a `404 Not Found` error when accessing any file in a bucket using a custom domain name, the client is automatically redirected to a unified custom error page at `https://yourdomain/404.html`.

#### Step 1: Attach a custom domain name


Before you create a redirection rule, you must attach a custom domain name to the bucket. The redirection feature works only for requests made through a custom domain name that is attached to the bucket. Requests made through a standard OSS endpoint (`http(s)://..aliyuncs.com`) do not trigger redirection rules. Instead, they return a `400 Bad Request` error.


-

On the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket.

-

In the navigation pane on the left, choose Bucket Settings > Domain Names, and then click Attach Domain.

-

In the Attach Domain panel, enter a custom domain name. For example, enter `customdomain.com`. Replace this with your actual domain name. If the bucket is in the Chinese mainland, the domain name must have an ICP filing.

-

Follow the prompts to configure CNAME parsing. Point your custom domain name to the CNAME address that is provided by OSS.

#### Step 2: Create a redirection rule


-

In the navigation pane on the left, choose Data Management > Mirroring-based Back-to-origin.

-

On the Mirroring-based Back-to-origin page, click Create Rule.

-

In the Create Rule panel, configure the following parameters:


-

Origin Fetch Type: Select Redirection.

-

Condition: Set HTTP Status Code to 404.

-

Origin URL: Select Redirect to a fixed URL.


-

Protocol (first column): Select https.

-

Domain Name (second column): Enter the domain name where the custom error page is located, such as yourdomain.com.

-

Path (third column): Enter the path of the custom error page, such as 404.html.

-

Redirection Code: Select 302 or 307. Because this is a redirect for an error page, do not use a 301 permanent redirect.

-

Click OK.

#### Step 3: Validate the rule


In the following `curl` command, replace `customdomain` with the custom domain name attached to your bucket. Then, access an object that does not exist.


`shell
curl -I "http://customdomain.com/does-not-exist.html"
`


The expected response is a 302 status code and the correct `Location` header.


`shell
HTTP/1.1 302 Found
Server: AliyunOSS
Date: Wed, 03 Sep 2025 07:25:01 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 68B7ED4D949F8A38365CC014
Location: https://yourdomain.com/404.html
`


## Seamless data migration


When you gradually migrate data from an origin server, such as a self-managed data center, to OSS, some objects may not be synchronized yet. If you directly access these non-existent objects, a `404 Not Found` error occurs, which affects business continuity. By configuring redirection rules, you can allow OSS to return a 3xx redirect response when a specific HTTP error, such as 404, occurs. This response seamlessly guides the client to the origin server to retrieve the content. This feature is often used during the transition phase of a smooth migration. For example, when a client accesses a file that has not yet been migrated in the `examplefolder/` directory of a bucket using a custom domain name, the client is automatically redirected to the corresponding path on the legacy origin server at `https://yourdomain.com/`.

#### Step 1: Attach a custom domain name


Before you create a redirection rule, you must attach a custom domain name to the bucket. The redirection feature works only for requests made through a custom domain name that is attached to the bucket. Requests made through a standard OSS endpoint (`http(s)://..aliyuncs.com`) do not trigger redirection rules. Instead, they return a `400 Bad Request` error.


-

On the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket.

-

In the navigation pane on the left, choose Bucket Settings > Domain Names, and then click Attach Domain.

-

In the Attach Domain panel, enter a custom domain name. For example, enter `customdomain.com`. Replace this with your actual domain name. If the bucket is in the Chinese mainland, the domain name must have an ICP filing.

-

Follow the prompts to configure CNAME parsing. Point your custom domain name to the CNAME address that is provided by OSS.

#### Step 2: Create a redirection rule


-

In the navigation pane on the left, choose Data Management > Mirroring-based Back-to-origin.

-

On the Mirroring-based Back-to-origin page, click Create Rule.

-

In the Create Rule panel, configure the following parameters:


-

Origin Fetch Type: Select Redirection.

-

Condition:


-

Set HTTP Status Code to 404.

-

File Prefix: Set this to the directory being migrated, such as `examplefolder/`. If you want the rule to apply to the entire bucket, leave this empty.

-

Origin URL: Select Add Prefix and Suffix. This is key to ensuring seamless path mapping. Do not select Redirect to a fixed URL.


-

Protocol (first column): Select the protocol supported by the legacy origin server, such as https.

-

Domain Name (second column): Enter the domain name of the legacy origin server, such as `yourdomain.com`.

-

Path (third column): Keep this empty. The Add Prefix and Suffix pattern automatically appends the user-requested path, such as `examplefolder/file.jpg`, to the domain name.

-

Redirection Code: Select 302. A 302 is a temporary redirect, which is ideal for transitional scenarios such as data migration. Do not use 301. A 301 is a permanent redirect. Browsers and CDN nodes aggressively cache 301 redirects. If you set a 301 redirect, requests might be forced to the legacy origin server even after you migrate the files to OSS. This can easily cause major issues in production.


-

Click OK.

#### Step 3: Validate the rule


In the following `curl` command, replace `customdomain` with the custom domain name attached to your bucket. Then, access an object that does not exist.


`shell
curl -I "http://customdomain.com/examplefolder/does-not-exist.html"
`


The expected response is a 302 status code and the correct `Location` header.


`shell
HTTP/1.1 302 Found
Server: AliyunOSS
Date: Wed, 03 Sep 2025 08:28:21 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 68B7FC25107134303531344B
Location: https://yourdomain.com/examplefolder/does-not-exist.html
`


#### Step 4: Migrate data and switch traffic


-

For more information, see [Migrate data to OSS](https://www.alibabacloud.com/help/en/oss/user-guide/data-migration-overview).

-

After the migration is complete, verify the data integrity in OSS.

-

Gradually narrow the scope of the redirection rule, for example, by targeting only specific subdirectories that have not yet been migrated. Or, you can disable the rule entirely to switch all traffic to OSS.

## Quotas and limits


-

Applicable domain names: Rules apply only to requests made through a custom domain name attached to a bucket. They do not apply to requests made through a standard OSS endpoint (bucket endpoint).

-

Number of rules: You can configure up to 20 rules for each bucket. OSS matches requests against rules in ascending order of their rule numbers (RuleNumber). Once a request matches a rule, subsequent rules are not executed.

-

Matching logic: File prefix and suffix matching is case-sensitive and does not support wildcard characters. When you configure multiple rules, you must set different file prefixes or suffixes to distinguish them.

## FAQ

#### I configured a rule, but I still get a 404/403 error instead of a redirect. Why?


Check the following items in order:


-

Check the access domain name: Confirm that you are using the custom domain name attached to the bucket for access, not the standard OSS endpoint. Using the standard OSS endpoint results in a `400 Bad Request` error.

-

Check bucket permissions and status code: If the bucket permission is private, accessing a non-existent object usually returns a `403 Forbidden` error. Confirm that your rule includes a trigger condition for the `403` status code.

-

Check rule priority: Confirm that no other rule with a lower rule number has already matched the request.

#### Why does a double slash (//) appear in the redirected URL?


This is usually caused by incorrect path concatenation. Check the configuration of the File Prefix and Replace Prefix (if used). For example, if the file prefix is `path/`, the replacement prefix should be `new-path`, not `/new-path`. This avoids duplicating the `/` that follows the domain name.

#### I modified a redirection rule, but the changes did not take effect. Why?


If you previously used a `301` (permanent redirect), your browser or a CDN node might have aggressively cached the old redirection rule. You can try clearing your browser cache, purging the CDN cache, or using your browser's incognito or private mode to test.

#### Why do I get stuck in an infinite redirect loop?


Check the redirection target address. Make sure the target address does not, directly or indirectly, point back to a URL that triggers an OSS redirection rule. This is especially important when you use a CDN that follows redirects. Check whether the CDN's back-to-origin configuration is mistakenly sending requests back to the custom domain name of the OSS bucket.

#### How can I find out which rule was matched?


Currently, OSS access logs do not include a field that identifies which redirection rule was matched. To troubleshoot, you can gradually narrow the scope of your rules or temporarily disable other rules. You can also catch the `3xx` response on the client side and inspect the `Location` header to see if the redirection is happening as expected.

Thank you! We've received your  feedback.