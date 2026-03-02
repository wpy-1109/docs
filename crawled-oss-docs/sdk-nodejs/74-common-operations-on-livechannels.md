# LiveChannel管理（Node.js SDK）

Source: https://help.aliyun.com/zh/oss/developer-reference/common-operations-on-livechannels

---

- LiveChannel管理（Node.js SDK）-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# LiveChannel管理（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍LiveChannel常见操作，例如创建LiveChannel、列举LiveChannel及删除LiveChannel等。

## 创建LiveChannel

通过RTMP协议上传音视频数据前，必须先调用该接口创建一个LiveChannel。调用PutLiveChannel接口会返回RTMP推流地址，以及对应的播放地址。

以下代码用于创建LiveChannel：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称，LiveChannel名称不能包含正斜线（/），例如mychannel。
const cid = 'mychannel';
const conf = {
  // 填写LiveChannel的描述信息，最大长度不能超过128字节。
  Description: 'this is my channel',
  // 指定LiveChannel的状态。此处指定为enabled，表示启用LiveChannel。如需禁用LiveChannel，请将该参数设置为disabled。
  Status: 'enabled',
  Target: {
    // 指定转储的类型，目前仅支持HLS。
    Type: 'HLS',
    // 指定每个ts文件的时长，单位为秒。
    FragDuration: '10',
    // 当Type为HLS时，指定m3u8文件中包含ts文件的个数。
    FragCount: '5',
    // 当Type为HLS时，指定生成的m3u8文件的名称。名称必须以”.m3u8”结尾，长度范围为6~128字节。
    PlaylistName: 'playlist.m3u8'
  }
};

// 创建LiveChannel。
store.putChannel(cid, conf).then(r=>console.log(r))
```

## 获取LiveChannel信息

以下代码用于获取指定的LiveChannel信息：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称
const cid = 'mychannel'; 

// 获取LiveChannel信息。
store.getChannel(cid).then(r=>console.log(r));
```

## 设置LiveChannel状态

以下代码用于设置LiveChannel状态：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称。
const cid = 'mychannel';

// LiveChannel分为启用（enabled）和禁用（disabled）两种状态。
// LiveChannel处于disabled状态时，OSS会禁止您向该LiveChannel进行推流操作。如果您正在向该LiveChannel推流，那么推流的客户端会被强制断开（会有10s左右的延迟）。
store.putChannelStatus(cid, 'disabled').then(r=>console.log(r));
```

## 获取LiveChannel状态信息

以下代码用于获取指定LiveChannel的推流状态信息：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称。
const cid = 'mychannel';
// 获取LiveChannel状态信息。
store.getChannelStatus(cid).then(r=>console.log(r))
```

## 生成LiveChannel播放列表

PostVodPlaylist接口用于为指定的LiveChannel生成一个点播用的播放列表。OSS会查询指定时间范围内由该LiveChannel推流生成的ts文件，并将其拼装为一个m3u8播放列表。

以下代码用于生成LiveChannel播放列表：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称。
const cid = 'mychannel';

const r = await this.store.createVod(cid, 're-play', {
  // 指定查询ts文件的起始时间，格式为Unix时间戳。
  startTime: 1460464870,
  // 指定查询ts文件的终止时间，格式为Unix时间戳。
  endTime: 1460465877
  // EndTime必须大于StartTime，且时间跨度不能大于1天。
}).then(r=>console.log(r))
```

## 列举指定的LiveChannel

以下代码用于列举指定的LiveChannel：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

const r = await this.store.listChannels({
  // 列举前缀为'my'的LiveChannel。
  prefix: 'my',
  // 指定返回的LiveChannel的最大个数为3个。
  'max-keys': 3
}).then(r=>console.log(r))
```

## 获取LiveChannel推流记录

GetLiveChannelHistory接口用于获取指定LiveChannel的推流记录。使用GetLiveChannelHistory接口最多会返回指定LiveChannel最近的10次推流记录。

以下代码用于获取LiveChannel推流记录：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称。
const cid = 'mychannel';
// 获取LiveChannel推流记录。
store.getChannelHistory(cid).then(r=>console.log(r))
```

## 删除LiveChannel
重要 - 当有客户端正在向LiveChannel推流时，删除请求会失败。
- DeleteLiveChannel接口只会删除LiveChannel本身，不会删除推流生成的文件。

以下代码用于删除指定的LiveChannel：

```
const OSS = require('ali-oss');

const store = new OSS({
  // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
  region: 'yourRegion',
  // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  authorizationV4: true,
  // 填写Bucket名称。
  bucket: 'examplebucket',
})

// 填写LiveChannel名称。
const cid = 'mychannel'; 

// 删除LiveChannel。
store.deleteChannel(cid).then(r=>console.log(r))
```

## 相关文档
- 关于创建LiveChannel的API接口说明，请参见[PutLiveChannel](https://help.aliyun.com/zh/oss/developer-reference/putlivechannel#reference-d34-zcd-xdb)。
- 关于获取LiveChannel配置信息的API接口说明，请参见[GetLiveChannelInfo](https://help.aliyun.com/zh/oss/developer-reference/getlivechannelinfo#reference-ekp-dkd-xdb)。
- 关于设置LiveChannel的API接口说明，请参见[PutLiveChannelStatus](https://help.aliyun.com/zh/oss/developer-reference/putlivechannelstatus#reference-r5k-kcd-xdb)。
- 关于获取LiveChannel状态的API接口说明，请参见[GetLiveChannelStat](https://help.aliyun.com/zh/oss/developer-reference/getlivechannelstat#reference-ov4-n3d-xdb)。
- 关于列举指定LiveChannel的API接口说明，请参见[ListLiveChannel](https://help.aliyun.com/zh/oss/developer-reference/listlivechannel#reference-idb-smd-xdb)。
- 关于生成LiveChannel播放列表的API接口说明，请参见[PostVodPlaylist](https://help.aliyun.com/zh/oss/developer-reference/postvodplaylist#reference-ry3-fhd-xdb)。
- 关于获取LiveChannel推流记录的API接口说明，请参见[GetLiveChannelHistory](https://help.aliyun.com/zh/oss/developer-reference/getlivechannelhistory#reference-kjz-yld-xdb)。
- 关于删除LiveChannel的API接口说明，请参见[DeleteLiveChannel](https://help.aliyun.com/zh/oss/developer-reference/deletelivechannel#reference-d4g-k12-xdb)。

[上一篇：使用自定义域名（Node.js SDK）](/zh/oss/developer-reference/use-custom-domain-names)[下一篇：图片处理（Node.js SDK）](/zh/oss/developer-reference/img-5)该文章对您有帮助吗？反馈
  
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