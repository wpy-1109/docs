# Image Processing (IMG) - Add Watermarks

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/add-watermarks

You can add watermarks to images stored on OSS to prevent unauthorized data replication and use.

## Scenarios

- **Copyright protection**: Identify copyrighted images
- **Brand promotion**: Enhance brand visibility with logos/names
- **Tamper prevention**: Increase difficulty of tampering documents
- **Image plagiarism prevention**: Show images are copyrighted
- **Legal compliance**: Fulfill legal requirements

## Usage Notes

- Only images stored in the current bucket can be used as watermarks
- Watermark images must be JPG, PNG, BMP, WebP, or TIFF format
- Maximum 3 different image watermarks per image
- Traditional Chinese characters cannot be used as text watermarks

## Parameters

Action: `watermark`

### Basic Parameters

| Parameter | Required | Description | Value |
|-----------|----------|-------------|-------|
| t | No | Opacity of watermark | [0,100], default: 100 (opaque) |
| g | No | Position on image | nw, north, ne, west, center, east, sw, south, se (default: se) |
| x | No | Horizontal offset (pixels) | [0,4096], default: 10 |
| y | No | Vertical offset (pixels) | [0,4096], default: 10 |
| voffset | No | Vertical offset from middle line | [-1000,1000], default: 0 |
| fill | No | Tile watermarks across image | 0 (default, no tiling), 1 (tile) |
| padx | No | Horizontal spacing when tiling | [0,4096], default: 0 |
| pady | No | Vertical spacing when tiling | [0,4096], default: 0 |

### Position Values

```
nw -------- north -------- ne
|                           |
west ------ center ------ east
|                           |
sw -------- south -------- se
```

### Image Watermark Parameters

| Parameter | Required | Description | Value |
|-----------|----------|-------------|-------|
| image | Yes | Base64-encoded object name of watermark image | URL-safe Base64 string |
| P | No | Size of watermark relative to original (%) | [1,100] |

### Text Watermark Parameters

| Parameter | Required | Description | Value |
|-----------|----------|-------------|-------|
| text | Yes | Base64-encoded text content | Max 64 chars before encoding |
| type | No | Base64-encoded font name | See font table below, default: wqy-zenhei |
| color | No | Text color (RGB hex) | e.g., 000000 (black), FFFFFF (white) |
| size | No | Text size (pixels) | (0,1000], default: 40 |
| shadow | No | Shadow opacity | [0,100], default: 0 |
| rotate | No | Clockwise rotation degrees | [0,360], default: 0 |

### Available Fonts

| Font | Value | Base64 Encoding |
|------|-------|-----------------|
| WenQuanYi Zen Hei | wqy-zenhei | d3F5LXplbmhlaQ |
| WenQuanYi Micro Hei | wqy-microhei | d3F5LW1pY3JvaGVp |
| Fangzheng Shusong | fangzhengshusong | ZmFuZ3poZW5nc2h1c29uZw |
| Fangzheng Kaiti | fangzhengkaiti | ZmFuZ3poZW5na2FpdGk |
| Fangzheng Heiti | fangzhengheiti | ZmFuZ3poZW5naGVpdGk |
| Fangzheng Fangsong | fangzhengfangsong | ZmFuZ3poZW5nZmFuZ3Nvbmc |
| DroidSansFallback | droidsansfallback | ZHJvaWRzYW5zZmFsbGJhY2s |

### Text-and-Image Watermark Parameters

| Parameter | Required | Description | Value |
|-----------|----------|-------------|-------|
| order | No | Order of text and image | 0 (default, image on top), 1 (text on top) |
| align | No | Alignment | 0 (top), 1 (center), 2 (default, bottom) |
| interval | No | Spacing between text and image (pixels) | [0,1000], default: 0 |

## Base64 Encoding for Watermark Parameters

1. Encode watermark parameters in Base64
2. Replace `+` with `-`
3. Replace `/` with `_`
4. Remove trailing `=` signs

## Examples

### Text Watermark

Add "Hello World" text:
```
?x-oss-process=image/watermark,text_SGVsbG8gV29ybGQ
```

Full text watermark with styling:
```
?x-oss-process=image/resize,w_300,h_300/watermark,type_d3F5LXplbmhlaQ,size_30,text_SGVsbG8gV29ybGQ,color_FFFFFF,shadow_50,t_100,g_se,x_10,y_10
```

### Image Watermark

Add panda.png as watermark:
```
?x-oss-process=image/watermark,image_cGFuZGEucG5n
```

Image watermark with image in subdirectory (image/panda.png -> aW1hZ2UvcGFuZGEucG5n):
```
?x-oss-process=image/watermark,image_aW1hZ2UvcGFuZGEucG5n
```

With preprocessing:
```
?x-oss-process=image/resize,w_300/watermark,image_cGFuZGEucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMzA,t_90,g_se,x_10,y_10
```

### Multiple Watermarks

```
?x-oss-process=image/watermark,image_cGFuZGEucG5n/watermark,image_VHVsaXBzLmpwZw,g_west,x_10,y_10
```

### Text + Image Watermark

```
?x-oss-process=image/watermark,image_cGFuZGEucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMzA,text_SGVsbG8gV29ybGQ
```

### Vertical Text Arrangement

Split into multiple watermark actions:
```
?x-oss-process=image/watermark,text_SGVsbG8gV29ybGQ/watermark,text_SGVsbG8gV29ybGQy,y_60
```

## FAQ

**Q: Can I use online or local images as watermarks?**
A: No, watermark images must be stored in the same bucket. Upload them first.

**Q: Text watermark "font content is too large" error?**
A: Maximum 64 English characters (each Chinese character counts as 3). Shorten the text.

**Q: How to add watermark to private objects?**
A: Add IMG parameters to the signature, not to the end of a signed URL.

**Q: Can I set a background color for image watermarks?**
A: No, background colors for image watermarks are not supported.

**Q: How many watermarks can I add?**
A: Up to 3 watermarks per image. Submit a ticket for more.

**Q: Does OSS support dynamic watermark sizing?**
A: No, implement size detection logic on your client/server side.
