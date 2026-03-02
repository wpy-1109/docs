# 使用iOS SDK为上传下载文件开启MD5和CRC64完整性校验

Source: https://help.aliyun.com/zh/oss/developer-reference/data-security-7

---

- 使用iOS SDK为上传下载文件开启MD5和CRC64完整性校验-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 数据安全性（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
 iOS SDK提供了数据完整性校验来保证您在上传、下载过程中数据的安全性。

## 上传文件的数据完整性校验

由于移动端网络环境的复杂性，数据在客户端和服务器之间传输时有可能会出错。OSS提供了基于MD5和CRC64的端到端的数据完整性验证功能。
- MD5校验需要在上传文件时提供文件的Content-MD5值，OSS服务器会帮助用户进行MD5校验，仅当OSS服务器接收到文件的MD5值和上传提供的MD5一致时才可以上传成功，以此保证上传数据的完整性。
```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];
// 填写Bucket名称，例如examplebucket。
put.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
put.objectKey = @"exampledir/exampleobject.txt";
put.uploadingFileURL = [NSURL fileURLWithPath:@""];
// put.uploadingData = ; // 直接上传NSData。
// 设置Content-MD5。
put.contentMd5 = [OSSUtil base64Md5ForFilePath:@""]; 
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
```
- CRC校验与MD5相比，CRC64可以在文件上传的同时计算CRC值。
```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];
// 填写Bucket名称，例如examplebucket。
put.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
put.objectKey = @"exampledir/exampleobject.txt";
put.uploadingFileURL = [NSURL fileURLWithPath:@""];
// put.uploadingData = ; // 直接上传NSData。
// 开启CRC校验。
put.crcFlag = OSSRequestCRCOpen;
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
```

## 下载文件的数据完整性校验

iOS SDK在下载过程中提供了基于CRC的端到端的数据完整性效验功能。

在读取数据流时，如果开启了CRC校验，会在数据流读取完成时自动验证数据完整性。

以下代码用于开启CRC校验：

```
OSSGetObjectRequest * request = [OSSGetObjectRequest new];
request.bucketName = @"examplebucket";
request.objectKey = @"exampledir/exampleobject.txt";
// 设置下载文件的本地路径
request.downloadToFileURL = [NSURL fileURLWithPath:@""];
// 开启CRC校验。
request.crcFlag = OSSRequestCRCOpen;
OSSTask * task = [client getObject:request];
[task continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"download object success!");
    } else {
        NSLog(@"download object failed, error: %@" ,task.error);
    }
    return nil;
}];
// [task waitUntilFinished];
```

开启CRC校验后，如果设置了onReceiveData block，需自行比较CRC值是否一致。

```
OSSGetObjectRequest * request = [OSSGetObjectRequest new];
request.bucketName = @"examplebucket";
request.objectKey = @"exampledir/exampleobject.txt";
// 设置下载文件的本地路径
request.downloadToFileURL = [NSURL fileURLWithPath:@""];
// 开启CRC校验
request.crcFlag = OSSRequestCRCOpen;
__block uint64_t localCrc64 = 0;
NSMutableData *receivedData = [NSMutableData data];
request.onRecieveData = ^(NSData *data) {
    if (data)
    {
        NSMutableData *mutableData = [data mutableCopy];
        void *bytes = mutableData.mutableBytes;
        localCrc64 = [OSSUtil crc64ecma:localCrc64 buffer:bytes length:data.length];
        [receivedData appendData:data];
    }
};
__block uint64_t remoteCrc64 = 0;
OSSTask * task = [client getObject:request];
[task continueWithBlock:^id(OSSTask *task) {
    OSSGetObjectResult *result = task.result;
    if (result.remoteCRC64ecma)
    {
        NSScanner *scanner = [NSScanner scannerWithString:result.remoteCRC64ecma];
        [scanner scanUnsignedLongLong:&remoteCrc64];
        if (remoteCrc64 == localCrc64)
        {
            NSLog(@"crc64校验成功!");
        }
        else
        {
            NSLog(@"crc64校验失败!");
        }
   }
   return nil;
}];
// waitUntilFinished会阻塞当前线程，但是不会阻塞上传任务进程。
// [task waitUntilFinished];
```

[上一篇：对象标签（iOS SDK）](/zh/oss/developer-reference/object-tagging-1)[下一篇：图片处理（iOS SDK）](/zh/oss/developer-reference/img-8)该文章对您有帮助吗？反馈
  
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