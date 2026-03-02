# SDK授权访问的不同实现方式

Source: https://help.aliyun.com/zh/oss/developer-reference/authorize-access

---

- SDK授权访问的不同实现方式-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 授权访问（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
Android SDK提供了STS鉴权模式、自签名模式以及预签名URL的方式，用于保障移动终端的安全性。

## 背景信息

无论是STS鉴权模式还是自签名模式，您实现的回调函数都需要保证调用时Token、Signature的返回结果。如果您需要实现向业务Server获取Token、Signature的网络请求，建议调用网络库的同步接口。回调都是在SDK发起具体请求时，在请求的子线程中执行，所以不会阻塞主线程。

## STS鉴权模式
说明 
使用STS模式授权需要先开通阿里云访问控制RAM服务。

OSS可以通过阿里云STS（Security Token Service）进行临时授权访问。阿里云STS是为云计算用户提供临时访问令牌的Web服务。通过STS，您可以为第三方应用或子用户（即用户身份由您自己管理的用户）颁发一个自定义时效和权限的访问凭证。关于STS的更多信息，请参见[什么是STS](https://help.aliyun.com/zh/ram/user-guide/what-is-sts#reference-ong-5nv-xdb)。

STS的优势如下：
- 您无需透露您的长期密钥（AccessKey）给第三方应用，只需生成一个访问令牌并将令牌交给第三方应用。您可以自定义这个令牌的访问权限及有效期限。
- 您无需关心权限撤销问题，访问令牌过期后自动失效。

通过STS临时授权访问OSS的步骤如下：
- 获取临时访问凭证临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。临时访问凭证有效时间单位为秒，最小值为900，最大值以当前角色设定的最大会话时间为准。更多信息，请参见[设置RAM角色最大会话时间](https://help.aliyun.com/zh/ram/user-guide/specify-the-maximum-session-duration-for-a-ram-role#task-2498608)。您可以通过以下两种方式获取临时访问凭证。方式一通过调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口获取临时访问凭证。
- 方式二通过[各语言STS SDK](https://help.aliyun.com/zh/ram/developer-reference/sts-sdk-overview#reference-w5t-25v-xdb)获取临时访问凭证。
- 使用临时访问凭证初始化SDK。
```
String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";

OSSCredentialProvider credentialProvider = new OSSStsTokenCredentialProvider("StsToken.AccessKeyId", "StsToken.SecretKeyId", "StsToken.SecurityToken");

OSS oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);                  
```
通过临时访问凭证初始化SDK时，需要注意StsToken的有效时间。以下代码用于在判断StsToken的有效时间小于5分钟时对StsToken进行更新：
```
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
sdf.setTimeZone(TimeZone.getTimeZone("UTC"));
Date date = sdf.parse("");
long expiration = date.getTime() / 1000;
// 如果StsToken即将过期，有效时间小于5分钟，则更新StsToken。
if (DateUtil.getFixedSkewedTimeMillis() / 1000 > expiration - 5 * 60) {
    oss.updateCredentialProvider(new OSSStsTokenCredentialProvider("StsToken.AccessKeyId", "StsToken.SecretKeyId", "StsToken.SecurityToken"));
}
```
手动更新StsToken当判断StsToken即将过期时，您可以重新构造OSSClient，也可以通过如下方式更新CredentialProvider：
```
oss.updateCredentialProvider(new OSSStsTokenCredentialProvider("StsToken.AccessKeyId", "StsToken.SecretKeyId", "StsToken.SecurityToken"));                   
```
- 自动更新StsToken如果您期望SDK自动更新StsToken，那么您需要在SDK的应用中实现回调。通过您实现回调的方式去获取Federation Token（即StsToken），SDK会使用此StsToken来进行加签处理，并在需要更新时主动调用此回调来获取StsToken。
```
String endpoint = "http://oss-cn-hangzhou.aliyuncs.com";

OSSCredentialProvider credentialProvider = new OSSFederationCredentialProvider() {

    @Override
    public OSSFederationToken getFederationToken() {
    // 获取FederationToken，并将其构造为OSSFederationToken对象返回。如果因某种原因FederationToken获取失败，服务器则直接返回null。

        OSSFederationToken token;
        // 从您的服务器中获取Token。
        return token;
    }
};

OSS oss = new OSSClient(getApplicationContext(), endpoint, credentialProvider);                    
```
说明 如果您已经通过其他方式获取了StsToken所需的各个字段，也可以在回调中直接返回StsToken。但您需要手动处理StsToken的更新，且更新后重新设置该OSSClient实例的OSSCredentialProvider。假设您访问的Server地址为http://localhost:8080/distribute-token.json，则返回的数据如下：
```
{
    "StatusCode": 200,
    "AccessKeyId":"STS.iA645eTOXEqP3cg3****",
    "AccessKeySecret":"rV3VQrpFQ4BsyHSAvi5NVLpPIVffDJv4LojU****",
    "Expiration":"2015-11-03T09:52:59Z",
    "SecurityToken":"CAES7QIIARKAAZPlqaN9ILiQZPS+JDkS/GSZN45RLx4YS/p3OgaUC+oJl3XSlbJ7StKpQ****"}                    
```
实现OSSFederationCredentialProvider的示例如下：
```
OSSCredentialProvider credetialProvider = new OSSFederationCredentialProvider() {
    @Override
    public OSSFederationToken getFederationToken() {
        try {
            URL stsUrl = new URL("http://localhost:8080/distribute-token.json");
            HttpURLConnection conn = (HttpURLConnection) stsUrl.openConnection();
            InputStream input = conn.getInputStream();
            String jsonText = IOUtils.readStreamAsString(input, OSSConstants.DEFAULT_CHARSET_NAME);
            JSONObject jsonObjs = new JSONObject(jsonText);
            String ak = jsonObjs.getString("AccessKeyId");
            String sk = jsonObjs.getString("AccessKeySecret");
            String token = jsonObjs.getString("SecurityToken");
            String expiration = jsonObjs.getString("Expiration");
            return new OSSFederationToken(ak, sk, token, expiration);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
};                    
```

## 预签名URL

### 注意事项
- 生成预签名URL过程中，SDK利用本地存储的密钥信息，根据特定算法计算出签名（signature），然后将其附加到URL上，以确保URL的有效性和安全性。这一系列计算和构造URL的操作都是在客户端完成，不涉及网络请求到服务端。因此，生成预签名URL时不需要授予调用者特定权限。但是，为避免第三方用户无法对预签名URL授权的资源执行相关操作，需要确保调用生成预签名URL接口的身份主体被授予对应的权限。例如，通过预签名URL上传文件时，需要授予oss:PutObject权限。通过预签名URL下载或预览文件时，需要授予oss:GetObject权限。
- 通过以下示例生成的预签名URL中如果包含特殊符号`+`，可能出现无法正常访问该预签名URL的现象。如需正常访问该预签名URL，请将预签名URL中的`+`替换为`%2B`。

以下是使用预签名URL临时授权的常见示例。

### 生成预签名URL并通过预签名URL上传文件
- 生成用于上传的预签名URL。
```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写不包含Bucket名称在内源Object的完整路径，例如exampleobject.txt。
String objectKey = "exampleobject.txt";
// 设置content-type。
String contentType = "application/octet-stream";
String url = null;
try {
    // 生成用于上传文件的预签名URL。
    GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(bucketName, objectKey);
    // 设置预签名URL的过期时间为30分钟。
    request.setExpiration(30*60);
    request.setContentType(contentType);    
    request.setMethod(HttpMethod.PUT);
    url = oss.presignConstrainedObjectURL(request);
    Log.d("url", url);
} catch (ClientException e) {
    e.printStackTrace();
}
```
- 通过预签名URL上传文件。
```
// 填写生成的预签名URL。
String url = "";
// 指定本地文件的完整路径。
String localFile = "/storage/emulated/0/oss/examplefile";
// 设置content-type。
String contentType = "application/octet-stream";
// 通过预签名URL上传文件。
OkHttpClient client = new OkHttpClient();
Request putRequest = new Request.Builder()
        .url(url)
        .put(RequestBody.create(MediaType.parse(contentType), new File(localFile)))
        .build();
client.newCall(putRequest).enqueue(new Callback() {
    @Override
    public void onFailure(Call call, IOException e) {
        e.printStackTrace();
    }

    @Override
    public void onResponse(Call call, Response response) throws IOException {
        Log.d("response", response.body().string());
    }
});
```

### 生成预签名URL并通过预签名URL下载文件
- 生成用于下载的预签名URL。
```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写不包含Bucket名称在内源Object的完整路径，例如exampleobject.txt。
String objectKey = "exampleobject.txt";
String url = null;
try {
    // 生成用于下载文件的预签名URL。
    GeneratePresignedUrlRequest request = new GeneratePresignedUrlRequest(bucketName, objectKey);
    // 设置预签名URL的过期时间为30分钟。
    request.setExpiration(30*60);
    request.setMethod(HttpMethod.GET);
    url = oss.presignConstrainedObjectURL(request);
    Log.d("url", url);
} catch (ClientException e) {
    e.printStackTrace();
}
```
- 通过预签名URL下载文件。
```
// 填写生成的预签名URL。
String url = "";
OkHttpClient client = new OkHttpClient();
// 通过预签名URL下载文件。
Request getRequest = new Request.Builder()
        .url(url)
        .get()
        .build();
client.newCall(getRequest).enqueue(new Callback() {
    @Override
    public void onFailure(Call call, IOException e) {
        e.printStackTrace();
    }

    @Override
    public void onResponse(Call call, Response response) throws IOException {
        if (response.code() == 203 || response.code() >= 300) {
            Log.d("download", "fail");
            Log.d("download", response.body().string());
            return;
        }
        // 请求成功。
        InputStream inputStream = response.body().byteStream();

        byte[] buffer = new byte[2048];
        int len;

        while ((len = inputStream.read(buffer)) != -1) {
            // 处理下载的数据，例如图片展示或者写入文件等。
        }
    }
});
```

[上一篇：图片处理（Android SDK）](/zh/oss/developer-reference/img-1)[下一篇：异常处理（Android SDK）](/zh/oss/developer-reference/exception-handling-3)该文章对您有帮助吗？反馈
  
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