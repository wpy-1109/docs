# CDN Acceleration for OSS

Source: https://help.aliyun.com/zh/oss/user-guide/cdn-acceleration

## Overview

CDN acceleration provides global distributed caching for OSS. When distributing static resources (images, audio/video, documents) to global users, CDN significantly improves access speed, reduces latency, and lowers traffic costs.

## How It Works

1. **Request Routing**: User request is routed via intelligent DNS to the nearest CDN node with optimal network conditions
2. **Origin Fetch**: If the CDN node has no cached copy, it fetches from the OSS origin
3. **Cache Storage**: CDN node caches the resource according to preset cache rules and returns it to the user
4. **Cache Hit**: Subsequent requests for the same resource are served directly from CDN cache without origin fetch

## Quick Setup

### Prerequisites
- A registered domain name
- ICP filing completed if acceleration region includes mainland China

### Step 1: Add CDN Acceleration Domain and Configure Origin

1. Go to CDN Console > Add Domain
2. Select acceleration region and business type
3. Enter acceleration domain (recommend using subdomain like `oss.example.com`)
4. Add source as **OSS Domain** and select target Bucket
5. Complete domain addition

### Step 2: Configure CNAME DNS Record

1. Go to DNS Console > Target domain > Resolution Settings
2. Add CNAME record:
   - **Record Type**: CNAME
   - **Host Record**: `@` (main domain) or subdomain prefix (e.g., `oss`)
   - **Record Value**: CDN-assigned CNAME (e.g., `oss.example.com.w.cdngslb.com`)

DNS propagation may take minutes to hours depending on TTL settings.

### Step 3: Enable Private Bucket Origin Access

For private Buckets, enable Private Bucket Back-to-Origin in CDN console:
1. Navigate to target domain > Back-to-Origin Configuration
2. Enable **Alibaba Cloud OSS Private Bucket Back-to-Origin**
3. Select **Same Account** or **Cross Account** back-to-origin

**Important**: After enabling, clients must use URLs **without** signature parameters. URLs with `Expires`, `Signature` parameters will cause 403 errors.

### Step 4: Verify Acceleration

Compare loading times between OSS direct URL and CDN-accelerated URL. Check the `X-Cache` response header:
- **HIT**: Successfully served from CDN cache
- **MISS**: Cache miss, fetched from origin

## Scenario: Video and Large File Acceleration

### Required Configuration
- **Enable Range Back-to-Origin**: Allows CDN to request large files in segments (supports video seek and resumable download)
- **Set Long Cache Times**: Videos rarely update; recommend 30+ days cache
- **Use Resource Prefetch**: Pre-distribute videos to edge nodes before publication

### Video Bitrate Guidelines

| Bitrate | Use Case | Notes |
|---|---|---|
| 500-2000 kbps | Mobile, standard quality | Recommended, smooth loading |
| 2000-4000 kbps | Desktop, HD quality | Requires sufficient user bandwidth |
| >6000 kbps | Ultra HD/4K | May load slowly; provide multiple bitrate versions |

## Scenario: Multi-Bucket Origin Configuration

### Option 1: Independent Subdomain Architecture

| Resource Type | Subdomain | Configuration |
|---|---|---|
| Images | `img.example.com` | Long-term cache strategy |
| Audio/Video | `video.example.com` | Enable Range back-to-origin |
| Sensitive Documents | `docs.example.com` | Enable URL authentication |

**Advantages**: Semantic subdomains, DNS-level traffic splitting, independent cache/security/monitoring per Bucket.

### Option 2: Unified Domain with Path Routing

Use CDN rules engine to route different paths to different Buckets:
- `http://oss.example.com/bucket1/*` -> cdn-bucket1
- `http://oss.example.com/bucket2/*` -> cdn-bucket2

Configure URL rewrite rules to strip virtual paths:
```
^/bucket1/(.*)$ -> /$1 (break)
^/bucket2/(.*)$ -> /$1 (break)
```

### Cross-Account Private Bucket Origin

Use CDN acceleration domain from Account A to fetch from Account B's private Bucket:
1. Add OSS custom origin with target Bucket domain
2. Enable cross-account private Bucket back-to-origin
3. Provide AccessKey ID and Secret with target Bucket access

## Production Best Practices

### Security: Enable HTTPS
- Configure HTTPS certificate for acceleration domain
- Enable forced HTTPS redirect
- Note: Wildcard certificates (`*.example.com`) only match second-level domains
- OSS does not support HTTP/2; use CDN for HTTP/2 support

### Performance: Cache Strategy

| File Type | Recommended Cache Time | Notes |
|---|---|---|
| Rarely updated static files (images, videos) | 1+ months | Minimize unnecessary origin fetches |
| Frequently updated static files (JS, CSS) | Hours to days | Use version numbers (e.g., `style.v1.1.css`) |
| Dynamic files or APIs | 0 seconds (no cache) | Always fetch latest content |

### Enable Image Processing with CDN
By default CDN filters all URL parameters for cache optimization. To use OSS image processing (`?x-oss-process=...`):
- Set parameter handling to **Retain All Parameters** or **Retain Specified Parameters** (`x-oss-process`)

### Resource Prefetch and Auto-Refresh
- **Prefetch**: Pre-distribute hot resources before launches/events
- **Auto-refresh**: Enable CDN Cache Auto-Refresh in Bucket domain management; OSS triggers CDN refresh on file updates

### CORS Configuration
Configure CORS headers at CDN level (not just OSS) to prevent caching issues:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, GET, HEAD, PUT, DELETE
Access-Control-Max-Age: 3600
```

### Large File Optimization
- **Enable Range Back-to-Origin** for video/large file distribution
- **Enable Gzip Compression** for text files (JS, CSS, HTML)

### Zero-Downtime Domain Migration
1. Complete CDN configuration and test in staging
2. Gradual traffic migration during off-peak hours
3. Monitor access logs and error rates
4. Full migration after verification
5. Maintain rollback plan

## Security: Anti-Hotlinking

- **Referer whitelist/blacklist**: Validate HTTP Referer header
- **URL Authentication**: For private Buckets with CDN, enable CDN-level URL authentication
- **Important**: CDN hotlink requests may hit cache without reaching OSS, bypassing OSS anti-hotlinking. Always configure anti-hotlinking at CDN level.

## Billing

| Fee Type | Description |
|---|---|
| CDN fees | CDN traffic charges for accelerated access |
| OSS fees | CDN back-to-origin outbound traffic when cache misses occur |

## FAQ

### CDN back-to-origin 5xx errors
Check: source site configuration, HTTPS certificates, network connectivity, origin server load.

### 403 Forbidden with static website hosting + CDN
**Cause**: CDN private back-to-origin sends signed requests, but OSS static hosting requires anonymous requests. **Solution**: Use CDN URL rewrite (`^/$` -> `/index.html`) instead of OSS static hosting.

### Can I upload files via CDN domain?
Not recommended for security reasons. Use OSS domain with minimal permissions for uploads.

### CDN acceleration reduces OSS outbound traffic?
Yes, if CDN cache hit rate is high. Higher hit rate = less origin traffic = more cost savings.

### Why does OSS still incur outbound traffic after CDN?
Possible causes: direct OSS access in code, low CDN cache hit rate, public-read Bucket targeted by malicious access.
