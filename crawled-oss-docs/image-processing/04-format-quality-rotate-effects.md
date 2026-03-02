# Image Processing (IMG) - Format, Quality, Rotate, Flip, Circle, Rounded Corners

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/

## Overview

OSS Image Processing (IMG) provides real-time image processing via URL parameters. All operations use the `x-oss-process=image/` prefix.

### Chaining Operations

Multiple operations can be chained with `/`:
```
?x-oss-process=image/resize,w_300/quality,q_80/format,png/rounded-corners,r_20
```

---

## Format Conversion

Action: `format`

Convert images between formats.

### Supported Formats

| Format | Description |
|--------|-------------|
| jpg | JPEG format |
| png | PNG format |
| bmp | BMP format |
| gif | GIF format |
| webp | WebP format |
| tiff | TIFF format |
| avif | AVIF format |
| heic | HEIC format |

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| format | Target format | jpg, png, bmp, gif, webp, tiff, avif |
| interlace | Progressive display (JPEG only) | 0 (default, non-interlaced), 1 (interlaced/progressive) |

### Examples

```
# Convert to PNG
?x-oss-process=image/format,png

# Convert to WebP
?x-oss-process=image/format,webp

# Convert to progressive JPEG
?x-oss-process=image/interlace,1

# Resize and convert to WebP
?x-oss-process=image/resize,w_300/format,webp
```

### Notes

- When converting GIF to other formats, only the first frame is used
- WebP and AVIF offer better compression than JPEG/PNG
- Use WebP for web delivery to reduce bandwidth

---

## Quality Adjustment

Action: `quality`

Control compression quality for JPEG and WebP images.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| q | Relative quality (percentage of original) | [1,100] |
| Q | Absolute quality (fixed quality level) | [1,100] |

### Examples

```
# Relative quality 80%
?x-oss-process=image/quality,q_80

# Absolute quality 90
?x-oss-process=image/quality,Q_90

# Resize, set quality, and convert format
?x-oss-process=image/resize,w_800/quality,q_85/format,webp
```

### Notes

- `q` (relative): Applied as a percentage of the original quality. If source is 80% and you set q_80, result is 64%
- `Q` (absolute): Sets an absolute quality level regardless of source quality
- Lower values = smaller file size but reduced image quality
- Only affects lossy formats (JPEG, WebP)

---

## Rotate

Action: `rotate`

Rotate images clockwise by specified degrees.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| rotate | Clockwise rotation angle | [0,360] |

### Examples

```
# Rotate 90 degrees clockwise
?x-oss-process=image/rotate,90

# Rotate 180 degrees
?x-oss-process=image/rotate,180

# Rotate 270 degrees (90 counter-clockwise)
?x-oss-process=image/rotate,270
```

### Notes

- Rotation may increase the dimensions of the output image
- The rotated image canvas is expanded to fit the rotated content

---

## Auto-Orient

Action: `auto-orient`

Automatically rotate images based on EXIF orientation data.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| auto-orient | Auto-rotate based on EXIF | 0 (do not rotate), 1 (auto-rotate, default) |

### Examples

```
# Auto-orient based on EXIF
?x-oss-process=image/auto-orient,1

# Disable auto-orient
?x-oss-process=image/auto-orient,0
```

### Notes

- By default, OSS auto-orients images based on EXIF data
- Useful for photos taken on mobile devices with varying orientations
- Set to 0 if you want to preserve the original EXIF orientation

---

## Flip Images

Action: `flip` (available in newer versions)

Flip images horizontally or vertically.

### Examples

```
# Horizontal flip
?x-oss-process=image/flip,horizontal

# Vertical flip
?x-oss-process=image/flip,vertical
```

---

## Circle Crop

Action: `circle`

Crop an image into a circular shape.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| r | Radius of the circle (pixels) | [1, min(width/2, height/2)] |

### Examples

```
# Circle crop with radius 100
?x-oss-process=image/circle,r_100

# Circle crop and convert to PNG (for transparency)
?x-oss-process=image/circle,r_100/format,png

# Resize then circle crop
?x-oss-process=image/resize,w_200,h_200,m_fill/circle,r_100/format,png
```

### Notes

- If the radius exceeds the shorter edge / 2, the circle is reduced to fit
- Output format should be **PNG** to support transparency (areas outside the circle)
- If output is JPEG, the background outside the circle will be white

---

## Rounded Corners

Action: `rounded-corners`

Apply rounded corners to an image.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| r | Corner radius (pixels) | [1, min(width/2, height/2)] |

### Examples

