# Troubleshooting CORS Issues

Source: https://help.aliyun.com/zh/oss/user-guide/cors-settings

## Overview

Cross-Origin Resource Sharing (CORS) errors are common when web applications access OSS resources from a different domain. Understanding CORS mechanics and proper configuration is essential for browser-based OSS access.

## Understanding CORS

### Why CORS Errors Occur
Browsers enforce the Same-Origin Policy: JavaScript can only make requests to the same origin (protocol + domain + port). When a web page at `https://www.example.com` tries to access `https://bucket.oss-cn-hangzhou.aliyuncs.com`, the browser blocks it unless OSS responds with proper CORS headers.

### CORS Flow
1. **Simple Request**: Browser sends request directly; OSS must respond with `Access-Control-Allow-Origin` header
2. **Preflight Request**: For complex requests (PUT, DELETE, custom headers), browser first sends OPTIONS request; OSS must respond with allowed methods/headers

## Common CORS Error Scenarios

### Scenario 1: No CORS Rules Configured

**Error**: `Access to XMLHttpRequest at 'https://...' from origin 'https://...' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.`

**Solution**: Add CORS rules to the Bucket:
1. Navigate to **Bucket > Permission Control > CORS Rules**
2. Add a rule:
   - **Allowed Origins**: `https://www.example.com` (or `*` for testing)
   - **Allowed Methods**: GET, POST, PUT, DELETE, HEAD
   - **Allowed Headers**: `*`
   - **Expose Headers**: `x-oss-request-id, ETag, Content-Length`
   - **Max Age**: 3600
   - **Allow Credentials**: Yes (if sending cookies/auth)

### Scenario 2: CORS Works for GET but Not PUT/DELETE

**Cause**: PUT and DELETE are not in the allowed methods.

**Solution**: Add PUT, DELETE, POST to allowed methods in CORS configuration.

### Scenario 3: CORS Headers Missing with CDN

**Cause**: CDN caches the first response (which may not include CORS headers if the first request was from the same origin or a non-browser client).

**Solutions**:
1. **Configure CORS at CDN level** (recommended):
   ```
   Access-Control-Allow-Origin: *
   Access-Control-Allow-Methods: GET, POST, PUT, DELETE, HEAD
   Access-Control-Max-Age: 3600
   ```
2. **Enable Vary: Origin** caching in CDN to cache different CORS responses per origin

### Scenario 4: Preflight (OPTIONS) Request Fails

**Cause**: OSS doesn't have a rule matching the preflight request's `Access-Control-Request-Method` or `Access-Control-Request-Headers`.

**Solution**:
- Ensure allowed methods include the requested method
- Ensure allowed headers include all custom headers sent by the client
- Use `*` for allowed headers if unsure which headers are needed

### Scenario 5: Credentials Not Allowed

**Error**: `Response to preflight request doesn't pass access control check: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'.`

**Cause**: When sending requests with credentials (cookies, auth headers), `Access-Control-Allow-Origin` cannot be `*`.

**Solution**:
- Set specific origin instead of `*`: `https://www.example.com`
- Enable **Allow Credentials** in CORS rule

## CORS Configuration Reference

### OSS Console Configuration

| Field | Description | Example |
|---|---|---|
| **Allowed Origins** | Origins that can send cross-origin requests | `https://www.example.com`, `https://*.example.com` |
| **Allowed Methods** | HTTP methods allowed | GET, PUT, POST, DELETE, HEAD |
| **Allowed Headers** | Request headers allowed in actual request | `*`, `Content-Type`, `Authorization` |
| **Expose Headers** | Response headers accessible to browser JavaScript | `x-oss-request-id`, `ETag` |
| **Max Age (seconds)** | Preflight result cache duration | 3600 |
| **Allow Credentials** | Whether to allow credentials | Yes/No |

### API Configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration>
  <CORSRule>
    <AllowedOrigin>https://www.example.com</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>DELETE</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
    <ExposeHeader>x-oss-request-id</ExposeHeader>
    <ExposeHeader>ETag</ExposeHeader>
    <MaxAgeSeconds>3600</MaxAgeSeconds>
  </CORSRule>
</CORSConfiguration>
```

## Debugging CORS Issues

### Step 1: Check Browser Console
Open Developer Tools (F12) > Console tab. CORS errors appear here with detailed messages.

### Step 2: Inspect Network Requests
In Developer Tools > Network tab:
- Look for the preflight OPTIONS request
- Check its response status (should be 200)
- Verify response headers include:
  - `Access-Control-Allow-Origin`
  - `Access-Control-Allow-Methods`
  - `Access-Control-Allow-Headers`

### Step 3: Test with curl
```bash
# Test preflight request
curl -I -X OPTIONS \
  -H "Origin: https://www.example.com" \
  -H "Access-Control-Request-Method: PUT" \
  -H "Access-Control-Request-Headers: Content-Type" \
  https://bucket.oss-cn-hangzhou.aliyuncs.com/test

# Check response for CORS headers
```

### Step 4: Verify CORS Configuration
```bash
# Get current CORS config
ossutil cors-options --method GET --origin https://www.example.com \
  oss://bucket-name/
```

## Common Mistakes

1. **Wildcard with credentials**: Using `*` as origin while sending credentials
2. **Missing Expose Headers**: Not exposing `ETag` or `x-oss-request-id` (needed by SDK)
3. **CDN without CORS**: Configuring CORS only on OSS but not on CDN
4. **Wrong origin format**: Including trailing slash or path in origin
5. **Case sensitivity**: HTTP methods must be uppercase (GET, not get)
6. **Max rules limit**: OSS supports up to 10 CORS rules per Bucket
