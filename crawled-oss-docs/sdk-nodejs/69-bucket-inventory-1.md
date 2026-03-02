# 使用Node.js SDK管理存储空间清单配置

Source: https://help.aliyun.com/zh/oss/developer-reference/bucket-inventory-1

---

- 使用Node.js SDK管理存储空间清单配置-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 存储空间清单（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何使用Node.js添加、查看、列举、删除存储空间（Bucket）的清单（Inventory）配置。
重要 
如果您通过RAM用户使用清单功能，请确保已拥有清单功能的相关权限。关于清单功能的权限说明，请参见[OSS Action分类](https://help.aliyun.com/zh/oss/ram-policy-overview/#concept-y5r-5rm-2gb/section-x3c-nsm-2gb)。

## 添加清单配置

添加清单配置时，有如下注意事项：
- 单个Bucket最多只能配置1000条清单规则。
- 配置清单的源Bucket与存放导出的清单文件所在的目标Bucket必须位于同一个Region。

以下代码用于为某个Bucket添加清单配置。

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourBucketName填写存储空间名称。
  bucket: 'yourBucketName',
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
});

const inventory = {
  // 设置清单配置ID。
  id: 'default',
  // 清单配置是否启用的标识，取值为true或者false。
  isEnabled: false,
  // （可选）设置清单筛选规则，指定筛选object的前缀。
  prefix: 'ttt',
  OSSBucketDestination: {
    // 设置清单格式。
    format: 'CSV',
    // yourAccountId填写目标Bucket拥有者的账号ID。
    accountId: 'yourAccountId',
    // AliyunOSSRole填写目标Bucket的角色名称。
    rolename: 'AliyunOSSRole',
    // yourBucketName填写目标Bucket的名称。
    bucket: 'yourBucketName',
    // （可选）yourPrefix填写清单结果的存储路径前缀。
    prefix: 'yourPrefix ',
    // 如果需要使用SSE-OSS加密清单，请参考以下代码。
    // encryption: {'SSE-OSS': ''}
    // 如果需要使用SSE-KMS加密清单，请参考以下代码。
    /*
    encryption: {
      'SSE-KMS': {
        keyId: 'test-kms-id';
      };
    */
  },
  // 设置清单的生成计划，WEEKLY对应每周一次，DAILY对应每天一次。
  frequency: 'Daily',
  // 设置清单结果中包含了Object的所有版本, 如果设置为Current，则表示仅包含Object的当前版本。
  includedObjectVersions: 'All',
  optionalFields: {
    // （可选）设置清单中包含的Object属性。
    field: [
      'Size',
      'LastModifiedDate',
      'ETag',
      'StorageClass',
      'IsMultipartUploaded',
      'EncryptionStatus',
    ],
  },
};

async function putInventory() {
  // yourBucketName填写需要添加清单配置的Bucket名称。
  const bucket = 'yourBucketName';
  try {
    await client.putBucketInventory(bucket, inventory);
    console.log('清单配置添加成功');
  } catch (err) {
    console.log('清单配置添加失败：', err);
  }
}

putInventory();

```

## 查看清单配置

以下代码用于查看某个Bucket的清单配置。

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourBucketName填写存储空间名称。
  bucket: 'yourBucketName',
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
});

async function getBucketInventoryById() {
  // yourBucketName填写指定获取清单配置的Bucket名称。
  const bucket = 'yourBucketName';
  try {
    // 查看清单配置。
    const result = await client.getBucketInventory(bucket, 'inventoryid');
    console.log(result.inventory);
  } catch (err) {
    console.log(err);
  }
}

getBucketInventoryById();

```

## 批量列举清单配置
说明 
单次请求最多可获取100条清单配置项内容。若需获取超过100条清单配置项，则需发送多次请求，并保留相应的Token，作为下一次请求的参数。

以下代码用于批量列举某个Bucket的清单配置。

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourBucketName填写存储空间名称。
  bucket: 'yourBucketName',
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
});

async function listBucketInventory() {
  const bucket = 'yourBucketName'; // 填写指定存储空间名称。

  async function getNextPage(nextContinuationToken) {
    // 使用nextContinuationToken来获取下一页，如果不提供token，则获取第一页。
    const result = await client.listBucketInventory(bucket, nextContinuationToken);

    // 输出结果。
    console.log(result.inventoryList);

    // 如果还有下一页，递归调用函数。
    if (result.nextContinuationToken) {
      await getNextPage(result.nextContinuationToken);
    }
  }

  // 开始获取第一页。
  await getNextPage();
}

listBucketInventory();

```

## 删除清单配置

以下代码用于删除某个Bucket的清单配置。

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourBucketName填写存储空间名称。
  bucket: 'yourBucketName',
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourregion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
});

async function deleteBucketInventoryById() {
  // yourBucketName填写指定存储空间名称。
  const bucket = 'yourBucketName';
  // 删除指定ID的清单配置。
  const inventory_id = 'Your InventoryId';
  try {
    await client.deleteBucketInventory(bucket, inventory_id);
  } catch (err) {
    console.log(err);
  }
}

deleteBucketInventoryById();

```

## 相关文档
- 关于存储空间清单的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss?spm=a2c4g.11186623.0.0.13994772cq23ae#getBucketInventoryname-inventoryid-options)。
- 关于添加存储空间清单配置的API接口说明，请参见[PutBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/putbucketinventory#doc-api-Oss-PutBucketInventory)。
- 关于查看存储空间清单配置的API接口说明，请参见[GetBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/getbucketinventory#reference-2379122)。
- 关于批量列举存储空间清单配置的API接口说明，请参见[ListBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/listbucketinventory#reference-2379134)。
- 关于删除存储空间清单配置的API接口说明，请参见[DeleteBucketInventory](https://help.aliyun.com/zh/oss/developer-reference/deletebucketinventory#reference-2379150)。

[上一篇：生命周期（Node.js SDK）](/zh/oss/developer-reference/manage-lifecycle-rules-3)[下一篇：静态网站托管（镜像回源）（Node.js SDK）](/zh/oss/developer-reference/static-website-hosting-7)该文章对您有帮助吗？反馈
  
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