# Image Processing (IMG) - Custom Crop

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/custom-crop

You can use the custom crop feature to obtain images of a specific size.

## Scenarios

- **Web design**: Crop images to fit profile pictures, backgrounds, product displays
- **Social media**: Crop to platform-specific dimensions
- **Mobile apps**: Crop icons, splash screens for different resolutions
- **Image database**: Uniformly crop images for archiving

## Notes

- Specified width and height cannot exceed 16,384 pixels
- If starting coordinates exceed the original image, a BadRequest error is returned
- If crop area exceeds boundaries, system crops to the image edge

## Parameters

Action: `crop`

| Parameter | Description | Value |
|-----------|-------------|-------|
| w | Width of crop area | [0, image width], default: max |
| h | Height of crop area | [0, image height], default: max |
| x | X coordinate (from upper-left) | [0, image width] |
| y | Y coordinate (from upper-left) | [0, image height] |
| g | Crop origin position | nw, north, ne, west, center, east, sw, south, se, face, auto |
| p | Resize percentage for face crop | [1,200] (only with g_face) |

### Crop Origin Positions

```
nw -------- north -------- ne
|                           |
west ------ center ------ east
|                           |
sw -------- south -------- se
```

### Position Calculation

| Origin | Calculation |
|--------|-------------|
| nw | 0, 0 |
| north | srcW/2 - w/2, 0 |
| ne | srcW - w, 0 |
| west | 0, srcH/2 - h/2 |
| center | srcW/2 - w/2, srcH/2 - h/2 |
| east | srcW - w, srcH/2 - h/2 |
| sw | 0, srcH - h |
| south | srcW/2 - w/2, srcH - h |
| se | srcW - w, srcH - h |

## Examples

### Crop from specific starting point
```
?x-oss-process=image/crop,x_800,y_500
```

### Crop with specific dimensions from starting point
```
?x-oss-process=image/crop,x_800,y_500,w_300,h_300
```

### Crop from lower-right corner
```
?x-oss-process=image/crop,g_se,w_900,h_900
```

### Crop with offset from lower-right
```
?x-oss-process=image/crop,g_se,x_100,y_200,w_900,h_900
```

### Smart cropping (requires IMM)
```
?x-oss-process=image/crop,g_auto
```

### Face-centered crop (requires IMM)
```
?x-oss-process=image/crop,g_face,w_200,h_200
```

### Face crop with 2x enlargement
```
?x-oss-process=image/crop,g_face,p_200
```

> **Note**: `g_face` and `g_auto` require binding the bucket to an IMM project. Anonymous access is not supported for these features.
