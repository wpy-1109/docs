# C++SDK客户端初始化与配置

Source: https://help.aliyun.com/zh/oss/developer-reference/initialization-12

---

- C++SDK客户端初始化与配置-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 初始化（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OssClient用于管理存储空间（Bucket）和文件（Object）等OSS资源。使用C++ SDK发起OSS请求时，您需要初始化一个OssClient实例，并根据需要修改ClientConfiguration的默认配置项。

## 新建OssClient
重要 - OssClient是线程安全的，允许多线程访问同一实例。您可以结合业务需求，复用同一个OssClient实例，也可以创建多个OssClient实例，分别使用。
- InitializeSdk()和ShutdownSdk()是全局性接口，在程序生命周期内只需要调用一次。

### V4签名（推荐）

推荐使用更安全的V4签名算法。使用V4签名初始化时，除指定Endpoint以外，您还需要指定阿里云通用Region ID作为发起请求地域的标识，示例值为`cn-hangzhou`。同时声明`SignatureVersionType::V4`。OSS C++ SDK 1.10.0及以上版本支持V4签名。

以使用OSS域名新建OSSClient时使用V4签名为例，其他通过自定义域名、STS等新建OSSClient的场景可参考以下示例执行相应修改。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

### V1签名（不推荐）
重要 
阿里云对象存储OSS自2025年03月01日起不再对新用户（即新UID ）开放使用V1签名，并将于2025年09月01日起停止更新与维护且不再对新增Bucket开放使用V1签名。请尽快切换到V4签名，避免影响服务。更多信息，请参见[公告说明](https://www.aliyun.com/notice/detail/116888)。

### 使用OSS域名新建OSSClient

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);   

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

### 使用自定义域名新建OSSClient

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写自定义域名。*/
    std::string Endpoint = "yourEndpoint";
    
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.isCname = true;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);   

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

### 使用STS新建OSSClient

STS临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。关于如何获取STS临时访问凭证的具体操作，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#concept-xzh-nzk-2gb)。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
        
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已通过环境变量设置临时访问密钥和安全令牌。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf); 

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

## 配置OssClient

ClientConfiguration是OssClient的配置类，您可通过此配置类来配置代理、连接超时、最大连接数等参数。

通过OssClient可设置的参数如下：
| 参数 | 描述|
| isCname | 是否支持直接使用Cname作为Endpoint。默认不支持。|
| userAgent | 用户代理，指HTTP的User-Agent头。默认代理为aliyun-sdk-cpp/1.X.X。|
| maxConnections | 连接池数。默认为16个。|
| requestTimeoutMs | 请求超时时间。请求超时没有收到数据将会关闭连接，默认为10000ms。|
| connectTimeoutMs | 建立连接的超时时间。默认为5000ms。|
| retryStrategy | 自定义失败重试策略。|
| proxyScheme | 代理协议，默认为HTTP。|
| proxyPort | 代理服务器端口。|
| proxyPassword | 代理服务器验证的密码。|
| proxyUserName | 代理服务器验证的用户名。|
| verifySSL | 是否开启SSL证书校验，默认关闭。
说明 
C++ SDK 1.8.2及以上版本默认开启SSL证书校验。|
| caPath | 用于设置CA证书根路径，当verifySSL为true时有效，默认为空。|
| caFile | 用于设置CA证书路径，当verifySSL为true时有效，默认为空。|
| enableCrc64 | 是否开启CRC64校验，默认开启。|
| enableDateSkewAdjustment | 是否开启HTTP请求时间自动修正，默认开启。|
| sendRateLimiter | 上传限速（单位KB/s）。|
| recvRateLimiter | 下载限速（单位KB/s）。|

## 设置超时时间

以下代码用于设置超时时间：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    
    /* 初始化网络等资源。*/
    InitializeSdk();
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;

    /* 设置连接池数，默认为16个。*/
    conf.maxConnections = 20;

    /* 设置请求超时时间，超时没有收到数据就关闭连接，默认为10000ms。*/
    conf.requestTimeoutMs = 8000;

    /* 设置建立连接的超时时间，默认为5000ms。*/
    conf.connectTimeoutMs = 8000;

    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);  
    client.SetRegion(Region);

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

## 设置SSL证书校验

