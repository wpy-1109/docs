# Go SDK - Presigned URLs, Lifecycle, Versioning, Access Control, Encryption, Error Handling

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go

## Presigned URLs

### V1 SDK

```go
// Generate signed GET URL (download)
signedURL, err := bucket.SignURL("example.txt", oss.HTTPGet, 3600) // 1 hour
fmt.Println("Download URL:", signedURL)

// Generate signed PUT URL (upload)
signedURL, err := bucket.SignURL("example.txt", oss.HTTPPut, 3600)
fmt.Println("Upload URL:", signedURL)

// With content type
options := []oss.Option{
    oss.ContentType("application/octet-stream"),
}
signedURL, err := bucket.SignURL("example.txt", oss.HTTPPut, 3600, options...)
```

### V2 SDK

```go
import "time"

// Generate presigned download URL
result, err := client.Presign(ctx,
    &oss.GetObjectRequest{
        Bucket: oss.Ptr("examplebucket"),
        Key:    oss.Ptr("exampleobject.txt"),
    },
    oss.PresignExpires(60*time.Second))

fmt.Printf("Method: %s\n", result.Method)
fmt.Printf("URL: %s\n", result.URL)
fmt.Printf("Expiration: %s\n", result.Expiration)

// Generate presigned upload URL
result, err := client.Presign(ctx,
    &oss.PutObjectRequest{
        Bucket: oss.Ptr("examplebucket"),
        Key:    oss.Ptr("exampleobject.txt"),
    },
    oss.PresignExpires(3600*time.Second))
```

## Lifecycle Rules

### V1 SDK

```go
// Set lifecycle rules
rules := []oss.LifecycleRule{
    {
        ID:     "rule1",
        Prefix: "logs/",
        Status: "Enabled",
        Expiration: &oss.LifecycleExpiration{
            Days: 30,
        },
    },
    {
        ID:     "rule2",
        Prefix: "archive/",
        Status: "Enabled",
        Transitions: []oss.LifecycleTransition{
            {
                Days:         60,
                StorageClass: oss.StorageIA,
            },
        },
    },
}
err := client.SetBucketLifecycle("my-bucket", rules)

// Get lifecycle rules
result, err := client.GetBucketLifecycle("my-bucket")
for _, rule := range result.Rules {
    fmt.Printf("Rule: %s, Prefix: %s, Status: %s\n",
        rule.ID, rule.Prefix, rule.Status)
}

// Delete lifecycle rules
err := client.DeleteBucketLifecycle("my-bucket")
```

## Versioning

### V1 SDK

```go
// Enable versioning
err := client.SetBucketVersioning("my-bucket", oss.VersionEnabled)

// Suspend versioning
err := client.SetBucketVersioning("my-bucket", oss.VersionSuspended)

// Get versioning status
result, err := client.GetBucketVersioning("my-bucket")
fmt.Printf("Versioning: %s\n", result.Status)

// Download specific version
body, err := bucket.GetObject("example.txt",
    oss.VersionId("your-version-id"))

// Delete specific version
err = bucket.DeleteObject("example.txt",
    oss.VersionId("your-version-id"))

// List versions
result, err := bucket.ListObjectVersions()
for _, v := range result.ObjectVersions {
    fmt.Printf("Key: %s, VersionId: %s, IsLatest: %v\n",
        v.Key, v.VersionId, v.IsLatest)
}
```

## Access Control

### V1 SDK

```go
// Set bucket ACL
err := client.SetBucketACL("my-bucket", oss.ACLPublicRead)
// Options: ACLPrivate, ACLPublicRead, ACLPublicReadWrite

// Get bucket ACL
result, err := client.GetBucketACL("my-bucket")
fmt.Printf("ACL: %s\n", result.ACL)

// Set object ACL
err = bucket.SetObjectACL("example.txt", oss.ACLPublicRead)

// Get object ACL
result, err := bucket.GetObjectACL("example.txt")
```

### CORS

```go
rules := []oss.CORSRule{
    {
        AllowedOrigin: []string{"https://example.com"},
        AllowedMethod: []string{"GET", "PUT", "POST"},
        AllowedHeader: []string{"*"},
        MaxAgeSeconds: 3600,
    },
}
err := client.SetBucketCORS("my-bucket", rules)
```

## Encryption

### Server-Side Encryption