```
# Rounded corners with radius 30
?x-oss-process=image/rounded-corners,r_30

# Rounded corners with PNG format (for transparency)
?x-oss-process=image/rounded-corners,r_30/format,png

# Resize and add rounded corners
?x-oss-process=image/resize,w_300,h_200,m_fill/rounded-corners,r_20/format,png
```

### Notes

- Output format should be **PNG** for transparency support
- If radius exceeds the shorter edge / 2, it is reduced to fit

---

## Indexed Slice

Action: `indexcrop`

Divide the image into equal parts and return a specific section.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| x | Width of each slice | Positive integer |
| y | Height of each slice | Positive integer |
| i | Index of the slice to return (0-based) | Non-negative integer |

### Examples

```
# Divide horizontally into 100px slices, return the 3rd slice
?x-oss-process=image/indexcrop,x_100,i_2
```

---

## Brightness

Action: `bright`

Adjust the brightness of an image.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| bright | Brightness level | [-100,100], 0 = no change |

### Examples

```
# Increase brightness
?x-oss-process=image/bright,50

# Decrease brightness
?x-oss-process=image/bright,-30
```

---

## Contrast

Action: `contrast`

Adjust the contrast of an image.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| contrast | Contrast level | [-100,100], 0 = no change |

### Examples

```
# Increase contrast
?x-oss-process=image/contrast,50

# Decrease contrast
?x-oss-process=image/contrast,-30
```

---

## Sharpen

Action: `sharpen`

Sharpen an image.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| sharpen | Sharpen value | [50,399], recommended 100 |

### Examples

```
# Apply sharpening
?x-oss-process=image/sharpen,100
```

---

## Blur

Action: `blur`

Apply Gaussian blur to an image.

### Parameters

| Parameter | Description | Value |
|-----------|-------------|-------|
| r | Blur radius | [1,50] |
| s | Standard deviation | [1,50] |

### Examples

```
# Apply blur
?x-oss-process=image/blur,r_3,s_2

# Heavy blur
?x-oss-process=image/blur,r_10,s_10
```

---

## Image Info

Action: `info`

Get image metadata information (returned as JSON).

### Examples

```
# Get image information
?x-oss-process=image/info
```

### Response Format (JSON)

```json
{
  "FileSize": {"value": "1024"},
  "Format": {"value": "jpg"},
  "ImageHeight": {"value": "800"},
  "ImageWidth": {"value": "600"},
  "ResolutionUnit": {"value": "1"},
  "XResolution": {"value": "72/1"},
  "YResolution": {"value": "72/1"}
}
```

---

## Average Hue

Action: `average-hue`

Calculate the average color of an image (returned as hex).

### Examples

```
# Get average color
?x-oss-process=image/average-hue
```

### Response Format

```json
{
  "RGB": "0x5c783b"
}
```

---

## Image Style

You can create named styles that combine multiple processing parameters for reuse.

### Creating a Style

Styles are created in the OSS Console under Bucket > Data Processing > Image Processing > Image Styles.

### Using a Style

```
?x-oss-process=style/style-name
```

### Example

If you create a style named "thumbnail" with parameters `image/resize,w_200,h_200,m_fill/quality,q_80/format,webp`:

```
https://bucket.oss-region.aliyuncs.com/photo.jpg?x-oss-process=style/thumbnail
```

---

## Pipeline Processing

Chain multiple operations in sequence:

```
?x-oss-process=image/resize,w_800/crop,w_500,h_300,g_center/quality,q_85/watermark,text_SGVsbG8,size_20,g_se/format,webp
```

This pipeline:
1. Resizes to 800px width
2. Crops 500x300 from center
3. Sets quality to 85%
4. Adds "Hello" text watermark
5. Converts to WebP

---

## Persistent Image Processing

To save processed images permanently (not just serve on-the-fly):

### Using ossutil

```bash
ossutil cp oss://bucket/source.jpg oss://bucket/processed.jpg \
  --meta x-oss-process:image/resize,w_300/format,webp
```

### Using SDK

Use the `process` parameter in PutObject or CopyObject operations to save processed results.

---

## Limits Summary

| Item | Limit |
|------|-------|
| Source image format | JPG, PNG, BMP, GIF, WebP, TIFF, HEIC |
| Source image size | Max 20 MB (adjustable) |
| Source image dimensions | Max 30,000 px per side, max 250M total pixels |
| Output dimensions | Max 16,384 px per side, max 16,777,216 total pixels |
| Watermark images per image | Max 3 |
| Style name length | Max 50 characters |
| Operations per pipeline | No hard limit, but complex pipelines may timeout |
