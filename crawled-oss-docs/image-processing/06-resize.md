# Image Resize Operations

Source: https://help.aliyun.com/zh/oss/user-guide/img-overview

## Overview

The resize operation allows you to scale images by specifying target dimensions and resize modes.

## URL Format

```
?x-oss-process=image/resize,<params>
```

## Resize Modes

| Mode | Parameter | Description |
|---|---|---|
| **Proportional (fit)** | `m_lfit` | Scale to fit within specified dimensions (default) |
| **Proportional (cover)** | `m_mfit` | Scale to cover minimum specified dimensions |
| **Fill** | `m_fill` | Scale and crop to exactly fill specified dimensions |
| **Pad** | `m_pad` | Scale and pad with solid color to fill dimensions |
| **Fixed** | `m_fixed` | Force exact width and height (may distort) |

## Parameters

| Parameter | Description | Value Range |
|---|---|---|
| `w_<value>` | Target width in pixels | 1-16384 |
| `h_<value>` | Target height in pixels | 1-16384 |
| `l_<value>` | Longest side in pixels | 1-16384 |
| `s_<value>` | Shortest side in pixels | 1-16384 |
| `p_<value>` | Scale percentage | 1-1000 |
| `limit_0` | Allow upscaling | 0 (allow) or 1 (prevent, default) |
| `color_<hex>` | Padding color (for m_pad) | 6-digit hex (e.g., FF0000) |

## Examples

### Scale to width 300px (maintain aspect ratio)
```
?x-oss-process=image/resize,w_300
```

### Scale to fit within 300x200
```
?x-oss-process=image/resize,m_lfit,w_300,h_200
```

### Fill 300x200 with center crop
```
?x-oss-process=image/resize,m_fill,w_300,h_200
```

### Scale to 50% of original
```
?x-oss-process=image/resize,p_50
```

### Pad to 300x300 with white background
```
?x-oss-process=image/resize,m_pad,w_300,h_300,color_FFFFFF
```

### Force exact dimensions (may distort)
```
?x-oss-process=image/resize,m_fixed,w_300,h_200
```

### Scale with longest side = 500px
```
?x-oss-process=image/resize,l_500
```

## Notes

- By default, images are NOT upscaled (limit_1). Set `limit_0` to allow upscaling.
- Original aspect ratio is maintained except in `m_fixed` mode.
- For animated GIF images, resize applies to all frames.
- Maximum output dimensions: 16,384 x 16,384 pixels.
- If only width or height is specified, the other dimension scales proportionally.
