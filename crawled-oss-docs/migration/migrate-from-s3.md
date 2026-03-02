# Migrate Data from Amazon S3 to Alibaba Cloud OSS

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/migrate-data-from-amazon-s3-to-alibaba-cloud-oss

## Overview

This guide covers the end-to-end migration process from Amazon S3 to Alibaba Cloud OSS using Data Online Migration and other tools.

## Prerequisites

1. An Alibaba Cloud account with OSS activated
2. A destination OSS bucket created in the desired region
3. AWS IAM credentials with the following permissions:
   - `s3:GetObject`
   - `s3:ListBucket`
   - `s3:GetBucketLocation`
4. An Alibaba Cloud RAM user with OSS write permissions

## Method 1: Data Online Migration (Recommended)

### Step 1: Activate Data Online Migration

1. Log in to the Alibaba Cloud Console
2. Search for "Data Online Migration" or navigate to it through the product menu
3. Activate the service if not already enabled

### Step 2: Create a Migration Task

1. Click **Create Migration Task**
2. Configure the **Source**:
   - **Source Type**: Amazon S3
   - **Source Bucket**: Your S3 bucket name
   - **Access Key ID**: AWS Access Key ID
   - **Access Key Secret**: AWS Secret Access Key
   - **Source Endpoint**: e.g., `s3.us-west-2.amazonaws.com`
   - **Source Prefix** (optional): Filter by prefix, e.g., `data/`

3. Configure the **Destination**:
   - **Destination Bucket**: Your OSS bucket name
   - **Destination Endpoint**: e.g., `oss-cn-hangzhou.aliyuncs.com`
   - **Access Key ID**: Alibaba Cloud Access Key ID
   - **Access Key Secret**: Alibaba Cloud Access Key Secret
   - **Destination Prefix** (optional): Add a prefix to all migrated objects

4. Configure **Migration Settings**:
   - **Migration Type**: Full migration or incremental migration
   - **Overwrite Policy**: Always overwrite, overwrite if different size/time, or never overwrite
   - **Speed Limit** (optional): Throttle bandwidth in MB/s
   - **Schedule** (optional): Schedule the migration to run at specific times

5. Click **Create** to start the migration

### Step 3: Monitor Progress

- View migration task status in the Data Online Migration console
- Check progress, success/failure counts, and data volume
- Review detailed logs for any failed objects

## Method 2: OSSImport

### Standalone Mode Configuration

**local_job.cfg example:**
```properties
# Source configuration
srcType=s3
srcAccessKey=<AWS_ACCESS_KEY_ID>
srcSecretKey=<AWS_SECRET_ACCESS_KEY>
srcDomain=s3.us-west-2.amazonaws.com
srcBucket=source-s3-bucket
srcPrefix=

# Destination configuration
destAccessKey=<ALIBABA_ACCESS_KEY_ID>
destSecretKey=<ALIBABA_ACCESS_KEY_SECRET>
destDomain=oss-cn-hangzhou.aliyuncs.com
destBucket=destination-oss-bucket
destPrefix=

# Migration settings
isSkipExistFile=false
workerCount=10
taskObjectCountLimit=10000
taskObjectSizeLimit=1073741824
```

### Run the Migration

```bash
# Start the migration
bash import.sh

# Check status
bash stat.sh

# Retry failed tasks
bash retry.sh
```

## Method 3: Application-Level Migration (S3 Compatibility)

For applications using the S3 API, you can migrate by updating endpoint and credential configurations:

### Before (S3)
```python
import boto3

s3 = boto3.client('s3',
    aws_access_key_id='AWS_ACCESS_KEY',
    aws_secret_access_key='AWS_SECRET_KEY',
    region_name='us-west-2'
)
```

### After (OSS with S3 compatibility)
```python
import boto3

oss = boto3.client('s3',
    aws_access_key_id='ALIBABA_ACCESS_KEY',
    aws_secret_access_key='ALIBABA_SECRET_KEY',
    endpoint_url='https://oss-cn-hangzhou.aliyuncs.com',
    region_name='cn-hangzhou'
)
```

## Post-Migration Verification

1. **Object Count**: Compare the number of objects in S3 and OSS
2. **Data Size**: Verify total data volume matches
3. **Content Integrity**: Spot-check objects by comparing checksums (ETag/MD5)
4. **Metadata**: Verify that object metadata has been preserved
5. **Permissions**: Configure appropriate ACL/bucket policies on OSS

## Best Practices

- **Test with a small dataset first** before migrating the full dataset
- **Use incremental migration** to catch changes during the migration window
- **Set up monitoring** to track migration progress and failures
- **Plan for DNS cutover** if switching application endpoints from S3 to OSS
- **Keep source data** until migration is fully verified
- **Consider transfer acceleration** for cross-region migrations
