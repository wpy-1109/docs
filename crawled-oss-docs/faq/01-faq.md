# OSS Frequently Asked Questions (FAQ)

> Source: Alibaba Cloud OSS Documentation - FAQ

## General Questions

### What is Alibaba Cloud OSS?

Alibaba Cloud Object Storage Service (OSS) is a cloud-based object storage service that provides secure, cost-effective, and highly durable storage for large amounts of data. It is designed to store and access any type of data from anywhere on the internet.

### What are the key features of OSS?

- Unlimited storage capacity with elastic scaling
- 99.9999999999% (12 nines) data durability
- Multiple storage classes for cost optimization
- Comprehensive security features (encryption, access control, compliance)
- Built-in image/video processing capabilities
- S3-compatible API
- Global acceleration and CDN integration

### What regions does OSS support?

OSS is available in all Alibaba Cloud regions worldwide, including:
- China: Beijing, Shanghai, Hangzhou, Shenzhen, Guangzhou, Chengdu, Hong Kong, etc.
- Asia Pacific: Singapore, Sydney, Tokyo, Mumbai, Jakarta, Seoul, etc.
- Europe: London, Frankfurt
- Middle East: Dubai
- Americas: US East (Virginia), US West (Silicon Valley)

---

## Bucket Questions

### How many buckets can I create?

Up to **100 buckets** per Alibaba Cloud account (soft limit). You can request an increase via Quota Center.

### Can I rename a bucket?

**No.** Bucket names cannot be changed after creation. You must create a new bucket and migrate data.

### What are the bucket naming rules?

- 3 to 63 characters
- Lowercase letters, numbers, and hyphens only
- Must start and end with a lowercase letter or number
- Globally unique across all Alibaba Cloud accounts

### Can I change the region of a bucket?

**No.** The region is set at creation and cannot be changed. Use Cross-Region Replication (CRR) to replicate data to another region.

### What happens when I delete a bucket?

The bucket must be empty (no objects, no incomplete multipart uploads). Deleting a bucket is irreversible. The bucket name becomes available for other users after deletion.

---

## Object Questions

### What is the maximum object size?

The maximum object size is **48.8 TB** for a single object (using multipart upload).

### What is the maximum size for a simple upload?

Simple upload supports objects up to **5 GB**. For larger objects, use multipart upload.

### Can I rename an object?

OSS does not have a native rename operation. To "rename," you must:
1. Copy the object to the new key
2. Delete the old object

### What is the maximum number of objects in a bucket?

There is **no limit** on the number of objects in a bucket.

### How do I organize objects in folders?

OSS uses a flat namespace. "Folders" are simulated using prefixes with `/` separators. For example, `images/2024/photo.jpg` appears as a folder structure but is actually a single object key.

---

## Upload & Download Questions

### What upload methods does OSS support?

| Method | Max Size | Use Case |
|--------|----------|----------|
| Simple Upload (PutObject) | 5 GB | Small files |
| Multipart Upload | 48.8 TB | Large files, resumable |
| Append Upload | 5 GB per append | Log files, streaming |
| Form Upload (PostObject) | 5 GB | Browser-based uploads |

### How do I upload files larger than 5 GB?

Use **multipart upload**:
1. Initialize the upload (InitiateMultipartUpload)
2. Upload parts in parallel (UploadPart), each 100 KB to 5 GB
3. Complete the upload (CompleteMultipartUpload)

ossutil and SDKs handle this automatically.

### How do I resume an interrupted upload?

Use multipart upload with checkpoint files:
```bash
ossutil cp largefile.zip oss://bucket/ --checkpoint-dir ./checkpoint
```

### How do I download large files efficiently?

- Use **Range GET** for parallel downloads
- Enable **Transfer Acceleration** for cross-region downloads
- Use **CDN** for frequently accessed content

### What is Transfer Acceleration?

Transfer Acceleration uses Alibaba Cloud's globally distributed edge nodes to accelerate uploads and downloads. It's especially useful for:
- Cross-border transfers
- Long-distance uploads/downloads
- Mobile applications with global users

---

## Access Control Questions

### What are the ACL options for buckets and objects?

| ACL | Description |
|-----|-------------|
| private | Only the owner can read/write (default) |
| public-read | Anyone can read, only owner can write |
| public-read-write | Anyone can read and write (not recommended) |

### How do I grant temporary access to a private object?

Use **signed URLs** (pre-signed URLs):
```bash
ossutil presign oss://bucket/private-object --expires 3600
```
This generates a URL valid for 1 hour.

### How do I grant cross-account access?

Use **bucket policies** to grant access to specific Alibaba Cloud accounts or RAM users from other accounts.

