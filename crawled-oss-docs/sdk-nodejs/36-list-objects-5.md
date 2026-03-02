# 使用Node.js SDK通过不同参数列举Object和目录

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects-5

---

- 使用Node.js SDK通过不同参数列举Object和目录-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
本文介绍如何列举指定存储空间下（Bucket）的所有文件（Object）、指定个数的文件、指定前缀的文件等。

## 列举方法

您可以调用`list`或`listV2`方法，一次性列举某个Bucket下最多1000个Object。您可以通过指定参数实现多种列举功能，例如通过指定参数列举指定起始位置后的所有文件、列举指定目录下的文件和子目录、以及列举结果分页。这两个接口的主要区别如下：
- 使用`list`方法列举文件时，默认返回owner信息。
- 使用`listV2`方法列举文件时，需通过fetchOwner指定是否在返回结果中包含owner信息。说明 对于开启版本控制的Bucket，建议使用`listV2`接口列举文件。

以下分别介绍通过`list`以及`listV2`方法列举文件时涉及的参数说明。
- 通过list方法列举文件list涉及参数说明如下：参数类型描述prefixstring列举符合特定前缀的文件。delimiterstring对文件名称进行分组的字符。markerstring列举文件名在marker之后的文件。max-keysnumber | string指定最多返回的文件个数。encoding-type'url' | ''对返回的内容进行编码并指定编码类型为URL。
- 通过listV2方法列举文件listV2涉及参数说明如下：参数类型描述prefixstring列举符合特定前缀的文件。continuation-tokenstring从此token开始获取文件列表。delimiterstring对文件名称进行分组的字符。max-keysnumber | string指定最多返回的文件个数。start-afterstring设定从start-after之后按字母排序开始返回Object。fetch-ownerboolean是否在返回结果中包含owner信息 。encoding-type'url' | ''对返回的内容进行编码并指定编码类型为URL。

## 简单列举文件

以下代码用于列举指定Bucket的文件，默认列举100个文件。
- 通过list方法 
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
    // 不带任何参数，默认最多返回100个文件。
    const result = await client.list();
    console.log(result);
}

list();
```
- 通过listV2方法 
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
    // 不带任何参数，默认最多返回100个文件。
    const result = await client.listV2();
    console.log(result);
}

list();
```

## 列举指定个数的文件

以下代码用于通过max-keys参数列举Bucket下指定个数的文件。
- 通过list方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
    const result = await client.list({
        // 设置按字母排序最多返回前10个文件。
      "max-keys": 10
  });
    console.log(result);
}

list();
```
- 通过listV2方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
    const result = await client.listV2({
        // 设置按字母排序最多返回前10个文件。
      "max-keys": 10
  });
    console.log(result);
}

list();
```

## 列举指定前缀的文件

以下代码用于通过prefix参数列举Bucket中包含指定前缀的文件。
- 通过list方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
  const result = await client.list({
    // 列举10个文件。
    "max-keys": 10,
    // 列举文件名中包含前缀foo/的文件。
    prefix: 'foo/'
  });
  console.log(result);
}

list();
```
- 通过listV2方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
  const result = await client.listV2({
    // 列举10个文件。
    "max-keys": 10,
    // 列举文件名中包含前缀foo/的文件。
    prefix: 'foo/'
  });
  console.log(result);
}

list();
```

## 列举指定文件名后的文件

以下代码用于列举文件名称字典序排在指定字符串（marker或startAfter）之后的文件。
- 通过list方法参数marker代表文件名称。
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

// 列举字典序排在test之后的文件。默认列举100个文件。
const marker = 'test'
async function list () {
  const result = await client.list({
    marker
  });
  console.log(result);
}

list();
```
- 通过listV2方法startAfter代表文件名称。
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
  const result = await client.listV2({
    // 列举a/文件夹下名称在a/b之后的文件及子文件夹。
    delimiter: '/',
    prefix: 'a/',
    'start-after': 'a/b'
  });
  console.log(result.objects, result.prefixes);
}

list();
```

## 分页列举所有文件

以下代码用于分页列举指定Bucket下的所有文件。每页列举的文件个数通过max-keys指定。
- 通过list方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

let marker = null; 

// 每页列举20个文件。
const maxKeys = 20;

async function list () {
  do {
    const result = await client.list({
      marker: marker, 
      'max-keys': maxKeys
    });
    marker = result.nextMarker;
    console.log(result);
  } while (marker);
}

