# 使用C# SDK V1快速入门实现文件上传下载及管理

Source: https://help.aliyun.com/zh/oss/developer-reference/quick-start-using-oss-sdk-for-csharp-v1

---

- 使用C# SDK V1快速入门实现文件上传下载及管理-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 快速入门（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文为您提供使用OSS C# SDK 进行常见存储操作的快速入门。您将学习如何安装SDK、配置访问凭证，以及执行基本操作，包括创建存储空间（Bucket）、上传、下载、列举和删除文件（Object）等。

## 注意事项

关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。

## 配置凭证

请确认您已[注册阿里云账号](https://account.aliyun.com/register/qr_register.htm?oauth_callback=https%3A%2F%2Fbailian.console.aliyun.com%2F%3FapiKey%3D1)，并完成实名认证。
- [创建有OSS管理权限的RAM用户AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。使用ROS脚本快速创建有OSS管理权限的RAM用户AccessKey在资源编排ROS控制台的[创建资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks/create?templateUrl=https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241114/itgrlo/createossadmin.yaml&step=1&hideTemplateSelector=false)页面的安全确认下，勾选确认，然后单击创建。创建完成后，在输出中，复制创建的AccessKey。
- 使用RAM用户AccessKey配置环境变量。
## Linux
在命令行界面执行以下命令来将环境变量设置追加到`~/.bashrc `文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```
执行以下命令使变更生效。
```
source ~/.bashrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

## macOS
- 在终端中执行以下命令，查看默认Shell类型。
```
echo $SHELL
```
根据默认Shell类型进行操作。
#### Zsh
执行以下命令来将环境变量设置追加到 `~/.zshrc` 文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
```
- 执行以下命令使变更生效。
```
source ~/.zshrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

#### Bash
- 执行以下命令来将环境变量设置追加到 `~/.bash_profile` 文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile
```
- 执行以下命令使变更生效。
```
source ~/.bash_profile
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

## Windows

## CMD
- 在CMD中运行以下命令。
```
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```
运行以下命令，检查环境变量是否生效。
```
echo %OSS_ACCESS_KEY_ID%
echo %OSS_ACCESS_KEY_SECRET%
```

## PowerShell
- 在PowerShell中运行以下命令。
```
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
运行以下命令，检查环境变量是否生效。
```
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

- 参考上述方式修改系统环境变量后，请重启或刷新您的编译运行环境，包括IDE、命令行界面、其他桌面应用程序及后台服务，以确保最新的系统环境变量成功加载。

## 安装SDK

## Windows 环境安装

## NuGet 方式安装
- 如果您的Visual Studio没有安装NuGet，请先安装[NuGet](https://docs.nuget.org/docs/start-here/installing-nuget)。
- 在Visual Studio中新建或者打开已有的项目，选择工具 > NuGet程序包管理器 > 管理解决方案的NuGet程序包。
- 搜索aliyun.oss.sdk，在结果中找到Aliyun.OSS.SDK（适用于.NET Framework）或Aliyun.OSS.SDK.NetCore（适用于.Net Core），选择最新版本，单击安装。

## DLL 引用方式安装
- 下载并解压.NET SDK开发包。
- 在Release模式下编译aliyun-oss-sdk项目，生成DLL库。
- 打开Visual Studio的解决方案资源管理器，选择您的项目，右击项目名称 ，选择 引用 > 添加引用 ，在弹出的对话框中选择浏览。
- 找到DLL库生成的bin目录，选择Aliyun.OSS.dll文件，单击确定。

## 项目引入方式安装

如果是下载了SDK包或者从GitHub上下载了源码，并通过源码安装，操作步骤如下：
- 在Visual Studio中，右击选择解决方案，在弹出的菜单中单击添加现有项目。
- 在弹出的对话框中选择aliyun-oss-sdk.csproj文件，单击打开。
- 右击项目名称，选择引用 > 添加引用，在弹出的对话框中选择项目选项卡，选中aliyun-oss-sdk项目，单击确定。

## Unix/Mac 环境安装

通过NuGet方式安装的步骤如下：
- 在Xamarin中新建或者打开已有的项目，选择工具Add NuGet Packages。
- 搜索到Aliyun.OSS.SDK或Aliyun.OSS.SDK.NetCore，选择最新版本，单击Add Package添加到项目应用中。

## 快速使用

以下示例程序演示了如何创建存储空间（Bucket）、上传、下载、列举和删除文件（Object）等。

### 创建存储空间

```
using Aliyun.OSS;
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// yourBucketName填写Bucket名称。
var bucketName = "yourBucketName";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);
try
{
    // 创建存储空间。
    var bucket = client.CreateBucket(bucketName);
    Console.WriteLine("Create bucket succeeded, {0} ", bucket.Name);
}
catch (Exception ex)
{
    Console.WriteLine("Create bucket failed, {0}", ex.Message);
}
```

### 上传文件

```
using Aliyun.OSS;

// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。
var objectName = "exampledir/exampleobject.txt";
// 填写本地文件完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
var localFilename = "D:\\localpath\\examplefile.txt";

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
    var result = client.PutObject(bucketName, objectName, localFilename);
    Console.WriteLine("Put object succeeded, ETag: {0} ", result.ETag);
}
catch (Exception ex)
{
    Console.WriteLine("Put object failed, {0}", ex.Message);
}
```

### 下载文件

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
// 下载Object到本地文件examplefile.txt，并保存到指定的本地路径中（D:\\localpath）。如果指定的本地文件存在会覆盖，不存在则新建。
// 如果未指定本地路径，则下载后的文件默认保存到示例程序所属项目对应本地路径中。
var downloadFilename = "D:\\localpath\\examplefile.txt";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);

try
{   
    // 下载文件。
    var result = client.GetObject(bucketName, objectName);
    using (var requestStream = result.Content)
    {
        using (var fs = File.Open(downloadFilename, FileMode.OpenOrCreate))
        {
            int length = 4 * 1024;
            var buf = new byte[length];
            do
            {
                length = requestStream.Read(buf, 0, length);
                fs.Write(buf, 0, length);
            } while (length != 0);
        }
    }
    Console.WriteLine("Get object succeeded");
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

### 列举文件

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

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);

try
{
    var objects = new List();
    ObjectListing result = null;
    string nextMarker = string.Empty;
    do
    {
        var listObjectsRequest = new ListObjectsRequest(bucketName)
        {
            Marker = nextMarker,
        };
        // 列举文件。
        result = client.ListObjects(listObjectsRequest);
        foreach (var summary in result.ObjectSummaries)
        {
            Console.WriteLine(summary.Key);
            objects.Add(summary.Key);
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

### 删除文件

```
using Aliyun.OSS;
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
var endpoint = "yourEndpoint";
// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET");
// 填写Bucket名称，例如examplebucket。
var bucketName = "examplebucket";
// 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。
var objectName = "exampledir/exampleobject.txt";

// 创建ClientConfiguration实例，按照您的需要修改默认参数。
var conf = new ClientConfiguration();

// 设置v4签名。
conf.SignatureVersion = SignatureVersion.V4;

// 创建OssClient实例。
var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf);
client.SetRegion(region);

try
{
    // 删除文件。
    client.DeleteObject(bucketName, objectName);
    Console.WriteLine("Delete object succeeded");
}
catch (Exception ex)
{
    Console.WriteLine("Delete object failed, {0}", ex.Message);
}
```

### 运行示例
- 在您的测试工程目录下创建main.cs文件，根据需要将示例代码拷贝至main.cs文件中。
- 请替换以下命令里的"yourRegion"、"yourBucketName"、"yourObjectName"为您的实际配置，其中yourRegion填写bucket所在地域，例如华东1（杭州）填写为cn-hangzhou。
```
dotnet script main.cs --   
```

## 常见问题

### 当使用SDK时遇到报错AccessDenied该如何进行排查？

当您遇到AccessDenied错误时通常是因为没有相应的访问权限。以下是解决此问题的步骤：
- 确认AccessKey ID和AccessKey Secret：请确保您使用了正确的AccessKey ID和AccessKey Secret。详情请参见[创建AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair#task-188766)。
- 检查RAM用户权限：确认RAM用户是否拥有Bucket或Object相关操作权限。具体步骤，请参见[为RAM用户授权](https://help.aliyun.com/zh/ram/grant-permissions-to-a-ram-user#task-187800)。
- 检查Bucket Policy：如果错误信息中提到“Access denied by bucket policy”，则表明是受到Bucket Policy的策略拒绝了。详情请参考[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)。
- 更多错误类型的查询，请您参阅[EC错误码](https://help.aliyun.com/zh/oss/user-guide/error-codes/)，例如关于访问控制方面的常见报错，可参见[03-ACCESS_CONTROL](https://help.aliyun.com/zh/oss/user-guide/03-access-control/)。

## 相关文档
- 关于OSS C# SDK 的更多信息，请参见[官方文档](https://github.com/aliyun/aliyun-oss-csharp-sdk)。
- 更多功能的代码示例，请参见[Github示例](https://github.com/aliyun/aliyun-oss-csharp-sdk/tree/master/samples/Samples)。

[上一篇：安装（C# SDK V1）](/zh/oss/developer-reference/installation-oss-sdk-for-csharp-v1)[下一篇：高级配置（C# SDK V1）](/zh/oss/developer-reference/advanced-config-using-oss-sdk-for-csharp-v1/)该文章对您有帮助吗？反馈
  
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