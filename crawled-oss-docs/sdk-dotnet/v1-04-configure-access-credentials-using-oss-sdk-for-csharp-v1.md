# C#SDK访问凭证配置方法选型指南

Source: https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-using-oss-sdk-for-csharp-v1

---

- C#SDK访问凭证配置方法选型指南-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 配置访问凭证（C# SDK V1）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
使用C# SDK发起OSS请求，您需要配置访问凭证。阿里云服务会通过访问凭证验证您的身份信息和访问权限。您可以根据使用场景对认证和授权的要求，选择不同的方式提供凭证。

## 注意事项
- 如果您希望获取关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 如果您希望创建RAM用户的AccessKey，请参见[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。

## 凭证提供者选型参考

OSS支持多种方式初始化凭证提供者，您可以根据使用场景对认证和授权的要求，选择对应的方式初始化凭证提供者。
| 凭证提供者初始化方式 | 适用场景 | 是否需要提供前置的AK或STS Token | 底层实现基于的凭证 | 凭证有效期 | 凭证轮转或刷新方式|
| [使用RAM用户的AK](#dd657ea839xv1) | 部署运行在安全、稳定且不易受外部攻击的环境的应用程序，无需频繁轮转凭证就可以长期访问云服务 | 是 | AK | 长期 | 手动轮转|
| [使用STS临时访问凭证](#3a2b4ef1697pd) | 部署运行在不可信的环境的应用程序，希望能控制访问的有效期、权限 | 是 | STS Token | 临时 | 手动刷新|
| [使用RAMRoleARN](#cf008d6649g6n) | 需要授权访问云服务，例如跨阿里云账号访问云服务的应用程序 | 是 | STS Token | 临时 | 自动刷新|
| [使用ECSRAMRole](#bb4c2dbc56ayp) | 部署运行在阿里云的ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中的应用程序 | 否 | STS Token | 临时 | 自动刷新|
| [使用OIDCRoleARN](#c3176515f0csi) | 部署运行在阿里云的容器服务Kubernetes版的Worker节点中的不可信应用程序 | 否 | STS Token | 临时 | 自动刷新|
| [使用CredentialsURI](#125b4be3a2ey2) | 需要通过外部系统获取访问凭证的应用程序 | 否 | STS Token | 临时 | 自动刷新|
| [自定义访问凭证](#b22ad1c8bdpzv) | 如果以上凭证配置方式都不满足要求时，您可以自定义获取凭证的方式 | 自定义 | 自定义 | 自定义 | 自定义|

## 常用配置示例

### 使用RAM用户的AK

如果您的应用程序部署运行在安全、稳定且不易受外部攻击的环境中，需要长期访问您的OSS，且不能频繁轮转凭证时，您可以使用阿里云主账号或RAM用户的AK（Access Key ID、Access Key Secret）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个AK，存在安全性风险和维护复杂度增加的风险。如何获取AK，请参见[CreateAccessKey - 创建主账号或RAM用户访问密钥](https://help.aliyun.com/zh/ram/developer-reference/api-ims-2019-08-15-createaccesskey)。

#### 环境变量
警告 
阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 使用AK设置环境变量。
## Mac OS X/Linux/Unix

```
export ALIBABA_CLOUD_ACCESS_KEY_ID=
export ALIBABA_CLOUD_ACCESS_KEY_SECRET=
```

## Windows

```
set ALIBABA_CLOUD_ACCESS_KEY_ID=
set ALIBABA_CLOUD_ACCESS_KEY_SECRET=
```
- 使用环境变量来传递凭证信息。
```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET。
var accessKeyId = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET");
var credentialsProvider = new DefaultCredentialsProvider(new DefaultCredentials(accessKeyId, accessKeySecret, ""));   

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);                                                                                                                        
```

#### 静态凭证

以下示例代码展示了如何对访问凭据直接进行硬编码，显式设置要使用的访问密钥。
警告 
请勿将访问凭据嵌入到生产环境的应用程序中，此方法仅用于测试目的。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET。
var accessKeyId = "LTAI5tQQx1DWEYK7********" ;
var accessKeySecret = "s5LkMqKmmKbt3zjs7MNJTj********" ;
var credentialsProvider = new DefaultCredentialsProvider(new DefaultCredentials(accessKeyId, accessKeySecret, ""));   

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);     
```

### 使用STS临时访问凭证

如果您的应用程序需要临时访问OSS，您可以使用通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个STS Token，存在安全性风险和维护复杂度增加的风险。此外，如果您需要多次临时访问OSS，您需要手动刷新STS Token。
重要 - 如果您希望通过OpenAPI的方式简单快速获取到STS临时访问凭证，请参见[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)。
- 如果您希望通过SDK的方式获取STS临时访问凭证，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#section-rjh-18m-7kp)。
- 请注意，STS Token在生成的时候需要指定过期时间，过期后自动失效不能再使用。
- 如果您希望获取关于STS服务的接入点列表，请参见[服务接入点](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-endpoint)。

#### 环境变量
- 使用临时身份凭证设置环境变量。
## Mac OS X/Linux/Unix

```
export ALIBABA_CLOUD_ACCESS_KEY_ID=
export ALIBABA_CLOUD_ACCESS_KEY_SECRET=
export ALIBABA_CLOUD_SECURITY_TOKEN=
```

## Windows

```
set OSS_ACCESS_KEY_ID=
set OSS_ACCESS_KEY_SECRET=
set OSS_SESSION_TOKEN=
```
- 通过环境变量来传递凭证信息。
```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET 和 OSS_SESSION_TOKEN。
var accessKeyId = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID");
var accessKeySecret = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET");
var token = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_SECURITY_TOKEN");

var credentialsProvider = new DefaultCredentialsProvider(new DefaultCredentials(accessKeyId, accessKeySecret, token));

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);

```

#### 静态凭证

您可以在应用程序中对凭据直接进行硬编码，显式设置要使用的临时访问密钥。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET 和 OSS_SESSION_TOKEN。
var accessKeyId = "STS.NTZdStF79CVRTQuWCfXTT****";
var accessKeySecret = "5rm8PfEiK8enp56zzAMX4RbZUraoKbWXvCf1xAuT****"
var token = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_SECURITY_TOKEN");

var credentialsProvider = new DefaultCredentialsProvider(new DefaultCredentials(accessKeyId, accessKeySecret, token));

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);

```

## 更多场景化配置示例

### 使用RAMRoleARN

如果您的应用程序需要授权访问OSS，例如跨阿里云账号访问OSS，您可以使用RAMRoleARN初始化凭证提供者。该方式底层实现是STS Token。通过指定RAM角色的ARN（Alibabacloud Resource Name），Credentials工具会前往STS服务获取STS Token，并在会话到期前自动刷新STS Token。此外，您还可以通过为`policy`赋值来限制RAM角色到一个更小的权限集合。
重要 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请考虑创建新的AK进行轮换。
- 如需获取RAMRoleARN，请直接访问[CreateRole - 创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 安装阿里云凭证库，具体请参见[管理访问凭证](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-net-access-credentials)。
- 配置访问凭证。
```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

class CredentialsProviderWrapper : ICredentialsProvider
{
    private Aliyun.Credentials.Client client;
    public CredentialsProviderWrapper(Aliyun.Credentials.Client client)
    {
        this.client = client;
    }

    public ICredentials GetCredentials()
    {
        var accessKeyId = client.GetAccessKeyId();
        var accessKeySecret = client.GetAccessKeySecret();
        var token = client.GetSecurityToken();
        return new DefaultCredentials(accessKeyId, accessKeySecret, token);
    }

    public void SetCredentials(ICredentials creds)
    {
    }
};

var config = new Aliyun.Credentials.Models.Config()
{
    Type = "ram_role_arn",
    AccessKeyId = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID"),
    AccessKeySecret = Environment.GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
    // 以下操作默认直接填入参数数值，您也可以通过添加环境变量，并使用Environment.GetEnvironmentVariable("")的方式来get对应参数
    // 要扮演的RAM角色ARN，示例值：acs:ram::123456789012****:role/adminrole
    RoleArn = "", // RoleArn默认环境变量规范名称ALIBABA_CLOUD_ROLE_ARN
    // 角色会话名称
    RoleSessionName = "", // RoleSessionName默认环境变量规范名称ALIBABA_CLOUD_ROLE_SESSION_NAME
};
var credentialsClient = new Aliyun.Credentials.Client(config);

var credentialsProvider = new CredentialsProviderWrapper(credentialsClient);

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);

```

### 使用ECSRAMRole

如果您的应用程序运行在ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中，建议您使用ECSRAMRole初始化凭证提供者。该方式底层实现是STS Token。ECSRAMRole允许您将一个角色关联到ECS实例、ECI实例或容器服务 Kubernetes 版的Worker节点，实现在实例内部自动刷新STS Token。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。如何获取ECSRAMRole，请参见[CreateRole - 创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 安装阿里云凭证库，具体请参见[管理访问凭证](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-net-access-credentials)。
- 配置ECSRAMRole作为访问凭证。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

class CredentialsProviderWrapper : ICredentialsProvider
{
    private Aliyun.Credentials.Client client;
    public CredentialsProviderWrapper(Aliyun.Credentials.Client client)
    {
        this.client = client;
    }

    public ICredentials GetCredentials()
    {
        var accessKeyId = client.GetAccessKeyId();
        var accessKeySecret = client.GetAccessKeySecret();
        var token = client.GetSecurityToken();
        return new DefaultCredentials(accessKeyId, accessKeySecret, token);
    }

    public void SetCredentials(ICredentials creds)
    {
    }
};

var config = new Aliyun.Credentials.Models.Config()
{
    Type = "ecs_ram_role",
    // 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数
    RoleName = ""     
};
var credentialsClient = new Aliyun.Credentials.Client(config);

var credentialsProvider = new CredentialsProviderWrapper(credentialsClient);

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);

```

### 使用OIDCRoleARN

在容器服务Kubernetes版中设置了Worker节点RAM角色后，对应节点内的Pod中的应用也就可以像ECS上部署的应用一样，通过元数据服务（Meta Data Server）获取关联角色的STS Token。但如果容器集群上部署的是不可信的应用（比如部署您的客户提交的应用，代码也没有对您开放），您可能并不希望它们能通过元数据服务获取Worker节点关联实例RAM角色的STS Token。为了避免影响云上资源的安全，同时又能让这些不可信的应用安全地获取所需的STS Token，实现应用级别的权限最小化，您可以使用RRSA（RAM Roles for Service Account）功能。该方式底层实现是STS Token。阿里云容器集群会为不同的应用Pod创建和挂载相应的服务账户OIDC Token文件，并将相关配置信息注入到环境变量中，Credentials工具通过获取环境变量的配置信息，调用STS服务的AssumeRoleWithOIDC接口换取绑定角色的STS Token。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。详情请参见[通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services#task-2142941)。

注入的环境变量如下：

ALIBABA_CLOUD_ROLE_ARN：RAM角色名称ARN；

ALIBABA_CLOUD_OIDC_PROVIDER_ARN：OIDC提供商ARN；

ALIBABA_CLOUD_OIDC_TOKEN_FILE：OIDC Token文件路径；

配置OIDCRoleArn作为访问凭证。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

class CredentialsProviderWrapper : ICredentialsProvider
{
    private Aliyun.Credentials.Client client;
    public CredentialsProviderWrapper(Aliyun.Credentials.Client client)
    {
        this.client = client;
    }

    public ICredentials GetCredentials()
    {
        var accessKeyId = client.GetAccessKeyId();
        var accessKeySecret = client.GetAccessKeySecret();
        var token = client.GetSecurityToken();
        return new DefaultCredentials(accessKeyId, accessKeySecret, token);
    }

    public void SetCredentials(ICredentials creds)
    {}
};

var config = new Aliyun.Credentials.Models.Config()
{
    Type = "oidc_role_arn",
    // RAM角色名称ARN，可以通过环境变量ALIBABA_CLOUD_ROLE_ARN设置RoleArn
    RoleArn = "",
    // OIDC提供商ARN，可以通过环境变量ALIBABA_CLOUD_OIDC_PROVIDER_ARN设置OidcProviderArn
    OIDCProviderArn = "",
    // OIDC Token文件路径，可以通过环境变量ALIBABA_CLOUD_OIDC_TOKEN_FILE设置OidcTokenFilePath
    OIDCTokenFilePath = "",
    // 角色会话名称，可以通过环境变量ALIBABA_CLOUD_ROLE_SESSION_NAME设置RoleSessionName
    RoleSessionName = "",
    // 设置更小的权限策略，非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
    Policy = "",
    RoleSessionExpiration = 3600  
};
var credentialsClient = new Aliyun.Credentials.Client(config);
var credentialsProvider = new CredentialsProviderWrapper(credentialsClient);
//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";
var conf = new ClientConfiguration();
var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);
```

### 使用CredentialsURI

如果您的应用程序需要通过外部系统获取阿里云凭证，从而实现灵活的凭证管理和无密钥访问，您可以使用CredentialsURI初始化凭证提供者。该方式底层实现是STS Token。Credentials工具通过您提供的URI获取STS Token，完成凭证客户端初始化。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。需要注意的是，提供CredentialsURI响应的后端服务需要实现STS Token的自动刷新逻辑，确保您的应用程序始终能获取到有效凭证。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

class CredentialsProviderWrapper : ICredentialsProvider
{
    private Aliyun.Credentials.Client client;
    public CredentialsProviderWrapper(Aliyun.Credentials.Client client)
    {
        this.client = client;
    }

    public ICredentials GetCredentials()
    {
        var accessKeyId = client.GetAccessKeyId();
        var accessKeySecret = client.GetAccessKeySecret();
        var token = client.GetSecurityToken();
        return new DefaultCredentials(accessKeyId, accessKeySecret, token);
    }

    public void SetCredentials(ICredentials creds)
    {}
};

var config = new Aliyun.Credentials.Models.Config()
{
    // 凭证类型。
    Type = "credentials_uri",
    // 获取凭证的 URI，格式为http://local_or_remote_uri/，可以通过环境变量ALIBABA_CLOUD_CREDENTIALS_URI设置CredentialsUri
    CredentialsURI = "" 
};
var credentialsClient = new Aliyun.Credentials.Client(config);
var credentialsProvider = new CredentialsProviderWrapper(credentialsClient);
//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";
var conf = new ClientConfiguration();
var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);
```

### 自定义访问凭证

如果以上凭证配置方式都不满足要求时，您还可以通过实现Credential Providers接口的方式，来自定义凭证提供方式。

```
using Aliyun.OSS;
using Aliyun.OSS.Common;
using Aliyun.OSS.Common.Authentication;

class CustomCredentialsProvider : ICredentialsProvider
{
    public CustomCredentialsProvider()
    {
    }

    public ICredentials GetCredentials()
    {
        //TODO
        //自定义访问凭证的获取方法

        string accessKeyId;
        string accessKeySecret;
        //string token;

        // 返回长期凭证 access_key_id, access_key_secrect
        return new DefaultCredentials(accessKeyId, accessKeySecret, "");

        // 返回 临时凭证 access_key_id, access_key_secrect, token
        // 对于临时凭证，需要根据过期时间，刷新凭证。
        // return new DefaultCredentials(accessKeyId, accessKeySecrect, token);
    }

    public void SetCredentials(ICredentials creds)
    {
    }
};

var credentialsProvider = new CustomCredentialsProvider();

//  填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
const string endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

// 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。
const string region = "cn-hangzhou";

var conf = new ClientConfiguration();

var client = new OssClient(endpoint, credentialsProvider, conf);
client.SetRegion(region);

```

### 如何查看RAM用户的AK？是否可以查看旧的AccessKey Secret？
- 如需查看RAM用户的AK，请直接参考文档[查看RAM用户的AccessKey信息](https://help.aliyun.com/zh/ram/user-guide/view-the-accesskey-pairs-of-a-ram-user)。
- RAM用户的AccessKey Secret仅在创建时显示，之后无法查看，若您已经遗忘了的话无法找回。您可以直接访问[RAM控制台](https://ram.console.aliyun.com/users)选择具体用户，并创建新的AccessKey进行轮换。详细请参见[创建AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)。

### 使用RAM用户的AK进行上传文件时，报错AccessDenied如何排查？

上传文件时出现AccessDenied的问题，通常是因为使用了错误的AK信息或没有给RAM用户添加上传文件的权限，您可以按照以下步骤检查：
- 检查您使用的RAM用户的AK是否正确，请直接参考文档[查看RAM用户的AccessKey信息](https://help.aliyun.com/zh/ram/user-guide/view-the-accesskey-pairs-of-a-ram-user)。
- RAM用户的AccessKey Secret仅在创建时显示，之后无法查看，若您已经遗忘了的话无法找回。您可以直接访问[RAM控制台](https://ram.console.aliyun.com/users)选择具体用户，并创建新的AccessKey进行轮换。详细请参见[创建AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair)。
- 登录[RAM控制台](https://ram.console.aliyun.com/users)选择具体用户，给RAM用户添加上传文件到OSS的权限。

### 在使用外网Endpoint访问OSS时，报错无法连接该如何排查？

出现外网Endpoint无法连接的问题，通常是因为使用了错误的Endpoint地址或Bucket所在地域与请求的Endpoint不匹配。请您按照以下步骤检查：
- 确认Bucket所在地域：登录阿里云控制台，找到您的Bucket，确认其所在地域。
- 使用正确的Endpoint：根据Bucket所在地域，使用对应的外网Endpoint。例如，如果Bucket位于华东1（杭州），则应使用oss-cn-hangzhou.aliyuncs.com。各地域的Endpoint信息请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)。
- 检查网络连接：确保您的网络环境可以正常访问互联网，避免因网络问题导致连接失败。

### 如果遇到报错问题该如何查询具体的错误类型？

关于错误类型的查询，OSS文档提供了[EC错误码](https://help.aliyun.com/zh/oss/user-guide/error-codes/)供您参阅，例如关于认证方面的常见报错问题，请参见[02-AUTH](https://help.aliyun.com/zh/oss/user-guide/02-auth/)。

[上一篇：高级配置（C# SDK V1）](/zh/oss/developer-reference/advanced-config-using-oss-sdk-for-csharp-v1/)[下一篇：初始化（C# SDK V1）](/zh/oss/developer-reference/initialization-ossclient)该文章对您有帮助吗？反馈
  
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