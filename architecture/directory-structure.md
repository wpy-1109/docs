# Alibaba Cloud OSS Documentation - Directory Structure

## Overview

This document defines the file and folder organization for the Mintlify documentation project. All content files use the `.mdx` extension. The structure mirrors the navigation hierarchy for easy maintenance.

---

## Root Directory

```
oss-docs/
├── docs.json                          # Mintlify configuration (navigation, theme, etc.)
├── favicon.png                        # Site favicon
├── logo-light.svg                     # Logo for light mode
├── logo-dark.svg                      # Logo for dark mode
│
├── snippets/                          # Reusable content snippets
│   ├── prerequisites.mdx              # Common prerequisites block
│   ├── security-warning.mdx           # Credential security warning
│   ├── endpoints-table.mdx            # Region/endpoint reference table
│   ├── storage-classes-table.mdx      # Storage class comparison table
│   ├── support-link.mdx               # Support ticket link card
│   ├── sdk-init-python.mdx            # Python SDK initialization
│   ├── sdk-init-java.mdx              # Java SDK initialization
│   ├── sdk-init-go.mdx                # Go SDK initialization
│   ├── sdk-init-nodejs.mdx            # Node.js SDK initialization
│   ├── sdk-init-php.mdx               # PHP SDK initialization
│   ├── sdk-init-dotnet.mdx            # .NET SDK initialization
│   ├── sdk-init-cpp.mdx               # C++ SDK initialization
│   ├── sdk-init-browser.mdx           # Browser.js SDK initialization
│   ├── sdk-init-android.mdx           # Android SDK initialization
│   ├── sdk-init-ios.mdx               # iOS SDK initialization
│   └── sdk-init-ruby.mdx              # Ruby SDK initialization
│
├── images/                            # Static image assets
│   ├── architecture/                  # Architecture diagrams
│   ├── screenshots/                   # Console screenshots
│   └── og/                            # Open Graph images
│
├── get-started/                       # Tab 1: Get Started
├── guides/                            # Tab 2: Guides
├── api-reference/                     # Tab 3: API Reference
├── sdks/                              # Tab 4: SDKs
├── tools/                             # Tab 5: Tools (part of Tools & Resources)
└── resources/                         # Tab 5: Resources (part of Tools & Resources)
```

---

## get-started/ (Tab 1)

```
get-started/
├── index.mdx                          # Landing page (hero, Cards, quick nav)
├── what-is-oss.mdx                    # Product overview, features, use cases
│
├── quickstart/
│   ├── console.mdx                    # Quickstart via OSS Console
│   ├── cli.mdx                        # Quickstart via ossutil CLI
│   └── sdk.mdx                        # Quickstart via SDK (multi-language)
│
└── concepts/
    ├── buckets.mdx                    # Buckets concept
    ├── objects.mdx                    # Objects concept
    ├── regions-and-endpoints.mdx      # Regions and endpoints
    ├── storage-classes.mdx            # Storage classes explained
    ├── access-control-overview.mdx    # Access control overview
    ├── naming-conventions.mdx         # Bucket and object naming rules
    ├── limits.mdx                     # Service limits and quotas
    └── consistency-model.mdx          # Consistency guarantees
```

---

## guides/ (Tab 2)

