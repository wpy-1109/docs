# 为C++ SDK配置多种OSS访问凭证提供者

Source: https://help.aliyun.com/zh/oss/developer-reference/c-configure-access-credentials

---

- 为C++ SDK配置多种OSS访问凭证提供者-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 配置访问凭证（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
使用C++ SDK发起OSS请求，您需要配置访问凭证。阿里云服务会通过访问凭证验证您的身份信息和访问权限。您可以根据使用场景对认证和授权的要求，选择不同类型的访问凭证。本文介绍如何配置临时访问凭证和长期访问凭证。

## 前提条件

在配置访问凭证前，您需要安装OSS C++ SDK。详情请参见[安装（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/installation-12)。

## 初始化凭证提供者

### 凭证提供者选型

OSS支持多种方式初始化凭证提供者，您可以根据使用场景对认证和授权的要求，选择对应的方式初始化凭证提供者。
| 凭证提供者初始化方式 | 适用场景 | 是否需要提供前置的AK或STS Token | 底层实现基于的凭证 | 凭证有效期 | 凭证轮转或刷新方式|
| [方式一：使用AK](#dd657ea839xv1) | 部署运行在安全、稳定且不易受外部攻击的环境的应用程序，无需频繁轮转凭证就可以长期访问云服务 | 是 | AK | 长期 | 手动轮转|
| [方式二：使用STS Token](#3a2b4ef1697pd) | 部署运行在不可信的环境的应用程序，希望能控制访问的有效期、权限 | 是 | STS Token | 临时 | 手动刷新|
| [方式三：自定义访问凭证](#3502d8074270l) | 如果以上凭证配置方式都不满足要求时，您可以自定义获取凭证的方式 | 自定义 | 自定义 | 自定义 | 自定义|

### 方式一：使用AK

如果您的应用程序部署运行在安全、稳定且不易受外部攻击的环境中，需要长期访问您的OSS，且不能频繁轮转凭证时，您可以使用阿里云主账号或RAM用户的AK（Access Key ID、Access Key Secret）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个AK，存在安全性风险和维护复杂度增加的风险。如何获取AK，请参见[CreateAccessKey - 创建主账号或RAM用户访问密钥](https://help.aliyun.com/zh/ram/developer-reference/api-ims-2019-08-15-createaccesskey)。

#### 环境变量
警告 
阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 使用AK设置环境变量。
## Mac OS X/Linux/Unix

```
export OSS_ACCESS_KEY_ID=
export OSS_ACCESS_KEY_SECRET=
```

## Windows

```
set OSS_ACCESS_KEY_ID=
set OSS_ACCESS_KEY_SECRET=
```
- 使用环境变量来传递凭证信息。
```
auto credentialsProvider = std::make_shared();
OssClient client(Endpoint, credentialsProvider, conf);
```

#### 静态凭证

您可以在代码中使用变量来引用凭证，这些变量在运行时会被环境变量、配置文件或其他外部数据源中的实际凭证值填充。
- 配置凭证信息之后可以使用以下示例来进行信息传递。
```
std::string accessKeyId = std::getenv("ALIBABA_CLOUD_ACCESS_KEY_ID");
std::string accessKeySecret = std::getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET");

auto credentialsProvider = std::make_shared(accessKeyId, accessKeySecret, "");
OssClient client(Endpoint, credentialsProvider, conf);
```

### 方式二：使用STS Token

如果您的应用程序需要临时访问OSS，您可以使用通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个STS Token，存在安全性风险和维护复杂度增加的风险。此外，如果您需要多次临时访问OSS，您需要手动刷新STS Token。如何获取STS Token，请参见[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)。
- 使用临时身份凭证设置环境变量。
## Mac OS X/Linux/Unix

```
export OSS_ACCESS_KEY_ID=
export OSS_ACCESS_KEY_SECRET=
export OSS_SESSION_TOKEN=
```

## Windows

```
set OSS_ACCESS_KEY_ID=
set OSS_ACCESS_KEY_SECRET=
set OSS_SESSION_TOKEN=
```
- 通过环境变量来传递凭证信息。
```
auto credentialsProvider = std::make_shared();
OssClient client(Endpoint, credentialsProvider, conf);
```

### 方式三：自定义访问凭证

如果以上凭证配置方式都不满足要求时，您还可以通过实现Credential Providers接口的方式，来自定义凭证提供方式。

```
#include 
using namespace AlibabaCloud::OSS;

class CustomCredentialsProvider : public CredentialsProvider
{
public:
    CustomCredentialsProvider()
    {
    }
    ~CustomCredentialsProvider()
    {
    }

    Credentials getCredentials() override
    {
        std::string accessKeyId;
        std::string accessKeySecret;
        //std::string token;

        //TODO
        //自定义访问凭证的获取方法

         // 返回长期凭证 accessKeyId, accessKeySecret
        auto cred = Credentials(accessKeyId, accessKeySecret, "");

        // 返回 临时凭证 accessKeyId, accessKeySecret, token
        // 对于临时凭证，需要根据过期时间，刷新凭证。        
        // auto cred = Credentials(accessKeyId, accessKeySecret, token);
        
        return cred;
    }
private:
};

ClientConfiguration conf;
auto credentialsProvider = std::make_shared();
OssClient client(Endpoint, credentialsProvider, conf);

```

## 后续步骤

配置访问凭证后，您需要初始化OSSClient。详情请参见[初始化（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/initialization-12)。

[上一篇：安装（C++ SDK）](/zh/oss/developer-reference/installation-12)[下一篇：初始化（C++ SDK）](/zh/oss/developer-reference/initialization-12)该文章对您有帮助吗？反馈
  
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