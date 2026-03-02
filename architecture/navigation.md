# Alibaba Cloud OSS Documentation - Navigation Structure

## Overview

This document defines the Mintlify-compatible navigation structure organized into 5 tabs. Each tab contains groups with pages listed in recommended display order.

---

## Tab 1: Get Started

The entry point for new users. Covers product overview, quickstarts, and foundational concepts.

```
Tab: "Get Started"
├── Group: "Introduction" (icon: book-open)
│   ├── get-started/index                         # Welcome / Landing Page
│   └── get-started/what-is-oss                    # What is OSS?
│
├── Group: "Quickstart" (icon: rocket)
│   ├── get-started/quickstart/console             # Quickstart: Console
│   ├── get-started/quickstart/cli                 # Quickstart: ossutil CLI
│   └── get-started/quickstart/sdk                 # Quickstart: SDK
│
└── Group: "Core Concepts" (icon: lightbulb)
    ├── get-started/concepts/buckets               # Buckets
    ├── get-started/concepts/objects                # Objects
    ├── get-started/concepts/regions-and-endpoints  # Regions & Endpoints
    ├── get-started/concepts/storage-classes        # Storage Classes
    ├── get-started/concepts/access-control-overview # Access Control Overview
    ├── get-started/concepts/naming-conventions     # Naming Conventions
    ├── get-started/concepts/limits                 # Limits & Quotas
    └── get-started/concepts/consistency-model      # Consistency Model
```

## Tab 2: Guides

Task-oriented developer guides organized by what users want to accomplish.

