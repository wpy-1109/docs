# Python SDK - Initialization

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python-configuration-access-credentials

## V1 SDK (oss2) - Initialization

### Using AccessKey Directly

```python
import oss2

auth = oss2.Auth('<your-access-key-id>', '<your-access-key-secret>')
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', '<your-bucket-name>')
```

### Using Environment Variables (Recommended)

```python
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Ensure OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET are set
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', '<your-bucket-name>')
```

### Using STS Temporary Credentials

```python
import oss2

auth = oss2.StsAuth(
    '<your-access-key-id>',
    '<your-access-key-secret>',
    '<your-security-token>'
)
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', '<your-bucket-name>')
```

## V2 SDK - Initialization

### Using Environment Variables

```python
import alibabacloud_oss_v2 as oss

credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

cfg = oss.config.load_default()
cfg.credentials_provider = credentials_provider
cfg.region = 'cn-hangzhou'

client = oss.Client(cfg)
```

### Using Static Credentials

```python
import alibabacloud_oss_v2 as oss

credentials_provider = oss.credentials.StaticCredentialsProvider(
    access_key_id='<your-access-key-id>',
    access_key_secret='<your-access-key-secret>'
)

cfg = oss.config.load_default()
cfg.credentials_provider = credentials_provider
cfg.region = 'cn-hangzhou'

client = oss.Client(cfg)
```

## Credential Methods (Order of Preference)

1. **Environment variables** (`OSS_ACCESS_KEY_ID`, `OSS_ACCESS_KEY_SECRET`)
2. **RAM role / STS temporary credentials**
3. **Instance RAM role** (for ECS instances)
4. **Static credentials** (least recommended for production)

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `region` | Region identifier (e.g., `cn-hangzhou`) | Required |
| `endpoint` | Custom OSS endpoint | Auto-generated from region |
| `credentials_provider` | Credential provider | Required |
| `connect_timeout` | Connection timeout (seconds) | 60 |
| `readwrite_timeout` | Read/write timeout (seconds) | 120 |
