# NodeJS SDK列举对象的所有版本

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects-8

---

- NodeJS SDK列举对象的所有版本-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 列举文件（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何在开启版本控制状态下列举存储空间下（Bucket）的所有文件（Object）、指定个数的文件、指定前缀的文件等。

## 列举Bucket中所有Object的信息

以下代码用于列举指定Bucket中包括删除标记（Delete Marker）在内的所有Object的版本信息：

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: 'yourbucketname'
});

// 列举包括删除标记在内的所有Object的版本信息。
async function getObjectVersions() {
  let nextKeyMarker = null;
  let nextVersionMarker = null;
  let versionListing = null;
  do {
    versionListing = await client.getBucketVersions({
      keyMarker: nextKeyMarker,
      versionIdMarker: nextVersionMarker,
    });

    versionListing.objects.forEach((o) => {
      console.log(`${o.name}, ${o.versionId}`);
    });
    versionListing.deleteMarker.forEach((o) => {
      console.log(`${o.name}, ${o.versionId}`);
    });

    nextKeyMarker = versionListing.NextKeyMarker;
    nextVersionMarker = versionListing.NextVersionIdMarker;
  } while (versionListing.isTruncated);
}

getObjectVersions();
```

## 列举指定前缀Object的版本信息

以下代码用于列举指定前缀Object的版本信息：

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: 'yourbucketname'
});

// 指定列举以"test-"为前缀的Object的版本信息。
async function getObjectVersionsByPrefix() {
  let nextKeyMarker = null;
  let nextVersionMarker = null;
  let versionListing = null;
  const prefix = 'test-'
  do {
    versionListing = await client.getBucketVersions({
      keyMarker: nextKeyMarker,
      versionIdMarker: nextVersionMarker,
      prefix
    })
    versionListing.objects.forEach(o => {
      console.log(`${o.name}, ${o.versionId}`)
    })
    versionListing.deleteMarker.forEach(o => {
      console.log(`${o.name}, ${o.versionId}`)
    })
    nextKeyMarker = versionListing.NextKeyMarker;
    nextVersionMarker = versionListing.NextVersionIdMarker;
  } while (versionListing.isTruncated);
}

getObjectVersionsByPrefix();
```

## 列举指定个数Object的版本信息

以下代码用于列举指定个数Object的版本信息：

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: 'yourbucketname'
});

async function getObjectVersionByNumber() {
  // 指定最多列举100个Object的版本信息。
  const versionListing = await client.getBucketVersions({
    "max-keys": 100,
  });
  // 获取Object的版本信息。在未开启版本控制的情况下，VersionId为none。
  versionListing.objects.forEach((o) => {
    console.log(`${o.name}, ${o.versionId}`);
  });
  versionListing.deleteMarker.forEach((o) => {
    console.log(`${o.name}, ${o.versionId}`);
  });
}

getObjectVersionByNumber();
```

## 文件夹功能

OSS没有文件夹的概念，所有元素都是以文件来存储。创建文件夹本质上来说是创建了一个大小为0并以正斜线（/）结尾的文件。这个文件可以被上传和下载，控制台会对以正斜线（/）结尾的文件以文件夹的方式展示。

通过delimiter和prefix两个参数可以模拟文件夹功能：
- 如果设置prefix为某个文件夹名称，则会列举以此prefix开头的文件，即该文件夹下所有的文件和子文件夹（目录）均显示为Object。
- 如果在设置了prefix的情况下，将delimiter设置为正斜线（/），则只列举该文件夹下的文件和子文件夹（目录），该文件夹下的子文件夹（目录）显示为CommonPrefixes，子文件夹下的文件和文件夹不显示。

假设存储空间中包含oss.jpg、fun/test.jpg、fun/movie/001.avi和fun/movie/007.avi4个文件，正斜线（/）作为文件夹的分隔符。以下示例说明了如何通过模拟文件夹的方式列举文件。

### 列举根目录下的Object的版本信息

以下代码用于列举根目录下的Object的版本信息：

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: 'yourbucketname'
});

// 指定delimiter参数为正斜线（/），将会列举根目录下的Object的版本信息以及文件夹名称。
async function getRootObjectVersions() {
  let nextKeyMarker = null;
  let nextVersionMarker = null;
  let versionListing = null;
  do {
    versionListing = await client.getBucketVersions({
      keyMarker: nextKeyMarker,
      versionIdMarker: nextVersionMarker,
      delimiter: "/",
    });
    nextKeyMarker = versionListing.NextKeyMarker;
    nextVersionMarker = versionListing.NextVersionIdMarker;
    console.log(versionListing);
  } while (versionListing.isTruncated);
}

getRootObjectVersions();
```

### 列举目录下的文件和子目录

以下代码用于列举指定目录下的文件和子目录：

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: 'yourbucketname'
});

// 设置prefix参数来获取fun目录下的所有文件与文件夹，同时设置delimiter参数为正斜线（/）作为文件夹的分隔符。
async function getObjectVersionsByPrefixAndDirectory() {
  let nextKeyMarker = null;
  let nextVersionMarker = null;
  let versionListing = null;
  let prefix = "foo/";
  do {
    versionListing = await client.getBucketVersions({
      keyMarker: nextKeyMarker,
      versionIdMarker: nextVersionMarker,
      prefix,
      delimiter: "/",
    });
    nextKeyMarker = versionListing.NextKeyMarker;
    nextVersionMarker = versionListing.NextVersionIdMarker;
    console.log(versionListing);
  } while (versionListing.isTruncated);
}

getObjectVersionsByPrefixAndDirectory();
```

## 相关文档

关于列举文件的API接口说明，请参见[ListObjectVersions（GetBucketVersions）](https://help.aliyun.com/zh/oss/developer-reference/listobjectversions#reference-n2s-xy3-fhb)。

[上一篇：拷贝文件（Node.js SDK）](/zh/oss/developer-reference/copy-objects-13)[下一篇：删除文件（Node.js SDK）](/zh/oss/developer-reference/delete-objects-15)该文章对您有帮助吗？反馈
  
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