```
Tab: "Guides"
├── Group: "Bucket Operations" (icon: folder)
│   ├── guides/buckets/create-bucket               # Create a Bucket
│   ├── guides/buckets/list-buckets                # List Buckets
│   ├── guides/buckets/query-bucket-info           # Query Bucket Info
│   ├── guides/buckets/delete-bucket               # Delete a Bucket
│   ├── guides/buckets/bucket-tagging              # Bucket Tagging
│   ├── guides/buckets/resource-groups             # Resource Groups
│   ├── guides/buckets/pay-by-requester            # Pay-by-Requester
│   └── guides/buckets/storage-capacity            # View Storage Usage
│
├── Group: "Upload & Download" (icon: arrow-up-from-bracket)
│   ├── guides/objects/upload-objects               # Upload Objects
│   ├── guides/objects/multipart-upload             # Multipart Upload
│   ├── guides/objects/append-upload                # Append Upload
│   ├── guides/objects/form-upload                  # Form Upload (POST)
│   ├── guides/objects/resumable-upload             # Resumable Upload
│   ├── guides/objects/upload-callback              # Upload Callbacks
│   ├── guides/objects/download-objects             # Download Objects
│   ├── guides/objects/range-download               # Range Download
│   ├── guides/objects/resumable-download           # Resumable Download
│   ├── guides/objects/conditional-download         # Conditional Download
│   └── guides/objects/streaming-upload-download    # Streaming Upload & Download
│
├── Group: "Manage Objects" (icon: file)
│   ├── guides/objects/copy-objects                 # Copy Objects
│   ├── guides/objects/move-rename-objects          # Move / Rename Objects
│   ├── guides/objects/delete-objects               # Delete Objects
│   ├── guides/objects/restore-objects              # Restore Archived Objects
│   ├── guides/objects/manage-object-metadata       # Object Metadata
│   ├── guides/objects/object-tagging               # Object Tagging
│   ├── guides/objects/manage-directories           # Manage Directories
│   ├── guides/objects/manage-symbolic-links        # Symbolic Links
│   ├── guides/objects/prevent-overwrite            # Prevent Overwrite
│   ├── guides/objects/select-object                # Query Objects (Select)
│   ├── guides/objects/single-connection-throttling # Bandwidth Throttling
│   └── guides/objects/progress-bars                # Progress Bars
│
├── Group: "Access Control" (icon: shield-halved)
│   ├── guides/access-control/ram-policies          # RAM Policies
│   ├── guides/access-control/bucket-policies       # Bucket Policies
│   ├── guides/access-control/acls                  # ACLs
│   ├── guides/access-control/sts-temporary-credentials # STS Temporary Credentials
│   ├── guides/access-control/presigned-urls        # Presigned URLs
│   ├── guides/access-control/access-points         # Access Points
│   ├── guides/access-control/object-fc-access-points # Object Process Access Points
│   ├── guides/access-control/block-public-access   # Block Public Access
│   └── guides/access-control/cors                  # CORS
│
├── Group: "Security" (icon: lock)
│   ├── guides/security/server-side-encryption      # Server-Side Encryption
│   ├── guides/security/client-side-encryption      # Client-Side Encryption
│   ├── guides/security/https-tls                   # HTTPS / TLS
│   ├── guides/security/hotlink-protection          # Hotlink Protection
│   ├── guides/security/ddos-protection             # DDoS Protection
│   ├── guides/security/worm-retention              # WORM Retention Policies
│   ├── guides/security/data-verification           # Data Verification
│   ├── guides/security/compliance                  # Compliance
│   └── guides/security/sandbox                     # OSS Sandbox
│
├── Group: "Data Management" (icon: database)
│   ├── guides/data-management/lifecycle-rules      # Lifecycle Rules
│   ├── guides/data-management/versioning           # Versioning
│   ├── guides/data-management/cross-region-replication # Cross-Region Replication
│   ├── guides/data-management/same-region-replication # Same-Region Replication
│   ├── guides/data-management/bucket-inventory     # Bucket Inventory
│   ├── guides/data-management/data-redundancy      # Data Redundancy (LRS/ZRS)
│   ├── guides/data-management/archive-direct-read  # Archive Direct Reading
│   ├── guides/data-management/storage-class-conversion # Storage Class Conversion
│   ├── guides/data-management/scheduled-backup     # Scheduled Backup
│   └── guides/data-management/batch-operations     # Batch Operations
│
├── Group: "Networking & Acceleration" (icon: globe)
│   ├── guides/networking/custom-domain-names       # Custom Domain Names
│   ├── guides/networking/cdn-acceleration          # CDN Acceleration
│   ├── guides/networking/transfer-acceleration     # Transfer Acceleration
│   ├── guides/networking/privatelink               # PrivateLink
│   ├── guides/networking/ecs-reverse-proxy         # ECS Reverse Proxy
│   ├── guides/networking/bucket-domain-access      # Bucket Domain Access
│   └── guides/networking/global-acceleration       # Global Acceleration
│
├── Group: "Logging & Monitoring" (icon: chart-line)
│   ├── guides/logging-monitoring/access-logging    # Access Logging
│   ├── guides/logging-monitoring/real-time-log-query # Real-Time Log Query
│   ├── guides/logging-monitoring/custom-log-fields # Custom Log Fields
│   ├── guides/logging-monitoring/monitoring-alerts # Monitoring & Alerts
│   └── guides/logging-monitoring/access-monitor    # Access Monitor
│
├── Group: "Data Processing" (icon: image)
│   ├── guides/data-processing/image-processing     # Image Processing
│   ├── guides/data-processing/image-style          # Image Styles
│   ├── guides/data-processing/video-processing     # Video Processing
│   ├── guides/data-processing/content-detection    # Content Detection
│   ├── guides/data-processing/ai-content-awareness # AI Content Awareness
│   └── guides/data-processing/data-indexing        # Data Indexing (MetaQuery)
│
└── Group: "Advanced Topics" (icon: gear)
    ├── guides/advanced/static-website-hosting      # Static Website Hosting
    ├── guides/advanced/event-notifications         # Event Notifications
    ├── guides/advanced/function-compute-triggers   # Function Compute Triggers
    ├── guides/advanced/back-to-origin              # Back-to-Origin
    ├── guides/advanced/data-lake-integration       # Data Lake Integration
    ├── guides/advanced/hierarchical-namespace       # Hierarchical Namespace
    ├── guides/advanced/authentication              # Authentication Details
    ├── guides/advanced/s3-compatibility            # S3 Compatibility
    ├── guides/advanced/direct-client-upload         # Direct Client Upload
    ├── guides/advanced/efc-cache                   # EFC Cache
    └── guides/advanced/qos-throttling              # QoS Throttling
```