```go
// Set default encryption (SSE-OSS)
rule := oss.ServerEncryptionRule{
    SSEDefault: oss.SSEDefaultRule{
        SSEAlgorithm: "AES256",
    },
}
err := client.SetBucketEncryption("my-bucket", rule)

// Set default encryption (SSE-KMS)
rule := oss.ServerEncryptionRule{
    SSEDefault: oss.SSEDefaultRule{
        SSEAlgorithm: "KMS",
        KMSMasterKeyID: "<your-cmk-id>",
    },
}
err := client.SetBucketEncryption("my-bucket", rule)

// Get encryption config
result, err := client.GetBucketEncryption("my-bucket")

// Delete encryption config
err := client.DeleteBucketEncryption("my-bucket")
```

### Per-Object Encryption

```go
err = bucket.PutObject("encrypted.txt", strings.NewReader("secret data"),
    oss.ServerSideEncryption("AES256"))
```

## Client-Side Encryption (V2 SDK)

```go
import "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/crypto"

mc, err := crypto.CreateMasterRsa(materialDesc, "yourRsaPublicKey", "yourRsaPrivateKey")
eclient, err := oss.NewEncryptionClient(client, mc)

// Upload encrypted
eclient.PutObject(ctx, &oss.PutObjectRequest{
    Bucket: oss.Ptr("my-bucket"),
    Key:    oss.Ptr("encrypted.txt"),
    Body:   strings.NewReader("secret data"),
})

// Download and decrypt
result, err := eclient.GetObject(ctx, &oss.GetObjectRequest{
    Bucket: oss.Ptr("my-bucket"),
    Key:    oss.Ptr("encrypted.txt"),
})
```

## Error Handling

### V1 SDK

```go
err := bucket.PutObjectFromFile("example.txt", "/path/to/file")
if err != nil {
    switch e := err.(type) {
    case oss.ServiceError:
        fmt.Printf("Server Error - Code: %s, Message: %s, RequestId: %s, HostId: %s\n",
            e.Code, e.Message, e.RequestId, e.HostId)
    case oss.UnexpectedStatusCodeError:
        fmt.Printf("Unexpected Status: %d\n", e.Got())
    default:
        fmt.Printf("Error: %v\n", err)
    }
}
```

### V2 SDK

```go
result, err := client.PutObject(ctx, request)
if err != nil {
    var se *oss.ServiceError
    if errors.As(err, &se) {
        fmt.Printf("Service Error: Code=%s, Message=%s, RequestId=%s\n",
            se.Code, se.Message, se.RequestId)
    } else {
        fmt.Printf("Error: %v\n", err)
    }
}
```

## Common Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `AccessDenied` | 403 | Access denied |
| `BucketAlreadyExists` | 409 | Bucket already exists |
| `BucketNotEmpty` | 409 | Bucket is not empty |
| `NoSuchBucket` | 404 | Bucket does not exist |
| `NoSuchKey` | 404 | Object does not exist |
| `InvalidAccessKeyId` | 403 | Invalid AccessKey |
| `SignatureDoesNotMatch` | 403 | Signature mismatch |

## Image Processing

### V1 SDK

```go
// Resize
options := []oss.Option{
    oss.Process("image/resize,m_fixed,w_100,h_100"),
}
body, err := bucket.GetObject("photo.jpg", options...)

// Watermark
options := []oss.Option{
    oss.Process("image/watermark,text_SGVsbG8gT1NT"),
}

// Format conversion
options := []oss.Option{
    oss.Process("image/format,png"),
}

// Use predefined style
options := []oss.Option{
    oss.Process("style/my-style-name"),
}
```

## Documentation Reference Links

| Topic | V1 URL |
|-------|--------|
| Installation | https://help.aliyun.com/zh/oss/developer-reference/go-installation |
| Quick Start | https://help.aliyun.com/zh/oss/developer-reference/quick-start |
| Buckets | https://help.aliyun.com/zh/oss/developer-reference/buckets-3/ |
| Objects | https://help.aliyun.com/zh/oss/developer-reference/objects/ |
| Access Control | https://help.aliyun.com/zh/oss/developer-reference/access-control-1/ |
| Data Security | https://help.aliyun.com/zh/oss/developer-reference/data-security/ |
| Versioning | https://help.aliyun.com/zh/oss/developer-reference/versioning-12/ |
| Encryption | https://help.aliyun.com/zh/oss/developer-reference/data-encryption-4/ |
| Lifecycle | https://help.aliyun.com/zh/oss/developer-reference/data-management-1/ |
| Image Processing | https://help.aliyun.com/zh/oss/developer-reference/img-4 |
| Error Handling | https://help.aliyun.com/zh/oss/developer-reference/error-handling-2 |
