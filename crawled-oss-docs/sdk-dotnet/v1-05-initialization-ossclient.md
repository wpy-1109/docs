# 使用C# SDK创建并配置OssClient

Source: https://help.aliyun.com/zh/oss/developer-reference/initialization-ossclient

---

- 使用C# SDK创建并配置OssClient-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 初始化（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OssClient是OSS服务的C#客户端，用于管理存储空间（Bucket）和文件（Object）等OSS资源。

## 新建OssClient

您可以通过以下多种方式新建OssClient。

### V4签名（推荐）

推荐使用更安全的V4签名算法。使用V4签名初始化时，除指定Endpoint以外，您还需要指定阿里云通用Region ID作为发起请求地域的标识，示例值为`cn-hangzhou`。同时声明SignVersion.V4。OSS .NET SDK 2.14.0及以上版本支持V4签名。

以使用OSS域名新建OSSClient时使用V4签名为例，其他通过自定义域名、STS等新建OSSClient的场景可参考以下示例执行相应修改。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");、

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
```

### V1签名（不推荐）
重要 
阿里云对象存储OSS自2025年03月01日起不再对新用户（即新UID ）开放使用V1签名，并将于2025年09月01日起停止更新与维护且不再对新增Bucket开放使用V1签名。请尽快切换到V4签名，避免影响服务。更多信息，请参见[公告说明](https://www.aliyun.com/notice/detail/116888)。

### 使用OSS域名新建OssClient

以下代码用于使用OSS域名新建OssClient。

```
using Aliyun.OSS;
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
  
// 构造OssClient实例。
var ossClient = new OssClient(endpoint, accessKeyId, accessKeySecret);                    
```

### 使用自定义域名新建OssClient

以下代码用于使用自定义域名新建OssClient。
重要 
使用自定义域名时，不支持使用ossClient.listBuckets方法。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写自定义域名。
const string endpoint = "yourDomain";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 打开CNAME开关。CNAME是指将自定义域名绑定到存储空间的过程。
conf.IsCname = true;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);                    
```

### 使用STS新建OssClient

以下代码用于使用STS新建一个OssClient。

```
using Aliyun.OSS;
// 运行本代码示例之前，请确保已使用STS服务获取的临时访问密钥设置环境变量YOUR_ACCESS_KEY_ID和YOUR_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("YOUR_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("YOUR_ACCESS_KEY_ID");
// 从STS服务获取的安全令牌（SecurityToken）。
const string  securityToken = "yourSecurityToken";
// 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 构造OssClient实例。
var ossClient = new OssClient(endpoint, accessKeyId, accessKeySecret, securityToken);
```

## 配置OssClient

ClientConfiguration是OSSClient的配置类，您可通过此类来配置代理、连接超时、最大连接数等参数。可设置的参数如下：
| 参数 | 描述 | 默认值|
| ConnectionLimit | 最大并发连接数。 | 512|
| MaxErrorRetry | 请求失败后最大的重试次数。 | 3|
| ConnectionTimeout | 设置连接超时时间，单位为毫秒。 | -1（不超时）|
| EnalbeMD5Check | 上传或下载数据时是否开启MD5校验。
- true：开启MD5校验。
- false：关闭MD5校验。
重要 
使用MD5校验时会有一定的性能开销。 | false|
| IsCname | Endpoint是否支持CNAME。CNAME用于将自定义域名绑定到存储空间。 | false|
| ProgressUpdateInterval | 进度条更新间隔，单位为字节。 | 8096|
| ProxyHost | 代理服务器，例如`example.aliyundoc.com`。 | 无|
| ProxyPort | 代理端口，例如`3128` 或 `8080`。 | 无|
| ProxyUserName | 代理服务账号，可选参数。 | 无|
| ProxyPassword | 代理服务密码，可选参数。 | 无|

以下代码用于配置OssClient。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

var conf = new ClientConfiguration();
// 设置最大并发连接数。
ClientConfiguration.ConnectionLimit = 512;
// 设置请求失败后最大的重试次数。
conf.MaxErrorRetry = 3;
// 设置连接超时时间。
conf.ConnectionTimeout = 300;
// 开启MD5校验。
conf.EnalbeMD5Check = true;
// 设置代理服务器。
conf.ProxyHost = "example.aliyundoc.com";
// 设置代理端口。
conf.ProxyPort = 3128;
// 设置代理网络的访问账号。
conf.ProxyUserName = "user";
// 设置代理网络的访问密码。
conf.ProxyPassword = "password";

var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);            
```

[上一篇：配置访问凭证（C# SDK V1）](/zh/oss/developer-reference/configure-access-credentials-using-oss-sdk-for-csharp-v1)[下一篇：存储空间（C# SDK V1）](/zh/oss/developer-reference/manage-buckets-using-oss-sdk-for-csharp-v1/)该文章对您有帮助吗？反馈
  
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