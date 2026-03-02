# OSS Frequently Asked Questions (FAQ) - Official

> Source: https://www.alibabacloud.com/help/en/oss/faq-15

## General FAQ

### What is Alibaba Cloud OSS?

Alibaba Cloud OSS is a secure, cost-effective, highly durable, and scalable storage service that allows you to store a large volume of data. OSS is designed to provide data durability of at least 99.9999999999% (twelve 9s) and service availability of at least 99.995%.

### What are the features of OSS?

OSS supports RESTful API operations. You can store and access data from all applications anytime and anywhere. OSS is highly scalable and you are charged only for the resources that you use. OSS provides:

- OSS SDKs and migration tools
- Multiple storage classes (Standard, IA, Archive, Cold Archive, Deep Cold Archive)
- Image and media processing capabilities
- Seamless CDN integration

### Who are the intended users of OSS?

OSS is suitable for users who need to store large volumes of data:

- **Audio, video, and image applications**: Short video storage, live recording, video on demand, photo sharing
- **Education**: Online education platforms storing large volumes of data
- **AI and IoT**: Autonomous driving training data, video surveillance
- **Cinematic rendering**: Media assets storage and intelligent processing
- **Genomics**: Raw genomic data storage and analytics

### What data does OSS store?

OSS stores attachments, high-definition images, audio and video objects, backup objects, file synchronization data, and online storage system objects.

### What is the upper limit of data volume?

OSS does not impose limits on total storage capacity or bucket capacity. Objects up to 5 GB can be uploaded via the console. For larger objects (up to 48.8 TB), use multipart upload, ossbrowser, or ossutil.

### What are the storage classes of OSS?

| Storage Class | Description |
|---------------|-------------|
| Standard | Hot data, frequently accessed |
| Infrequent Access (IA) | Data accessed less than once per month |
| Archive | Data accessed less than once per quarter |
| Cold Archive | Long-term archival, rarely accessed |
| Deep Cold Archive | Compliance archival, almost never accessed |

### How do I select an appropriate storage class?

The billable size, storage duration, restoration time, and data retrieval costs vary by storage class. If 70% of your data is not accessed for more than 30 days, store it as IA or Archive. Use lifecycle rules for automatic transitions.

### Does Alibaba Cloud use data stored in OSS?

No. Alibaba Cloud does not use or disclose your data without authorization. Data is processed only based on your service requirements or legal requirements.

### How does OSS handle traffic spikes?

OSS is designed to handle traffic spikes from Internet applications. Pay-as-you-go pricing and unlimited capacity ensure uninterrupted service. OSS balances loads to prevent impact from spikes.

### How is data organized in OSS?

OSS is a distributed object storage service using key-value pair format. OSS uses a flat structure for objects stored in buckets. Directories are simulated using key prefixes with `/` separators.

### What intelligent features does OSS support?

- Integration with Hadoop, Spark, MaxCompute, Batch Compute, HPC, EMR
- Image processing and content detection
- Intelligent Media Management (IMM) integration

---

## FAQ about Regions

### Where is my data stored?

When you create a bucket, you specify a region. By default, OSS backs up data to one zone. With zone-redundant storage (ZRS), data is stored across multiple zones.

### How do I determine which region to use?

Consider physical locations, relationships between cloud services, and resource prices.

---

## FAQ about Billing

### How are users charged?

OSS supports pay-as-you-go billing. No minimum usage fee. Resource plans are available for cost savings.

### How am I charged when other accounts access my OSS resources?

You are charged based on standard pricing. Enable pay-by-requester mode to shift costs to requesters.

### How do I deactivate OSS?

OSS does not have a deactivation feature. Delete your resources to stop charges.

---

## FAQ about Security

### Is data stored securely?

Yes. Only the resource owner can access resources by default. OSS provides user identity verification and access control policies (ACLs, RAM policies, bucket policies).

### What access control methods are available?

