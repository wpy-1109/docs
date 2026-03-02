# Android SDK管理Bucket访问日志转存

Source: https://help.aliyun.com/zh/oss/developer-reference/logging-14

---

- Android SDK管理Bucket访问日志转存-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 日志转存（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
访问OSS的过程中会产生大量的访问日志。您可以通过日志转存功能将这些日志按照固定命名规则，以小时为单位生成日志文件写入您指定的存储空间（Bucket）。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。
说明 
调用日志转存开启或关闭接口成功后需要刷新页面才能看到成功开启转存，只是切换页签无法看到正确信息，请注意。

## 开启日志转存

以下代码用于开启日志转存功能。

```
PutBucketLoggingRequest request = new PutBucketLoggingRequest();
// 指定要开启访问日志记录的源Bucket。
request.setBucketName("yourSourceBucketName");
// 指定存储访问日志的目标Bucket。
// 目标Bucket和源Bucket必须属于同一地域。源Bucket和目标Bucket可以是同一个Bucket，也可以是不同的Bucket。
request.setTargetBucketName("yourTargetBucketName");
// 设置日志文件存放的目录。
request.setTargetPrefix("");

OSSAsyncTask task = oss.asyncPutBucketLogging(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(PutBucketLoggingRequest request, PutBucketLoggingResult result) {
        OSSLog.logInfo("code::"+result.getStatusCode());
    }

    @Override
    public void onFailure(PutBucketLoggingRequest request, ClientException clientException, ServiceException serviceException) {
         OSSLog.logError("error: "+serviceException.getRawMessage());
    }
});
task.waitUntilFinished();
```

## 查看日志转存配置

以下代码用于查看日志转存配置。
说明 
调用成功后输出结果格式为“testBucket*path”，其中"*"之前的"testBucket"为桶名，之后的"path"为存储路径

```
GetBucketLoggingRequest request = new GetBucketLoggingRequest();
request.setBucketName("yourSourceBucketName");
OSSAsyncTask task = oss.asyncGetBucketLogging(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(GetBucketLoggingRequest request, GetBucketLoggingResult result) {
        Log.i("i", "info: " + result.getTargetBucketName()+"*"+result.getTargetPrefix());

    }

    @Override
    public void onFailure(GetBucketLoggingRequest request, ClientException clientException, ServiceException serviceException) {
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
task.waitUntilFinished();
```

## 关闭日志转存

以下代码用于关闭日志转存功能。

```
DeleteBucketLoggingRequest request = new DeleteBucketLoggingRequest();
request.setBucketName("yourSourceBucketName");
OSSAsyncTask task = oss.asyncDeleteBucketLogging(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(DeleteBucketLoggingRequest request, DeleteBucketLoggingResult result) {
        Log.i("i", "code:"+result.getStatusCode());

    }

    @Override
    public void onFailure(DeleteBucketLoggingRequest request, ClientException clientException, ServiceException serviceException) {
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

task.waitUntilFinished();
            
```

## 相关文档
- 关于日志转存的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/OSSBucketTest.java)。
- 关于开启日志转存功能的API接口说明，请参见[PutBucketLogging](https://help.aliyun.com/zh/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)。
- 关于查看日志转存配置的API接口说明，请参见[GetBucketLogging](https://help.aliyun.com/zh/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)。
- 关于关闭日志转存功能的API接口说明，请参见[DeleteBucketLogging](https://help.aliyun.com/zh/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)。
- 关于初始化OSSClient，请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

[上一篇：生命周期（Android SDK）](/zh/oss/developer-reference/manage-lifecycle-rules-4)[下一篇：图片处理（Android SDK）](/zh/oss/developer-reference/img-1)该文章对您有帮助吗？反馈
  
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