```
guides/
├── buckets/
│   ├── create-bucket.mdx
│   ├── list-buckets.mdx
│   ├── query-bucket-info.mdx
│   ├── delete-bucket.mdx
│   ├── bucket-tagging.mdx
│   ├── resource-groups.mdx
│   ├── pay-by-requester.mdx
│   └── storage-capacity.mdx
│
├── objects/
│   ├── upload-objects.mdx             # Simple upload (multi-language)
│   ├── multipart-upload.mdx
│   ├── append-upload.mdx
│   ├── form-upload.mdx
│   ├── resumable-upload.mdx
│   ├── upload-callback.mdx
│   ├── download-objects.mdx
│   ├── range-download.mdx
│   ├── resumable-download.mdx
│   ├── conditional-download.mdx
│   ├── streaming-upload-download.mdx
│   ├── copy-objects.mdx
│   ├── move-rename-objects.mdx
│   ├── delete-objects.mdx
│   ├── restore-objects.mdx
│   ├── manage-object-metadata.mdx
│   ├── object-tagging.mdx
│   ├── manage-directories.mdx
│   ├── manage-symbolic-links.mdx
│   ├── prevent-overwrite.mdx
│   ├── select-object.mdx
│   ├── single-connection-throttling.mdx
│   └── progress-bars.mdx
│
├── access-control/
│   ├── ram-policies.mdx
│   ├── bucket-policies.mdx
│   ├── acls.mdx
│   ├── sts-temporary-credentials.mdx
│   ├── presigned-urls.mdx
│   ├── access-points.mdx
│   ├── object-fc-access-points.mdx
│   ├── block-public-access.mdx
│   └── cors.mdx
│
├── security/
│   ├── server-side-encryption.mdx
│   ├── client-side-encryption.mdx
│   ├── https-tls.mdx
│   ├── hotlink-protection.mdx
│   ├── ddos-protection.mdx
│   ├── worm-retention.mdx
│   ├── data-verification.mdx
│   ├── compliance.mdx
│   └── sandbox.mdx
│
├── data-management/
│   ├── lifecycle-rules.mdx
│   ├── versioning.mdx
│   ├── cross-region-replication.mdx
│   ├── same-region-replication.mdx
│   ├── bucket-inventory.mdx
│   ├── data-redundancy.mdx
│   ├── archive-direct-read.mdx
│   ├── storage-class-conversion.mdx
│   ├── scheduled-backup.mdx
│   └── batch-operations.mdx
│
├── networking/
│   ├── custom-domain-names.mdx
│   ├── cdn-acceleration.mdx
│   ├── transfer-acceleration.mdx
│   ├── privatelink.mdx
│   ├── ecs-reverse-proxy.mdx
│   ├── bucket-domain-access.mdx
│   └── global-acceleration.mdx
│
├── logging-monitoring/
│   ├── access-logging.mdx
│   ├── real-time-log-query.mdx
│   ├── custom-log-fields.mdx
│   ├── monitoring-alerts.mdx
│   └── access-monitor.mdx
│
├── data-processing/
│   ├── image-processing.mdx
│   ├── image-style.mdx
│   ├── video-processing.mdx
│   ├── content-detection.mdx
│   ├── ai-content-awareness.mdx
│   └── data-indexing.mdx
│
└── advanced/
    ├── static-website-hosting.mdx
    ├── event-notifications.mdx
    ├── function-compute-triggers.mdx
    ├── back-to-origin.mdx
    ├── data-lake-integration.mdx
    ├── hierarchical-namespace.mdx
    ├── authentication.mdx
    ├── s3-compatibility.mdx
    ├── direct-client-upload.mdx
    ├── efc-cache.mdx
    └── qos-throttling.mdx
```

---

## api-reference/ (Tab 3)

