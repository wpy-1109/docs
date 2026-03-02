# 文件数据存储管理处理

Source: https://help.aliyun.com/zh/oss/developer-reference/preface-4/

---

- 文件数据存储管理处理-OSS C# SDK V1-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# OSS C# SDK V1
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS C# SDK适用于 .NET Framework 2.0及以上版本。本文档基于OSS C# SDK 2.8.0编写。

兼容性
- 对于2.x.x 系列SDK：接口：兼容。
- 命名空间：兼容。
- 对于1.0.x 系列SDK：接口：兼容。
- 命名空间：不兼容。Aliyun.OpenServices.OpenStorageService变更为Aliyun.OSS。

## SDK源码和API文档

SDK源码请参见GitHub地址：[GitHub](https://github.com/aliyun/aliyun-oss-csharp-sdk)。更多信息请参见[API Doc](http://gosspublic.alicdn.com/AliyunNetSDK/apidocs/latest/index.html)。

## 示例代码

OSS C# SDK提供丰富的示例代码。您可以从[GitHub](https://github.com/aliyun/aliyun-oss-csharp-sdk/tree/master/samples/Samples)获取示例代码。示例代码包括以下内容：
| 示例文件 | 示例内容|
| [PutObjectSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/PutObjectSample.cs) | [上传文件](https://help.aliyun.com/zh/oss/overview-41#concept-32090-zh)|
| [AppendObjectSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/AppendObjectSample.cs) | [追加上传](https://help.aliyun.com/zh/oss/developer-reference/append-upload-10#concept-91099-zh)|
| [DoesObjectExistSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/DoesObjectExistSample.cs) | [判断文件是否存在](https://help.aliyun.com/zh/oss/developer-reference/determine-whether-an-object-exists-using-oss-sdk-for-csharp-v1#concept-91918-zh)|
| [DeleteObjectsSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/DeleteObjectsSample.cs) | [删除文件](https://help.aliyun.com/zh/oss/developer-reference/delete-objects-16#concept-91924-zh)|
| [CopyObjectSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/CopyObjectSample.cs) | [拷贝文件](https://help.aliyun.com/zh/oss/developer-reference/copy-objects-using-oss-sdk-for-csharp-v1#concept-91925-zh)|
| [ModifyObjectMetaSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ModifyObjectMetaSample.cs) | [管理文件元数据](https://help.aliyun.com/zh/oss/developer-reference/manage-object-metadata-8#concept-91920-zh)|
| [MultipartUploadSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/MultipartUploadSample.cs) | [分片上传](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-10#concept-91103-zh)|
| [ResumableSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ResumableSample.cs) | [断点续传上传](https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-8#concept-91101-zh)|
| [GetObjectSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/GetObjectSample.cs) | [下载文件](https://help.aliyun.com/zh/oss/overview-42#concept-32091-zh)|
| [GetObjectByRangeSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/GetObjectByRangeSample.cs) | [范围下载](https://help.aliyun.com/zh/oss/developer-reference/range-download-4#concept-91750-zh)|
| [GetObjectAclSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/GetObjectAclSample.cs) | [管理文件访问权限](https://help.aliyun.com/zh/oss/developer-reference/manage-object-acls-13#concept-91919-zh)|
| [SetObjectAclSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetObjectAclSample.cs) | [管理文件访问权限](https://help.aliyun.com/zh/oss/developer-reference/manage-object-acls-13#concept-91919-zh)|
| [ListObjectsSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ListObjectsSample.cs) | [列举文件](https://help.aliyun.com/zh/oss/developer-reference/list-objects-15#concept-91923-zh)|
| [UrlSignatureSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/UrlSignatureSample.cs) | [使用预签名URL上传](https://help.aliyun.com/zh/oss/developer-reference/upload-objects-using-presigned-urls-generated-with-sdk-for-net#concept-32093-zh)|
| [UploadCallbackSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/UploadCallbackSample.cs) | [上传回调](https://help.aliyun.com/zh/oss/developer-reference/upload-callbacks-9#concept-91107-zh)|
| [ProgressSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ProgressSample.cs) | [上传进度条](https://help.aliyun.com/zh/oss/developer-reference/progress-bars-6#concept-91108-zh)和[下载进度条](https://help.aliyun.com/zh/oss/developer-reference/progress-bars-3#concept-91759-zh)|
| [CNameSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/CNameSample.cs) | 使用自定义域名访问OSS（CNAME）|
| [PostPolicySample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/PostPolicySample.cs) | [表单上传](https://help.aliyun.com/zh/oss/developer-reference/postobject#reference-smp-nsw-wdb)|
| [CreateBucketSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/CreateBucketSample.cs) | [创建存储空间](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#section-s5m-v12-lfb)|
| [DeleteBucketSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/DeleteBucketSample.cs) | [删除存储空间](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#concept-32089-zh)|
| [DoesBucketExistSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/DoesBucketExistSample.cs) | [判断存储空间是否存在](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#concept-32089-zh)|
| [ListBucketsSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ListBucketsSample.cs) | [列举存储空间](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#concept-32089-zh)|
| [SetBucketAclSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetBucketAclSample.cs) | [设置存储空间的访问权限](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v1#concept-32089-zh)|
| [SetBucketLifecycleSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetBucketLifecycleSample.cs) | [生命周期](https://help.aliyun.com/zh/oss/developer-reference/lifecycle-rules-2#concept-32094-zh)|
| [SetBucketLoggingSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetBucketLoggingSample.cs) | [访问日志](https://help.aliyun.com/zh/oss/developer-reference/logging-2#concept-48308-zh)|
| [SetBucketRefererSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetBucketRefererSample.cs) | [防盗链](https://help.aliyun.com/zh/oss/developer-reference/dotnet-hotlink-protection#concept-32096-zh)|
| [SetBucketWetbsiteSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetBucketWetbsiteSample.cs) | [静态网站托管](https://help.aliyun.com/zh/oss/developer-reference/static-website-hosting#concept-90311-zh)|
| [SetBucketCorsSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/SetBucketCorsSample.cs) | [跨域资源共享](https://help.aliyun.com/zh/oss/developer-reference/cors-9#concept-32095-zh)|
| [ImageProcessSample.cs](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ImageProcessSample.cs) | [图片处理](https://help.aliyun.com/zh/oss/developer-reference/img-3#concept-48309-zh)|

## 后续参考
- [安装](https://help.aliyun.com/zh/oss/developer-reference/installation-oss-sdk-for-csharp-v1)
- [初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-ossclient)
- [配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-using-oss-sdk-for-csharp-v1)
- [快速入门](https://help.aliyun.com/zh/oss/developer-reference/quick-start-using-oss-sdk-for-csharp-v1)
- [存储空间](https://help.aliyun.com/zh/oss/developer-reference/manage-buckets-using-oss-sdk-for-csharp-v1/)
- [权限控制](https://help.aliyun.com/zh/oss/developer-reference/manage-acls-using-oss-sdk-for-csharp-v1/)
- [对象/文件](https://help.aliyun.com/zh/oss/developer-reference/perform-operations-on-objects-using-oss-sdk-for-csharp-v1/)
- [数据安全](https://help.aliyun.com/zh/oss/developer-reference/data-security-oss-sdk-for-csharp-v1/)
- [数据管理](https://help.aliyun.com/zh/oss/developer-reference/data-management-2/)
- [图片处理](https://help.aliyun.com/zh/oss/developer-reference/img-3)
- [异常处理](https://help.aliyun.com/zh/oss/developer-reference/exception-handling-2)

[上一篇：异步处理（C# SDK V2）](/zh/oss/developer-reference/asynchronous-processing-using-oss-sdk-for-csharp-v2)[下一篇：安装（C# SDK V1）](/zh/oss/developer-reference/installation-oss-sdk-for-csharp-v1)该文章对您有帮助吗？反馈
  
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