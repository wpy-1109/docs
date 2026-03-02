# 使用Node.js SDK按指定范围下载Object

Source: https://help.aliyun.com/zh/oss/developer-reference/range-download-9

---

- 使用Node.js SDK按指定范围下载Object-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 范围下载（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
如果仅需要文件（Object）中的部分数据，您可以使用范围下载，下载指定范围内的数据。

## 指定正常的下载范围

当您指定的范围首端和末端都在文件的有效区间内，则按指定区间正常下载文件。例如现有大小为1000字节的Object，则指定的有效区间应为0~999。

以下代码用于指定正常的下载范围来下载文件：

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket'
});

async function main() {
  const start = 1, end = 900;
  // yourObjectName表示不包含Bucket名称在内的Object的完整路径，例如destfolder/examplefile.txt。
  // 获取目标Object的1~900字节范围内的数据，包含1和900，共900字节的数据。
  // 如果指定范围的首端或末端不在有效区间，则下载整个文件的内容，返回HTTP Code为200。
  const result = await client.get("", {
    headers: {
      Range: `bytes=${start}-${end}`,
    },
  })
  console.log(result.content.toString())
};

main();
```

关于Bucket命名规范的详情，请参见[存储空间（Bucket）](https://help.aliyun.com/zh/oss/terms-2#section-yxy-jmt-tdb)。关于Object命名规范的详情，请参见[对象（Object）](https://help.aliyun.com/zh/oss/terms-2#section-ihw-kmt-tdb)。

## 标准行为范围下载

通过在请求中增加请求头`x-oss-range-behavior:standard`，改变指定范围不在有效区间时OSS的下载行为。

以下代码用于标准行为范围下载：

```
const OSS = require('ali-oss');

const client = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket'
});

async function main() {
  // 上传大小为10字节的文件exampleobject.txt。
  const buf = Buffer.from("abcdefghij");
  await client.put("exampleobject.txt", buf);
  const result = await client.get("exampleobject.txt", {
  // 指定Range: bytes=5-15，此时范围末端取值不在有效区间，返回6~10字节范围内容，且HTTP Code为206。
    headers: {
      Range: "bytes=5-15",      
      "x-oss-range-behavior": "standard",
    },
  });
  console.log(result.content.toString() === 'fghij')
  console.log(result.res.status === 206)
  try{
    await client.get("exampleobject.txt", {
      // 指定Range: bytes=15-25，此时范围首端取值不在有效区间，返回HTTP Code为416，错误码为InvalidRange。
      headers: {
        Range: "bytes=15-25",        
        "x-oss-range-behavior": "standard",
      },
    })
  }catch(e) {
    console.log(e.status === 416);
    console.log(e.name === 'InvalidRangeError')
  }
}

main();
```

## 相关文档

关于范围下载的API接口说明，请参见[GetObject](https://help.aliyun.com/zh/oss/developer-reference/getobject#reference-ccf-rgd-5db)。

[上一篇：流式下载（Node.js SDK）](/zh/oss/developer-reference/streaming-download-2)[下一篇：限定条件下载（Node.js SDK）](/zh/oss/developer-reference/conditional-download-7)该文章对您有帮助吗？反馈
  
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