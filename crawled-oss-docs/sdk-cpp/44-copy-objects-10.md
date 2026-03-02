# 使用C++ SDK在Bucket间复制小文件与大文件

Source: https://help.aliyun.com/zh/oss/developer-reference/copy-objects-10

---

- 使用C++ SDK在Bucket间复制小文件与大文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 拷贝文件（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何将源Bucket中的文件（Object）复制到同一地域下相同或不同目标Bucket中。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。
- 拷贝文件时，您必须拥有源文件的读权限及目标Bucket的读写权限。
- 拷贝文件时，您需要确保源Bucket和目标Bucket均未设置合规保留策略，否则报错The object you specified is immutable.。
- 不支持跨地域拷贝。例如不能将华东1（杭州）地域存储空间中的文件拷贝到华北1（青岛）地域。

## 拷贝小文件

对于小于1GB 的文件，您可以通过client.CopyObject方法将文件从一个存储空间（源存储空间）复制到同一地域的另一个存储空间（目标存储空间）。该方法的参数指定方式说明如下：
| 参数指定方式 | 描述|
| CopyObjectOutcome OssClient::CopyObject(const CopyObjectRequest &request) | 允许指定目标文件的元数据和拷贝的限制条件。如果拷贝操作的源文件地址和目标文件地址相同，则直接替换源文件的元数据。|

以下代码用于拷贝小文件：

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
    /* 填写源Bucket名称，例如srcexamplebucket。*/
    std::string SourceBucketName = "srcexamplebucket";
    /* 填写与源Bucket处于同一地域的目标Bucket名称，例如destbucket。*/
    std::string CopyBucketName = "destbucket";
    /* 填写源Object的完整路径，完整路径中不能包含Bucket名称，例如srcdir/scrobject.txt。*/
    std::string SourceObjectName = "srcdir/scrobject.txt";
    /* 填写目标Object的完整路径，完整路径中不能包含Bucket名称，例如destdir/destobject.txt。*/
    std::string CopyObjectName = "destdir/destobject.txt";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    CopyObjectRequest request(CopyBucketName, CopyObjectName);
    request.setCopySource(SourceBucketName, SourceObjectName);

    /* 拷贝文件。*/
    auto outcome = client.CopyObject(request);

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 拷贝大文件

对于大于1 GB的文件，需要使用分片拷贝（UploadPartCopy）。分片拷贝分为三步：
- 通过client.InitiateMultipartUpload初始化分片拷贝任务。
- 通过client.UploadPartCopy进行分片拷贝。除最后一个分片外，其它分片都要大于100 KB。
- 通过client.CompleteMultipartUpload提交分片拷贝任务。

以下代码用于拷贝大文件：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息 */    
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写源Bucket名称，例如srcexamplebucket。*/
    std::string SourceBucketName = "srcexamplebucket";
    /* 填写与源Bucket处于同一地域的目标Bucket名称，例如destbucket。*/
    std::string CopyBucketName = "destbucket";
    /* 填写源Object的完整路径，完整路径中不能包含Bucket名称，例如srcdir/scrobject.txt。*/
    std::string SourceObjectName = "srcdir/scrobject.txt";
    /* 填写目标Object的完整路径，完整路径中不能包含Bucket名称，例如destdir/destobject.txt。*/
    std::string CopyObjectName = "destdir/destobject.txt";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    auto getObjectMetaReq = GetObjectMetaRequest(SourceBucketName, SourceObjectName);
    auto getObjectMetaResult = client.GetObjectMeta(getObjectMetaReq);
    if (!getObjectMetaResult.isSuccess()) {
        std::cout (objectSize / partSize);
    /* 计算分片个数。*/
    if (objectSize % partSize != 0) {
        partCount++;
    }

    /* 对每一个分片进行拷贝。*/
    for (int i = 1; i 
## 相关文档
- 关于拷贝小文件以及大文件的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/object/ObjectSample.cc)。
- 关于拷贝小文件的API接口说明，请参见[CopyObject](https://help.aliyun.com/zh/oss/developer-reference/copyobject#reference-mvx-xxc-5db)。
- 关于拷贝大文件的API接口说明，请参见[UploadPartCopy](https://help.aliyun.com/zh/oss/developer-reference/uploadpartcopy#reference-t4b-vpx-wdb)。

[上一篇：删除文件（C++ SDK）](/zh/oss/developer-reference/delete-objects-10)[下一篇：禁止覆盖同名文件（C++ SDK）](/zh/oss/developer-reference/prevent-objects-from-being-overwritten-by-objects-that-have-the-same-names-4)该文章对您有帮助吗？反馈
  
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