## Tab 3: API Reference

REST API documentation organized by resource type.

```
Tab: "API Reference"
├── Group: "Overview" (icon: code)
│   ├── api-reference/overview                     # API Overview
│   ├── api-reference/common-headers               # Common HTTP Headers
│   ├── api-reference/signature-v4                 # Signature Version 4
│   └── api-reference/error-codes                  # Error Codes
│
├── Group: "Service Operations" (icon: server)
│   ├── api-reference/service-operations/DescribeRegions
│   └── api-reference/service-operations/ListBuckets
│
├── Group: "Bucket - Basic" (icon: folder)
│   ├── api-reference/bucket-basic/PutBucket
│   ├── api-reference/bucket-basic/GetBucketInfo
│   ├── api-reference/bucket-basic/GetBucketLocation
│   ├── api-reference/bucket-basic/GetBucketStat
│   ├── api-reference/bucket-basic/ListObjectsV2
│   ├── api-reference/bucket-basic/ListObjects
│   └── api-reference/bucket-basic/DeleteBucket
│
├── Group: "Bucket - ACL & Policy" (icon: shield)
│   ├── api-reference/bucket-acl-policy/PutBucketAcl
│   ├── api-reference/bucket-acl-policy/GetBucketAcl
│   ├── api-reference/bucket-acl-policy/PutBucketPolicy
│   ├── api-reference/bucket-acl-policy/GetBucketPolicy
│   ├── api-reference/bucket-acl-policy/GetBucketPolicyStatus
│   ├── api-reference/bucket-acl-policy/DeleteBucketPolicy
│   ├── api-reference/bucket-acl-policy/PutPublicAccessBlock
│   ├── api-reference/bucket-acl-policy/GetPublicAccessBlock
│   ├── api-reference/bucket-acl-policy/DeletePublicAccessBlock
│   ├── api-reference/bucket-acl-policy/PutBucketPublicAccessBlock
│   ├── api-reference/bucket-acl-policy/GetBucketPublicAccessBlock
│   └── api-reference/bucket-acl-policy/DeleteBucketPublicAccessBlock
│
├── Group: "Bucket - Access Points" (icon: circle-nodes)
│   ├── api-reference/access-points/CreateAccessPoint
│   ├── api-reference/access-points/GetAccessPoint
│   ├── api-reference/access-points/ListAccessPoints
│   ├── api-reference/access-points/DeleteAccessPoint
│   ├── api-reference/access-points/PutAccessPointPolicy
│   ├── api-reference/access-points/GetAccessPointPolicy
│   ├── api-reference/access-points/DeleteAccessPointPolicy
│   ├── api-reference/access-points/PutAccessPointPublicAccessBlock
│   ├── api-reference/access-points/GetAccessPointPublicAccessBlock
│   ├── api-reference/access-points/DeleteAccessPointPublicAccessBlock
│   ├── api-reference/access-points/CreateAccessPointForObjectProcess
│   ├── api-reference/access-points/GetAccessPointForObjectProcess
│   ├── api-reference/access-points/ListAccessPointsForObjectProcess
│   ├── api-reference/access-points/DeleteAccessPointForObjectProcess
│   ├── api-reference/access-points/PutAccessPointConfigForObjectProcess
│   ├── api-reference/access-points/GetAccessPointConfigForObjectProcess
│   ├── api-reference/access-points/PutAccessPointPolicyForObjectProcess
│   ├── api-reference/access-points/GetAccessPointPolicyForObjectProcess
│   ├── api-reference/access-points/DeleteAccessPointPolicyForObjectProcess
│   └── api-reference/access-points/WriteGetObjectResponse
│
├── Group: "Bucket - Configuration" (icon: sliders)
│   ├── api-reference/bucket-encryption/PutBucketEncryption
│   ├── api-reference/bucket-encryption/GetBucketEncryption
│   ├── api-reference/bucket-encryption/DeleteBucketEncryption
│   ├── api-reference/bucket-encryption/PutBucketHttpsConfig
│   ├── api-reference/bucket-encryption/GetBucketHttpsConfig
│   ├── api-reference/bucket-tags/PutBucketTags
│   ├── api-reference/bucket-tags/GetBucketTags
│   ├── api-reference/bucket-tags/DeleteBucketTags
│   ├── api-reference/bucket-transfer/PutBucketTransferAcceleration
│   ├── api-reference/bucket-transfer/GetBucketTransferAcceleration
│   ├── api-reference/bucket-payment/PutBucketRequestPayment
│   ├── api-reference/bucket-payment/GetBucketRequestPayment
│   ├── api-reference/bucket-resource-group/PutBucketResourceGroup
│   └── api-reference/bucket-resource-group/GetBucketResourceGroup
│
├── Group: "Bucket - Lifecycle & Versioning" (icon: clock-rotate-left)
│   ├── api-reference/bucket-lifecycle/PutBucketLifecycle
│   ├── api-reference/bucket-lifecycle/GetBucketLifecycle
│   ├── api-reference/bucket-lifecycle/DeleteBucketLifecycle
│   ├── api-reference/bucket-versioning/PutBucketVersioning
│   ├── api-reference/bucket-versioning/GetBucketVersioning
│   └── api-reference/bucket-versioning/ListObjectVersions
│
├── Group: "Bucket - Replication" (icon: rotate)
│   ├── api-reference/bucket-replication/PutBucketReplication
│   ├── api-reference/bucket-replication/GetBucketReplication
│   ├── api-reference/bucket-replication/GetBucketReplicationLocation
│   ├── api-reference/bucket-replication/GetBucketReplicationProgress
│   ├── api-reference/bucket-replication/DeleteBucketReplication
│   └── api-reference/bucket-replication/PutBucketRTC
│
├── Group: "Bucket - Logging" (icon: file-lines)
│   ├── api-reference/bucket-logging/PutBucketLogging
│   ├── api-reference/bucket-logging/GetBucketLogging
│   ├── api-reference/bucket-logging/DeleteBucketLogging
│   ├── api-reference/bucket-logging/PutUserDefinedLogFieldsConfig
│   ├── api-reference/bucket-logging/GetUserDefinedLogFieldsConfig
│   └── api-reference/bucket-logging/DeleteUserDefinedLogFieldsConfig
│
├── Group: "Bucket - Website & CORS" (icon: browser)
│   ├── api-reference/bucket-website/PutBucketWebsite
│   ├── api-reference/bucket-website/GetBucketWebsite
│   ├── api-reference/bucket-website/DeleteBucketWebsite
│   ├── api-reference/bucket-cors/PutBucketCors
│   ├── api-reference/bucket-cors/GetBucketCors
│   ├── api-reference/bucket-cors/DeleteBucketCors
│   ├── api-reference/bucket-cors/OptionObject
│   ├── api-reference/bucket-referer/PutBucketReferer
│   └── api-reference/bucket-referer/GetBucketReferer
│
├── Group: "Bucket - Inventory" (icon: clipboard-list)
│   ├── api-reference/bucket-inventory/PutBucketInventory
│   ├── api-reference/bucket-inventory/GetBucketInventory
│   ├── api-reference/bucket-inventory/ListBucketInventory
│   └── api-reference/bucket-inventory/DeleteBucketInventory
│
├── Group: "Bucket - WORM" (icon: vault)
│   ├── api-reference/bucket-worm/InitiateBucketWorm
│   ├── api-reference/bucket-worm/AbortBucketWorm
│   ├── api-reference/bucket-worm/CompleteBucketWorm
│   ├── api-reference/bucket-worm/ExtendBucketWorm
│   └── api-reference/bucket-worm/GetBucketWorm
│
├── Group: "Bucket - CNAME" (icon: link)
│   ├── api-reference/bucket-cname/PutCname
│   ├── api-reference/bucket-cname/GetCnameToken
│   ├── api-reference/bucket-cname/CreateCnameToken
│   ├── api-reference/bucket-cname/ListCname
│   └── api-reference/bucket-cname/DeleteCname
│
├── Group: "Bucket - Advanced" (icon: microchip)
│   ├── api-reference/bucket-access-monitor/PutBucketAccessMonitor
│   ├── api-reference/bucket-access-monitor/GetBucketAccessMonitor
│   ├── api-reference/bucket-archive-direct-read/PutBucketArchiveDirectRead
│   ├── api-reference/bucket-archive-direct-read/GetBucketArchiveDirectRead
│   ├── api-reference/bucket-meta-query/OpenMetaQuery
│   ├── api-reference/bucket-meta-query/DoMetaQuery
│   ├── api-reference/bucket-meta-query/GetMetaQueryStatus
│   └── api-reference/bucket-meta-query/CloseMetaQuery
│
├── Group: "Object - Basic" (icon: file)
│   ├── api-reference/object-basic/PutObject
│   ├── api-reference/object-basic/PostObject
│   ├── api-reference/object-basic/GetObject
│   ├── api-reference/object-basic/HeadObject
│   ├── api-reference/object-basic/GetObjectMeta
│   ├── api-reference/object-basic/CopyObject
│   ├── api-reference/object-basic/AppendObject
│   ├── api-reference/object-basic/SealAppendObject
│   ├── api-reference/object-basic/DeleteObject
│   ├── api-reference/object-basic/DeleteMultipleObjects
│   ├── api-reference/object-basic/RestoreObject
│   ├── api-reference/object-basic/CleanRestoredObject
│   ├── api-reference/object-basic/SelectObject
│   ├── api-reference/object-basic/CreateSelectObjectMeta
│   ├── api-reference/object-basic/Rename
│   └── api-reference/object-basic/Callback
│
├── Group: "Object - ACL & Tags" (icon: tag)
│   ├── api-reference/object-acl-tagging/PutObjectAcl
│   ├── api-reference/object-acl-tagging/GetObjectAcl
│   ├── api-reference/object-acl-tagging/PutObjectTagging
│   ├── api-reference/object-acl-tagging/GetObjectTagging
│   ├── api-reference/object-acl-tagging/DeleteObjectTagging
│   ├── api-reference/object-symlink/PutSymlink
│   ├── api-reference/object-symlink/GetSymlink
│   ├── api-reference/object-directory/CreateDirectory
│   └── api-reference/object-directory/DeleteDirectory
│
├── Group: "Multipart Upload" (icon: layer-group)
│   ├── api-reference/multipart-upload/InitiateMultipartUpload
│   ├── api-reference/multipart-upload/UploadPart
│   ├── api-reference/multipart-upload/UploadPartCopy
│   ├── api-reference/multipart-upload/CompleteMultipartUpload
│   ├── api-reference/multipart-upload/AbortMultipartUpload
│   ├── api-reference/multipart-upload/ListMultipartUploads
│   └── api-reference/multipart-upload/ListParts
│
├── Group: "Image Style" (icon: palette)
│   ├── api-reference/img-style/PutStyle
│   ├── api-reference/img-style/GetStyle
│   ├── api-reference/img-style/ListStyle
│   └── api-reference/img-style/DeleteStyle
│
└── Group: "Live Channel" (icon: video)
    ├── api-reference/live-channel/PutLiveChannel
    ├── api-reference/live-channel/PutLiveChannelStatus
    ├── api-reference/live-channel/GetLiveChannelInfo
    ├── api-reference/live-channel/GetLiveChannelStat
    ├── api-reference/live-channel/GetLiveChannelHistory
    ├── api-reference/live-channel/ListLiveChannel
    ├── api-reference/live-channel/PostVodPlaylist
    ├── api-reference/live-channel/GetVodPlaylist
    └── api-reference/live-channel/DeleteLiveChannel
```

