# iOSSDK初始化与配置OSSClient实例

Source: https://help.aliyun.com/zh/oss/developer-reference/initialization-8

---

- iOSSDK初始化与配置OSSClient实例-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 初始化（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSSClient是OSS服务的iOS客户端，为调用者提供了一系列的方法进行操作、管理存储空间（Bucket）和文件（Object）等。在使用SDK发起对OSS的请求前，您需要初始化一个OSSClient实例，并对OSSClient实例进行必要设置。
说明 
OSSClient的生命周期需与应用程序的生命周期保持一致。即您需要在应用启动时创建一个全局的OSSClient，在应用结束时销毁OSSClient。

## 初始化OSSClient
重要 
移动终端是一个不受信任的环境，把`AccessKeyId`和`AccessKeySecret`直接保存在终端用来加签请求，存在极高的风险。推荐使用STS鉴权模式或自签名模式。

您可以通过以下多种方式新建OSSClient。

### 使用STS新建OSSClient

以下代码用于使用STS新建OSSClient。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
NSString *endpoint = @"yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
NSString *accessKeyId = @"yourAccessKeyId";
NSString *accessKeySecret = @"yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
NSString *securityToken = @"yourSecurityToken";
NSString *region = @"yourRegion";

id credentialProvider = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:accessKeyId secretKeyId:accessKeySecret securityToken:securityToken];
OSSClientConfiguration *configuration = [OSSClientConfiguration new];
configuration.signVersion = OSSSignVersionV4;
OSSClient *client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credentialProvider clientConfiguration:configuration];
client.region = region;
```

### 使用自定义域名新建OSSClient

以下代码用于使用自定义域名新建OSSClient。

```
// yourEndpoint填写自定义域名。
NSString *endpoint = @"yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
NSString *accessKeyId = @"yourAccessKeyId";
NSString *accessKeySecret = @"yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
NSString *securityToken = @"yourSecurityToken";
NSString *region = @"yourRegion";

id credentialProvider = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:accessKeyId secretKeyId:accessKeySecret securityToken:securityToken];
OSSClientConfiguration *configuration = [OSSClientConfiguration new];
configuration.signVersion = OSSSignVersionV4;
OSSClient *client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credentialProvider clientConfiguration:configuration];
client.region = region;
```

### 专有云或专有域环境新建OSSClient

以下代码用于在专有云或专有域环境新建OSSClient。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。
NSString *endpoint = @"yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
NSString *accessKeyId = @"yourAccessKeyId";
NSString *accessKeySecret = @"yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
NSString *securityToken = @"yourSecurityToken";
NSString *region = @"yourRegion";

id credentialProvider = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:accessKeyId secretKeyId:accessKeySecret securityToken:securityToken];
OSSClientConfiguration *configuration = [OSSClientConfiguration new];
// 跳过CNAME解析。
configuration.cnameExcludeList = @[endpoint];
configuration.signVersion = OSSSignVersionV4;
OSSClient *client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credentialProvider clientConfiguration:configuration];
client.region = region;
```

## 配置OSSClient

ClientConfiguration是OSSClient的配置类，您可通过此类来配置代理、连接超时、最大连接数等参数。
| 参数 | 描述 | 方法|
| maxRetryCount | 请求失败后最大的重试次数。默认3次。 | configuration.maxRetryCount|
| maxConcurrentRequestCount | 最大并发数。默认为5。 | configuration.maxConcurrentRequestCount|
| enableBackgroundTransmitService | 是否开启后台任务，默认不开启。 | configuration.enableBackgroundTransmitService|
| backgroundSesseionIdentifier | 自定义后台会话标识符，默认值为`com.aliyun.oss.backgroundsession`。 | configuration.backgroundSesseionIdentifier|
| isHttpdnsEnable | 是否开启httpDns。
- true：2.10.14及以下版本默认开启httpDns。
- false：2.10.14及以上版本默认关闭httpDns。 | configuration.isHttpdnsEnable|
| timeoutIntervalForRequest | 请求超时时间，默认15秒。 | configuration.timeoutIntervalForRequest|
| timeoutIntervalForResource | 资源超时时间，默认7天。 | configuration.timeoutIntervalForResource|
| proxyHost | 代理服务器主机地址。 | configuration.proxyHost|
| proxyPort | 代理服务器端口。 | configuration.proxyPort|
| userAgentMark | 用户代理中HTTP的User-Agent头。 | configuration.userAgentMark|
| cnameExcludeList | 列表中的元素将跳过CNAME解析。 | configuration.cnameExcludeList|
| crc64Verifiable | 是否开启CRC64校验。取值如下：
- YES：开启CRC64校验。
- NO（默认值）：关闭CRC64校验。 | configuration.crc64Verifiable|
| isAllowUACarrySystemInfo | 是否允许User-Agent携带系统信息。取值如下：
- YES：允许User-Agent携带系统信息。
- NO（默认值）：不允许User-Agent携带系统信息。 | configuration.isAllowUACarrySystemInfo|
| isFollowRedirectsEnable | 是否开启HTTP重定向。取值如下：
- YES：开启HTTP重定向。
- NO（默认值）：关闭HTTP重定向。 | configuration.isFollowRedirectsEnable|

