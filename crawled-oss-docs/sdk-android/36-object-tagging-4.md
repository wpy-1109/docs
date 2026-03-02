# 使用Android SDK设置获取和删除Object标签

Source: https://help.aliyun.com/zh/oss/developer-reference/object-tagging-4

---

- 使用Android SDK设置获取和删除Object标签-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 对象标签（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS支持使用标签对存储空间（Bucket）中的文件（Object）进行分类。本文介绍如何设置、获取以及删除Object标签。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

## 设置对象标签

### 上传Object时设置对象标签
说明 
上传文件时，如果配置的路径下已存在同名的文件，则原文件会被新上传的文件覆盖；如果不想覆盖同名文件，可以通过配置相应参数实现，具体请参考[禁止覆盖同名文件（Android SDK）](https://help.aliyun.com/zh/oss/developer-reference/prevent-objects-from-being-overwritten-by-objects-with-the-same-names-1)。

以下代码用于上传Object时设置对象标签。

```
// 构造上传请求。
// 依次填写Bucket名称（例如examplebucket）、Object完整路径（例如exampledir/exampleobject.txt）和本地文件完整路径（例如/storage/emulated/0/oss/examplefile.txt）。
// Object完整路径中不能包含Bucket名称。
PutObjectRequest put = new PutObjectRequest("examplebucket", "exampledir/exampleobject.txt", "/storage/emulated/0/oss/examplefile.txt");
Map tags = new HashMap();
// 设置标签信息。
tags.put("key1", "value1");
tags.put("Key2", "value2");
String tagHeader = OSSUtils.paramToQueryString(tags, "UTF-8");

ObjectMetadata metadata = new ObjectMetadata();
metadata.setHeader("x-oss-tagging", tagHeader);
put.setMetadata(metadata);

// 异步上传时支持设置进度回调。
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
```

### 为已上传Object添加或更改对象标签

以下代码用于为已上传Object添加或更改对象标签。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";

Map tags = new HashMap();
// 设置标签信息。
tags.put("owner", "John");
tags.put("type", "document");

PutObjectTaggingRequest putObjectTaggingRequest = new PutObjectTaggingRequest(bucketName, objectName, tags);
oss.asyncPutObjectTagging(putObjectTaggingRequest, new OSSCompletedCallback() {
    @Override
    public void onSuccess(PutObjectTaggingRequest request, PutObjectTaggingResult result) {
        Log.d("PutTagging", "PutTaggingSuccess");
    }

    @Override
    public void onFailure(PutObjectTaggingRequest request, ClientException clientException, ServiceException serviceException) {
        // 请求异常。
        if (clientException != null) {
            // 客户端异常，例如网络异常等。
            clientException.printStackTrace();
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
```

### 拷贝Object时设置对象标签

以下代码用于拷贝Object时设置对象标签。

```
// 创建CopyObject请求。
// 依次填写Bucket名称（例如examplebucket）、Object完整路径（例如exampledir/exampleobject.txt）、目标Bucket名称（例如destexamplebucket）、目标Object完整路径（例如destexampledir/exampleobject.txt）。
// Object完整路径中不能包含Bucket名称。
CopyObjectRequest copyObjectRequest = new CopyObjectRequest("examplebucket", "exampledir/exampleobject.txt",
        "destexamplebucket", "destexampledir/exampleobject.txt");
ObjectMetadata objectMetadata = new ObjectMetadata();
Map tags = new HashMap();
// 设置目标Object的标签信息。
tags.put("key1", "value1");
tags.put("key2", "value2");
String tagHeader = OSSUtils.paramToQueryString(tags, "UTF-8");
objectMetadata.setHeader("x-oss-tagging", tagHeader);
// 忽略源Object的标签，直接采用请求中指定的标签信息。
objectMetadata.setHeader("x-oss-tagging-directive", "REPLACE");
copyObjectRequest.setNewObjectMetadata(objectMetadata);

OSSAsyncTask copyTask = oss.asyncCopyObject(copyObjectRequest, new OSSCompletedCallback() {
    @Override
    public void onSuccess(CopyObjectRequest request, CopyObjectResult result) {
        Log.d("copyObject", "copy success!");
    }

    @Override
    public void onFailure(CopyObjectRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 请求异常。
        if (clientExcepion != null) {
            // 客户端异常，例如网络异常等。
            clientExcepion.printStackTrace();
        }
        if (serviceException != null) {
            // 服务异常。
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
```

### 为软链接文件设置对象标签

以下代码用于为软链接文件设置对象标签。

```
PutSymlinkRequest putSymlink = new PutSymlinkRequest();
// 填写Bucket名称，例如examplebucket。
putSymlink.setBucketName("examplebucket");
// 设置软链接文件名。
putSymlink.setObjectKey("yourSymLink");
// 设置目标文件名。
putSymlink.setTargetObjectName("yourTargetObjectName");

Map tags = new HashMap();
// 设置标签信息。
tags.put("key1", "value1");
tags.put("key2", "value2");
String tagHeader = OSSUtils.paramToQueryString(tags, "UTF-8");
ObjectMetadata metadata = new ObjectMetadata();
metadata.setHeader("x-oss-tagging", tagHeader);
putSymlink.setMetadata(metadata);

OSSAsyncTask task = oss.asyncPutSymlink(putSymlink, new OSSCompletedCallback() {
    @Override
    public void onSuccess(PutSymlinkRequest request, PutSymlinkResult result) {
        OSSLog.logInfo("code:"+result.getStatusCode());

    }

    @Override
    public void onFailure(PutSymlinkRequest request, ClientException clientException,
                          ServiceException serviceException) {
        OSSLog.logError("error: "+serviceException.getRawMessage());

    }
});
```

## 获取Object标签信息

以下代码用于获取Object的标签信息。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 获取Object的标签信息。
GetObjectTaggingRequest getObjectTaggingRequest = new GetObjectTaggingRequest(bucketName, objectName);
oss.asyncGetObjectTagging(getObjectTaggingRequest, new OSSCompletedCallback() {
    @Override
    public void onSuccess(GetObjectTaggingRequest request, GetObjectTaggingResult result) {
        for (Map.Entry s : result.getTags().entrySet()) {
            Log.d("tag", "key: " + s.getKey() + ", value: " + s.getValue());
        }
    }

    @Override
    public void onFailure(GetObjectTaggingRequest request, ClientException clientException, ServiceException serviceException) {
        // 请求异常。
        if (clientException != null) {
            // 客户端异常，例如网络异常等。
            clientException.printStackTrace();
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
```

## 删除Object标签信息

以下代码用于删除Object的标签信息。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 删除Object的标签信息。
DeleteObjectTaggingRequest deleteObjectTaggingRequest = new DeleteObjectTaggingRequest(bucketName, objectName);
oss.asyncDeleteObjectTagging(deleteObjectTaggingRequest, new OSSCompletedCallback() {
    @Override
    public void onSuccess(DeleteObjectTaggingRequest request, DeleteObjectTaggingResult result) {
        Log.d("deleteTagging", "deleteTagging success");
    }

    @Override
    public void onFailure(DeleteObjectTaggingRequest request, ClientException clientException, ServiceException serviceException) {
        // 请求异常。
        if (clientException != null) {
            // 客户端异常，例如网络异常等。
            clientException.printStackTrace();
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
```

## 相关文档
- 关于对象标签的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/ObjectTaggingTest.java)。
- 关于设置Object标签的API接口说明，请参见[PutObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/putobjecttagging#reference-185784)。
- 关于获取Object标签的API接口说明，请参见[GetObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/getobjecttagging#concept-185787)。
- 关于删除Object标签的API接口说明，请参见[DeleteObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/deleteobjecttagging#reference-185788)。
- 关于禁止覆盖同名文件，请参见[禁止覆盖同名文件（Android SDK）](https://help.aliyun.com/zh/oss/developer-reference/prevent-objects-from-being-overwritten-by-objects-with-the-same-names-1)。
- 关于初始化OSSClient，请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

[上一篇：获取文件元数据（Android SDK）](/zh/oss/developer-reference/query-object-metadata-5)[下一篇：解冻文件（Android SDK）](/zh/oss/developer-reference/restore-an-archive-object)该文章对您有帮助吗？反馈
  
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