## Tab 4: SDKs

SDK documentation organized by language with consistent structure per SDK.

```
Tab: "SDKs"
├── Group: "Overview" (icon: code)
│   └── sdks/overview                              # SDK Overview & Feature Matrix
│
├── Group: "Java" (icon: java)
│   ├── sdks/java/installation
│   ├── sdks/java/initialization
│   ├── sdks/java/quick-start
│   ├── sdks/java/bucket-operations
│   ├── sdks/java/upload-objects
│   ├── sdks/java/multipart-upload
│   ├── sdks/java/download-objects
│   ├── sdks/java/copy-objects
│   ├── sdks/java/manage-objects
│   ├── sdks/java/presigned-urls
│   ├── sdks/java/access-control
│   ├── sdks/java/lifecycle
│   ├── sdks/java/versioning
│   ├── sdks/java/encryption
│   ├── sdks/java/image-processing
│   └── sdks/java/error-handling
│
├── Group: "Python" (icon: python)
│   ├── sdks/python/installation
│   ├── sdks/python/initialization
│   ├── sdks/python/quick-start
│   ├── sdks/python/bucket-operations
│   ├── sdks/python/upload-objects
│   ├── sdks/python/multipart-upload
│   ├── sdks/python/download-objects
│   ├── sdks/python/manage-objects
│   ├── sdks/python/presigned-urls
│   ├── sdks/python/access-control
│   └── sdks/python/advanced-features
│
├── Group: "Go" (icon: golang)
│   ├── sdks/go/installation
│   ├── sdks/go/initialization
│   ├── sdks/go/quick-start
│   ├── sdks/go/bucket-operations
│   ├── sdks/go/upload-objects
│   ├── sdks/go/multipart-upload
│   ├── sdks/go/download-objects
│   ├── sdks/go/manage-objects
│   └── sdks/go/advanced-features
│
├── Group: "Node.js" (icon: node-js)
│   ├── sdks/nodejs/installation
│   ├── sdks/nodejs/initialization
│   ├── sdks/nodejs/quick-start
│   ├── sdks/nodejs/bucket-operations
│   ├── sdks/nodejs/upload-objects
│   ├── sdks/nodejs/multipart-upload
│   ├── sdks/nodejs/upload-callbacks
│   ├── sdks/nodejs/download-objects
│   ├── sdks/nodejs/manage-objects
│   ├── sdks/nodejs/presigned-urls
│   ├── sdks/nodejs/access-control
│   ├── sdks/nodejs/lifecycle
│   ├── sdks/nodejs/versioning
│   ├── sdks/nodejs/cors
│   ├── sdks/nodejs/static-website
│   ├── sdks/nodejs/image-processing
│   └── sdks/nodejs/custom-domain
│
├── Group: "PHP" (icon: php)
│   ├── sdks/php/installation
│   ├── sdks/php/initialization
│   ├── sdks/php/quick-start
│   ├── sdks/php/bucket-operations
│   ├── sdks/php/upload-objects
│   ├── sdks/php/multipart-upload
│   ├── sdks/php/download-objects
│   ├── sdks/php/manage-objects
│   ├── sdks/php/presigned-urls
│   ├── sdks/php/access-control
│   └── sdks/php/advanced-features
│
├── Group: ".NET" (icon: microsoft)
│   ├── sdks/dotnet/installation
│   ├── sdks/dotnet/initialization
│   ├── sdks/dotnet/quick-start
│   ├── sdks/dotnet/bucket-operations
│   ├── sdks/dotnet/upload-objects
│   ├── sdks/dotnet/multipart-upload
│   ├── sdks/dotnet/download-objects
│   ├── sdks/dotnet/manage-objects
│   ├── sdks/dotnet/presigned-urls
│   ├── sdks/dotnet/access-control
│   └── sdks/dotnet/advanced-features
│
├── Group: "C++" (icon: c)
│   ├── sdks/cpp/installation
│   ├── sdks/cpp/initialization
│   ├── sdks/cpp/quick-start
│   ├── sdks/cpp/bucket-operations
│   ├── sdks/cpp/upload-objects
│   ├── sdks/cpp/multipart-upload
│   ├── sdks/cpp/download-objects
│   ├── sdks/cpp/manage-objects
│   ├── sdks/cpp/access-control
│   └── sdks/cpp/advanced-features
│
├── Group: "Browser.js" (icon: window-maximize)
│   ├── sdks/browser-js/installation
│   ├── sdks/browser-js/initialization
│   ├── sdks/browser-js/quick-start
│   ├── sdks/browser-js/upload-objects
│   ├── sdks/browser-js/download-objects
│   ├── sdks/browser-js/manage-objects
│   └── sdks/browser-js/access-control
│
├── Group: "Android" (icon: android)
│   ├── sdks/android/installation
│   ├── sdks/android/initialization
│   ├── sdks/android/quick-start
│   ├── sdks/android/upload-objects
│   ├── sdks/android/download-objects
│   ├── sdks/android/manage-objects
│   └── sdks/android/access-control
│
├── Group: "iOS" (icon: apple)
│   ├── sdks/ios/installation
│   ├── sdks/ios/initialization
│   ├── sdks/ios/quick-start
│   ├── sdks/ios/upload-objects
│   ├── sdks/ios/download-objects
│   ├── sdks/ios/manage-objects
│   └── sdks/ios/access-control
│
└── Group: "Ruby" (icon: gem)
    ├── sdks/ruby/installation
    ├── sdks/ruby/initialization
    ├── sdks/ruby/quick-start
    ├── sdks/ruby/bucket-operations
    ├── sdks/ruby/upload-objects
    ├── sdks/ruby/download-objects
    └── sdks/ruby/manage-objects
```

