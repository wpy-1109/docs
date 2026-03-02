# 文件管理核心操作方法概览

Source: https://help.aliyun.com/zh/oss/developer-reference/manage-objects-8/

---

[首页](https://help.aliyun.com/)
 [对象存储](/zh/oss/)
 [开发参考](/zh/oss/developer-reference/)
 [SDK参考](/zh/oss/developer-reference/sdk-code-samples/)
 [OSS Browser.js SDK](/zh/oss/developer-reference/browser-js/)
 管理文件（Browser.js SDK）
 
 

 
# 管理文件（Browser.js SDK）

 
更新时间: 2025-11-28 16:06:37

 

 

OSS Browser.js SDK提供多种管理存储空间（Bucket）内文件（Object）的方式。请结合自身业务场景，灵活选用以下多种文件的管理方式：
- 当您需要了解Bucket内所有文件或者指定目录下包含的文件和子目录相关信息时，请使用列举文件。具体操作，请参见[列举文件（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/list-objects-16#concept-2161421)。
- 当您需要将某个Bucket中的文件复制到同一地域下相同或不同目标Bucket时，请使用拷贝文件。具体操作，请参见[拷贝文件（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/copy-objects-15#concept-2166879)。
- 当您不希望在上传或拷贝文件过程中覆盖已有的同名文件时，请使用禁止覆盖同名文件。具体操作，请参见[禁止覆盖同名文件（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/prevent-objects-from-being-overwritten-by-objects-with-the-same-names#concept-2161349)。
- 当您需要读取归档或冷归档文件时，需要先解冻这两种类型的文件。具体操作，请参见[解冻文件（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/restore-objects-13#concept-2167072)。
- 当您需要快速访问Bucket内的常用文件时，您可以通过软链接快速打开源文件。具体操作，请参见[管理软链接（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/manage-symbolic-links-17#concept-2167079)。
- 当您需要标识文件的用途或属性等，您可以在上传文件时指定文件元数据。具体操作，请参见[管理文件元数据（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/manage-object-metadata-3#concept-2166880)。

 上一篇: 限定条件下载（Browser.js SDK）
 下一篇: 判断文件是否存在（Browser.js SDK）