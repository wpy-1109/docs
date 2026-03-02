# C#SDK不同场景的文件下载方式

Source: https://help.aliyun.com/zh/oss/developer-reference/download-file-using-oss-sdk-for-csharp-v1/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS C# SDK V1](/zh/oss/developer-reference/preface-4/)
 [对象/文件（C# SDK V1）](/zh/oss/developer-reference/perform-operations-on-objects-using-oss-sdk-for-csharp-v1/)
 下载文件（C# SDK V1）
 
 

 
# 下载文件（C# SDK V1）

 
更新时间: 2025-11-28 15:22:12

 

 

OSS C# SDK支持多种下载文件的方式，您可以结合自身业务场景选用不同的下载方式：
- 当您需要在文件下载过程中逐步处理数据，您可以选择流式下载。具体操作，请参见[流式下载（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/streaming-download-3#concept-91748-zh)。
- 当您仅需要文件中的部分数据，您可以使用范围下载。具体操作，请参见[范围下载（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/range-download-4#concept-91750-zh)。
- 当您需要进行大文件的稳定下载，您可以使用断点续传下载。具体操作，请参见[断点续传下载（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/resumable-download-4#concept-91756-zh)。
- 当您需要在下载过程中查看下载进度，您可以使用进度条功能。具体操作，请参见[进度条（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/progress-bars-3#concept-91759-zh)。

 上一篇: 上传回调（C# SDK V1）
 下一篇: 流式下载（C# SDK V1）