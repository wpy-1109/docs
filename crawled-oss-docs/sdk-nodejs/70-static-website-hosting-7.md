# 网站托管与镜像回源Nodejs代码示例

Source: https://help.aliyun.com/zh/oss/developer-reference/static-website-hosting-7

---

- 网站托管与镜像回源Nodejs代码示例-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 静态网站托管（镜像回源）（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
您可以将存储空间（Bucket）设置为静态网站托管模式并设置镜像回源的跳转规则（RoutingRule）。静态网站托管模式配置生效后，访问网站相当于访问Bucket，并且能够自动跳转至指定的索引页面和错误页面。镜像回源的跳转规则配置生效后，可用于数据无缝迁移到OSS的场景。

## 静态网站托管

静态网站是指所有的网页都由静态内容构成，包括客户端执行的脚本（例如JavaScript）。您可以通过静态网站托管功能将您的静态网站托管到Bucket，并使用Bucket的访问域名访问这个网站。
- ### 设置静态网站托管
以下代码用于设置静态网站托管：
```
const OSS = require('ali-oss')

const client = new OSS({
  // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

// 设置静态网站托管。
async function putBucketWebsite () {
  try {
    // 填写Bucket名称，例如examplebucket。    
    const result = await client.putBucketWebsite('examplebucket', {
    // 设置静态网站托管的默认主页。
    index: 'index.html',
    // 设置静态网站托管的默认404页。
    error: 'error.html'
  });
   console.log(result);
  } catch (e) {
    console.log(e);
  }
}

putBucketWebsite();            
```
- ### 查看静态网站托管配置
以下代码用于查看静态网站托管配置：
```
const OSS = require('ali-oss')

const client = new OSS({
  // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

// 查看静态网站托管配置的默认首页和默认404页。
async function getBucketWebsite () {
  try {
    // 填写Bucket名称，例如examplebucket。
    const result = await client.getBucketWebsite('examplebucket');
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

getBucketWebsite();            
```
- ### 删除静态网站托管配置
以下代码用于删除静态网站托管配置：
```
const OSS = require('ali-oss')

const client = new OSS({
  // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

// 删除静态网站托管配置。
async function deleteBucketWebsite() {
  try {
    // 填写Bucket名称，例如examplebucket。
    const result = await client.deleteBucketWebsite('examplebucket');
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

deleteBucketWebsite();            
```

## 镜像回源

镜像回源主要用于数据无缝迁移到OSS的场景。例如某服务已经在用户建立的源站或者在其他云产品上运行，现因业务发展，需要将服务迁移至OSS，迁移时需保证服务的正常运行。您可以在迁移过程中使用镜像回源规则获取未迁移至OSS的部分数据，保证服务的正常运行。
- ### 设置镜像回源
例如，当请求者访问目标Bucket中不存在的文件时，可以通过指定回源条件和回源地址，从源站中获取目标文件。例如您在华东1（杭州）有名为examplebucket的Bucket，您希望请求者访问Bucket根目录下examplefolder目录中不存在的文件时，可以从https://www.example.com/站点的examplefolder目录获取目标文件。以下代码用于设置符合上述场景的镜像回源规则：
```
const OSS = require('ali-oss')
constpath=require("path")

const client = new OSS({
  // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

async function putBucketWebsite() {
  try {
    // 填写Bucket名称，例如examplebucket。
    const result = await client.putBucketWebsite("examplebucket", {
      // 设置静态网站托管的默认主页。
      index: "index.html",
      // 设置静态网站托管的默认404页。
      error: "error.html",
      // 指定访问子目录时，是否支持转到子目录下的默认主页。
      // supportSubDir:true ,
      // 指定设置默认主页后，访问以非正斜线（/）结尾的Object，且该Object不存在时的行为。仅在SupportSubDir设置为true时生效。
      // type: 0 ,
      routingRules: [
         { RuleNumber: 1,
             // 只有匹配此前缀的Object才能匹配此规则。
             Condition: { KeyPrefixEquals: "examplefolder/" ,
                          // 访问指定Object时，返回status 404才能匹配此规则。
                          HttpErrorCodeReturnedEquals: 404
                        },
             // 指定跳转的类型。
             Redirect: { RedirectType: "Mirror",
                         // 指定执行跳转或者镜像回源规则时，是否携带请求参数。
                         PassQueryString: true,
                         // 指定镜像回源的源站地址。
                         MirrorURL: 'http://example.com/',                         
                         // 与PassQueryString作用相同，优先级高于PassQueryString。只有设置RedirectType为Mirror时才生效。
                         MirrorPassQueryString:true,
                         // 如果镜像回源获取的结果为3xx，是否继续跳转到指定的Location获取数据。只有设置RedirectType为Mirror时才生效。此处设置此项为true，表明OSS会继续请求Location对应的地址。
                         MirrorFollowRedirect:true,
                         // 是否检查回源body的MD5。
                         MirrorCheckMd5:false,
                         // 指定镜像回源时携带的Header。
                         // 是否透传除以下Header之外的其他Header到源站。
                         MirrorHeaders:{ PassAll: true,
                                         // 将Pass中指定的Header透传到源站。
                                         Pass:'myheader-key1',
                                         Pass:'myheader-key2',
                                         // 禁止将Remove中指定的Header透传到源站。
                                         Remove:'myheader-key3',
                                         Remove:'myheader-key4'}
                        }}
       ] 
    });
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

putBucketWebsite();
```
- ### 获取镜像回源配置
以下代码用于获取镜像回源配置：
```
const OSS = require('ali-oss')
constpath=require("path")

const client = new OSS({
  // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

// 获取镜像回源配置。
async function getBucketWebsite () {
  try {
    // 填写Bucket名称，例如examplebucket。
    const result = await client.getBucketWebsite('examplebucket');
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

getBucketWebsite();            
```
- ### 删除镜像回源配置
以下代码用于删除镜像回源配置：
```
const OSS = require('ali-oss')
constpath=require("path")

const client = new OSS({
  // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // yourBucketName填写Bucket名称。
  bucket: 'yourBucketName',
});

// 删除镜像回源配置。
async function deleteBucketWebsite() {
  try {
    // 填写Bucket名称，例如examplebucket。
    const result = await client.deleteBucketWebsite('examplebucket');
    console.log(result);
  } catch (e) {
    console.log(e);
  }
}

deleteBucketWebsite();            
```

## 相关文档
- 关于设置静态网站托管或者镜像回源的API接口说明，请参见[PutBucketWebsite](https://help.aliyun.com/zh/oss/developer-reference/putbucketwebsite#reference-hwb-yr5-tdb)。
- 关于获取静态网站托管或者镜像回源的API接口说明，请参见[GetBucketWebsite](https://help.aliyun.com/zh/oss/developer-reference/getbucketwebsite#reference-wvy-s4w-tdb)。
- 关于删除静态网站托管或者镜像回源的API接口说明，请参见[DeleteBucketWebsite](https://help.aliyun.com/zh/oss/developer-reference/deletebucketwebsite#reference-zrl-msw-tdb)。

[上一篇：存储空间清单（Node.js SDK）](/zh/oss/developer-reference/bucket-inventory-1)[下一篇：日志转存（Node.js SDK）](/zh/oss/developer-reference/logging-8)该文章对您有帮助吗？反馈
  
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