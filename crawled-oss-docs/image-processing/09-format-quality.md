# Image Format Conversion and Quality

Source: https://help.aliyun.com/zh/oss/user-guide/img-overview

## Format Conversion (format)

Convert images between different formats.

### URL Format
```
?x-oss-process=image/format,<format>
```

### Supported Formats

| Format | Parameter | Notes |
|---|---|---|
| JPEG | `jpg` or `jpeg` | Best for photos, lossy compression |
| PNG | `png` | Supports transparency, lossless |
| WebP | `webp` | Modern format, better compression |
| BMP | `bmp` | Uncompressed, large file size |
| GIF | `gif` | Supports animation |
| TIFF | `tiff` | High quality, large file size |
| AVIF | `avif` | Modern format, excellent compression |

### Examples
```
# Convert to WebP (30-50% smaller than JPEG)
?x-oss-process=image/format,webp

# Convert to PNG (for transparency)
?x-oss-process=image/format,png

# Convert to AVIF (best compression)
?x-oss-process=image/format,avif
```

### Auto-Format (Accept Header)

For web applications, you can let OSS automatically choose the best format based on the browser's Accept header:
```
?x-oss-process=image/format,webp
```
Browsers that support WebP will receive WebP; others will receive the original format.

## Quality (quality)

Adjust JPEG/WebP compression quality.

### URL Format
```
?x-oss-process=image/quality,q_<value>
```

### Parameters

| Parameter | Description | Value Range |
|---|---|---|
| `q_<value>` | Absolute quality | 1-100 |
| `Q_<value>` | Relative quality (% of original) | 1-100 |

### Difference Between q and Q
- `q_80`: Sets output quality to 80 regardless of original quality
- `Q_80`: Sets output quality to 80% of the original quality. If original is 90, output is 72.

### Examples
```
# Set absolute quality to 80
?x-oss-process=image/quality,q_80

# Set relative quality to 90% of original
?x-oss-process=image/quality,Q_90

# Convert to WebP with quality 75
?x-oss-process=image/format,webp/quality,q_75
```

## Interlace / Progressive JPEG (interlace)

Enable progressive JPEG encoding for better perceived loading speed.

### URL Format
```
?x-oss-process=image/interlace,<0|1>
```

| Value | Description |
|---|---|
| `0` | Baseline JPEG (default) |
| `1` | Progressive JPEG |

Progressive JPEGs load in multiple passes, showing a blurry full image first, then progressively sharpening. This improves perceived loading speed for web pages.

### Example
```
# Convert to progressive JPEG
?x-oss-process=image/interlace,1

# Progressive JPEG with quality 85
?x-oss-process=image/interlace,1/quality,q_85
```

## Image Info (info)

Retrieve image metadata including dimensions, format, and EXIF data.

### URL Format
```
?x-oss-process=image/info
```

### Response (JSON)
```json
{
    "FileSize": {"value": "1234567"},
    "Format": {"value": "jpg"},
    "ImageHeight": {"value": "1080"},
    "ImageWidth": {"value": "1920"},
    "Orientation": {"value": "1"},
    "ResolutionUnit": {"value": "2"},
    "XResolution": {"value": "72/1"},
    "YResolution": {"value": "72/1"}
}
```

## Average Hue (average-hue)

Get the average color of the image. Useful for generating placeholder backgrounds.

### URL Format
```
?x-oss-process=image/average-hue
```

### Response (JSON)
```json
{
    "RGB": "0x5C7A3E"
}
```

## Optimization Recommendations

### For Web Images
```
# Optimal web thumbnail: resize + WebP + quality 80 + progressive
?x-oss-process=image/resize,w_800/format,webp/quality,q_80/interlace,1
```

### For Mobile Images
```
# Mobile-optimized: smaller size + WebP + lower quality
?x-oss-process=image/resize,w_400/format,webp/quality,q_70
```

### File Size Reduction Comparison

| Strategy | Typical File Size Reduction |
|---|---|
| JPEG quality 80 | ~30% smaller than quality 100 |
| Convert to WebP | ~30-50% smaller than JPEG |
| Convert to AVIF | ~50% smaller than JPEG |
| Resize to 50% | ~75% smaller |
| Combined (resize + WebP + q_75) | ~85-90% smaller |
