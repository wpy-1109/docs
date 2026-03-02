# Node.js SDK文件上传方式汇总

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-objects-9/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS Node.js SDK](/zh/oss/developer-reference/nodejs-sdk/)
 [对象/文件（Node.js SDK）](/zh/oss/developer-reference/objects-5/)
 上传文件（Node.js SDK）
 
 

 
# 上传文件（Node.js SDK）

 
更新时间: 2025-11-28 15:32:26

 

 

在对象存储OSS中，操作的基本数据单元是文件（Object）。OSS Node.js SDK提供了丰富的文件上传方式，包含如下：
- [上传本地文件（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/upload-a-local-file)：最大不能超过5 GB。
- [上传本地内存（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/upload-from-local-memory)：最大不能超过5 GB。
- [流式上传（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/streaming-upload-1)：最大不能超过5 GB。
- [分片上传（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-3)：当文件较大时，可以使用分片上传，最大不能超过48.8 TB。
- [追加上传（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-4)：使用AppendObject方法在已上传的Appendable Object类型文件后面直接追加内容。最大不能超过5 GB。
- [断点续传上传（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-5)：支持并发上传、断点续传、自定义分片大小。大文件上传推荐使用断点续传。最大不能超过48.8 TB。
- [上传回调（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/upload-callbacks-4)：支持完成文件上传时提供回调给应用服务器。

 上一篇: 对象/文件（Node.js SDK）
 下一篇: 上传本地文件（Node.js SDK）