# NodeJS SDK分片上传使用方法与示例

Source: https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-3

---

- NodeJS SDK分片上传使用方法与示例-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 分片上传（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS提供的分片上传（Multipart Upload）功能，将要上传的较大文件（Object）分成多个分片（Part）来分别上传，上传完成后再调用CompleteMultipartUpload接口将这些Part组合成一个Object来达到断点续传的效果。

## 背景信息

当需要上传的文件较大时，您可以通过`MultipartUpload`方法进行分片上传。分片上传是指将要上传的文件分成多个数据块（Part）来分别上传。当其中一些分片上传失败后，OSS将保留上传进度记录。当您再次重传时，只需要上传失败的分片，不需要重新上传整个文件。
重要 
通常在文件大于100 MB的情况下，建议采用分片上传的方法，通过断点续传和重试，提高上传成功率。如果在文件小于100 MB的情况下使用分片上传，且partSize设置不合理的情况下，可能会出现无法完整显示上传进度的情况。对于小于100 MB的文件，建议使用简单上传的方式。

在使用`MultipartUpload`方法时，如果遇到`ConnectionTimeoutError`超时问题，业务方需自行处理超时逻辑。例如通过缩小分片大小、增加超时时间、重试请求或者捕获`ConnectionTimeoutError`错误等方法处理超时。更多信息，请参见[网络错误处理](https://help.aliyun.com/zh/oss/network-connection-timeout-handling)。

分片上传涉及的相关参数说明请参见下表。
| 类型 | 参数 | 说明|
| 必选参数 | name {String} | Object完整路径，Object完整路径中不能包含Bucket名称。|
| file {String|File} | 表示文件路径或者HTML5文件。|
| [options] {Object} 可选参数 | [checkpoint] {Object} | 记录本地分片上传结果的文件。开启断点续传功能时需要设置此参数，上传过程中的进度信息会保存在该文件中，如果某一分片上传失败，再次上传时会根据文件中记录的点继续上传。上传完成后，该文件会被删除。|
| [parallel] {Number} | 并发上传的分片个数，默认值为5。如果无特殊需求，无需手动设置此参数。|
| [partSize] {Number} | 指定上传的每个分片的大小，范围为100 KB~5 GB。单个分片默认大小为1 * 1024 * 1024（即1 MB）。如果无特殊需求，无需手动设置此参数。|
| [progress] {Function} | 表示进度回调函数，用于获取上传进度，可以是async的函数形式。回调函数包含三个参数：
- percentage {Number}：进度百分比（0~1之间的小数）。
- checkpoint {Object}：与[options] {Object}中的[checkpoint] {Object}定义相同。
- res {Object}：单个分片上传成功返回的response。|
| [meta] {Object} | 用户自定义的Header meta信息，Header前缀为`x-oss-meta-`。|
| [mime] {String} | 设置Content-Type请求头。|
| [headers] {Object} | 其他Header。更多信息，请参见[RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616.html)。其中：
- 'Cache-Control'：通用消息头被用在HTTP请求和响应中通过指定指令来实现缓存机制，例如`Cache-Control: public, no-cache`。
- 'Content-Disposition'：指示回复的内容该以何种形式展示，是以网页预览的形式，还是以附件的形式下载并保存到本地，例如`Content-Disposition: somename`。
- 'Content-Encoding'：用于对特定媒体类型的数据进行压缩，例如`Content-Encoding: gzip`。
- 'Expires'：缓存内容的过期时间，单位为毫秒。|

## 分片上传完整示例
重要 
Node.js分片上传过程中不支持MD5校验。建议分片上传完成后调用CRC64库自行判断是否进行CRC64校验。

以下代码通过`multipartUpload`方法进行分片上传。

```
const OSS = require('ali-oss');
const path = require("path");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: 'yourbucketname',
});

const progress = (p, _checkpoint) => {
  // Object的上传进度。
  console.log(p); 
  // 分片上传的断点信息。
  console.log(_checkpoint); 
};

const headers = {  
  // 指定Object的存储类型。
  'x-oss-storage-class': 'Standard', 
  // 指定Object标签，可同时设置多个标签。
  'x-oss-tagging': 'Tag1=1&Tag2=2', 
  // 指定初始化分片上传时是否覆盖同名Object。此处设置为true，表示禁止覆盖同名Object。
  'x-oss-forbid-overwrite': 'true'
}

// 开始分片上传。
async function multipartUpload() {
  try {
    // 依次填写Object完整路径（例如exampledir/exampleobject.txt）和本地文件的完整路径（例如D:\\localpath\\examplefile.txt）。Object完整路径中不能包含Bucket名称。
    // 如果本地文件的完整路径中未指定本地路径（例如examplefile.txt），则默认从示例程序所属项目对应本地路径中上传文件。
    const result = await client.multipartUpload('exampledir/exampleobject.txt', path.normalize('D:\\localpath\\examplefile.txt'), {
      progress,
      // headers,
      // 指定meta参数，自定义Object的元数据。通过head接口可以获取到Object的meta数据。
      meta: {
        year: 2020,
        people: 'test',
      },
    });
    console.log(result);
    // 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
    const head = await client.head('exampledir/exampleobject.txt');
    console.log(head);
  } catch (e) {
    // 捕获超时异常。
    if (e.code === 'ConnectionTimeoutError') {
      console.log('TimeoutError');
      // do ConnectionTimeoutError operation
    }
    console.log(e);
  }
}

multipartUpload();
```

以上分片上传完整示例调用的方法`multipartUpload`中封装了初始化分片上传、上传分片以及完成分片上传三个API接口。如果您希望分步骤实现分片上传，请依次调用[.initMultipartUpload](https://github.com/ali-sdk/ali-oss/blob/565bd8606ffe518dbe98628f86f10f5ff047745f/README.md#initmultipartuploadname-options)、[.uploadPart](https://github.com/ali-sdk/ali-oss/blob/565bd8606ffe518dbe98628f86f10f5ff047745f/README.md#uploadpartname-uploadid-partno-file-start-end-options)以及[.completeMultipartUpload](https://github.com/ali-sdk/ali-oss/blob/565bd8606ffe518dbe98628f86f10f5ff047745f/README.md#completemultipartuploadname-uploadid-parts-options)方法。

## 取消分片上传事件

您可以调用`client.abortMultipartUpload`方法来取消分片上传事件。当一个分片上传事件被取消后，无法再使用该uploadId做任何操作，已经上传的分片数据会被删除。

以下代码用于取消分片上传事件。

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: "yourregion",
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: "yourbucketname",
});

