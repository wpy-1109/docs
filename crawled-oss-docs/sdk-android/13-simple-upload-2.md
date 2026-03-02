# 使用Android SDK实现简单上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/simple-upload-2

---

- 使用Android SDK实现简单上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

  [](https://www.aliyun.com/)[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)查看 "" 全部搜索结果[](https://www.aliyun.com/search?from=h5-global-nav-search)[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

  [官方文档](/zh)
 
[

用户指南
](/zh/oss/user-guide/)

 - [

开发参考
](/zh/oss/developer-reference/)

 - [

产品计费
](/zh/oss/billing/)

 - [

常见问题
](/zh/oss/oss-faq/)

 - [

动态与公告
](/zh/oss/announcements-and-updates/)

[首页](/zh)
# 简单上传（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
简单上传是指通过PutObject方法上传单个文件（Object）。简单上传包括上传本地文件和二进制byte[]数组。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

## 权限说明

阿里云账号默认拥有全部权限。阿里云账号下的RAM用户或RAM角色默认没有任何权限，需要阿里云账号或账号管理员通过[RAM Policy](https://help.aliyun.com/zh/oss/ram-policy-overview/)或[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)授予操作权限。
| API | Action | 说明|
| PutObject | `oss:PutObject` | 上传Object。|
| `oss:PutObjectTagging` | 上传Object时，如果通过x-oss-tagging指定Object的标签，则需要此操作的权限。|
| `kms:GenerateDataKey` | 上传Object时，如果Object的元数据包含X-Oss-Server-Side-Encryption: KMS，则需要这两个操作的权限。|
| `kms:Decrypt`|

## 上传本地文件

您可以通过同步方式或者异步方式上传本地文件到OSS。

调用同步接口上传

以下代码用于以同步方式上传examplefile.txt文件到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件。

```
// 构造上传请求。
// 依次填写Bucket名称（例如examplebucket）、Object完整路径（例如exampledir/exampleobject.txt）和本地文件完整路径（例如/storage/emulated/0/oss/examplefile.txt）。
// Object完整路径中不能包含Bucket名称。
PutObjectRequest put = new PutObjectRequest("examplebucket", "exampledir/exampleobject.txt", "/storage/emulated/0/oss/examplefile.txt");

// 设置文件元数据为可选操作。
 ObjectMetadata metadata = new ObjectMetadata();
// metadata.setContentType("application/octet-stream"); // 设置content-type。
// metadata.setContentMD5(BinaryUtil.calculateBase64Md5(uploadFilePath)); // 校验MD5。
// 设置Object的访问权限为私有。
metadata.setHeader("x-oss-object-acl", "private");
// 设置Object的存储类型为标准存储。
metadata.setHeader("x-oss-storage-class", "Standard");
// 设置禁止覆盖同名Object。
// metadata.setHeader("x-oss-forbid-overwrite", "true");
// 指定Object的对象标签，可同时设置多个标签。
// metadata.setHeader("x-oss-tagging", "a:1");
// 指定OSS创建目标Object时使用的服务端加密算法 。
// metadata.setHeader("x-oss-server-side-encryption", "AES256");
// 表示KMS托管的用户主密钥，该参数仅在x-oss-server-side-encryption为KMS时有效。
// metadata.setHeader("x-oss-server-side-encryption-key-id", "9468da86-3509-4f8d-a61e-6eab1eac****");

put.setMetadata(metadata);

try {
    PutObjectResult putResult = oss.putObject(put);

    Log.d("PutObject", "UploadSuccess");
    Log.d("ETag", putResult.getETag());
    Log.d("RequestId", putResult.getRequestId());
} catch (ClientException e) {
    // 客户端异常，例如网络异常等。
    e.printStackTrace();
} catch (ServiceException e) {
    // 服务端异常。
    Log.e("RequestId", e.getRequestId());
    Log.e("ErrorCode", e.getErrorCode());
    Log.e("HostId", e.getHostId());
    Log.e("RawMessage", e.getRawMessage());
}
```

对于Android10及以上版本的分区存储，您可以使用文件的Uri上传文件到OSS。

```
// 构造上传请求。
// 依次填写Bucket名称（例如examplebucket）和Object完整路径（例如exampledir/exampleobject.txt）。
// Object完整路径中不能包含Bucket名称。
PutObjectRequest put = new PutObjectRequest("examplebucket", "exampledir/exampleobject.txt",fileUri);

// 设置文件元数据。
// ObjectMetadata metadata = new ObjectMetadata();
// 设置Content-Type。
// metadata.setContentType("text/plain"); 
// 校验MD5。
// metadata.setContentMD5(BinaryUtil.calculateBase64Md5(uploadFilePath)); 
// put.setMetadata(metadata);

try {
    PutObjectResult putResult = oss.putObject(put);

    Log.d("PutObject", "UploadSuccess");
    Log.d("ETag", putResult.getETag());
    Log.d("RequestId", putResult.getRequestId());
} catch (ClientException e) {
    // 客户端异常，例如网络异常等。
    e.printStackTrace();
} catch (ServiceException e) {
    // 服务端异常。
    Log.e("RequestId", e.getRequestId());
    Log.e("ErrorCode", e.getErrorCode());
    Log.e("HostId", e.getHostId());
    Log.e("RawMessage", e.getRawMessage());
}
```

调用异步接口上传
说明 
在Android中，只能在子线程调用、而不能在UI线程调用同步接口，否则将出现异常。如果希望直接在UI线程中上传，请使用异步接口。

以下代码用于以异步方式上传examplefile.txt文件到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件。

```
// 构造上传请求。
// 依次填写Bucket名称（例如examplebucket）、Object完整路径（例如exampledir/exampleobject.txt）和本地文件完整路径（例如/storage/emulated/0/oss/examplefile.txt）。
// Object完整路径中不能包含Bucket名称。
PutObjectRequest put = new PutObjectRequest("examplebucket", "exampledir/exampleobject.txt", "/storage/emulated/0/oss/examplefile.txt");

// 异步上传时可以设置进度回调。
put.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(PutObjectRequest request, long currentSize, long totalSize) {
        Log.d("PutObject", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

OSSAsyncTask task = oss.asyncPutObject(put, new OSSCompletedCallback() {
    @Override
    public void onSuccess(PutObjectRequest request, PutObjectResult result) {
        Log.d("PutObject", "UploadSuccess");
        Log.d("ETag", result.getETag());
        Log.d("RequestId", result.getRequestId());
    }

    @Override
    public void onFailure(PutObjectRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 请求异常。
        if (clientExcepion != null) {
            // 客户端异常，例如网络异常等。
            clientExcepion.printStackTrace();
        }
        if (serviceException != null) {
            // 服务端异常。
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
// 取消上传任务。
// task.cancel(); 
// 等待上传任务完成。
// task.waitUntilFinished(); 
```

对于Android10及以上版本的分区存储，您可以使用文件的Uri上传文件到OSS。

```
// 构造上传请求。
// 依次填写Bucket名称（例如examplebucket）和Object完整路径（例如exampledir/exampleobject.txt）。
// Object完整路径中不能包含Bucket名称。
PutObjectRequest put = new PutObjectRequest("examplebucket", "exampledir/exampleobject.txt", fileUri);

// 异步上传时可以设置进度回调。
put.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(PutObjectRequest request, long currentSize, long totalSize) {
        Log.d("PutObject", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

OSSAsyncTask task = oss.asyncPutObject(put, new OSSCompletedCallback() {
    @Override
    public void onSuccess(PutObjectRequest request, PutObjectResult result) {
        Log.d("PutObject", "UploadSuccess");
        Log.d("ETag", result.getETag());
        Log.d("RequestId", result.getRequestId());
    }

    @Override
    public void onFailure(PutObjectRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 请求异常。
        if (clientExcepion != null) {
            // 客户端异常，例如网络异常等。
            clientExcepion.printStackTrace();
        }
        if (serviceException != null) {
            // 服务端异常。
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
// 取消上传任务。
// task.cancel(); 
// 等待上传任务完成。
// task.waitUntilFinished(); 
```

## 上传二进制byte[]数组

以下代码用于以同步方式上传二进制byte[]数组到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件。

```
byte[] uploadData = new byte[100 * 1024];
new Random().nextBytes(uploadData);

// 构造上传请求。
// 依次填写Bucket名称（例如examplebucket）和Object完整路径（例如exampledir/exampleobject.txt）。
// Object完整路径中不能包含Bucket名称。
PutObjectRequest put = new PutObjectRequest("examplebucket", "exampledir/exampleobject.txt", uploadData);

try {
    PutObjectResult putResult = oss.putObject(put);

    Log.d("PutObject", "UploadSuccess");
    Log.d("ETag", putResult.getETag());
    Log.d("RequestId", putResult.getRequestId());
} catch (ClientException e) {
    // 客户端异常，例如网络异常等。
    e.printStackTrace();
} catch (ServiceException e) {
    // 服务端异常。
    Log.e("RequestId", e.getRequestId());
    Log.e("ErrorCode", e.getErrorCode());
    Log.e("HostId", e.getHostId());
    Log.e("RawMessage", e.getRawMessage());
}
```

## 相关文档
- 关于简单上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/OSSPutObjectTest.java)。
- 关于简单上传的API接口说明，请参见[PutObject](https://help.aliyun.com/zh/oss/developer-reference/putobject#reference-l5p-ftw-tdb)。
- 关于初始化OSSClient，请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

[上一篇：上传文件（Android SDK）](/zh/oss/developer-reference/upload-objects-1/)[下一篇：追加上传（Android SDK）](/zh/oss/developer-reference/append-upload-5)该文章对您有帮助吗？反馈
  
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[通义大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证： [浙B2-20080101](http://beian.miit.gov.cn/) 域名注册服务机构许可： [浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[](https://zzlz.gsxt.gov.cn/businessCheck/verifKey.do?showType=p&serial=91330106673959654P-SAIC_SHOW_10000091330106673959654P1710919400712&signData=MEUCIQDEkCd8cK7%2Fyqe6BNMWvoMPtAnsgKa7FZetfPkjZMsvhAIgOX1G9YC6FKyndE7o7hL0KaBVn4f%20V%2Fiof3iAgpsV09o%3D)[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)