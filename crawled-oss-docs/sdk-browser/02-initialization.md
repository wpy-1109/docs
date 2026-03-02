# 使用Browser.js SDK初始化和配置Client

Source: https://help.aliyun.com/zh/oss/developer-reference/initialization

---

- 使用Browser.js SDK初始化和配置Client-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 初始化（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
Client是OSS Browser.js的客户端，用于管理存储空间和文件等OSS资源。使用Browser.js SDK发起OSS请求时，您需要初始化一个Client实例，并根据需要修改默认配置项。

## 前提条件

已安装Browser.js SDK。具体操作，请参见[安装（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/installation)。

## 新建Client

### V4签名（推荐）

推荐使用更安全的V4签名算法。使用V4签名初始化时，需要声明authorizationV4。OSS Browser.js SDK 6.20.0及以上版本支持V4签名。

以使用OSS域名初始化时使用V4签名为例，其他通过自定义域名等初始化的场景可参考以下示例执行相应修改。

```

  
    
    Document
  
  
    
    
    
      const client = new OSS({
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，yourRegion填写为oss-cn-hangzhou。
        region: 'yourRegion',
	authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
      });
    
  

```

### V1签名（不推荐）
重要 
阿里云对象存储OSS自2025年03月01日起不再对新用户（即新UID ）开放使用V1签名，并将于2025年09月01日起停止更新与维护且不再对新增Bucket开放使用V1签名。请尽快切换到V4签名，避免影响服务。更多信息，请参见[公告说明](https://www.aliyun.com/notice/detail/116888)。

```

  
    
    Document
  
  
    
    
    
      const client = new OSS({
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，yourRegion填写为oss-cn-hangzhou。
        region: 'yourRegion',
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
      });
    
  

```

## 配置Client

您可以在初始化Client时按需添加配置项，例如通过`timeout`指定请求超时时间，通过`stsToken`指定临时访问凭证等。关于Browser.js支持的配置项以及配置示例，具体参数请参考下方说明。

### options参数说明：
- accessKeyId {String}：在阿里云控制台网站上创建的访问密钥。
- accessKeySecret {String}：在阿里云控制台创建的访问密钥秘密。
- [stsToken] {String}：用于临时授权。
- [refreshSTSToken] {Function}：当STS信息过期时自动设置stsToken、accessKeyId、accessKeySecret的函数。返回值必须是包含stsToken、accessKeyId、accessKeySecret的对象。
- [refreshSTSTokenInterval] {number}：STS令牌刷新间隔时间（毫秒）。应小于STS信息的过期间隔，默认为300000毫秒（5分钟）。
- [bucket] {String}：您想访问的默认Bucket。如果没有Bucket，请先使用putBucket()创建一个。
- [endpoint] {String}：OSS区域域名。优先级高于region。根据需要设置为外网域名、内网域名或加速域名等，请参考终端节点列表。
- [region] {String}：Bucket数据所在的区域位置，默认为oss-cn-hangzhou。
- [internal] {Boolean}：是否通过阿里云内网访问OSS，默认为false。如果您的服务器也在阿里云上运行，可以设置为true以节省大量费用。
- [secure] {Boolean}：指示OSS客户端使用HTTPS（secure: true）还是HTTP（secure: false）协议。
- [timeout] {String|Number}：针对所有操作的实例级别超时时间，默认为60秒。
- [cname] {Boolean}：默认为false，使用自定义域名访问OSS。如果为true，则可以在endpoint字段中填写自定义域名。
- [isRequestPay] {Boolean}：默认为false，表示是否开启Bucket的请求者支付功能，如果为true，会向OSS服务器发送头部'x-oss-request-payer': 'requester'。
- [useFetch] {Boolean}：默认为false，仅在浏览器环境中生效。如果为true，意味着使用fetch模式上传对象，否则使用XMLHttpRequest。
- [retryMax] {Number}：当请求因网络错误或超时出错时自动重试发送请求的最大次数。使用putStream时不支持重试。
- [authorizationV4] {Boolean}：使用V4签名。默认为false。

### 示例
- 基本用法
```
const OSS = require('ali-oss');

const store = new OSS({
  region: 'yourRegion',
  authorizationV4: true,
  accessKeyId: 'your access key',
  accessKeySecret: 'your access secret',
  stsToken: 'yourSecurityToken',
  bucket: 'your bucket name',
});
```
- 使用加速访问endpoint说明 全球加速访问endpoint：oss-accelerate.aliyuncs.com中国内地以外区域的加速访问endpoint：oss-accelerate-overseas.aliyuncs.com
```
const OSS = require('ali-oss');

const store = new OSS({
  region: 'yourRegion',
  authorizationV4: true,
  accessKeyId: 'your access key',
  accessKeySecret: 'your access secret',
  stsToken: 'yourSecurityToken',
  bucket: 'your bucket name',
  endpoint: 'oss-accelerate.aliyuncs.com',
});
```
- 使用自定义访问方式
```
const OSS = require('ali-oss');

const store = new OSS({
  region: 'yourRegion',
  authorizationV4: true,
  stsToken: 'yourSecurityToken',
  accessKeyId: 'your access key',
  accessKeySecret: 'your access secret',
  cname: true,
  endpoint: 'your custome domain',
});
```
- 使用STS Token访问
```
const OSS = require('ali-oss');

const store = new OSS({
  region: 'yourRegion',
  authorizationV4: true,
  accessKeyId: 'your STS key',
  accessKeySecret: 'your STS secret',
  stsToken: 'your STS token',
  refreshSTSToken: async () => {
    const info = await fetch('you sts server');
    return {
      accessKeyId: info.accessKeyId,
      accessKeySecret: info.accessKeySecret,
      stsToken: info.stsToken,
    };
  },
  refreshSTSTokenInterval: 300000,
});
```
- 使用流重新尝试请求
```
for (let i = 0; i ', fs.createReadStream(''));
    console.log(result);
    break; // break if success
  } catch (e) {
    console.log(e);
  }
}
```
- 使用V4签名，并使用可选的additionalHeaders选项（类型为字符串数组），其中的值需要包含在标头中
```
const OSS = require('ali-oss');

const store = new OSS({
  accessKeyId: 'your access key',
  accessKeySecret: 'your access secret',
  bucket: 'your bucket name',
  region: 'oss-cn-hangzhou',
  authorizationV4: true ,
  stsToken: 'yourSecurityToken',
});

try {
  const bucketInfo = await store.getBucketInfo('your bucket name');
  console.log(bucketInfo);
} catch (e) {
  console.log(e);
}

try {
  const putObjectResult = await store.put('your bucket name', 'your object name', {
    headers: {
      // The headers of this request
      header1: 'value1',
      header2: 'value2',
    },
    // The keys of the request headers that need to be calculated into the V4 signature. Please ensure that these additional headers are included in the request headers.
    additionalHeaders: ['additional header1', 'additional header2'],
  });
  console.log(putObjectResult);
} catch (e) {
  console.log(e);
}
```

[上一篇：安装（Browser.js SDK）](/zh/oss/developer-reference/installation)[下一篇：授权访问（Browser.js SDK）](/zh/oss/developer-reference/authorize-access-6)该文章对您有帮助吗？反馈
  
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