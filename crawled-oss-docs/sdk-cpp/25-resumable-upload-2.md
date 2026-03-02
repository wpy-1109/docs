# 使用C++ SDK实现断点续传上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-2

---

- 使用C++ SDK实现断点续传上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 断点续传上传（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
通过断点续传上传的方式将文件上传到OSS前，您可以指定断点记录点。上传过程中，如果出现网络异常或程序崩溃导致文件上传失败时，将从断点记录处继续上传未上传完成的部分。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。
- 要断点续传上传，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。
- 使用断点续传上传时，文件上传的进度信息会记录在Checkpoint文件中，如果上传过程中某一分片上传失败，再次上传时会从Checkpoint文件中记录的点继续上传，从而达到断点续传的效果。上传完成后，Checkpoint文件会被删除。
- 请勿修改Checkpoint文件中携带的校验信息。如果Checkpoint文件损坏，则会重新上传所有分片。
- 如果上传过程中本地文件发生了改变，则会重新上传所有分片。

## 实现方法

您可以通过client.ResumableUploadObject方法实现断点续传上传。此方法中的UploadObjectRequest请求包含以下参数：
| 参数 | 描述 | 是否必须 | 默认值 | 设置方法|
| bucket | 存储空间名称。 | 是 | 无 | 通过构造方法设置|
| key | 上传到OSS的文件名称。 | 是 | 无|
| filePath | 上传的本地文件名称。 | 否 | 无|
| partSize | 上传的分片大小，取值范围为100 KB~5 GB。 | 否 | 8 MB | 通过setPartSize设置|
| threadNum | 分片上传的并发数。 | 否 | 3 | 通过构造函数或者setThreadNum设置|
| checkpointDir | 记录本地分片上传结果的文件。上传过程中的进度信息会保存在该文件中，如果某一分片上传失败，再次上传时会根据文件中记录的点继续上传。上传完成后，该文件会被删除。 | 否 | 与DownloadFile同目录 | 通过构造函数或者setCheckpointDir设置|

## 示例代码

以下代码用于断点续传上传。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    / *yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn - hangzhou。 * /
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写Object的完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。*/
    std::string UploadFilePath = "D:\\localpath\\examplefile.txt";
    /* 记录本地分片上传结果的文件。上传过程中的进度信息会保存在该文件中，如果某一分片上传失败，再次上传时会根据文件中记录的断点继续上传。上传完成后，该文件会被删除。*/
    /* 设置断点记录文件所在的目录，并确保指定的目录已存在，例如D:\\local。如果未设置该值，则不会记录断点续传信息，不会使用断点续传。*/
    std::string CheckpointFilePath = "D:\\local";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 断点续传上传。*/
    UploadObjectRequest request(BucketName, ObjectName, UploadFilePath, CheckpointFilePath);
    auto outcome = client.ResumableUploadObject(request);

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 相关文档

关于断点续传上传的完整代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/f7ef0efa45e17da815020a18919551973cc98089/sample/src/object/ObjectSample.cc#L318)。

[上一篇：追加上传（C++ SDK）](/zh/oss/developer-reference/append-upload-9)[下一篇：分片上传（C++ SDK）](/zh/oss/developer-reference/multipart-upload-9)该文章对您有帮助吗？反馈
  
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