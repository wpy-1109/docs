# BrowserjsSDK文件管理FAQ

Source: https://help.aliyun.com/zh/oss/developer-reference/faq

---

- BrowserjsSDK文件管理FAQ-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 常见问题（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文主要介绍Browser.js SDK中的常见问题与解决方法。

## 如何调用STS

浏览器是不受信任的环境，如果把AccessKey ID和AccessKey Secret直接保存在浏览器端，存在极高的风险。建议在浏览器环境下使用[STS](https://help.aliyun.com/zh/ram/user-guide/what-is-sts#concept-ong-5nv-xdb)模式进行OSS接口调用。

获取STS token后，即可进行SDK初始化操作。

```

  $.ajax("http://your_sts_server/",{method: 'GET'},function (err, result) {
    let client = new OSS({
      authorizationV4: true,
      accessKeyId: result.AccessKeyId,
      accessKeySecret: result.AccessKeySecret,
      stsToken: result.SecurityToken,
      region: 'yourRegion',
      bucket: 'yourBucketName'
    });
  });

            
```

## 如何开启HTTPS访问

您可以在初始化SDK时，通过设置`secure:true`的方式开启HTTPS访问。更多信息，请参见[初始化（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/initialization)。

## 浏览器跨域问题如何解决

在浏览器中使用SDK前，需要对Bucket配置跨域规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。

## 如何设置上传文件的用户自定义数据（meta）、文件类型（mime）和请求头（header）

请参见[简单上传（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/simple-upload-8)。

## 关于浏览器端断点续传的说明

将checkpoint保存到浏览器的localstorage，在下次调用时传入checkpoint参数，即可实现断点续传功能。更多信息，请参见[断点续传上传（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/resumable-upload-9)。

## 如何上传文件到指定目录

通过在上传的Object名称前指定前缀的方式实现将文件上传到指定目录。

```
let OSS = require('ali-oss')
let client = new OSS({
  authorizationV4: true,
  region: 'yourRegion',
  accessKeyId: 'yourAccessKeyId',
  accessKeySecret: 'yourAccessKeySecret',
  bucket: 'yourBucketName'
});

client.multipartUpload('base-dir/' +'object-key', 'local-file', {
    progress: async function (p) {
      console.log('Progress: ' + p);
    }
  });
  console.log(result);
}).catch((err) => {
  console.log(err);
});

            
```

## 如何上传base64编码的图片

base64先转码成指定格式图片，然后调用OSS上传接口进行上传。更多信息，请参见[Github示例](https://github.com/ali-sdk/ali-oss/blob/master/example/src/main.js#L109)。

```
/**
 * base64 to file
 * @param dataurl   base64 content
 * @param filename  set up a meaningful suffix, or you can set mime type in options
 * @returns {File|*}
 */
const dataURLtoFile = function dataURLtoFile(dataurl, filename) {
  const arr = dataurl.split(',');
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new Blob([u8arr], { type: mime });// if env support File, also can use this: return new File([u8arr], filename, { type: mime });
};

// client表示OSS client实例
const uploadBase64Img = function uploadBase64Img(client) {
  // base64格式的内容
  const base64Content = 'data:image:****';
  const filename = 'img.png';
  const imgfile = dataURLtoFile(base64Content, filename);
 //key表示上传的object key，imgFile表示dataURLtoFile处理后返回的图片。
  client.multipartUpload(key, imgfile).then((res) => {
    console.log('upload success: %j', res);
  }).catch((err) => {
    console.error(err);
  });
};
```

## 如何限制上传文件的大小

在浏览器中可以根据document.getElementById(“file”).files[0].size获取上传文件的大小（字节数）。更多信息，请参见[Web端直传实践](https://help.aliyun.com/zh/oss/use-postobject-to-upload-objects-by-using-web-clients#concept-iyn-vfy-5db)的post请求。

## 如何获取上传进度

您可以通过分片上传的方式获取上传进度。更多信息，请参见[分片上传（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-11)。

## 如何获取下载进度

浏览器中无法获取进度，可调用`signatureUrl`方法，获取下载地址。更多信息，请参见[相关文档](https://help.aliyun.com/zh/oss/developer-reference/preview-or-download-an-object#concept-64052-zh)。

## 如何获取Object的签名URL

可调用`signatureUrl`方法，获取下载地址。更多信息，请参见[预览或下载文件（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/preview-or-download-an-object)。

## 如何使用SDK生成的签名URL并进行资源上传

签名URL常用于授权给第三方进行资源的下载和上传操作。下载请参见上一条。SDK中提供signatureUrl API，用于返回一个经过签名的URL，用户直接使用该URL上传或者下载资源即可。利用签名URL上传资源请参见SDK工程示例[签名URL上传资源示例](https://github.com/ali-sdk/ali-oss/blob/master/example/src/main.js)。

## 如何使用表单上传方式上传资源到OSS服务器

请参见[Web端直传实践](https://help.aliyun.com/zh/oss/use-postobject-to-upload-objects-by-using-web-clients#concept-iyn-vfy-5db)。

## 如何运行示例工程

进入ali-oss/example执行` npm run start`。

## 如何添加上传回调

```
const uploadFile = function uploadFile(client) {
if (!uploadFileClient || Object.keys(uploadFileClient).length === 0) {
uploadFileClient = client;
}

const file = document.getElementById('file').files[0];
const key = document.getElementById('object-key-file').value.trim() || 'object';

console.log(`${file.name} => ${key}`);
const options = {
progress,
partSize: 500 * 1024,
timeout:60000,
meta: {
year: 2017,
people: 'test',
},
callback: {

// 添加上传回调的位置。
url: 'https://example.aliyundoc.com/v2/sync',
/* host: 'oss-cn-shenzhen.aliyuncs.com', */
/* eslint no-template-curly-in-string: [0] */
body: 'bucket=${bucket}&object=${object}&var1=${x:var1}',
contentType: 'application/x-www-form-urlencoded',
customValue: {
var1: 'value1',
var2: 'value2',
},
},
```

关于上传回调的更多信息，请参见[原理介绍](https://help.aliyun.com/zh/oss/overview-20/#concept-qp2-g4y-5db)。

## 浏览器是否支持以chunck的方法浏览文件？

不支持。

## 如何通过OSS js SDK进行日志收集？

具体操作，请参见[GitHub](https://github.com/luozhang002/oss-js-sdk-log)。

## 常见错误参考
- [SDK开启异常日志](https://help.aliyun.com/zh/oss/developer-reference/error-handling#concept-64055-zh)
- [ OSS常见错误](https://help.aliyun.com/zh/oss/user-guide/overview-14#concept-dt2-hq3-wdb)

[上一篇：异常处理（Browser.js SDK）](/zh/oss/developer-reference/error-handling)[下一篇：OSS Kotlin SDK V2（预览版）](/zh/oss/developer-reference/oss-kotlin-sdk-v2-preview)该文章对您有帮助吗？反馈
  
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