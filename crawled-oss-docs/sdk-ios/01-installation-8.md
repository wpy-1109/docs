# 安装对象存储OSS的iOS SDK

Source: https://help.aliyun.com/zh/oss/developer-reference/installation-8

---

- 安装对象存储OSS的iOS SDK-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 安装（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
如果您需要管理OSS存储空间、上传下载文件、进行图片处理等，可以先安装OSS iOS SDK。本文介绍如何安装OSS iOS SDK。

## 环境要求
- iOS系统版本：iOS 8.0及以上
- macOS版本：10.10及以上

## 直接引入Framework

如何获取OSS iOS SDK Framework，请参见[GitHub](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/README-CN.md)。

在Xcode中，直接把Framework拖入您对应的Target下即可，在弹出框选中Copy items if needed。

## Pod依赖

如果工程是通过Pod管理依赖，只需在Podfile中加入以下依赖，不需要再导入Framework。

```
pod 'AliyunOSSiOS'           
```
说明 
您可以选择直接引入Framework或者Pod依赖两种方式中的任意一种。

## 工程中引入头文件

```
#import             
```
重要 
引入Framework后，需要在工程`Build Settings`的`Other Linker Flags`中加入`-ObjC`。如果工程已设置了`-force_load`选项，则需要加入`-force_load /AliyunOSSiOS`。

## 在Swift中使用SDK

OSS提供了Objective-C版本的 SDK，在Swift项目中可以使用Objective-C版本的SDK混合编码。OSS提供了Swift如何使用SDK的Demo。更多信息，请参见[GitHub](https://github.com/aliyun/aliyun-oss-ios-sdk/tree/master/OSSSwiftDemo)。

## 兼容IPv6-Only网络

为了解决无线网络下域名解析容易遭到劫持的问题，OSS移动端SDK引入了HTTPDNS进行域名解析，直接使用IP请求OSS服务端。在IPv6-Only 的网络下可能会遇到兼容性问题。苹果官方近期发布了关于IPv6-only网络环境兼容的App审核要求。为此，SDK从2.5.0版本开始已经做了兼容性处理。在新版本中，除了-ObjC的设置，还需要引入如下两个系统库：

```
libresolv.tbd
CoreTelephony.framework
SystemConfiguration.framework            
```

## 关于苹果ATS政策

WWDC 2016开发者大会上，苹果宣布从2017年1月1日起，苹果App Store中的所有App都必须启用App Transport Security(ATS)安全功能。即所有新提交的App默认不允许使用`NSAllowsArbitraryLoads`绕过ATS限制。此外，还需保证App的所有网络请求都必须通过HTTPS加密，否则可能会在应用审核时遇到麻烦。

OSS iOS SDK在`2.6.0`以上版本中对此做出支持。SDK不会自行发出任何非HTTPS请求，同时SDK支持`https://`前缀的`Endpoint`，只需要设置正确的HTTPS `Endpoint`，即可保证发出的网络请求均符合要求。
重要 - 设置`Endpoint`时，需使用`https://`前缀的URL。
- 在实现加签、获取STS Token等回调时，需确保不会发出非HTTPS的请求。

[上一篇：OSS iOS SDK](/zh/oss/developer-reference/preface-5/)[下一篇：初始化（iOS SDK）](/zh/oss/developer-reference/initialization-8)该文章对您有帮助吗？反馈
  
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