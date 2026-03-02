# iOS SDK使用x

Source: https://help.aliyun.com/zh/oss/developer-reference/prevent-objects-from-being-overwritten-by-objects-that-have-the-same-names-14

---

- iOS SDK使用x-oss-forbid-overwrite禁止覆盖同名文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 禁止覆盖同名文件（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
默认情况下，如果新添加文件（Object）与现有文件同名且对该文件有访问权限，则新添加的文件将覆盖原有的文件。本文介绍如何通过设置请求头x-oss-forbid-overwrite在简单上传、拷贝文件及分片上传等场景中禁止覆盖同名文件。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。

## 简单上传

以下代码用于简单上传时禁止覆盖同名文件：

```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];

// 填写Bucket名称，例如examplebucket。关于Bucket名称命名规范的更多信息，请参见Bucket。
put.bucketName = @"examplebucket";
// 填写不包含Bucket名称在内的Object完整路径，例如exampledir/exampleobject.txt。关于Object名称命名规范的更多信息，请参见Object。
put.objectKey = @"exampledir/exampleobject.txt";
// 填写待上传的本地文件所在的完整路径。
put.uploadingFileURL = [NSURL fileURLWithPath:@"/storage/emulated/0/oss/examplefile.txt"];

// 指定上传文件操作时是否覆盖同名Object。
// 不指定x-oss-forbid-overwrite时，默认覆盖同名Object。
// 指定x-oss-forbid-overwrite为false时，表示允许覆盖同名Object。
// 指定x-oss-forbid-overwrite为true时，表示禁止覆盖同名Object，如果同名Object已存在，程序将报错。
put.objectMeta = @{@"x-oss-forbid-overwrite": @"true"};

// （可选）设置上传进度。
put.uploadProgress = ^(int64_t bytesSent, int64_t totalByteSent, int64_t totalBytesExpectedToSend) {
    // 指定当前上传长度、当前已上传总长度以及待上传的总长度。
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
// 实现同步阻塞等待任务完成。
// [putTask waitUntilFinished];
```

## 拷贝文件

以下代码用于拷贝文件时禁止覆盖同名文件：

```
OSSCopyObjectRequest * copy = [OSSCopyObjectRequest new];
// 填写源Bucket名称。
copy.sourceBucketName = @"srcbucket";
// 填写源Bucket内的Object完整路径。
copy.sourceObjectKey = @"dir1/srcobject.txt";
// 填写目标Bucket名称。
copy.bucketName = @"destbucket";
// 填写目标Bucket内的Object完整路径。
copy.objectKey = @"dir2/destobject.txt";

// 指定上传文件操作时是否覆盖同名Object。
// 不指定x-oss-forbid-overwrite时，默认覆盖同名Object。
// 指定x-oss-forbid-overwrite为false时，表示允许覆盖同名Object。
// 指定x-oss-forbid-overwrite为true时，表示禁止覆盖同名Object，如果同名Object已存在，程序将报错。
copy.objectMeta = @{@"x-oss-forbid-overwrite": @"true"};

OSSTask * task = [client copyObject:copy];
[task continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"copy object success!");
    } else {
        NSLog(@"copy object failed, error: %@" , task.error);
    }
    return nil;
}];
// 实现同步阻塞等待任务完成。
// [putTask waitUntilFinished];
```

## 分片上传

以下代码用于分片上传时禁止覆盖同名文件：

```
__block NSString * uploadId = nil;
__block NSMutableArray * partInfos = [NSMutableArray new];
// 填写Bucket名称，例如examplebucket。
NSString * uploadToBucket = @"examplebucket";
// 填写不包含Bucket名称在内的Object完整路径，例如exampledir/exampleobject.txt。
NSString * uploadObjectkey = @"exampledir/exampleobject.txt";
OSSInitMultipartUploadRequest * init = [OSSInitMultipartUploadRequest new];
init.bucketName = uploadToBucket;
init.objectKey = uploadObjectkey;

// 指定上传文件操作时是否覆盖同名Object。
// 不指定x-oss-forbid-overwrite时，默认覆盖同名Object。
// 指定x-oss-forbid-overwrite为false时，表示允许覆盖同名Object。
// 指定x-oss-forbid-overwrite为true时，表示禁止覆盖同名Object，如果同名Object已存在，程序将报错。
init.objectMeta = @{@"x-oss-forbid-overwrite": @"true"};
// multipartUploadInit返回的结果中包含UploadId，UploadId是分片上传的唯一标识。您可以根据该uploadId发起相关操作，例如取消分片上传、查询分片上传等。
OSSTask * initTask = [client multipartUploadInit:init];
[initTask waitUntilFinished];
if (!initTask.error) {
    OSSInitMultipartUploadResult * result = initTask.result;
    uploadId = result.uploadId;
} else {
    NSLog(@"multipart upload failed, error: %@", initTask.error);
    return;
}

// 填写待上传的本地文件所在的完整路径。
NSString * filePath = @"/storage/emulated/0/oss/examplefile.txt";
// 获取待上传文件的大小。
uint64_t fileSize = [[[NSFileManager defaultManager] attributesOfItemAtPath:filePath error:nil] fileSize];
// 设置分片号，从1开始标识。每一个上传的Part都有一个分片号，取值范围是1~10000。
int chuckCount = *;
// 设置分片大小，单位为字节，取值范围为100 KB~5 GB。
uint64_t offset = fileSize/chuckCount;
for (int i = 1; i 
## 相关文档
- 关于简单上传的API接口说明，请参见[PutObject](https://help.aliyun.com/zh/oss/developer-reference/putobject#reference-l5p-ftw-tdb)。
- 关于拷贝文件的API接口说明，请参见[CopyObject](https://help.aliyun.com/zh/oss/developer-reference/copyobject#reference-mvx-xxc-5db)。
- 分片上传的完整实现涉及三个API接口，详情如下：关于初始化分片上传事件的API接口说明，请参见[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)。
- 关于分片上传Part的API接口说明，请参见[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)。
- 关于完成分片上传的API接口说明，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。
- 关于初始化OSSClient，请参见[如何初始化OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。

[上一篇：转换文件存储类型（iOS SDK）](/zh/oss/developer-reference/convert-the-storage-classes-of-objects-6)[下一篇：管理软链接（iOS SDK）](/zh/oss/developer-reference/manage-symbolic-links)该文章对您有帮助吗？反馈
  
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