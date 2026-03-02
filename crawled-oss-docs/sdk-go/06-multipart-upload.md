# Go SDK - Multipart Upload

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/go-multipart-upload

## V1 SDK - Basic Multipart Upload

```go
bucket, err := client.Bucket("my-bucket")

// Step 1: Initiate
initResult, err := bucket.InitiateMultipartUpload("large-file.zip")
uploadId := initResult.UploadID

// Step 2: Upload parts
var parts []oss.UploadPart
partSize := int64(5 * 1024 * 1024) // 5MB
file, _ := os.Open("/path/to/large-file.zip")
defer file.Close()
stat, _ := file.Stat()
fileSize := stat.Size()

partNumber := 1
for offset := int64(0); offset < fileSize; offset += partSize {
    size := partSize
    if offset+size > fileSize {
        size = fileSize - offset
    }

    part, err := bucket.UploadPart(initResult, file, size, partNumber)
    if err != nil {
        log.Fatal(err)
    }
    parts = append(parts, part)
    partNumber++
}

// Step 3: Complete
_, err = bucket.CompleteMultipartUpload(initResult, parts)
```

## V1 SDK - Resumable Upload

```go
err = bucket.UploadFile("large-file.zip", "/path/to/file.zip",
    100*1024*1024,                          // 100MB per part
    oss.Routines(5),                        // 5 concurrent goroutines
    oss.Checkpoint(true, "/tmp/checkpoint")) // Enable checkpoint for resume
```

## V2 SDK - Multipart Upload

```go
package main

import (
    "context"
    "fmt"
    "io"
    "log"
    "os"
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

    bucket := "my-bucket"
    key := "large-files/video.mp4"
    localFile := "/path/to/large-video.mp4"

    // Step 1: Initiate
    initResult, err := client.InitiateMultipartUpload(ctx, &oss.InitiateMultipartUploadRequest{
        Bucket:      oss.Ptr(bucket),
        Key:         oss.Ptr(key),
        ContentType: oss.Ptr("video/mp4"),
    })
    if err != nil {
        log.Fatalf("Failed to initiate: %v", err)
    }
    uploadId := initResult.UploadId

    // Step 2: Upload parts
    file, _ := os.Open(localFile)
    defer file.Close()
    partSize := int64(5 * 1024 * 1024) // 5MB
    parts := make([]oss.UploadPart, 0)
    partNumber := int32(1)
    buffer := make([]byte, partSize)

    for {
        n, err := io.ReadFull(file, buffer)
        if err != nil && err != io.EOF && err != io.ErrUnexpectedEOF {
            log.Fatal(err)
        }
        if n == 0 {
            break
        }
        partResult, err := client.UploadPart(ctx, &oss.UploadPartRequest{
            Bucket:     oss.Ptr(bucket),
            Key:        oss.Ptr(key),
            UploadId:   uploadId,
            PartNumber: partNumber,
            Body:       io.NopCloser(strings.NewReader(string(buffer[:n]))),
        })
        if err != nil {
            client.AbortMultipartUpload(ctx, &oss.AbortMultipartUploadRequest{
                Bucket: oss.Ptr(bucket), Key: oss.Ptr(key), UploadId: uploadId,
            })
            log.Fatalf("Failed to upload part %d: %v", partNumber, err)
        }
        parts = append(parts, oss.UploadPart{PartNumber: partNumber, ETag: partResult.ETag})
        partNumber++
        if err == io.EOF || err == io.ErrUnexpectedEOF {
            break
        }
    }

    // Step 3: Complete
    completeResult, err := client.CompleteMultipartUpload(ctx, &oss.CompleteMultipartUploadRequest{
        Bucket:   oss.Ptr(bucket),
        Key:      oss.Ptr(key),
        UploadId: uploadId,
        CompleteMultipartUpload: &oss.CompleteMultipartUpload{Parts: parts},
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Upload completed! ETag: %s\n", oss.ToString(completeResult.ETag))
}
```

## V2 SDK - High-Level Uploader (Recommended)

Automatic multipart upload with parallel uploading, progress tracking, and resume support:

```go
uploader := oss.NewUploader(client, func(uo *oss.UploaderOptions) {
    uo.ParallelNum = 5                        // 5 parallel uploads
    uo.PartSize = 10 * 1024 * 1024            // 10MB per part
    uo.LeavePartsOnError = false              // Clean up on error
    uo.EnableCheckpoint = true                // Enable resume
    uo.CheckpointDir = "/tmp/oss-checkpoints" // Checkpoint directory
})

// Progress callback
progressFn := func(increment, transferred, total int64) {
    percentage := float64(transferred) * 100 / float64(total)
    fmt.Printf("\rUploading: %.2f%% (%d/%d bytes)", percentage, transferred, total)
}

result, err := uploader.UploadFile(ctx, &oss.PutObjectRequest{
    Bucket:      oss.Ptr("my-bucket"),
    Key:         oss.Ptr("uploads/large-file.zip"),
    ContentType: oss.Ptr("application/zip"),
    Metadata: map[string]string{
        "uploader": "oss-go-sdk-v2",
    },
    ProgressFn: progressFn,
}, "/path/to/large-file.zip")

if err != nil {
    log.Fatalf("Upload failed: %v", err)
}
fmt.Printf("\nETag: %s, VersionId: %s, CRC64: %s\n",
    oss.ToString(result.ETag),
    oss.ToString(result.VersionId),
    oss.ToString(result.HashCRC64))
```

## Abort Multipart Upload

```go
// V1
bucket.AbortMultipartUpload(initResult)

// V2
client.AbortMultipartUpload(ctx, &oss.AbortMultipartUploadRequest{
    Bucket:   oss.Ptr(bucket),
    Key:      oss.Ptr(key),
    UploadId: uploadId,
})
```
