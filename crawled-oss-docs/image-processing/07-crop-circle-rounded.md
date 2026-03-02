# Image Crop, Circle, and Rounded Corners

Source: https://help.aliyun.com/zh/oss/user-guide/img-overview

## Custom Crop (crop)

Crop a specific region from the image.

### URL Format
```
?x-oss-process=image/crop,<params>
```

### Parameters

| Parameter | Description | Value Range |
|---|---|---|
| `w_<value>` | Crop width in pixels | 0 to image width |
| `h_<value>` | Crop height in pixels | 0 to image height |
| `x_<value>` | X-axis offset (from gravity point) | 0 to image width |
| `y_<value>` | Y-axis offset (from gravity point) | 0 to image height |
| `g_<position>` | Gravity (anchor point) | See position values |

### Position Values for Gravity (g_)

```
nw (top-left)     north (top-center)    ne (top-right)
west (mid-left)   center (middle)       east (mid-right)
sw (bottom-left)  south (bottom-center) se (bottom-right)
```

### Examples

```
# Crop 200x200 from center
?x-oss-process=image/crop,w_200,h_200,g_center

# Crop 300x100 from top-left with 10px offset
?x-oss-process=image/crop,w_300,h_100,g_nw,x_10,y_10

# Crop 200x200 from bottom-right corner
?x-oss-process=image/crop,w_200,h_200,g_se
```

## Index Crop (indexcrop)

Split the image into equal tiles and select one.

### URL Format
```
?x-oss-process=image/indexcrop,x_<width>,i_<index>
```

### Parameters

| Parameter | Description |
|---|---|
| `x_<value>` | Width of each tile in pixels |
| `y_<value>` | Height of each tile in pixels |
| `i_<value>` | Index of the tile to return (0-based) |

### Example
```
# Split into 100px-wide tiles, return the first tile
?x-oss-process=image/indexcrop,x_100,i_0
```

## Circle Crop (circle)

Crop the image into a circle.

### URL Format
```
?x-oss-process=image/circle,r_<radius>
```

### Parameters

| Parameter | Description |
|---|---|
| `r_<value>` | Circle radius in pixels |

### Notes
- If the radius exceeds the shortest side of the image, the shortest side is used
- The circle is centered on the image
- Areas outside the circle become transparent (PNG output) or white (JPEG output)
- For transparent backgrounds, output as PNG:
  ```
  ?x-oss-process=image/circle,r_100/format,png
  ```

### Example
```
# Circle crop with 100px radius
?x-oss-process=image/circle,r_100

# Circle crop with transparent background
?x-oss-process=image/circle,r_100/format,png
```

## Rounded Corners (rounded-corners)

Add rounded corners to the image.

### URL Format
```
?x-oss-process=image/rounded-corners,r_<radius>
```

### Parameters

| Parameter | Description |
|---|---|
| `r_<value>` | Corner radius in pixels |

### Notes
- If the radius exceeds the shortest side, the shortest side is used
- Corners become transparent (PNG) or white (JPEG)
- For transparent corners, output as PNG

### Example
```
# Rounded corners with 30px radius
?x-oss-process=image/rounded-corners,r_30

# Rounded corners with transparent background
?x-oss-process=image/rounded-corners,r_30/format,png
```

## Combining Crop Operations

Crop operations can be chained with other operations:

```
# Resize to 500px wide, then crop 200x200 from center, then add rounded corners
?x-oss-process=image/resize,w_500/crop,w_200,h_200,g_center/rounded-corners,r_20/format,png
```
