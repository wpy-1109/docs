# 使用C++ SDK配置生命周期规则转换存储类型与删除对象

Source: https://help.aliyun.com/zh/oss/developer-reference/lifecycle-5

---

- 使用C++ SDK配置生命周期规则转换存储类型与删除对象-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 生命周期（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
并不是所有上传至OSS的数据都需要频繁访问，但基于数据合规或者存档等原因，部分数据仍需要继续以冷存储类型进行保存。或者基于业务使用场景，希望批量删除Bucket内不再需要保存的数据。您可以配置基于最后一次修改时间（Last Modified Time）的生命周期规则，定期将Object从热存储类型转为冷存储类型或者删除Object，以降低存储成本。

## 注意事项
- 在配置基于最后一次修改时间的生命周期规则之前，请确保您已了解该功能。详情请参见[基于最后一次修改时间的生命周期规则](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)。
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。
- 要设置生命周期规则，您必须有`oss:PutBucketLifecycle`权限；要查看生命周期规则，您必须有`oss:GetBucketLifecycle`权限；要清空生命周期规则，您必须有`oss:DeleteBucketLifecycle`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 设置生命周期规则

以下代码用于为examplebucket设置基于最后一次修改时间策略的生命周期规则。设置完成后，如果您希望修改其中的一条或多条生命周期规则，请参见[如何修改其中一条或多条生命周期规则配置？](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#66e3fe0b87hr7)

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /*初始化OSS账号信息。*/
    
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /*填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

    /*初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    SetBucketLifecycleRequest request(BucketName);
    std::string date("2022-10-12T00:00:00.000Z");

    /*设置标签。*/
    Tagging tagging;
    tagging.addTag(Tag("key1", "value1"));
    tagging.addTag(Tag("key2", "value2"));

    /*指定生命周期规则。*/
    auto rule1 = LifecycleRule();
    rule1.setID("rule1");
    rule1.setPrefix("test1/");
    rule1.setStatus(RuleStatus::Enabled);
    rule1.setExpiration(3);
    rule1.setTags(tagging.Tags());

    /*指定过期时间。*/
    auto rule2 = LifecycleRule();
    rule2.setID("rule2");
    rule2.setPrefix("test2/");
    rule2.setStatus(RuleStatus::Disabled);
    rule2.setExpiration(date);

    /*rule3为针对版本控制状态下的Bucket的生命周期规则。*/
    auto rule3 = LifecycleRule();
    rule3.setID("rule3");
    rule3.setPrefix("test3/");
    rule3.setStatus(RuleStatus::Disabled);

    /*设置Object距其最后修改时间365天之后自动转为归档类型。*/  
    auto transition = LifeCycleTransition();  
    transition.Expiration().setDays(365);
    transition.setStorageClass(StorageClass::Archive);
    rule3.addTransition(transition);

    /*设置自动移除过期删除标记。*/
    rule3.setExpiredObjectDeleteMarker(true);

    /*设置非当前版本的Object距最后修改时间10天之后转为低频访问类型。*/
    auto transition1 = LifeCycleTransition();  
    transition1.Expiration().setDays(10);
    transition1.setStorageClass(StorageClass::IA);

    /*设置非当前版本的Object距最后修改时间20天之后转为归档类型。*/
    auto transition2 = LifeCycleTransition();  
    transition2.Expiration().setDays(20);
    transition2.setStorageClass(StorageClass::Archive);

    /*设置Object在其成为非当前版本30天之后删除。*/
    auto expiration  = LifeCycleExpiration(30);
    rule3.setNoncurrentVersionExpiration(expiration);

    LifeCycleTransitionList noncurrentVersionStorageTransitions{transition1, transition2};
    rule3.setNoncurrentVersionTransitionList(noncurrentVersionStorageTransitions);

    /*设置生命周期规则。*/
    LifecycleRuleList list{rule1, rule2, rule3};
    request.setLifecycleRules(list);
    auto outcome = client.SetBucketLifecycle(request);

    if (!outcome.isSuccess()) {
        /*异常处理 */
        std::cout 
## 查看生命周期规则

以下代码用于查看examplebucket的生命周期规则。

```
#include 
using namespace AlibabaCloud::OSS;
std::string ToStorageClassName(const StorageClass& storageClass) {
    switch (storageClass) {
        case StorageClass::Standard:
            return "Standard";
        case StorageClass::IA:
            return "IA";
        case StorageClass::Archive:
            return "Archive";
        case StorageClass::ColdArchive:
            return "ColdArchive";
        default:
            return "Unknown";
    }
}
int main(void)
{
    /*初始化OSS账号信息。*/
    
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /*填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
  
    /*初始化网络等资源。*/
    InitializeSdk();
  
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    /*查看生命周期规则。*/
    auto outcome = client.GetBucketLifecycle(BucketName);
    if (outcome.isSuccess()) {
        std::cout 
## 清空生命周期规则

以下代码用于清空examplebucket的所有生命周期规则。如果您需要删除其中一条或者多条生命周期规则，请参见[如何删除其中一条或多条生命周期规则？](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#80811cc9cawfo)。

```
#include 

using namespace AlibabaCloud::OSS;

int main(void)
{
    /*初始化OSS账号信息。*/
    
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /*填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
  
    /*初始化网络等资源。*/
    InitializeSdk();
  
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    /*清空生命周期规则。*/
    DeleteBucketLifecycleRequest request(BucketName);
    auto outcome = client.DeleteBucketLifecycle(request);
    if (!outcome.isSuccess()) {
        /*异常处理 */
        std::cout 
## 相关文档
- 关于生命周期规则的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/master/test/src/Object/ObjectTaggingTest.cc)。
- 关于设置生命周期规则的API接口说明，请参见[PutBucketLifecycle](https://help.aliyun.com/zh/oss/developer-reference/putbucketlifecycle#reference-xlw-dbv-tdb)。
- 关于查看生命周期规则的API接口说明，请参见[GetBucketLifecycle](https://help.aliyun.com/zh/oss/developer-reference/getbucketlifecycle#reference-zq5-grw-tdb)。
- 关于清空生命周期规则的API接口说明，请参见[DeleteBucketLifecycle](https://help.aliyun.com/zh/oss/developer-reference/deletebucketlifecycle#reference-wl1-xsw-tdb)。

[上一篇：数据管理（C++ SDK）](/zh/oss/developer-reference/data-management-5/)[下一篇：存储空间清单（C++ SDK）](/zh/oss/developer-reference/bucket-inventory-4)该文章对您有帮助吗？反馈
  
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