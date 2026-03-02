# 调用iOS SDK接口创建存储空间

Source: https://help.aliyun.com/zh/oss/developer-reference/create-buckets-1

---

- 调用iOS SDK接口创建存储空间-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 创建存储空间（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
存储空间（Bucket）是存储对象（Object）的容器。对象都隶属于存储空间。本文介绍如何创建存储空间。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。说明 所创建存储空间的所属地域取决于初始化配置的endpoint地域信息。
- 北京时间2025年10月13日10:00:00起，OSS逐步调整所有地域通过API、SDK、ossutil创建Bucket时默认开启阻止公共访问。各个地域的生效变更时间，请参见[公告说明](https://www.aliyun.com/notice/117116)。

## 权限说明

阿里云账号默认拥有全部权限。阿里云账号下的RAM用户或RAM角色默认没有任何权限，需要阿里云账号或账号管理员通过[RAM Policy](https://help.aliyun.com/zh/oss/ram-policy-overview/)或[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)授予操作权限。
| API | Action | 说明|
| PutBucket | `oss:PutBucket` | 创建Bucket。|
| `oss:PutBucketAcl` | 创建Bucket后，修改Bucket的ACL，需要此操作的权限。|

## 示例代码

以下代码用于创建名为examplebucket的存储空间：

```
// 构建创建Bucket的请求。
OSSCreateBucketRequest * create = [OSSCreateBucketRequest new];
// 设置存储空间名称为examplebucket。
create.bucketName = @"examplebucket";
// 设置访问权限为私有。
create.xOssACL = @"private";
// 设置存储类型为低频访问类型IA。
create.storageClass = OSSBucketStorageClassIA;

OSSTask * createTask = [client createBucket:create];

[createTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"create bucket success!");
    } else {
        NSLog(@"create bucket failed, error: %@", task.error);
    }
    return nil;
}];
// 实现同步阻塞等待任务完成。
// [createTask waitUntilFinished];          
```

## 相关文档
- 关于创建存储空间的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/AliyunOSSiOSTests/OSSBucketTests.m)。
- 关于创建存储空间的API接口说明，请参见[PutBucket](https://help.aliyun.com/zh/oss/developer-reference/putbucket#doc-api-Oss-PutBucket)。
- 关于初始化OSSClient，请参见[如何初始化OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。

[上一篇：存储空间（iOS SDK）](/zh/oss/developer-reference/buckets-1/)[下一篇：列举存储空间（iOS SDK）](/zh/oss/developer-reference/list-buckets-10)该文章对您有帮助吗？反馈
  
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