# ossutil 1.0 Overview

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/overview-59/

ossutil allows you to manage Object Storage Service (OSS) data by using command lines on Windows, Linux, and macOS operating systems.

> **Note:** Alibaba Cloud recommends upgrading to **ossutil 2.0**. See the ossutil 2.0 documentation for the latest features.

## Key Improvements in ossutil 2.0

- **New command syntax**: Multi-level commands (API-level and high-level)
- **Optimized configuration**: Simplified initial setup, multiple profiles via `--profile`
- **Multiple filter parameters**: Path, file size, modified time, metadata filters
- **Flexible output formats**: JSON, YAML, XML via `--output-format`
- **Enhanced security**: Environment variables for credentials, `--dry-run` option

## ossutil 1.0 Common Commands

| Command | Description |
|---------|-------------|
| access-monitor | Set access tracking state of a bucket |
| appendfromfile | Append content to appendable objects |
| bucket-cname | Query CNAME configurations |
| bucket-encryption | Manage bucket encryption |
| bucket-policy | Manage bucket policies |
| bucket-tagging | Manage bucket tags |
| bucket-versioning | Manage versioning |
| cat | Output object content |
| config | Create configuration file |
| cors | Manage CORS rules |
| cors-options | Test cross-origin requests |
| cp | Upload, download, or copy objects |
| create-symlink | Create symbolic links |
| du | Query storage usage |
| getallpartsize | Query multipart upload sizes |
| hash | Calculate CRC-64 or MD5 hash |
| help | Query command help |
| inventory | Manage inventory configurations |
| lifecycle | Manage lifecycle rules |
| listpart | List multipart upload parts |
| logging | Manage logging configurations |
| lrb | List buckets by region |
| ls | List buckets, objects, or parts |
| mb | Create a bucket |
| mkdir | Create a directory |
| object-tagging | Manage object tags |
| probe | Monitor and troubleshoot access |
| read-symlink | Read symbolic link description |
| referer | Manage hotlink protection |
| replication | Manage Cross-Region Replication (CRR) |
| request-payment | Configure pay-by-requester |
| resource-group | Configure resource groups |
| restore | Restore frozen objects |
| revert-versioning | Recover deleted objects to latest version |
| rm | Delete buckets, objects, or parts |
| set-acl | Configure ACL for buckets/objects |
| set-meta | Configure object metadata |
| sign | Generate signed URLs |
| stat | Get bucket/object information |
| style | Configure image styles |
| sync | Synchronize files/objects |
| update | Update ossutil version |
| website | Manage static website hosting |
| worm | Query retention policies |
