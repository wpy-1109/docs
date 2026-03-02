# 使用C# SDK实现完整的分片上传流程

Source: https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-10

---

- 使用C# SDK实现完整的分片上传流程-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 分片上传（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS提供的分片上传（Multipart Upload）功能，将要上传的较大文件（Object）分成多个分片（Part）来分别上传，上传完成后再调用CompleteMultipartUpload接口将这些Part组合成一个Object来达到断点续传的效果。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[初始化（C# SDK V1）](https://help.aliyun.com/zh/oss/developer-reference/initialization-ossclient#concept-32087-zh)。
- 要分片上传，您必须有`oss:PutObject`权限。具体操作，请参见[RAM Policy常见示例](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 分片上传流程

分片上传（Multipart Upload）分为以下三个步骤：
- 初始化一个分片上传事件。  调用InitiateMultipartUploadRequest方法返回OSS创建的全局唯一的uploadId。
- 上传分片。  调用UploadPartRequest方法上传分片数据。说明 对于同一个uploadId，分片号（PartNumber）标识了该分片在整个文件内的相对位置。如果使用同一个分片号上传了新的数据，则OSS上该分片已有的数据将会被覆盖。
- OSS将收到的分片数据的MD5值放在ETag头内返回给用户。
- OSS计算上传数据的[MD5](https://help.aliyun.com/zh/oss/user-guide/can-i-use-etag-values-as-oss-md5-hashes-to-check-data-consistency)值，并与SDK计算的MD5值比较，如果不一致则返回InvalidDigest错误码。
- 完成分片上传。  所有分片上传完成后，调用CompleteMultipartUploadRequest方法将所有分片合并成完整的文件。

## 分片上传完整示例

以下通过一个完整的示例对分片上传的流程进行逐步解析：

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称。
var bucketName = "examplebucket";
// 填写Object完整路径。Object完整路径中不能包含Bucket名称。
var objectName = "exampleobject.txt";
// 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
var localFilename = "D:\\localpath\\examplefile.txt";
// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);

// 初始化分片上传，返回uploadId。
var uploadId = "";
try
{
    // 定义上传的文件及所属Bucket的名称。您可以在InitiateMultipartUploadRequest中设置ObjectMeta，但不必指定其中的ContentLength。
    var request = new InitiateMultipartUploadRequest(bucketName, objectName);
    var result = client.InitiateMultipartUpload(request);
    uploadId = result.UploadId;
    // 打印UploadId。
    Console.WriteLine("Init multi part upload succeeded");
    // 根据uploadId执行取消分片上传事件或者列举已上传分片的操作。
    // 如果您需要根据您需要uploadId执行取消分片上传事件的操作，您需要在调用InitiateMultipartUpload完成初始化分片之后获取uploadId。 
    // 如果您需要根据您需要uploadId执行列举已上传分片的操作，您需要在调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前获取uploadId。
    Console.WriteLine("Upload Id:{0}", result.UploadId);
}
catch (Exception ex)
{
    Console.WriteLine("Init multi part upload failed, {0}", ex.Message);
    Environment.Exit(1);
}
// 计算分片总数。
// 分片最小值为100 KB，最大值为5 GB。最后一个分片的大小允许小于100 KB。
var partSize = 100 * 1024;
var fi = new FileInfo(localFilename);
var fileSize = fi.Length;
var partCount = fileSize / partSize;
if (fileSize % partSize != 0)
{
    partCount++;
}
//  当初始化分片成功时，开始分片上传。PartETags是保存PartETag的列表，OSS收到用户提交的分片列表后，会逐一验证每个分片数据的有效性。当所有的数据分片通过验证后，OSS会将这些分片组合成一个完整的文件。
var partETags = new List();
try
{
    using (var fs = File.Open(localFilename, FileMode.Open))
    {
        for (var i = 0; i 
## 取消分片上传事件

您可以调用client.AbortMultipartUpload方法来取消分片上传事件。当一个分片上传事件被取消后，无法再使用这个uploadId做任何操作，已经上传的分片数据会被删除。

以下代码用于取消分片上传事件。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称。
var bucketName = "examplebucket";
// 填写Object完整路径。Object完整路径中不能包含Bucket名称。
var objectName = "exampleobject.txt";
// 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后的返回结果。
var uploadId = "yourUploadId";
// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
// 初始化分片上传。
try
{
    var request = new InitiateMultipartUploadRequest(bucketName, objectName);
    var result = client.InitiateMultipartUpload(request);
    uploadId = result.UploadId;
    // 打印uploadId。
    Console.WriteLine("Init multi part upload succeeded");
    Console.WriteLine("Upload Id:{0}", result.UploadId);
}
catch (Exception ex)
{
    Console.WriteLine("Init multi part upload failed, {0}", ex.Message);
}
// 取消分片上传。
try
{
    var request = new AbortMultipartUploadRequest(bucketName, objectName, uploadId);
    client.AbortMultipartUpload(request);
    Console.WriteLine("Abort multi part succeeded， {0}", uploadId);
}
catch (Exception ex)
{
    Console.WriteLine("Abort multi part failed, {0}", ex.Message);
}
```

## 列举已上传的分片

以下代码用于列举已上传的分片：

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称。
var bucketName = "examplebucket";
// 填写Object完整路径。Object完整路径中不能包含Bucket名称。
var objectName = "exampleobject.txt";
// 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前的返回结果。
var uploadId = "yourUploadId";
// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
try
{
    PartListing listPartsResult = null;
    var nextMarker = 0;
    do 
    {
        var listPartsRequest = new ListPartsRequest(bucketName, objectName, uploadId) 
        {
            PartNumberMarker = nextMarker,
        };
        // 列举已上传的分片。
        listPartsResult = client.ListParts(listPartsRequest);
        Console.WriteLine("List parts succeeded");
        // 遍历所有分片。
        var parts = listPartsResult.Parts;
        foreach (var part in parts)
        {
            Console.WriteLine("partNumber: {0}, ETag: {1}, Size: {2}", part.PartNumber, part.ETag, part.Size);
        }
        nextMarker = listPartsResult.NextPartNumberMarker;
    } while (listPartsResult.IsTruncated);
}
catch (Exception ex)
{
    Console.WriteLine("List parts failed, {0}", ex.Message);
}
```

## 列举分片上传事件

调用ossClient.listMultipartUploads方法列举出所有执行中的分片上传事件，即已初始化但尚未完成或已取消的分片上传事件。可设置的参数如下：
| 参数 | 作用 | 设置方法|
| prefix | 限定返回的文件名称必须以指定的prefix作为前缀。注意使用prefix查询时，返回的文件名称中仍会包含prefix。 | ListMultipartUploadsRequest.setPrefix(String prefix)|
| delimiter | 用于对文件名称进行分组的一个字符。所有名称包含指定的前缀且第一次出现delimiter字符之间的文件作为一组元素。 | ListMultipartUploadsRequest.setDelimiter(String delimiter)|
| maxUploads | 限定此次返回分片上传事件的最大数目，默认值和最大值均为1000。 | ListMultipartUploadsRequest.setMaxUploads(Integer maxUploads)|
| keyMarker | 所有文件名称的字母序大于keyMarker参数值的分片上传事件。可以与uploadIdMarker参数一同使用来指定返回结果的起始位置。 | ListMultipartUploadsRequest.setKeyMarker(String keyMarker)|
| uploadIdMarker | 与keyMarker参数一同使用来指定返回结果的起始位置。 如果未设置keyMarker参数，则此参数无效。如果设置了keyMarker参数，则查询结果中包含：
- 名称的字母序大于keyMarker参数值的所有文件。
- 文件名称等于keyMarker参数值且uploadId比uploadIdMarker参数值大的所有分片上传事件。 | ListMultipartUploadsRequest.setUploadIdMarker(String uploadIdMarker)|

以下代码用于列举分片上传事件。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称。
var bucketName = "examplebucket";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
try
{
    MultipartUploadListing multipartUploadListing = null;
    var nextMarker = string.Empty;
    do
    {
        // 列举分片上传事件。
        var request = new ListMultipartUploadsRequest(bucketName)
        {
            KeyMarker = nextMarker,
        };
        multipartUploadListing = client.ListMultipartUploads(request);
        Console.WriteLine("List multi part succeeded");
        // 列举各个分片上传事件的信息。
        foreach (var mu in multipartUploadListing.MultipartUploads)
        {
            Console.WriteLine("Key: {0},  UploadId: {1}", mu.Key, mu.UploadId);
        }
        // 返回结果中isTruncated为false，nextKeyMarker和nextUploadIdMarker作为下次读取的起点。
        nextMarker = multipartUploadListing.NextKeyMarker;
    } while (multipartUploadListing.IsTruncated);
}
catch (Exception ex)
{
    Console.WriteLine("List multi part uploads failed, {0}", ex.Message);
}
```

## 指定前缀和最大返回条数

以下代码通过指定前缀和最大返回条数来进行分片上传：

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称。
var bucketName = "examplebucket";

// 定义前缀。
var prefix = "yourObjectPrefix";
// 定义最大返回条数为100。
var maxUploads = 100;
// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
try
{
    MultipartUploadListing multipartUploadListing = null;
    var nextMarker = string.Empty;
    do
    {
        // 列举分片上传事件。默认列举1000个分片。
        var request = new ListMultipartUploadsRequest(bucketName)
        {
            KeyMarker = nextMarker,
            // 指定前缀。
            Prefix = prefix,
            // 指定最大返回条数。
            MaxUploads = maxUploads,
        };
        multipartUploadListing = client.ListMultipartUploads(request);
        Console.WriteLine("List multi part succeeded");
        // 列举各个分片上传事件的信息。
        foreach (var mu in multipartUploadListing.MultipartUploads)
        {
            Console.WriteLine("Key: {0},  UploadId: {1}", mu.Key, mu.UploadId);
        }
        nextMarker = multipartUploadListing.NextKeyMarker;
    } while (multipartUploadListing.IsTruncated);
}
catch (Exception ex)
{
    Console.WriteLine("List multi part uploads failed, {0}", ex.Message);
}
```

## 相关文档
- 关于分片上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/MultipartUploadSample.cs)。
- 分片上传的完整实现涉及三个API接口，详情如下：关于初始化分片上传事件的API接口说明，请参见[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)。
- 关于分片上传Part的API接口说明，请参见[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)。
- 关于完成分片上传的API接口说明，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。
- 关于取消分片上传事件的API接口说明，请参见[AbortMultipartUpload](https://pkg.go.dev/github.com/aliyun/aliyun-oss-go-sdk/oss#Bucket.AbortMultipartUpload)。
- 关于列举已上传分片的API接口说明，请参见[ListUploadedParts](https://pkg.go.dev/github.com/aliyun/aliyun-oss-go-sdk/oss#Bucket.ListUploadedParts)。
- 关于列举所有执行中的分片上传事件（即已初始化但尚未完成或已取消的分片上传事件）的API接口说明，请参见[ListMultipartUploads](https://pkg.go.dev/github.com/aliyun/aliyun-oss-go-sdk/oss#Bucket.ListMultipartUploads)。

[上一篇：断点续传上传（C# SDK V1）](/zh/oss/developer-reference/resumable-upload-8)[下一篇：进度条（C# SDK V1）](/zh/oss/developer-reference/progress-bars-6)该文章对您有帮助吗？反馈
  
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