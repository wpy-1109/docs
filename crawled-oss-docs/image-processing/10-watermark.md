# Image Watermark - Text and Image

Source: https://help.aliyun.com/zh/oss/user-guide/img-overview

## Overview

OSS supports adding both text and image watermarks to images. Watermarks can be positioned at various locations and customized with size, transparency, and other parameters.

## Image Watermark

Add an image (logo, badge) as a watermark overlay.

### URL Format
```
?x-oss-process=image/watermark,image_<Base64EncodedURL>,<params>
```

### Parameters

| Parameter | Description | Value |
|---|---|---|
| `image_<value>` | Base64-encoded URL of watermark image | Must be in same Bucket or accessible URL |
| `t_<value>` | Transparency | 0-100 (default: 100, fully opaque) |
| `g_<value>` | Position (gravity) | nw, north, ne, west, center, east, sw, south, se |
| `x_<value>` | Horizontal margin from edge | Pixels (default: 10) |
| `y_<value>` | Vertical margin from edge | Pixels (default: 10) |
| `voffset_<value>` | Vertical offset (from center) | Pixels (can be negative) |

### Watermark Image Requirements
- Must be stored in the same Bucket or accessible via URL
- The image URL must be Base64-encoded (URL-safe Base64)
- Recommended: PNG with transparency for best results

### Base64 Encoding
```python
import base64
watermark_url = "logo.png"  # Object key in same bucket
encoded = base64.urlsafe_b64encode(watermark_url.encode()).decode().rstrip('=')
# Result: bG9nby5wbmc
```

### Examples
```
# Add logo at bottom-right corner
?x-oss-process=image/watermark,image_bG9nby5wbmc,g_se,x_10,y_10

# Add logo at center with 50% transparency
?x-oss-process=image/watermark,image_bG9nby5wbmc,g_center,t_50

# Add logo at top-left
?x-oss-process=image/watermark,image_bG9nby5wbmc,g_nw,x_20,y_20
```

## Text Watermark

Add text as a watermark overlay.

### URL Format
```
?x-oss-process=image/watermark,text_<Base64Text>,<params>
```

### Parameters

| Parameter | Description | Value |
|---|---|---|
| `text_<value>` | Base64-encoded watermark text | UTF-8 text, URL-safe Base64 |
| `type_<value>` | Base64-encoded font name | See font list |
| `size_<value>` | Font size | 1-1000 (default: 40) |
| `color_<value>` | Font color | 6-digit hex without # (default: 000000) |
| `t_<value>` | Transparency | 0-100 (default: 100) |
| `g_<value>` | Position (gravity) | nw, north, ne, west, center, east, sw, south, se |
| `x_<value>` | Horizontal margin | Pixels (default: 10) |
| `y_<value>` | Vertical margin | Pixels (default: 10) |
| `shadow_<value>` | Text shadow transparency | 0-100 |
| `rotate_<value>` | Text rotation angle | 0-360 |
| `fill_<value>` | Tile fill (repeat watermark) | 0 or 1 |

### Supported Fonts

| Font | Base64 Value | Description |
|---|---|---|
| Wen Quan Yi Zheng Hei | `d3F5LXplbmhlaQ` | Chinese (simplified) |
| Wen Quan Yi Micro Hei | `d3F5LW1pY3JvaGVp` | Chinese (simplified) |
| Fang Song | `ZmFuZ3Nvbmc` | Chinese (simplified) |
| Hei Ti | `aGVpdGk` | Chinese (simplified) |
| Kai Ti | `a2FpdGk` | Chinese (simplified) |
| Song Ti | `c29uZ3Rp` | Chinese (simplified) |
| Arial | `YXJpYWw` | English |
| Times New Roman | `dGltZXMgbmV3IHJvbWFu` | English |
| Courier New | `Y291cmllciBuZXc` | English |

### Text Encoding
```python
import base64
text = "Sample Watermark"
encoded = base64.urlsafe_b64encode(text.encode()).decode().rstrip('=')
# Result: U2FtcGxlIFdhdGVybWFyaw
```

### Examples
```
# Simple text watermark at bottom-right
?x-oss-process=image/watermark,text_U2FtcGxlIFdhdGVybWFyaw,g_se,x_10,y_10

# White text, large font, with shadow
?x-oss-process=image/watermark,text_U2FtcGxlIFdhdGVybWFyaw,color_FFFFFF,size_60,shadow_50,g_se

# Red text at center with transparency
?x-oss-process=image/watermark,text_U2FtcGxlIFdhdGVybWFyaw,color_FF0000,t_50,g_center,size_80

# Tiled watermark (repeating across image)
?x-oss-process=image/watermark,text_Q29weXJpZ2h0,fill_1,size_20,color_CCCCCC,t_30
```

## Mixed Watermark (Image + Text)

You can combine image and text watermarks in a single request by chaining operations:

```
# Image watermark at bottom-right + text watermark at bottom-left
?x-oss-process=image/watermark,image_bG9nby5wbmc,g_se,x_10,y_10/watermark,text_Q29weXJpZ2h0,g_sw,x_10,y_10,size_16,color_FFFFFF
```

## Multiple Watermarks

You can add multiple watermarks by chaining watermark operations:
```
?x-oss-process=image/watermark,text_V2F0ZXJtYXJrMQ,g_nw,x_10,y_10/watermark,text_V2F0ZXJtYXJrMg,g_se,x_10,y_10
```

## Position Reference

```
┌──────────────────────────────────────┐
│ nw          north          ne        │
│                                      │
│                                      │
│ west        center         east      │
│                                      │
│                                      │
│ sw          south          se        │
└──────────────────────────────────────┘
```

The `x_` and `y_` parameters specify the margin from the edge indicated by the gravity position.
