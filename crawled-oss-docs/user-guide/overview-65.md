# What is document processing?

Document conversion provided by Intelligent Media Management (IMM) allows you to convert documents to supported formats. You can upload a source document to Object Storage Service (OSS) and call `x-oss-process` and `x-oss-async-process` to process the source document anytime, anywhere, and from any connected device by using different features, such as document conversion, online document preview, and online file editing.

## Processing parameters


OSS allows you to use one or more parameters to process a document. You can also specify multiple parameters in a style to process multiple documents at a time. For more information about styles, see [Style](https://www.alibabacloud.com/help/en/oss/user-guide/styles).


If you specify multiple parameters, OSS processes the document based on the parameters in the order in which the parameters are specified. The following table describes the processing parameters of different features.











(https://www.alibabacloud.com/help/en/oss/user-guide/document-conversion)


(https://www.alibabacloud.com/help/en/oss/user-guide/online-object-preview)


(https://www.alibabacloud.com/help/en/oss/user-guide/online-object-editing)


(https://www.alibabacloud.com/help/en/oss/user-guide/document-snapshot)


(https://www.alibabacloud.com/help/en/oss/user-guide/smart-document-overview/)


| Feature | Parameter | Description |
| --- | --- | --- |
| Document conversion | doc/convert | Convert a document in OSS to the required format. |
| Online document preview | doc/preview | Preview a document in OSS online. |
| Online file editing | doc/edit | Collaboratively edit a document in OSS online. |
| Document snapshot | doc/snapshot | Generate a snapshot for a specific page of a document in OSS. |
| Intelligent document processing | Refer to specific documents | Process documents in OSS by using AI-driven capabilities, including content translation, polishing, summarization, document continuation, document enrichment, and tone adjustment. |


## Methods


-

Call x-oss-async-process to convert the format of a document. For more information, see [Asynchronous processing](https://www.alibabacloud.com/help/en/oss/user-guide/asynchronous-processing).

-

Create a batch processing job to convert the format of multiple objects in a bucket at a time. For more information, see [Batch processing](https://www.alibabacloud.com/help/en/oss/user-guide/batch-processing).

-

Create a trigger to convert the format of new objects in a bucket. For more information, see [Triggers](https://www.alibabacloud.com/help/en/oss/user-guide/triggers).

-

Call x-oss-process to preview a document online, edit a document online, capture snapshots of a document, and use intelligent document processing. For more information, see [Synchronous processing](https://www.alibabacloud.com/help/en/oss/user-guide/synchronous-processing).

## Limits

### Object formats supported by document conversion


-

Supported formats for the source document








| Document type | Object suffix |
| --- | --- |
| Text document | doc, dot, wps, wpt, docx, dotx, docm, dotm, txt, wpss, lrc, c, cpp, h, asm, s, java, asp, bat, bas, prg, cmd, rtf, txt, log, xml, htm, and html |
| Presentation document | pptx, ppt, pot, potx, pps, ppsx, dps, dpt, pptm, potm, ppsm, and dpss |
| Table document | xls, xlt, et, ett, xlsx, xltx, csv, xlsb, xlsm, xltm, and ets |
| PDF document | pdf |


-

Supported formats for the destination document








| Format | Description |
| --- | --- |
| JPEG | Each page is converted to a JPEG image. |
| PNG | Each page is converted to a PNG image. |
| PDF | Each document is converted to a PDF object. |
| TXT | Each document is converted to a TXT object. |


### Limits on the object size and page number for document conversion


-

A single document conversion task supports a source object that is up to 200 MB in size.

-

No limit is imposed on the number of pages of the source object converted at a time. However, if the number of pages is too large, the document conversion task may time out. In this case, you must specify the page number parameter for the document conversion task to convert the source object page by page. Example:


`plaintext
POST /exmaple.docx?x-oss-async-process HTTP/1.1
Host: doc-demo.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 28 Oct 2022 06:40:10 GMT
Authorization: OSS qn6q:77Dv

 // Convert page 1 to page 10 of the example.docx object to PNG images. The PNG images are stored in oss://test-bucket/doc_images/page.png.
x-oss-async-process=doc/convert,pages_MS0xMA,target_png,source_docx|sys/saveas,b_dGVzdC1idWNrZXQ,o_ZG9jX2ltYWdlcy97aW5kZXh9LnBuZw
`


### Object formats supported by online document preview


The following table describes the object formats supported by online document preview.








| Document type | Object suffix |
| --- | --- |
| Text document | doc, dot, wps, wpt, docx, dotx, docm, dotm, and rtf |
| Table document | xls, xlt, et, xlsx, xltx, csv, xlsm, and xltm |
| Presentation document | ppt, pptx, pptm, ppsx, ppsm, pps, potx, potm, dpt, and dps |
| PDF document | pdf |


### Object formats supported by online file editing


The following table describes the object formats supported by online file editing.








| Document type | Object suffix |
| --- | --- |
| Text document | doc, dot, wps, wpt, docx, dotx, docm, and dotm |
| Table document | xls, xlt, et, xlsx, xltx, xlsm, and xltm |
| Presentation document | ppt, pptx, pptm, ppsx, ppsm, pps, potx, potm, dpt, and dps |


### Limits on the object size and page number for online file editing and online document preview


-

A single online file editing or online document preview task supports an object that is up to 200 MB in size.

-

No limit is imposed on the number of pages of an object for an online file editing or online document preview task.

### Supported formats for snapshots captured by using document snapshot


-

JPG and PNG snapshots are supported.

## Billing rules


You are charged the following fees when you use document processing:


-

Document processing fees: Charged by IMM. For more information, see [Billable items](https://www.alibabacloud.com/help/en/imm/product-overview/billable-items).

-

API operation calling fees: A Get request is generated when you perform online document preview, online file editing, and document snapshot tasks. You are charged based on the number of requests. For more information, see [API operation calling fees](https://www.alibabacloud.com/help/en/oss/api-operation-calling-fees).

-

Traffic fees: You are charged for outbound traffic over the Internet based on the size of the destination objects returned for online document preview, online file editing, and document snapshot tasks. For more information, see [Traffic fees](https://www.alibabacloud.com/help/en/oss/traffic-fees).


Thank you! We've received your  feedback.