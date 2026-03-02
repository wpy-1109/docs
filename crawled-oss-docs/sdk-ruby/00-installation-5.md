# 在Linux Windows和macOS上安装OSS Ruby SDK

Source: https://help.aliyun.com/zh/oss/developer-reference/installation-5

---

- 在Linux Windows和macOS上安装OSS Ruby SDK-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 安装（Ruby SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
如果您需要管理OSS存储空间、上传下载文件、管理文件访问权限等，可以先安装OSS Ruby SDK。本文介绍如何安装OSS Ruby SDK。

## 操作步骤

### Linux

以下以Ubuntu 22.04版本为例。
- 使用apt-get包管理器安装Ruby。
```
apt-get install -y ruby
```
- 将阿里云的RubyGems镜像添加为新的RubyGems源，并删除默认的RubyGems源。
```
gem sources -a http://mirrors.aliyun.com/rubygems/ -r https://rubygems.org/
```
- 安装依赖。
```
sudo apt-get install ruby ruby-dev zlib1g-dev
```
重要 SDK依赖的某些gem是本地扩展的形式，因此需要安装ruby-dev以支持编译本地扩展的gem。
- SDK依赖处理XML的gem（nokogiri）环境中要求包含zlib库。
- 安装OSS Ruby SDK。
#### 方式一：通过gem方式安装

```
gem install aliyun-sdk --clear-sources --source https://gems.ruby-china.com
```

#### 方式二：通过bundler安装
在应用程序的`Gemfile`中添加`gem 'aliyun-sdk', '~> 0.6.0'`。
- 选择社区镜像源进行安装。
```
bundle config mirror.https://rubygems.org https://gems.ruby-china.com 
bundle install                        
```
说明 https://gems.ruby-china.com是完整的RubyGems镜像，与官方源自动同步， 并由Ruby China社区维护，不方便访问rubygems.org的用户可以使用此镜像源。

### Windows
- 前往[RubyInstaller](http://rubyinstaller.org/downloads/)下载Ruby+Devkit安装包，双击安装，根据安装向导进行安装。
- 输入命令`gem install aliyun-sdk`。 安装完成后，输入`irb`进入Ruby交互式命令行。在交互式命令行中输入`require 'aliyun/oss'`，如果显示true，则表明OSS Ruby SDK已完成安装。

## macOS
- 在终端输入`xcode-select --install`安装Xcode command line tools。 如果安装失败，建议手动下载并安装。 说明 使用您的Apple ID登录后从[苹果开发者网站](https://developer.apple.com/downloads/)下载Xcode command line tools。注意选择与您的系统匹配的版本。下载完成后双击加载dmg文件，然后在打开的窗口中双击安装程序进行安装，在安装的过程中需要输入您的系统密码。
- 在终端输入以下命令安装brew。 
```
 ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"                          
```
- 在终端输入以下命令安装Ruby。 
```
 brew install ruby
 exec $SHELL -l                                
```
- 在终端输入以下命令安装OSS Ruby SDK。 
```
 gem install aliyun-sdk                                
```
- 在终端输入以下命令验证SDK是否已安装成功。如果显式true，则表明OSS Ruby SDK已完成安装。 
```
 irb
 > require 'aliyun/oss'
 => true                                
```

## 相关文档
- [github地址](https://github.com/aliyun/aliyun-oss-ruby-sdk)
- [API文档地址](http://www.rubydoc.info/gems/aliyun-sdk/)
- [ChangeLog](https://github.com/aliyun/aliyun-oss-ruby-sdk/blob/master/CHANGELOG.md)

[上一篇：OSS Ruby SDK](/zh/oss/developer-reference/ruby/)[下一篇：初始化（Ruby SDK）](/zh/oss/developer-reference/initialization-11)该文章对您有帮助吗？反馈
  
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