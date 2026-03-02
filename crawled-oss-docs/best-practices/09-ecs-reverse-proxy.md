# ECS Reverse Proxy for OSS Access

Source: https://help.aliyun.com/zh/oss/user-guide/access-oss-through-ecs-reverse-proxy

## Overview

In some scenarios, you may need to access OSS through a reverse proxy running on an ECS instance rather than directly. Common use cases include:
- Custom domain access without CDN
- Adding custom business logic to OSS requests
- Routing requests through a private network
- Consolidating multiple storage backends behind a single endpoint

## Architecture

```
Client -> ECS (Nginx Reverse Proxy) -> OSS Bucket
```

The ECS instance acts as an intermediary, forwarding client requests to OSS and returning responses.

## Configuration with Nginx on Ubuntu/CentOS

### Step 1: Install Nginx

**Ubuntu**:
```bash
sudo apt update
sudo apt install nginx
```

**CentOS**:
```bash
sudo yum install nginx
```

### Step 2: Configure Nginx Reverse Proxy

Edit the Nginx configuration file:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://your-bucket.oss-cn-hangzhou-internal.aliyuncs.com;
        proxy_set_header Host your-bucket.oss-cn-hangzhou-internal.aliyuncs.com;

        # Optional: Hide OSS error details
        proxy_intercept_errors on;

        # Optional: Set proxy timeouts
        proxy_connect_timeout 10s;
        proxy_read_timeout 60s;
        proxy_send_timeout 60s;
    }
}
```

**Key Points**:
- Use the **internal endpoint** (`oss-cn-hangzhou-internal.aliyuncs.com`) when ECS and OSS are in the same region to avoid traffic fees
- Set the `Host` header to match the OSS Bucket endpoint
- Enable proxy error interception to return custom error pages

### Step 3: Enable HTTPS (Recommended)

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass https://your-bucket.oss-cn-hangzhou-internal.aliyuncs.com;
        proxy_set_header Host your-bucket.oss-cn-hangzhou-internal.aliyuncs.com;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}
```

### Step 4: Restart Nginx

```bash
sudo systemctl restart nginx
```

## Configuration on Windows (IIS)

For Windows ECS instances, configure IIS as a reverse proxy:
1. Install URL Rewrite and Application Request Routing (ARR) modules
2. Enable proxy in ARR
3. Create URL Rewrite inbound rules to forward requests to OSS

## Best Practices

### Performance
- Place ECS and OSS in the **same region** for internal network access (free traffic, lower latency)
- Configure appropriate proxy buffer sizes for large file transfers
- Enable Gzip compression on the proxy for text-based content

### Security
- Never expose the OSS AccessKey through the proxy
- Use signed URLs for private content access
- Configure rate limiting to prevent abuse
- Set up access logging for audit trails

### High Availability
- Use multiple ECS instances behind a Server Load Balancer (SLB)
- Configure health checks for the proxy servers
- Set up auto-scaling for traffic spikes

## When to Use Reverse Proxy vs. CDN

| Feature | ECS Reverse Proxy | CDN Acceleration |
|---|---|---|
| Global edge caching | No | Yes |
| Custom business logic | Yes | Limited |
| Cost | ECS instance cost | CDN traffic cost |
| Setup complexity | Higher | Lower |
| Best for | Custom routing, internal use | Public content distribution |

## Integration with HTTPDNS

For mobile applications, integrate Alibaba Cloud HTTPDNS with OSS SDK to avoid DNS hijacking:
- HTTPDNS provides DNS resolution via HTTP, bypassing local DNS
- Prevents man-in-the-middle attacks on DNS
- Improves resolution accuracy and speed
