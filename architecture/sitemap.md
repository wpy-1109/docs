# Alibaba Cloud OSS Documentation - Complete Site Map

## Overview

This site map defines the full page hierarchy for the rebuilt Alibaba Cloud OSS documentation. Pages are organized across 5 primary tabs with progressive disclosure from beginner to advanced. Estimated total: ~250 final pages.

---

## Tab 1: Get Started

```
get-started/
  index.mdx                                    # Landing page with hero, Cards, quick navigation
  what-is-oss.mdx                              # Product overview, features, use cases
  quickstart/
    console.mdx                                # Quickstart: OSS Console
    cli.mdx                                    # Quickstart: ossutil CLI
    sdk.mdx                                    # Quickstart: SDK (multi-language CodeGroup)
  concepts/
    buckets.mdx                                # What are buckets, naming, properties
    objects.mdx                                # What are objects, keys, metadata
    regions-and-endpoints.mdx                  # Regions, endpoints, internal vs public
    storage-classes.mdx                        # Standard, IA, Archive, Cold Archive, Deep Cold Archive
    access-control-overview.mdx                # Overview of RAM, bucket policy, ACL, STS
    naming-conventions.mdx                     # Bucket and object naming rules
    limits.mdx                                 # Service limits and quotas
    consistency-model.mdx                      # Strong consistency guarantees
```

## Tab 2: Guides

```
guides/
  buckets/
    create-bucket.mdx                          # Create a bucket (Console + SDK)
    list-buckets.mdx                           # List and query buckets
    query-bucket-info.mdx                      # Get bucket metadata and stats
    delete-bucket.mdx                          # Delete a bucket
    bucket-tagging.mdx                         # Manage bucket tags
    resource-groups.mdx                        # Configure resource groups
    pay-by-requester.mdx                       # Enable requester-pays
    storage-capacity.mdx                       # View bucket resource usage
  objects/
    upload-objects.mdx                         # Simple upload (multi-language CodeGroup)
    multipart-upload.mdx                       # Multipart upload for large files
    append-upload.mdx                          # Append upload
    form-upload.mdx                            # POST (form-based) upload
    resumable-upload.mdx                       # Resumable upload
    upload-callback.mdx                        # Server-side upload callbacks
    download-objects.mdx                       # Simple download
    range-download.mdx                         # Partial / range download
    resumable-download.mdx                     # Resumable download
    conditional-download.mdx                   # Conditional download (If-Modified-Since, etc.)
    streaming-upload-download.mdx              # Streaming upload and download
    copy-objects.mdx                           # Copy objects (simple + multipart copy)
    move-rename-objects.mdx                    # Move / rename objects
    delete-objects.mdx                         # Delete single and multiple objects
    restore-objects.mdx                        # Restore Archive / Cold Archive objects
    manage-object-metadata.mdx                 # Set and query object metadata
    object-tagging.mdx                         # Manage object tags
    manage-directories.mdx                     # Create, list, and delete directories
    manage-symbolic-links.mdx                  # Create and read symbolic links
    prevent-overwrite.mdx                      # Prevent object overwrite
    select-object.mdx                          # Query CSV/JSON objects (OSS Select)
    single-connection-throttling.mdx           # Single-connection bandwidth throttling
    progress-bars.mdx                          # Upload/download progress tracking
  access-control/
    ram-policies.mdx                           # RAM policy configuration
    bucket-policies.mdx                        # Bucket-level access policies
    acls.mdx                                   # Bucket and object ACLs
    sts-temporary-credentials.mdx              # STS temporary access tokens
    presigned-urls.mdx                         # Pre-signed URLs for temporary access
    access-points.mdx                          # OSS Access Points
    object-fc-access-points.mdx                # Access Points for Object Process (FC)
    block-public-access.mdx                    # Block public access settings
    cors.mdx                                   # Cross-origin resource sharing (CORS)
  security/
    server-side-encryption.mdx                 # SSE-OSS, SSE-KMS, SSE-SM4
    client-side-encryption.mdx                 # Client-side encryption
    https-tls.mdx                              # Enforce HTTPS / TLS configuration
    hotlink-protection.mdx                     # Referer-based hotlink protection
    ddos-protection.mdx                        # Anti-DDoS protection
    worm-retention.mdx                         # WORM retention policies (compliance)
    data-verification.mdx                      # CRC-64 / Content-MD5 integrity checks
    compliance.mdx                             # Compliance certifications
    sandbox.mdx                                # OSS sandbox restrictions
  data-management/
    lifecycle-rules.mdx                        # Lifecycle rules for automatic transitions/deletion
    versioning.mdx                             # Object versioning
    cross-region-replication.mdx               # Cross-region replication (CRR)
    same-region-replication.mdx                # Same-region replication
    bucket-inventory.mdx                       # Bucket inventory reports
    data-redundancy.mdx                        # Redundancy types (LRS, ZRS)
    archive-direct-read.mdx                    # Archive direct reading
    storage-class-conversion.mdx               # Convert storage classes
    scheduled-backup.mdx                       # Scheduled backup configuration
    batch-operations.mdx                       # Batch / bulk operations
  networking/
    custom-domain-names.mdx                    # Map custom domain names (CNAME)
    cdn-acceleration.mdx                       # CDN acceleration
    transfer-acceleration.mdx                  # Transfer acceleration (global edge nodes)
    privatelink.mdx                            # Access OSS via PrivateLink
    ecs-reverse-proxy.mdx                      # Access via ECS reverse proxy
    bucket-domain-access.mdx                   # Access via bucket domain name
    global-acceleration.mdx                    # Global accelerated access
  logging-monitoring/
    access-logging.mdx                         # Enable and manage access logs
    real-time-log-query.mdx                    # Real-time log query
    custom-log-fields.mdx                      # User-defined log fields
    monitoring-alerts.mdx                      # CloudMonitor metrics and alerting
    access-monitor.mdx                         # Access monitor (data access patterns)
  data-processing/
    image-processing.mdx                       # IMG: resize, crop, watermark, format
    image-style.mdx                            # IMG style presets
    video-processing.mdx                       # Video snapshots and processing
    content-detection.mdx                      # Content moderation / detection
    ai-content-awareness.mdx                   # AI content awareness features
    data-indexing.mdx                          # Data indexing (MetaQuery)
  advanced/
    static-website-hosting.mdx                 # Host a static website on OSS
    event-notifications.mdx                    # Event notifications (MNS, Function Compute)
    function-compute-triggers.mdx              # Function Compute integration
    back-to-origin.mdx                         # Mirroring-based back-to-origin
    data-lake-integration.mdx                  # Connect OSS to data lake ecosystems
    hierarchical-namespace.mdx                 # Enable hierarchical namespace
    authentication.mdx                         # Signature V1 / V4, authentication details
    s3-compatibility.mdx                       # Amazon S3 API compatibility
    direct-client-upload.mdx                   # Upload directly from clients (browser/mobile)
    efc-cache.mdx                              # EFC cache acceleration
    qos-throttling.mdx                         # Resource pool QoS configuration
```

