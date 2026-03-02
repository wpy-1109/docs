# 下载文件（Browser.js SDK）

Source: https://help.aliyun.com/zh/oss/developer-reference/download-objects-20/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS Browser.js SDK](/zh/oss/developer-reference/browser-js/)
 下载文件（Browser.js SDK）
 
 

 
# 下载文件（Browser.js SDK）

 
更新时间: 2025-11-28 16:06:14

 

 

OSS Browser.js SDK支持多种下载文件的方式，您可以结合自身业务场景选用不同的下载方式：
- 当您需要通过文件URL的方式下载或预览文件时，您可以在浏览器中通过`signatureUrl`方法生成用于预览或下载的文件URL。具体操作，请参见[预览或下载文件（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/preview-or-download-an-object#concept-64052-zh)。
- 当您仅需要文件中的部分数据，您可以使用范围下载。具体操作，请参见[范围下载（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/range-download-3#concept-2166799)。
- 当您需要结合多个条件来限制下载行为时，您可以使用限定条件下载。例如只下载早于指定时间内修改的文件，或者与指定ETag匹配的文件等。具体操作，请参见[限定条件下载（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/conditional-download-3#concept-2166878)。

 上一篇: 上传回调（Browser.js SDK）
 下一篇: 预览或下载文件（Browser.js SDK）