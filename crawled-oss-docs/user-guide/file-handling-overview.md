# What is File Processing

File Processing allows you to compress, decompress, and perform other operations on files in various formats. You can upload the original files to Object Storage Service (OSS) and call the RESTful API operation `x-oss-process` to compress, decompress, and perform other operations on the files anywhere, anytime, and from any connected devices.

## Parameter


You can encapsulate the pointcloud/compress parameter in styles to process documents. For more information about the styles, see [styles](https://www.alibabacloud.com/help/en/oss/user-guide/styles).


The following table describes the parameter.











(https://www.alibabacloud.com/help/en/oss/user-guide/point-cloud-compression)


| Processing operation | Parameter | Description |
| --- | --- | --- |
| Point cloud compression | pointcloud/compress | Compresses point cloud data (PCD) in Object Storage Service (OSS) to reduce the amount of data transferred over networks. |


## Usage


You can process images by calling the x-oss-process operation. For more information, see [Synchronous processing](https://www.alibabacloud.com/help/en/oss/user-guide/synchronous-processing).

## Limits


-

File Processing supports only files in PCD format.

-

The file to be processed can be up to 20 MB in size. You are required to call the x-oss-async-process operation to process files that exceed the upper limit. For more information, see [Point cloud compression](https://www.alibabacloud.com/help/en/imm/user-guide/point-cloud-compression-1).

## Billing


The fees for File Processing are included in the bills of Intelligent Media Management (IMM) service. For more information, see [Billing items](https://www.alibabacloud.com/help/en/imm/product-overview/billable-items).

Thank you! We've received your  feedback.