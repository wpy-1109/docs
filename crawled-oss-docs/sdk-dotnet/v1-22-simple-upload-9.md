# 资源耗尽错误排查

Source: https://help.aliyun.com/zh/oss/developer-reference/simple-upload-9

---

- 资源耗尽错误排查 - Vertex AI - 谷歌云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 简单上传（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
简单上传是指通过PutObject方法上传单个文件（Object）。简单上传包括上传字符串和上传本地文件，您可以使用同步方式或者异步方式进行上传。您也可以使用MD5校验来确保上传过程中的数据完整性。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-ossclient#concept-32087-zh)。

## 权限说明

阿里云账号默认拥有全部权限。阿里云账号下的RAM用户或RAM角色默认没有任何权限，需要阿里云账号或账号管理员通过[RAM Policy](https://help.aliyun.com/zh/oss/ram-policy-overview/)或[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)授予操作权限。
| API | Action | 说明|
| PutObject | `oss:PutObject` | 上传Object。|
| `oss:PutObjectTagging` | 上传Object时，如果通过x-oss-tagging指定Object的标签，则需要此操作的权限。|
| `kms:GenerateDataKey` | 上传Object时，如果Object的元数据包含X-Oss-Server-Side-Encryption: KMS，则需要这两个操作的权限。|
| `kms:Decrypt`|

## 上传字符串

以下代码用于将字符串上传到目标存储空间examplebucket中的exampleobject.txt文件。

```
using System.Text;
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。
var objectName = "exampledir/exampleobject.txt";
// 填写字符串。
var objectContent = "More than just cloud.";
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
    byte[] binaryData = Encoding.ASCII.GetBytes(objectContent);
    MemoryStream requestContent = new MemoryStream(binaryData);
    // 上传文件。
    client.PutObject(bucketName, objectName, requestContent);
    Console.WriteLine("Put object succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
```

## 上传本地文件

以下代码用于将本地文件examplefile.txt上传到目标存储空间examplebucket中的exampleobject.txt文件。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。
var objectName = "exampledir/exampleobject.txt";
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
try
{
    // 上传文件。
    client.PutObject(bucketName, objectName, localFilename);
    Console.WriteLine("Put object succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
```

## 上传文件并且带MD5校验

为保证客户端发送的数据和OSS服务端接收到的数据一致，您可以在ObjectMeta中增加Content-Md5值，OSS服务端会使用该MD5值做校验。
重要 
使用MD5校验时，性能会有所下降。

以下代码用于上传本地文件时进行MD5校验。

```
using System;
using System.IO;

using Aliyun.OSS;
using Aliyun.OSS.Util;
using Aliyun.OSS.Common;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。
var objectName = "exampledir/exampleobject.txt";
// 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
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
try
{
    // 计算MD5。
    string md5;
    using (var fs = File.Open(localFilename, FileMode.Open))
    {
        md5 = OssUtils.ComputeContentMd5(fs, fs.Length);
    }
    var objectMeta = new ObjectMetadata
    {
        ContentMd5 = md5
    };
    // 上传文件。
    client.PutObject(bucketName, objectName, localFilename, objectMeta);
    Console.WriteLine("Put object succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
```

## 异步上传

以下代码用于以异步方式将本地文件examplefile.txt上传到目标存储空间examplebucket中的exampleobject.txt文件。使用异步上传时，您需要实现自己的回调处理函数。

```
using System;
using System.IO;
using System.Threading;

using Aliyun.OSS;
using Aliyun.OSS.Common;

// 异步上传。
namespace AsyncPutObject
{
    class Program
    {
        // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
        static string endpoint = "yourEndpoint";
        // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
        var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
        var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
        // 填写Bucket名称，例如examplebucket。
        static string bucketName = "examplebucket";
        // 填写Object完整路径。Object完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。
        static string objectName = "exampledir/exampleobject.txt";
        // 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        static string localFilename = "D:\\localpath\\examplefile.txt";

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
        
        private static void PutObjectCallback(IAsyncResult ar)
        {
            try
            {
                client.EndPutObject(ar);
                Console.WriteLine(ar.AsyncState as string);
                Console.WriteLine("Put object succeeded");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                _event.Set();
            }
        }

        public static void AsyncPutObject()
        {
            try
            {
                using (var fs = File.Open(localFilename, FileMode.Open))
                {
                    var metadata = new ObjectMetadata();
                    // 增加自定义元数据。
                    metadata.UserMetadata.Add("mykey1", "myval1");
                    metadata.UserMetadata.Add("mykey2", "myval2");
                    metadata.CacheControl = "No-Cache";
                    metadata.ContentType = "text/txt";
                    string result = "Notice user: put object finish";

                    // 异步上传。
                    client.BeginPutObject(bucketName, objectName, fs, metadata, PutObjectCallback, result.ToCharArray());

                    _event.WaitOne();
                }
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
        }

        static void Main(string[] args)
        {
            Program.AsyncPutObject();
        }
    }
}            
```

## 相关文档
- 关于简单上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-csharp-sdk/blob/master/samples/Samples/PutObjectSample.cs)。
- 关于简单上传的API接口说明，请参见[PutObject](https://help.aliyun.com/zh/oss/developer-reference/putobject#reference-l5p-ftw-tdb)。

[上一篇：上传文件（C# SDK V1）](/zh/oss/developer-reference/upload-objects-using-oss-sdk-for-csharp-v1/)[下一篇：追加上传（C# SDK V1）](/zh/oss/developer-reference/append-upload-10)该文章对您有帮助吗？反馈
  
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