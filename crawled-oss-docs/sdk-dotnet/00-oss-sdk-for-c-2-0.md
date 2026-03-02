# 快速入门OSS C# SDK V2

Source: https://help.aliyun.com/zh/oss/developer-reference/oss-sdk-for-c-2-0/

---

- 快速入门OSS C# SDK V2-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# OSS C# SDK V2
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
[GitHub](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/README-CN.md)｜[SDK Releases](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/releases)

## 快速接入

接入OSS C# SDK V2的流程如下：

### 环境准备
- 适用于`.NET Framework 471`及以上版本。
- 适用于`.NET Standard 2.0`及以上版本。
- 适用于`.NET5.0`及以上版本。
- 如果当前计算环境中不存在所需 .NET 环境或版本过低，请参考以下步骤：对于.NET Framework：请访问[Microsoft 官网](https://dotnet.microsoft.com/zh-cn/download/dotnet-framework)下载并安装.NET Framework 4.7.1 或更高版本。
- 对于.NET Standard：通常 .NET Standard 是由其他.NET实现（如 .NET Framework 或 .NET）支持的，确保您已安装相应的.NET实现即可。
- 对于.NET：请访问[.NET 官网](https://dotnet.microsoft.com/zh-cn/download)下载并安装.NET 5.0或更高版本。

### 安装SDK

推荐您使用最新的OSS C# SDK V2版本，确保本文中的代码示例可以正常运行。关于版本功能的更多信息，请参见[Releases](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/releases)。

## 通过 NuGet 安装
- 检查NuGet是否已安装：确保你的Visual Studio已经安装了NuGet包管理器。如果未安装，可以通过Visual Studio的“工具”->“获取工具和功能”进入Visual Studio Installer，在工作负载中勾选“.NET桌面开发”或者“ASP.NET和Web开发”，这将自动包含NuGet包管理器。
- 打开项目：在Visual Studio中新建一个项目或打开已有项目。
- 访问NuGet程序包管理器：在菜单栏选择“工具”->“NuGet程序包管理器”->“管理解决方案的NuGet程序包”。
- 搜索并安装SDK：在NuGet包管理器的“浏览”选项卡中，输入`AlibabaCloud.OSS.V2`进行搜索。
- 在搜索结果中找到`AlibabaCloud.OSS.V2`，查看其详细信息，并确保选择最新稳定版本。
- 点击“安装”按钮来安装该包。等待安装完成。
- 确认安装成功：安装完成后，可以在解决方案资源管理器中的“引用”下看到`AlibabaCloud.OSS.V2`。此时，你就可以在项目中使用这个SDK提供的功能了。

## 项目引入方式安装
- 克隆GitHub仓库：打开命令提示符或Git Bash，执行以下命令来克隆仓库：
```
git clone https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2.git
```
- 添加项目到解决方案：在Visual Studio中右键点击解决方案（Solution），“添加”->“现有项目...”。
- 浏览到克隆下来的源码目录，选择`AlibabaCloud.OSS.V2.csproj`文件，然后点击“打开”。
- 添加项目引用：右键点击你的项目，选择“添加”->“引用...”。
- 在弹出的对话框中切换到“项目”选项卡，找到并勾选`AlibabaCloud.OSS.V2`项目，点击“确定”。

### 配置访问凭证

使用 RAM 用户的 AccessKey 配置访问凭证。
- 在 [RAM 控制台](https://ram.console.aliyun.com/users/create)，创建使用永久 AccessKey 访问的 RAM 用户，保存 AccessKey，然后为该用户授予 `AliyunOSSFullAccess` 权限。
- 使用 RAM 用户 AccessKey 配置环境变量。
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

### 初始化客户端

使用[地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)初始化 OSSClient，并运行测试代码。

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

运行后将会输出上传文件成功的结果：

```
PutObject done
StatusCode: 200
RequestId: 68808D6D6A91E53037F7AAE9
Response Headers:
Server : AliyunOSS
Date : Wed, 23 Jul 2025 07:21:17 GMT
Connection : keep-alive
x-oss-request-id : 68808D6D6A91E53037F7AAE9
Vary : Origin
ETag : "968205D07B5A124D6ADA9336826C2C90"
x-oss-hash-crc64ecma : 11833582957755287462
x-oss-version-id : CAEQpgEYgYCA3fPQ2MEZIiA2ZmI4NGZkZWQzMWY0ZDZkOTFmMjUxYzRkNGMxODdkZg--
x-oss-server-time : 90
Content-Length : 0
Content-MD5 : loIF0HtaEk1q2pM2gmwskA==
```

## 客户端配置

客户端支持哪些配置？
| 参数名 | 说明 | 示例|
| `Region` | (必选)请求发送的区域,必选 | Configuration.Region = "cn-hangzhou"|
| `Endpoint` | 访问域名 | Configuration.Endpoint = "oss-cn-hangzhou.aliyuncs.com"|
| `RetryMaxAttempts` | 失败请求的最大重试次数 | Configuration.RetryMaxAttempts = 5|
| `Retryer` | HTTP请求时的重试实现 | Configuration.Retryer = new Retry.DefaultRetryer()|
| `HttpTransport` | 自定义HTTP客户端 | Configuration.HttpTransport = new HttpTransport()|
| `CredentialsProvider` | （必选）设置访问凭证 | Configuration.CredentialsProvider = new EnvironmentVariableCredentialsProvider()|
| `UsePathStyle` | 使用路径请求风格，即二级域名请求风格，默认为bucket托管域名 | Configuration.UsePathStyle = true|
| `UseCName` | 是否使用自定义域名访问，默认不使用 | Configuration.UseCName = true|
| `ConnectTimeout` | 建立连接的超时时间,默认值为10 秒 | Configuration.ConnectTimeout = TimeSpan.FromSeconds(30)|
| `ReadWriteTimeout` | 应用读写数据的超时时间,默认值为20 秒 | Configuration.ReadWriteTimeout = TimeSpan.FromMinutes(2)|
| `InsecureSkipVerify` | 是否跳过SSL证书校验，默认检查SSL证书 | Configuration.InsecureSkipVerify = true|
| `EnabledRedirect` | 是否开启HTTP重定向,默认不开启 | Configuration.EnabledRedirect = true|
| `ProxyHost` | 设置代理服务器 | Configuration.ProxyHost = "http://proxy.example.com:8080"|
| `SignatureVersion` | 签名版本，默认值为v4 | Configuration.SignatureVersion = "v4"|
| `DisableSsl` | 不使用https请求，默认使用https | Configuration.DisableSsl = true|
| `UseDualStackEndpoint` | 是否使用双栈域名访问，默认不使用 | Configuration.UseDualStackEndpoint = true|
| `UseAccelerateEndpoint` | 是否使用传输加速域名访问，默认不使用 | Configuration.UseAccelerateEndpoint = true|
| `UseInternalEndpoint` | 是否使用内网域名访问，默认不使用 | Configuration.UseInternalEndpoint = true|
| `DisableUploadCrc64Check` | 上传时关闭CRC64校验，默认开启CRC64校验 | Configuration.DisableUploadCrc64Check = true|
| `DisableDownloadCrc64Check` | 下载时关闭CRC64校验，默认开启CRC64校验 | Configuration.DisableDownloadCrc64Check = true|
| `AdditionalHeaders` | 指定额外的签名请求头，V4签名下有效 | Configuration.AdditionalHeaders = new List<string> { "x-oss-meta-*" }|
| `UserAgent` | 指定额外的User-Agent信息 | Configuration.UserAgent = "MyApp/1.0"|

### 使用自定义域名

使用OSS默认域名访问时，可能会出现文件禁止访问、文件无法预览等问题；通过[通过自定义域名访问OSS](https://help.aliyun.com/zh/oss/user-guide/access-buckets-via-custom-domain-names#concept-zt4-cvy-5db)，不仅支持浏览器直接预览文件，还可结合CDN加速分发。

```
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = "https://www.example-***.com";  // 必须项，请填写您的自定义域名。例如www.example-***.com

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;
// 若已指定了endpoint，则覆盖默认的endpoint
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 请注意，设置true开启CNAME选项，否则无法使用自定义域名
cfg.UseCName = true;

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 使用创建好的client执行后续操作...
```

### 使用内网域名

使用内网域名访问同地域的OSS资源，可以降低流量成本并提高访问速度。

```
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = "https://oss-cn-hangzhou-internal.aliyuncs.com";  // 可选项，指定访问OSS服务的内网域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou-internal.aliyuncs.com

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;
// 若已指定了endpoint，则覆盖默认的endpoint
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 您也可以无需指定内网endpoint，直接设置cfg.UseInternalEndpoint = true配置内网域名
// cfg.UseInternalEndpoint = true;

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 使用创建好的client执行后续操作...
```

### 使用传输加速域名

```
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = "https://oss-accelerate.aliyuncs.com";  // 可选项，填写Bucket所在地域对应的传输加速Endpoint。以华东1（杭州）为例，Endpoint填写为'https://oss-accelerate.aliyuncs.com'

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;
// 若已指定了endpoint，则覆盖默认的endpoint
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 您也可以无需指定传输加速endpoint，直接设置cfg.UseAccelerateEndpoint = true配置传输加速域名
// cfg.UseAccelerateEndpoint = true;

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 使用创建好的client执行后续操作...	
```

### 使用专有域

```
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = "https://service.corp.example.com";  // 必须项，请填写您的专有域。例如：https://service.corp.example.com

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;
// 若已指定了endpoint，则覆盖默认的endpoint
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 使用创建好的client执行后续操作...	
```

### 使用金融云域名

以下是使用[金融云](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#dbe294402aq6j)域名配置OSSClient的示例代码。

```
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou"; // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
// 必须项， 填写Bucket所在地域对应的内网Endpoint。以华东1 金融云为例，Endpoint填写为'https://oss-cn-hzjbp-a-internal.aliyuncs.com',
// 如需指定为http协议，请在指定域名时填写为'http://oss-cn-hzjbp-a-internal.aliyuncs.com'
var endpoint = "https://oss-cn-hzjbp-a-internal.aliyuncs.com";

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;
// 若已指定了endpoint，则覆盖默认的endpoint
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 使用创建好的client执行后续操作...	
```

### 使用政务云域名

以下是使用[政务云](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#3e2a1817f0pps)域名配置OSSClient的示例代码。

```
using OSS = AlibabaCloud.OSS.V2; // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-north-2-gov-1"; // 必须项，设置Bucket所在的区域（Region）。以华北2 阿里政务云1为例，Region填写为cn-north-2-gov-1
// 必须项，填写Bucket所在地域对应的内网Endpoint。以华北2 阿里政务云1为例，Endpoint填写为'https://oss-cn-north-2-gov-1-internal.aliyuncs.com',
// 如需指定为http协议，请在指定域名时填写为'http://oss-cn-north-2-gov-1-internal.aliyuncs.com'
var endpoint = "https://oss-cn-north-2-gov-1-internal.aliyuncs.com";

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;
// 若已指定了endpoint，则覆盖默认的endpoint
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 使用创建好的client执行后续操作...	
```

## 访问凭证配置

OSS 提供多种凭证初始化方式。请根据您的认证和授权需求选择合适的初始化方式。

如何选择访问凭证？
| 凭证提供者初始化方式 | 适用场景 | 是否需要提供前置的AK或STS Token | 底层实现基于的凭证 | 凭证有效期 | 凭证轮转或刷新方式|
| 使用RAM用户的AK | 部署运行在安全、稳定且不易受外部攻击的环境的应用程序，无需频繁轮转凭证就可以长期访问云服务 | 是 | AK | 长期 | 手动轮转|
| 使用STS临时访问凭证 | 部署运行在不可信的环境的应用程序，希望能控制访问的有效期、权限 | 是 | STS Token | 临时 | 手动刷新|
| 使用RAMRoleARN | 需要授权访问云服务，例如跨阿里云账号访问云服务的应用程序 | 是 | STS Token | 临时 | 自动刷新|
| 使用ECSRAMRole | 部署运行在阿里云的ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中的应用程序 | 否 | STS Token | 临时 | 自动刷新|
| 使用OIDCRoleARN | 部署运行在阿里云的容器服务Kubernetes版的Worker节点中的不可信应用程序 | 否 | STS Token | 临时 | 自动刷新|
| 使用自定义访问凭证 | 如果以上凭证配置方式都不满足要求时，您可以自定义获取凭证的方式 | 自定义 | 自定义 | 自定义 | 自定义|

### 使用RAM用户的AK

如果您的应用程序部署运行在安全、稳定且不易受外部攻击的环境中，需要长期访问您的OSS，且不能频繁轮转凭证时，您可以使用阿里云主账号或RAM用户的AK（Access Key ID、Access Key Secret）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个AK，存在安全性风险和维护复杂度增加的风险。
警告 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请考虑创建新的AK进行轮换。

## 环境变量
- 使用RAM用户AccessKey配置环境变量。
### Linux
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

### macOS
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

### Windows

#### CMD
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

#### PowerShell
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
- 使用环境变量来传递凭证信息。
```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

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
```

## 静态凭证

以下示例代码展示了如何对访问凭据直接进行硬编码，显式设置要使用的访问密钥。
警告 
请勿将访问凭据嵌入到生产环境的应用程序中，此方法仅用于测试目的。

```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

var cfg = OSS.Configuration.LoadDefault();

// 填写RAM用户AccessKey ID和AccessKey Secret。
var access_key_id = "yourAccessKeyId";
var access_key_secret = "yourAccessKeySecret";
// 创建静态凭证提供者，显式设置RAM用户密钥AccessKey ID和AccessKey Secret
cfg.CredentialsProvider = new OSS.Credentials.StaticCredentialsProvider(access_key_id,access_key_secret);

// 设置配置的Bucket区域
cfg.Region = region;   
// 若已指定了endpoint，则覆盖默认的endpoint 
if(endpoint != null) 
{
    cfg.Endpoint = endpoint;
} 

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);
```

### 使用STS临时访问凭证

如果您的应用程序需要临时访问OSS，您可以使用通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个STS Token，存在安全性风险和维护复杂度增加的风险。此外，如果您需要多次临时访问OSS，您需要手动刷新STS Token。
重要 - 如果您希望通过OpenAPI的方式简单快速获取到STS临时访问凭证，请参见[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)。
- 如果您希望通过SDK的方式获取STS临时访问凭证，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#section-rjh-18m-7kp)。
- 请注意，STS Token在生成的时候需要指定过期时间，过期后自动失效不能再使用。
- 如果您希望获取关于STS服务的接入点列表，请参见[服务接入点](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-endpoint)。

## 环境变量
- 使用临时身份凭证设置环境变量。
## Mac OS X/Linux/Unix
警告 请注意，此处使用的是通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token），而非RAM用户的Access Key和Access Key Secret。
- 请注意区分STS服务获取的Access Key ID以STS开头，例如“STS.L4aBSCSJVMuKg5U1****”。

```
export OSS_ACCESS_KEY_ID=
export OSS_ACCESS_KEY_SECRET=
export OSS_SESSION_TOKEN=
```

## Windows
警告 - 请注意，此处使用的是通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token），而非RAM用户的AK（Access Key ID、Access Key Secret）。
- 请注意区分STS服务获取的Access Key ID以STS开头，例如“STS.L4aBSCSJVMuKg5U1****”。

```
set OSS_ACCESS_KEY_ID=
set OSS_ACCESS_KEY_SECRET=
set OSS_SESSION_TOKEN=
```
- 通过环境变量来传递凭证信息。
```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET、OSS_SESSION_TOKEN）
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
```

## 静态凭证

以下示例代码展示了如何对访问凭据直接进行硬编码，显式设置要使用的临时访问密钥。
警告 
请勿将访问凭据嵌入到生产环境的应用程序中，此方法仅用于测试目的。

```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

var cfg = OSS.Configuration.LoadDefault();

// 填写获取的临时访问密钥AccessKey ID和AccessKey Secret，非阿里云账号AccessKey ID和AccessKey Secret。
// 请注意区分STS服务获取的Access Key ID是以STS开头，如下所示。
var access_key_id = "STS.****************";
var access_key_secret = "yourAccessKeySecret";
// 填写获取的STS安全令牌（SecurityToken）。
var securityToken = "yourSecurityToken";
// 创建静态凭证提供者，显式设置临时访问密钥AccessKey ID和AccessKey Secret，以及STS安全令牌
cfg.CredentialsProvider = new OSS.Credentials.StaticCredentialsProvide(access_key_id, access_key_secret, securityToken);

// 设置配置的Bucket区域
cfg.Region = region;   
// 若已指定了endpoint，则覆盖默认的endpoint 
if(endpoint != null) 
{
    cfg.Endpoint = endpoint;
} 

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg);
```

### 使用RAMRoleARN

如果您的应用程序需要授权访问OSS，例如跨阿里云账号访问OSS，您可以使用RAMRoleARN初始化凭证提供者。该方式底层实现是STS Token。通过指定RAM角色的ARN（Alibabacloud Resource Name），Credentials工具会前往STS服务获取STS Token，并在会话到期前调用AssumeRole接口申请新的STS Token。此外，您还可以通过为`policy`赋值来限制RAM角色到一个更小的权限集合。
重要 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请考虑创建新的AK进行轮换。
- 如需获取RAMRoleARN，请直接访问[创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 添加Aliyun.Credentials依赖。
```
dotnet add package Aliyun.Credentials --source https://api.nuget.org/v3/index.json
```
- 配置AK和RAMRoleARN作为访问凭证。
```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

// 阿里云凭证配置 - 使用RAM角色ARN方式
// 更多凭证类型示例参考：https://github.com/aliyun/credentials-csharp
var credConfig = new Aliyun.Credentials.Models.Config()
{
    // 指定凭证类型为RAM角色ARN
    Type = "ram_role_arn",
    // 从环境变量读取AccessKeyId
    AccessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"),
    // 从环境变量读取AccessKeySecret
    AccessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"),
    // RAM角色ARN，格式：acs:ram::USER_Id:role/ROLE_NAME
    // 也可通过环境变量ALIBABA_CLOUD_ROLE_ARN设置
    RoleArn = "acs:ram::***************:role/******",
    // 角色会话名称，用于标识当前会话
    RoleSessionName = "",
    // 可选参数，限制STS令牌的权限范围
    Policy = "",
    // 可选参数，设置STS令牌的有效期（秒）
    RoleSessionExpiration = 3600,
};

// 创建凭证客户端实例，用于获取临时访问凭证
var credClient = new Aliyun.Credentials.Client(credConfig);

// 将通用凭证转换为OSS SDK所需的凭证提供器
var credentialsProvider = new OSS.Credentials.CredentialsProvideFunc(() =>
{
    // 获取临时凭证
    var credential = credClient.GetCredential();

    // 构造OSS SDK所需的凭证对象
    return new OSS.Credentials.Credentials(
        credential.AccessKeyId,      // 临时AccessKey ID
        credential.AccessKeySecret,  // 临时AccessKey Secret
        credential.SecurityToken);   // 安全令牌（STS Token）
});

// 加载OSS SDK的默认配置
// 默认从环境变量中加载凭证信息（此处已被自定义凭证覆盖）
var cfg = OSS.Configuration.LoadDefault();
// 设置OSS区域
cfg.Region = region;
// 设置自定义凭证提供器
cfg.CredentialsProvider = credentialsProvider;

// 如果指定了自定义endpoint，则覆盖默认设置
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 创建ListBuckets操作的分页器
// 用于获取当前账号下的所有OSS存储桶
var paginator = client.ListBucketsPaginator(new OSS.Models.ListBucketsRequest());

// 异步迭代存储桶分页结果
Console.WriteLine("Buckets:");
await foreach (var page in paginator.IterPageAsync())
{
    // 遍历每个页面中的存储桶
    foreach (var bucket in page.Buckets ?? [])
    {
        // 输出存储桶信息：名称、存储类型和位置
        Console.WriteLine($"Bucket:{bucket.Name}, {bucket.StorageClass}, {bucket.Location}");
    }
}

```

### 使用ECSRAMRole

如果您的应用程序运行在ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中，建议您使用ECSRAMRole初始化凭证提供者。该方式底层实现是STS Token。ECSRAMRole允许您将一个角色关联到ECS实例、ECI实例或容器服务 Kubernetes 版的Worker节点，实现在实例内部自动刷新STS Token。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。如何获取ECSRAMRole，请参见[创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 添加Aliyun.Credentials依赖。
```
dotnet add package Aliyun.Credentials --source https://api.nuget.org/v3/index.json
```
- 配置ECSRAMRole作为访问凭证。
```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用
using Aliyun.Credentials.Models;

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

// 创建凭证配置，使用ECS RAM角色方式认证
var credConfig = new Aliyun.Credentials.Models.Config()
{
    // 凭证类型
    Type = "ecs_ram_role",
    // 账户RoleName，非必填，不填则自动获取，建议设置，可以减少请求up to reduce requests
    RoleName = ""
};

// 创建凭证客户端，用于获取临时访问凭证
var credClient = new Aliyun.Credentials.Client(credConfig);

// 将通用凭证转换为OSS SDK所需的凭证提供器
var credentialsProvider = new OSS.Credentials.CredentialsProviderFunc(() =>
{
    // 获取临时凭证
    var credential = credClient.GetCredential();

    // 构造OSS SDK所需的凭证对象
    return new OSS.Credentials.Credentials(
        credential.AccessKeyId,      // 临时AccessKey ID
        credential.AccessKeySecret,  // 临时AccessKey Secret
        credential.SecurityToken);   // 安全令牌（STS Token）
});

// 加载OSS客户端的默认配置
var cfg = OSS.Configuration.LoadDefault();

// 设置OSS区域
cfg.Region = region;

// 设置自定义凭证提供器
cfg.CredentialsProvider = credentialsProvider;

// 如果指定了自定义endpoint，则覆盖默认设置
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 用于获取当前角色账号下的所有OSS存储桶
var paginator = client.ListBucketsPaginator(new OSS.Models.ListBucketsRequest());

// 异步迭代存储桶分页结果
Console.WriteLine("Buckets:");
await foreach (var page in paginator.IterPageAsync())
{
    // 遍历每个页面中的存储桶
    foreach (var bucket in page.Buckets ?? [])
    {
        // 输出存储桶信息：名称、存储类型和位置
        Console.WriteLine($"Bucket:{bucket.Name}, {bucket.StorageClass}, {bucket.Location}");
    }
}
```

### 使用OIDCRoleARN

在容器服务Kubernetes版中设置了Worker节点RAM角色后，对应节点内的Pod中的应用也就可以像ECS上部署的应用一样，通过元数据服务（Meta Data Server）获取关联角色的STS Token。但如果容器集群上部署的是不可信的应用（比如部署您的客户提交的应用，代码也没有对您开放），您可能并不希望它们能通过元数据服务获取Worker节点关联实例RAM角色的STS Token。为了避免影响云上资源的安全，同时又能让这些不可信的应用安全地获取所需的STS Token，实现应用级别的权限最小化，您可以使用RRSA（RAM Roles for Service Account）功能。该方式底层实现是STS Token。阿里云容器集群会为不同的应用Pod创建和挂载相应的服务账户OIDC Token文件，并将相关配置信息注入到环境变量中，Credentials工具通过获取环境变量的配置信息，调用STS服务的AssumeRoleWithOIDC接口换取绑定角色的STS Token。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。详情请参见[通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services#task-2142941)。
- 添加Aliyun.Credentials依赖。
```
dotnet add package Aliyun.Credentials --source https://api.nuget.org/v3/index.json
```
- 配置OIDCRoleArn作为访问凭证。
```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用
using Aliyun.Credentials.Models;

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

// 创建凭证配置，使用ECS RAM角色方式认证
var credConfig = new Aliyun.Credentials.Models.Config()
{
   // 凭证类型
    Type = "oidc_role_arn",
    // 格式: acs:ram::用户Id:role/角色名
    // roleArn 可不设，但需要通过设置 ALIBABA_CLOUD_ROLE_ARN 来代替
    RoleArn = "",
    // 格式: acs:ram::用户Id:oidc-provider/OIDC身份提供商名称
    // OIDCProviderArn 可不设，但需要通过设置 ALIBABA_CLOUD_OIDC_PROVIDER_ARN 来代替
    OIDCProviderArn = "",
    // 格式: path
    // OIDCTokenFilePath 可不设，但需要通过设置 ALIBABA_CLOUD_OIDC_TOKEN_FILE 来代替
    OIDCTokenFilePath = "/Users/xxx/xxx",
    // 角色会话名称
    RoleSessionName = "",
    // 可选, 限制 STS Token 的权限
    Policy = "",
    // 可选, 限制 STS Token 的有效时间
    RoleSessionExpiration = 3600,
};

// 创建凭证客户端，用于获取临时访问凭证
var credClient = new Aliyun.Credentials.Client(credConfig);

// 将通用凭证转换为OSS SDK所需的凭证提供器
var credentialsProvider = new OSS.Credentials.CredentialsProvideFunc(() =>
{
    // 获取临时凭证
    var credential = credClient.GetCredential();

    // 构造OSS SDK所需的凭证对象
    return new OSS.Credentials.Credentials(
        credential.AccessKeyId,      // 临时AccessKey ID
        credential.AccessKeySecret,  // 临时AccessKey Secret
        credential.SecurityToken);   // 安全令牌（STS Token）
});

// 加载OSS客户端的默认配置
var cfg = OSS.Configuration.LoadDefault();

// 设置OSS区域
cfg.Region = region;

// 设置自定义凭证提供器
cfg.CredentialsProvider = credentialsProvider;

// 如果指定了自定义endpoint，则覆盖默认设置
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 用于获取当前角色账号下的所有OSS存储桶
var paginator = client.ListBucketsPaginator(new OSS.Models.ListBucketsRequest());

// 异步迭代存储桶分页结果
Console.WriteLine("Buckets:");
await foreach (var page in paginator.IterPageAsync())
{
    // 遍历每个页面中的存储桶
    foreach (var bucket in page.Buckets ?? [])
    {
        // 输出存储桶信息：名称、存储类型和位置
        Console.WriteLine($"Bucket:{bucket.Name}, {bucket.StorageClass}, {bucket.Location}");
    }
}
```

### 使用自定义访问凭证

当以上凭证配置方式不满足要求时，您可以自定义获取凭证的方式。

通过Credentials.CredentialsProvideFunc接口

```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com

// 显式设置访问凭证，仅作演示用例。实际项目中您可以通过获取环境变量方式获取
var AccessKeyId = "your AccessKeyId";  // 必须项，RAM用户或STS临时访问凭证AccessKeyId
var AccessKeySecret = "your AccessKeySecret";  // 必须项，RAM用户或STS临时访问凭证AccessKeySecret
// var SecurityToken = "your STS Token";  // 可选项，使用临时访问凭证可配置此变量

// 将通用凭证转换为OSS SDK所需的凭证提供器
var credentialsProvider = new OSS.Credentials.CredentialsProvideFunc(() =>
{
   
    // 使用长期凭证构造OSS SDK所需的凭证对象 
    return new OSS.Credentials.Credentials(
        AccessKeyId,        // RAM用户AccessKey ID
        AccessKeySecret);   // RAM用户AccessKey Secret

    // 使用临时访问凭证构造OSS SDK所需的凭证对象 
    // return new OSS.Credentials.Credentials(
    //     AccessKeyId,      // 临时AccessKey ID
    //     AccessKeySecret,  // 临时AccessKey Secret
    //     SecurityToken);   // 安全令牌（STS Token）
});

// 加载OSS客户端的默认配置
var cfg = OSS.Configuration.LoadDefault();

// 设置OSS区域
cfg.Region = region;

// 设置自定义凭证提供器
cfg.CredentialsProvider = credentialsProvider;

// 如果指定了自定义endpoint，则覆盖默认设置
if (endpoint != null)
{
    cfg.Endpoint = endpoint;
}

// 使用配置创建OSS客户端实例
using var client = new OSS.Client(cfg);

// 用于获取当前角色账号下的所有OSS存储桶
var paginator = client.ListBucketsPaginator(new OSS.Models.ListBucketsRequest());

// 异步迭代存储桶分页结果
Console.WriteLine("Buckets:");
await foreach (var page in paginator.IterPageAsync())
{
    // 遍历每个页面中的存储桶
    foreach (var bucket in page.Buckets ?? [])
    {
        // 输出存储桶信息：名称、存储类型和位置
        Console.WriteLine($"Bucket:{bucket.Name}, {bucket.StorageClass}, {bucket.Location}");
    }
}
```

## 示例代码

OSS C# SDK V2提供丰富的示例代码供参考或直接使用。
| 示例内容 | GitHub示例文件|
| [创建存储空间（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/create-buckets-using-oss-sdk-for-csharp-v2) | [PutBucket.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutBucket/Program.cs)|
| [列举存储空间（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/list-buckets-using-oss-sdk-for-csharp-v2) | [ListBuckets.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/ListBuckets/Program.cs)|
| [判断存储空间是否存在（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/determine-whether-the-bucket-exists-using-oss-sdk-for-csharp-v2) | [IsBucketExist.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/IsBucketExist/Program.cs)|
| [获取存储空间的地域（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/query-the-region-of-the-bucket-using-oss-sdk-for-csharp-v2) | [GetBucketLocation.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetBucketLocation/Program.cs)|
| [获取存储空间的信息（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/query-bucket-information-using-oss-sdk-for-csharp-v2) | [GetBucketInfo.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetBucketInfo/Program.cs)|
| [获取存储空间的存储容量（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/query-the-storage-capacity-of-a-bucket-using-oss-sdk-for-csharp-v2) | [GetBucketStat.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetBucketStat/Program.cs)|
| [删除存储空间（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/delete-buckets-using-oss-sdk-for-csharp-v2) | [DeleteBucket.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/DeleteBucket/Program.cs)|
| [简单上传（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/simple-upload-using-oss-sdk-for-csharp-v2) | [PutObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutObject/Program.cs)|
| [追加上传（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-using-oss-sdk-for-csharp-v2) | [AppendObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/AppendObject/Program.cs)|
| [分片上传（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-using-oss-sdk-for-csharp-v2) | [MultipartUpload.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/dev-2505/sample/MultipartUpload/Program.cs)|
| [表单上传（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/form-upload-using-oss-sdk-for-csharp-v2) | [PostObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/dev-2505/sample/PostObject/Program.cs)|
| [使用预签名URL上传（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/upload-objects-using-presigned-urls-generated-with-oss-sdk-for-csharp-v2) | [PresignPutObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PresignPutObject/Program.cs)|
| [下载文件到内存（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/download-objects-to-the-local-memory-using-oss-sdk-for-csharp-v2) | [GetObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetObject/Program.cs)|
| [下载文件到本地（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/download-objects-to-a-local-disk-using-oss-sdk-for-csharp-v2) | [GetObjectToFile.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetObjectToFile/Program.cs)|
| [使用预签名URL下载（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/download-objects-using-presigned-urls-generated-with-oss-sdk-for-csharp-v2) | [PresignGetObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PresignGetObject/Program.cs)|
| [拷贝对象（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/copy-objects-using-oss-sdk-for-c-v2) | [CopyObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/CopyObject/Program.cs)|
| [判断文件是否存在（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/determine-whether-an-object-exists-using-oss-sdk-for-csharp-v2) | [IsObjectExist.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/IsObjectExist/Program.cs)|
| [列举文件（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/list-objects-using-oss-sdk-for-csharp-v2) | [ListObjects.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/ListObjectsV2/Program.cs)|
| [删除文件（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/delete-objects-using-oss-sdk-for-csharp-v2) | [DeleteObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/DeleteObject/Program.cs)|
| [管理软链接（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-symbolic-links-using-oss-sdk-for-csharp-v2) | - [PutSymlink.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutSymlink/Program.cs)
- [GetSymlink.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetSymlink/Program.cs)|
| [设置对象标签（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/configure-tags-for-objects-using-oss-sdk-for-csharp-v2) | [PutObjectTagging.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutObjectTagging/Program.cs)|
| [获取对象标签（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/query-the-tags-of-an-object-using-oss-sdk-for-csharp-v2) | [GetObjectTagging.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetObjectTagging/Program.cs)|
| [删除对象标签（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/delete-tags-using-oss-sdk-for-csharp-v2) | [DeleteObjectTagging.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/DeleteObjectTagging/Program.cs)|
| [管理存储空间读写权限（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-acls-of-buckets-using-oss-sdk-for-csharp-v2) | - [PutBucketAcl.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutBucketAcl/Program.cs)
- [GetBucketAcl.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetBucketAcl/Program.cs)|
| [管理文件访问权限（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-acls-of-objects-using-oss-sdk-for-csharp-v2) | - [PutObjectAcl.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutObjectAcl/Program.cs)
- [GetObjectAcl.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetObjectAcl/Program.cs)|
| [管理版本控制（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-versioning-using-oss-sdk-for-csharp-v2) | - [PutBucketVersioning.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PutBucketVersioning/Program.cs)
- [GetBucketVersioning.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/GetBucketVersioning/Program.cs)|
| [同步处理（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/synchronous-processing-using-oss-sdk-for-csharp-v2) | [ProcessObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/ProcessObject/Program.cs)|
| [异步处理（C# SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/asynchronous-processing-using-oss-sdk-for-csharp-v2) | [AsyncProcessObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/AsyncProcessObject/Program.cs)|

[上一篇：常见问题（PHP SDK V1）](/zh/oss/developer-reference/faq-23)[下一篇：存储空间（C# SDK V2）](/zh/oss/developer-reference/manage-buckets-using-oss-sdk-for-c-2-0/)该文章对您有帮助吗？反馈
  
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