以下代码用于使用ClientConfiguration配置OSSClient参数。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
NSString *endpoint = @"yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
NSString *accessKeyId = @"yourAccessKeyId";
NSString *accessKeySecret = @"yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
NSString *securityToken = @"yourSecurityToken";
NSString *region = @"yourRegion";

id credentialProvider = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:accessKeyId secretKeyId:accessKeySecret securityToken:securityToken];
OSSClientConfiguration *configuration = [OSSClientConfiguration new];
// 使用v4签名
configuration.signVersion = OSSSignVersionV4;
// 请求失败后最大的重试次数。
configuration.maxRetryCount = 3;
// 最大并发数。
configuration.maxConcurrentRequestCount = 3;
// 是否开启后台任务。
configuration.enableBackgroundTransmitService = YES;
// 自定义后台会话标识符。
configuration.backgroundSesseionIdentifier = @"yourBackgroundSesseionIdentifier";
// 是否开启httpDns。
configuration.isHttpdnsEnable = YES;
// 请求超时时间。
configuration.timeoutIntervalForRequest = 15;
// 资源超时时间。
configuration.timeoutIntervalForResource = 24 * 60 * 60;
// 代理服务器主机地址。
configuration.proxyHost = @"yourProxyHost";
// 代理服务器端口。
configuration.proxyPort = @8080;
// 用户代理中HTTP的User-Agent头。
configuration.userAgentMark = @"yourUserAgent";
// 列表中的元素将跳过CNAME解析。
configuration.cnameExcludeList = @[@"yourCname"];
// 是否开启CRC校验。
configuration.crc64Verifiable = YES;
// 是否允许User-Agent携带系统信息。
configuration.isAllowUACarrySystemInfo = YES;
// 是否开启HTTP重定向。
configuration.isFollowRedirectsEnable = NO;

OSSClient *client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credentialProvider clientConfiguration:configuration];
client.region = region;
```

## 启用日志

移动端的使用环境比较复杂，部分区域或某个时段会出现无法正常使用OSS SDK的情况。为了进一步定位开发者遇到的问题，OSS SDK在开启日志记录功能后，会将日志信息记录在本地。使用OSSClient前完成初始化，并调用如下方法开启日志记录。

```
// 日志样式。
//2017/10/25 11:05:43:863  [Debug]: 第17次：{number = 3, name = (null)}
//2017/10/25 11:05:43:863  [Debug]: 第15次：
//2017/10/25 11:05:43:863  [Debug]: ----------TestDebug------------
// 开启日志记录。
[OSSLog enableLog];                
```
说明 - 日志文件存储在沙盒的Caches/OSSLogs文件夹内。
- 您可以自行选择将文件上传至服务器，或者选择接入阿里云日志服务上传日志文件。

## OSSTask
- 所有调用API操作均会返回一个OSSTask。
```
OSSTask * task = [client getObject:get];
```
- 设置OSSTask。为OSSTask设置延续 (continuation) 以实现异步回调。
```
[task continueWithBlock: ^(OSSTask *task) {
    // do something
    ...
    return nil;
}];
```
- 等待OSSTask完成以实现同步回调。
```
[task waitUntilFinished];
```

[上一篇：安装（iOS SDK）](/zh/oss/developer-reference/installation-8)[下一篇：快速入门（iOS SDK）](/zh/oss/developer-reference/getting-started-with-oss-sdk-for-ios)该文章对您有帮助吗？反馈
  
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