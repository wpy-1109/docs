# 使用C++SDK通过图片处理参数和样式处理图片

Source: https://help.aliyun.com/zh/oss/developer-reference/image-processing

---

- 使用C++SDK通过图片处理参数和样式处理图片-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 图片处理（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
图片处理是OSS提供的海量、安全、低成本、高可靠的图片处理服务。原始图片上传到OSS后，您可以通过简单的RESTful接口，在任何时间、任何地点、任何互联网设备上对图片进行处理。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。

## 使用图片处理参数处理图片

### 使用单个图片处理参数处理图片

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
    /* 指定原图所在的Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 指定原图名称。如果图片不在Bucket根目录，需携带图片完整路径，例如exampledir/example.jpg。*/
    std::string ObjectName = "exampledir/example.jpg";

     /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 将图片缩放为固定宽高100 px后保存在本地。*/
    std::string Process = "image/resize,m_fixed,w_100,h_100";
    GetObjectRequest request(BucketName, ObjectName);
    request.setProcess(Process);
    auto outcome = client.GetObject(request);
    if (outcome.isSuccess()) {
    std::cout 
### 使用多个图片处理参数处理图片

使用多个图片处理参数处理图片时，多个参数之间以正斜线（/）分隔。

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
    /* 指定原图所在的Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 指定原图名称。如果图片不在Bucket根目录，需携带图片完整路径，例如exampledir/example.jpg。*/
    std::string ObjectName = "exampledir/example.jpg";

     /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 将图片缩放为固定宽高100 px后，再旋转90°，之后保存在本地。*/
    std::string Process = "image/resize,m_fixed,w_100,h_100/rotate,90";
    GetObjectRequest request(BucketName, ObjectName);
    request.setProcess(Process);
    auto outcome = client.GetObject(request);
    if (outcome.isSuccess()) {
    std::cout 
## 使用图片样式处理图片
- 创建图片样式。您可以在一个样式（Style）中包含多个图片处理参数，快速实现复杂的图片处理操作。具体操作，请参见[图片样式](https://help.aliyun.com/zh/oss/user-guide/image-styles#concept-mr2-x3c-wdb)。
- 使用图片样式处理图片。
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
    /* 指定原图所在的Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 指定原图名称。如果图片不在Bucket根目录，需携带图片完整路径，例如exampledir/example.jpg。*/
    std::string ObjectName = "exampledir/example.jpg";

     /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 使用图片样式处理图片。其中，yourCustomStyleName填写步骤1创建的图片样式名称。*/
    std::string Process = "style/yourCustomStyleName";
    GetObjectRequest request(BucketName, ObjectName);
    request.setProcess(Process);
    auto outcome = client.GetObject(request);
    if (outcome.isSuccess()) {
    std::cout 
## 图片处理持久化

您可以通过ImgSaveAs接口将图片保存至当前存储空间。以下代码用于图片处理持久化操作：

```
#include 
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 指定Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 指定原图名称。如果图片不在Bucket根目录，需携带文件完整路径，例如example/example.jpg。*/
    std::string SourceObjectName = "example/example.jpg";
    /* 指定处理后图片名称。如果图片不在Bucket根目录，需携带文件完整访问路径，例如exampledir/example.jpg。*/
    std::string TargetObjectName = "exampledir/example.jpg";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 将图片缩放为固定宽高100 px后转存到当前Bucket。*/
    std::string Process = "image/resize,m_fixed,w_100,h_100";
    std::stringstream ss;
    ss  
## 生成带图片处理参数的文件签名URL

通过文件URL访问私有权限文件时需要携带签名。OSS不支持在带签名的URL后直接添加图片处理参数。如果您需要对私有权限的图片进行处理，您需要将图片处理参数加入到签名中，代码示例如下：

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
    /* 填写图片所在的Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 指定图片名称。如果图片不在Bucket根目录，需携带文件完整路径，例如exampledir/example.jpg。*/
    std::string ObjectName = "exampledir/example.jpg";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 生成带图片处理参数的文件签名URL。*/
    std::string Process = "image/resize,m_fixed,w_100,h_100";
    GeneratePresignedUrlRequest request(BucketName, ObjectName, Http::Get);
    request.setProcess(Process);
    /* 使用URL的最大时间限制为32400。*/
    auto outcome = client.GeneratePresignedUrl(request);
	
    if (outcome.isSuccess()) {
    std::cout 
## 图片处理工具

您可以通过可视化图片处理工具[ImageStyleViewer](https://gosspublic.alicdn.com/image/index.html)直观地看到OSS图片处理结果。

## 相关文档
- 关于图片处理支持的参数说明，请参见[处理参数](https://help.aliyun.com/zh/oss/user-guide/overview-17/#section-tx1-qtj-ar8)。
- 关于图片处理的样式说明，请参见[图片样式](https://help.aliyun.com/zh/oss/user-guide/image-styles#concept-mr2-x3c-wdb)。

[上一篇：日志转存（C++ SDK）](/zh/oss/developer-reference/logging-10)[下一篇：常见问题（C++ SDK）](/zh/oss/developer-reference/faq-20)该文章对您有帮助吗？反馈
  
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