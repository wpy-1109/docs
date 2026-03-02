# Go SDK - Initialization

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go-initialization

## V1 SDK - Creating a Client

### Using AccessKey Directly

```go
package main

import (
    "fmt"
    "github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
    endpoint := "https://oss-cn-hangzhou.aliyuncs.com"
    accessKeyId := "<your-access-key-id>"
    accessKeySecret := "<your-access-key-secret>"

    client, err := oss.New(endpoint, accessKeyId, accessKeySecret)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }

    fmt.Println("Client created successfully")
    _ = client
}
```

### Using Environment Variables

```go
package main

import (
    "fmt"
    "os"
    "github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
    endpoint := "https://oss-cn-hangzhou.aliyuncs.com"
    accessKeyId := os.Getenv("ALIYUN_ACCESS_KEY_ID")
    accessKeySecret := os.Getenv("ALIYUN_ACCESS_KEY_SECRET")

    client, err := oss.New(endpoint, accessKeyId, accessKeySecret)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    _ = client
}
```

### Using STS Temporary Credentials

```go
client, err := oss.New(endpoint, accessKeyId, accessKeySecret,
    oss.SecurityToken(securityToken))
```

## V2 SDK - Creating a Client

### Using Environment Variables (Recommended)

```go
package main

import (
    "context"
    "log"
    "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
    "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

func main() {
    // Method 1: Only specify Region (recommended)
    cfg := oss.LoadDefaultConfig().
        WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
        WithRegion("cn-hangzhou")

    client := oss.NewClient(cfg)

    // Method 2: Specify both Region and Endpoint
    // cfg := oss.LoadDefaultConfig().
    //     WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
    //     WithRegion("cn-hangzhou").
    //     WithEndpoint("https://oss-cn-hangzhou.aliyuncs.com")

    _ = client
}
```

## Configuration Notes

- **V2 SDK uses V4 signature by default** for improved security
- **Region is required** for V2 SDK; the endpoint is auto-constructed from region
- When region is `cn-hangzhou`, the constructed endpoint is `https://oss-cn-hangzhou.aliyuncs.com`
- SDK defaults to HTTPS; to use HTTP, specify the endpoint with `http://` prefix
