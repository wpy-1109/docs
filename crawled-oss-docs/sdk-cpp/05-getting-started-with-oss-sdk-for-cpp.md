# C++SDK基础操作示例代码

Source: https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-cpp

---

- C++SDK基础操作示例代码-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 快速入门（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本节介绍如何快速使用OSS C++ SDK完成常见操作，如创建存储空间（Bucket）、上传文件、下载文件（Object）等。
说明 
示例代码中的conf为ClientConfiguration的实例，ClientConfiguration是OssClient的配置类，您可以通过此配置类来配置代理、连接超时、最大连接数等参数。更多信息，请参见[初始化（C++ SDK）](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#concept-32133-zh)。

## 创建存储空间

存储空间是OSS的全局命名空间，相当于数据的容器，可以存储若干文件。
说明 
关于存储空间命名规范的更多信息，请参见[基本概念](https://help.aliyun.com/zh/oss/terms-2#concept-izx-fmt-tdb)中的命名规范。关于获取Endpoint的更多信息，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。

以下代码用于创建examplebucket存储空间。

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
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 指定新创建Bucket的名称、存储类型和ACL。*/
    CreateBucketRequest request(BucketName, StorageClass::IA, CannedAccessControlList::PublicReadWrite);

    /* 创建Bucket。*/
    auto outcome = client.CreateBucket(request);

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 上传文件

以下代码用于上传文件到OSS。

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
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写文件完整路径，例如exampledir/exampleobject.txt。文件完整路径中不能包含Bucket名称。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 上传文件。*/
    /* 填写本地文件完整路径，例如D:\\localpath\\examplefile.txt，其中localpath为本地文件examplefile.txt所在本地路径。*/
    auto outcome = client.PutObject(BucketName, ObjectName,"D:\\localpath\\examplefile.txt");

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 下载文件

以下代码用于将指定的OSS文件下载到本地文件。

```
#include 
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
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 下载Object到本地文件examplefile.txt，并保存到指定的本地路径中（D:\\localpath）。如果指定的本地文件存在会覆盖，不存在则新建。*/
    /* 如果未指定本地路径，则下载后的文件默认保存到示例程序所属项目对应本地路径中。*/
    std::string FileNametoSave = "D:\\localpath\\examplefile.txt";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 下载Object到本地文件。*/
    GetObjectRequest request(BucketName, ObjectName);
    request.setResponseStreamFactory([=]() {return std::make_shared(FileNametoSave, std::ios_base::out | std::ios_base::in | std::ios_base::trunc| std::ios_base::binary); });

    auto outcome = client.GetObject(request);

    if (outcome.isSuccess()) {    
        std::cout 
## 列举文件

以下代码用于列举存储空间bucket下的文件。默认列举100个文件。

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
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 列举文件。*/
    ListObjectsRequest request(BucketName);
    auto outcome = client.ListObjects(request);

    if (!outcome.isSuccess()) {    
        /* 异常处理。*/
        std::cout 
## 删除文件

以下代码用于删除指定文件。

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
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写文件完整路径，例如exampledir/exampleobject.txt。文件完整路径中不能包含Bucket名称。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    DeleteObjectRequest request(BucketName, ObjectName);

    /* 删除文件。*/
    auto outcome = client.DeleteObject(request);

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 相关文档
- 关于快速入门涉及的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc)。
- 关于创建存储空间的API接口说明，请参见[PutBucket](https://help.aliyun.com/zh/oss/developer-reference/putbucket#reference-wdh-fj5-tdb)。
- 关于上传文件的API接口说明，请参见[PutObject](https://help.aliyun.com/zh/oss/developer-reference/putobject#reference-l5p-ftw-tdb)。
- 关于下载文件的API接口说明，请参见[GetObject](https://help.aliyun.com/zh/oss/developer-reference/getobject#reference-ccf-rgd-5db)。
- 关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)。
- 关于删除文件的API接口说明，请参见[DeleteObject](https://help.aliyun.com/zh/oss/developer-reference/deleteobject#reference-iqc-mqv-wdb)。

[上一篇：初始化（C++ SDK）](/zh/oss/developer-reference/initialization-12)[下一篇：存储空间（C++ SDK）](/zh/oss/developer-reference/buckets-5/)该文章对您有帮助吗？反馈
  
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