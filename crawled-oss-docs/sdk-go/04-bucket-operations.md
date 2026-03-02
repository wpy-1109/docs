# Go SDK - Bucket Operations

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go-manage-buckets

## V1 SDK

### Create a Bucket

```go
err := client.CreateBucket("my-bucket")

// With options
err := client.CreateBucket("my-bucket",
    oss.StorageClass(oss.StorageStandard),
    oss.ACL(oss.ACLPrivate),
    oss.RedundancyType(oss.RedundancyLRS))
```

### List Buckets

```go
result, err := client.ListBuckets()
if err != nil {
    log.Fatal(err)
}
for _, bucket := range result.Buckets {
    fmt.Printf("Bucket: %s, Location: %s\n", bucket.Name, bucket.Location)
}
```

### Check if Bucket Exists

```go
exists, err := client.IsBucketExist("my-bucket")
fmt.Printf("Bucket exists: %v\n", exists)
```

### Get Bucket Info

```go
info, err := client.GetBucketInfo("my-bucket")
fmt.Printf("Name: %s\n", info.BucketInfo.Name)
fmt.Printf("Location: %s\n", info.BucketInfo.Location)
fmt.Printf("StorageClass: %s\n", info.BucketInfo.StorageClass)
```

### Set Bucket ACL

```go
err := client.SetBucketACL("my-bucket", oss.ACLPublicRead)
// Options: ACLPrivate, ACLPublicRead, ACLPublicReadWrite
```

### Delete a Bucket

```go
err := client.DeleteBucket("my-bucket")
```

## V2 SDK

### Create a Bucket

```go
result, err := client.PutBucket(ctx, &oss.PutBucketRequest{
    Bucket: oss.Ptr("my-bucket"),
})
fmt.Printf("Bucket created: statusCode=%d, requestId=%s\n",
    result.StatusCode, oss.ToString(result.Headers.Get("X-Oss-Request-Id")))
```

### List Buckets

```go
result, err := client.ListBuckets(ctx, &oss.ListBucketsRequest{})
for _, b := range result.Buckets {
    fmt.Printf("Bucket: %s, Location: %s\n",
        oss.ToString(b.Name), oss.ToString(b.Location))
}
```

### Delete a Bucket

```go
_, err := client.DeleteBucket(ctx, &oss.DeleteBucketRequest{
    Bucket: oss.Ptr("my-bucket"),
})
```
