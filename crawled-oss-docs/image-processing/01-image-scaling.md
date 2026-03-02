# Image Processing (IMG) - Image Scaling

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/resize-images-4

You can scale an image up or down by adding image scaling parameters to a GetObject request.

## Scenarios

- **Web design**: Adapt images to different screen sizes and resolutions
- **Social media**: Process user-uploaded images into standard preview dimensions
- **Image recognition and analysis**: Scale images to improve processing efficiency

## Limits

### Source Image Limits

| Item | Description |
|------|-------------|
| Image format | JPG, PNG, BMP, GIF, WebP, TIFF, or HEIC |
| Image size | Cannot exceed 20 MB (adjustable via Quota Center) |
| Image dimensions | Width or height cannot exceed 30,000 px. Total pixels cannot exceed 250 million |

> For animated images (e.g., GIF), total pixels = width x height x number of frames.

### Scaled Image Limits

| Item | Description |
|------|-------------|
| Image scaling | Width or height cannot exceed 16,384 px. Total pixels cannot exceed 16,777,216 |

## Usage

Add `?x-oss-process=image/resize,parame_value` to the image URL.

### Public-read images

Append parameters directly to the URL:
```
https://bucket.oss-region.aliyuncs.com/example.jpg?x-oss-process=image/resize,p_50
```

### Private images

Call an SDK with signature information or use the API.

## Parameters

### Proportional Scaling

| Parameter | Description | Value |
|-----------|-------------|-------|
| p | Scales by percentage | [1,1000]. <100 = scale down, >100 = scale up |

> Not supported for animated images.

### Scaling by Specified Dimensions

| Parameter | Description | Value |
|-----------|-------------|-------|
| w | Width of scaled image | [1,16384] |
| h | Height of scaled image | [1,16384] |
| m | Scaling mode | lfit, mfit, fill, pad, fixed |
| l | Longer edge of scaled image | [1,16384] |
| s | Shorter edge of scaled image | [1,16384] |
| limit | Whether to scale up if target > source | 1 (default, no upscale), 0 (allow upscale) |
| color | Padding color for pad mode | RGB hex (e.g., 000000, FFFFFF) |

### Scaling Modes

| Mode | Description |
|------|-------------|
| **lfit** (default) | Proportionally scales to fit within specified width and height |
| **mfit** | Proportionally scales to cover the specified width and height |
| **fill** | Proportionally scales to cover, then crops from center |
| **pad** | Proportionally scales to fit, then pads with color |
| **fixed** | Forces exact dimensions (may distort) |

### Scaling Mode Calculation Example

Source: 200 px x 100 px, Target: 150 px x 80 px

| Mode | Result |
|------|--------|
| lfit | 150 px x 75 px |
| mfit | 160 px x 80 px |
| fill | 150 px x 80 px |
| pad | 150 px x 80 px |
| fixed | 150 px x 80 px |

## Examples

### Scale down by percentage
```
?x-oss-process=image/resize,p_50
```
2500x1875 -> 1250x938

### Scale up by percentage
```
?x-oss-process=image/resize,p_120
```
2500x1875 -> 3000x2250

### Fixed width, adaptive height
```
?x-oss-process=image/resize,w_200
```
2500x1875 -> 200x150

### Scale up with limit_0
```
?x-oss-process=image/resize,w_3000,limit_0
```
2500x1875 -> 3000x2250

### Fixed height, adaptive width
```
?x-oss-process=image/resize,h_100
```
2500x1875 -> 133x100

### Fixed longer edge
```
?x-oss-process=image/resize,l_200
```
2500x1875 -> 200x150

### Fixed shorter edge
```
?x-oss-process=image/resize,s_200
```
2500x1875 -> 267x200

### Pad to fixed dimensions
```
?x-oss-process=image/resize,m_pad,w_100,h_100
```
2500x1875 -> 100x100 (with white padding)

### Pad with custom color
```
?x-oss-process=image/resize,m_pad,w_100,h_100,color_FF0000
```
2500x1875 -> 100x100 (with red padding)

### Fill (scale + center crop)
```
?x-oss-process=image/resize,m_fill,w_100,h_100
```
2500x1875 -> 100x100

### Force fixed dimensions
```
?x-oss-process=image/resize,m_fixed,w_100,h_100
```
2500x1875 -> 100x100 (may distort)

## Billing

| API | Billable Item | Description |
|-----|---------------|-------------|
| GetObject | GET requests | Charged based on number of successful requests |
| | Outbound traffic | Charged when using public or acceleration endpoints |
| | IA data retrieval | Charged for IA storage class objects |
| | Archive data retrieval | Charged for Archive objects with real-time access |
| | Transfer acceleration | Charged when using acceleration endpoints |

## API Usage

```http
GET /oss.jpg?x-oss-process=image/resize,p_50 HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 28 Oct 2022 06:40:10 GMT
Authorization: SignatureValue
```
