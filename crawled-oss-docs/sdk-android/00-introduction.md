# 安卓端对象存储文件管理

Source: https://help.aliyun.com/zh/oss/developer-reference/introduction/

---

- 安卓端对象存储文件管理-OSS Android SDK-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# OSS Android SDK
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文档基于OSS Android SDK 2.9.19编写。
说明 
OSS不支持Flutter SDK。

## 基本信息
| SDK名称 | 对象存储OSS Android SDK|
| 开发者 | 阿里云计算有限公司|
| SDK版本 | 2.9.21|
| SDK包名 | com.alibaba.sdk.android.oss|
| SDK更新时间 | 2024.11.29|
| SDK大小 | 312 KB|
| SDK MD5值 | e994864f851204b01e0346ff731f4172|
| 隐私政策 | [对象存储OSS隐私政策](https://terms.alicdn.com/legal-agreement/terms/privacy_policy_full/20240202100310511/20240202100310511.html)|
| SDK下载 | [oss-android-sdk-2.9.21.aar](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241211/ksiida/oss-android-sdk-2.9.21.aar)|

## 版本说明

在下载OSS Android SDK之前，请选择合适的版本。OSS通过MVNRepository管理开放的下载源码路径并提供GitHub的源代码参考。
| 来源 | 描述|
| MVNRepository | 用于下载OSS源码包的路径。您可以在MVNRepository中获取Gradle项目注入OSS Android SDK依赖的准确版本。
说明 
建议您获取OSS Android SDK的最新版本进行调试，避免报错。

更多信息，请参见[Aliyun OSS Android SDK](https://mvnrepository.com/artifact/com.aliyun.dpa/oss-android-sdk)。|
| GitHub | 用于记录GitHub源码发布版本的标签信息。您可以在GitHub上浏览源代码并查看丰富的代码示例。更多信息，请参见[Aliyun OSS Android SDK Release](https://mvnrepository.com/artifact/com.aliyun.dpa/oss-android-sdk)。|

## 兼容性

Android SDK具有向下兼容的特性，新版本完全兼容老版本。

## SDK源码

SDK源码请参见[GitHub](https://github.com/aliyun/aliyun-oss-android-sdk)。

## 示例代码

OSS Android SDK提供丰富的示例代码，方便您参考或直接使用。

示例代码包括以下内容：
| 示例文件 | 示例内容|
| [BaseTestCase.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/BaseTestCase.java) | [初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#concept-32044-zh)|
| [OSSBucketTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/OSSBucketTest.java) | - [创建存储空间](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-5#concept-32052-zh)、[获取存储空间的访问权限](https://help.aliyun.com/zh/oss/developer-reference/query-bucket-acls#concept-2382425)、[获取存储空间信息](https://help.aliyun.com/zh/oss/developer-reference/query-bucket-information-3#concept-2382429)、[删除存储空间](https://help.aliyun.com/zh/oss/developer-reference/delete-buckets-1#concept-2382431)、[列举存储空间](https://help.aliyun.com/zh/oss/developer-reference/list-buckets-4#concept-2122993)
- [生命周期](https://help.aliyun.com/zh/oss/developer-reference/manage-lifecycle-rules-4#concept-2071421)、[防盗链](https://help.aliyun.com/zh/oss/developer-reference/android-hotlink-protection#concept-2118548)、[日志转存](https://help.aliyun.com/zh/oss/developer-reference/logging-14#concept-2055089)|
| [OSSPutObjectTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/OSSPutObjectTest.java) | [简单上传](https://help.aliyun.com/zh/oss/developer-reference/simple-upload-2#concept-bts-m54-mfb)、[追加上传](https://help.aliyun.com/zh/oss/developer-reference/append-upload-5#concept-frp-1bp-mfb)、[上传回调](https://help.aliyun.com/zh/oss/developer-reference/upload-callbacks-5#concept-amg-wbp-mfb)、[批量删除文件](https://help.aliyun.com/zh/oss/developer-reference/delete-an-object#section-ta0-qox-ivi)、[进度条](https://help.aliyun.com/zh/oss/developer-reference/progress-bar-7#concept-xlp-vnd-nfb)|
| [MultipartUploadTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/MultipartUploadTest.java) | [分片上传](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-6#concept-1925841)|
| [ResumableUploadTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/ResumableUploadTest.java) | [断点续传上传](https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-4#concept-32050-zh)|
| [OSSGetObjectTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/OSSGetObjectTest.java) | [下载文件](https://help.aliyun.com/zh/oss/developer-reference/overview-5#concept-32048-zh)|
| [ManageObjectTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/ManageObjectTest.java) | [判断文件是否存在](https://help.aliyun.com/zh/oss/developer-reference/determine-whether-an-object-exists-7#concept-scc-qnp-mfb)、[获取文件访问权限](https://help.aliyun.com/zh/oss/developer-reference/query-the-acl-of-an-object#concept-2046809)、[拷贝文件](https://help.aliyun.com/zh/oss/developer-reference/copy-an-object-3#concept-dkq-tnp-mfb)、[列举文件](https://help.aliyun.com/zh/oss/developer-reference/list-objects-4#concept-unn-lpd-nfb)、[单个删除文件](https://help.aliyun.com/zh/oss/developer-reference/delete-an-object#section-gkk-t20-elg)、[设置Content-Type](https://help.aliyun.com/zh/oss/developer-reference/specify-content-type-for-an-object#concept-og3-b32-qgb)、[获取文件元数据](https://help.aliyun.com/zh/oss/developer-reference/query-object-metadata-5#concept-vp1-dnp-mfb)|
| [RestoreObjectTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/RestoreObjectTest.java) | [解冻文件](https://help.aliyun.com/zh/oss/developer-reference/restore-an-archive-object#concept-2150681)|
| [SymlinkTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/SymlinkTest.java) | [管理软链接](https://help.aliyun.com/zh/oss/developer-reference/manage-symbolic-links-12#concept-2150666)|
| [CRC64Test.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/CRC64Test.java) | [数据安全性](https://help.aliyun.com/zh/oss/developer-reference/data-verification-3#concept-iyw-wmp-mfb)|
| [OSSAuthenticationTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/OSSAuthenticationTest.java) | [签名URL](https://help.aliyun.com/zh/oss/sign-a-url#concept-32049-zh)、[授权访问](https://help.aliyun.com/zh/oss/developer-reference/authorize-access#concept-32046-zh)|
| [ImagePersistTest.java](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/ImagePersistTest.java) | [图片处理](https://help.aliyun.com/zh/oss/developer-reference/img-1#concept-qrm-ycn-mfb)|

## 后续参考
- [安装](https://help.aliyun.com/zh/oss/developer-reference/installation-1)
- [初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-1)
- [配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/android-configure-access-credentials)
- [快速入门](https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-android)
- [存储空间](https://help.aliyun.com/zh/oss/developer-reference/buckets-4/)
- [对象/文件](https://help.aliyun.com/zh/oss/developer-reference/objects-6/)
- [数据安全](https://help.aliyun.com/zh/oss/developer-reference/data-security-6/)
- [数据管理](https://help.aliyun.com/zh/oss/developer-reference/data-management-6/)
- [图片处理](https://help.aliyun.com/zh/oss/developer-reference/img-1)
- [授权访问](https://help.aliyun.com/zh/oss/developer-reference/authorize-access)
- [异常处理](https://help.aliyun.com/zh/oss/developer-reference/exception-handling-3)
- [常见问题](https://help.aliyun.com/zh/oss/developer-reference/faq-11)

[上一篇：OSS Kotlin SDK V2（预览版）](/zh/oss/developer-reference/oss-kotlin-sdk-v2-preview)[下一篇：安装（Android SDK）](/zh/oss/developer-reference/installation-1)该文章对您有帮助吗？反馈
  
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