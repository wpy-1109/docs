# How do I use the new version of GetObject to process images?

You can specify Image Processing (IMG) parameters in GetObject requests to process image objects in Object Storage Service (OSS). For example, you can add image watermarks to images or convert image formats.

## IMG parameters


OSS allows you to use one or more parameters to process images. You can also encapsulate multiple IMG parameters in a style and use the style to process images. For more information about image styles, see [Image styles](https://www.alibabacloud.com/help/en/oss/user-guide/image-styles#concept-mr2-x3c-wdb).


If you specify multiple IMG parameters, OSS processes the image based on the parameters in the order they are specified. The following table describes IMG parameters.











(https://www.alibabacloud.com/help/en/oss/user-guide/resize-images-4#concept-hxj-c4n-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/add-watermarks#concept-hrt-sv5-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/custom-crop#concept-bbn-14s-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/adjust-image-quality#concept-exc-qp5-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/convert-image-formats-2#concept-mf3-md5-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/advanced-compression-of-heif-or-avif-images#concept-2055010)


(https://www.alibabacloud.com/help/en/oss/user-guide/query-the-exif-data-of-an-image-4#concept-nbj-1fv-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/auto-rotate-4#concept-ugq-tvs-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/circle-crop#concept-n5s-3ms-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/indexed-slice#concept-ecq-cqs-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/rounded-rectangle-4#concept-xts-dss-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/blur#concept-bwn-mvt-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/rotate#concept-yvv-25t-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/gradual-display#concept-avy-pf5-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/query-the-average-tone#concept-hsb-wcv-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/brightness#concept-mv4-fxt-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/sharpen#concept-cyw-zzt-vdb)


(https://www.alibabacloud.com/help/en/oss/user-guide/contrast#concept-dpw-4yt-vdb)


| Operation | Parameter | Description |
| --- | --- | --- |
| Resizing | resize | Resizes images. |
| Watermarking | watermark | Adds image watermarks or text watermarks to images. |
| Custom cropping | crop | Crops rectangular images based on the specified size. |
| Image quality adjustment | quality | Adjusts the quality of images in the JPG format and WebP format. |
| Format conversion | format | Converts the formats of images to specified formats. |
| Advanced compression of HEIF or AVIF images | format | Converts image formats to HEIF or AVIF that provides high compression efficiency |
| Image information query | info | Obtains image information, including basic information and Exchangeable Image File Format (EXIF) information. |
| Auto orientation | auto-orient | Auto-rotates images. |
| Circle crop | circle | Crops images into circles of the specified size based on the center point of images. |
| Indexed slice | indexcrop | Crops images along the specified horizontal axis or vertical axis and selects one of the images. |
| Rounded rectangle | rounded-corners | Crops images into rounded rectangles based on the specified rounded radius. |
| Blurring effect | blur | Blurs images. |
| Rotation | rotate | Rotates images clockwise by a specified angle. |
| Gradual display | interlace | Configures gradual display for JPG images. |
| Average hue query | average-hue | Queries the average hue of images. |
| Brightness adjustment | bright | Adjusts the brightness of images. |
| Sharpening | sharpen | Sharpens images. |
| Contrast adjustment | contrast | Adjusts the contrast of images. |


For example, if you add the `resize` and `quality` parameters to process the `example.jpg` image, the URL of the image is `https://oss-console-img-demo-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/example.jpg?x-oss-process=image/resize,w_300/quality,q_90`. You can configure Alibaba Cloud CDN back-to-origin rules to filter out or retain the IMG parameters contained in the URLs of images that you want to retrieve. This way, you can retrieve source images or images that are processed by using IMG parameters.


-

Retrieve a source image


You can enable the parameter filtering feature of Alibaba Cloud CDN to filter out all parameters that follow the question mark (?) in the URL of the image that you want to retrieve. In this example, the `example.jpg` source image is retrieved.

-

Retrieve a processed image


You can enable the parameter retaining feature of Alibaba Cloud CDN to retain all parameters that follow the question mark (?) in the URL of the image that you want to retrieve. In this example, the processed image is retrieved.


For more information about Alibaba Cloud CDN back-to-origin rules, see [Ignore parameters](https://www.alibabacloud.com/help/en/cdn/user-guide/ignore-parameters#task-187634).

## IMG methods


You can use object URLs, API operations, and SDKs to process images. For more information, see [IMG implementation modes](https://www.alibabacloud.com/help/en/oss/user-guide/img-implementation-modes#concept-m4f-dcn-vdb).

## Limits








-


-


-

(https://smartservice.console.alibabacloud.com/#/ticket/createIndex)





(https://smartservice.console.alibabacloud.com/#/ticket/createIndex)


> NOTE:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/user-guide/image-styles)


-


-


-


-


-


-


> NOTE:

> NOTE: 


> NOTE: 

(https://smartservice.console.alibabacloud.com/#/ticket/createIndex)


| Item | Description |
| --- | --- |
| Image formats | Only JPG, PNG, BMP, GIF, WebP, TIFF, HEIC, and AVIF images are supported. Only resizing, cropping, rotation, and watermarking are supported for dynamic images, such as GIF images. If you want to encode or decode dynamic images in the WebP format, submit a ticket. |
| Image size | The size of a source image cannot exceed 20 MB. |
| Image width and height | For the rotate operation, the height or width of the source image cannot exceed 4,096 pixels. For other operations, the width or height of the source image cannot exceed 30,000 pixels, and the total pixel number of the source image cannot exceed 250 million. The total pixel number of a dynamic image, such as a GIF image, is calculated based on the following formula: Width × Height × Number of image frames. The total pixel number of a static image, such as a PNG image, is calculated based on the following formula: Width × Height. |
| Image compression | The width or height of a compressed image cannot exceed 16,384 pixels. The total pixel number of a compressed image cannot exceed 16,777,216. |
| Advanced image compression | The number of pixels of a compressed HEIC image cannot exceed 4,096 × 4,096. The number of pixels of a compressed AVIF image cannot exceed 4,096 × 2,304. |
| Image styles | You can create up to 50 image styles for each bucket. If your business requires more than 50 styles for a bucket, submit a ticket. Note You can include multiple IMG parameters in an image style to perform complex operations on images that are stored in a bucket. For more information, see Image styles. |
| Processing capability | Per-second processing throughput (by source image)The maximum throughput of image processing is 20 MB/s for the following regions: China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), and China (Shenzhen). The maximum throughput of image processing for other regions is 2 MB/s. Queries per second (QPS)The QPS limit is 50 for China (Hangzhou), China (Shanghai), China (Beijing), China (Zhangjiakou), and China (Shenzhen). The QPS limit for other regions is 5. Note You may want to go beyond the preceding limits in computationally intensive business applications, such as encoding WebP, AVIF, or HEIF images at a resolution higher than 1080p. To increase the limits, contact technical support. |


## Billing


You are charged the following fees when you use IMG:


-

API operation calling fees


A GetObject request is generated each time you use IMG to process an image. You are charged based on the number of generated requests. For more information, see [Request fees](https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees#concept-2558398).

-

Traffic fees


You are charged for the outbound traffic over the Internet based on the size of processed images. For more information, see [Traffic fees](https://www.alibabacloud.com/help/en/oss/traffic-fees#concept-2558367).

## IMG versions


IMG provides two versions of API operations. This topic describes the new version of the API operations. Update support is no longer provided for the old version. For more information about the compatibility of the new and old versions of API operations, see [Differences between the old and new versions of IMG](https://www.alibabacloud.com/help/en/oss/user-guide/differences-between-the-old-and-new-versions-of-img#concept-tmj-dxc-wdb).


Thank you! We've received your  feedback.