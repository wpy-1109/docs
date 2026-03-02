# Image Processing Overview

Source: https://help.aliyun.com/zh/oss/user-guide/data-processing-overview

## Overview

OSS Image Processing (IMG) is a built-in service that allows you to process images stored in OSS on-the-fly by appending processing parameters to the image URL. Processing is triggered via the `x-oss-process=image/` parameter.

## URL Format

```
https://<BucketName>.<Endpoint>/<ObjectName>?x-oss-process=image/<action>,<params>
```

**Example**:
```
https://my-bucket.oss-cn-hangzhou.aliyuncs.com/photo.jpg?x-oss-process=image/resize,w_300,h_200
```

## Supported Operations

| Operation | Description | Parameter Prefix |
|---|---|---|
| resize | Scale/resize images | `resize,` |
| crop | Crop to specific area | `crop,` |
| indexcrop | Split into equal tiles | `indexcrop,` |
| rounded-corners | Add rounded corners | `rounded-corners,` |
| circle | Circular crop | `circle,` |
| rotate | Rotate by degrees | `rotate,` |
| auto-orient | Auto-orient by EXIF | `auto-orient,` |
| blur | Apply Gaussian blur | `blur,` |
| bright | Adjust brightness | `bright,` |
| contrast | Adjust contrast | `contrast,` |
| sharpen | Sharpen image | `sharpen,` |
| format | Convert format | `format,` |
| quality | Set JPEG quality | `quality,` |
| watermark | Add text/image watermark | `watermark,` |
| interlace | Progressive JPEG | `interlace,` |
| average-hue | Get average color | `average-hue` |
| info | Get image info (EXIF) | `info` |

## Pipeline Processing

Chain multiple operations using `/` separator:
```
?x-oss-process=image/resize,w_300/crop,w_200,h_200,g_center/watermark,text_SGVsbG8=
```

Processing is applied left-to-right.

## Limits

| Limit | Value |
|---|---|
| Maximum source image size | 20 MB |
| Maximum source image dimensions | 30,000 x 30,000 pixels |
| Maximum output dimensions | 16,384 x 16,384 pixels |
| Maximum pipeline operations | 20 per request |
| Supported source formats | JPEG, PNG, BMP, GIF, WebP, TIFF, AVIF |
| Supported output formats | JPEG, PNG, BMP, GIF, WebP, AVIF |

## Image Styles

You can create named styles that encapsulate multiple processing parameters:
1. Navigate to **Bucket > Data Processing > Image Processing**
2. Create a style with a name (e.g., `thumbnail`)
3. Configure processing parameters
4. Access using: `?x-oss-process=style/thumbnail`

### Style Separator

You can configure a custom separator (default: `-`) to use styles in the URL path:
```
https://bucket.endpoint.com/photo.jpg-thumbnail
```

## Original Image Protection

When enabled, the original image cannot be accessed directly. Only processed versions (via `x-oss-process` or styles) can be accessed.

Configuration:
1. Navigate to **Bucket > Data Processing > Image Processing > Access Settings**
2. Enable **Original Image Protection**
3. Specify protected suffixes (e.g., `.jpg`, `.png`)

## Persistent Processing

By default, image processing is on-the-fly (processed images are not stored). For persistent processing:
- Use `x-oss-process` with `sys/saveas` to save the processed result:
```
?x-oss-process=image/resize,w_300|sys/saveas,o_<Base64EncodedObjectKey>,b_<Base64EncodedBucketName>
```

## Integration with CDN

When using CDN with OSS image processing:
- Set CDN parameter handling to **Retain All Parameters** or retain `x-oss-process`
- CDN caches processed results (each unique `x-oss-process` URL is a separate cache entry)
- Consider using styles for cleaner URLs and better cache utilization
