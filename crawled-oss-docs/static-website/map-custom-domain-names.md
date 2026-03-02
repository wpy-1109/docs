# Map Custom Domain Names

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/map-custom-domain-names-5

## Overview

Alibaba Cloud Object Storage Service (OSS) allows you to bind a custom domain name to your OSS bucket using a CNAME record. This enables you to access your OSS resources via your own domain (e.g., `static.example.com`) instead of the default OSS endpoint.

## Steps to Bind a Custom Domain with HTTPS

### Step 1: Add a Custom Domain in the OSS Console

1. Log in to the [OSS Console](https://oss.console.aliyun.com)
2. Select your target bucket
3. Navigate to **Bucket Settings** > **Domain Names** (or **Transmission** > **Domain Names**)
4. Click **Bind Custom Domain Name** and enter your domain

### Step 2: Configure the CNAME Record

Go to your DNS provider (e.g., Alibaba Cloud DNS) and add a CNAME record:

| Field | Value |
|-------|-------|
| **Record Type** | CNAME |
| **Host** | e.g., `static` (for `static.example.com`) |
| **Value** | `your-bucket-name.oss-<region>.aliyuncs.com` |

Wait for DNS propagation.

### Step 3: Enable HTTPS (Certificate Binding)

In the OSS console under your custom domain settings, enable **Certificate Hosting / HTTPS**:

- **Upload your own SSL/TLS certificate** (certificate + private key), or
- **Use a free certificate** issued through Alibaba Cloud Certificate Management Service, or
- **Select an existing certificate** from Alibaba Cloud Certificate Management

Once bound, your custom domain will support HTTPS access (e.g., `https://static.example.com/object-key`).

### Step 4: Mandatory CNAME Verification (Effective March 20, 2025)

For new domain bindings, Alibaba Cloud requires CNAME ownership verification. You must add a specific verification CNAME record before the binding is approved. This policy helps prevent unauthorized domain binding.

## Important Notes

- **CDN Acceleration**: If you want to use Alibaba Cloud CDN with your custom domain, configure the CNAME provided by CDN (not the OSS endpoint directly). The CDN CNAME takes precedence.
- **Certificate Limits**: Free certificates typically cover single domains. Wildcard or multi-domain certificates may require purchase.
- **HTTP to HTTPS Redirect**: You can configure force-HTTPS redirection in OSS or CDN settings.
- **Region Matching**: Ensure the OSS endpoint region matches your bucket's region.
- **ICP Filing**: Required if your domain resolves to servers in mainland China.
