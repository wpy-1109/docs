# 使用Android SDK完成文件上传下载等常见操作

Source: https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-android

---

- 使用Android SDK完成文件上传下载等常见操作-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 快速入门（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何快速使用OSS Android SDK完成常见操作，例如创建存储空间、上传文件（Object）、下载文件等。

## 前提条件

已安装Android SDK。具体操作，请参见[安装（Android SDK）](https://help.aliyun.com/zh/oss/developer-reference/installation-1#concept-32043-zh)。

## 示例工程

示例工程用法如下：
- 查看sample目录（包含上传本地文件、下载文件、断点续传、设置回调等示例），详情请参见[GitHub](https://github.com/aliyun/aliyun-oss-android-sdk/tree/master/app)。
- 直接git clone[工程](https://github.com/aliyun/aliyun-oss-android-sdk.git)。

运行本工程前，您需要配置必要参数Config。Config配置示例如下：

```
public class Config {    

    // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
    public static final String OSS_ENDPOINT = "https://oss-cn-hangzhou.aliyuncs.com";
    // 填写callback地址。
    public static final String OSS_CALLBACK_URL = "https://oss-demo.aliyuncs.com:23450";
    // 填写STS鉴权服务器地址。
    // 您还可以根据工程sts_local_server目录中本地鉴权服务脚本代码启动本地STS鉴权服务器。
    public static final String STS_SERVER_URL = "http://****/sts/getsts";
    
    public static final String BUCKET_NAME = "yourBucketName";
    public static final String OSS_ACCESS_KEY_ID = "yourAccessKeyId";;
    public static final String OSS_ACCESS_KEY_SECRET = "yourAccessKeySecret";

    public static final int DOWNLOAD_SUC = 1;
    public static final int DOWNLOAD_Fail = 2;
    public static final int UPLOAD_SUC = 3;
    public static final int UPLOAD_Fail = 4;
    public static final int UPLOAD_PROGRESS = 5;
    public static final int LIST_SUC = 6;
    public static final int HEAD_SUC = 7;
    public static final int RESUMABLE_SUC = 8;
    public static final int SIGN_SUC = 9;
    public static final int BUCKET_SUC = 10;
    public static final int GET_STS_SUC = 11;
    public static final int MULTIPART_SUC = 12;
    public static final int STS_TOKEN_SUC = 13;
    public static final int FAIL = 9999;
    public static final int REQUESTCODE_AUTH = 10111;
    public static final int REQUESTCODE_LOCALPHOTOS = 10112;
}
```
- 关于如何配置STS鉴权服务器地址，请参见[快速搭建移动应用直传服务](https://help.aliyun.com/zh/oss/user-guide/set-up-direct-data-transfer-for-mobile-apps#concept-kxc-brw-5db)。
- 关于sts_local_server 脚本内容，请参见[GitHub](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/app/sts_local_server/python)。
- 关于如何创建AccessKey，请参见[创建AccessKey](https://help.aliyun.com/zh/document_detail/53045.html)。

运行工程demo如下：

## 创建存储空间

存储空间是OSS的全局命名空间，相当于数据的容器，可以存储若干文件。以下代码用于创建存储空间。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
String endpoint = "yourEndpoint";
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration config = new ClientConfiguration();
config.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);

// 填写存储空间名称。
CreateBucketRequest createBucketRequest = new CreateBucketRequest("bucketName");
// 设置存储空间的访问权限为公共读，默认为私有读写。
createBucketRequest.setBucketACL(CannedAccessControlList.PublicRead);
// 指定存储空间所在的地域。
createBucketRequest.setLocationConstraint("oss-cn-hangzhou");
OSSAsyncTask createTask = oss.asyncCreateBucket(createBucketRequest, new OSSCompletedCallback() {
    @Override
    public void onSuccess(CreateBucketRequest request, CreateBucketResult result) {
        Log.d("locationConstraint", request.getLocationConstraint());
        }
    @Override
    public void onFailure(CreateBucketRequest request, ClientException clientException, ServiceException serviceException) {
        // 请求异常。
        if (clientException != null) {
            // 本地异常，如网络异常等。
            clientException.printStackTrace();
        }
        if (serviceException != null) {
            // 服务异常。
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
```

## 上传文件

以下代码用于将本地文件上传到OSS。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
String endpoint = "yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration config = new ClientConfiguration();
config.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);

// 构造上传请求。
PutObjectRequest put = new PutObjectRequest("", "", "");

// 异步上传时可以设置进度回调。
put.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(PutObjectRequest request, long currentSize, long totalSize) {
        Log.d("PutObject", "currentSize: " + currentSize + " totalSize: " + totalSize);
    }
});

OSSAsyncTask task = oss.asyncPutObject(put, new OSSCompletedCallback() {
    @Override
    public void onSuccess(PutObjectRequest request, PutObjectResult result) {
        Log.d("PutObject", "UploadSuccess");
        Log.d("ETag", result.getETag());
        Log.d("RequestId", result.getRequestId());
    }

    @Override
    public void onFailure(PutObjectRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 请求异常。
        if (clientExcepion != null) {
            // 本地异常，如网络异常等。
            clientExcepion.printStackTrace();
        }
        if (serviceException != null) {
            // 服务异常。
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
// task.cancel(); // 可以取消任务。
// task.waitUntilFinished(); // 等待上传完成。
```

## 下载文件

以下代码用于下载OSS文件到本地文件。

```
// yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
String endpoint = "yourEndpoint";
// 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
String accessKeyId = "yourAccessKeyId";
String accessKeySecret = "yourAccessKeySecret";
// 从STS服务获取的安全令牌（SecurityToken）。
String securityToken = "yourSecurityToken";
// yourEndpoint填写Bucket所在地域。以华东1（杭州）为例，region填写为cn-hangzhou。
String region = "yourRegion";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider(accessKeyId, accessKeySecret, securityToken);
ClientConfiguration config = new ClientConfiguration();
config.setSignVersion(SignVersion.V4);
// 创建OSSClient实例。
OSSClient oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);
oss.setRegion(region);
// 构造下载文件请求。
GetObjectRequest get = new GetObjectRequest("", "");

OSSAsyncTask task = oss.asyncGetObject(get, new OSSCompletedCallback() {
    @Override
    public void onSuccess(GetObjectRequest request, GetObjectResult result) {
        // 请求成功。
        Log.d("asyncGetObject", "DownloadSuccess");
        Log.d("Content-Length", "" + result.getContentLength());

        InputStream inputStream = result.getObjectContent();
        byte[] buffer = new byte[2048];
        int len;

        try {
            while ((len = inputStream.read(buffer)) != -1) {
                // 您可以在此处编写代码来处理下载的数据。
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    // GetObject请求成功，返回GetObjectResult。GetObjectResult包含一个输入流的实例。您需要自行处理返回的输入流。
    public void onFailure(GetObjectRequest request, ClientException clientExcepion, ServiceException serviceException) {
        // 请求异常。
        if (clientExcepion != null) {
            // 本地异常，如网络异常等。
            clientExcepion.printStackTrace();
        }
        if (serviceException != null) {
            // 服务异常。
            Log.e("ErrorCode", serviceException.getErrorCode());
            Log.e("RequestId", serviceException.getRequestId());
            Log.e("HostId", serviceException.getHostId());
            Log.e("RawMessage", serviceException.getRawMessage());
        }
    }
});
// 取消任务。
// task.cancel(); 
// 等待任务完成。
// task.waitUntilFinished(); 
```

[上一篇：配置访问凭证（Android SDK）](/zh/oss/developer-reference/android-configure-access-credentials)[下一篇：存储空间（Android SDK）](/zh/oss/developer-reference/buckets-4/)该文章对您有帮助吗？反馈
  
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