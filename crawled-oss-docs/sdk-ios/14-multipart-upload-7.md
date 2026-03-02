# 使用iOS SDK分片上传大文件

Source: https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-7

---

- 使用iOS SDK分片上传大文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 分片上传（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS的分片上传（Multipart Upload）用于将要上传的较大的文件（Object）分成多个数据块（OSS中称之为Part）来分别上传，上传完成后再调用CompleteMultipartUpload接口将这些Part组合成一个Object。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化（iOS SDK）](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。说明 所创建存储空间的所属地域取决于初始化配置的endpoint地域信息。
- 要上传文件，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 分片上传流程

分片上传的基本流程如下：
- 将要上传的文件按照一定的大小分片。
- 初始化一个分片上传任务（[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)）。
- 逐个或并行上传分片（[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)）。
- 完成上传（[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)）。

该过程需注意以下几点：
- 除了最后一块Part，其他Part的大小不能小于100 KB，否则会导致调用CompleteMultipartUpload接口失败。
- 要上传的文件切分成Part之后，文件顺序是通过上传过程中指定的partNumber来确定的，实际执行中并没有顺序要求，因此可以实现并发上传。 具体的并发个数并不是越多速度越快，要结合用户自身的网络情况和设备负载综合考虑。网络情况较好时，建议增大分片大小。反之，减小分片大小。
- 默认情况下，已经上传但还没有调用CompleteMultipartUpload的Part是不会被自动回收的，因此如果要终止上传并删除占用的空间请调用[AbortMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)。如果需要自动回收上传的Part，请参见[生命周期管理](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#concept-y2g-szy-5db)。

## 分片上传完整示例

以下通过一个完整的示例对分片上传的流程进行逐步解析：

```
__block NSString * uploadId = nil;
__block NSMutableArray * partInfos = [NSMutableArray new];
// 填写Bucket名称，例如examplebucket。
NSString * uploadToBucket = @"examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
NSString * uploadObjectkey = @"exampledir/exampleobject.txt";
// OSSInitMultipartUploadRequest用于指定上传文件的名称以及上传文件所属的存储空间的名称。
OSSInitMultipartUploadRequest * init = [OSSInitMultipartUploadRequest new];
init.bucketName = uploadToBucket;
init.objectKey = uploadObjectkey;
// init.contentType = @"application/octet-stream";
// multipartUploadInit返回的结果中包含UploadId，UploadId是分片上传的唯一标识。
OSSTask * initTask = [client multipartUploadInit:init];
[initTask waitUntilFinished];
if (!initTask.error) {
    OSSInitMultipartUploadResult * result = initTask.result;
    uploadId = result.uploadId;
    // 根据uploadId执行取消分片上传事件或者列举已上传分片的操作。
    // 如果您需要根据您需要uploadId执行取消分片上传事件的操作，您需要在调用InitiateMultipartUpload完成初始化分片之后获取uploadId。
    // 如果您需要根据您需要uploadId执行列举已上传分片的操作，您需要在调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前获取uploadId。
    //NSLog(@"UploadId": %@, uploadId);
} else {
    NSLog(@"multipart upload failed, error: %@", initTask.error);
    return;
}

// 指定要上传的文件。
NSString * filePath = @"";
// 获取文件大小。
uint64_t fileSize = [[[NSFileManager defaultManager] attributesOfItemAtPath:filePath error:nil] fileSize];
// 设置分片上传数量。
int chuckCount = 10;
// 设置分片大小。
uint64_t offset = fileSize/chuckCount;
for (int i = 1; i 
## 本地文件分片上传
说明 
分片上传完整示例是按照分片上传流程逐步实现的完整代码，本地文件分片上传的代码是将分片上传完整示例中的代码进行了封装，您只需要使用MultipartUploadRequest即可实现分片上传。

以分片上传的方式上传本地文件的代码示例如下。

```
// 填写Bucket名称，例如examplebucket。
NSString *bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
NSString *objectKey = @"exampledir/exampleobject.txt";

OSSMultipartUploadRequest * multipartUploadRequest = [OSSMultipartUploadRequest new];
multipartUploadRequest.bucketName = bucketName;
multipartUploadRequest.objectKey = objectKey;
// 设置分片大小，默认256 KB。
multipartUploadRequest.partSize = 1024 * 1024;
multipartUploadRequest.uploadProgress = ^(int64_t bytesSent, int64_t totalByteSent, int64_t totalBytesExpectedToSend) {
    NSLog(@"progress: %lld, %lld, %lld", bytesSent, totalByteSent, totalBytesExpectedToSend);
};

multipartUploadRequest.uploadingFileURL = [[NSBundle mainBundle] URLForResource:@"wangwang" withExtension:@"zip"];
OSSTask * multipartTask = [client multipartUpload:multipartUploadRequest];
[[multipartTask continueWithBlock:^id(OSSTask *task) {
    if (task.error) {
        NSLog(@"error: %@", task.error);
    } else {
        NSLog(@"Upload file success");
    }
    return nil;
}] waitUntilFinished];
```

## 列举已上传分片

调用`listParts`方法获取某个上传事件所有已上传的分片。

```
OSSListPartsRequest * listParts = [OSSListPartsRequest new];
// 填写Bucket名称，例如examplebucket。
listParts.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
listParts.objectKey = @"exampledir/exampleobject.txt";
// 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前的返回结果。
listParts.uploadId = @"0004B999EF518A1FE585B0C9****";

OSSTask * listPartTask = [client listParts:listParts];

[listPartTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        NSLog(@"list part result success!");
        OSSListPartsResult * listPartResult = task.result;
        for (NSDictionary * partInfo in listPartResult.parts) {
            NSLog(@"each part: %@", partInfo);
        }
    } else {
        NSLog(@"list part result error: %@", task.error);
    }
    return nil;
}];
// waitUntilFinished会阻塞当前线程，但是不会阻塞上传任务进程。
// [listPartTask waitUntilFinished];            
```
重要 
默认情况下，如果存储空间中的分片上传事件的数量大于1000，则OSS仅返回1000个Multipart Upload信息，且返回结果中IsTruncated的值为false，并返回NextPartNumberMarker作为下次读取的起点。

## 取消分片上传

以下代码用于取消了对应`UploadId`的分片上传请求。

```
OSSAbortMultipartUploadRequest * abort = [OSSAbortMultipartUploadRequest new];
// 填写Bucket名称，例如examplebucket。
abort.bucketName = @"examplebucket";
// 填写文件完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
abort.objectKey = @"exampledir/exampleobject.txt";
// 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后的返回结果。
abort.uploadId = @"0004B999EF518A1FE585B0C9****";

