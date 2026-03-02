# 文件上传的多种实现方式

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-objects-12/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS iOS SDK](/zh/oss/developer-reference/preface-5/)
 [对象/文件（iOS SDK）](/zh/oss/developer-reference/objects-9/)
 上传文件（iOS SDK）
 
 

 
# 上传文件（iOS SDK）

 
更新时间: 2025-12-01 09:30:33

 

 

本文档介绍 OSS iOS SDK 上传文件的方式。

在 OSS 中，操作的基本数据单元是文件（Object）。OSS iOS SDK提供了以下四种文件上传方式：
- [简单上传（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/simple-upload-5#concept-vp1-tbg-4fb)：包括从内存中上传或上传本地文件。最大不能超过 5GB。
- [分片上传（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-7#concept-ch3-ffg-4fb)：当文件较大时，可以使用分片上传，最大不能超过48.8TB。
- [追加上传（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-7#concept-svd-kfg-4fb)：最大不能超过 5GB。
- [断点续传上传（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-3#concept-32063-zh)：支持并发上传、自定义分片大小。大文件上传推荐使用断点续传。最大不能超过 48.8TB。
说明 
各种上传方式的适用场景请参见操作指南中的[上传文件](https://help.aliyun.com/zh/oss/user-guide/upload-objects-to-oss/)。

上传过程中，您可以通过[进度条（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/progress-bar-3)查看上传进度。上传完成后，您还可以进行[上传回调（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/upload-callbacks-7#concept-crq-tfg-4fb)。

 上一篇: 对象/文件（iOS SDK）
 下一篇: 简单上传（iOS SDK）