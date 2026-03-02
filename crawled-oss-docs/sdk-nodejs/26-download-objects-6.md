# NodejsSDK下载文件不同方式与场景

Source: https://help.aliyun.com/zh/oss/developer-reference/download-objects-6/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS Node.js SDK](/zh/oss/developer-reference/nodejs-sdk/)
 [对象/文件（Node.js SDK）](/zh/oss/developer-reference/objects-5/)
 下载文件（Node.js SDK）
 
 

 
# 下载文件（Node.js SDK）

 
更新时间: 2025-11-28 15:32:54

 

 

OSS Node.js SDK支持多种下载文件的方式，您可以结合自身业务场景选用不同的下载方式：
- 当您需要将文件下载到本地或者下载到本地内存，请参见[下载到本地文件（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/download-objects-as-files-7)，[下载到本地内存（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/download-objects-to-the-local-memory-1)。
- 当您需要在文件下载过程中逐步处理数据，您可以使用流式下载。具体操作，请参见[流式下载（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/streaming-download-2)。
- 当您仅需要文件中的部分数据，您可以使用范围下载。具体操作，请参见[范围下载（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/range-download-3#concept-2166799)。
- 当您需要结合多个条件来限制下载行为时，您可以使用限定条件下载。例如只下载早于指定时间内修改的文件，或者与指定ETag匹配的文件等。具体操作，请参见[限定条件下载（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/conditional-download-3#concept-2166878)。

 上一篇: 使用预签名URL上传（Node.js SDK）
 下一篇: 下载到本地文件（Node.js SDK）