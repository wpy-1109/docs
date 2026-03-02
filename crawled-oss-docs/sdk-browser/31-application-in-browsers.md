# 使用Browser.js SDK从浏览器上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/application-in-browsers

---

- 使用Browser.js SDK从浏览器上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 浏览器的应用（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
 本文介绍浏览器的应用。

## 前提条件
- 已为Bucket配置跨域规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。
- 已搭建STS Server并从客户端获取临时授权信息。具体操作，请参见[搭建STS Server并从客户端获取临时授权信息](https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-browser-js#p-cs5-4y6-kc6)。

## 支持的浏览器

Browser.js SDK支持以下版本的浏览器：
- IE（>=10）和Edge重要 在IE中使用Browser.js SDK之前需要引入promise库。
- Browser.js SDK是通过File API进行文件操作，在一些较低版本的浏览器中运行会出现问题。建议使用第三方插件，通过对OSS API的调用，实现上传文件、下载文件等操作。具体示例，请参见[Web端直传实践](https://help.aliyun.com/zh/oss/use-cases/add-signatures-on-the-client-by-using-javascript-and-upload-data-to-oss#concept-frd-4gy-5db)。
- 主流版本的Chrome/Firefox/Safari
- 主流版本的Android/iOS/WindowsPhone系统默认浏览器

## 通过浏览器上传文件

以下示例代码用于通过浏览器上传文件。示例代码中使用了[Bootstrap](https://getbootstrap.com/)样式。

```

  
    
    Document
    
    
      .form-group {
        margin: 10px;
      }
    
  

  
    
      
      Select file
      
    
    
      
      Store as
      
    
    
      
      
    
    
      
      
        
          0%
        
      
    
    
    
    
      // 填写您的授权服务器地址，例如http://127.0.0.1:8000/sts。
      const appServer = "yourStsServer";
      // 填写Bucket名称，例如examplebucket。
      const bucket = "examplebucket";
      // 填写Bucket所在地域。以华东1（杭州）为例，region填写为oss-cn-hangzhou。
      const region = "oss-cn-hangzhou";

      const urllib = OSS.urllib;

      const applyTokenDo = function (func) {
        const url = appServer;
        return urllib
          .request(url, {
            method: "GET",
          })
          .then(function (result) {
            const creds = JSON.parse(result.data);
            // 通过临时访问凭证创建OSS Client。
            const client = new OSS({
             // yourRegion填写Bucket所在地域。以华东1（杭州）为例，yourRegion填写为oss-cn-hangzhou。
              region: region,
              authorizationV4: true,
              accessKeyId: creds.AccessKeyId,
              accessKeySecret: creds.AccessKeySecret,
              stsToken: creds.SecurityToken,
              bucket: bucket,
            });

            return func(client);
          });
      };

      let currentCheckpoint;
      const progress = async function progress(p, checkpoint) {
        currentCheckpoint = checkpoint;
        const bar = document.getElementById("progress-bar");
        bar.style.width = `${Math.floor(p * 100)}%`;
        bar.innerHTML = `${Math.floor(p * 100)}%`;
      };

      let uploadFileClient;
      const uploadFile = function (client) {
        if (!uploadFileClient || Object.keys(uploadFileClient).length === 0) {
          uploadFileClient = client;
        }

        const file = document.getElementById("file").files[0];
        const key =
          document.getElementById("object-key-file").value.trim() || "object";
        console.log(`${file.name} => ${key}`);
        // 通过multipartUpload上传选中的文件，并通过progress参数设置进度条。
        const options = {
          progress,
          partSize: 100 * 1024,
          meta: {
            year: 2017,
            people: "test",
          },
        };

        return client
          .multipartUpload(key, file, options)
          .then((res) => {
            console.log("upload success: %j", res);
            currentCheckpoint = null;
            uploadFileClient = null;
          })
          .catch((err) => {
            if (uploadFileClient && uploadFileClient.isCancel()) {
              console.log("stop-upload!");
            } else {
              console.error(err);
            }
          });
      };

      window.onload = function () {
        document.getElementById("file-button").onclick = function () {
          applyTokenDo(uploadFile);
        };
      };
    
  

```

## 相关文档

关于浏览器应用的完整示例代码，请参见[GitHub示例](https://github.com/rockuw/oss-in-browser)。

[上一篇：图片处理（Browser.js SDK）](/zh/oss/developer-reference/img)[下一篇：异常处理（Browser.js SDK）](/zh/oss/developer-reference/error-handling)该文章对您有帮助吗？反馈
  
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