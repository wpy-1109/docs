# 使用Ruby SDK通过STS和预签名URL实现OSS临时授权

Source: https://help.aliyun.com/zh/oss/developer-reference/authorized-access-2

---

- 使用Ruby SDK通过STS和预签名URL实现OSS临时授权-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 授权访问（Ruby SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何使用STS以及预签名URL临时授权访问OSS资源。

## 注意事项
- 由于STS临时账号以及预签名URL均需设置有效时长，当您使用STS临时账号生成预签名URL执行相关操作（例如上传、下载文件）时，以最小的有效时长为准。例如您的STS临时账号的有效时长设置为1200秒、预签名URL设置为3600秒时，当有效时长超过1200秒后，您无法使用此STS临时账号生成的预签名URL上传文件。
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建Client为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[初始化Client](https://help.aliyun.com/zh/oss/developer-reference/initialization-11#section-6ua-blr-7xk)。

## 使用STS进行临时授权

OSS可以通过阿里云STS（Security Token Service）进行临时授权访问。阿里云STS是为云计算用户提供临时访问令牌的Web服务。通过STS，您可以为第三方应用或子用户（即用户身份由您自己管理的用户）颁发一个自定义时效和权限的访问凭证。关于STS的更多信息，请参见[什么是STS](https://help.aliyun.com/zh/ram/user-guide/what-is-sts#reference-ong-5nv-xdb)。

STS的优势如下：
- 您无需透露您的长期密钥（AccessKey）给第三方应用，只需生成一个访问令牌并将令牌交给第三方应用。您可以自定义这个令牌的访问权限及有效期限。
- 您无需关心权限撤销问题，访问令牌过期后自动失效。

通过STS临时授权访问OSS的步骤如下：
- 获取临时访问凭证临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。临时访问凭证有效时间单位为秒，最小值为900，最大值以当前角色设定的最大会话时间为准。更多信息，请参见[设置RAM角色最大会话时间](https://help.aliyun.com/zh/ram/user-guide/specify-the-maximum-session-duration-for-a-ram-role#task-2498608)。您可以通过以下两种方式获取临时访问凭证。方式一通过调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/api-assumerole#reference-clc-3sv-xdb)接口获取临时访问凭证。
- 方式二通过[STS SDK概览](https://help.aliyun.com/zh/ram/developer-reference/sts-sdk-overview#reference-w5t-25v-xdb)获取临时访问凭证。
- 使用STS临时访问凭证上传文件。

```
require 'aliyun/sts'
require 'aliyun/oss'

sts = Aliyun::STS::Client.new(  。
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)
# 依次填写角色ARN并自定义角色会话名称。
token = sts.assume_role('role-arn', 'session-name')

client = Aliyun::OSS::Client.new(
  # Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
  access_key_id: 'token.access_key_id',
  access_key_secret: 'token.access_key_secret',
  # 从STS服务获取的安全令牌（SecurityToken）。
  sts_token: 'token.security_token')

# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')
# 上传文件。
bucket.put_object('exampleobject.txt', :file => 'D:\\localpath\\examplefile.txt')
```

## 使用预签名URL进行临时授权

### 注意事项
- 生成预签名URL过程中，SDK利用本地存储的密钥信息，根据特定算法计算出签名（signature），然后将其附加到URL上，以确保URL的有效性和安全性。这一系列计算和构造URL的操作都是在客户端完成，不涉及网络请求到服务端。因此，生成预签名URL时不需要授予调用者特定权限。但是，为避免第三方用户无法对预签名URL授权的资源执行相关操作，需要确保调用生成预签名URL接口的身份主体被授予对应的权限。例如，通过预签名URL下载或预览文件时，需要授予oss:GetObject权限。
- 您可以将生成的预签名URL提供给访客进行临时访问。生成预签名URL时，您可以自定义URL的过期时间来限制访客的访问时长。
- 如果需要生成HTTPS协议的预签名URL，请将Endpoint中的通信协议设置为HTTPS。
- 通过以下示例生成的预签名URL中如果包含特殊符号`+`，可能出现无法正常访问该预签名URL的现象。如需正常访问该预签名URL，请将预签名URL中的`+`替换为`%2B`。

### 生成预签名URL并通过预签名URL下载文件
- 生成用于下载的预签名URL。
```
require 'aliyun/oss'

client = Aliyun::OSS::Client.new(
  # Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)
# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')

# 生成预签名URL，并指定URL有效时间为1小时（3600秒）。
puts bucket.object_url('my-object', true, 3600)
```
- 在移动端或者浏览器端通过签名URL下载文件。Android-Java
```
// 填写生成的签名URL。
String url = "";
OkHttpClient client = new OkHttpClient();
// 通过签名URL下载文件。
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
Object C
```
// 使用签名URL下载文件。
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
JavaScript
```
// 通过HTML中标签的download属性、Web API中的window.open等方式使用获取的文件URL。
```

## 相关文档
- 关于使用STS进行临时授权详细用法和参数说明，请参见[API文档](https://www.rubydoc.info/gems/aliyun-sdk/)。
- 关于在URL中加入签名信息，然后将预签名URL转给第三方实现授权访问的更多信息，请参见[签名版本1](https://help.aliyun.com/zh/oss/developer-reference/ddd-signatures-to-urls#concept-xqh-2df-xdb)。

[上一篇：删除文件（Ruby SDK）](/zh/oss/developer-reference/delete-objects)[下一篇：异常处理（Ruby SDK）](/zh/oss/developer-reference/handle-exceptions-4)该文章对您有帮助吗？反馈
  
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