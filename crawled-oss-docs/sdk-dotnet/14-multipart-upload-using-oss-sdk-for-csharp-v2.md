# 使用C# SDK V2分片上传大文件

Source: https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-using-oss-sdk-for-csharp-v2

---

- 使用C# SDK V2分片上传大文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 分片上传（C# SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS提供的分片上传（Multipart Upload）功能，将要上传的较大文件（Object）分成多个分片（Part）来分别上传，上传完成后再调用CompleteMultipartUploadAsync接口将这些Part组合成一个Object。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要分片上传，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 分片上传流程

分片上传（Multipart Upload）分为以下三个步骤：
- 初始化一个分片上传事件。 调用Client.InitiateMultipartUploadAsync方法返回OSS创建的全局唯一的uploadID。
- 上传分片。  调用Client.UploadPartAsync方法上传分片数据。说明 对于同一个uploadID，分片号（partNumber）标识了该分片在整个文件内的相对位置。如果使用同一个分片号上传了新的数据，那么OSS上该分片已有的数据将会被覆盖。
- OSS将收到的分片数据的MD5值放在ETag头内返回给用户。
- OSS计算上传数据的[MD5](https://help.aliyun.com/zh/oss/user-guide/can-i-use-etag-values-as-oss-md5-hashes-to-check-data-consistency)值，并与SDK计算的MD5值比较，如果不一致则返回InvalidDigest错误码。
- 完成分片上传。  所有分片上传完成后，调用Client.CompleteMultipartUploadAsync方法将所有分片合并成完整的文件。

## 示例代码

以下代码展示如何将本地的大文件分割成多个分片文件并发上传到存储空间，然后合并成完整的文件对象。

```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var bucket = "you bucket name";  // 必须项，Bucket名称
var key = "your object key";  // 必须项，待上传的目标文件对象名称
var partSize = 512*1024;  // 必须项，每次上传文件的分片大小，以512*1024为例，每个分片大小512kb
var filePath = "filePath";  // 必须项，需上传的目标文件路径

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

// 初始化分片上传
var initResult = await client.InitiateMultipartUploadAsync(new()
{
    Bucket = bucket,
    Key = key
});

// 打开要上传的文件
using var file = File.OpenRead(filePath);
long fileSize = file.Length;
long partNumber = 1;

// 存储所有分片上传后的信息
var uploadParts = new List();

// 分块上传文件
for (long offset = 0; offset  { return (left.PartNumber > right.PartNumber) ? 1 : -1; });

// 完成分片上传
var cmResult = await client.CompleteMultipartUploadAsync(new()
{
    Bucket = bucket,
    Key = key,
    UploadId = initResult.UploadId,
    CompleteMultipartUpload = new ()
    {
        Parts = uploadParts
    }
});

// 打印上传结果
Console.WriteLine("MultipartUpload done");  // 提示操作完成
Console.WriteLine($"StatusCode: {cmResult.StatusCode}");  // HTTP状态码
Console.WriteLine($"RequestId: {cmResult.RequestId}");  // RequestId，用于阿里云排查问题
Console.WriteLine("Response Headers:");  // 响应头信息
cmResult.Headers.ToList().ForEach(x => Console.WriteLine(x.Key + " : " + x.Value));  // 遍历并打印所有响应头
```

## 相关文档

关于分片上传的完整示例代码，请参见[multipartUpload.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/dev-2505/sample/MultipartUpload/Program.cs)。

[上一篇：追加上传（C# SDK V2）](/zh/oss/developer-reference/append-upload-using-oss-sdk-for-csharp-v2)[下一篇：表单上传（C# SDK V2）](/zh/oss/developer-reference/form-upload-using-oss-sdk-for-csharp-v2)该文章对您有帮助吗？反馈
  
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