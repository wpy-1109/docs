# 安装和使用Browser.js SDK

Source: https://help.aliyun.com/zh/oss/developer-reference/installation

---

- 安装和使用Browser.js SDK-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 安装（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
如果您需要管理OSS存储空间、上传下载文件、管理数据、进行图片处理等，可以先安装OSS Browser.js SDK。本文为您介绍如何安装和使用OSS Browser.js SDK。

## 准备工作
- 使用RAM用户或STS方式访问由于阿里云账号AccessKey拥有所有API访问权限，建议遵循阿里云安全最佳实践。如果部署在服务端，可以使用RAM用户或STS来进行API访问或日常运维管控操作，如果部署在客户端，请使用STS方式来进行API访问。更多信息，请参见[访问控制](https://help.aliyun.com/zh/oss/user-guide/permissions-and-access-control-overview#concept-e4s-mhv-tdb)。
- 设置跨域资源共享（CORS）通过浏览器直接访问OSS时，CORS配置规则要求如下：来源：设置精准域名（例如`https://www.aliyun.com`）或带有通配符星号（*）的域名（例如`https://*.aliyun.com`）。
- 允许Methods：请根据实际使用场景，选择不同的Methods。例如分片上传时，设置为PUT；删除文件时，设置为DELETE。
- 允许Headers：设置为`*`。
- 暴露Headers：请根据实际使用场景，设置暴露的Headers。例如设置为`ETag`、`x-oss-request-id`和`x-oss-version-id`。

具体操作，请参见[跨域设置](https://help.aliyun.com/zh/oss/user-guide/cors-settings)。

## 注意事项

OSS Browser.js SDK通过[Browserify](http://browserify.org/)和[Babel](https://babeljs.io/)产生适用于浏览器的代码。由于浏览器环境的特殊性，无法使用以下功能：
- 流式上传：浏览器中无法设置chunked编码，建议使用分片上传替代。
- 操作本地文件：浏览器中不能直接操作本地文件系统，建议使用签名URL的方式下载文件。
- 由于OSS暂时不支持Bucket相关的跨域请求，建议在控制台执行Bucket相关操作。

## 下载SDK

目前官网文档中的demo都是基于SDK 6.x，版本低于6.x的可参考[5.x开发文档](https://github.com/ali-sdk/ali-oss/blob/5.x/README.md)，如果要升级到6.x请参考[升级文档](https://github.com/ali-sdk/ali-oss/blob/master/UPGRADING.md)。
- [Github地址](https://github.com/ali-sdk/ali-oss)
- [API使用说明](https://github.com/ali-sdk/ali-oss#summary)
- [ChangeLog](https://github.com/ali-sdk/ali-oss/blob/master/CHANGELOG.md)

## 安装SDK
- 支持的浏览器IE（>=10）
- Edge
- 主流版本的Chrome、Firefox、Safari
- 主流版本的Android、iOS、Windows Phone系统默认浏览器
- 安装方式您可以通过以下任意方式安装Browser.js SDK。
### 浏览器引入
重要 因部分浏览器不支持promise，需要引入promise兼容库。 例如IE10和IE11需要引入promise-polyfill。
```

      

```
说明 引入在线资源方式依赖于CDN服务器的稳定性，推荐用户使用离线方式引入，即通过本地资源或自行构建的方式引入。
- 使用引入本地资源方式时，src请填写本地资源相对于示例程序的相对路径。
- 本文以6.20.0版本为例。更多版本，请参见[ali-oss](https://github.com/ali-sdk/ali-oss/releases)。

在代码中使用OSS对象：
重要 
由于Browser.js SDK通常在浏览器环境下使用，为避免暴露阿里云账号访问密钥（AccessKey ID和AccessKey Secret），强烈建议您使用临时访问凭证的方式执行OSS相关操作。

临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。您可以通过调用STS服务的[AssumeRole](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)接口或者使用[各语言STS SDK](https://help.aliyun.com/zh/ram/developer-reference/sts-sdk-overview#reference-w5t-25v-xdb)来获取临时访问凭证。关于搭建STS服务的具体操作，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#concept-xzh-nzk-2gb)。

```

  const client = new OSS({
    // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
    region: 'yourRegion',
    // 开启V4版本签名。
    authorizationV4: true,
    // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
    accessKeyId: 'yourAccessKeyId',
    accessKeySecret: 'yourAccessKeySecret',
    // 从STS服务获取的安全令牌（SecurityToken）。
    stsToken: 'yourSecurityToken',
    refreshSTSToken: async () => {
    // 向您搭建的STS服务获取临时访问凭证。
      const info = await fetch('your_sts_server');
      return {
        accessKeyId: info.accessKeyId,
        accessKeySecret: info.accessKeySecret,
        stsToken: info.stsToken
      }
    },
    // 刷新临时访问凭证的时间间隔，单位为毫秒。
    refreshSTSTokenInterval: 300000,
    // 填写Bucket名称。
    bucket: 'examplebucket'
  });
                           
```

### 使用npm安装SDK开发包

```
npm install ali-oss
```

成功完成后，即可使用import或require进行引用。由于浏览器中原生不支持`require`模式，因此需要在开发环境中配合相关的打包工具，例如`webpack`、`browserify`等。

```
const OSS = require('ali-oss');

const client = new OSS({
    // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
    region: 'yourRegion',
    // 开启V4版本签名。
    authorizationV4: true,
    // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
    accessKeyId: 'yourAccessKeyId',
    accessKeySecret: 'yourAccessKeySecret',
    // 从STS服务获取的安全令牌（SecurityToken）。
    stsToken: 'yourSecurityToken',
    refreshSTSToken: async () => {
    // 向您搭建的STS服务获取临时访问凭证。
      const info = await fetch('your_sts_server');
      return {
        accessKeyId: info.accessKeyId,
        accessKeySecret: info.accessKeySecret,
        stsToken: info.stsToken
      }
    },
    // 刷新临时访问凭证的时间间隔，单位为毫秒。
    refreshSTSTokenInterval: 300000,
    // 填写Bucket名称。
    bucket: 'examplebucket'
});
```

## 使用方式

OSS Browser.js SDK支持同步和异步的使用方式。同步和异步方式均使用`new OSS()`创建client。

### 同步方式

基于ES7规范的`async/await`，使得异步方式同步化。

以下以同步方式上传文件为例。

```
// 实例化OSS Client。
const client = new OSS(...);

async function put () {
  try {
    // object表示上传到OSS的文件名称。
    // file表示浏览器中需要上传的文件，支持HTML5 file和Blob类型。
    const r1 = await client.put('object', file);
    console.log('put success: %j', r1);
    const r2 = await client.get('object');
    console.log('get success: %j', r2);
  } catch (e) {
    console.error('error: %j', e);
  }
}

put();                    
```

### 异步方式

与Callback方式类似，API接口返回[Promise](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Promise)，使用`then()`处理返回结果，使用`catch()`处理错误。

以下以异步方式下载文件为例。

```
// 实例化OSS Client。
const client = new OSS(...);

// object表示上传到OSS的文件名称。
// file表示浏览器中需要上传的文件，支持HTML5 file和Blob类型。
client.put('object', file).then(function (r1) {
  console.log('put success: %j', r1);
  return client.get('object');
}).then(function (r2) {
  console.log('get success: %j', r2);
}).catch(function (err) {
  console.error('error: %j', err);
});                    
```

[上一篇：OSS Browser.js SDK](/zh/oss/developer-reference/browser-js/)[下一篇：初始化（Browser.js SDK）](/zh/oss/developer-reference/initialization)该文章对您有帮助吗？反馈
  
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