C++ SDK 1.8.2及以上的版本默认自动开启SSL证书校验。如果出现SSL证书校验失败，您需要根据实际情况设置正确的证书路径，或者关闭SSL证书校验。

以下代码用于设置SSL证书校验：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    
    /* 初始化网络等资源。*/
    InitializeSdk();
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;

    /* 设置SSL证书校验开关，默认为true，即开启证书校验。*/
    conf.verifySSL = true;

    /* 设置CA证书根路径，当verifySSL为true时有效，默认为空。*/
    conf.caPath = "/etc/ssl/certs/";

    /* 设置CA证书路径，当verifySSL为true时有效，默认为空。*/
    conf.caFile = "/etc/ssl/certs/ca-certificates.crt";;

    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);  
    client.SetRegion(Region);

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

## 设置限速处理

以下代码用于设置上传或下载限速：

```
#include 
#include 

using namespace AlibabaCloud::OSS;

class UserRateLimiter : public RateLimiter
{
public:
    UserRateLimiter() : rate_(0) {};
    ~UserRateLimiter() {};
    virtual void setRate(int rate) { rate_ = rate; };
    virtual int Rate() const { return rate_; };
private:
    int rate_;
};

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;

    auto sendrateLimiter = std::make_shared();
    auto recvrateLimiter = std::make_shared();
    conf.sendRateLimiter = sendrateLimiter;
    conf.recvRateLimiter = recvrateLimiter;

    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 设置下载限速（单位KB/s）。*/
    recvrateLimiter->setRate(256);

    /* 设置上传限速（单位KB/s）。*/
    sendrateLimiter->setRate(256);

    /* 上传文件。yourLocalFilename填写本地文件完整路径。*/
    auto outcome = client.PutObject(BucketName, ObjectName, "yourLocalFilename");  

    /* 上传过程中更新上传限速（单位KB/s）。*/
    sendrateLimiter->setRate(300);

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

## 设置重试策略

以下代码用于设置重试策略：

```
#include 
#include 

using namespace AlibabaCloud::OSS;

class UserRetryStrategy : public RetryStrategy
{
public:

    /* maxRetries表示最大重试次数，scaleFactor为重试等待时间的尺度因子。*/
    UserRetryStrategy(long maxRetries = 3, long scaleFactor = 300) :
        m_scaleFactor(scaleFactor), m_maxRetries(maxRetries)  
    {}

    /* 您可以自定义shouldRetry函数，该函数用于判断是否进行重试。*/
    bool shouldRetry(const Error & error, long attemptedRetries) const;

    /* 您可以自定义calcDelayTimeMs函数，该函数用于计算重试的延迟等待时间。*/
    long calcDelayTimeMs(const Error & error, long attemptedRetries) const;

private:
    long m_scaleFactor;
    long m_maxRetries;
};

bool UserRetryStrategy::shouldRetry(const Error & error, long attemptedRetries) const
{    
    if (attemptedRetries >= m_maxRetries)
        return false;

    long responseCode = error.Status();

    //http code
    if ((responseCode == 403 && error.Message().find("RequestTimeTooSkewed") != std::string::npos) ||
        (responseCode > 499 && responseCode (5);
    conf.retryStrategy = defaultRetryStrategy;

    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);  
    client.SetRegion(Region);

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

## 设置代理服务器

以下代码用户设置代理服务器：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    
    /* 初始化网络等资源。*/
    InitializeSdk();
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;

    /* 设置代理服务地址。*/
    conf.proxyHost = "yourProxyHost";

    /* 设置代理服务端口。*/
    conf.proxyPort = 1234;

    /* 设置代理服务器验证的用户名,可选。*/
    conf.proxyUserName = "yourProxyUserName";

    /* 设置代理服务器验证的密码,可选。*/
    conf.proxyPassword = "yourProxyPassword";

    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 释放网络等资源。*/
    ShutdownSdk();
    return 0;
}
```

[上一篇：配置访问凭证（C++ SDK）](/zh/oss/developer-reference/c-configure-access-credentials)[下一篇：快速入门（C++ SDK）](/zh/oss/developer-reference/getting-started-with-oss-sdk-for-cpp)该文章对您有帮助吗？反馈
  
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