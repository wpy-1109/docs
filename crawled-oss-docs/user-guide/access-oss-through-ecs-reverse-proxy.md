# Access OSS through an ECS reverse proxy

The dynamic IP addresses of OSS endpoints can complicate firewall whitelist configurations and other integrations requiring a fixed IP, often resulting in failed or restricted access. A common solution is to deploy an Nginx reverse proxy on an ECS instance that has a static public IP. By routing traffic through this instance, the proxy forwards requests to OSS, thereby providing a stable IP address for accessing your OSS resources.

## How it works


This solution uses one or more ECS Instances with static public IP addresses as traffic gateways. Nginx runs as a reverse proxy on these instances, forwarding public access requests to OSS. The workflow is as follows:


-

A client initiates a request to access an OSS resource through the Static Public IP Address (or an Elastic IP Address (EIP)) of the ECS Instance.

-

The Nginx service on the ECS Instance receives and processes the request.

-

Based on its configuration, Nginx forwards the request to the target OSS bucket.

-

OSS processes the request and returns the response data to Nginx.

-

Nginx sends the response data back to the client, completing the proxy process.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/4304963671/CAEQTBiBgMD4w9nfyRkiIDIxNDY0MzY5Y2UxMDRmZDBhNjRjOWIyYWRhNDcxY2Jm5700039_20250910163454.791.svg)
## Configure the ECS reverse proxy

#### Step 1: Create an ECS instance


The Nginx reverse proxy runs on the ECS instance.


-

