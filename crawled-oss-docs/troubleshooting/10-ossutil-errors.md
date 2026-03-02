# Troubleshooting ossutil Errors

Source: https://help.aliyun.com/zh/oss/

## Overview

ossutil is the official CLI tool for Alibaba Cloud OSS. This guide covers common errors and their solutions.

## Configuration Issues

### Invalid Configuration File

**Error**: `Error: invalid config file`

**Solution**: Recreate the configuration:
```bash
ossutil config
# Follow the prompts to enter:
# - Endpoint: oss-cn-hangzhou.aliyuncs.com
# - AccessKey ID: your-access-key-id
# - AccessKey Secret: your-access-key-secret
```

**Config file location**: `~/.ossutilconfig`

**Config file format**:
```ini
[Credentials]
language=EN
endpoint=oss-cn-hangzhou.aliyuncs.com
accessKeyID=your-access-key-id
accessKeySecret=your-access-key-secret
```

### Wrong Endpoint

**Error**: `NoSuchBucket` or `AccessDenied`

**Cause**: Endpoint doesn't match the Bucket's region.

**Solution**:
```bash
# Specify endpoint per command
ossutil ls oss://my-bucket/ -e oss-cn-beijing.aliyuncs.com

# Or update config
ossutil config -e oss-cn-beijing.aliyuncs.com
```

## Upload/Download Errors

### Upload Timeout

**Error**: `read tcp: i/o timeout` or `connection reset`

**Solutions**:
1. Increase timeout: `--timeout 300`
2. Use multipart upload for large files: `--bigfile-threshold 100000000` (100 MB)
3. Increase retry count: `--retry-times 10`
4. Use checkpoint for resumable upload: `--checkpoint-dir /tmp/oss-checkpoint`

### Large File Upload

```bash
# Recommended settings for large files
ossutil cp large-file.zip oss://bucket/path/ \
  --bigfile-threshold 104857600 \
  --part-size 10485760 \
  --parallel 10 \
  --checkpoint-dir /tmp/checkpoint/ \
  --retry-times 5
```

### Batch Upload/Download

```bash
# Upload a directory recursively
ossutil cp /local/dir/ oss://bucket/remote/dir/ -r

# Download a directory recursively
ossutil cp oss://bucket/remote/dir/ /local/dir/ -r

# Sync (only transfer changed files)
ossutil sync /local/dir/ oss://bucket/remote/dir/
```

### Permission Denied During Upload

**Error**: `AccessDenied`

**Checklist**:
- [ ] Verify AccessKey ID and Secret
- [ ] Check RAM permissions for `oss:PutObject`
- [ ] Verify Bucket name and region
- [ ] Check Bucket Policy for deny rules
- [ ] Ensure Block Public Access isn't interfering (for public Buckets)

## Common Command Errors

### ls (List Objects)

```bash
# List Buckets
ossutil ls

# List objects in a Bucket
ossutil ls oss://bucket-name/

# List with details (size, date)
ossutil ls oss://bucket-name/ -d

# List all objects recursively
ossutil ls oss://bucket-name/ --all-type
```

### cp (Copy/Upload/Download)

```bash
# Upload
ossutil cp local-file.txt oss://bucket/path/file.txt

# Download
ossutil cp oss://bucket/path/file.txt local-file.txt

# Copy between Buckets
ossutil cp oss://source-bucket/file.txt oss://dest-bucket/file.txt
```

### rm (Delete)

```bash
# Delete a single object
ossutil rm oss://bucket/path/file.txt

# Delete objects recursively (use with caution!)
ossutil rm oss://bucket/path/ -r

# Delete with confirmation prompt
ossutil rm oss://bucket/path/ -r --confirm
```

### stat (Object Info)

```bash
# Get object metadata
ossutil stat oss://bucket/path/file.txt
```

## Performance Optimization

### Speed Up Transfers
```bash
# Increase parallelism
ossutil cp /dir/ oss://bucket/ -r \
  --parallel 20 \
  --part-size 5242880 \
  --jobs 10

# Use internal endpoint (from ECS)
ossutil cp /dir/ oss://bucket/ -r \
  -e oss-cn-hangzhou-internal.aliyuncs.com
```

### Monitor Transfer Progress
```bash
# Enable progress bar
ossutil cp large-file.zip oss://bucket/ --progress
```

## Troubleshooting Checklist

- [ ] Verify ossutil version is up to date: `ossutil version`
- [ ] Check configuration: `ossutil config -e`
- [ ] Verify connectivity: `ossutil ls`
- [ ] Check specific Bucket access: `ossutil ls oss://bucket-name/`
- [ ] Enable verbose output: `--loglevel debug`
- [ ] Check for proxy issues: set `http_proxy`/`https_proxy` environment variables
