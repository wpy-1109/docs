# 通过Node.js SDK管理存储空间标签

Source: https://help.aliyun.com/zh/oss/developer-reference/bucket-tagging-2

---

- 通过Node.js SDK管理存储空间标签-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 存储空间标签（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
您可以通过存储空间（Bucket）的标签功能，对Bucket进行分类管理，例如ListBucket时只显示带有指定标签的Bucket。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以从环境变量读取访问凭证为例。如何配置访问凭证，请参见[Java配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/oss-java-configure-access-credentials#main-2350752)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[常见场景配置示例](https://help.aliyun.com/zh/oss/developer-reference/initialization-3#section-ngr-tjb-kfb)。
- 每个Bucket最多可设置20个标签（Key-Value对）。
- Key和Value必须为UTF-8编码。
- Key最大长度为64字符，区分大小写，不能为空。Key不支持以`http://`、`https://`、`Aliyun`为前缀（不区分大小写）。
- Value最大长度为128字符，可以为空。

## 设置存储空间标签

以下代码用于为存储空间设置标签。

```
const OSS = require('ali-oss')

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

// 设置Bucket标签。
async function putBucketTags(bucketName, tag) {
  try {
    const result = await client.putBucketTags(bucketName, tag);
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

const tag = { a: '1', b: '2' };
putBucketTags('bucketName', tag)
```

## 获取存储空间标签

以下代码用于获取存储空间的标签。

```
const OSS = require('ali-oss')

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

//获取Bucket标签。
async function getBucketTags(bucketName) {
  try {
    const result = await client.getBucketTags(bucketName);
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

getBucketTags('bucketName')
```

## 列举带指定标签的存储空间

以下代码用于列举带指定标签的Bucket。

```
const OSS = require('ali-oss')

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',

});

// 列举带指定标签的Bucket。
async function listBucketTags() {
  try {
    const params = {
      // 填充tag-key、tag-value字段到listBuckets接口的params参数中。
      'tag-key': 'yourTagKey',
      'tag-value': 'yourTagValue'
    }
    const result = await client.listBuckets(params);
    console.log(result);
  } catch (err) {
    console.log(err);
  }
}

listBucketTags();
```

## 删除存储空间标签

以下代码用于删除存储空间的标签。

```
const OSS = require('ali-oss')

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',

});

// 删除Bucket标签。
async function deleteBucketTags(bucketName) {
  try {
    const result = await client.deleteBucketTags(bucketName);
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

deleteBucketTags('bucketName')
```

## 相关文档
- 关于存储空间标签的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss?spm=a2c4g.11186623.0.0.13994772cq23ae#putBucketTagsname-tag-options)。
- 关于设置存储空间标签的API接口说明，请参见[PutBucketTags](https://help.aliyun.com/zh/oss/developer-reference/putbuckettags#concept-261782)。
- 关于获取存储空间标签的API接口说明，请参见[GetBucketTags](https://help.aliyun.com/zh/oss/developer-reference/getbuckettags#concept-261796)。
- 关于删除存储空间标签的API接口说明，请参见[DeleteBucketTags](https://help.aliyun.com/zh/oss/developer-reference/deletebuckettags#concept-261821)。

[上一篇：请求者付费模式（Node.js SDK）](/zh/oss/developer-reference/pay-by-requester-5)[下一篇：权限控制（Node.js SDK）](/zh/oss/developer-reference/access-control-5/)该文章对您有帮助吗？反馈
  
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