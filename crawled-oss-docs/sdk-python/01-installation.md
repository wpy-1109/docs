# Python SDK Installation

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python-installation

## SDK Versions

| Feature | SDK V1 (`oss2`) | SDK V2 (`alibabacloud-oss-v2`) |
|---------|-----------------|-------------------------------|
| **Install command** | `pip install oss2` | `pip install alibabacloud-oss-v2` |
| **Status** | Legacy / maintained | **Recommended** (actively developed) |
| **Python version** | 3.x | 3.x |
| **Async support** | No | Yes |
| **CRC checksum** | Basic | Enhanced |
| **Credential providers** | Basic | Full credential chain support |

## Prerequisites

- Python 3.x (Python 2.x is no longer supported)
- pip package manager

## Install V1 SDK (oss2)

```bash
pip install oss2
```

### Verify Installation

```bash
python -c "import oss2; print(oss2.__version__)"
```

## Install V2 SDK (Recommended)

```bash
pip install alibabacloud-oss-v2
```

### Verify Installation

```bash
python -c "import alibabacloud_oss_v2; print('SDK V2 installed successfully')"
```

## Install from Source

```bash
git clone https://github.com/aliyun/alibabacloud-oss-python-sdk-v2.git
cd alibabacloud-oss-python-sdk-v2
pip install -e .
```
