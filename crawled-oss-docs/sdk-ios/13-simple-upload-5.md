# 通过iOS SDK上传本地文件或内存数据

Source: https://help.aliyun.com/zh/oss/developer-reference/simple-upload-5

---

- 通过iOS SDK上传本地文件或内存数据-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 简单上传（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何从内存中上传文件或者上传本地文件。您也可以使用MD5校验来确保上传过程中的数据完整性。

## 注意事项

使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。
说明 
所创建存储空间的所属地域取决于初始化配置的endpoint地域信息。

## 权限说明

阿里云账号默认拥有全部权限。阿里云账号下的RAM用户或RAM角色默认没有任何权限，需要阿里云账号或账号管理员通过[RAM Policy](https://help.aliyun.com/zh/oss/ram-policy-overview/)或[Bucket Policy](https://help.aliyun.com/zh/oss/user-guide/oss-bucket-policy/)授予操作权限。
| API | Action | 说明|
| PutObject | `oss:PutObject` | 上传Object。|
| `oss:PutObjectTagging` | 上传Object时，如果通过x-oss-tagging指定Object的标签，则需要此操作的权限。|
| `kms:GenerateDataKey` | 上传Object时，如果Object的元数据包含X-Oss-Server-Side-Encryption: KMS，则需要这两个操作的权限。|
| `kms:Decrypt`|

## 从内存中上传文件或上传本地文件

上传文件时可以直接上传OSSData或者通过NSURL上传文件。

```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];

// 填写Bucket名称，例如examplebucket。
put.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
put.objectKey = @"exampledir/exampleobject.txt";
put.uploadingFileURL = [NSURL fileURLWithPath:@""];
// put.uploadingData = ; // 直接上传NSData。

// （可选）设置上传进度。
put.uploadProgress = ^(int64_t bytesSent, int64_t totalByteSent, int64_t totalBytesExpectedToSend) {
    // 指定当前上传长度、当前已经上传总长度、待上传的总长度。
    NSLog(@"%lld, %lld, %lld", bytesSent, totalByteSent, totalBytesExpectedToSend);
};
// 配置可选字段。
// put.contentType = @"application/octet-stream";
// 设置Content-MD5。
// put.contentMd5 = @"eB5eJF1ptWaXm4bijSPyxw==";
// 设置Object的编码方式。
// put.contentEncoding = @"identity";
// 设置Object的展示形式。
// put.contentDisposition = @"attachment";
// 可以在上传文件时设置文件元数据或者HTTP头部。
// NSMutableDictionary *meta = [NSMutableDictionary dictionary];
// 设置文件元数据。
// [meta setObject:@"value" forKey:@"x-oss-meta-name1"];
// 设置Object的访问权限为私有。
// [meta setObject:@"private" forKey:@"x-oss-object-acl"];
// 设置Object的归档类型为标准存储。
// [meta setObject:@"Standard" forKey:@"x-oss-storage-class"];
// 设置覆盖同名目标Object。
// [meta setObject:@"true" forKey:@"x-oss-forbid-overwrite"];
// 指定Object的对象标签，可同时设置多个标签。
// [meta setObject:@"a:1" forKey:@"x-oss-tagging"];
// 指定OSS创建目标Object时使用的服务器端加密算法。
// [meta setObject:@"AES256" forKey:@"x-oss-server-side-encryption"];
// 表示KMS托管的用户主密钥，该参数仅在x-oss-server-side-encryption为KMS时有效。
// [meta setObject:@"9468da86-3509-4f8d-a61e-6eab1eac****" forKey:@"x-oss-server-side-encryption-key-id"];
// put.objectMeta = meta;
OSSTask * putTask = [client putObject:put];

[putTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"upload object success!");
    } else {
        NSLog(@"upload object failed, error: %@" , task.error);
    }
    return nil;
}];
// waitUntilFinished会阻塞当前线程，但是不会阻塞上传任务进程。
// [putTask waitUntilFinished];
// [put cancel];
```

## 上传到文件目录

OSS没有文件夹的概念，所有元素都是以文件来存储。OSS提供了创建模拟文件夹的方式。创建模拟文件夹本质上是创建了一个名称以正斜线（/）结尾的文件以实现将文件上传至目录，控制台会对以正斜线（/）结尾的文件以文件夹的方式展示。

例如上传文件时，如果把objectKey设置为`folder/subfolder/file`，表示将file文件上传到`folder/subfolder/`目录下。
说明 
路径默认是根目录，不需要以正斜线 （/）开头。

## 上传文件时设置contentType并带有MD5校验

为保证客户端发送的数据和OSS服务端接收到的数据一致，您可以在上传文件时增加contentMd5值，OSS服务端会使用该MD5值做校验。上传文件时还可以显式指定contentType，如果未显式指定contentType，则SDK会根据文件名或者上传的objectKey自行判断。
重要 
使用MD5校验时，性能会有所下降。

SDK提供了便捷的Base64和contentMd5的计算方法。

```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];
// 填写Bucket名称，例如examplebucket。
put.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
put.objectKey = @"exampledir/exampleobject.txt";
put.uploadingFileURL = [NSURL fileURLWithPath:@""];
// 直接上传NSData。
// put.uploadingData = ; 
// （可选）设置contentType。
put.contentType = @"application/octet-stream";
// （可选）设置contentMd5校验。
// 设置文件路径的contentMd5校验。
put.contentMd5 = [OSSUtil base64Md5ForFilePath:@""]; 
// 设置二进制数据的contentMd5校验。
// put.contentMd5 = [OSSUtil base64Md5ForData:];
// （可选）设置上传进度。
put.uploadProgress = ^(int64_t bytesSent, int64_t totalByteSent, int64_t totalBytesExpectedToSend) {
    // 指定当前上传长度、当前已经上传总长度、待上传的总长度。
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
// waitUntilFinished会阻塞当前线程，但是不会阻塞上传任务进程。
// [putTask waitUntilFinished];
// [put cancel];
```

## 相关文档
- 关于简单上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/AliyunOSSiOSTests/OSSObjectTests.m)。
- 关于简单上传的API接口说明，请参见[PutObject](https://help.aliyun.com/zh/oss/developer-reference/putobject#reference-l5p-ftw-tdb)。
- 关于初始化OSSClient，请参见[如何初始化OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。

[上一篇：上传文件（iOS SDK）](/zh/oss/developer-reference/upload-objects-12/)[下一篇：分片上传（iOS SDK）](/zh/oss/developer-reference/multipart-upload-7)该文章对您有帮助吗？反馈
  
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