# Go SDK Installation

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go-installation

## SDK Versions

| Feature | SDK V1 (`aliyun-oss-go-sdk`) | SDK V2 (`alibabacloud-oss-go-sdk-v2`) |
|---------|------------------------------|---------------------------------------|
| **Import** | `github.com/aliyun/aliyun-oss-go-sdk/oss` | `github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss` |
| **Status** | Stable / maintained | **Recommended** (actively developed) |
| **Signature** | V1 | V4 (more secure) |
| **Resumable** | Basic | Advanced with checkpoints |

## Prerequisites

- Go 1.18 or later

## Install V1 SDK

```bash
go get github.com/aliyun/aliyun-oss-go-sdk
```

Import in your code:

```go
import "github.com/aliyun/aliyun-oss-go-sdk/oss"
```

## Install V2 SDK (Recommended)

```bash
go get github.com/aliyun/alibabacloud-oss-go-sdk-v2
```

Import in your code:

```go
import (
    "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
    "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)
```