```
api-reference/
├── overview.mdx
├── common-headers.mdx
├── signature-v4.mdx
├── error-codes.mdx
│
├── service-operations/
│   ├── DescribeRegions.mdx
│   └── ListBuckets.mdx
│
├── bucket-basic/
│   ├── PutBucket.mdx
│   ├── GetBucketInfo.mdx
│   ├── GetBucketLocation.mdx
│   ├── GetBucketStat.mdx
│   ├── ListObjectsV2.mdx
│   ├── ListObjects.mdx
│   └── DeleteBucket.mdx
│
├── bucket-acl-policy/
│   ├── PutBucketAcl.mdx
│   ├── GetBucketAcl.mdx
│   ├── PutBucketPolicy.mdx
│   ├── GetBucketPolicy.mdx
│   ├── GetBucketPolicyStatus.mdx
│   ├── DeleteBucketPolicy.mdx
│   ├── PutPublicAccessBlock.mdx
│   ├── GetPublicAccessBlock.mdx
│   ├── DeletePublicAccessBlock.mdx
│   ├── PutBucketPublicAccessBlock.mdx
│   ├── GetBucketPublicAccessBlock.mdx
│   └── DeleteBucketPublicAccessBlock.mdx
│
├── access-points/
│   ├── CreateAccessPoint.mdx
│   ├── GetAccessPoint.mdx
│   ├── ListAccessPoints.mdx
│   ├── DeleteAccessPoint.mdx
│   ├── PutAccessPointPolicy.mdx
│   ├── GetAccessPointPolicy.mdx
│   ├── DeleteAccessPointPolicy.mdx
│   ├── PutAccessPointPublicAccessBlock.mdx
│   ├── GetAccessPointPublicAccessBlock.mdx
│   ├── DeleteAccessPointPublicAccessBlock.mdx
│   ├── CreateAccessPointForObjectProcess.mdx
│   ├── GetAccessPointForObjectProcess.mdx
│   ├── ListAccessPointsForObjectProcess.mdx
│   ├── DeleteAccessPointForObjectProcess.mdx
│   ├── PutAccessPointConfigForObjectProcess.mdx
│   ├── GetAccessPointConfigForObjectProcess.mdx
│   ├── PutAccessPointPolicyForObjectProcess.mdx
│   ├── GetAccessPointPolicyForObjectProcess.mdx
│   ├── DeleteAccessPointPolicyForObjectProcess.mdx
│   └── WriteGetObjectResponse.mdx
│
├── bucket-encryption/
│   ├── PutBucketEncryption.mdx
│   ├── GetBucketEncryption.mdx
│   ├── DeleteBucketEncryption.mdx
│   ├── PutBucketHttpsConfig.mdx
│   └── GetBucketHttpsConfig.mdx
│
├── bucket-tags/
│   ├── PutBucketTags.mdx
│   ├── GetBucketTags.mdx
│   └── DeleteBucketTags.mdx
│
├── bucket-lifecycle/
│   ├── PutBucketLifecycle.mdx
│   ├── GetBucketLifecycle.mdx
│   └── DeleteBucketLifecycle.mdx
│
├── bucket-versioning/
│   ├── PutBucketVersioning.mdx
│   ├── GetBucketVersioning.mdx
│   └── ListObjectVersions.mdx
│
├── bucket-replication/
│   ├── PutBucketReplication.mdx
│   ├── GetBucketReplication.mdx
│   ├── GetBucketReplicationLocation.mdx
│   ├── GetBucketReplicationProgress.mdx
│   ├── DeleteBucketReplication.mdx
│   └── PutBucketRTC.mdx
│
├── bucket-logging/
│   ├── PutBucketLogging.mdx
│   ├── GetBucketLogging.mdx
│   ├── DeleteBucketLogging.mdx
│   ├── PutUserDefinedLogFieldsConfig.mdx
│   ├── GetUserDefinedLogFieldsConfig.mdx
│   └── DeleteUserDefinedLogFieldsConfig.mdx
│
├── bucket-website/
│   ├── PutBucketWebsite.mdx
│   ├── GetBucketWebsite.mdx
│   └── DeleteBucketWebsite.mdx
│
├── bucket-cors/
│   ├── PutBucketCors.mdx
│   ├── GetBucketCors.mdx
│   ├── DeleteBucketCors.mdx
│   └── OptionObject.mdx
│
├── bucket-referer/
│   ├── PutBucketReferer.mdx
│   └── GetBucketReferer.mdx
│
├── bucket-inventory/
│   ├── PutBucketInventory.mdx
│   ├── GetBucketInventory.mdx
│   ├── ListBucketInventory.mdx
│   └── DeleteBucketInventory.mdx
│
├── bucket-worm/
│   ├── InitiateBucketWorm.mdx
│   ├── AbortBucketWorm.mdx
│   ├── CompleteBucketWorm.mdx
│   ├── ExtendBucketWorm.mdx
│   └── GetBucketWorm.mdx
│
├── bucket-transfer/
│   ├── PutBucketTransferAcceleration.mdx
│   └── GetBucketTransferAcceleration.mdx
│
├── bucket-payment/
│   ├── PutBucketRequestPayment.mdx
│   └── GetBucketRequestPayment.mdx
│
├── bucket-resource-group/
│   ├── PutBucketResourceGroup.mdx
│   └── GetBucketResourceGroup.mdx
│
├── bucket-cname/
│   ├── PutCname.mdx
│   ├── GetCnameToken.mdx
│   ├── CreateCnameToken.mdx
│   ├── ListCname.mdx
│   └── DeleteCname.mdx
│
├── bucket-access-monitor/
│   ├── PutBucketAccessMonitor.mdx
│   └── GetBucketAccessMonitor.mdx
│
├── bucket-data-redundancy/
│   ├── CreateBucketDataRedundancyTransition.mdx
│   ├── GetBucketDataRedundancyTransition.mdx
│   ├── ListBucketDataRedundancyTransition.mdx
│   ├── DeleteBucketDataRedundancyTransition.mdx
│   └── ListUserDataRedundancyTransition.mdx
│
├── bucket-data-accelerator/
│   ├── PutBucketDataAccelerator.mdx
│   ├── GetBucketDataAccelerator.mdx
│   └── DeleteBucketDataAccelerator.mdx
│
├── bucket-archive-direct-read/
│   ├── PutBucketArchiveDirectRead.mdx
│   └── GetBucketArchiveDirectRead.mdx
│
├── bucket-anti-ddos/
│   ├── InitBucketAntiDDosInfo.mdx
│   ├── InitUserAntiDDosInfo.mdx
│   ├── UpdateBucketAntiDDosInfo.mdx
│   ├── UpdateUserAntiDDosInfo.mdx
│   ├── ListBucketAntiDDosInfo.mdx
│   └── GetUserAntiDDosInfo.mdx
│
├── bucket-resource-pool/
│   ├── GetResourcePoolInfo.mdx
│   ├── ListResourcePools.mdx
│   ├── PutBucketResourcePoolBucketGroup.mdx
│   ├── ListResourcePoolBuckets.mdx
│   ├── ListResourcePoolBucketGroups.mdx
│   ├── PutResourcePoolRequesterQosInfo.mdx
│   ├── GetResourcePoolRequesterQosInfo.mdx
│   ├── ListResourcePoolRequesterQosInfos.mdx
│   ├── DeleteResourcePoolRequesterQosInfo.mdx
│   ├── PutResourcePoolBucketGroupQosInfo.mdx
│   ├── GetResourcePoolBucketGroupQosInfo.mdx
│   ├── ListResourcePoolBucketGroupQosInfos.mdx
│   └── DeleteResourcePoolBucketGroupQosInfo.mdx
│
├── bucket-meta-query/
│   ├── OpenMetaQuery.mdx
│   ├── DoMetaQuery.mdx
│   ├── GetMetaQueryStatus.mdx
│   └── CloseMetaQuery.mdx
│
├── object-basic/
│   ├── PutObject.mdx
│   ├── PostObject.mdx
│   ├── GetObject.mdx
│   ├── HeadObject.mdx
│   ├── GetObjectMeta.mdx
│   ├── CopyObject.mdx
│   ├── AppendObject.mdx
│   ├── SealAppendObject.mdx
│   ├── DeleteObject.mdx
│   ├── DeleteMultipleObjects.mdx
│   ├── RestoreObject.mdx
│   ├── CleanRestoredObject.mdx
│   ├── SelectObject.mdx
│   ├── CreateSelectObjectMeta.mdx
│   ├── Rename.mdx
│   └── Callback.mdx
│
├── object-acl-tagging/
│   ├── PutObjectAcl.mdx
│   ├── GetObjectAcl.mdx
│   ├── PutObjectTagging.mdx
│   ├── GetObjectTagging.mdx
│   └── DeleteObjectTagging.mdx
│
├── object-symlink/
│   ├── PutSymlink.mdx
│   └── GetSymlink.mdx
│
├── object-directory/
│   ├── CreateDirectory.mdx
│   └── DeleteDirectory.mdx
│
├── multipart-upload/
│   ├── InitiateMultipartUpload.mdx
│   ├── UploadPart.mdx
│   ├── UploadPartCopy.mdx
│   ├── CompleteMultipartUpload.mdx
│   ├── AbortMultipartUpload.mdx
│   ├── ListMultipartUploads.mdx
│   └── ListParts.mdx
│
├── img-style/
│   ├── PutStyle.mdx
│   ├── GetStyle.mdx
│   ├── ListStyle.mdx
│   └── DeleteStyle.mdx
│
└── live-channel/
    ├── PutLiveChannel.mdx
    ├── PutLiveChannelStatus.mdx
    ├── GetLiveChannelInfo.mdx
    ├── GetLiveChannelStat.mdx
    ├── GetLiveChannelHistory.mdx
    ├── ListLiveChannel.mdx
    ├── PostVodPlaylist.mdx
    ├── GetVodPlaylist.mdx
    └── DeleteLiveChannel.mdx
```

