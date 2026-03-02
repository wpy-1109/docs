# 使用C++ SDK管理存储空间的清单配置

Source: https://help.aliyun.com/zh/oss/developer-reference/bucket-inventory-4

---

- 使用C++ SDK管理存储空间的清单配置-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 存储空间清单（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何添加、查看、批量列举和删除存储空间（Bucket）的清单（Inventory）配置。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。
- 请确保您拥有调用添加、查看、列举和删除存储空间清单配置的权限。Bucket所有者默认拥有此类权限，如果您无此类权限，请先向Bucket所有者申请对应操作的权限。
- 单个Bucket最多只能有1000条清单配置。
- 配置清单的源Bucket与存放导出的清单文件所在的目标Bucket必须位于同一个Region。

## 添加清单配置

以下代码用于为某个Bucket添加清单配置：

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

    InventoryConfiguration inventoryConf;
    /* 指定清单规则名称，该名称在当前Bucket下必须全局唯一。*/
    inventoryConf.setId("inventoryId");

    /* 清单配置是否启用的标识，可选值为true或false。*/
    inventoryConf.setIsEnabled(true);

    /* (可选)清单筛选的前缀。指定前缀后，清单将筛选出符合前缀的Object。*/
    inventoryConf.setFilter(InventoryFilter("objectPrefix"));

    InventoryOSSBucketDestination dest;
    /* 导出清单文件的文件格式。*/
    dest.setFormat(InventoryFormat::CSV);
    /* 存储空间拥有者的账户UID。*/
    dest.setAccountId("10988548********");
    /* 指定角色名称，该角色需要拥有读取源存储空间所有文件以及向目标存储空间写入文件的权限，格式为acs:ram::uid:role/rolename。*/
    dest.setRoleArn("acs:ram::10988548********:role/inventory-test");
    /* 存放导出的清单文件的存储空间。*/
    dest.setBucket("yourDstBucketName");
    /* 清单文件的存储路径前缀。*/
    dest.setPrefix("yourPrefix");
    /* (可选)清单文件的加密方式, 可选SSEOSS或者SSEKMS方式加密。*/
    //dest.setEncryption(InventoryEncryption(InventorySSEOSS()));
    //dest.setEncryption(InventoryEncryption(InventorySSEKMS("yourKmskeyId")));
    inventoryConf.setDestination(dest);

    /* 清单文件导出的周期, 可选为Daily或者Weekly。*/
    inventoryConf.setSchedule(InventoryFrequency::Daily);

    /* 是否在清单中包含Object版本信息, 可选为All或者Current。*/
    inventoryConf.setIncludedObjectVersions(InventoryIncludedObjectVersions::All);

    /* (可选)设置清单结果中应包含的配置项, 请按需配置。*/
    InventoryOptionalFields field { 
        InventoryOptionalField::Size, InventoryOptionalField::LastModifiedDate, 
        InventoryOptionalField::ETag, InventoryOptionalField::StorageClass, 
        InventoryOptionalField::IsMultipartUploaded, InventoryOptionalField::EncryptionStatus
    };
    inventoryConf.setOptionalFields(field);

    /* 设置清单配置。*/
    auto outcome = client.SetBucketInventoryConfiguration(
        SetBucketInventoryConfigurationRequest(BucketName, inventoryConf));

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 查看清单配置

以下代码用于查看某个Bucket的清单配置：

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

    /* 填写清单规则名称。*/
    std::string InventoryId = "yourInventoryId";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 获取清单配置。*/
    auto outcome = client.GetBucketInventoryConfiguration(
        GetBucketInventoryConfigurationRequest(BucketName, InventoryId));

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout (inventoryConf.Schedule()) (inventoryConf.IncludedObjectVersions()) (field) 
## 批量列举清单配置
说明 
单次请求最多可获取100条清单配置项内容。若需获取超过100条清单配置项，则需发送多次请求，并保留相应的Token，作为下一次请求的参数。

以下代码用于批量列举某个Bucket的清单配置：

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

    /* 设置请求参数。*/
    std::string nextToken = "";
    bool isTruncated = false;
    do {
        /* 列举清单配置，每次请求最多返回100条记录。*/
        auto request = ListBucketInventoryConfigurationsRequest(BucketName);
        request.setContinuationToken(nextToken);
        auto outcome = client.ListBucketInventoryConfigurations(request);

        if (!outcome.isSuccess()) {    
            /*异常处理。*/
            std::cout (inventoryConf.Schedule()) (inventoryConf.IncludedObjectVersions()) (field) 
## 删除清单配置

以下代码用于删除某个Bucket的清单配置：

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

    /* 填写清单规则名称。*/
    std::string InventoryId = "yourInventoryId";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 删除清单配置。*/
    auto outcome = client.DeleteBucketInventoryConfiguration(
        DeleteBucketInventoryConfigurationRequest(BucketName, InventoryId));;

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 相关文档
- 关于添加存储空间清单配置的API接口说明，请参见[PutBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/putbucketinventory#reference-2379014)。
- 关于查看存储空间清单配置的API接口说明，请参见[GetBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/getbucketinventory#reference-2379122)。
- 关于批量列举存储空间清单配置的API接口说明，请参见[ListBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/listbucketinventory#reference-2379134)。
- 关于删除存储空间清单配置的API接口说明，请参见[DeleteBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/deletebucketinventory#reference-2379150)。

[上一篇：生命周期（C++ SDK）](/zh/oss/developer-reference/lifecycle-5)[下一篇：静态网站托管（C++ SDK）](/zh/oss/developer-reference/static-website-hosting-9)该文章对您有帮助吗？反馈
  
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