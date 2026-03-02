# iOS通过示例代码实现OSS资源断点续传下载

Source: https://help.aliyun.com/zh/oss/developer-reference/resumable-download

---

- iOS通过示例代码实现OSS资源断点续传下载-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 断点续传下载（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
断点续传下载是指客户端在从网络上下载资源时，由于某种原因中断下载。再次开启下载时可以从已下载完成的部分开始继续下载未完成的部分，从而节省时间和流量。

## 流程说明

在手机端使用App下载视频时，下载期间如果从Wifi模式切换到移动网络，App默认会中断下载。开启断点续传下载后，当您从移动网络再次切换到Wifi模式时，即可从上一次中断的位置继续下载。

执行断点续传下载操作时，效果图如下所示。

断点续传下载流程如下所示。

## 功能说明
- HTTP1.1中新增了Range头的支持，用于指定获取数据的范围。Range的格式分为以下几种。数据范围说明Range: bytes=100-从101字节之后开始传输，直到传输到最后一个字节。Range: bytes=100-200从101字节开始传输，到201字节结束。通常用于较大的文件分片传输，例如视频传输。Range: bytes=-100传输倒数100字节的内容，不是从0开始的100字节。Range: bytes=0-100, 200-300同时指定多个范围的内容。
- 断点续传下载时需要使用`If-Match`头来验证服务器上的文件是否发生变化，`If-Match`对应的是`ETag`的值。
- 客户端发起请求时在Header中携带`Range`、`If-Match`，OSS Server收到请求后会验证If-Match中的ETag值。如果不匹配，则返回412 precondition状态码。
- OSS Server针对GetObject目前已支持`Range`、`If-Match`、`If-None-Match`、`If-Modified-Since`、`If-Unmodified-Since`，因此您可以在移动端实践OSS资源的断点续传下载功能。

## 示例代码
重要 
OSS iOS SDK不支持断点续传下载。以下代码仅供参考了解下载流程，不建议在生产项目中使用。如需下载，可自行实现或使用第三方开源的下载框架。

iOS断点续传下载示例代码如下：

