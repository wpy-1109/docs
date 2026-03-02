# 使用iOS SDK示例代码上传与下载文件

Source: https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-ios

---

- 使用iOS SDK示例代码上传与下载文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 快速入门（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何快速使用OSS iOS SDK完成常见操作，例如创建存储空间（Bucket）、上传文件（Object）、下载文件等。

## 前提条件

已安装iOS SDK。具体操作，请参见[安装（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/installation-8)。

## 示例工程

您可以通过查看以下示例工程，了解如何上传创建存储空间、本地文件、下载文件等操作：
- [iOS demo示例](https://github.com/aliyun/aliyun-oss-ios-sdk/tree/master/Example/AliyunOSSSDK-iOS-Example)
- [Mac demo示例](https://github.com/aliyun/aliyun-oss-ios-sdk/tree/master/Example/AliyunOSSSDK-OSX-Example)
- [Swift demo示例](https://github.com/aliyun/aliyun-oss-ios-sdk/tree/master/OSSSwiftDemo)
- [测试用例](https://github.com/aliyun/AliyunOSSiOS/tree/master/AliyunOSSiOSTests)

示例工程用法如下：
- 克隆工程：通过 git clone 获取示例[工程](https://github.com/aliyun/aliyun-oss-ios-sdk)。
- 配置参数。运行AliyunOSSSwift实例前，您需要在[OSSSwiftGlobalDefines.swift](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/OSSSwiftDemo/OSSSwiftDemo/Classes/OSSSwiftGlobalDefines.swift)文件中配置必要参数。
- 运行AliyunOSSSDK前，您需要在[OSSTestMacros.h](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/AliyunOSSiOSTests/OSSTestMacros.h)文件中配置必要参数。
- 启动本地 STS 鉴权服务。根据工程sts_local_server目录中本地鉴权服务[脚本文件](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/Scripts/sts.py)启动本地STS鉴权服务器，配置其中的AccessKeyId、AccessKeySecret以及RoleArn参数信息。
- 通过Python启动本机HTTP服务[httpserver.py](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/Scripts/httpserver.py)，以便在客户端代码中访问本地服务获取StsToken.AccessKeyId、StsToken.SecretKey和StsToken.SecurityToken。

运行工程IOS demo得到如下： 

## 示例代码

以下演示了在iOS平台以及Mac平台上传和下载文件的流程。
- 导入OSS软件包在使用OSS服务前，请先导入所需的头文件。
```
#import                             
```
- [初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)OSSClient授权访问OSS支持三种鉴权方式：明文设置、自签名模式、STS鉴权模式。建议移动端使用STS鉴权模式，详细配置说明请参见[STS鉴权模式](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-4#section-tpr-krj-lfb)。获取临时访问凭证明文设置：直接使用AccessKeyId和AccessKeySecret进行鉴权。
- 自签名模式：生成签名字符串进行鉴权，请参见[自签名模式](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-4#title-t91-tc7-lei)。
- STS鉴权模式：使用临时安全凭证进行鉴权。调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/api-assumerole#reference-clc-3sv-xdb)接口或使用[各语言STS SDK](https://help.aliyun.com/zh/ram/developer-reference/sts-sdk-overview#reference-w5t-25v-xdb)来获取临时访问凭证，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#concept-xzh-nzk-2gb)。
- 使用临时访问凭证初始化SDK。
- 以下是一个在完整应用程序生命周期中初始化 OSSClient 的示例代码：
```
@interface AppDelegate ()
@property (nonatomic, strong) OSSClient *client;
@end
/**
 * 获取sts信息的url,配置在业务方自己的搭建的服务器上。
 */
#define OSS_STS_URL                 @"oss_sts_url"
/**
 * bucket所在的region的endpoint。
 */
#define OSS_ENDPOINT                @"your bucket's endpoint"
/**
 * bucket所在的region。
 */
#define OSS_REGION                	@"your bucket's region"

@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    
    // 初始化OSSClient实例
    [self setupOSSClient];    
    return YES;
}
- (void)setupOSSClient {
    // 初始化具有自动刷新的provider
    id credentialProvider = [[OSSAuthCredentialProvider alloc] initWithAuthServerUrl:OSS_STS_URL];   
    // client端的配置,如超时时间，开启dns解析等等
    OSSClientConfiguration *cfg = [[OSSClientConfiguration alloc] init];
    cfg.signVersion = OSSSignVersionV4;
    client = [[OSSClient alloc] initWithEndpoint:OSS_ENDPOINT credentialProvider:credentialProvider clientConfiguration:cfg];
    client.region = OSS_REGION;
}
```
说明 如果您的应用只用到一个[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)下的bucket，建议保持OSSClient实例与应用程序的生命周期一致。
- 创建存储空间以下代码用于创建名为examplebucket的存储空间。
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
// 实现阻塞等待任务完成。
// [createTask waitUntilFinished];          
```
说明 SDK的所有操作都会返回`OSSTask`，您可以为`OSSTask`设置延续动作，等待其异步完成，也可以通过调用`waitUntilFinished`阻塞等待其完成。
- 上传文件 以下代码用于将本地文件上传到OSS。
```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];
// 填写Bucket名称，例如examplebucket。
put.bucketName = @"examplebucket";
// 填写Object完整路径。Object完整路径中不能包含Bucket名称，例如exampledir/testdir/exampleobject.txt。
put.objectKey = @"exampledir/testdir/exampleobject.txt";
put.uploadingFileURL = [NSURL fileURLWithPath:@""];
// put.uploadingData = ; // 直接上传NSData。
// 直接上传NSData。
put.uploadProgress = ^(int64_t bytesSent, int64_t totalByteSent, int64_t totalBytesExpectedToSend) {
    NSLog(@"%lld, %lld, %lld", bytesSent, totalByteSent, totalBytesExpectedToSend);
};
OSSTask * putTask = [client putObject:put];
[putTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"upload object success!");
    } else {
        NSLog(@"upload object failed, error: %@" , task.error);
    }
    return nil;
}];
// 实现阻塞等待任务完成。
// [putTask waitUntilFinished];
```
- 下载指定文件 以下代码用于下载指定OSS文件到本地文件。
```
OSSGetObjectRequest * request = [OSSGetObjectRequest new];
// 填写Bucket名称，例如examplebucket。
request.bucketName = @"examplebucket";
// 填写Object完整路径。Object完整路径中不能包含Bucket名称，例如exampledir/testdir/exampleobject.txt。
request.objectKey = @"exampledir/testdir/exampleobject.txt";
request.downloadProgress = ^(int64_t bytesWritten, int64_t totalBytesWritten, int64_t totalBytesExpectedToWrite) {
    NSLog(@"%lld, %lld, %lld", bytesWritten, totalBytesWritten, totalBytesExpectedToWrite);
};
OSSTask * getTask = [client getObject:request];
[getTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"download object success!");
        OSSGetObjectResult * getResult = task.result;
        NSLog(@"download result: %@", getResult.downloadedData);
    } else {
        NSLog(@"download object failed, error: %@" ,task.error);
    }
    return nil;
}];
// 实现阻塞等待任务完成。
// [task waitUntilFinished];
```

[上一篇：初始化（iOS SDK）](/zh/oss/developer-reference/initialization-8)[下一篇：配置访问凭证（iOS SDK）](/zh/oss/developer-reference/ios-configure-access-credentials)该文章对您有帮助吗？反馈
  
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