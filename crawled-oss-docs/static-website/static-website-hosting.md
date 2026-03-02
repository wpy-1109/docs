# Static Website Hosting

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/static-website-hosting

## Overview

Alibaba Cloud Object Storage Service (OSS) allows you to host static websites directly from a bucket. You can configure a default homepage (index document) and a custom error page (error document) for your bucket.

## Prerequisites

- You have an Alibaba Cloud OSS bucket already created
- You have the necessary RAM permissions to manage the bucket (`oss:PutBucketWebsite`)
- Your static website files (HTML, CSS, JS, images, etc.) are ready for upload
- The bucket's ACL should be set to **Public Read** if you want the website to be publicly accessible

## Configuration via OSS Console

1. Log in to the [OSS Management Console](https://oss.console.aliyun.com)
2. In the left navigation pane, click **Buckets** and select the target bucket
3. Navigate to **Basic Settings** > **Static Pages**
4. Click **Configure** and set the following:
   - **Default Homepage (Index Document):** e.g., `index.html`
   - **Default 404 Page (Error Document):** e.g., `error.html`
   - **Subfolder Homepage:** Optionally enable if you want subdirectories to resolve to their own index files
5. Click **Save**

## Configuration Options

| Setting | Description | Example |
|---------|-------------|---------|
| **Index Document** | The default homepage file served when users access the root or a subdirectory | `index.html` |
| **Error Document** | The custom 404 error page returned when a user requests an object that does not exist | `error.html` |
| **Subfolder Homepage** | Redirects subfolder requests to their own index page | Enable/Disable |

## Configuration via API (PutBucketWebsite)

```xml
PUT /?website HTTP/1.1
Host: bucket-name.oss-cn-hangzhou.aliyuncs.com

<WebsiteConfiguration>
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>error.html</Key>
  </ErrorDocument>
</WebsiteConfiguration>
```

## Configuration via ossutil (CLI)

```bash
ossutil website --method put oss://your-bucket-name local://website-config.xml
```

## Configuration via SDK (Python)

```python
import oss2

auth = oss2.Auth('<AccessKeyId>', '<AccessKeySecret>')
bucket = oss2.Bucket(auth, 'https://oss-<region>.aliyuncs.com', '<bucket-name>')

from oss2.models import BucketWebsite
bucket.put_bucket_website(BucketWebsite('index.html', 'error.html'))
```

## Accessing the Website

Once configured, your static website is accessible at:

```
http://<bucket-name>.oss-<region>.aliyuncs.com/
```

Or with a custom domain:

```
https://www.yourdomain.com
```

## Custom Domain Binding

### Steps

1. In the OSS Console, go to **Bucket Settings** > **Domain Names**
2. Click **Bind Custom Domain Name**
3. Enter your domain (e.g., `www.example.com`)
4. Choose binding method:
   - **Direct binding** (CNAME to OSS endpoint)
   - **Via CDN acceleration** (recommended for production)

### Configure DNS (CNAME Record)

At your domain registrar/DNS provider, add a CNAME record:

| Record Type | Host | Value |
|-------------|------|-------|
| CNAME | `www` | `your-bucket-name.oss-cn-region.aliyuncs.com` |

> If using CDN, point the CNAME to the CDN-assigned domain instead.

### CNAME Ownership Verification (Effective March 20, 2025)

For new domain bindings, Alibaba Cloud requires CNAME ownership verification. You must add a specific verification CNAME record before the binding is approved.

## Enable HTTPS

1. In the OSS console under your custom domain settings, enable **Certificate Hosting / HTTPS**
2. Options:
   - **Upload your own SSL/TLS certificate** (certificate + private key)
   - **Use a free certificate** from Alibaba Cloud Certificate Management Service
   - **Select an existing certificate** from Alibaba Cloud Certificate Management
3. Once bound, your custom domain will support HTTPS access

## Important Notes

- **Bucket ACL**: Must be set to **Public Read** for anonymous visitors to access the site
- **ICP Filing**: If your domain resolves to servers in mainland China, an ICP filing (备案) is required
- **Subdomain vs. Root Domain**: Root/apex domains cannot use CNAME directly - consider using CDN or Alibaba Cloud DNS for apex domain support
- **File Permissions**: Uploaded objects must be publicly readable
- **Static Content Only**: Supports HTML, CSS, JavaScript, images, and other static content - no server-side scripting
- **Error Document**: Only handles 404 (Not Found) errors; other HTTP errors return standard OSS responses

## Common Use Cases

- Single-page applications (React, Vue, Angular)
- Documentation sites
- Landing pages / marketing sites
- Blog/portfolio hosting
