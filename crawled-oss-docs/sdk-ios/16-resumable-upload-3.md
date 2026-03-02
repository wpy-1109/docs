# 使用iOS SDK实现大文件断点续传

Source: https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-3

---

- 使用iOS SDK实现大文件断点续传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 断点续传上传（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
在无线网络下，上传比较大的文件持续时间长，可能会遇到因为网络条件差、用户切换网络等原因导致上传中途失败，整个文件需要重新上传。为此，iOS SDK提供了断点续传上传功能。

## 背景信息

对于移动端而言，如果不是大文件（例如小于5 GB的文件），不建议使用断点续传的方式上传。断点续传上传是通过分片上传实现的，上传单个文件需要进行多次网络请求，效率不高。对于通过断点续传的方式上传大于5 GB的文件时：
- 断点续传上传前 通过断点续传上传的方式将文件上传到OSS前，您可以指定断点记录的保存文件夹。断点续传上传仅在本次上传生效。如果未指定断点记录的保存文件夹，假设某个分片因为网络原因等导致文件上传失败时，将耗用大量的重试时间及流量来重新上传整个大文件。
- 如果指定了断点记录的保存文件夹，在文件上传失败时，将从断点记录处继续上传未上传完成的部分。
- 断点续传上传时 断点续传上传仅支持上传本地文件。断点续传上传支持上传回调，使用方法与常见的上传回调类似。具体操作，请参见[Callback](https://help.aliyun.com/zh/oss/developer-reference/callback#reference-zkm-311-hgb)。
- 断点续传上传依赖InitMultipartUpload、UploadPart、ListParts、CompleteMultipartUpload、AbortMultipartUpload等接口来实现。如果您需要通过STS鉴权模式来使用断点续传上传，则需要保证您拥有访问以上API接口的权限。
- 断点续传上传默认已开启每个分片上传时的MD5校验，因此无需在请求中设置`Content-Md5`头部。
- 如果同一任务一直得不到续传，可能会在OSS上积累无用碎片。此时，您可以为Bucket设置lifeCycle规则的方式来定时清理碎片，详情请参见[生命周期管理](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。 重要 出于碎片管理的原因，如果在断点续传时取消当前上传任务，默认会同步清理已经上传到服务器的分片。取消上传任务时如果仍希望保留断点上传记录，则需要指定断点记录的保存文件夹并修改deleteUploadIdOnCancelling参数。如果服务端保留记录时间过长，且Bucket已设置lifeCycle规则定时清理了服务端分片，会出现服务端和移动端记录不一致的问题。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。说明 所创建存储空间的所属地域取决于初始化配置的endpoint地域信息。
- 要上传文件，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 示例代码
- 断点记录在本地持久保存时，调用`resumableUpload`方法实现断点续传上传的过程如下： 
```
OSSResumableUploadRequest * resumableUpload = [OSSResumableUploadRequest new];
resumableUpload.bucketName = OSS_BUCKET_PRIVATE;
//...
NSString *cachesDir = [NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES) firstObject];
resumableUpload.recordDirectoryPath = cachesDir;
                    
```
说明 使用断点续传上传文件失败时会生成断点记录文件，然后从断点记录处继续上传直到上传完成。上传成功后会自动删除断点记录文件，默认情况下不会在本地持久保存断点记录。
- 断点续传上传的完整示例代码如下： 
```
// 获取UploadId上传文件。
OSSResumableUploadRequest * resumableUpload = [OSSResumableUploadRequest new];
resumableUpload.bucketName = ;
// objectKey等同于objectName，表示断点上传文件到OSS时需要指定包含文件后缀在内的完整路径，例如abc/efg/123.jpg
resumableUpload.objectKey = ;
resumableUpload.partSize = 1024 * 1024;
resumableUpload.uploadProgress = ^(int64_t bytesSent, int64_t totalByteSent, int64_t totalBytesExpectedToSend) {
    NSLog(@"%lld, %lld, %lld", bytesSent, totalByteSent, totalBytesExpectedToSend);
};
NSString *cachesDir = [NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES) firstObject];
// 设置断点记录保存路径。
resumableUpload.recordDirectoryPath = cachesDir;
// 将参数deleteUploadIdOnCancelling设置为NO，表示不删除断点记录文件，上传失败后将从断点记录处继续上传直到文件上传完成。如果不设置此参数，即保留默认值YES，表示删除断点记录文件，下次再上传同一文件时则重新上传。
resumableUpload.deleteUploadIdOnCancelling = NO;

resumableUpload.uploadingFileURL = [NSURL fileURLWithPath:];
OSSTask * resumeTask = [client resumableUpload:resumableUpload];
[resumeTask continueWithBlock:^id(OSSTask *task) {
    if (task.error) {
        NSLog(@"error: %@", task.error);
        if ([task.error.domain isEqualToString:OSSClientErrorDomain] && task.error.code == OSSClientErrorCodeCannotResumeUpload) {
            // 此任务无法续传，需获取新的uploadId重新上传。
        }
    } else {
        NSLog(@"Upload file success");
    }
    return nil;
}];

// [resumeTask waitUntilFinished];

// [resumableUpload cancel];
                    
```

[上一篇：追加上传（iOS SDK）](/zh/oss/developer-reference/append-upload-7)[下一篇：上传回调（iOS SDK）](/zh/oss/developer-reference/upload-callbacks-7)该文章对您有帮助吗？反馈
  
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