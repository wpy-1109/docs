# C#SDK文件上传方法功能总览

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-objects-using-oss-sdk-for-csharp-v1/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS C# SDK V1](/zh/oss/developer-reference/preface-4/)
 [对象/文件（C# SDK V1）](/zh/oss/developer-reference/perform-operations-on-objects-using-oss-sdk-for-csharp-v1/)
 上传文件（C# SDK V1）
 
 

 
# 上传文件（C# SDK V1）

 
更新时间: 2025-11-28 15:21:36

 

 

在OSS中，操作的基本数据单元是文件（Object）。OSS C# SDK提供了丰富的文件上传方式：
- [简单上传（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/simple-upload-9#concept-91093-zh)：文件最大不能超过5GB。
- [追加上传（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-10#concept-91099-zh)：文件最大不能超过5GB。
- [断点续传上传（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-8#concept-91101-zh)：支持并发、断点续传、自定义分片大小。大文件上传推荐使用断点续传。最大不能超过48.8TB。
- [分片上传（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-10#concept-91103-zh)：当文件较大时，可以使用分片上传，最大不能超过48.8TB。

上传过程中，您可以[设置文件元数据](https://help.aliyun.com/zh/oss/developer-reference/manage-object-metadata-8#concept-91920-zh)，也可以通过[进度条（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/progress-bars-6#concept-91108-zh)功能查看上传进度。上传完成后，您还可以进行[上传回调（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/upload-callbacks-9#concept-91107-zh)。

 上一篇: 对象/文件（C# SDK V1）
 下一篇: 简单上传（C# SDK V1）