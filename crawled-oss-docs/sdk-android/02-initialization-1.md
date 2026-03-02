# AndroidSDK客户端初始化参数配置

Source: https://help.aliyun.com/zh/oss/developer-reference/initialization-1

---

- AndroidSDK客户端初始化参数配置-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 初始化（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSSClient是OSS服务的Android客户端，为调用者提供了一系列的方法进行操作、管理存储空间（Bucket）和文件（Object）等。在使用SDK发起对OSS的请求前，您需要初始化一个OSSClient实例，并对OSSClient实例进行必要的设置。
说明 
OSSClient的生命周期需与应用程序的生命周期保持一致。即您需要在应用启动时创建一个全局的OSSClient，在应用结束时销毁OSSClient。

## 初始化OSSClient
重要 
移动终端是一个不受信任的环境，把`AccessKeyId`和`AccessKeySecret`直接保存在终端用来加签请求，存在极高的风险。推荐使用STS鉴权模式或自签名模式。

您可以通过以下多种方式新建OSSClient。
说明 
如果需要调用接口执行上传、下载等操作，请参见[快速入门（Android SDK）](https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-android)。

列举存储空间所使用的OSSClient初始化方式与这里示例中的通用形式不同，具体请参考[列举存储空间（Android SDK）](https://help.aliyun.com/zh/oss/developer-reference/list-buckets-4)。

### 使用STS新建OSSClient

以下代码用于使用STS新建OSSClient。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
String endpoint = "yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration config = new ClientConfiguration();
config.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);
```

### 使用自定义域名新建OSSClient

以下代码用于使用自定义域名新建OSSClient。

```
// yourEndpoint填写自定义域名。
String endpoint = "yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration config = new ClientConfiguration();
config.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);
```

### 专有云或专有域环境新建OSSClient

以下代码用于在专有云或专有域环境新建OSSClient。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。
String endpoint = "yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration configuration = new ClientConfiguration();
// 跳过CNAME解析。
List excludeList = new ArrayList<>();
excludeList.add(endpoint);
configuration.setCustomCnameExcludeList(excludeList);
// 创建OSSClient实例。
configuration.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);
```

## 配置OSSClient

ClientConfiguration是OSSClient的配置类，您可通过此类来配置代理、连接超时、最大连接数等参数。
| 参数 | 描述 | 方法|
| maxConcurrentRequest | 最大并发数。默认为5。 | ClientConfiguration.setMaxConcurrentRequest|
| socketTimeout | Socket层传输数据的超时时间，单位为毫秒。默认为60000毫秒。 | ClientConfiguration.setSocketTimeout|
| connectionTimeout | 建立连接的超时时间，单位为毫秒。默认为60000毫秒。 | ClientConfiguration.setConnectionTimeout|
| max_log_size | 日志文件大小。默认5 MB | ClientConfiguration.setMaxLogSize|
| maxErrorRetry | 请求失败后最大的重试次数。默认2次。 | ClientConfiguration.setMaxErrorRetry|
| customCnameExcludeList | 列表中的元素将跳过CNAME解析。 | ClientConfiguration.setCustomCnameExcludeList|
| proxyHost | 代理服务器主机地址。 | ClientConfiguration.setProxyHost|
| proxyPort | 代理服务器端口。 | ClientConfiguration.setProxyPort|
| mUserAgentMark | 用户代理中HTTP的User-Agent头。 | ClientConfiguration.setUserAgentMark|
| httpDnsEnable | 是否开启httpDns。
- true：2.9.12以下版本默认开启httpDns。
- false：2.9.12及以上版本默认关闭httpDns。 | ClientConfiguration.setHttpDnsEnable|
| checkCRC64 | 是否开启CRC64校验。取值如下：
- true：开启CRC64校验。
- false（默认值）：关闭CRC64校验。 | ClientConfiguration.setCheckCRC64|
| followRedirectsEnable | 是否开启HTTP重定向。取值如下：
- true：开启HTTP重定向。
- false（默认值）：关闭HTTP重定向。 | ClientConfiguration.setFollowRedirectsEnable|
| okHttpClient | 自定义okhttpClient。 | ClientConfiguration.setOkHttpClient|