async function abortMultipartUpload() {
  // 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
  const name = "exampledir/exampleobject.txt";
  // 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后的返回结果。
  const uploadId = "0004B999EF518A1FE585B0C9360D****";
  const result = await client.abortMultipartUpload(name, uploadId);
  console.log(result);
}

abortMultipartUpload();

```

## 列举分片上传事件

调用`client.listUploads`方法列举出所有执行中的分片上传事件，即已初始化但尚未完成或尚未取消的分片上传事件。

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: "yourregion",
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: "yourbucketname",
});

async function listUploads(query = {}) {
  // query中支持设置prefix、marker、delimiter、upload-id-marker和max-uploads参数。
  const result = await client.listUploads(query);

  result.uploads.forEach((upload) => {
    // 分片上传的uploadId。
    console.log(upload.uploadId);
    // 将所有上传完成后的分片（Part）组合为一个完整的Object，并指定Object完整路径。
    console.log(upload.name);
  });
}

const query = {
  // 指定此次返回Multipart Uploads事件的最大个数。max-uploads参数的默认值和最大值均为1000。
  "max-uploads": 1000,
};
listUploads(query);

```

## 列举已上传的分片

分片上传过程中，调用`client.listParts`方法列举指定uploadId下所有已经上传成功的分片。

```
const OSS = require("ali-oss");

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: "yourregion",
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写存储空间名称。
  bucket: "yourbucketname",
});

async function listParts() {
  const query = {
    // 指定此次返回的最大分片（Part）个数。max-parts参数的默认值和最大值均为1000。
    "max-parts": 1000,
  };
  let result;
  do { 
    result = await client.listParts(
      // 填写Object完整路径（例如exampledir/exampleobject.txt）。Object完整路径中不能包含Bucket名称。
      "exampledir/exampleobject.txt",
      // uploadId来源于调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前的返回结果
      "0004B999EF518A1FE585B0C9360D****",
      query
    );
    // 指定下次列举分片的起始位置，只有分片号大于此参数值的分片会被列举。
    query["part-number-marker"] = result.nextPartNumberMarker;
    result.parts.forEach((part) => {
      console.log(part.PartNumber);
      console.log(part.LastModified);
      console.log(part.ETag);
      console.log(part.Size);
    });
  } while (result.isTruncated === "true");
}

listParts();
```

## 相关文档
- 关于分片上传的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss/blob/565bd8606ffe518dbe98628f86f10f5ff047745f/README.md#initmultipartuploadname-options)。
- Node.js SDK分片上传调用的方法`multipartUpload`中封装了三个API接口，详情如下：关于初始化分片上传事件的API接口说明，请参见[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)。
- 关于分片上传Part的API接口说明，请参见[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)。
- 关于完成分片上传的API接口说明，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。
- 关于取消分片上传事件的API接口说明，请参见[AbortMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)。
- 关于列举已上传分片的API接口说明，请参见[ListParts](https://help.aliyun.com/zh/oss/developer-reference/listparts#reference-hzm-1zx-wdb)。
- 关于列举所有执行中的分片上传事件（即已初始化但尚未完成或尚未取消的分片上传事件）的API接口说明，请参见[ListMultipartUploads](https://help.aliyun.com/zh/oss/developer-reference/listmultipartuploads#reference-hj2-3wx-wdb)。

[上一篇：流式上传（Node.js SDK）](/zh/oss/developer-reference/streaming-upload-1)[下一篇：追加上传（Node.js SDK）](/zh/oss/developer-reference/append-upload-4)该文章对您有帮助吗？反馈
  
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