Log on to the [ECS console](https://ecs.console.alibabacloud.com/) and click Create Instance.

-

Create an ECS instance with the following configurations. Keep the default settings for other options.


-

Billing Method: Select Pay-As-You-Go.

-

Region: Select the same Region as your target OSS bucket. This lets you use the internal endpoint, which saves on traffic costs.

-

Network and Zone: Select the default Virtual Private Cloud (VPC) and Availability Zone (AZ).

-

Instance: Click All Instance Types. Then, search for and select `ecs.e-c1m2.large`.


> NOTE:

> NOTE: 


> NOTE: Note 

If this instance type is sold out, select another one.


-

Image: Select Public Image > Alibaba Cloud Linux (Alibaba Cloud Linux 3.2104 LTS 64-bit).

-

System Disk: Set the capacity of the Enterprise SSD (ESSD) to 40 GiB.

-

Public IP Address: Select Assign Public IPv4 Address.

-

Bandwidth Billing Method: Select Pay-by-traffic (CDT) to save costs.

-

Maximum Bandwidth: Select 5 Mbps or higher.

-

Security Group: Select New Security Group. Under Open IPv4 Ports/Protocols, select HTTP (TCP：80) to allow traffic to the Nginx listening port.

-

Logon Credentials: Select Custom Password. Set the username to root and create a Logon Password. Store your password securely.

#### Step 2: Install and configure the Nginx reverse proxy


After creating the ECS instance, install Nginx and configure its reverse proxy rules.


-

Install the Nginx service.


`shell
yum install -y nginx
`


-

Create and edit the configuration file. For easier management, create a separate configuration file, such as `oss_proxy.conf`, in the `/etc/nginx/conf.d/` directory.


`shell
vi /etc/nginx/conf.d/oss_proxy.conf
`


Copy the following production-grade configuration template into the file. Modify the internal endpoint of the bucket and the public IP address of the ECS instance as indicated in the comments.


`nginx
# Define the OSS backend and enable keep-alive connections for better performance.
upstream oss_backend {
    # [Required] Replace the string "your-bucket.oss-cn-hangzhou-internal.aliyuncs.com" with the internal endpoint of your bucket.
    server your-bucket.oss-cn-hangzhou-internal.aliyuncs.com:80;
    # Recommended number of keep-alive connections. Adjust based on concurrent traffic
    keepalive 64;
}

# Define the log format for the production environment, including key information such as upstream response time.
log_format production '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for" '
                      'rt=$request_time uct="$upstream_connect_time" uht="$upstream_header_time" urt="$upstream_response_time"';

server {
    listen 80;
    # [Required] Replace the string "your_ecs_public_ip_or_domain" with the public IP address of the ECS instance or a domain name that resolves to this IP.
    server_name your_ecs_public_ip_or_domain;

    # Access log path and format.
    access_log /var/log/nginx/oss_proxy.access.log production;
    error_log /var/log/nginx/oss_proxy.error.log;

    # Dynamic DNS resolution to ensure Nginx is aware of OSS backend IP changes.
    resolver 100.100.2.136 100.100.2.138 valid=60s;

    # Health check endpoint for load balancers or monitoring systems.
    location /health {
        access_log off;
        return 200 "healthy";
    }

    location / {
        # Proxy requests to the upstream OSS backend.
        proxy_pass http://oss_backend;

        # Critical: Ensure HTTP/1.1 and keep-alive connections are enabled
        proxy_http_version 1.1;
        proxy_set_header Connection "";

        # Critical: Set the Host header to the bucket's internal endpoint to ensure signature validation passes.
        # [Required] Replace the string "your-bucket.oss-cn-hangzhou-internal.aliyuncs.com" with the internal endpoint of your bucket.
        proxy_set_header Host "your-bucket.oss-cn-hangzhou-internal.aliyuncs.com";

        # Forward the client's real IP address.
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;

        # Set proxy timeout values.
        proxy_connect_timeout 10s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;

        # Maximum allowed size for file uploads. 0 means unlimited. Set according to your business needs.
        client_max_body_size 1024m;
    }
}
`


Confirm the configuration, save the file and exit the editor.

-

Check the Nginx configuration file for syntax errors.


`shell
nginx -t
`


If the output shows `syntax is ok` and `test is successful`, the configuration syntax is correct.

-

Start the Nginx service to apply the configuration.


`shell
systemctl start nginx
`


## Verify the reverse proxy


Choose a verification method based on your bucket's access permissions.

#### Public-read and public-read-write buckets


To access an object in OSS, use the URL `http://<ecs_public_ip>/<object_path>` in a web browser. Replace `<ecs_public_ip>` with your ECS instance's Public IP Address (which you can find in the [ECS console](https://ecs.console.alibabacloud.com/server)), and `<object_path>` with the object's path within the bucket. For example, if the object `dest.jpg` is in the `exampledir` directory of your bucket, the `<object_path>` is `exampledir/dest.jpg`. The following figure shows a successful access attempt:


![image.jpeg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3218867571/p1006506.jpeg)

#### Private buckets


If the bucket is private, the access URL must include a signature. The following steps show how to obtain a signed URL for an object from the console. For more information about signatures, see [Signature V4 (recommended)](https://www.alibabacloud.com/help/en/oss/developer-reference/add-signatures-to-urls).


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the desired bucket.

-

Find the target object and click Details in the Actions column.

-

Click Copy File URL. In the copied URL, replace https with http and the bucket's domain name with the public IP address of your ECS instance.

-

Access the modified URL in your browser.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3218867571/p1005891.png)

## Apply in production


For production environments, follow these best practices for service stability, security, and cost-effectiveness.

#### Best practices


-

High availability architecture: Use a production architecture of "Server Load Balancer (SLB) + ECS Instances across multiple Availability Zones" to avoid a single point of failure.

-

Enable HTTPS: In a production environment, enforce HTTPS access to secure data in transit. This requires configuring an SSL certificate for Nginx and setting up automatic redirection from HTTP to HTTPS.


> NOTE:

> NOTE: 


> NOTE: Note 

To enable HTTPS access, ensure the security group for your ECS instance has an inbound rule that allows traffic on TCP port 443.


For further instructions, see [Use security groups](https://www.alibabacloud.com/help/en/ecs/user-guide/start-using-security-groups).


`nginx
# ... upstream and log_format configurations remain the same ...

# HTTP server block: Force redirect to HTTPS
server {
    listen 80;
    # [Required] Replace the string "your_ecs_public_ip_or_domain" with the public IP address of the ECS instance or a domain name that resolves to this IP.
    server_name your_ecs_public_ip_or_domain;

    # Redirect all HTTP requests to HTTPS with a 301 status code.
    return 301 https://$host$request_uri;
}

# HTTPS server block: Handle the actual proxy service.
server {
    # Listen on port 443 for SSL connections.
    listen 443 ssl http2;
    # [Required] Replace the string "your_ecs_public_ip_or_domain" with the public IP address of the ECS instance or a domain name that resolves to this IP.
    server_name your_ecs_public_ip_or_domain;

    # --- SSL certificate configuration ---
    # [Required] Replace the following strings with the paths to your SSL certificate and private key files.
    ssl_certificate /path/to/your/fullchain.pem;
    ssl_certificate_key /path/to/your/private.key;

    # --- SSL security enhancement configuration ---
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # Access log path and format.
    access_log /var/log/nginx/oss_proxy.access.log production;
    error_log /var/log/nginx/oss_proxy.error.log;

    # Dynamic DNS resolution (same as original configuration).
    resolver 100.100.2.136 100.100.2.138 valid=60s;

    # Health check endpoint (same as original configuration).
    location /health {
        access_log off;
        return 200 "healthy";
    }

    location / {
        # ... all proxy_* configurations are identical to the original ...
        proxy_pass http://oss_backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        # [Required] Replace the string "your-bucket.oss-cn-hangzhou-internal.aliyuncs.com" with the internal endpoint of your bucket.
        proxy_set_header Host "your-bucket.oss-cn-hangzhou-internal.aliyuncs.com";
        proxy_set_header X-Forwarded-For $proxy_add_x_forw_for;
        proxy_set_header X-Real-IP $remote_addr;
        # Add the X-Forwarded-Proto header to let the backend know the client is accessing via HTTPS.
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 10s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
        client_max_body_size 1024m;
    }
}
`


-

Configure proxy buffers: For large file transfers, enable and configure proxy buffers. This optimizes memory usage and improves performance by preventing slow clients from holding open long-lived connections to the backend OSS. Add the following configuration to the location block:


`nginx
location / {
    # ... other proxy_* configurations ...

    # Enable proxy buffering and set the number and size of buffers.
    proxy_buffering on;
    proxy_buffers 8 128k;
    proxy_buffer_size 128k;
    proxy_busy_buffers_size 256k;
}
`


-

Use EIPs: Bind an Elastic IP Address (EIP) to the entry point of your proxy cluster (either an SLB or an ECS instance) to ensure a stable public IP address.

-

Use a domain name for access: We recommend resolving a domain name to the proxy server's IP address and serving traffic through that domain. This simplifies future maintenance and scaling.

#### Fault tolerance strategies


-

Health check: To automatically isolate failed instances, configure your load balancer to perform regular health checks on Nginx's `/health` endpoint.

-

Timeout settings: Properly configure Nginx's `proxy_connect_timeout`, `proxy_read_timeout`, and other timeout parameters to prevent connection buildup from backend OSS latency.

-

Retry mechanism: If your client application supports it, add retry logic at the application layer for 5xx errors.

#### Risk prevention


-

Security hardening: In your ECS Security Group and network ACLs, allow access only from necessary IP addresses and ports. Consider deploying a Web Application Firewall (WAF) in front of the proxy to defend against common web attacks.

-

Monitoring and alerting: Monitor Nginx's access and error logs, along with key performance indicators such as request latency, error rate, and the ECS instance's CPU, memory, and network utilization. Set appropriate alert thresholds for these metrics.

-

Change and rollback management: Thoroughly test any changes to the Nginx configuration. To enable quick rollbacks if errors occur, keep historical versions of configuration files.

## FAQ

#### How can I preview images or web files from a bucket in a browser?


Due to OSS security mechanisms, accessing images or web files through the default domain name forces a download instead of an in-browser preview. To preview these objects directly in a browser, map a custom domain name to the bucket and use that custom domain name in your Nginx configuration. For more information, see [Access OSS through a custom domain name](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names).

#### Troubleshooting 403 Forbidden errors when accessing private buckets


A 403 error typically indicates a problem with signature validation or permissions. Follow these steps to troubleshoot:


-

Check the Nginx configuration: Make sure that the value set for the `proxy_set_header Host` directive exactly matches the internal endpoint of the bucket you are accessing. This is a critical factor for V4 signature validation.

-

Check signature generation: Confirm that the `Host` header used to calculate the signed URL is identical to the `Host` header in your Nginx configuration.

-

Check bucket permissions: Verify whether the bucket policy or RAM policy grants the necessary permissions for the operation.

-

Check ECS role authorization: If your application accesses OSS through an ECS Instance RAM Role, ensure the role has been granted the appropriate permissions to access the target bucket.

#### What should I do if a large file upload fails with a 413 Request Entity Too Large error?


This error occurs because the size of the uploaded file exceeds Nginx's default limit. In your Nginx configuration file, adjust the `client_max_body_size` value in the `server` or `location` block. For example, `client_max_body_size 2048m;` allows uploads up to 2 GB. Reload the Nginx configuration for the change to take effect.

#### Access fails occasionally with a 502 Bad Gateway error in the Nginx logs. What is the cause?


A 502 error indicates that Nginx could not get a valid response from the backend (OSS). Possible causes include:


-

DNS resolution issue: Ensure the `resolver` directive is in your Nginx configuration. Without it, Nginx might use a cached, stale IP address to access OSS.

-

Network connectivity: Check the outbound rules of the ECS instance's security group and any network ACL settings to ensure they allow access to the target region's OSS endpoint.

-

Endpoint configuration error: Verify that the endpoint specified in `proxy_pass` and `proxy_set_header Host` is spelled correctly and is valid.

#### How can I use a single Nginx instance to proxy multiple different buckets?


Use Nginx's `map` directive to dynamically select a backend bucket based on the request's `Host` header.


`nginx
# /etc/nginx/conf.d/multi_oss_proxy.conf

# Dynamically map the Host header to the OSS internal endpoint.
map $http_host $oss_backend_host {
    # [Required] Map a.example.com to the internal endpoint of bucket-a.
    "a.example.com" "bucket-a.oss-cn-hangzhou-internal.aliyuncs.com";
    # [Required] Map b.example.com to the internal endpoint of bucket-b.
    "b.example.com" "bucket-b.oss-cn-shenzhen-internal.aliyuncs.com";
    # Default value. This value can be left unset or point to a default bucket.
    default "";
}

server {
    listen 80;
    # Listen on multiple domain names.
    server_name a.example.com b.example.com;

    # ... other configurations such as logs, resolver, etc. ...

    location / {
        # If the mapping result is empty, a 404 error is returned.
        if ($oss_backend_host = "") {
            return 404;
        }

        # Dynamically set the proxy_pass and Host header.
        proxy_pass http://$oss_backend_host;
        proxy_set_header Host $oss_backend_host;

        # ... other proxy_* configurations ...
    }
}
`


Thank you! We've received your  feedback.