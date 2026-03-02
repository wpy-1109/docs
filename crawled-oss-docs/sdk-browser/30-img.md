# 图片处理（Browser.js SDK）

Source: https://help.aliyun.com/zh/oss/developer-reference/img

---

- 图片处理（Browser.js SDK）-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 图片处理（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
 图片处理是OSS提供的海量、安全、低成本、高可靠的图片处理服务。原始图片上传到OSS后，您可以通过简单的RESTful接口，在任何时间、任何地点、任何互联网设备上对图片进行处理。

## 注意事项
- 当您使用webpack或browserify等打包工具时，请通过npm install ali-oss的方式安装Browser.js SDK。
- 通过浏览器访问OSS时涉及跨域请求，如果未设置跨域规则，浏览器会拒绝跨域访问请求。如果您希望通过浏览器可以正常访问OSS，需要通过OSS设置跨域规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。
- 由于Browser.js SDK通常在浏览器环境下使用，为避免暴露阿里云账号访问密钥（AccessKey ID和AccessKey Secret），强烈建议您使用临时访问凭证的方式执行OSS相关操作。临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。获取临时访问凭证的具体操作，请参见[授权访问（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-6#section-iy3-bfe-7mn)。

## 使用图片处理参数处理图片

### 使用单个图片处理参数处理图片

```

  
    
    Document
  

  
    
    
    
      const client = new OSS({
	authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        refreshSTSToken: async () => {
          // 向您搭建的STS服务获取临时访问凭证。
          const info = await fetch("your_sts_server");
          return {
            accessKeyId: info.accessKeyId,
            accessKeySecret: info.accessKeySecret,
            stsToken: info.stsToken,
          };
        },
        // 刷新临时访问凭证的时间间隔，单位为毫秒。
        refreshSTSTokenInterval: 300000,
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "yourRegion",
      });

      // 将图片缩放为固定宽高100 px。
      async function scale() {
        try {
          // 填写Object完整路径，例如exampledir/exampleobject.jpg。Object完整路径中不能包含Bucket名称。
          const result = await client.signatureUrl("exampledir/exampleobject.jpg", {
            expires: 3600,
            process: "image/resize,m_fixed,w_100,h_100",
          });
          console.log(result);
        } catch (e) {
          console.log(e);
        }
      }

      scale();
    
  

```

### 使用多个图片处理参数处理图片

使用多个图片处理参数处理图片时，多个参数之间以正斜线（/）分隔。

```
!DOCTYPE html>

  
    
    Document
  

  
    
    
    
      const client = new OSS({
        authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        refreshSTSToken: async () => {
          // 向您搭建的STS服务获取临时访问凭证。
          const info = await fetch("your_sts_server");
          return {
            accessKeyId: info.accessKeyId,
            accessKeySecret: info.accessKeySecret,
            stsToken: info.stsToken,
          };
        },
        // 刷新临时访问凭证的时间间隔，单位为毫秒。
        refreshSTSTokenInterval: 300000,
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "oss-cn-hangzhou",
      });

      // 将图片缩放为固定宽高100 px后，再旋转90°。
      async function resize() {
        try {
          // 填写Object完整路径，例如exampledir/exampleobject.jpg。Object完整路径中不能包含Bucket名称。
          const result = await client.signatureUrl("exampledir/exampleobject.jpg", {
            expires: 3600,
            process: "image/resize,m_fixed,w_100,h_100/rotate,90",
          });
          console.log(result);
        } catch (e) {
          console.log(e);
        }
      }

      resize();
    
  

```

## 使用图片样式处理图片
- 创建图片样式。您可以在一个样式（Style）中包含多个图片处理参数，快速实现复杂的图片处理操作。具体操作，请参见[图片样式](https://help.aliyun.com/zh/oss/user-guide/image-styles)。
- 使用图片样式处理图片。
```

  
    
    Document
  

  
    
    
    
      const client = new OSS({
	authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        refreshSTSToken: async () => {
          // 向您搭建的STS服务获取临时访问凭证。
          const info = await fetch("your_sts_server");
          return {
            accessKeyId: info.accessKeyId,
            accessKeySecret: info.accessKeySecret,
            stsToken: info.stsToken,
          };
        },
        // 刷新临时访问凭证的时间间隔，单位为毫秒。
        refreshSTSTokenInterval: 300000,
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "oss-cn-hangzhou",
      });

      // 将图片缩放为固定宽高100 px后，再旋转90°。
      async function style() {
        try {
          // 填写Object完整路径，例如exampledir/exampleobject.jpg。Object完整路径中不能包含Bucket名称。
          const result = await client.signatureUrl("exampledir/exampleobject.jpg", {
            expires: 3600,
            // yourCustomStyleName填写步骤1创建的图片样式名称。
            process: "style/yourCustomStyleName",
          });
          console.log(result);
        } catch (e) {
          console.log(e);
        }
      }

      style();
    
  

```

## 图片处理持久化

图片处理服务默认不保存处理后的图片，您可以通过图片处理持久化操作将处理后的图片保存到原图所在Bucket。

以下代码用于图片处理持久化。

```

  
    
    Document
  

  
    
    
    
      const client = new OSS({
	authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        refreshSTSToken: async () => {
          // 向您搭建的STS服务获取临时访问凭证。
          const info = await fetch("your_sts_server");
          return {
            accessKeyId: info.accessKeyId,
            accessKeySecret: info.accessKeySecret,
            stsToken: info.stsToken,
          };
        },
        // 刷新临时访问凭证的时间间隔，单位为毫秒。
        refreshSTSTokenInterval: 300000,
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "oss-cn-hangzhou",
      });

      // 填写源Object完整路径，例如exampledir/src.png。Object完整路径中不能包含Bucket名称。
      const sourceImage = "exampledir/src.png";
      // 填写图片处理后的目标Object完整路径，例如exampledir/dest.png。Object完整路径中不能包含Bucket名称。
      const targetImage = "exampledir/dest.png";
      async function processImage(processStr, targetBucket) {
        const result = await client.processObjectSave(
          sourceImage,
          targetImage,
          processStr,
          targetBucket
        );
        console.log(result.res.status);
      }

      // 将原图缩放为固定宽高100 px并保存到原图所在Bucket。
      processImage("image/resize,m_fixed,w_100,h_100", "examplebucket");
    
  

           
```

## 生成带图片处理参数的文件签名URL

通过文件URL访问私有权限文件时需要携带签名。OSS不支持在带签名的URL后直接添加图片处理参数。如果您需要对私有权限的图片进行处理，您需要将图片处理参数加入到签名中，代码示例如下：

```

  
    
    Document
  

  
    
    
    
      const client = new OSS({
        authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        refreshSTSToken: async () => {
          // 向您搭建的STS服务获取临时访问凭证。
          const info = await fetch("your_sts_server");
          return {
            accessKeyId: info.accessKeyId,
            accessKeySecret: info.accessKeySecret,
            stsToken: info.stsToken,
          };
        },
        // 刷新临时访问凭证的时间间隔，单位为毫秒。
        refreshSTSTokenInterval: 300000,
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "oss-cn-hangzhou",
      });

      // 生成带图片处理参数的文件签名URL，并设置签名URL的过期时间为600s（最长过期时间为32400s）。
      const signUrl = client.signatureUrl("oss.png", {
        expires: 600,
        process: "image/resize,w_300",
      });
      console.log("signUrl=" + signUrl);
    
  

```

## 图片处理工具

您可以通过可视化图片处理工具[ImageStyleViewer](https://gosspublic.alicdn.com/image/index.html)直观地看到OSS图片处理结果。

[上一篇：使用自定义域名（Browser.js SDK）](/zh/oss/developer-reference/map-custom-domain-names)[下一篇：浏览器的应用（Browser.js SDK）](/zh/oss/developer-reference/application-in-browsers)该文章对您有帮助吗？反馈
  
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