# 使用iOS SDK设置获取和删除对象标签

Source: https://help.aliyun.com/zh/oss/developer-reference/object-tagging-1

---

- 使用iOS SDK设置获取和删除对象标签-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 对象标签（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS支持使用标签对存储空间（Bucket）中的文件（Object）进行分类。本文介绍如何设置、获取以及删除Object标签。

## 注意事项

使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。

## 设置对象标签

### 上传Object时设置对象标签

以下代码用于上传Object时设置对象标签。

```
OSSPutObjectRequest * put = [OSSPutObjectRequest new];

// 填写Bucket名称，例如examplebucket。
put.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
put.objectKey = @"exampledir/exampleobject.txt";
put.uploadingFileURL = [NSURL fileURLWithPath:@""];
// 设置对象标签信息，例如标签的key为owner，value为John。
NSDictionary *tagging = @{@"owner": @"John"};
put.objectMeta = @{@"x-oss-tagging": [OSSUtil populateQueryStringFromParameter:tagging]};

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
// [putTask waitUntilFinished];
// [put cancel];
```

### 为已上传Object添加或更改对象标签

以下代码用于为已上传Object添加或更改对象标签。

```
OSSPutObjectTaggingRequest *putTaggingRequest = [OSSPutObjectTaggingRequest new];
// 填写Bucket名称，例如examplebucket。
putTaggingRequest.bucketName = @"examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
putTaggingRequest.objectKey = @"exampledir/exampleobject.txt";
// 设置标签信息。
NSDictionary *tags = @{@"key1":@"value1", @"key2":@"value2"};
putTaggingRequest.tags = tags;
OSSTask * putTask= [client putObjectTagging:putTaggingRequest];
[putTask continueWithBlock:^id _Nullable(OSSTask * _Nonnull task) {
    if (task.error) {
        NSLog(@"error: %@", task.error);
    } else {
        NSLog(@"put tagging success");
    }
    return nil;
}];
// [putTask waitUntilFinished];
```

### 拷贝Object时设置对象标签

以下代码用于拷贝Object时设置对象标签。

```
OSSCopyObjectRequest * copy = [OSSCopyObjectRequest new];
// 填写源Bucket名称。
copy.sourceBucketName = @"sourceBucketName";
// 填写源objectKey。
copy.sourceObjectKey = @"sourceObjectKey";
// 填写目标Bucket名称。
copy.bucketName = @"bucketName";
// 填写目标objectKey。
copy.objectKey = @"objectKey";
// 设置对象标签信息。
NSDictionary *tagging = @{@"owner": @"John"};
copy.objectMeta = @{
    @"x-oss-tagging": [OSSUtil populateQueryStringFromParameter:tagging],
    @"x-oss-tagging-directive": @"Replace"
};

OSSTask * task = [client copyObject:copy];
[task continueWithBlock:^id(OSSTask *task) {
    if (task.error) {
        NSLog(@"error: %@", task.error);
    } else {
        NSLog(@"copy object success");
    }
    return nil;
}];
// [task waitUntilFinished];
```

### 为软链接文件设置对象标签

以下代码用于为软链接文件设置对象标签。

```
OSSPutSymlinkRequest * putSymlinkRequest = [OSSPutSymlinkRequest new];
// 填写Bucket名称。
putSymlinkRequest.bucketName = @"examplebucket";
// 填写软链接名称。
putSymlinkRequest.objectKey = @"examplesymlink";
// 填写软链接指定的Object完整路径。Object完整路径中不能包含Bucket名称。
putSymlinkRequest.targetObjectName = @"exampleobject.txt";
// 设置对象标签信息。
NSDictionary *tagging = @{@"owner": @"John"};
putSymlinkRequest.objectMeta = @{
    @"x-oss-tagging": [OSSUtil populateQueryStringFromParameter:tagging],
};

OSSTask * putSymlinktask = [client putSymlink:putSymlinkRequest];
[putSymlinktask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"put symlink success");
    } else {
        NSLog(@"put symlink failed, error: %@", task.error);
    }
    return nil;
}];
// [putSymlinktask waitUntilFinished];
```

## 获取Object标签信息

以下代码用于获取Object的标签信息。

```
OSSGetObjectTaggingRequest *getTaggingRequest = [OSSGetObjectTaggingRequest new];
// 填写Bucket名称。
getTaggingRequest.bucketName = @"examplebucket";
// 填写Object名称。
getTaggingRequest.objectKey = @"exampledir/exampleobject.txt";
OSSTask * getTask = [client getObjectTagging:getTaggingRequest];
// 获取Object的标签信息。
[getTask continueWithBlock:^id _Nullable(OSSTask * _Nonnull task) {
    if (!task.error) {
        OSSGetObjectTaggingResult *result = task.result;
        for (NSString *key in [result.tags allKeys]) {
            NSLog(@"tagging %@: %@", key, result.tags[key]);
        }
    } else {
        NSLog(@"get object tagging fail! error: %@", task.error);
    }

    return nil;
}];
// [getTask waitUntilFinished];
```

## 删除Object标签信息

以下代码用于删除Object的标签信息。

```
OSSDeleteObjectTaggingRequest *deleteTaggingRequest = [OSSDeleteObjectTaggingRequest new];
// 填写Bucket名称。
deleteTaggingRequest.bucketName = @"examplebucket";
// 填写Object名称。
deleteTaggingRequest.objectKey = @"exampledir/exampleobject.txt";
OSSTask *deleteTask = [client deleteObjectTagging:deleteTaggingRequest];
// 删除Object的标签信息。
[deleteTask continueWithBlock:^id _Nullable(OSSTask * _Nonnull task) {
    if (!task.error) {
        NSLog(@"delete object tagging success");
    } else {
        NSLog(@"delete object tagging fail! error: %@", task.error);
    }
    return nil;
}];
// [deleteTask waitUntilFinished];
```

## 相关文档
- 关于设置Object标签的API接口说明，请参见[PutObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/putobjecttagging#reference-185784)。
- 关于获取Object标签的API接口说明，请参见[GetObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/getobjecttagging#concept-185787)。
- 关于删除Object标签的API接口说明，请参见[DeleteObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/deleteobjecttagging#reference-185788)。

[上一篇：管理文件访问权限（iOS SDK）](/zh/oss/developer-reference/manage-the-acl-of-an-object)[下一篇：数据安全性（iOS SDK）](/zh/oss/developer-reference/data-security-7)该文章对您有帮助吗？反馈
  
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