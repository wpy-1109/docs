# 使用C# SDK V2实现简单上传与追加上传

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-object-using-oss-sdk-for-csharp-v2

---

- 使用C# SDK V2实现简单上传与追加上传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 上传文件（C# SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何使用C# SDK V2在开启版本控制的存储空间（Bucket）中上传文件（Object）。

## 注意事项

本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。

## 权限说明

阿里云账号默认拥有全部权限。阿里云账号下的RAM用户或RAM角色默认没有任何权限，需要阿里云账号或账号管理员通过[RAM Policy](https://help.aliyun.com/zh/oss/ram-policy-overview/)或[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)授予操作权限。
| API | Action | 说明|
| PutObject | `oss:PutObject` | 上传Object。|
| `oss:PutObjectTagging` | 上传Object时，如果通过x-oss-tagging指定Object的标签，则需要此操作的权限。|
| `kms:GenerateDataKey` | 上传Object时，如果Object的元数据包含X-Oss-Server-Side-Encryption: KMS，则需要这两个操作的权限。|
| `kms:Decrypt`|

## 示例代码

### 简单上传
说明 - 在已开启版本控制的Bucket中，OSS会为新添加的Object自动生成唯一的VersionId，并在响应header中通过x-oss-version-id形式返回。
- 在暂停了版本控制的Bucket中，新添加的Object的VersionId为“null”，上传同名Object，后一次会覆盖前一次上传的文件内容。OSS保证同一个Object只会有一个版本的ID为“null”。

您可以使用以下代码进行简单上传。

```
using System.Text; // 引入System.Text命名空间，用于处理字符编码（如UTF-8编码字符串）
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var bucket = "your bucket name";  // 必须项，设置目标Bucket名称
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var key = "your object key"; // 必须项，指定上传的对象名称。格式（folder/objectName）

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

// 待上传的对象内容。示例内容：简单字符串"hello oss!"，实际场景中可为文件流、字节数组等
var content = "hello oss!";
// 将字符串转换为UTF-8编码的字节数组，再包装为MemoryStream
// MemoryStream用于在内存中处理数据流，适合小文件上传；大文件建议使用FileStream
var bodyStream = new MemoryStream(Encoding.UTF8.GetBytes(content));

// 调用PutObjectAsync方法异步上传对象（需传入包含Bucket、Key和Body的请求对象）
// 该方法会将bodyStream中的数据上传至指定Bucket的Key路径下
var result = await client.PutObjectAsync(new OSS.Models.PutObjectRequest()
{
    Bucket = bucket,    // 目标Bucket名称
    Key = key,          // 对象在Bucket中的唯一Key 
    Body = bodyStream   // 要上传的内容流（此处为内存中的字符串数据）
});

// 打印上传结果
Console.WriteLine("PutObject done");  // 提示操作完成
Console.WriteLine($"StatusCode: {result.StatusCode}");  // HTTP状态码
Console.WriteLine($"RequestId: {result.RequestId}");  // RequestId，用于阿里云排查问题
Console.WriteLine("Response Headers:");  // 响应头信息
result.Headers.ToList().ForEach(x => Console.WriteLine(x.Key + " : " + x.Value));  // 遍历并打印所有响应头
```

### 追加上传

在受版本控制的Bucket中，仅支持对于当前版本为Appendable类型的Object执行追加（AppendObject）操作，不支持对于历史版本为Appendable类型的Object执行AppendObject操作。
说明 - 对当前版本为Appendable类型的Object执行AppendObject操作时，OSS不会为该Appendable类型的Object生成历史版本。
- 对当前版本为Appendable类型的Object执行PutObject或DeleteObject操作时，OSS会将该Appendable类型的Object保留为历史版本，且该Object不允许继续追加。
- 不支持对当前版本为非Appendable类型的Object（包括 Normal Object、Delete Marker等）执行AppendObject 操作。

您可以使用以下代码进行追加上传。

```
﻿using System.Text; // 引入System.Text命名空间，用于处理字符编码（如UTF-8编码字符串）
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var bucket = "you bucket name";  // 必须项，设置目标Bucket名称 
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var key = "your object key"; // 必须项，需追加的对象名称。格式（folder/objectName）

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

// 定义要追加到OSS对象的第一部分内容
var content1 = "hello,";
// 定义要追加到OSS对象的第二部分内容
var content2 = "oss!";

// 调用AppendObjectAsync方法，执行第一次追加操作
var result1 = await client.AppendObjectAsync(new OSS.Models.AppendObjectRequest()
{
    // 指定目标Bucket
    Bucket = bucket,
    // 指定目标Object名称 
    Key = key,
    // 首次追加时，起始位置必须为0
    Position = 0,
    Body = new MemoryStream(Encoding.UTF8.GetBytes(content1))
 });

// 调用AppendObjectAsync方法，执行第二次追加操作，接续在上一次结束的位置
var result2 = await client.AppendObjectAsync(new OSS.Models.AppendObjectRequest()
{
     // 目标Bucket保持不变
    Bucket = bucket,
    // 目标Object名称保持不变
    Key = key,
    // 从上一次追加结束的位置继续写入
    Position = result1.NextAppendPosition,
    Body = new MemoryStream(Encoding.UTF8.GetBytes(content2))
});

// 打印上传结果
Console.WriteLine("AppendObject done"); // 提示操作完成
Console.WriteLine($"StatusCode: {result2.StatusCode}");  // HTTP状态码
Console.WriteLine($"RequestId: {result2.RequestId}");   // RequestId，用于阿里云排查问题
Console.WriteLine("Response Headers:"); // 响应头信息
result2.Headers.ToList().ForEach(x => Console.WriteLine(x.Key + " : " + x.Value));   // 遍历并打印所有响应头
Console.WriteLine($"NextAppendPosition: {result2.NextAppendPosition}"); // 输出下一次追加的起始位置
```

[上一篇：管理版本控制（C# SDK V2）](/zh/oss/developer-reference/manage-versioning-using-oss-sdk-for-csharp-v2)[下一篇：下载文件](/zh/oss/developer-reference/download-objects-using-oss-sdk-for-csharp-v2)该文章对您有帮助吗？反馈
  
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