## Tab 5: Tools & Resources

CLI tools, supplementary tools, best practices, troubleshooting, pricing, and reference content.

```
Tab: "Tools & Resources"
├── Group: "ossutil (CLI)" (icon: terminal)
│   ├── tools/ossutil/overview
│   ├── tools/ossutil/commands
│   └── tools/ossutil/ossutil-v1
│
├── Group: "ossbrowser (GUI)" (icon: window-maximize)
│   └── tools/ossbrowser/overview
│
├── Group: "Terraform" (icon: cloud)
│   ├── tools/terraform/overview
│   └── tools/terraform/manage-oss
│
├── Group: "OSS-HDFS" (icon: hard-drive)
│   ├── tools/oss-hdfs/overview
│   ├── tools/oss-hdfs/setup
│   ├── tools/oss-hdfs/limitations
│   └── tools/oss-hdfs/migration
│
├── Group: "Vector Search" (icon: magnifying-glass)
│   ├── tools/vectors/overview
│   ├── tools/vectors/quickstart
│   ├── tools/vectors/vector-index
│   └── tools/vectors/embeddings-cli
│
├── Group: "MCP Server" (icon: robot)
│   └── tools/mcp-server/overview
│
├── Group: "Best Practices" (icon: star)
│   ├── resources/best-practices/performance
│   ├── resources/best-practices/security
│   ├── resources/best-practices/cost-optimization
│   ├── resources/best-practices/migration-from-s3
│   ├── resources/best-practices/migration-overview
│   ├── resources/best-practices/migration-tools
│   ├── resources/best-practices/hadoop-optimization
│   └── resources/best-practices/direct-client-upload-practices
│
├── Group: "Troubleshooting" (icon: wrench)
│   ├── resources/troubleshooting/error-codes
│   ├── resources/troubleshooting/common-issues
│   └── resources/troubleshooting/sdk-troubleshooting
│
├── Group: "FAQ" (icon: circle-question)
│   ├── resources/faq/general
│   ├── resources/faq/billing
│   ├── resources/faq/security-faq
│   └── resources/faq/sdk-faq
│
├── Group: "Pricing" (icon: dollar-sign)
│   ├── resources/pricing/overview
│   ├── resources/pricing/storage-fees
│   ├── resources/pricing/traffic-fees
│   ├── resources/pricing/api-fees
│   ├── resources/pricing/pay-as-you-go
│   ├── resources/pricing/resource-plans
│   └── resources/pricing/query-bills
│
└── Group: "Reference" (icon: book)
    ├── resources/release-notes
    ├── resources/s3-compatibility
    ├── resources/sdk-compliance-guide
    └── resources/glossary
```