## Tab 3: API Reference

```
api-reference/
  overview.mdx                                 # API overview, endpoints, authentication
  common-headers.mdx                           # Common HTTP headers and parameters
  signature-v4.mdx                             # Signature Version 4 details
  error-codes.mdx                              # Error codes reference table
  service-operations/
    DescribeRegions.mdx                        # Describe available regions
    ListBuckets.mdx                            # List all buckets (GetService)
  bucket-basic/
    PutBucket.mdx                              # Create bucket
    GetBucketInfo.mdx                          # Get bucket information
    GetBucketLocation.mdx                      # Get bucket location
    GetBucketStat.mdx                          # Get bucket statistics
    ListObjectsV2.mdx                          # List objects V2
    ListObjects.mdx                            # List objects V1
    DeleteBucket.mdx                           # Delete bucket
  bucket-acl-policy/
    PutBucketAcl.mdx                           # Set bucket ACL
    GetBucketAcl.mdx                           # Get bucket ACL
    PutBucketPolicy.mdx                        # Set bucket policy
    GetBucketPolicy.mdx                        # Get bucket policy
    GetBucketPolicyStatus.mdx                  # Get bucket policy status
    DeleteBucketPolicy.mdx                     # Delete bucket policy
    PutPublicAccessBlock.mdx                   # Set public access block
    GetPublicAccessBlock.mdx                   # Get public access block
    DeletePublicAccessBlock.mdx                # Delete public access block
    PutBucketPublicAccessBlock.mdx             # Set bucket public access block
    GetBucketPublicAccessBlock.mdx             # Get bucket public access block
    DeleteBucketPublicAccessBlock.mdx          # Delete bucket public access block
  access-points/
    CreateAccessPoint.mdx                      # Create access point
    GetAccessPoint.mdx                         # Get access point
    ListAccessPoints.mdx                       # List access points
    DeleteAccessPoint.mdx                      # Delete access point
    PutAccessPointPolicy.mdx                   # Set access point policy
    GetAccessPointPolicy.mdx                   # Get access point policy
    DeleteAccessPointPolicy.mdx                # Delete access point policy
    PutAccessPointPublicAccessBlock.mdx        # Set access point public access block
    GetAccessPointPublicAccessBlock.mdx        # Get access point public access block
    DeleteAccessPointPublicAccessBlock.mdx     # Delete access point public access block
    CreateAccessPointForObjectProcess.mdx      # Create access point for object process
    GetAccessPointForObjectProcess.mdx         # Get access point for object process
    ListAccessPointsForObjectProcess.mdx       # List access points for object process
    DeleteAccessPointForObjectProcess.mdx      # Delete access point for object process
    PutAccessPointConfigForObjectProcess.mdx   # Set object process config
    GetAccessPointConfigForObjectProcess.mdx   # Get object process config
    PutAccessPointPolicyForObjectProcess.mdx   # Set object process policy
    GetAccessPointPolicyForObjectProcess.mdx   # Get object process policy
    DeleteAccessPointPolicyForObjectProcess.mdx # Delete object process policy
    WriteGetObjectResponse.mdx                 # Write get object response (for FC)
  bucket-encryption/
    PutBucketEncryption.mdx                    # Set bucket encryption
    GetBucketEncryption.mdx                    # Get bucket encryption
    DeleteBucketEncryption.mdx                 # Delete bucket encryption
    PutBucketHttpsConfig.mdx                   # Set bucket HTTPS config
    GetBucketHttpsConfig.mdx                   # Get bucket HTTPS config
  bucket-tags/
    PutBucketTags.mdx                          # Set bucket tags
    GetBucketTags.mdx                          # Get bucket tags
    DeleteBucketTags.mdx                       # Delete bucket tags
  bucket-lifecycle/
    PutBucketLifecycle.mdx                     # Set lifecycle rules
    GetBucketLifecycle.mdx                     # Get lifecycle rules
    DeleteBucketLifecycle.mdx                  # Delete lifecycle rules
  bucket-versioning/
    PutBucketVersioning.mdx                    # Set versioning status
    GetBucketVersioning.mdx                    # Get versioning status
    ListObjectVersions.mdx                     # List object versions
  bucket-replication/
    PutBucketReplication.mdx                   # Set replication rules
    GetBucketReplication.mdx                   # Get replication rules
    GetBucketReplicationLocation.mdx           # Get replication location
    GetBucketReplicationProgress.mdx           # Get replication progress
    DeleteBucketReplication.mdx                # Delete replication rules
    PutBucketRTC.mdx                           # Set replication time control
  bucket-logging/
    PutBucketLogging.mdx                       # Set access logging
    GetBucketLogging.mdx                       # Get access logging
    DeleteBucketLogging.mdx                    # Delete access logging
    PutUserDefinedLogFieldsConfig.mdx          # Set custom log fields
    GetUserDefinedLogFieldsConfig.mdx          # Get custom log fields
    DeleteUserDefinedLogFieldsConfig.mdx       # Delete custom log fields
  bucket-website/
    PutBucketWebsite.mdx                       # Set website configuration
    GetBucketWebsite.mdx                       # Get website configuration
    DeleteBucketWebsite.mdx                    # Delete website configuration
  bucket-cors/
    PutBucketCors.mdx                          # Set CORS rules
    GetBucketCors.mdx                          # Get CORS rules
    DeleteBucketCors.mdx                       # Delete CORS rules
    OptionObject.mdx                           # Preflight (OPTIONS) request
  bucket-referer/
    PutBucketReferer.mdx                       # Set hotlink protection
    GetBucketReferer.mdx                       # Get hotlink protection
  bucket-inventory/
    PutBucketInventory.mdx                     # Set inventory configuration
    GetBucketInventory.mdx                     # Get inventory configuration
    ListBucketInventory.mdx                    # List inventory configurations
    DeleteBucketInventory.mdx                  # Delete inventory configuration
  bucket-worm/
    InitiateBucketWorm.mdx                     # Initiate WORM policy
    AbortBucketWorm.mdx                        # Abort WORM policy
    CompleteBucketWorm.mdx                     # Complete (lock) WORM policy
    ExtendBucketWorm.mdx                       # Extend WORM retention
    GetBucketWorm.mdx                          # Get WORM policy
  bucket-transfer/
    PutBucketTransferAcceleration.mdx          # Set transfer acceleration
    GetBucketTransferAcceleration.mdx          # Get transfer acceleration
  bucket-payment/
    PutBucketRequestPayment.mdx                # Set requester-pays
    GetBucketRequestPayment.mdx                # Get requester-pays
  bucket-resource-group/
    PutBucketResourceGroup.mdx                 # Set resource group
    GetBucketResourceGroup.mdx                 # Get resource group
  bucket-cname/
    PutCname.mdx                               # Add custom domain name
    GetCnameToken.mdx                          # Get CNAME token
    CreateCnameToken.mdx                       # Create CNAME token
    ListCname.mdx                              # List CNAME records
    DeleteCname.mdx                            # Delete CNAME record
  bucket-access-monitor/
    PutBucketAccessMonitor.mdx                 # Set access monitor
    GetBucketAccessMonitor.mdx                 # Get access monitor
  bucket-data-redundancy/
    CreateBucketDataRedundancyTransition.mdx   # Create redundancy transition
    GetBucketDataRedundancyTransition.mdx      # Get redundancy transition
    ListBucketDataRedundancyTransition.mdx     # List redundancy transitions
    DeleteBucketDataRedundancyTransition.mdx   # Delete redundancy transition
    ListUserDataRedundancyTransition.mdx       # List user redundancy transitions
  bucket-data-accelerator/
    PutBucketDataAccelerator.mdx               # Set data accelerator
    GetBucketDataAccelerator.mdx               # Get data accelerator
    DeleteBucketDataAccelerator.mdx            # Delete data accelerator
  bucket-archive-direct-read/
    PutBucketArchiveDirectRead.mdx             # Set archive direct read
    GetBucketArchiveDirectRead.mdx             # Get archive direct read
  bucket-anti-ddos/
    InitBucketAntiDDosInfo.mdx                 # Init bucket anti-DDoS
    InitUserAntiDDosInfo.mdx                   # Init user anti-DDoS
    UpdateBucketAntiDDosInfo.mdx               # Update bucket anti-DDoS
    UpdateUserAntiDDosInfo.mdx                 # Update user anti-DDoS
    ListBucketAntiDDosInfo.mdx                 # List bucket anti-DDoS
    GetUserAntiDDosInfo.mdx                    # Get user anti-DDoS
  bucket-resource-pool/
    GetResourcePoolInfo.mdx                    # Get resource pool info
    ListResourcePools.mdx                      # List resource pools
    PutBucketResourcePoolBucketGroup.mdx       # Set bucket group
    ListResourcePoolBuckets.mdx                # List resource pool buckets
    ListResourcePoolBucketGroups.mdx           # List bucket groups
    PutResourcePoolRequesterQosInfo.mdx        # Set requester QoS
    GetResourcePoolRequesterQosInfo.mdx        # Get requester QoS
    ListResourcePoolRequesterQosInfos.mdx      # List requester QoS
    DeleteResourcePoolRequesterQosInfo.mdx     # Delete requester QoS
    PutResourcePoolBucketGroupQosInfo.mdx      # Set bucket group QoS
    GetResourcePoolBucketGroupQosInfo.mdx      # Get bucket group QoS
    ListResourcePoolBucketGroupQosInfos.mdx    # List bucket group QoS
    DeleteResourcePoolBucketGroupQosInfo.mdx   # Delete bucket group QoS
  bucket-meta-query/
    OpenMetaQuery.mdx                          # Enable data indexing
    DoMetaQuery.mdx                            # Execute data query
    GetMetaQueryStatus.mdx                     # Get indexing status
    CloseMetaQuery.mdx                         # Disable data indexing
  object-basic/
    PutObject.mdx                              # Upload object (PUT)
    PostObject.mdx                             # Upload object (POST form)
    GetObject.mdx                              # Download object (GET)
    HeadObject.mdx                             # Get object metadata (HEAD)
    GetObjectMeta.mdx                          # Get basic object metadata
    CopyObject.mdx                             # Copy object
    AppendObject.mdx                           # Append upload
    SealAppendObject.mdx                       # Seal append object
    DeleteObject.mdx                           # Delete object
    DeleteMultipleObjects.mdx                  # Delete multiple objects
    RestoreObject.mdx                          # Restore archived object
    CleanRestoredObject.mdx                    # Clean restored object
    SelectObject.mdx                           # Query object content (Select)
    CreateSelectObjectMeta.mdx                 # Create select object metadata
    Rename.mdx                                 # Rename object
    Callback.mdx                               # Upload callback
  object-acl-tagging/
    PutObjectAcl.mdx                           # Set object ACL
    GetObjectAcl.mdx                           # Get object ACL
    PutObjectTagging.mdx                       # Set object tags
    GetObjectTagging.mdx                       # Get object tags
    DeleteObjectTagging.mdx                    # Delete object tags
  object-symlink/
    PutSymlink.mdx                             # Create symbolic link
    GetSymlink.mdx                             # Get symbolic link
  object-directory/
    CreateDirectory.mdx                        # Create directory
    DeleteDirectory.mdx                        # Delete directory
  multipart-upload/
    InitiateMultipartUpload.mdx                # Initiate multipart upload
    UploadPart.mdx                             # Upload part
    UploadPartCopy.mdx                         # Upload part (copy)
    CompleteMultipartUpload.mdx                # Complete multipart upload
    AbortMultipartUpload.mdx                   # Abort multipart upload
    ListMultipartUploads.mdx                   # List multipart uploads
    ListParts.mdx                              # List uploaded parts
  img-style/
    PutStyle.mdx                               # Create image style
    GetStyle.mdx                               # Get image style
    ListStyle.mdx                              # List image styles
    DeleteStyle.mdx                            # Delete image style
  live-channel/
    PutLiveChannel.mdx                         # Create live channel
    PutLiveChannelStatus.mdx                   # Set live channel status
    GetLiveChannelInfo.mdx                     # Get live channel info
    GetLiveChannelStat.mdx                     # Get live channel stats
    GetLiveChannelHistory.mdx                  # Get live channel history
    ListLiveChannel.mdx                        # List live channels
    PostVodPlaylist.mdx                        # Post VOD playlist
    GetVodPlaylist.mdx                         # Get VOD playlist
    DeleteLiveChannel.mdx                      # Delete live channel
```

