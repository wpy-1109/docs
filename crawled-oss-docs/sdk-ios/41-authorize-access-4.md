# iOSSDK多种访问授权实现方法

Source: https://help.aliyun.com/zh/oss/developer-reference/authorize-access-4

---

- iOSSDK多种访问授权实现方法-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 授权访问（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
iOS SDK提供了STS鉴权模式、自签名模式以及URL预签名的方式来保障移动终端的安全性。

## 注意事项

无论是STS鉴权模式还是自签名模式，您实现的回调函数都需要保证调用时Token、Signature的返回结果。如果您需要实现向业务Server获取Token、Signature的网络请求，建议调用网络库的同步接口。回调都是在SDK发起具体请求时，在请求的子线程中执行，所以不会阻塞主线程。

## STS鉴权模式

通过STS临时授权访问OSS的步骤如下：
- 获取临时访问凭证临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。临时访问凭证有效时间单位为秒，最小值为900，最大值以当前角色设定的最大会话时间为准。更多信息，请参见[设置RAM角色最大会话时间](https://help.aliyun.com/zh/ram/user-guide/specify-the-maximum-session-duration-for-a-ram-role#task-2498608)。您可以通过以下两种方式获取临时访问凭证。方式一通过调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/api-assumerole#reference-clc-3sv-xdb)接口获取临时访问凭证。
- 方式二通过[各语言STS SDK](https://help.aliyun.com/zh/ram/developer-reference/sts-sdk-overview#reference-w5t-25v-xdb)获取临时访问凭证。
- 使用临时访问凭证初始化SDK
```
id credential = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:@"" secretKeyId:@"" securityToken:@""];
client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credential];
```
说明 如果您需要使用OSSAuthCredentialProvider初始化SDK，请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。通过临时访问凭证初始化SDK时，需要注意StsToken的有效时间。以下代码用于判断StsToken的有效时间：
```
NSDateFormatter * fm = [NSDateFormatter new];
fm.locale = [NSLocale localeWithLocaleIdentifier:@"en_US_POSIX"];
[fm setDateFormat:@"yyyy-MM-dd'T'HH:mm:ssZ"];
NSDate *expirationDate = [fm dateFromString:@""];
NSTimeInterval interval = [expirationDate timeIntervalSinceDate:[NSDate date]];
// 即将过期，有效时间小于5分钟。
if (interval  credential = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:@"" secretKeyId:@"" securityToken:@""];
    client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credential];
}
```
手动更新StsToken当判断StsToken即将过期时，您可以重新构造OSSClient，也可以通过如下方式更新CredentialProvider。
```
id credential = [[OSSStsTokenCredentialProvider alloc] initWithAccessKeyId:@"" secretKeyId:@"" securityToken:@""];
client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credential];
```
- 自动更新StsToken如果您期望SDK自动更新StsToken，那么您需要在SDK的应用中实现回调。通过您实现回调的方式去获取Federation Token（即StsToken），SDK会使用此StsToken来进行加签处理，并在需要更新时主动调用此回调来获取StsToken。
```
id credential = [[OSSFederationCredentialProvider alloc] initWithFederationTokenGetter:^OSSFederationToken * {
    // 您需要在此处实现获取一个FederationToken，并构造成OSSFederationToken对象返回。
    // 如果由于某种原因获取失败，直接返回nil。
      OSSFederationToken * token;
    // 从您的服务器中获取token。
    ...
    return token;
}];
client = [[OSSClient alloc] initWithEndpoint:endpoint credentialProvider:credential];
```
说明 如果您已经通过其他方式获取了StsToken所需的各个字段，也可以在回调中直接返回StsToken。但您需要手动处理StsToken的更新，且更新后重新设置该OSSClient实例的OSSCredentialProvider。假设您访问的Server地址为http://localhost:8080/distribute-token.json，则返回的数据如下：
```
{
    "StatusCode": 200,
    "AccessKeyId":"STS.iA645eTOXEqP3cg3****",
    "AccessKeySecret":"rV3VQrpFQ4BsyHSAvi5NVLpPIVffDJv4LojU****",
    "Expiration":"2015-11-03T09:52:59Z",
    "SecurityToken":"CAES7QIIARKAAZPlqaN9ILiQZPS+JDkS/GSZN45RLx4YS/p3OgaUC+oJl3XSlbJ7StKpQ****"
}                           
```
实现OSSFederationCredentialProvider的示例如下。
```
id credential2 = [[OSSFederationCredentialProvider alloc] initWithFederationTokenGetter:^OSSFederationToken * {
    // 构造请求访问您的业务Server。
    NSURL * url = [NSURL URLWithString:@"http://localhost:8080/distribute-token.json"];
    // 通过request设置自有服务器需要的参数。
    NSURLRequest * request = [NSURLRequest requestWithURL:url];
    OSSTaskCompletionSource * tcs = [OSSTaskCompletionSource taskCompletionSource];
    NSURLSession * session = [NSURLSession sharedSession];
    // 发送请求。
    NSURLSessionTask * sessionTask = [session dataTaskWithRequest:request
                                                completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
                                                    if (error) {
                                                        [tcs setError:error];
                                                        return;
                                                    }
                                                    [tcs setResult:data];
                                                }];
    [sessionTask resume];
    // 需要阻塞等待请求返回。
    [tcs.task waitUntilFinished];
    // 解析结果。
    if (tcs.task.error) {
        NSLog(@"get token error: %@", tcs.task.error);
        return nil;
    } else {
        // 返回数据为JSON格式，需要解析返回数据得到token的各个字段。
        NSDictionary * object = [NSJSONSerialization JSONObjectWithData:tcs.task.result
                                                                options:kNilOptions
                                                                  error:nil];
        OSSFederationToken * token = [OSSFederationToken new];
        token.tAccessKey = [object objectForKey:@"AccessKeyId"];
        token.tSecretKey = [object objectForKey:@"AccessKeySecret"];
        token.tToken = [object objectForKey:@"SecurityToken"];
        token.expirationTimeInGMTFormat = [object objectForKey:@"Expiration"];
        NSLog(@"get token: %@", token);
        return token;
    }
}];
```

## 预签名URL

### 注意事项
- 生成预签名URL过程中，SDK利用本地存储的密钥信息，根据特定算法计算出签名（signature），然后将其附加到URL上，以确保URL的有效性和安全性。这一系列计算和构造URL的操作都是在客户端完成，不涉及网络请求到服务端。因此，生成预签名URL时不需要授予调用者特定权限。但是，为避免第三方用户无法对预签名URL授权的资源执行相关操作，需要确保调用生成预签名URL接口的身份主体被授予对应的权限。例如，通过预签名URL上传文件时，需要授予oss:PutObject权限。通过预签名URL下载或预览文件时，需要授予oss:GetObject权限。
- 通过以下示例生成的预签名URL中如果包含特殊符号`+`，可能出现无法正常访问该预签名URL的现象。如需正常访问该预签名URL，请将预签名URL中的`+`替换为`%2B`。

### 使用预签名URL上传文件
- 生成用于上传文件的预签名URL。
```
// 填写Bucket名称。
NSString *bucketName = @"examplebucket";
// 填写Object名称。
NSString *objectKey = @"exampleobject.txt";
NSURL *file = [NSURL fileURLWithPath:@""];
NSString *contentType = [OSSUtil detemineMimeTypeForFilePath:file.absoluteString uploadName:objectKey];
__block NSString *urlString;
// 生成用于上传的预签名URL，并指定预签名URL过期时间为30分钟。
OSSTask *task = [client presignConstrainURLWithBucketName:bucketName
                                            withObjectKey:objectKey
                                               httpMethod:@"PUT"
                                   withExpirationInterval:30 * 60
                                           withParameters:@{}
                                              contentType:contentType
                                               contentMd5:nil];
[task continueWithBlock:^id _Nullable(OSSTask * _Nonnull task) {
    if (task.error) {
        NSLog(@"presign error: %@", task.error);
    } else {
        urlString = task.result;
        NSLog(@"url: %@", urlString);
    }
    return nil;
}];
```
- 使用预签名URL上传文件。
```
// 通过预签名URL上传文件。
NSURL * url = [NSURL URLWithString:urlString];
NSMutableURLRequest * request = [NSMutableURLRequest requestWithURL:url];
request.HTTPMethod = @"PUT";
request.allHTTPHeaderFields = @{OSSHttpHeaderContentType: contentType};
NSURLSession * session = [NSURLSession sharedSession];
NSURLSessionTask * sessionTask = [session uploadTaskWithRequest:request
                                                       fromFile:file
                                              completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
    if (error) {
        NSLog(@"upload error: %@", error);
        return;
    } else if (((NSHTTPURLResponse*)response).statusCode == 203 ||
               ((NSHTTPURLResponse*)response).statusCode >= 300) {
        NSString *body = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
        NSLog(@"upload error: %@", body);
        return;
    }
    NSLog(@"upload success");
}];
[sessionTask resume];
```

### 使用预签名URL下载文件
- 生成用于下载文件的预签名URL。
```
// 填写Bucket名称。
NSString *bucketName = @"examplebucket";
// 填写Object名称。
NSString *objectKey = @"exampleobject.txt";
__block NSString *urlString;
// 生成用于下载的预签名URL，并指定预签名URL过期时间为30分钟。
OSSTask *task = [client presignConstrainURLWithBucketName:bucketName
                                            withObjectKey:objectKey
                                               httpMethod:@"GET"
                                   withExpirationInterval:30 * 60
                                           withParameters:@{}];
[task continueWithBlock:^id _Nullable(OSSTask * _Nonnull task) {
    if (task.error) {
        NSLog(@"presign error: %@", task.error);
    } else {
        urlString = task.result;
        NSLog(@"url: %@", urlString);
    }
    return nil;
}];
```
- 使用预签名URL下载文件。
```
// 使用预签名URL下载文件。
NSURL * url = [NSURL URLWithString:urlString];
NSURLRequest * request = [NSURLRequest requestWithURL:url];
NSURLSession * session = [NSURLSession sharedSession];
NSURLSessionTask * sessionTask = [session dataTaskWithRequest:request
                                            completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
    if (error) {
        NSLog(@"download error: %@", error);
        return;
    } else if (((NSHTTPURLResponse*)response).statusCode == 203 ||
               ((NSHTTPURLResponse*)response).statusCode >= 300) {
        NSString *body = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
        NSLog(@"download error: %@", body);
        return;
    }
    NSLog(@"download success");
}];
[sessionTask resume];
```

[上一篇：图片处理（iOS SDK）](/zh/oss/developer-reference/img-8)[下一篇：异常响应（iOS SDK）](/zh/oss/developer-reference/handle-exceptions)该文章对您有帮助吗？反馈
  
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