- **ACLs**: Bucket-level and object-level (private, public-read, public-read-write)
- **RAM Policies**: Fine-grained identity-based policies
- **Bucket Policies**: Resource-based policies with IP/VPC restrictions

### What encryption methods does OSS provide?

- **Server-side encryption (SSE)**: OSS encrypts objects before storage, decrypts on download
- **Client-side encryption**: Objects encrypted locally before upload

### How do I prevent accidental deletion?

Enable **versioning** to protect against unintended overwrites/deletions. Previous versions are preserved and recoverable.

### What is a retention policy (WORM)?

Write Once Read Many (WORM) prevents objects from being deleted or overwritten for a specified period. Suitable for medical records, contracts, compliance data.

### Does OSS support online object modification?

No. Download the object, modify locally, and re-upload.

### Does OSS use the triplicate mechanism?

No. OSS uses erasure coding (EC) for storage performance and reliability.

### How is the 99.995% uptime calculated?

- Error rate per 5 minutes = Failed requests / Total valid requests x 100%
- Uptime = (1 - Sum of error rates / Total 5-minute periods) x 100%

---

## FAQ about Data Replication

### How do I replicate data across regions?

Use Cross-Region Replication (CRR). Multiple CRR rules can be configured per bucket for automatic, asynchronous replication.

### What are the advantages of CRR?

- **Compliance**: Store replicas at geographic distance
- **Low latency**: Serve users from closest region
- **Disaster recovery**: Maintain replicas in separate data centers
- **Data migration**: Move data between regions

### How am I charged for CRR?

Cross-region traffic and per-request fees are charged on pay-as-you-go basis. Resource plans are not available for CRR.

---

## FAQ about Data Query

### How do I query data in OSS?

Use the **SelectObject** operation with SQL statements to query specific data in CSV or JSON objects. This avoids downloading entire objects for analysis.

---

## FAQ about Storage Management

### What is OSS lifecycle management?

Configure lifecycle rules to:
- Delete objects no longer accessed
- Transition storage classes (e.g., Standard -> IA -> Archive)
- Reduce storage costs automatically

### Example Lifecycle Scenarios

**Medical records**: Convert to Archive 180 days after upload.

**Call records**: Frequent access for 2 months, occasional for 6 months, delete after 2 years.

---

## FAQ about Objects

### Maximum object size?

48.8 TB per object (using multipart upload).

### Maximum simple upload size?

5 GB. Use multipart upload for larger files.

### Can I rename an object?

No native rename. Copy to new key, then delete the old one.

### Maximum objects per bucket?

No limit.

### How do I organize objects in folders?

Folders are simulated using key prefixes with `/` separators. OSS uses a flat namespace.

---

## FAQ about Buckets

### How many buckets can I create?

100 per account (soft limit, requestable increase).

### Can I rename a bucket?

No. Create a new bucket and migrate data.

### Can I change a bucket's region?

No. Use CRR to replicate data to another region.

---

## FAQ about Access Control

### What is the difference between RAM policies and bucket policies?

| Feature | RAM Policy | Bucket Policy |
|---------|-----------|---------------|
| Scope | User/role | Bucket/resource |
| Cross-account | Use STS | Yes |
| IP/VPC restrictions | Limited | Full support |

### How do I grant temporary access?

Use **signed URLs** or **STS temporary credentials**.

---

## FAQ about Encryption

### What encryption options?

| Type | Description |
|------|-------------|
| SSE-KMS | KMS-managed keys with rotation |
| SSE-OSS | OSS-managed AES-256 keys |
| Client-side | Application-level encryption |

### Is data encrypted in transit?

Yes, when using HTTPS endpoints.

---

## FAQ about Image Processing

### What features are supported?

Resize, crop, rotate, flip, watermark, format conversion, quality adjustment, blur, sharpen, brightness, contrast, circle crop, rounded corners, image info.

### Maximum source image size?

20 MB (adjustable via Quota Center).

### How do I process images?

Add `?x-oss-process=image/` parameters to the image URL.
