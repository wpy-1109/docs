# Image Rotate, Blur, Brightness, Contrast, Sharpen

Source: https://help.aliyun.com/zh/oss/user-guide/img-overview

## Rotate (rotate)

Rotate the image clockwise by a specified angle.

### URL Format
```
?x-oss-process=image/rotate,<degrees>
```

### Parameters
| Parameter | Description | Value Range |
|---|---|---|
| `<degrees>` | Rotation angle (clockwise) | 0-360 |

### Examples
```
# Rotate 90 degrees clockwise
?x-oss-process=image/rotate,90

# Rotate 180 degrees
?x-oss-process=image/rotate,180

# Rotate 45 degrees
?x-oss-process=image/rotate,45
```

**Note**: Non-right-angle rotations (e.g., 45 degrees) will increase the canvas size. The new background areas are white for JPEG or transparent for PNG.

## Auto-Orient (auto-orient)

Automatically rotate the image based on EXIF orientation data. Useful for photos from cameras/phones that may have rotation metadata.

### URL Format
```
?x-oss-process=image/auto-orient,value_<0|1>
```

| Value | Description |
|---|---|
| `value_0` | Disable auto-orientation |
| `value_1` | Enable auto-orientation (default if auto-orient is used) |

### Example
```
# Auto-orient based on EXIF
?x-oss-process=image/auto-orient,value_1
```

## Blur (blur)

Apply Gaussian blur to the image.

### URL Format
```
?x-oss-process=image/blur,r_<radius>,s_<sigma>
```

### Parameters
| Parameter | Description | Value Range |
|---|---|---|
| `r_<value>` | Blur radius | 1-50 |
| `s_<value>` | Standard deviation (sigma) | 1-50 |

**Larger radius**: More pixels affected (bigger blur area)
**Larger sigma**: More intense blur effect

### Examples
```
# Light blur
?x-oss-process=image/blur,r_3,s_2

# Heavy blur (for backgrounds or privacy)
?x-oss-process=image/blur,r_50,s_50

# Medium blur
?x-oss-process=image/blur,r_10,s_5
```

## Brightness (bright)

Adjust the brightness of the image.

### URL Format
```
?x-oss-process=image/bright,<value>
```

### Parameters
| Parameter | Description | Value Range |
|---|---|---|
| `<value>` | Brightness adjustment | -100 to 100 |

- **0**: No change
- **Positive values**: Brighter
- **Negative values**: Darker

### Examples
```
# Increase brightness by 50
?x-oss-process=image/bright,50

# Decrease brightness by 30
?x-oss-process=image/bright,-30
```

## Contrast (contrast)

Adjust the contrast of the image.

### URL Format
```
?x-oss-process=image/contrast,<value>
```

### Parameters
| Parameter | Description | Value Range |
|---|---|---|
| `<value>` | Contrast adjustment | -100 to 100 |

- **0**: No change
- **Positive values**: Higher contrast
- **Negative values**: Lower contrast

### Examples
```
# Increase contrast
?x-oss-process=image/contrast,50

# Decrease contrast
?x-oss-process=image/contrast,-30
```

## Sharpen (sharpen)

Apply sharpening to the image.

### URL Format
```
?x-oss-process=image/sharpen,<value>
```

### Parameters
| Parameter | Description | Value Range |
|---|---|---|
| `<value>` | Sharpening intensity | 50-399 |

### Examples
```
# Light sharpening
?x-oss-process=image/sharpen,100

# Strong sharpening
?x-oss-process=image/sharpen,300
```

## Combining Effects

```
# Resize, auto-orient, increase brightness and contrast, sharpen
?x-oss-process=image/resize,w_800/auto-orient,value_1/bright,20/contrast,30/sharpen,100

# Create a blurred background thumbnail
?x-oss-process=image/resize,w_400/blur,r_20,s_10/bright,-20
```