---

## sdks/ (Tab 4)

```
sdks/
├── overview.mdx                       # SDK overview, feature matrix, version table
│
├── java/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── download-objects.mdx
│   ├── copy-objects.mdx
│   ├── manage-objects.mdx
│   ├── presigned-urls.mdx
│   ├── access-control.mdx
│   ├── lifecycle.mdx
│   ├── versioning.mdx
│   ├── encryption.mdx
│   ├── image-processing.mdx
│   └── error-handling.mdx
│
├── python/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   ├── presigned-urls.mdx
│   ├── access-control.mdx
│   └── advanced-features.mdx
│
├── go/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   └── advanced-features.mdx
│
├── nodejs/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── upload-callbacks.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   ├── presigned-urls.mdx
│   ├── access-control.mdx
│   ├── lifecycle.mdx
│   ├── versioning.mdx
│   ├── cors.mdx
│   ├── static-website.mdx
│   ├── image-processing.mdx
│   └── custom-domain.mdx
│
├── php/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   ├── presigned-urls.mdx
│   ├── access-control.mdx
│   └── advanced-features.mdx
│
├── dotnet/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   ├── presigned-urls.mdx
│   ├── access-control.mdx
│   └── advanced-features.mdx
│
├── cpp/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── bucket-operations.mdx
│   ├── upload-objects.mdx
│   ├── multipart-upload.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   ├── access-control.mdx
│   └── advanced-features.mdx
│
├── browser-js/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── upload-objects.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   └── access-control.mdx
│
├── android/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── upload-objects.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   └── access-control.mdx
│
├── ios/
│   ├── installation.mdx
│   ├── initialization.mdx
│   ├── quick-start.mdx
│   ├── upload-objects.mdx
│   ├── download-objects.mdx
│   ├── manage-objects.mdx
│   └── access-control.mdx
│
└── ruby/
    ├── installation.mdx
    ├── initialization.mdx
    ├── quick-start.mdx
    ├── bucket-operations.mdx
    ├── upload-objects.mdx
    ├── download-objects.mdx
    └── manage-objects.mdx
```

