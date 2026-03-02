# Use Terraform to Manage OSS

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/use-terraform-to-manage-oss

## Overview

You can use Terraform to create and manage OSS buckets and their configurations. This page provides detailed examples of managing OSS resources with the Alibaba Cloud Terraform provider (`alicloud`).

## Prerequisites

1. Install Terraform on your local machine
2. Configure the Alibaba Cloud provider with valid credentials
3. Have an Alibaba Cloud account with OSS permissions

## Create a Bucket with Full Configuration

```hcl
resource "alicloud_oss_bucket" "full_example" {
  bucket        = "my-production-bucket"
  acl           = "private"
  storage_class = "Standard"

  # Enable versioning
  versioning {
    status = "Enabled"
  }

  # Server-side encryption
  server_side_encryption_rule {
    sse_algorithm = "AES256"
  }

  # Logging
  logging {
    target_bucket = alicloud_oss_bucket.log_bucket.id
    target_prefix = "log/"
  }

  # CORS configuration
  cors_rule {
    allowed_origins = ["https://example.com"]
    allowed_methods = ["GET", "PUT", "POST"]
    allowed_headers = ["*"]
    max_age_seconds = 3600
  }

  # Lifecycle rules
  lifecycle_rule {
    id      = "transition-to-ia"
    enabled = true
    prefix  = "data/"

    transitions {
      days          = 30
      storage_class = "IA"
    }

    transitions {
      days          = 90
      storage_class = "Archive"
    }
  }

  lifecycle_rule {
    id      = "expire-logs"
    enabled = true
    prefix  = "logs/"

    expiration {
      days = 180
    }
  }

  # Referer configuration
  referer_config {
    allow_empty = false
    referers    = ["https://example.com", "https://*.example.com"]
  }

  # Website configuration
  website {
    index_document = "index.html"
    error_document = "error.html"
  }

  tags = {
    Environment = "production"
    Team        = "engineering"
  }
}
```

## Upload Objects

```hcl
# Upload a file
resource "alicloud_oss_bucket_object" "upload_file" {
  bucket = alicloud_oss_bucket.full_example.bucket
  key    = "documents/readme.txt"
  source = "./files/readme.txt"
}

# Upload content directly
resource "alicloud_oss_bucket_object" "upload_content" {
  bucket       = alicloud_oss_bucket.full_example.bucket
  key          = "config/settings.json"
  content      = jsonencode({ "version" = "1.0" })
  content_type = "application/json"
}
```

## Data Sources

```hcl
# List buckets matching a pattern
data "alicloud_oss_buckets" "filtered" {
  name_regex = "my-.*-bucket"
}

output "bucket_names" {
  value = data.alicloud_oss_buckets.filtered.buckets[*].name
}

# List objects in a bucket
data "alicloud_oss_bucket_objects" "logs" {
  bucket_name = "my-production-bucket"
  key_prefix  = "logs/"
}
```

## Bucket Policy

```hcl
resource "alicloud_oss_bucket_policy" "example" {
  bucket = alicloud_oss_bucket.full_example.bucket

  policy = jsonencode({
    "Statement" = [
      {
        "Action"    = ["oss:GetObject"]
        "Effect"    = "Allow"
        "Principal" = ["*"]
        "Resource"  = ["acs:oss:*:*:my-production-bucket/public/*"]
      }
    ]
    "Version" = "1"
  })
}
```

## Import Existing Resources

```bash
# Import an existing bucket
terraform import alicloud_oss_bucket.example my-existing-bucket
```

## Best Practices

1. **Use variables** for bucket names and regions to support multiple environments
2. **Enable versioning** for production buckets to protect against accidental deletion
3. **Configure lifecycle rules** to optimize storage costs
4. **Use server-side encryption** for sensitive data
5. **Set up logging** for audit and compliance
6. **Apply tags** for cost allocation and resource management
