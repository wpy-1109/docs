# Image Styles, Persistent Processing, and Original Image Protection

Source: https://help.aliyun.com/zh/oss/user-guide/img-overview

## Image Styles

Image styles allow you to create named presets for frequently used processing parameter combinations.

### Creating Styles

1. Navigate to **Bucket > Data Processing > Image Processing**
2. Click **Create Style**
3. Enter a style name (e.g., `thumbnail`, `avatar`, `preview`)
4. Configure processing parameters via GUI or code
5. Save the style

### Using Styles

**Via style parameter**:
```
?x-oss-process=style/<style-name>
```

**Via style separator** (configured per Bucket):
```
https://bucket.endpoint.com/photo.jpg-<style-name>
```

Default separator: `-` (dash). Can be customized to `!`, `/`, or `_`.

### Style Examples

**Thumbnail style** (resize + quality):
```
image/resize,m_fill,w_200,h_200/quality,q_80/format,webp
```

**Avatar style** (circle crop + resize):
```
image/resize,m_fill,w_100,h_100/circle,r_50/format,png
```

**Preview style** (resize + watermark):
```
image/resize,w_800/watermark,text_UHJldmlldw,g_se,size_16,color_CCCCCC
```

### Style Limits
- Maximum 50 styles per Bucket
- Style name: 1-64 characters, alphanumeric and hyphens only

## Persistent Processing (Save As)

By default, image processing is on-the-fly. Use persistent processing to save results as new objects.

### URL Format
```
?x-oss-process=image/<operations>|sys/saveas,o_<Base64ObjectKey>,b_<Base64BucketName>
```

### Parameters

| Parameter | Description |
|---|---|
| `o_<value>` | Base64-encoded target object key (URL-safe Base64) |
| `b_<value>` | Base64-encoded target Bucket name (URL-safe Base64, optional) |

If `b_` is omitted, the result is saved in the same Bucket.

### Example: Generate and Save Thumbnail

```python
import base64
import oss2

auth = oss2.Auth('key-id', 'key-secret')
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'my-bucket')

# Encode target key
target_key = 'thumbnails/photo_thumb.jpg'
encoded_key = base64.urlsafe_b64encode(target_key.encode()).decode().rstrip('=')

# Process and save
process = f'image/resize,w_200,h_200|sys/saveas,o_{encoded_key}'
result = bucket.process_object('photos/photo.jpg', process)
```

### Use Cases
- Generate thumbnails on upload (via Function Compute trigger)
- Batch process existing images
- Create multiple size variants of uploaded images

## Original Image Protection

Prevent direct access to original images, allowing only processed versions.

### Configuration

1. Navigate to **Bucket > Data Processing > Image Processing > Access Settings**
2. Enable **Original Image Protection**
3. Specify **protected file suffixes** (e.g., `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`)

### Behavior When Enabled

| Access Pattern | Allowed? |
|---|---|
| `image.jpg` (direct access) | Blocked (403 Forbidden) |
| `image.jpg?x-oss-process=image/resize,w_300` | Allowed |
| `image.jpg?x-oss-process=style/thumbnail` | Allowed |
| `image.jpg-thumbnail` (style separator) | Allowed |
| Signed URL without processing | Blocked |
| Signed URL with processing | Allowed |

### Use Cases
- Protect high-resolution originals while serving optimized versions
- Enforce watermarking on all image access
- Prevent unauthorized downloading of source images
- Ensure all images go through a processing pipeline

### Notes
- Protection only applies to configured file suffixes
- Non-image files are not affected
- API/SDK access with valid credentials can still access originals
- Protection works with both anonymous and authenticated access

## Video Frame Capture

OSS also supports capturing frames from video files:

### URL Format
```
?x-oss-process=video/snapshot,t_<ms>,f_<format>,w_<width>,h_<height>,m_<mode>
```

### Parameters

| Parameter | Description |
|---|---|
| `t_<ms>` | Time position in milliseconds |
| `f_<format>` | Output format: jpg, png |
| `w_<pixels>` | Output width |
| `h_<pixels>` | Output height |
| `m_fast` | Fast mode (less accurate position, faster) |

### Example
```
# Capture frame at 5 seconds, 640x480, JPEG format
?x-oss-process=video/snapshot,t_5000,f_jpg,w_640,h_480

# Fast mode capture at 1 second
?x-oss-process=video/snapshot,t_1000,f_jpg,w_320,h_240,m_fast
```

### Supported Video Formats
MP4, AVI, FLV, MOV, MKV, and other common video formats.
