# Go SDK - Object Upload and Download

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go-upload-download

## V1 SDK - Upload

### Upload from File

```go
bucket, err := client.Bucket("my-bucket")
if err != nil {
    log.Fatal(err)
}

err = bucket.PutObjectFromFile("example.txt", "/path/to/local/file.txt")
if err != nil {
    log.Fatal(err)
}
fmt.Println("File uploaded successfully")
```

### Upload from String/Reader

```go
import "strings"

err = bucket.PutObject("example.txt", strings.NewReader("Hello OSS!"))
```

### Upload with Metadata

```go
options := []oss.Option{
    oss.ContentType("text/plain"),
    oss.Meta("author", "example-user"),
    oss.ObjectACL(oss.ACLPublicRead),
}
err = bucket.PutObject("example.txt", strings.NewReader("content"), options...)
```

## V1 SDK - Download

### Download to File

```go
err = bucket.GetObjectToFile("example.txt", "/path/to/local/file.txt")
```

### Download to Memory (Stream)

```go
body, err := bucket.GetObject("example.txt")
if err != nil {
    log.Fatal(err)
}
defer body.Close()

data, err := io.ReadAll(body)
fmt.Println(string(data))
```

### Range Download

```go
body, err := bucket.GetObject("example.txt", oss.Range(0, 1023))
```

### Conditional Download

```go
body, err := bucket.GetObject("example.txt",
    oss.IfModifiedSince(time.Date(2025, 1, 1, 0, 0, 0, 0, time.UTC)))
```

## V2 SDK - Upload

### Upload from String

```go
result, err := client.PutObject(ctx, &oss.PutObjectRequest{
    Bucket:      oss.Ptr("my-bucket"),
    Key:         oss.Ptr("documents/hello.txt"),
    Body:        strings.NewReader("Hello, Alibaba Cloud OSS!"),
    ContentType: oss.Ptr("text/plain"),
    Metadata: map[string]string{
        "author":  "John Doe",
        "version": "1.0",
    },
})
fmt.Printf("ETag: %s, VersionId: %s\n",
    oss.ToString(result.ETag), oss.ToString(result.VersionId))
```

### Upload from File

```go
file, err := os.Open("/path/to/local/file.jpg")
if err != nil {
    log.Fatal(err)
}
defer file.Close()
fileStat, _ := file.Stat()

result, err := client.PutObject(ctx, &oss.PutObjectRequest{
    Bucket:        oss.Ptr("my-bucket"),
    Key:           oss.Ptr("images/photo.jpg"),
    Body:          file,
    ContentType:   oss.Ptr("image/jpeg"),
    ContentLength: oss.Ptr(fileStat.Size()),
    StorageClass:  oss.StorageClassIA,
    Acl:           oss.ObjectACLPublicRead,
})
fmt.Printf("ETag: %s, CRC64: %s\n",
    oss.ToString(result.ETag), oss.ToString(result.HashCRC64))
```

## V2 SDK - Download

```go
result, err := client.GetObject(ctx, &oss.GetObjectRequest{
    Bucket: oss.Ptr("my-bucket"),
    Key:    oss.Ptr("example.txt"),
})
if err != nil {
    log.Fatal(err)
}
defer result.Body.Close()

data, err := io.ReadAll(result.Body)
fmt.Println(string(data))
```

## List Objects

### V1

```go
lsRes, err := bucket.ListObjects()
for _, object := range lsRes.Objects {
    fmt.Printf("Object: %s, Size: %d\n", object.Key, object.Size)
}

// With prefix
lsRes, err := bucket.ListObjects(oss.Prefix("photos/"))
```

### V2

```go
result, err := client.ListObjectsV2(ctx, &oss.ListObjectsV2Request{
    Bucket: oss.Ptr("my-bucket"),
    Prefix: oss.Ptr("photos/"),
})
for _, obj := range result.Contents {
    fmt.Printf("Key: %s, Size: %d\n",
        oss.ToString(obj.Key), obj.Size)
}
```

## Delete Objects

### V1

```go
// Single delete
err = bucket.DeleteObject("example.txt")

// Multiple delete
objectKeys := []string{"key1", "key2", "key3"}
result, err := bucket.DeleteObjects(objectKeys)
```

### V2

```go
_, err := client.DeleteObject(ctx, &oss.DeleteObjectRequest{
    Bucket: oss.Ptr("my-bucket"),
    Key:    oss.Ptr("example.txt"),
})
```

## Copy Objects

### V1

```go
_, err = bucket.CopyObject("source-key", "dest-key")

// Cross-bucket copy
_, err = bucket.CopyObjectFrom("source-bucket", "source-key", "dest-key")
```
