# 前言（C++ SDK）

Source: https://help.aliyun.com/zh/oss/developer-reference/introduction-4

---

- 前言（C++ SDK）-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 前言（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文档基于C++ SDK 1.9.1版本编写。

## SDK 源码

SDK源码请参见[GitHub](https://github.com/aliyun/aliyun-oss-cpp-sdk)。

## 示例代码

OSS C++ SDK提供丰富的示例代码，方便您参考或直接使用。示例代码包括以下内容：
| 示例文件 | 示例内容|
| [PutObjectFromFile ](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L81) | [上传文件 ](https://help.aliyun.com/zh/oss/developer-reference/overview-67#concept-32136-zh)|
| [GetObjectToFile](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L106) | [ 下载文件](https://help.aliyun.com/zh/oss/developer-reference/overview-69#concept-32137-zh)|
| [ AppendObject](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L258) | [追加上传（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-9#concept-90215-zh)|
| [MultipartUploadObject](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L542) | [分片上传（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-9#concept-90222-zh)|
| [HeadObject ](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L206) | [管理文件元数据（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/manage-object-metadata-5#concept-90504-zh)|
| [ListObjects](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/bucket/BucketSample.cc#L261) | [列举文件（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/list-objects-11#concept-jds-yrl-ngb)|
| [CopyObject](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L632) | [拷贝文件](https://help.aliyun.com/zh/oss/developer-reference/copy-objects-10#concept-fbl-yql-ngb)|
| [DeleteObject ](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L119) | [删除文件（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/delete-objects-10#concept-flf-frl-ngb)|
| [PutObjectProgress](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L318) | [进度条上传](https://help.aliyun.com/zh/oss/developer-reference/progress-bar-5#concept-90225-zh)|
| [DownloadObjectProcess](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L414) | [进度条下载](https://help.aliyun.com/zh/oss/developer-reference/progress-bar-2#concept-90284-zh)|
| [RestoreArchiveObject](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc#L598) | [解冻归档文件](https://help.aliyun.com/zh/oss/developer-reference/restore-objects-8#concept-90491-zh)|
| [BucketSample.cc](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/master/sample/src/bucket/BucketSample.cc) | 设置存储空间的[静态网站托管（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/static-website-hosting-9#concept-xmv-ggl-ngb)、[CORS](https://help.aliyun.com/zh/oss/developer-reference/cors-10#concept-89705-zh)、[生命周期（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/lifecycle-5#concept-32140-zh)、[访问日志](https://help.aliyun.com/zh/oss/developer-reference/logging-10#concept-89684-zh)、[授权访问（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/authorized-access-4#concept-32139-zh)等|
| [ObjectTrafficLimitTest.cc](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/master/test/src/Object/ObjectTrafficLimitTest.cc) | 设置上传、下载文件时的[单链接限速（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/single-connection-bandwidth-throttling-6#concept-1614726)|
| [ObjectRequestPaymentTest.cc](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/master/test/src/Object/ObjectRequestPaymentTest.cc) | 存储空间的[请求者付费模式（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/pay-by-requester-2#concept-944152)|
| [ObjectTaggingTest.cc](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/master/test/src/Object/ObjectTaggingTest.cc) | [设置](https://help.aliyun.com/zh/oss/developer-reference/configure-object-tagging-4#concept-727372)、[获取](https://help.aliyun.com/zh/oss/developer-reference/query-the-tags-of-an-object-2#concept-727373)、[删除](https://help.aliyun.com/zh/oss/developer-reference/delete-object-tags-2#concept-727374)对象标签以及[对象标签和生命周期管理（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/object-tagging-and-lifecycle-management-1#concept-727376)|

[上一篇：OSS C++ SDK](/zh/oss/developer-reference/cpp/)[下一篇：安装（C++ SDK）](/zh/oss/developer-reference/installation-12)该文章对您有帮助吗？反馈
  
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