### What is the difference between RAM policies and bucket policies?

| Feature | RAM Policy | Bucket Policy |
|---------|-----------|---------------|
| Scope | Attached to user/role | Attached to bucket |
| Management | IAM console | OSS console/API |
| Cross-account | No (use STS) | Yes |
| IP/VPC restrictions | Limited | Full support |

---

## Storage Class Questions

### What storage classes does OSS offer?

| Class | Access Frequency | Min Duration | Retrieval |
|-------|-----------------|--------------|-----------|
| Standard | Frequent | None | Immediate |
| IA | < once/month | 30 days | Immediate |
| Archive | < once/quarter | 60 days | 1-5 minutes |
| Cold Archive | Rarely | 180 days | 1-12 hours |
| Deep Cold Archive | Almost never | 180 days | Up to 48 hours |

### How do I change an object's storage class?

1. **Manual**: Copy the object with `--storage-class` parameter
2. **Automatic**: Configure lifecycle rules for automatic transitions

### What is the minimum storage duration charge?

If you delete or transition an object before the minimum storage duration, you are still charged for the full minimum duration. For example, deleting an IA object after 15 days still incurs 30 days of storage charges.

---

## Lifecycle & Versioning Questions

### What are lifecycle rules?

Lifecycle rules automate storage management by:
- Transitioning objects between storage classes
- Expiring (deleting) objects after a specified period
- Aborting incomplete multipart uploads

### How do I enable versioning?

Enable versioning via the OSS Console, SDK, or API. Once enabled, versioning can be **suspended** but **not disabled**.

### How do I recover a deleted object?

With versioning enabled:
1. Deleted objects receive a **delete marker**
2. List versions to find the previous version ID
3. Copy the previous version to restore it, or delete the delete marker

### Can I use lifecycle rules with versioning?

Yes. You can set rules to:
- Expire current versions after N days
- Expire non-current versions after N days
- Delete expired delete markers

---

## Encryption Questions

### What encryption options does OSS support?

| Type | Description |
|------|-------------|
| SSE-KMS | Server-side encryption with KMS-managed keys |
| SSE-OSS | Server-side encryption with OSS-managed keys (AES-256) |
| Client-side | Application encrypts data before uploading |

### Is data encrypted in transit?

Yes, when using HTTPS endpoints. You can enforce HTTPS-only access via bucket policy.

---

## Image Processing Questions

### What image processing features does OSS support?

- Resize, crop, rotate, flip
- Watermark (text and image)
- Format conversion (JPEG, PNG, WebP, AVIF, etc.)
- Quality adjustment
- Blur, sharpen, brightness, contrast
- Circle crop, rounded corners
- Image info/metadata

### What is the maximum source image size for processing?

**20 MB** by default (adjustable via Quota Center).

### How do I process images?

Add `?x-oss-process=image/` parameters to the image URL:
```
https://bucket.oss-region.aliyuncs.com/photo.jpg?x-oss-process=image/resize,w_300/format,webp
```

---

## Billing Questions

### How is OSS billed?

OSS uses pay-as-you-go billing by default:
- **Storage**: Per GB per month (varies by storage class)
- **Requests**: Per 10,000 requests (GET, PUT, etc.)
- **Data Transfer**: Per GB for internet egress
- **Data Retrieval**: Per GB for IA/Archive storage classes

### How can I reduce costs?

1. Use appropriate storage classes
2. Configure lifecycle rules
3. Purchase Storage Capacity Units (SCUs) for discounts
4. Use CDN to reduce egress costs
5. Clean up incomplete multipart uploads
6. Use internal endpoints for same-region access (free)

### Is internal traffic free?

Yes, data transfer between OSS and other Alibaba Cloud services **in the same region** via internal endpoints is free.

---

## Compatibility Questions

### Is OSS compatible with Amazon S3?

Yes, OSS provides S3-compatible APIs. Most S3 SDKs and tools work with OSS by changing the endpoint:
```
s3.amazonaws.com -> oss-region.aliyuncs.com
```

### Can I use AWS SDKs with OSS?

Yes. Configure the endpoint to point to the OSS endpoint and provide your AccessKey credentials. Some advanced features may not be fully compatible.

### What tools can I use with OSS?

| Tool | Type | Best For |
|------|------|----------|
| ossutil | CLI | Automation, scripting |
| ossbrowser | GUI | Visual management |
| OSS Console | Web | Quick configuration |
| ossfs | FUSE | Mount as filesystem |
| ossftp | FTP | FTP-based access |
| Rclone | CLI | Cross-cloud sync |
| S3 Browser | GUI | S3-compatible access |