## Tab 4: SDKs

```
sdks/
  overview.mdx                                 # SDK overview, supported languages, feature matrix
  java/
    installation.mdx                           # Install and configure Java SDK
    initialization.mdx                         # Initialize OSSClient
    quick-start.mdx                            # Quickstart: first upload/download
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Simple, append, form upload
    multipart-upload.mdx                       # Multipart and resumable upload
    download-objects.mdx                       # Download operations
    copy-objects.mdx                           # Copy and move objects
    manage-objects.mdx                         # List, delete, metadata, tags
    presigned-urls.mdx                         # Generate presigned URLs
    access-control.mdx                         # ACL, bucket policy, STS
    lifecycle.mdx                              # Lifecycle rule management
    versioning.mdx                             # Versioning operations
    encryption.mdx                             # Server-side and client-side encryption
    image-processing.mdx                       # Image processing via SDK
    error-handling.mdx                         # Error handling and retry
  python/
    installation.mdx                           # Install oss2 package
    initialization.mdx                         # Configure Auth and Bucket
    quick-start.mdx                            # Quickstart: first upload/download
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Simple, append, resumable upload
    multipart-upload.mdx                       # Multipart upload
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, metadata, tags
    presigned-urls.mdx                         # Generate presigned URLs
    access-control.mdx                         # ACL, bucket policy, STS
    advanced-features.mdx                      # Lifecycle, versioning, encryption, IMG
  go/
    installation.mdx                           # Install Go SDK
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart: first upload/download
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Upload operations
    multipart-upload.mdx                       # Multipart upload
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, metadata, tags
    advanced-features.mdx                      # Lifecycle, versioning, encryption
  nodejs/
    installation.mdx                           # Install ali-oss package
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart: first upload/download
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Simple, append, resumable upload
    multipart-upload.mdx                       # Multipart upload
    upload-callbacks.mdx                       # Upload callbacks
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy, metadata
    presigned-urls.mdx                         # Generate presigned URLs
    access-control.mdx                         # ACL, bucket policy
    lifecycle.mdx                              # Lifecycle rule management
    versioning.mdx                             # Versioning operations
    cors.mdx                                   # CORS configuration
    static-website.mdx                         # Static website hosting via SDK
    image-processing.mdx                       # Image processing
    custom-domain.mdx                          # Custom domain management
  php/
    installation.mdx                           # Install PHP SDK v2
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Upload operations
    multipart-upload.mdx                       # Multipart upload
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy, metadata
    presigned-urls.mdx                         # Presigned URLs
    access-control.mdx                         # Access control
    advanced-features.mdx                      # Lifecycle, versioning, encryption, CORS
  dotnet/
    installation.mdx                           # Install .NET SDK
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Upload operations
    multipart-upload.mdx                       # Multipart upload
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy, metadata
    presigned-urls.mdx                         # Presigned URLs
    access-control.mdx                         # Access control
    advanced-features.mdx                      # Lifecycle, versioning, encryption
  cpp/
    installation.mdx                           # Install C++ SDK
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Upload operations
    multipart-upload.mdx                       # Multipart upload
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy, metadata
    access-control.mdx                         # Access control
    advanced-features.mdx                      # Lifecycle, versioning, encryption
  browser-js/
    installation.mdx                           # Install Browser.js SDK
    initialization.mdx                         # Initialize client (STS-based)
    quick-start.mdx                            # Quickstart
    upload-objects.mdx                         # Upload from browser
    download-objects.mdx                       # Download / preview in browser
    manage-objects.mdx                         # List, delete, copy
    access-control.mdx                         # STS, signed URLs, CORS
  android/
    installation.mdx                           # Install Android SDK
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart
    upload-objects.mdx                         # Upload from Android
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy
    access-control.mdx                         # STS credentials
  ios/
    installation.mdx                           # Install iOS SDK
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart
    upload-objects.mdx                         # Upload from iOS
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy
    access-control.mdx                         # STS credentials
  ruby/
    installation.mdx                           # Install Ruby SDK
    initialization.mdx                         # Initialize client
    quick-start.mdx                            # Quickstart
    bucket-operations.mdx                      # Bucket CRUD operations
    upload-objects.mdx                         # Upload operations
    download-objects.mdx                       # Download operations
    manage-objects.mdx                         # List, delete, copy, metadata
```

