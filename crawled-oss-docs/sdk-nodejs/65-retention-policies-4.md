# 使用Node.js SDK配置与管理Bucket保留策略

Source: https://help.aliyun.com/zh/oss/developer-reference/retention-policies-4

---

- 使用Node.js SDK配置与管理Bucket保留策略-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 保留策略（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS保留策略具有WORM（Write Once Read Many）特性，满足用户以不可删除、不可篡改方式保存和使用数据。如果您希望指定时间内任何用户（包括资源拥有者）均不能修改和删除OSS某个Bucket中的Object，您可以选择为Bucket配置保留策略。在保留策略指定的Object保留时间到期之前，仅支持在Bucket中上传和读取Object。Object保留时间到期后，才可以修改或删除Object。
说明 
在配置保留策略之前，请确保您已了解该功能。详情请参见[保留策略（WORM）](https://help.aliyun.com/zh/oss/user-guide/oss-retention-policies)。

## 新建保留策略

以下代码用于新建保留策略。

```
const OSS = require('ali-oss');

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
// 创建保留策略。
async function initiateBucketWorm() {
 // yourbucketname填写存储空间名称。
  const bucket = 'yourbucketname'
  // 指定Object保护天数。
  const days = ''
    const res = await client.initiateBucketWorm(bucket, days)
  console.log(res.wormId)
}

initiateBucketWorm()
```

## 取消未锁定的保留策略

以下代码用于取消未锁定的保留策略：

```
const OSS = require('ali-oss');

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
// 取消保留策略。
async function abortBucketWorm() {
  // yourbucketname填写存储空间名称。
  const bucket = 'yourbucketname'
    try {
    await client.abortBucketWorm(bucket)
    console.log('abort success')
  } catch(err) {
        console.log('err: ', err)
    }
}

abortBucketWorm()
```

## 锁定保留策略

以下代码用于锁定保留策略。

```
const OSS = require('ali-oss');

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
// 锁定保留策略。
async function completeBucketWorm() {
  // yourbucketname填写存储空间名称。
  const bucket = 'yourbucketname'
  const wormId = 'Your Worm Id'
    try {
        await client.completeBucketWorm(bucket, wormId)
  } catch(err) {
      console.log(err)
  }
}

completeBucketWorm()
```

## 获取保留策略

以下代码用于获取保留策略。

```
const OSS = require('ali-oss');

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
// 获取保留策略。
async function getBucketWorm() {
  // yourbucketname填写存储空间名称。
  const bucket = 'yourbucketname'
    try {
        const res = await client.getBucketWorm(bucket)
    // 查看保留策略ID。
    console.log(res.wormId)
    // 查看保留策略状态。未锁定状态为"InProgress"，锁定状态为"Locked"。
    console.log(res.state)
    // 查看Object的保护时间。
    console.log(res.days)
  } catch(err) {
      console.log(err)
  }
}

getBucketWorm()
```

## 延长Object的保留天数

以下代码用于延长已锁定的保留策略中Object的保留天数.

```
const OSS = require('ali-oss');

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
// 延长已锁定的保留策略中Object的保留天数。
async function extendBucketWorm() {
  // yourbucketname填写存储空间名称。
  const bucket = 'yourbucketname'
  const wormId = 'Your Worm Id'
  const days = 'Retention Days'
    try {
        const res = await client.extendBucketWorm(bucket, wormId, days)
    console.log(res)
  } catch(err) {
      console.log(err)
  }
}

extendBucketWorm()
```

## 相关文档
- 关于保留策略的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss?spm=a2c4g.11186623.0.0.13994772cq23ae#abortBucketWormname-options)。
- 关于新建保留策略的API接口说明，请参见[InitiateBucketWorm](https://help.aliyun.com/zh/oss/developer-reference/initiatebucketworm#reference-2536872)。
- 关于取消未锁定的保留策略的API接口说明，请参见[AbortBucketWorm](https://help.aliyun.com/zh/oss/developer-reference/abortbucketworm#reference-2536930)。
- 关于锁定保留策略的API接口说明，请参见[CompleteBucketWorm](https://help.aliyun.com/zh/oss/developer-reference/completebucketworm#reference-2536956)。
- 关于获取保留策略的API接口说明，请参见[GetBucketWorm](https://help.aliyun.com/zh/oss/developer-reference/getbucketworm#reference-2537016)。
- 关于延长Object的保留天数的API接口说明，请参见[ExtendBucketWorm](https://help.aliyun.com/zh/oss/developer-reference/extendbucketworm#reference-2536974)。

[上一篇：跨域资源共享（Node.js SDK）](/zh/oss/developer-reference/cors-8)[下一篇：服务端加密（Node.js SDK）](/zh/oss/developer-reference/server-side-encryption-7)该文章对您有帮助吗？反馈
  
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