---

## tools/ and resources/ (Tab 5)

```
tools/
├── ossutil/
│   ├── overview.mdx
│   ├── commands.mdx
│   └── ossutil-v1.mdx
│
├── ossbrowser/
│   └── overview.mdx
│
├── terraform/
│   ├── overview.mdx
│   └── manage-oss.mdx
│
├── oss-hdfs/
│   ├── overview.mdx
│   ├── setup.mdx
│   ├── limitations.mdx
│   └── migration.mdx
│
├── vectors/
│   ├── overview.mdx
│   ├── quickstart.mdx
│   ├── vector-index.mdx
│   └── embeddings-cli.mdx
│
└── mcp-server/
    └── overview.mdx

resources/
├── best-practices/
│   ├── performance.mdx
│   ├── security.mdx
│   ├── cost-optimization.mdx
│   ├── migration-from-s3.mdx
│   ├── migration-overview.mdx
│   ├── migration-tools.mdx
│   ├── hadoop-optimization.mdx
│   └── direct-client-upload-practices.mdx
│
├── troubleshooting/
│   ├── error-codes.mdx
│   ├── common-issues.mdx
│   └── sdk-troubleshooting.mdx
│
├── faq/
│   ├── general.mdx
│   ├── billing.mdx
│   ├── security-faq.mdx
│   └── sdk-faq.mdx
│
├── pricing/
│   ├── overview.mdx
│   ├── storage-fees.mdx
│   ├── traffic-fees.mdx
│   ├── api-fees.mdx
│   ├── pay-as-you-go.mdx
│   ├── resource-plans.mdx
│   └── query-bills.mdx
│
├── release-notes.mdx
├── s3-compatibility.mdx
├── sdk-compliance-guide.mdx
└── glossary.mdx
```

---

## Content Mapping: Crawled Source to New Structure

This table maps the key crawled content directories to their new locations:

