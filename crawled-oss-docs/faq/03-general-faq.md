# OSS General FAQ

Source: https://help.aliyun.com/zh/oss/faq-overview

## Basic Concepts

### What is Alibaba Cloud OSS?
Alibaba Cloud Object Storage Service (OSS) is a massive, secure, low-cost, and highly reliable cloud storage service. It supports storing and accessing any type of data from anywhere on the internet. You can use OSS for various scenarios including data lake storage, website hosting, mobile app backends, backup and archiving, and big data analytics.

### What are the OSS storage classes?

| Storage Class | Use Case | Access Frequency | Min Storage Duration | Retrieval Time |
|---|---|---|---|---|
| **Standard** | Hot data, frequent real-time access | >1 access/month per file | None | Immediate |
| **Infrequent Access (IA)** | Warm data, less frequent access | <1 access/month per file | 30 days | Immediate |
| **Archive** | Cold data, long-term storage | <1 access/90 days per file | 60 days | ~1 minute (with Archive Direct Read) |
| **Cold Archive** | Rarely accessed data | <1 access/180 days per file | 180 days | 1-5 hours |
| **Deep Cold Archive** | Extremely rarely accessed data | Near-zero access | 180 days | 5-12 hours |

### What is the maximum file size supported?
- **Simple upload (PutObject)**: Up to 5 GB per file
- **Multipart upload**: Up to 48.8 TB per file (maximum 10,000 parts)
- **Console upload**: Up to 5 GB per file
- **Append upload**: Up to 5 GB per file

### How many Buckets can I create?
By default, you can create up to **100 Buckets** per Alibaba Cloud account. If you need more, submit a support ticket to request a quota increase.

### What are the Bucket naming rules?
- Length: 3-63 characters
- Characters: lowercase letters, numbers, and hyphens (-)
- Must start and end with a lowercase letter or number
- Cannot start with `http://` or `https://`
- Bucket names are **globally unique** across all Alibaba Cloud accounts

### What are the Object key naming rules?
- Length: 1-1023 bytes (UTF-8 encoded)
- Cannot start with `/` or `\`
- Object keys are case-sensitive
- Use forward slashes `/` as logical directory separators

## Access and Networking

### What are the OSS endpoints?
Each region has its own endpoints:

| Endpoint Type | Format | Example |
|---|---|---|
| Public | `oss-{region}.aliyuncs.com` | `oss-cn-hangzhou.aliyuncs.com` |
| Internal | `oss-{region}-internal.aliyuncs.com` | `oss-cn-hangzhou-internal.aliyuncs.com` |
| Transfer Acceleration | `oss-accelerate.aliyuncs.com` | Global acceleration endpoint |

**Important**: Internal endpoints are free of traffic charges and have lower latency when accessed from ECS in the same region.

### How do I bind a custom domain to a Bucket?
1. Navigate to **Bucket > Bucket Configuration > Domain Management**
2. Click **Bindomain**
3. Enter your custom domain name
4. Add a CNAME record in your DNS provider pointing to the Bucket domain
5. If in mainland China, domain must have ICP filing

### Can I access OSS from a VPC?
Yes. Use VPC endpoints or internal endpoints for private network access:
- Configure **PrivateLink** for VPC-level OSS access
- Use internal endpoints from ECS instances in the same region
- Configure **Access Points** for fine-grained VPC access control

## Security

### How do I control access to my OSS resources?
OSS provides multiple access control mechanisms:
1. **Bucket ACL**: Private, public-read, public-read-write
2. **Object ACL**: Per-object permission override
3. **RAM Policy**: Fine-grained IAM-based access control
4. **Bucket Policy**: Resource-based policy for cross-account access
5. **STS Temporary Credentials**: Time-limited access tokens
6. **Signed URLs**: Time-limited URLs for specific objects

### Does OSS support encryption?
Yes, OSS supports:
- **Server-Side Encryption (SSE-KMS)**: Keys managed by KMS
- **Server-Side Encryption (SSE-OSS)**: Keys managed by OSS (AES-256)
- **Client-Side Encryption**: User manages encryption/decryption

### How do I prevent hotlinking?
Configure **Referer whitelist** in Bucket settings:
1. Navigate to **Bucket > Permission Control > Anti-Hotlinking**
2. Add allowed Referer domains
3. Optionally deny empty Referer requests

## Billing

### How is OSS billed?
Main billing items:
- **Storage**: Based on volume and storage class
- **Traffic**: Outbound internet traffic (inbound is free; internal traffic is free)
- **Requests**: Per API request count
- **Data processing**: Image processing, video snapshots, etc.
- **Data retrieval**: For IA/Archive/Cold Archive objects

### Is there a free tier?
New users may receive trial quotas. Check the Alibaba Cloud console for current promotions.

### How can I reduce costs?
- Use **lifecycle rules** to transition cold data to lower-cost storage
- Use **internal endpoints** from same-region ECS (free traffic)
- Purchase **resource packages** for predictable workloads (20-40% savings)
- Enable **CDN** to reduce direct OSS outbound traffic
- Clean up **incomplete multipart uploads** (they consume storage)
- Delete unnecessary **historical versions** when using versioning

## Data Management

### Can I recover deleted files?
- **With versioning enabled**: Yes, deleted objects have delete markers and previous versions can be restored
- **Without versioning**: No, deleted objects cannot be recovered
- **With HBR backup**: Yes, restore from backup snapshots

### Does OSS support file/folder operations?
OSS is a flat key-value store. Directories are simulated using `/` delimiters in object keys. You can:
- Create "directories" by uploading objects with keys containing `/`
- List objects under a "directory" using prefix and delimiter parameters
- There is no separate directory creation API (directories are virtual)

### What is the maximum number of objects per Bucket?
There is no limit on the number of objects per Bucket. OSS can store an unlimited number of objects.

## Tools

### What tools can I use to manage OSS?
- **OSS Console**: Web-based management interface
- **ossutil**: Official CLI tool
- **ossbrowser**: GUI tool for desktop
- **OSS SDKs**: Available for Java, Python, Node.js, Go, PHP, .NET, C++, Ruby, Browser.js, Android, iOS
- **Alibaba Cloud CLI**: General-purpose Alibaba Cloud CLI with OSS support

### Can I mount OSS as a file system?
Yes, using **ossfs** (FUSE-based tool) on Linux:
- Mount a Bucket as a local directory
- Supports basic file operations (read, write, delete, list)
- Not recommended for high-performance or concurrent workloads
- Suitable for simple file sharing and log collection scenarios