OSSTask * abortTask = [client abortMultipartUpload:abort];

[abortTask waitUntilFinished];

if (!abortTask.error) {
    OSSAbortMultipartUploadResult * result = abortTask.result;
    uploadId = result.uploadId;
} else {
    NSLog(@"multipart upload failed, error: %@", abortTask.error);
    return;
}
// waitUntilFinished会阻塞当前线程，但是不会阻塞上传任务进程。
// [abortTask waitUntilFinished];            
```

## 相关文档
- 关于分片上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-ios-sdk/blob/master/AliyunOSSiOSTests/OSSObjectTests.m?file=OSSObjectTests.m)。
- 分片上传的完整实现涉及三个API接口，详情如下：关于初始化分片上传事件的API接口说明，请参见[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)。
- 关于分片上传Part的API接口说明，请参见[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)。
- 关于完成分片上传的API接口说明，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。
- 关于列举已上传分片的API接口说明，请参见[ListParts](https://help.aliyun.com/zh/oss/developer-reference/listparts#reference-hzm-1zx-wdb)。
- 关于取消分片上传事件的API接口说明，请参见[AbortMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)。

[上一篇：简单上传（iOS SDK）](/zh/oss/developer-reference/simple-upload-5)[下一篇：追加上传（iOS SDK）](/zh/oss/developer-reference/append-upload-7)该文章对您有帮助吗？反馈
  
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