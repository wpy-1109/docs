# Terraform Overview for OSS

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/terraform-overview

## Overview

The Alibaba Cloud Terraform Provider (`alicloud`) offers several resources and data sources for managing Object Storage Service (OSS) infrastructure as code.

## Terraform Resources for OSS

### alicloud_oss_bucket

Creates and manages an OSS bucket with support for:
- Bucket name, ACL, storage class
- Versioning, logging, lifecycle rules
- Server-side encryption
- Cross-region replication
- Website hosting configuration
- CORS rules
- Referer configuration

### alicloud_oss_bucket_object

Uploads and manages objects within an OSS bucket.

### alicloud_oss_bucket_acl

Manages access control lists for OSS buckets.

### alicloud_oss_bucket_policy

Configures bucket-level policies.

### alicloud_oss_bucket_versioning

Manages versioning settings for a bucket.

### alicloud_oss_bucket_lifecycle

Manages lifecycle rules separately from the bucket resource itself (newer provider versions).

## Data Sources

- **alicloud_oss_buckets** - Lists existing OSS buckets (supports filtering by name regex)
- **alicloud_oss_bucket_objects** - Lists objects within a bucket

## Example: Basic Bucket with Versioning and Lifecycle

```hcl
resource "alicloud_oss_bucket" "example" {
  bucket = "my-example-bucket"
  acl    = "private"

  versioning {
    status = "Enabled"
  }

  lifecycle_rule {
    id      = "rule-1"
    enabled = true
    prefix  = "logs/"

    expiration {
      days = 365
    }

    transitions {
      days          = 30
      storage_class = "IA"
    }

    transitions {
      days          = 60
      storage_class = "Archive"
    }
  }

  tags = {
    Environment = "Production"
  }
}

resource "alicloud_oss_bucket_object" "example" {
  bucket  = alicloud_oss_bucket.example.bucket
  key     = "example.txt"
  content = "Hello, World!"
}
```

## Supported Lifecycle Actions

| Action | Description |
|--------|-------------|
| **Expiration** | Automatically delete objects after a specified number of days or on a specific date |
| **Transitions** | Move objects to a different storage class (IA, Archive, Cold Archive) |
| **Abort Multipart Upload** | Clean up incomplete multipart uploads |
| **Noncurrent Version Expiration** | Expire noncurrent object versions (for versioned buckets) |
| **Noncurrent Version Transition** | Transition noncurrent versions to different storage classes |

## Key Lifecycle Parameters

- **`id`** - Unique identifier for the lifecycle rule
- **`enabled`** - Whether the rule is active (true/false)
- **`prefix`** - Object key prefix filter for the rule
- **`tags`** - Tag-based filtering for lifecycle rules
- **`expiration`** - Defines when objects expire
- **`transitions`** - Defines storage class transitions

## Provider Configuration

```hcl
provider "alicloud" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = var.region
}

variable "access_key" {
  description = "Alibaba Cloud Access Key ID"
  type        = string
  sensitive   = true
}

variable "secret_key" {
  description = "Alibaba Cloud Access Key Secret"
  type        = string
  sensitive   = true
}

variable "region" {
  description = "Alibaba Cloud Region"
  type        = string
  default     = "cn-hangzhou"
}
```

## References

- Terraform Provider Registry: https://registry.terraform.io/providers/aliyun/alicloud/latest/docs
- Use Terraform to Manage OSS: https://www.alibabacloud.com/help/en/oss/developer-reference/use-terraform-to-manage-oss
