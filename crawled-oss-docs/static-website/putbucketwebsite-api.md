# PutBucketWebsite API

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketwebsite

## Overview

The `PutBucketWebsite` API enables static website hosting for an OSS bucket and configures routing rules (e.g., default index page, error page, redirects).

## Request Syntax

```http
PUT /?website HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<WebsiteConfiguration>
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>error.html</Key>
  </ErrorDocument>
</WebsiteConfiguration>
```

## Key Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `IndexDocument.Suffix` | String | Yes | The default homepage (e.g., `index.html`) |
| `ErrorDocument.Key` | String | No | The default error page (e.g., `error.html` or `404.html`) |
| `RoutingRules` | Container | No | Redirect and routing rules for conditional routing |

## Requirements

- **Permission**: You must have `oss:PutBucketWebsite` permission
- **Bucket ACL**: The bucket typically needs to be set to `public-read` for the website to be publicly accessible
- **Method**: PUT
- **Endpoint**: Accessed via `BucketName.oss-<region>.aliyuncs.com`

## Routing Rules (Optional)

You can add conditional redirects using `RoutingRules`:

```xml
<WebsiteConfiguration>
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>error.html</Key>
  </ErrorDocument>
  <RoutingRules>
    <RoutingRule>
      <RuleNumber>1</RuleNumber>
      <Condition>
        <KeyPrefixEquals>docs/</KeyPrefixEquals>
      </Condition>
      <Redirect>
        <RedirectType>Mirror</RedirectType>
        <MirrorURL>http://example.com/</MirrorURL>
      </Redirect>
    </RoutingRule>
    <RoutingRule>
      <RuleNumber>2</RuleNumber>
      <Condition>
        <HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals>
      </Condition>
      <Redirect>
        <RedirectType>External</RedirectType>
        <Protocol>https</Protocol>
        <HostName>example.com</HostName>
        <ReplaceKeyWith>404.html</ReplaceKeyWith>
        <HttpRedirectCode>302</HttpRedirectCode>
      </Redirect>
    </RoutingRule>
  </RoutingRules>
</WebsiteConfiguration>
```

### Redirect Types

| Type | Description |
|------|-------------|
| `Mirror` | Back-to-origin mirroring - fetches content from the specified MirrorURL |
| `External` | External URL redirect - redirects the request to an external URL |
| `AliCDN` | Alibaba Cloud CDN redirect |

### Condition Parameters

| Parameter | Description |
|-----------|-------------|
| `KeyPrefixEquals` | Match objects with the specified key prefix |
| `HttpErrorCodeReturnedEquals` | Match when the specified HTTP error code is returned |
| `IncludeHeader` | Match based on request headers |

### Redirect Parameters

| Parameter | Description |
|-----------|-------------|
| `RedirectType` | The redirect type (Mirror, External, AliCDN) |
| `Protocol` | The protocol for the redirect (http or https) |
| `HostName` | The target hostname |
| `ReplaceKeyWith` | Replace the object key with the specified value |
| `ReplaceKeyPrefixWith` | Replace the key prefix with the specified value |
| `HttpRedirectCode` | The HTTP redirect code (301, 302, 307) |
| `MirrorURL` | The mirror origin URL (for Mirror type only) |

## Related APIs

| API | Description |
|-----|-------------|
| `GetBucketWebsite` | Retrieve the current website configuration |
| `DeleteBucketWebsite` | Remove the website hosting configuration |

## Response

A successful response returns HTTP status code 200.

## Error Codes

| Error Code | HTTP Status | Description |
|-----------|-------------|-------------|
| `InvalidArgument` | 400 | Invalid parameters in the request body |
| `AccessDenied` | 403 | You do not have permission to perform this operation |