| Crawled Source | New Location | Notes |
|---------------|-------------|-------|
| `user-guide/what-is-oss.md` | `get-started/what-is-oss.mdx` | Rewritten as landing content |
| `user-guide/get-started-with-oss.md` | `get-started/quickstart/*.mdx` | Split into 3 quickstarts |
| `user-guide/oss-bucket-*.md` | `get-started/concepts/buckets.mdx` + `guides/buckets/*.mdx` | Split concept vs how-to |
| `user-guide/object-*.md` | `get-started/concepts/objects.mdx` + `guides/objects/*.mdx` | Split concept vs how-to |
| `user-guide/upload-objects-*.md` | `guides/objects/upload-objects.mdx` | Consolidated with multi-lang |
| `user-guide/download-files.md` | `guides/objects/download-objects.mdx` | Consolidated with multi-lang |
| `user-guide/ram-policy.md` | `guides/access-control/ram-policies.mdx` | Enhanced with examples |
| `user-guide/data-encryption.md` | `guides/security/server-side-encryption.mdx` | Split SSE vs CSE |
| `user-guide/data-replication-*.md` | `guides/data-management/cross-region-replication.mdx` | Consolidated |
| `developer-reference/*.md` | `api-reference/**/*.mdx` | Reorganized by resource type |
| `api-reference/*.md` | `api-reference/**/*.mdx` | Reorganized by resource type |
| `sdk-java/*.md` | `sdks/java/*.mdx` | Standardized structure |
| `sdk-python/*.md` | `sdks/python/*.mdx` | Standardized structure |
| `sdk-go/*.md` | `sdks/go/*.mdx` | Standardized structure |
| `sdk-nodejs/*.md` | `sdks/nodejs/*.mdx` | Consolidated from 77 files |
| `sdk-php/*.md` | `sdks/php/*.mdx` | Consolidated from 87 files |
| `sdk-dotnet/*.md` | `sdks/dotnet/*.mdx` | Consolidated from 116 files |
| `sdk-browser/*.md` | `sdks/browser-js/*.mdx` | Consolidated from 34 files |
| `sdk-android/*.md` | `sdks/android/*.mdx` | Consolidated from 49 files |
| `sdk-ios/*.md` | `sdks/ios/*.mdx` | Consolidated from 44 files |
| `sdk-cpp/*.md` | `sdks/cpp/*.mdx` | Consolidated from 80 files |
| `sdk-ruby/*.md` | `sdks/ruby/*.mdx` | Consolidated from 34 files |
| `ossutil/*.md` | `tools/ossutil/*.mdx` | Kept separate |
| `ossbrowser/*.md` | `tools/ossbrowser/overview.mdx` | Single page |
| `best-practices/*.md` | `resources/best-practices/*.mdx` | Split into topics |
| `troubleshooting/*.md` | `resources/troubleshooting/*.mdx` | Split into topics |
| `faq/*.md` | `resources/faq/*.mdx` | Split by topic |
| `image-processing/*.md` | `guides/data-processing/image-processing.mdx` | Consolidated |
| `pricing/*.md` | `resources/pricing/*.mdx` | Restructured |
| `migration/*.md` | `resources/best-practices/migration-*.mdx` | Under best practices |
| `event-notifications/*.md` | `guides/advanced/event-notifications.mdx` | Consolidated |
| `static-website/*.md` | `guides/advanced/static-website-hosting.mdx` | Consolidated |
| `terraform/*.md` | `tools/terraform/*.mdx` | Kept separate |
| `oss-hdfs/*.md` | `tools/oss-hdfs/*.mdx` | Kept separate |
| `data-lake/*.md` | `guides/advanced/data-lake-integration.mdx` | Single page |
| `release-notes/*.md` | `resources/release-notes.mdx` | Consolidated |

### Key Consolidation Decisions

1. **SDK pages consolidated significantly**: The original has 548+ SDK files across 11 languages. Many are granular pages for individual operations (e.g., "create a bucket", "list buckets", "delete a bucket" as separate files). These are consolidated into operation-category pages (e.g., `bucket-operations.mdx` covers create, list, query, delete).

2. **User guide split by content type**: The original `user-guide/` mixes concepts and how-to instructions. These are split so concepts go to `get-started/concepts/` and task-oriented guides go to `guides/`.

3. **API reference reorganized by resource type**: The original has 188 flat API files. These are organized into subdirectories by resource (bucket-basic, bucket-acl-policy, object-basic, multipart-upload, etc.).

4. **Image processing consolidated**: 4 separate pages merged into a single comprehensive page in `guides/data-processing/`.

5. **Guides use multi-language code tabs**: Instead of separate pages per SDK for common operations, the Guides tab uses `<Tabs>` with code examples in Python, Java, Go, and Node.js inline. SDK-specific pages provide deeper coverage.
