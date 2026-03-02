# 使用Node.js SDK拷贝版本控制Bucket中的指定版本文件

Source: https://help.aliyun.com/zh/oss/developer-reference/copy-objects-13

---

- 使用Node.js SDK拷贝版本控制Bucket中的指定版本文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 拷贝文件（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何在受版本控制的存储空间（Bucket）中拷贝文件（Object）。您可以通过CopyObject的方法拷贝小于1 GB的文件，通过分片拷贝（UploadPartCopy）的方法拷贝大于1 GB的文件。

## 拷贝小文件

对于小于1 GB的文件，您可以通过CopyObject方法将文件从一个存储空间（源存储空间）复制到同一地域的另一个存储空间（目标存储空间）。
- x-oss-copy-source默认拷贝Object的当前版本。如果当前版本是删除标记，则返回404表示该Object不存在。您可以在x-oss-copy-source中加入versionId来拷贝指定的Object版本，删除标记不能被拷贝。
- 您可以将Object的早期版本拷贝到同一个Bucket中，拷贝Object的历史版本将会成为一个新的当前版本，达到恢复Object早期版本的目的。
- 如果目标Bucket已开启版本控制，OSS将会为新拷贝出来的Object自动生成唯一的版本ID，此版本ID将会在响应header 的x-oss-version-id中返回。如果目标Bucket未曾开启或者暂停了版本控制，OSS将会为新拷贝的Object自动生成version ID为”null“的版本，且会覆盖原先versionId为”null“的版本。
- 目标Bucket在开启或暂停版本控制状态下，不支持对Appendable类型Object执行拷贝操作。

以下代码用于拷贝小文件：

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

// 指定拷贝源Object的versionId。
const versionId = 'versionId';
// 指定拷贝源Object。
const srcObject = 'srcObject.txt';
// 指定拷贝源Bucket。
const srcBucket = 'srcBucket';
// 指定拷贝目标Object。
const targetObject = 'targetObject.txt';
async function Copy() {
  try {
    const result = await client.copy(targetObject, srcObject, srcBucket, {
      meta: {
        versionId: versionId
      }
    });

    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

Copy()
```

## 拷贝大文件

对于大于1 GB的文件，需要使用分片拷贝（multipartUploadCopy）的方法。

分片拷贝默认从一个已存在的Object的当前版本中拷贝数据来上传一个Part。允许通过在请求header : x-oss-copy-source中附带versionId的子条件，实现从Object的指定版本进行拷贝，如x-oss-copy-source : /SourceBucketName/SourceObjectName?versionId=111111。
说明 
SourceObjectName要进行URL编码。响应中将会返回被拷贝的Object版本ID： x-oss-copy-source-version-id。

如果未指定versionId且拷贝Object的当前版本为删除标记，OSS将返回404 Not Found。通过指定versionId来拷贝删除标记时，OSS将返回400 Bad Request。

以下代码用于分片拷贝：

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

// 指定拷贝源Object的versionId。
const versionId = 'versionId';
// 指定拷贝源Object。
const srcObject = "srcObject.txt";
// 指定拷贝源Bucket。
const srcBucket = 'srcBucket';
// 指定拷贝目标Object。
const targetObject = "targetObject.txt";

async function multipartUploadCopy() {
  const result = await client.multipartUploadCopy(
    targetObject,
    {
      sourceKey: srcObject,
      sourceBucketName: srcBucket,
    },
    {
      versionId
    }
  );
  console.log(result);
}

multipartUploadCopy();
```

## 相关文档
- 关于拷贝小文件的API接口说明，请参见[CopyObject](https://help.aliyun.com/zh/oss/developer-reference/copyobject#reference-mvx-xxc-5db)。
- 关于拷贝大文件的API接口说明，请参见[UploadPartCopy](https://help.aliyun.com/zh/oss/developer-reference/uploadpartcopy#reference-t4b-vpx-wdb)。

[上一篇：下载文件（Node.js SDK）](/zh/oss/developer-reference/download-objects-16)[下一篇：列举文件（Node.js SDK）](/zh/oss/developer-reference/list-objects-8)该文章对您有帮助吗？反馈
  
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