```
#import "DownloadService.h"
#import "OSSTestMacros.h"

@implementation DownloadRequest

@end

@implementation Checkpoint

- (instancetype)copyWithZone:(NSZone *)zone {
    Checkpoint *other = [[[self class] allocWithZone:zone] init];

    other.etag = self.etag;
    other.totalExpectedLength = self.totalExpectedLength;

    return other;
}

@end

@interface DownloadService()

@property (nonatomic, strong) NSURLSession *session;         // 网络会话。
@property (nonatomic, strong) NSURLSessionDataTask *dataTask;   // 数据请求任务。
@property (nonatomic, copy) DownloadFailureBlock failure;    // 请求出错。
@property (nonatomic, copy) DownloadSuccessBlock success;    // 请求成功。
@property (nonatomic, copy) DownloadProgressBlock progress;  // 下载进度。
@property (nonatomic, copy) Checkpoint *checkpoint;        // 检查节点。
@property (nonatomic, copy) NSString *requestURLString;    // 文件资源地址，用于下载请求。
@property (nonatomic, copy) NSString *headURLString;       // 文件资源地址，用于head请求。
@property (nonatomic, copy) NSString *targetPath;     // 文件存储路径。
@property (nonatomic, assign) unsigned long long totalReceivedContentLength; // 已下载文件大小。
@property (nonatomic, strong) dispatch_semaphore_t semaphore;

@end

@implementation DownloadService

- (instancetype)init
{
    self = [super init];
    if (self) {
        NSURLSessionConfiguration *conf = [NSURLSessionConfiguration defaultSessionConfiguration];
        conf.timeoutIntervalForRequest = 15;

        NSOperationQueue *processQueue = [NSOperationQueue new];
        _session = [NSURLSession sessionWithConfiguration:conf delegate:self delegateQueue:processQueue];
        _semaphore = dispatch_semaphore_create(0);
        _checkpoint = [[Checkpoint alloc] init];
    }
    return self;
}
// DownloadRequest是下载逻辑的核心。
+ (instancetype)downloadServiceWithRequest:(DownloadRequest *)request {
    DownloadService *service = [[DownloadService alloc] init];
    if (service) {
        service.failure = request.failure;
        service.success = request.success;
        service.requestURLString = request.sourceURLString;
        service.headURLString = request.headURLString;
        service.targetPath = request.downloadFilePath;
        service.progress = request.downloadProgress;
        if (request.checkpoint) {
            service.checkpoint = request.checkpoint;
        }
    }
    return service;
}

/**
 * 通过Head方法获取文件信息。OSS将文件的ETag和本地checkpoint中保存的ETag进行对比，并返回对比结果。
 */
- (BOOL)getFileInfo {
    __block BOOL resumable = NO;
    NSURL *url = [NSURL URLWithString:self.headURLString];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc]initWithURL:url];
    [request setHTTPMethod:@"HEAD"];
    // 处理Object相关信息，例如ETag用于断点续传时进行预检查，content-length用于计算下载进度。
    NSURLSessionDataTask *task = [[NSURLSession sharedSession] dataTaskWithRequest:request completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
        if (error) {
            NSLog(@"获取文件meta信息失败,error : %@", error);
        } else {
            NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)response;
            NSString *etag = [httpResponse.allHeaderFields objectForKey:@"Etag"];
            if ([self.checkpoint.etag isEqualToString:etag]) {
                resumable = YES;
            } else {
                resumable = NO;
            }
        }
        dispatch_semaphore_signal(self.semaphore);
    }];
    [task resume];

    dispatch_semaphore_wait(self.semaphore, DISPATCH_TIME_FOREVER);
    return resumable;
}

/**
 * 获取本地文件的大小。
 */
- (unsigned long long)fileSizeAtPath:(NSString *)filePath {
    unsigned long long fileSize = 0;
    NSFileManager *dfm = [NSFileManager defaultManager];
    if ([dfm fileExistsAtPath:filePath]) {
        NSError *error = nil;
        NSDictionary *attributes = [dfm attributesOfItemAtPath:filePath error:&error];
        if (!error && attributes) {
            fileSize = attributes.fileSize;
        } else if (error) {
            NSLog(@"error: %@", error);
        }
    }

    return fileSize;
}

- (void)resume {
    NSURL *url = [NSURL URLWithString:self.requestURLString];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc]initWithURL:url];
    [request setHTTPMethod:@"GET"];

    BOOL resumable = [self getFileInfo];    // 如果resumable返回NO，表明不满足断点续传的条件。
    if (resumable) {
        self.totalReceivedContentLength = [self fileSizeAtPath:self.targetPath];
        NSString *requestRange = [NSString stringWithFormat:@"bytes=%llu-", self.totalReceivedContentLength];
        [request setValue:requestRange forHTTPHeaderField:@"Range"];
    } else {
        self.totalReceivedContentLength = 0;
    }

    if (self.totalReceivedContentLength == 0) {
        [[NSFileManager defaultManager] createFileAtPath:self.targetPath contents:nil attributes:nil];
    }

    self.dataTask = [self.session dataTaskWithRequest:request];
    [self.dataTask resume];
}

- (void)pause {
    [self.dataTask cancel];
    self.dataTask = nil;
}

- (void)cancel {
    [self.dataTask cancel];
    self.dataTask = nil;
    [self removeFileAtPath: self.targetPath];
}

- (void)removeFileAtPath:(NSString *)filePath {
    NSError *error = nil;
    [[NSFileManager defaultManager] removeItemAtPath:self.targetPath error:&error];
    if (error) {
        NSLog(@"remove file with error : %@", error);
    }
}

#pragma mark - NSURLSessionDataDelegate

- (void)URLSession:(NSURLSession *)session task:(NSURLSessionTask *)task
// 判断下载任务是否完成，然后将结果返回给上层业务。
didCompleteWithError:(nullable NSError *)error {
    NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)task.response;
    if ([httpResponse isKindOfClass:[NSHTTPURLResponse class]]) {
        if (httpResponse.statusCode == 200) {
            self.checkpoint.etag = [[httpResponse allHeaderFields] objectForKey:@"Etag"];
            self.checkpoint.totalExpectedLength = httpResponse.expectedContentLength;
        } else if (httpResponse.statusCode == 206) {
            self.checkpoint.etag = [[httpResponse allHeaderFields] objectForKey:@"Etag"];
            self.checkpoint.totalExpectedLength = self.totalReceivedContentLength + httpResponse.expectedContentLength;
        }
    }

    if (error) {
        if (self.failure) {
            NSMutableDictionary *userInfo = [NSMutableDictionary dictionaryWithDictionary:error.userInfo];
            [userInfo oss_setObject:self.checkpoint forKey:@"checkpoint"];

            NSError *tError = [NSError errorWithDomain:error.domain code:error.code userInfo:userInfo];
            self.failure(tError);
        }
    } else if (self.success) {
        self.success(@{@"status": @"success"});
    }
}

- (void)URLSession:(NSURLSession *)session dataTask:(NSURLSessionDataTask *)dataTask didReceiveResponse:(NSURLResponse *)response completionHandler:(void (^)(NSURLSessionResponseDisposition))completionHandler
{
    NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse *)dataTask.response;
    if ([httpResponse isKindOfClass:[NSHTTPURLResponse class]]) {
        if (httpResponse.statusCode == 200) {
            self.checkpoint.totalExpectedLength = httpResponse.expectedContentLength;
        } else if (httpResponse.statusCode == 206) {
            self.checkpoint.totalExpectedLength = self.totalReceivedContentLength +  httpResponse.expectedContentLength;
        }
    }

    completionHandler(NSURLSessionResponseAllow);
}
// 将接收到的网络数据以追加上传的方式写入到文件中，并更新下载进度。
- (void)URLSession:(NSURLSession *)session dataTask:(NSURLSessionDataTask *)dataTask didReceiveData:(NSData *)data {

    NSFileHandle *fileHandle = [NSFileHandle fileHandleForWritingAtPath:self.targetPath];
    [fileHandle seekToEndOfFile];
    [fileHandle writeData:data];
    [fileHandle closeFile];

    self.totalReceivedContentLength += data.length;
    if (self.progress) {
        self.progress(data.length, self.totalReceivedContentLength, self.checkpoint.totalExpectedLength);
    }
}

@end
```
- DownloadRequest定义
```
#import 

typedef void(^DownloadProgressBlock)(int64_t bytesReceived, int64_t totalBytesReceived, int64_t totalBytesExpectToReceived);
typedef void(^DownloadFailureBlock)(NSError *error);
typedef void(^DownloadSuccessBlock)(NSDictionary *result);

@interface Checkpoint : NSObject

@property (nonatomic, copy) NSString *etag;     // 资源的ETag值。
@property (nonatomic, assign) unsigned long long totalExpectedLength;    // 文件总大小。

@end

@interface DownloadRequest : NSObject

@property (nonatomic, copy) NSString *sourceURLString;      // 下载的URL。

@property (nonatomic, copy) NSString *headURLString;        // 获取文件元数据的URL。

@property (nonatomic, copy) NSString *downloadFilePath;     // 文件的本地存储地址。

@property (nonatomic, copy) DownloadProgressBlock downloadProgress; // 下载进度。

@property (nonatomic, copy) DownloadFailureBlock failure;   // 下载成功的回调。

@property (nonatomic, copy) DownloadSuccessBlock success;   // 下载失败的回调。

@property (nonatomic, copy) Checkpoint *checkpoint;         // 存储文件的ETag。

@end

@interface DownloadService : NSObject

+ (instancetype)downloadServiceWithRequest:(DownloadRequest *)request;

/**
 * 启动下载。
 */
- (void)resume;

/**
 * 暂停下载。
 */
- (void)pause;

/**
 * 取消下载。
 */
- (void)cancel;

@end
```
- 上层业务调用
```
- (void)initDownloadURLs {
    OSSPlainTextAKSKPairCredentialProvider *pCredential = [[OSSPlainTextAKSKPairCredentialProvider alloc] initWithPlainTextAccessKey:OSS_ACCESSKEY_ID secretKey:OSS_SECRETKEY_ID];
    _mClient = [[OSSClient alloc] initWithEndpoint:OSS_ENDPOINT credentialProvider:pCredential];

    // 生成用于Get请求的带签名的URL。
    OSSTask *downloadURLTask = [_mClient presignConstrainURLWithBucketName:@"aliyun-dhc-shanghai" withObjectKey:OSS_DOWNLOAD_FILE_NAME withExpirationInterval:1800];
    [downloadURLTask waitUntilFinished];
    _downloadURLString = downloadURLTask.result;

    // 生成用于Head请求的带签名的URL。
    OSSTask *headURLTask = [_mClient presignConstrainURLWithBucketName:@"aliyun-dhc-shanghai" withObjectKey:OSS_DOWNLOAD_FILE_NAME httpMethod:@"HEAD" withExpirationInterval:1800 withParameters:nil];
    [headURLTask waitUntilFinished];

    _headURLString = headURLTask.result;
}

- (IBAction)resumeDownloadClicked:(id)sender {
    _downloadRequest = [DownloadRequest new];
    _downloadRequest.sourceURLString = _downloadURLString;       // 设置资源的URL。
    _downloadRequest.headURLString = _headURLString;
    NSString *documentPath = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject;
    _downloadRequest.downloadFilePath = [documentPath stringByAppendingPathComponent:OSS_DOWNLOAD_FILE_NAME];   // 设置下载文件的本地保存路径。

    __weak typeof(self) wSelf = self;
    _downloadRequest.downloadProgress = ^(int64_t bytesReceived, int64_t totalBytesReceived, int64_t totalBytesExpectToReceived) {
        // totalBytesReceived表示当前客户端已缓存的字节数，totalBytesExpectToReceived表示待下载的总字节数。
        dispatch_async(dispatch_get_main_queue(), ^{
            __strong typeof(self) sSelf = wSelf;
            CGFloat fProgress = totalBytesReceived * 1.f / totalBytesExpectToReceived;
            sSelf.progressLab.text = [NSString stringWithFormat:@"%.2f%%", fProgress * 100];
            sSelf.progressBar.progress = fProgress;
        });
    };
    _downloadRequest.failure = ^(NSError *error) {
        __strong typeof(self) sSelf = wSelf;
        sSelf.checkpoint = error.userInfo[@"checkpoint"];
    };
    _downloadRequest.success = ^(NSDictionary *result) {
        NSLog(@"下载成功");
    };
    _downloadRequest.checkpoint = self.checkpoint;

    NSString *titleText = [[_downloadButton titleLabel] text];
    if ([titleText isEqualToString:@"download"]) {
        [_downloadButton setTitle:@"pause" forState: UIControlStateNormal];
        _downloadService = [DownloadService downloadServiceWithRequest:_downloadRequest];
        [_downloadService resume];
    } else {
        [_downloadButton setTitle:@"download" forState: UIControlStateNormal];
        [_downloadService pause];
    }
}

- (IBAction)cancelDownloadClicked:(id)sender {
    [_downloadButton setTitle:@"download" forState: UIControlStateNormal];
    [_downloadService cancel];
}
```
说明 
暂停或取消下载时均能从failure回调中获取checkpoint。重启下载时，可以将checkpoint传到DownloadRequest，然后 DownloadService将使用checkpoint执行一致性校验。

[上一篇：范围下载（iOS SDK）](/zh/oss/developer-reference/range-download-7)[下一篇：限定条件下载（iOS SDK）](/zh/oss/developer-reference/conditional-download-6)该文章对您有帮助吗？反馈
  
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