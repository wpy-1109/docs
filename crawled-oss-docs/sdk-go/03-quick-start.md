# Go SDK - Quick Start

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go-quick-start

## V1 SDK Quick Start

```go
package main

import (
    "fmt"
    "log"
    "os"
    "github.com/aliyun/aliyun-oss-go-sdk/oss"
)

func main() {
    endpoint := "https://oss-cn-hangzhou.aliyuncs.com"
    accessKeyId := os.Getenv("ALIYUN_ACCESS_KEY_ID")
    accessKeySecret := os.Getenv("ALIYUN_ACCESS_KEY_SECRET")
    bucketName := "my-bucket"

    // Create client
    client, err := oss.New(endpoint, accessKeyId, accessKeySecret)
    if err != nil {
        log.Fatalf("Failed to create client: %v", err)
    }

    // Create bucket
    err = client.CreateBucket(bucketName)
    if err != nil {
        log.Fatalf("Failed to create bucket: %v", err)
    }

    // Get bucket handle
    bucket, err := client.Bucket(bucketName)
    if err != nil {
        log.Fatalf("Failed to get bucket: %v", err)
    }

    // Upload a file
    err = bucket.PutObjectFromFile("example.txt", "/path/to/local/file.txt")
    if err != nil {
        log.Fatalf("Failed to upload: %v", err)
    }
    fmt.Println("File uploaded successfully")

    // Download a file
    err = bucket.GetObjectToFile("example.txt", "/path/to/download/file.txt")
    if err != nil {
        log.Fatalf("Failed to download: %v", err)
    }
    fmt.Println("File downloaded successfully")

    // List objects
    lsRes, err := bucket.ListObjects()
    if err != nil {
        log.Fatalf("Failed to list objects: %v", err)
    }
    for _, object := range lsRes.Objects {
        fmt.Printf("Object: %s\n", object.Key)
    }

    // Delete object
    err = bucket.DeleteObject("example.txt")
    if err != nil {
        log.Fatalf("Failed to delete: %v", err)
    }
}
```

## V2 SDK Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"
    "strings"

    "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
    "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

func main() {
    cfg := oss.LoadDefaultConfig().
        WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
        WithRegion("cn-hangzhou")

    client := oss.NewClient(cfg)
    ctx := context.Background()

    bucket := "your-bucket-name"
    key := "your-object-name"

    // Upload from string
    body := strings.NewReader("hello oss")
    result, err := client.PutObject(ctx, &oss.PutObjectRequest{
        Bucket: oss.Ptr(bucket),
        Key:    oss.Ptr(key),
        Body:   body,
    })
    if err != nil {
        log.Fatalf("Failed to put object: %v", err)
    }
    fmt.Printf("Status: %s, ETag: %s\n", result.Status, oss.ToString(result.ETag))
}
```
