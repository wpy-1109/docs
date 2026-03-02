# RubySDK多种文件上传方式

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-objects-3/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS Ruby SDK](/zh/oss/developer-reference/ruby/)
 上传文件（Ruby SDK）
 
 

 
# 上传文件（Ruby SDK）

 
更新时间: 2025-11-28 16:03:28

 

 

本文介绍对象存储OSS Ruby SDK的多种文件上传方式。

OSS Ruby SDK文件上传方式如下：
- [上传本地文件（Ruby SDK）](https://help.aliyun.com/zh/oss/developer-reference/local-file-upload#concept-2233084)：最大不能超过5 GB。
- [流式上传（Ruby SDK）](https://help.aliyun.com/zh/oss/developer-reference/streaming-upload#concept-2233089)：最大不能超过5 GB。
- [断点续传上传（Ruby SDK）](https://help.aliyun.com/zh/oss/developer-reference/resumable-download-1#concept-2233093)：支持并发上传、断点续传、自定义分片大小。大文件上传推荐使用断点续传。最大不能超过48.8 TB。
- [追加上传（Ruby SDK）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-1#concept-2233095)：使用AppendObject方法在已上传的Appendable Object类型文件后面直接追加内容。最大不能超过5 GB。

上传完成后，您还可以进行[上传回调（Ruby SDK）](https://help.aliyun.com/zh/oss/developer-reference/upload-callbacks-1#concept-2233100)。

 上一篇: 使用自定义域名（Ruby SDK）
 下一篇: 上传本地文件（Ruby SDK）