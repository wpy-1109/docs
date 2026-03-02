# Static Website Hosting

Source: https://help.aliyun.com/zh/oss/user-guide/hosting-static-websites

## Overview

OSS static website hosting allows you to publish static files (HTML, CSS, JavaScript, etc.) stored in a Bucket as a publicly accessible website without maintaining traditional servers, significantly reducing operations costs and technical barriers.

## Hosting a Standard Static Website

Suitable for traditional multi-page static websites (corporate sites, product showcase sites).

**Important**: When accessing HTML files via OSS Bucket domain names, browsers force download instead of previewing for security reasons. To enable normal web browsing, you must bind a custom domain name. If the Bucket is in mainland China, the domain requires ICP filing.

### Step 1: Configure Static Website Hosting

1. Navigate to **Bucket > Data Management > Static Pages**
2. Click **Settings** and configure:
   - **Default Homepage**: Set to `index.html`
   - **Sub-directory Homepage**: Choose based on your site structure:
     - **Disabled (default)**: All URLs ending with `/` return the root directory's default homepage
     - **Enabled**: For complex sites with independent content sections (e.g., `/blog/`, `/docs/`). When enabled, set **File 404 Rules**:
       - **Redirect (default)**: Returns 302 redirect to directory homepage
       - **Index**: Returns directory homepage content with 200 status code (URL unchanged)
       - **NoSuchKey**: Always returns 404 error if file doesn't exist
   - **Default 404 Page**: Set to `error.html`
   - **Error Document Response Code**: Select `404`
3. Click **Save**

### Step 2: Upload Website Files

Upload HTML files to the Bucket via console drag-and-drop or ossutil.

### Step 3: Set Bucket Read Permission

1. **Disable Block Public Access**: Navigate to **Permission Control > Block Public Access**, toggle off
2. **Set Bucket ACL to Public Read**: Navigate to **Read/Write Permission**, set to `public-read`

**Warning**: Public read makes ALL files in the Bucket publicly accessible. Only store website resources (HTML, CSS, JS) in this Bucket. Keep sensitive data in separate Buckets with access control.

### Step 4: Verify Configuration

- Test homepage: Visit `http://example.com`
- Test 404 page: Visit `http://example.com/missing-object`

## Hosting SPA (Single Page Applications)

For modern web applications (React, Vue, Angular) with client-side routing.

### Step 1: Configure SPA Hosting

Key differences from standard static hosting:
- **Default Homepage**: `index.html`
- **Sub-directory Homepage**: **Disabled** (all URLs ending with `/` return root homepage)
- **Default 404 Page**: `index.html` (critical: redirects all routes to app entry point)
- **Error Document Response Code**: `200` (ensures correct status code for route navigation)

### Step 2-4: Same as Standard Hosting

Upload files, set public read, and verify.

**SPA Verification**: Accessing non-existent paths (e.g., `/missing-object`) should redirect to the app entry and return 200 OK, allowing the frontend router to handle the path.

## Production Environment Best Practices

### Security

#### Enable HTTPS
- Modern browsers show "Not Secure" warnings for HTTP sites
- Search engines give higher SEO scores to HTTPS sites
- HTTPS encrypts data in transit via TLS/SSL
- Force HTTPS access for custom domains

#### Configure Anti-Hotlinking (Referer Protection)
- Prevent other websites from directly linking to your static resources
- Set allowed domain whitelist
- Control bandwidth costs

#### Enable Access Logging
- Record all access requests for security audits
- Analyze user behavior and identify abnormal access patterns
- Enable real-time log queries for performance optimization and troubleshooting

### Performance

#### Configure CDN Acceleration
- Cache content at global edge nodes
- Significantly improve access speed for global users
- Reduce OSS direct traffic costs
- Essential for high-concurrency scenarios

#### Configure CORS Rules
- SPAs typically call backend APIs or third-party resources
- Browser same-origin policy restricts cross-origin requests
- Configure allowed request origins, methods, and headers

### Deployment

#### Version Management: Release and Rollback
- Enable OSS versioning for rollback capability
- Integrate with CI/CD tools (e.g., Jenkins) for automated deployment
- Implement continuous integration/continuous deployment workflows

## FAQ

### SPA page refresh shows 404 error
SPA routes are handled by frontend JavaScript. When directly accessing or refreshing non-root routes, the server can't find physical files. **Solution**: Set default 404 page to `index.html` and error response code to `200`.

### How to disable static website hosting
Navigate to **Data Management > Static Pages > Settings**, clear the default homepage and 404 page configurations, save.

### Does static hosting support dynamic content?
Static hosting only supports client-side content (HTML, CSS, JavaScript). Server-side languages (PHP, Python, Java) are not supported. For dynamic features, use client-side rendering frameworks or combine with Alibaba Cloud Function Compute for serverless backend APIs.
