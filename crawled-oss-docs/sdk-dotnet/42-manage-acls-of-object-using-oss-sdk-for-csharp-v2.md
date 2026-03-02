# 使用C# SDK V2设置和获取版本控制对象的访问权限

Source: https://help.aliyun.com/zh/oss/developer-reference/manage-acls-of-object-using-oss-sdk-for-csharp-v2

---

- 使用C# SDK V2设置和获取版本控制对象的访问权限-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 管理文件访问权限（C# SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何在受版本控制的存储空间（Bucket）中管理文件（Object）的访问权限（ACL）。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要设置Object访问权限，您必须具有`oss:PutObjectAcl`权限；要获取Object访问权限，您必须具有`oss:GetObjectAcl`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 读写权限类型

文件的访问权限（ACL）有以下四种：
| 访问权限 | 描述 | 访问权限值|
| 继承Bucket | 文件遵循存储空间的访问权限。 | default|
| 私有 | 文件的拥有者和授权用户有该文件的读写权限，其他用户没有权限操作该文件。 | private|
| 公共读 | 文件的拥有者和授权用户有该文件的读写权限，其他用户只有文件的读权限。请谨慎使用该权限。 | public-read|
| 公共读写 | 所有用户都有该文件的读写权限。请谨慎使用该权限。 | public-read-write|

文件的访问权限优先级高于存储空间的访问权限。例如存储空间的访问权限是私有，而文件的访问权限是公共读写，则所有用户都有该文件的读写权限。如果某个文件没有设置过访问权限，则遵循存储空间的访问权限。

## 示例代码
说明 - PutObjectAcl默认设置Object当前版本的ACL权限。如果Object的当前版本是删除标记（Delete Marker），OSS将返回404 Not Found。请求参数中指定versionId可以设置指定Object版本的ACL权限。
- GetObjectAcl默认获取Object当前版本的ACL权限。如果Object的当前版本是删除标记（Delete Marker），OSS将返回404 Not Found。请求参数中指定versionId可以获取指定Object版本的ACL权限。

您可以使用以下代码设置并获取文件的访问权限。

```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var bucket = "your bucket name";  // 必须项，目标Bucket名称
var key = "your object name";  // 必须项，目标对象名称
var acl = "your object Acl";  // 必须项，目标对象的访问权限，可选值为default、private、public-read、public-read-write
var versionId = "your object versionId";  // 必须项，指定目标对象的x-oss-version-id

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;   
// 若已指定了endpoint，则覆盖默认的endpoint 
if(endpoint != null) 
{
    cfg.Endpoint = endpoint;
} 

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg); 

// 调用PutObjectAclAsync方法设置目标对象访问权限
var result1 = await client.PutObjectAclAsync(new OSS.Models.PutObjectAclRequest()
{
    Bucket = bucket,
    Key = key,
    Acl = acl,
    VersionId = versionId,
});

// 调用GetObjectAclAsync方法，获取目标对象权限信息
var result2 = await client.GetObjectAclAsync(new OSS.Models.GetObjectAclRequest()
{
    Bucket = bucket,
    Key = key,
    VersionId = versionId,
});

// 打印结果信息
Console.WriteLine("GetObjectAcl done");  // 提示操作完成
Console.WriteLine($"StatusCode: {result2.StatusCode}");  // HTTP状态码
Console.WriteLine($"RequestId: {result2.RequestId}");  // RequestId，用于阿里云排查问题
Console.WriteLine("Response Headers:");  // 响应头信息
result2.Headers.ToList().ForEach(x => Console.WriteLine(x.Key + " : " + x.Value));  // 遍历并打印所有响应头
Console.WriteLine($"Acl: {result2.Acl}");   // 输出目标对象权限信息
```

[上一篇：列举文件（C# SDK V2）](/zh/oss/developer-reference/list-object-using-oss-sdk-for-csharp-v2)[下一篇：获取文件元数据（C# SDK V2）](/zh/oss/developer-reference/query-object-metadata-using-oss-sdk-for-csharp-v2)该文章对您有帮助吗？反馈
  
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