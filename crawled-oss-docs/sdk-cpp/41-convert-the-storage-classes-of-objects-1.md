# 使用C++ SDK通过复制Object转换存储类型

Source: https://help.aliyun.com/zh/oss/developer-reference/convert-the-storage-classes-of-objects-1

---

- 使用C++ SDK通过复制Object转换存储类型-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 转换文件存储类型（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS 提供多种存储类型，包括标准、低频访问、归档、冷归档和深度冷归档，以满足从热数据到冷数据的各种存储需求。在对象存储中，一旦对象被创建，其内容是不可修改的。这意味着，如果您想更改对象的存储类型，就无法直接修改原对象，而必须创建一个新的对象。因此，转换对象的存储类型需要使用 Bucket.CopyObject 方法，这一操作会通过复制原对象来实现存储类型的转换。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。
- 要转换文件存储类型，您必须具有`oss:GetObject`、`oss:PutObject`和`oss:RestoreObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 示例代码

### 将Object的存储类型从标准或低频访问转换为归档类型

```
#include 
#include 

using namespace AlibabaCloud::OSS;

int main(void)
{  
            
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
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
    
    /* 设置修改后的文件存储类型，例如将修改后的文件存储类型设置为归档类型。*/
    ObjectMetaData objectMeta;
    objectMeta.addHeader("x-oss-storage-class", "Archive");
    
    std::string SourceBucketName = BucketName;
    std::string SourceObjectName = ObjectName;
    
    CopyObjectRequest request(SourceBucketName, ObjectName, objectMeta);
    request.setCopySource(SourceBucketName, SourceObjectName);
    
    /* 修改为上述指定的文件存储类型。*/
    auto outcome = client.CopyObject(request);
    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
### 将Object的存储类型从归档转换为低频访问或者标准类型

```
#include 
#include 
#include 
using namespace AlibabaCloud::OSS;
int main(void)
{
    
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
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    /* 检查目标文件是否为归档类型。如果是，则需要先解冻才能更改存储类型。*/
    auto restoreOutcome = client.RestoreObject(BucketName, ObjectName);
    if (!restoreOutcome.isSuccess()) {
        /* 异常处理。*/
        std::cout  0)
    {
        auto meta = client.HeadObject(BucketName, ObjectName);
        std::string restoreStatus = meta.result().HttpMetaData()["x-oss-restore"];
        std::transform(restoreStatus.begin(), restoreStatus.end(), restoreStatus.begin(), ::tolower);
        if (!restoreStatus.empty() && 
        restoreStatus.compare(0, onGoingRestore.size(), onGoingRestore)==0) {
            std::cout 
## 相关文档
- 关于转换文件存储类型的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc)。
- 关于转换文件存储类型的API接口说明，请参见[CopyObject](https://help.aliyun.com/zh/oss/developer-reference/copyobject#reference-mvx-xxc-5db)。

[上一篇：管理文件元数据（C++ SDK）](/zh/oss/developer-reference/manage-object-metadata-5)[下一篇：列举文件（C++ SDK）](/zh/oss/developer-reference/list-objects-11)该文章对您有帮助吗？反馈
  
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