以下代码用于使用ClientConfiguration配置OSSClient参数。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
String endpoint = "yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";

ClientConfiguration configuration = new ClientConfiguration();
// 设置最大并发数，默认值5。
// configuration.setMaxConcurrentRequest(3);
// 设置Socket层传输数据的超时时间，默认值60s。
// configuration.setSocketTimeout(50000);
// 设置建立连接的超时时间，默认值60s。
// configuration.setConnectionTimeout(50000);
// 设置日志文件大小，默认值5 MB。
// configuration.setMaxLogSize(3 * 1024 * 1024);
// 请求失败后最大的重试次数，默认值2。
// configuration.setMaxErrorRetry(3);
// 列表中的元素将跳过CNAME解析。
// List cnameExcludeList = new ArrayList<>();
// cnameExcludeList.add("cname");
// configuration.setCustomCnameExcludeList(cnameExcludeList);
// 代理服务器主机地址。
// configuration.setProxyHost("yourProxyHost");
// 代理服务器端口。
// configuration.setProxyPort(8080);
// 用户代理中HTTP的User-Agent头。
// configuration.setUserAgentMark("yourUserAgent");
// 是否开启CRC校验，默认值false。
// configuration.setCheckCRC64(true);
// 是否开启HTTP重定向，默认值false。
// configuration.setFollowRedirectsEnable(true);
// 设置自定义OkHttpClient。
// OkHttpClient.Builder builder = new OkHttpClient.Builder();
// configuration.setOkHttpClient(builder.build());

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
configuration.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);
```

## 启用日志

移动端的使用环境比较复杂。会出现部分区域或某一个时段无法正常使用OSS SDK的情况。为了进一步方便开发者定位问题，OSS SDK在开启日志记录功能后，会将一些日志信息记录在本地。如需开启，需要在OSSClient使用之前进行初始化，调用方法如下。

```
// 日志样式。
// 通过调用OSSLog.enableLog()开启在控制台查看日志。
// 支持在手机内置sd卡路径\OSSLog\logs.csv下写入日志文件，默认不开启。
// 日志会记录OSS操作行为中的请求数据、返回数据、异常信息。
// 例如requestId、response header等。
// 以下为日志记录示例。
// Android版本。
// android_version：5.1  
// Android手机型号。
// mobile_model：XT1085
// 网络状况。  
// network_state：connected
// 网络连接类型。
// network_type：WIFI 
// 具体的操作行为信息。
// [2017-09-05 16:54:52] - Encounter local execpiton: //java.lang.IllegalArgumentException: The bucket name is invalid. 
// A bucket name must: 
// 1) be comprised of lower-case characters, numbers or dash(-); 
// 2) start with lower case or numbers; 
// 3) be between 3-63 characters long. 
//------>end of log
// 调用此方法开启日志。
OSSLog.enableLog();              
```
说明 
您可以自行选择将文件上传至服务器，或者选择接入阿里云日志服务上传日志文件。

## 同步接口和异步接口说明

考虑到移动端开发场景下不允许在UI线程执行网络请求的编程规范，Android SDK对上传和下载接口同时提供了同步和异步两种调用示例，其他接口以异步调用示例为主。
- 同步调用同步接口调用后会阻塞等待结果返回。
- 同步接口不能在UI线程调用。
- 调用同步接口遇到异常时，将直接抛出ClientException或者ServiceException异常。ClientException异常是指本地遇到的异常，如网络异常参数非法等。ServiceException异常是指OSS返回的服务异常，如鉴权失败、服务器错误等。
- 异步调用异步接口需要在请求时传入回调函数，请求的执行结果将在回调中处理。
- 异步请求遇到异常时，异常会在回调函数中处理。
- 调用异步接口时，函数会直接返回一个Task。
```
OSSAsyncTask task = oss.asyncGetObejct(...);
task.cancel(); // 取消任务。
task.waitUntilFinished(); // 等待直到任务完成。
GetObjectResult result = task.getResult(); // 阻塞等待结果返回。           
```

[上一篇：安装（Android SDK）](/zh/oss/developer-reference/installation-1)[下一篇：配置访问凭证（Android SDK）](/zh/oss/developer-reference/android-configure-access-credentials)该文章对您有帮助吗？反馈
  
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