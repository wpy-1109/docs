# 使用Node.jsSDK在上传时添加与管理对象标签

Source: https://help.aliyun.com/zh/oss/developer-reference/configure-object-tagging-6

---

- 使用Node.jsSDK在上传时添加与管理对象标签-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 设置对象标签（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS支持使用对象标签（Object Tagging）对存储空间（Bucket）中的文件（Object）进行分类，您可以针对相同标签的Object设置生命周期规则、访问权限等。

## 注意事项
- 在配置对象标签之前，请确保您已了解该功能。详情请参见[对象标签](https://help.aliyun.com/zh/oss/user-guide/object-tagging-8)。
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以从环境变量读取访问凭证为例。如何配置访问凭证，请参见[Java配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/oss-java-configure-access-credentials#main-2350752)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[常见场景配置示例](https://help.aliyun.com/zh/oss/developer-reference/initialization-3#section-ngr-tjb-kfb)。
- 仅Java SDK 3.5.0及以上版本支持设置对象标签。
- 要设置对象标签，您必须具有`oss:PutObjectTagging`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 上传Object时添加对象标签
- 简单上传时添加对象标签以下代码用于简单上传时（即通过PutObject方法）添加对象标签。
```
const OSS = require('ali-oss')

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

// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const objectName = 'exampledir/exampleobject.txt'
// 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。
// 如果未指定本地路径只填写了本地文件名称（例如examplefile.txt），则默认从示例程序所属项目对应本地路径中上传文件。
const localFilepath = 'D:\\localpath\\examplefile.txt'

// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document', 
}

client.put(objectName, localFilepath, {
  headers
})
```
- 分片上传时添加对象标签 以下代码用于分片上传时（即通过multipartUpload方法）添加对象标签。 
```
const OSS = require('ali-oss')

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

// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const objectName = 'exampledir/exampleobject.txt'
// 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。
// 如果未指定本地路径只填写了本地文件名称（例如examplefile.txt），则默认从示例程序所属项目对应本地路径中上传文件。
const localFilepath = 'D:\\localpath\\examplefile.txt'

// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document', 
}

async function setTag() {
  await client.multipartUpload(objectName, localFilepath, {
    // 设置分片大小，单位为字节。除了最后一个分片没有大小限制，其他的分片最小为100 KB。
    partSize: 100 * 1024,
    headers
  });
  const tag = await client.getObjectTagging(objectName);
  console.log(tag);
}

setTag()
```
- 追加上传时添加对象标签 以下代码用于追加上传时（即通过AppendObject方法）添加对象标签。 
```
const OSS = require('ali-oss')

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

// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const objectName = 'exampledir/exampleobject.txt'
// 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。
// 如果未指定本地路径只填写了本地文件名称（例如examplefile.txt），则默认从示例程序所属项目对应本地路径中上传文件。
const localFilepath = 'D:\\localpath\\examplefile.txt'

// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document',
}

// 追加上传文件，append接口指定header时，将会为文件设置标签。
// 只有第一次调用append接口设置的标签才会生效，后续再次调用append接口设置的标签不生效。
async function setTag() {
  await client.append(objectName, localFilepath, {
    // 设置分片大小，单位为字节。除了最后一个分片没有大小限制，其他的分片最小为100 KB。
    partSize: 100 * 1024,
    headers
  });
  const tag = await client.getObjectTagging(objectName);
  console.log(tag);
}

setTag()
```
- 断点续传上传时添加对象标签 以下代码用于断点续传上传时（即通过multipartUpload方法）添加对象标签。 
```
const OSS = require('ali-oss')

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

// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const objectName = 'exampledir/exampleobject.txt'
// 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。
// 如果未指定本地路径只填写了本地文件名称（例如examplefile.txt），则默认从示例程序所属项目对应本地路径中上传文件。
const localFilepath = 'D:\\localpath\\examplefile.txt'
// 设置断点信息。
letcheckpoint;

// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document',
}

async function setTag() {
  await client.multipartUpload(objectName, localFilepath, {
    checkponit,
    async progress(percentage, cpt) {
      checkpoint = cpt;
    },
    headers
  });
  const tag = await client.getObjectTagging(objectName);
  console.log(tag);
}

setTag()
```

## 为已上传Object添加或更改对象标签

如果上传Object时未添加对象标签或者添加的对象标签不满足使用需求，您可以在上传Object后为Object添加或更改对象标签。

以下代码用于为已上传Object添加或更改对象标签。

```
const OSS = require('ali-oss')

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

// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const objectName = 'exampledir/exampleobject.txt'
// 依次填写对象标签的键（例如owner）和值（例如John）。
const tag = { owner: 'John', type: 'document' };

async function putObjectTagging(objectName, tag) {
  try {
    const result = await client.putObjectTagging(objectName, tag);
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

putObjectTagging(objectName, tag)
```

## 为Object指定版本添加或更改对象标签

在已开启版本控制的Bucket中，通过指定Object的版本ID（versionId），您可以为Object指定版本添加或更改对象标签。

以下代码用于为Object指定版本添加或更改对象标签。
说明 
关于获取versionId的具体操作，请参见[列举文件（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/list-objects-8#concept-2000179)。

```
const OSS = require('ali-oss')

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

// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const objectName = 'exampledir/exampleobject.txt'
// 依次填写对象标签的键（例如owner）和值（例如John）。
const tag = { owner: 'John', type: 'document' };
// 填写Object的版本ID。
constversionId='CAEQIRiBgMDqvPqA3BciIDJhMjE4MWZkN2ViYTRmYzJhZjkxMzk2YWM2NjJk****'

async function putObjectTagging(objectName, tag) {
  try {
    const options = {
      versionId
    };
    const result = await client.putObjectTagging(objectName, tag, options);
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

putObjectTagging(objectName, tag)
```

## 拷贝Object时设置对象标签

拷贝Object时，可以指定如何设置目标Object的对象标签。取值如下：
- Copy（默认值）：复制源Object的对象标签到目标Object。
- Replace：忽略源Object的对象标签，直接采用请求中指定的对象标签。

以下分别提供了简单拷贝1 GB以下的Object及分片拷贝1 GB以上的Object时设置对象标签的详细示例。
- 简单拷贝时添加对象标签以下代码用于简单拷贝1 GB以下的Object时设置对象标签。
```
const OSS = require('ali-oss')

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

// 填写源Object完整路径，Object完整路径中不能包含Bucket名称。例如srcexampledir/exampleobject.txt。
const sourceObjectName = 'srcexampledir/exampleobject.txt';
// 填写目标Object完整路径，Object完整路径中不能包含Bucket名称。例如destexampledir/exampleobject.txt。
const targetObjectName = 'destexampledir/exampleobject.txt';

// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document',
  // 指定如何设置目标Object的对象标签。可选值包括Copy和Replace。默认值为Copy，Copy表示复制源Object的对象标签到目标Object。Replace表示忽略源Object的对象标签，直接采用请求中指定的对象标签。
  'x-oss-tagging-directive': 'Replace' 
}

async function setTag() {
  const result = await client.copy(targetObjectName, sourceObjectName, {
    headers
  });
  const tag = await client.getObjectTagging(targetObjectName)
  console.log(tag)
}

setTag()
```
- 分片拷贝时添加对象标签以下代码用于分片拷贝1 GB以上的Object时设置对象标签。
```
const OSS = require('ali-oss')

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

// 填写源Object完整路径，Object完整路径中不能包含Bucket名称。例如srcexampledir/exampleobject.txt。
const sourceObjectName = 'srcexampledir/exampleobject.txt'
// 填写目标Object完整路径，Object完整路径中不能包含Bucket名称。例如destexampledir/exampleobject.txt。
const targetObjectName = 'destexampledir/exampleobject.txt'

// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document',
}

async function setTag() {
  await client.multipartUploadCopy(targetObjectName, {
    sourceKey: sourceObjectName,
    sourceBucketName: 'examplebucket'
  }, {
    // 设置分片大小，单位为字节。除了最后一个分片没有大小限制，其他的分片最小为100 KB。
    partSize: 256 * 1024,
    headers
  });
  const tag = await client.getObjectTagging(targetObjectName)
  console.log(tag)
}

setTag()
```

## 为软链接文件设置标签

以下代码用于为软链接文件设置标签。

```
const OSS = require('ali-oss')

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

// 填写软链接完整路径，例如shortcut/myobject.txt。
const symLink = "shortcut/myobject.txt";
// 填写Object完整路径，Object完整路径中不能包含Bucket名称。例如exampledir/exampleobject.txt。
const targetObjectName = 'exampledir/exampleobject.txt'
                
// 设置请求头信息。
const headers = {
  // 依次填写对象标签的键（例如owner）和值（例如John）。
  'x-oss-tagging': 'owner=John&type=document',
}

async function setTag() {
  await client.putSymlink(symLink, targetObjectName, {
    storageClass: 'IA',
    meta: {
      uid: '1',
      slus: 'test.html'
    },
    headers
  });
  const tag = await client.getObjectTagging(targetObjectName)
  console.log(tag)
}

setTag()
```

## 相关文档
- 关于设置对象标签的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss?spm=a2c4g.11186623.0.0.13994772cq23ae#putObjectTaggingname-tag-options)。
- 关于设置对象标签的API接口说明，请参见[PutObjectTagging](https://help.aliyun.com/zh/oss/developer-reference/putobjecttagging#reference-185784)。

[上一篇：对象标签（Node.js SDK）](/zh/oss/developer-reference/object-tagging-6/)[下一篇：获取对象标签（Node.js SDK）](/zh/oss/developer-reference/query-the-tags-of-an-object-4)该文章对您有帮助吗？反馈
  
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