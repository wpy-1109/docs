# 使用BrowserjsSDK按限定条件下载文件

Source: https://help.aliyun.com/zh/oss/developer-reference/conditional-download-3

---

- 使用BrowserjsSDK按限定条件下载文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 限定条件下载（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
下载文件（Object）时，可以指定一个或多个限定条件。满足限定条件则下载，条件不满足则返回错误且不会触发下载行为。

## 注意事项
- 当您使用webpack或browserify等打包工具时，请通过npm install ali-oss的方式安装Browser.js SDK。
- 通过浏览器访问OSS时涉及跨域请求，如果未设置跨域规则，浏览器会拒绝跨域访问请求。如果您希望通过浏览器可以正常访问OSS，需要通过OSS设置跨域规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。
- 由于Browser.js SDK通常在浏览器环境下使用，为避免暴露阿里云账号访问密钥（AccessKey ID和AccessKey Secret），强烈建议您使用临时访问凭证的方式执行OSS相关操作。临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。获取临时访问凭证的具体操作，请参见[授权访问（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-6#section-iy3-bfe-7mn)。

## 示例代码

以下代码用于限定条件下载：

```

  
  Document

  上传
  下载
    
  
  
      const client = new OSS({
         // yourRegion填写Bucket所在地域。以华东1（杭州）为例，yourRegion填写为oss-cn-hangzhou。
         region: 'yourRegion',
         authorizationV4: true,
         // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
         accessKeyId: 'yourAccessKeyId',
         accessKeySecret: 'yourAccessKeySecret',
         // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
      });

    const download = document.getElementById('download')
    const upload = document.getElementById('upload')

    // 上传文件。  
    upload.addEventListener('click', () => {
      // 指定待上传的文件内容。
      const file = new Blob(['examplecontent'])
      // 指定待上传文件的完整路径，例如exampledir/exampleobject.txt。
      const fileName = 'exampledir/exampleobject.txt'
      const result = client.put(fileName, file).then(r => console.log(r))
    })

    // 下载文件。
    download.addEventListener('click', () => {
      // 指定待下载的字节范围。
      const start = 1, end = 5
      client.get('exampledir/exampleobject.txt', {
        headers: {
          // 在请求头If-Modified-Since中指定时间，如果指定的时间早于文件实际修改时间，则下载文件。如果指定的时间等于或者晚于文件实际修改时间，则返回304 Not Modified。
          "If-Modified-Since": new Date("1970-01-01").toGMTString()
          // 在请求头If-Unmodified-Since中指定时间，如果指定的时间等于或者晚于文件实际修改时间，则下载文件。如果指定的时间早于文件实际修改时间，则返回412 Precondition Failed。
          //"If-Unmodified-Since": new Date(1970-01-01).toGMTString()
          // 在请求头If-Match中传入ETag，如果传入的ETag和文件的ETag匹配，则下载文件。如果传入的ETag和文件的ETag不匹配，则返回412 Precondition Failed。
          //"If-Match": '5B3C1A2E0563E1B002CC607C****'
          // 在请求头If-None-Match中传入ETag，如果传入的ETag和文件的ETag不匹配，则下载文件。如果传入的ETag和文件的ETag匹配，则返回304 Not Modified。
          //"If-None-Match": '5B3C1A2E0563E1B002CC607C****'
        },
      }).then(r => {
        if (r.content.length > 0) {                
          const newBlob = new Blob([r.content], { type: r.res.headers['content-type'] });
          const link = document.createElement('a')
          link.href = window.URL.createObjectURL(newBlob)
          link.download = 'foo.txt'
          link.click()
          window.URL.revokeObjectURL(link.href)
        } else {
          console.log('错误码', r.res.status)
          console.log('没有符合条件的下载项')
        }
      })
    })

  

```

## 相关文档
- 关于限定条件下载的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss#getname-file-options)。
- 关于限定条件下载的API接口说明，请参见[GetObject](https://help.aliyun.com/zh/oss/developer-reference/getobject#reference-ccf-rgd-5db)。

[上一篇：范围下载（Browser.js SDK）](/zh/oss/developer-reference/range-download-3)[下一篇：管理文件（Browser.js SDK）](/zh/oss/developer-reference/manage-objects-8/)该文章对您有帮助吗？反馈
  
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