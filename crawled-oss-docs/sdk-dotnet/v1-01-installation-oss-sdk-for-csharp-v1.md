# 如何安装OSS C# SDK V1

Source: https://help.aliyun.com/zh/oss/developer-reference/installation-oss-sdk-for-csharp-v1

---

- 如何安装OSS C# SDK V1-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 安装（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
如果您需要管理OSS存储空间、上传下载文件、管理数据、进行图片处理等，可以先安装OSS C# SDK。本文介绍如何安装OSS C# SDK。

## 环境准备
- Windows 适用于.NET 2.0及以上版本
- 适用于Visual Studio 2010及以上版本
- Linux/Mac 适用于Mono 3.12及以上版本

## 下载SDK
- [直接下载](https://github.com/aliyun/aliyun-oss-csharp-sdk/archive/refs/tags/2.13.0.zip)
- [通过GitHub下载](https://github.com/aliyun/aliyun-oss-csharp-sdk.git?spm=a2c4g.11186623.2.15.5fce4144QhQZy7&file=aliyun-oss-csharp-sdk.git)
- [历史版本下载](https://github.com/aliyun/aliyun-oss-csharp-sdk/releases)

## 安装SDK
- Windows环境安装 NuGet方式安装 如果您的Visual Studio没有安装NuGet，请先安装[NuGet](https://docs.nuget.org/docs/start-here/installing-nuget)。
- 在Visual Studio中新建或者打开已有的项目，选择工具 > NuGet程序包管理器 > 管理解决方案的NuGet程序包。
- 搜索aliyun.oss.sdk，在结果中找到Aliyun.OSS.SDK（适用于.NET Framework）或Aliyun.OSS.SDK.NetCore（适用于.Net Core），选择最新版本，单击安装。
- DLL引用方式安装 下载并解压.NET SDK开发包。
- 在Release模式下编译aliyun-oss-sdk项目，生成DLL库。
- 打开Visual Studio的解决方案资源管理器，选择您的项目，右击项目名称 ，选择 引用 > 添加引用 ，在弹出的对话框中选择浏览。
- 找到DLL库生成的bin目录，选择Aliyun.OSS.dll文件，单击确定。
- 项目引入方式安装 如果是下载了SDK包或者从GitHub上下载了源码，并通过源码安装，操作步骤如下：在Visual Studio中，右击选择解决方案，在弹出的菜单中单击添加现有项目。
- 在弹出的对话框中选择aliyun-oss-sdk.csproj文件，单击打开。
- 右击项目名称，选择引用 > 添加引用，在弹出的对话框中选择项目选项卡，选中aliyun-oss-sdk项目，单击确定。
- Unix/Mac环境安装通过NuGet方式安装的步骤如下：在Xamarin中新建或者打开已有的项目，选择工具Add NuGet Packages。
- 搜索到Aliyun.OSS.SDK或Aliyun.OSS.SDK.NetCore，选择最新版本，单击Add Package添加到项目应用中。

[上一篇：OSS C# SDK V1](/zh/oss/developer-reference/preface-4/)[下一篇：快速入门（C# SDK V1）](/zh/oss/developer-reference/quick-start-using-oss-sdk-for-csharp-v1)该文章对您有帮助吗？反馈
  
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