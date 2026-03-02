# 使用Android SDK实现断点续传上传本地文件

Source: https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-4

---

- 使用Android SDK实现断点续传上传本地文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 断点续传上传（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
在无线网络下，上传较大的文件持续时间长，可能会遇到因为网络条件差、用户切换网络等原因导致上传中途失败，整个文件需要重新上传。为此，Android SDK提供了断点续传上传功能。

## 使用说明

Android SDK提供了resumableUpload以及sequenceUpload两种方法用于断点续传上传。
- （推荐）resumableUpload表示并发上传分片，即同时支持最多5个分片并发上传。
- sequenceUpload表示顺序上传分片，即上一个分片上传完成后开始上传下一个分片。

以下示例代码仅提供通过resumableUpload的方法断点续传上传。如果您希望通过断点续传的方式上传多个文件或视频，需创建多个ResumableUploadRequest。

## 注意事项

使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

对于移动端而言，如果不是大文件（例如小于5 GB的文件），不建议使用断点续传的方式上传。断点续传上传是通过分片上传实现的，上传单个文件需要进行多次网络请求，效率不高。对于通过断点续传的方式上传大于5 GB的文件时：
- 断点续传上传前 通过断点续传上传的方式将文件上传到OSS前，您可以指定断点记录的保存文件夹。断点续传上传仅在本次上传生效。如果未指定断点记录的保存文件夹，假设某个分片因为网络原因等导致文件上传失败时，将耗用大量的重试时间及流量来重新上传整个大文件。
- 如果指定了断点记录的保存文件夹，在文件上传失败时，将从断点记录处继续上传未上传完成的部分。
- 断点续传上传时 断点续传上传仅支持上传本地文件。断点续传上传支持上传回调，使用方法与常见的上传回调类似。具体操作，请参见[Callback](https://help.aliyun.com/zh/oss/developer-reference/callback#reference-zkm-311-hgb)。
- 断点续传上传依赖InitMultipartUpload、UploadPart、ListParts、CompleteMultipartUpload、AbortMultipartUpload等接口来实现。如果您需要通过STS鉴权模式来使用断点续传上传，则需要保证您拥有访问以上API接口的权限。
- 断点续传上传默认已开启每个分片上传时的MD5校验，因此无需在请求中设置`Content-Md5`头部。
- 如果同一任务一直未完成续传，可能会在OSS上积累无用的碎片。此时，您可以为Bucket设置生命周期规则来定时清理碎片。具体操作，请参见[生命周期管理](https://help.aliyun.com/zh/oss/configure-lifecycle-rules#concept-bmx-p2f-vdb)。

## 示例代码

您可以通过同步或者异步方式断点续传上传本地文件到OSS。

同步的方式

以下代码以同步的方式断点续传上传examplefile.txt文件到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件，并将断点记录文件保存到本地。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";

String recordDirectory = Environment.getExternalStorageDirectory().getAbsolutePath() + "/oss_record/";

File recordDir = new File(recordDirectory);

// 确保断点记录的保存文件夹已存在，如果不存在则新建断点记录的保存文件夹。
if (!recordDir.exists()) {
    recordDir.mkdirs();
}

// 创建断点续传上传请求，并指定断点记录文件的保存路径，保存路径为断点记录文件的绝对路径。
ResumableUploadRequest request = new ResumableUploadRequest(bucketName, objectName, localFilepath, recordDirectory);
// 调用OSSAsyncTask cancel()方法时，设置DeleteUploadOnCancelling为false，表示不删除断点记录文件，下次再上传同一个文件时将从断点记录处继续上传。如果不设置此参数，则默认值为true，表示删除断点记录文件，下次再上传同一个文件时则重新上传。
request.setDeleteUploadOnCancelling(false);
// 设置上传回调。
request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(ResumableUploadRequest request, long currentSize, long totalSize) {
        Log.d("resumableUpload", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

ResumableUploadResult uploadResult = oss.resumableUpload(request);
```

对于Android10及之后版本的分区存储，您可以使用文件的Uri上传文件到OSS。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";

String recordDirectory = getApplication().getFilesDir().getAbsolutePath() + "/oss_record/";

File recordDir = new File(recordDirectory);

// 确保断点记录的保存文件夹已存在，如果不存在则新建断点记录的保存文件夹。
if (!recordDir.exists()) {
    recordDir.mkdirs();
}

// 创建断点续传上传请求，并指定断点记录文件的保存路径，保存路径为断点记录文件的绝对路径。
// 这里参数"fileUri"需要填入文件的实际Uri值。
ResumableUploadRequest request = new ResumableUploadRequest(bucketName, objectName, fileUri, recordDirectory);
// 调用OSSAsyncTask cancel()方法时，设置DeleteUploadOnCancelling为false，表示不删除断点记录文件，下次再上传同一个文件时将从断点记录处继续上传。如果不设置此参数，则默认值为true，表示删除断点记录文件，下次再上传同一个文件时则重新上传。
request.setDeleteUploadOnCancelling(false);
// 设置上传回调。
request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(ResumableUploadRequest request, long currentSize, long totalSize) {
        Log.d("resumableUpload", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

ResumableUploadResult uploadResult = oss.resumableUpload(request);
```

如果在断点续传上传时无需将断点记录文件保存到本地，示例代码如下：

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";

// 创建断点续传上传请求。
ResumableUploadRequest request = new ResumableUploadRequest(bucketName, objectName, localFilepath);
// 设置上传回调。
request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(ResumableUploadRequest request, long currentSize, long totalSize) {
        Log.d("resumableUpload", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

ResumableUploadResult uploadResult = oss.resumableUpload(request);
```

异步的方式

以下代码以异步的方式断点续传上传examplefile.txt文件到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件，并将断点记录文件保存到本地。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";
String recordDirectory = Environment.getExternalStorageDirectory().getAbsolutePath() + "/oss_record/";

File recordDir = new File(recordDirectory);

// 确保断点记录的保存路径已存在，如果不存在则新建断点记录的保存路径。
if (!recordDir.exists()) {
    recordDir.mkdirs();
}

// 创建断点上传请求，并指定断点记录文件的保存路径，保存路径为断点记录文件的绝对路径。
ResumableUploadRequest request = new ResumableUploadRequest(bucketName, objectName, localFilepath, recordDirectory);
// 调用OSSAsyncTask cancel()方法时，设置DeleteUploadOnCancelling为false，表示不删除断点记录文件，下次再上传同一个文件时将从断点记录处继续上传。如果不设置此参数，则默认值为true，表示删除断点记录文件，下次再上传同一个文件时则重新上传。
request.setDeleteUploadOnCancelling(false);
// 设置上传过程回调。
request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(ResumableUploadRequest request, long currentSize, long totalSize) {
        Log.d("resumableUpload", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

OSSAsyncTask resumableTask = oss.asyncResumableUpload(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(ResumableUploadRequest request, ResumableUploadResult result) {
        Log.d("resumableUpload", "success!");
    }

    @Override
    public void onFailure(ResumableUploadRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 异常处理。
    }
});

// 等待完成断点上传任务。
resumableTask.waitUntilFinished();                
```

对于Android10及之后版本的分区存储，您可以使用文件的Uri上传文件到OSS。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
String recordDirectory = getApplication().getFilesDir().getAbsolutePath() + "/oss_record/";

File recordDir = new File(recordDirectory);

// 确保断点记录的保存文件夹已存在，如果不存在则新建断点记录的保存文件夹。
if (!recordDir.exists()) {
    recordDir.mkdirs();
}

// 创建断点续传上传请求，并指定断点记录文件的保存路径，保存路径为断点记录文件的绝对路径。
// 这里参数"fileUri"需要填入文件的实际Uri值。
ResumableUploadRequest request = new ResumableUploadRequest(bucketName, objectName, fileUri, recordDirectory);
// 调用OSSAsyncTask cancel()方法时，设置DeleteUploadOnCancelling为false时，表示不删除断点记录文件，下次再上传同一个文件时将从断点记录处继续上传。如果不设置此参数，则默认值为true，表示删除断点记录文件，下次再上传同一个文件时则重新上传。
request.setDeleteUploadOnCancelling(false);
// 设置上传回调。
request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(ResumableUploadRequest request, long currentSize, long totalSize) {
        Log.d("resumableUpload", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

OSSAsyncTask resumableTask = oss.asyncResumableUpload(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(ResumableUploadRequest request, ResumableUploadResult result) {
        Log.d("resumableUpload", "success!");
    }

    @Override
    public void onFailure(ResumableUploadRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 异常处理。
    }
});

// 等待完成断点上传任务。
resumableTask.waitUntilFinished();
```

如果在断点续传上传时无需将断点记录文件保存到本地，示例代码如下：

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";

// 创建断点上传请求。
ResumableUploadRequest request = new ResumableUploadRequest(bucketName, objectName, localFilepath);

// 设置上传过程回调。
request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(ResumableUploadRequest request, long currentSize, long totalSize) {
        Log.d("resumableUpload", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});
// 异步调用断点上传。
OSSAsyncTask resumableTask = oss.asyncResumableUpload(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(ResumableUploadRequest request, ResumableUploadResult result) {
        Log.d("resumableUpload", "success!");
    }

    @Override
    public void onFailure(ResumableUploadRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 异常处理。
    }
});

// 等待完成断点上传任务。
resumableTask.waitUntilFinished();                     
```

## 相关文档
- 关于Bucket设置生命周期规则，请参见[生命周期管理](https://help.aliyun.com/zh/oss/configure-lifecycle-rules#concept-bmx-p2f-vdb)。
- 关于断点续传上传支持上传回调使用方法，请参见[Callback](https://help.aliyun.com/zh/oss/developer-reference/callback#reference-zkm-311-hgb)。
- 关于初始化OSSClient，请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

[上一篇：分片上传（Android SDK）](/zh/oss/developer-reference/multipart-upload-6)[下一篇：进度条（Android SDK）](/zh/oss/developer-reference/progress-bar-7)该文章对您有帮助吗？反馈
  
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