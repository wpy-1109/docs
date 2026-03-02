# 使用C# SDK实现按前缀和分页列举文件

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects-15

---

- 使用C# SDK实现按前缀和分页列举文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 列举文件（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何列举指定存储空间下（Bucket）的所有文件（Object）、指定个数的文件、指定前缀的文件等。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-ossclient#concept-32087-zh)。
- 要列举文件，您必须有`oss:ListObjects`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 简单列举文件

以下代码用于简单列举指定Bucket下的100个文件。

```
using Aliyun.OSS;
// yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
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
    var listObjectsRequest = new ListObjectsRequest(bucketName);
    // 简单列举Bucket中的文件，默认返回100条记录。
    var result = client.ListObjects(listObjectsRequest);
    Console.WriteLine("List objects succeeded");
    foreach (var summary in result.ObjectSummaries)
    {
        Console.WriteLine("File name:{0}", summary.Key);
    }
}
catch (Exception ex)
{
    Console.WriteLine("List objects failed. {0}", ex.Message);
}
```

## 列举指定个数的文件

以下代码用于列举指定个数的文件。

```
using Aliyun.OSS;
// yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
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
    var listObjectsRequest = new ListObjectsRequest(bucketName)
    {
        // 通过MaxKeys指定列举文件的最大个数为200。 MaxKeys默认值为100，最大值为1000。
        MaxKeys = 200,
    };
    var result = client.ListObjects(listObjectsRequest);
    Console.WriteLine("List objects succeeded");
    foreach (var summary in result.ObjectSummaries)
    {
        Console.WriteLine(summary.Key);
    }
}
catch (Exception ex)
{
    Console.WriteLine("List objects failed, {0}", ex.Message);
}
```

## 列举指定前缀的文件

以下代码用于列举包含指定前缀（prefix）的文件。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
// yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 列举包含指定前缀test的文件。默认列举100个文件。
var prefix = "test";
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
    var keys = new List();
    ObjectListing result = null;
    string nextMarker = string.Empty;
    do
    {
        var listObjectsRequest = new ListObjectsRequest(bucketName)
        {
            Marker = nextMarker,
            MaxKeys = 100,
            Prefix = prefix,
        };
        result = client.ListObjects(listObjectsRequest);
        foreach (var summary in result.ObjectSummaries)
        {
            Console.WriteLine(summary.Key);
            keys.Add(summary.Key);
        }
        nextMarker = result.NextMarker;
    } while (result.IsTruncated);
    Console.WriteLine("List objects of bucket:{0} succeeded ", bucketName);
}
catch (OssException ex)
{
    Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}",
        ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId);
}
catch (Exception ex)
{
    Console.WriteLine("Failed with error info: {0}", ex.Message);
}
```

## 列举指定marker之后的文件

参数marker代表文件名称。以下代码用于列举指定marker之后的文件。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
// yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 设置marker，例如exampleobject.txt。
var marker = "exampleobject.txt";
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
    var keys = new List();
    ObjectListing result = null;
    string nextMarker = marker;
    do
    {
        var listObjectsRequest = new ListObjectsRequest(bucketName)
        // 您可以通过修改MaxKeys参数增大返回文件数量，也可以通过Marker参数分次读取。
        {
            Marker = nextMarker,
            MaxKeys = 100,
        };
        result = client.ListObjects(listObjectsRequest);
        foreach (var summary in result.ObjectSummaries)
        {
            Console.WriteLine(summary.Key);
            keys.Add(summary.Key);
        }
        nextMarker = result.NextMarker;
    // 如果IsTruncated为true， 则NextMarker将作为下次读取文件的起点。
    } while (result.IsTruncated);
    Console.WriteLine("List objects of bucket:{0} succeeded ", bucketName);
}
catch (OssException ex)
{
    Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}",
        ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId);
}
catch (Exception ex)
{
    Console.WriteLine("Failed with error info: {0}", ex.Message);
}
```

## 列举所有文件

以下代码用于列举指定Bucket下的所有文件。

```
using Aliyun.OSS;
// yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
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
// 列举所有文件。
public void ListObject(string bucketName)
{
    try
    {
        ObjectListing result = null; 
        string nextMarker = string.Empty;
        do
        {
            // 每页列举的文件个数通过MaxKeys指定，超出指定数量的文件将分页显示。
            var listObjectsRequest = new ListObjectsRequest(bucketName)
            {
                Marker = nextMarker,
                MaxKeys = 100
            };
            result = client.ListObjects(listObjectsRequest);  
            Console.WriteLine("File:");
            foreach (var summary in result.ObjectSummaries)
            {
                Console.WriteLine("Name:{0}", summary.Key);
            }
            nextMarker = result.NextMarker;
        } while (result.IsTruncated);
    }
    catch (Exception ex)
    {
        Console.WriteLine("List object failed. {0}", ex.Message);
    }
}
```

## 通过异步方式列举文件

以下代码用于异步方式列举文件：

```
using System;
using System.IO;
using System.Threading;
using Aliyun.OSS;
namespace AsyncListObjects
{
    class Program
    {   
        // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。
        static string endpoint = "yourEndpoint";
        // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
        var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
        var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
        // 填写Bucket名称，例如examplebucket。
        static string bucketName = "yourBucketName";
        static AutoResetEvent _event = new AutoResetEvent(false);
        // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
        const string region = "cn-hangzhou";
        
        // 创建ClientConfiguration实例，按照您的需要修改默认参数。
        var conf = new ClientConfiguration();
        
        // 设置v4签名。
        conf.SignatureVersion = SignatureVersion.V4;
        
        // 创建OssClient实例。
        var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
        client.SetRegion(region);
        static void Main(string[] args)
        {
            Program.AsyncListObjects();
            Console.ReadKey();
        }
        public static void AsyncListObjects()
        {
            try
            {
                var listObjectsRequest = new ListObjectsRequest(bucketName);
                client.BeginListObjects(listObjectsRequest, ListObjectCallback, null);
                _event.WaitOne();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Async list objects failed. {0}", ex.Message);
            }
        }
        // 通过ListObjectCallback方法异步调用结束后执行回调，如果使用异步类型的接口，都需要实现类似接口。
        private static void ListObjectCallback(IAsyncResult ar)
        {
            try
            {
                var result = client.EndListObjects(ar);
                foreach (var summary in result.ObjectSummaries)
                {
                    Console.WriteLine("文件名称: {0}", summary.Key);
                }
                _event.Set();
                Console.WriteLine("Async list objects succeeded");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Async list objects failed. {0}", ex.Message);
            }
        }
    }
}
```

## 相关文档
- 关于以同步方式列举文件的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ListObjectsSample.cs)。
- 关于以异步方式列举文件的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/ListObjectsSample.cs)。
- 关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)。

[上一篇：管理文件元数据（C# SDK V1）](/zh/oss/developer-reference/manage-object-metadata-8)[下一篇：删除文件（C# SDK V1）](/zh/oss/developer-reference/delete-objects-16)该文章对您有帮助吗？反馈
  
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