list();
```
- 通过listV2方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

async function list () {
  let continuationToken = null;
  // 每页列举20个文件。
  const maxKeys = 20;
  do {
    const result = await client.listV2({
      'continuation-token': continuationToken,
      'max-keys': maxKeys
      });
    continuationToken = result.nextContinuationToken;
        console.log(result);
  }while(continuationToken)
}

list();
```

## 列举结果返回文件owner信息

以下代码用于列举结果中返回文件的owner信息：

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

// 默认列举的文件信息中不包含owner信息。如需包含owner信息，fetch-owner参数取值为true。
async function list () {
  const result = await client.listV2({
    'fetch-owner': true
  });
  console.log(result.objects);
}

list();
```

## 列举指定目录下的文件和子目录

OSS没有文件夹的概念，所有元素都是以文件来存储。创建文件夹本质上来说是创建了一个大小为0并以正斜线（/）结尾的文件。这个文件可以被上传和下载，控制台会对以正斜线（/）结尾的文件以文件夹的方式展示。

通过delimiter和prefix两个参数可以模拟文件夹功能：
- 如果设置prefix为某个文件夹名称，则会列举以此prefix开头的文件，即该文件夹下所有的文件和子文件夹（目录）均显示为objects。
- 如果在设置了prefix的情况下，将delimiter设置为正斜线（/），则只列举该文件夹下的文件和子文件夹（目录），该文件夹下的子文件夹（目录）显示为CommonPrefixes，子文件夹下的文件和文件夹不显示。

假设Bucket中有如下文件：

```
foo/x
foo/y
foo/bar/a
foo/bar/b
foo/hello/C/1
foo/hello/C/2
...
foo/hello/C/9999
```

以下代码用于通过`list`或`listV2`的方法列举指定目录下的文件和子目录。
- 通过list方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

// 调用listDir函数，通过设置不同的文件前缀列举不同的目标文件。
async function listDir(dir) {
  try {
    const result = await client.list({
      prefix: dir,
      delimiter: '/'
    });
    if (result && result.prefixes) {
      result.prefixes.forEach(subDir => {
        console.log('SubDir: %s', subDir);
      });
    }
    if (result && result.objects) {
      result.objects.forEach(obj => {
        console.log('Object: %s', obj.name);
      });
    }
  } catch (e) {
    console.log(e);
  }
}

listDir('foo/');
// 预期返回如下：
// SubDir: foo/bar/
// SubDir: foo/hello/
// Object: foo/x
// Object: foo/y

listDir('foo/bar/');
// 预期返回如下：
// Object: foo/bar/a
// Object: foo/bar/b

listDir('foo/hello/C/');
// 预期返回如下：
// Object: foo/hello/C/1
// Object: foo/hello/C/2
// ...
// Object: foo/hello/C/9999
```
- 通过listV2方法
```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourbucketname填写存储空间名称。
  bucket: 'yourbucketname'
});

// 调用listV2Dir函数，通过设置不同的文件前缀列举不同的目标文件。
async function listV2Dir(dir) {
  try {
    const result = await client.listV2({
      prefix: dir,
      delimiter: '/'
    });
    if (result && result.prefixes) {
      result.prefixes.forEach(subDir => {
        console.log('SubDir: %s', subDir);
      });
    }
    if (result && result.objects) {
      result.objects.forEach(obj => {
        console.log('Object: %s', obj.name);
      });
    }
  } catch (e) {
    console.log(e);
  }
}

listDir('foo/');
// 预期返回
// SubDir: foo/bar/
// SubDir: foo/hello/
// Object: foo/x
// Object: foo/y

listDir('foo/bar/');
// 预期返回
// Object: foo/bar/a
// Object: foo/bar/b

listDir('foo/hello/C/');
// 预期返回
// Object: foo/hello/C/1
// Object: foo/hello/C/2
// ...
// Object: foo/hello/C/9999
```

## 相关文档
- 关于列举文件的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss?spm=a2c4g.11186623.0.0.13994772cq23ae#listquery-options)。
- 关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)和[ListObjectsV2（GetBucketV2）](https://help.aliyun.com/zh/oss/developer-reference/listobjects-v2#reference-2520881)。

[上一篇：管理文件元数据（Node.js SDK）](/zh/oss/developer-reference/manage-object-metadata-4)[下一篇：拷贝文件（Node.js SDK）](/zh/oss/developer-reference/copy-objects-5)该文章对您有帮助吗？反馈
  
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