## Tab 5: Tools & Resources

```
tools/
  ossutil/
    overview.mdx                               # ossutil 2.0 overview and installation
    commands.mdx                               # Command reference (cp, ls, rm, stat, etc.)
    ossutil-v1.mdx                             # ossutil 1.0 legacy reference
  ossbrowser/
    overview.mdx                               # ossbrowser GUI tool
  terraform/
    overview.mdx                               # Terraform provider for OSS
    manage-oss.mdx                             # Manage OSS resources with Terraform
  oss-hdfs/
    overview.mdx                               # OSS-HDFS overview
    setup.mdx                                  # Enable and configure OSS-HDFS
    limitations.mdx                            # Usage notes and limitations
    migration.mdx                              # Migrate HDFS data to OSS-HDFS
  vectors/
    overview.mdx                               # Vector bucket overview
    quickstart.mdx                             # Vector bucket quickstart
    vector-index.mdx                           # Vector index management
    embeddings-cli.mdx                         # Embeddings via CLI
  mcp-server/
    overview.mdx                               # OSS MCP Server (AI integration)
resources/
  best-practices/
    performance.mdx                            # Performance optimization
    security.mdx                               # Security hardening
    cost-optimization.mdx                      # Cost optimization
    migration-from-s3.mdx                      # Migrate from AWS S3
    migration-overview.mdx                     # Migration overview and tools
    migration-tools.mdx                        # Migration tools comparison
    hadoop-optimization.mdx                    # Hadoop + OSS optimization
    direct-client-upload-practices.mdx         # Direct upload from clients best practices
  troubleshooting/
    error-codes.mdx                            # Complete error code reference
    common-issues.mdx                          # Common issues and solutions
    sdk-troubleshooting.mdx                    # SDK-specific troubleshooting
  faq/
    general.mdx                                # General FAQ
    billing.mdx                                # Billing and pricing FAQ
    security-faq.mdx                           # Security FAQ
    sdk-faq.mdx                                # SDK FAQ
  pricing/
    overview.mdx                               # Billing overview
    storage-fees.mdx                           # Storage pricing
    traffic-fees.mdx                           # Traffic pricing
    api-fees.mdx                               # API call pricing
    pay-as-you-go.mdx                          # Pay-as-you-go model
    resource-plans.mdx                         # Subscription resource plans
    query-bills.mdx                            # Query and manage bills
  release-notes.mdx                            # Release notes and changelog
  s3-compatibility.mdx                         # S3 compatibility reference
  sdk-compliance-guide.mdx                     # SDK compliance guide
  glossary.mdx                                 # Terms and definitions
```
