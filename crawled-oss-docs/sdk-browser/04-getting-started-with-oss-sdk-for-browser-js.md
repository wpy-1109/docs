# 使用Browser.js SDK上传下载和列举文件

Source: https://help.aliyun.com/zh/oss/developer-reference/getting-started-with-oss-sdk-for-browser-js

---

- 使用Browser.js SDK上传下载和列举文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 快速入门（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何在Browser.js SDK中快速使用OSS服务，包括上传文件、下载文件和查看文件列表等。

## 前提条件
- 已安装Browser.js SDK。具体操作，请参见[安装（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/installation)。
- 已配置跨域资源共享（CORS）规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。

## 注意事项
- 目前浏览器中不允许执行Bucket相关的操作，仅允许执行Object相关的操作，例如PutObject、GetObject等。
- 由于Browser.js SDK通常在浏览器环境下使用，为避免暴露阿里云账号访问密钥（AccessKey ID和AccessKey Secret），强烈建议您使用临时访问凭证的方式执行OSS相关操作。临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。获取临时访问凭证的具体操作，请参见[授权访问（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-6#section-iy3-bfe-7mn)。

## 常见操作

以下为Browser.js SDK的常见操作。

### 搭建STS Server并从客户端获取临时授权信息
- 搭建STS Server。为方便您搭建STS Server，OSS提供了多个语言SDK demo。[Node.js](https://github.com/ali-sdk/ali-oss/blob/master/example/server/app.js#L9)
- [PHP](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20220831/ozpv/sts-server.zip)
- [Java](https://gosspublic.alicdn.com/AppTokenServerDemo.zip?spm=5176.doc31920.2.6.Fve3RI&file=AppTokenServerDemo.zip)
- [Ruby](https://github.com/rockuw/sts-app-server?spm=5176.doc31920.2.7.Fve3RI)
重要 
以上demo仅供参考，在具体的生产环境中，请自行开发鉴权等业务所需代码。
- 通过浏览器向搭建的STS服务发起请求，获取STS临时授权信息。 
```

  
    
    Document
  
  
    
    
      // OSS.urllib是SDK内部封装的发送请求的逻辑，开发者可以使用任何发送请求的库向your_sts_server发送请求。
      // your_sts_server需要填写步骤1中您搭建的STS Server的IP地址或域名。
      OSS.urllib.request(
        "your_sts_server",
        { method: "GET" },
        (err, response) => {
          if (err) {
            return alert(err);
          }
          try {
            result = JSON.parse(response);
          } catch (e) {
            errmsg = "parse sts response info error: " + e.message;
            return alert(errmsg);
          }
          console.log(result);
        }
      );
    
  

                            
```

### 上传文件

使用multipartUpload接口上传文件。

```

  
    
    Document
  

  
    上传
    
    
    
    
      const client = new OSS({
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "yourRegion",
        authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: "yourAccessKeyId",
        accessKeySecret: "yourAccessKeySecret",
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: "yourSecurityToken",
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
      });

      const headers = {
        // 指定该Object被下载时的网页缓存行为。
        "Cache-Control": "no-cache",
        // 指定该Object被下载时的名称。
        "Content-Disposition": "example.txt",
        // 指定过期时间，单位为毫秒。
        Expires: "1000",
        // 指定Object的存储类型。
        "x-oss-storage-class": "Standard",
        // 指定Object标签，可同时设置多个标签。
        "x-oss-tagging": "Tag1=1&Tag2=2",
        // 指定初始化分片上传时是否覆盖同名Object。此处设置为true，表示禁止覆盖同名Object。
        "x-oss-forbid-overwrite": "true",
      };

      // 指定上传到examplebucket的Object名称，例如exampleobject.txt。
      const name = "exampleobject.txt";
      // 获取DOM。
      const submit = document.getElementById("submit");
      const options = {
        // 获取分片上传进度、断点和返回值。
        progress: (p, cpt, res) => {
          console.log(p);
        },
        // 设置并发上传的分片数量。
        parallel: 4,
        // 设置分片大小。默认值为1 MB，最小值为100 KB，最大值为5 GB。最后一个分片的大小允许小于100 KB。
        partSize: 1024 * 1024,
        // headers,
        // 自定义元数据，通过HeadObject接口可以获取Object的元数据。
        meta: { year: 2020, people: "test" },
        mime: "text/plain",
      };

      // 监听按钮。
      submit.addEventListener("click", async () => {
        try {
          const data = document.getElementById("file").files[0];
          // 分片上传。
          const res = await client.multipartUpload(name, data, {
            ...options,
            // 设置上传回调。
            // 如果不涉及回调服务器，请删除callback相关设置。
            callback: {
              // 设置回调请求的服务器地址。
              url: "http://examplebucket.aliyuncs.com:23450",
              // 设置回调请求消息头中Host的值，即您的服务器配置Host的值。
              host: "yourHost",
              /* eslint no-template-curly-in-string: [0] */
              // 设置发起回调时请求body的值。
              body: "bucket=${bucket}&object=${object}&var1=${x:var1}",
              // 设置发起回调请求的Content-Type。
              contentType: "application/x-www-form-urlencoded",
              customValue: {
                // 设置发起回调请求的自定义参数。
                var1: "value1",
                var2: "value2",
              },
            },
          });
          console.log(res);
        } catch (err) {
          console.log(err);
        }
      });
    
  

```

### 下载文件

采用签名URL的方式生成文件的下载链接，您只需要单击链接即可下载文件。

```

  
    
    Document
  

  
    
    
    
      const client = new OSS({
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
        region: "yourRegion",
        authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: "yourAccessKeyId",
        accessKeySecret: "yourAccessKeySecret",
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: "yoursecurityToken",
        // 填写Bucket名称。
        bucket: "examplebucket",
      });

      // 配置响应头实现通过URL访问时自动下载文件，并设置下载后的文件名。
      const filename = "examplefile.txt";
      const response = {
        "content-disposition": `attachment; filename=${encodeURIComponent(
          filename
        )}`,
      };
      // 填写Object完整路径。Object完整路径中不能包含Bucket名称。
      const url = client.signatureUrl("exampleobject.txt", { response });
      console.log(url);
    
  

```

### 列举文件

以下代码用于列举文件。

```

  
    
    
    Document
    
  
  
          
      const client = new OSS({
        // yourRegion填写Bucket所在地域。以华东1（杭州）为例，yourRegion填写为oss-cn-hangzhou。
        region: "yourRegion",
        authorizationV4: true,
        // 从STS服务获取的临时访问密钥（AccessKey ID和AccessKey Secret）。
        accessKeyId: 'yourAccessKeyId',
        accessKeySecret: 'yourAccessKeySecret',
        // 从STS服务获取的安全令牌（SecurityToken）。
        stsToken: 'yourSecurityToken',
        // 填写Bucket名称，例如examplebucket。
        bucket: "examplebucket",
      });

      async function list(dir) {
        try {
          // 默认最多返回1000个文件。
          let result = await client.list();
          console.log(result);

          // 从上一次list操作读取的最后一个文件的下一个文件开始继续获取文件列表。
          if (result.isTruncated) {
            result = await client.list({ marker: result.nextMarker });
          }

          // 列出前缀为'ex'的文件。
          result = await client.list({
            prefix: "ex",
          });
          console.log(result);

          // 列出前缀为'ex'且文件名称字母序'example'之后的文件。
          result = await client.list({
            prefix: "ex",
            marker: "example",
          });
          console.log(result);
        } catch (e) {
          console.log(e);
        }
      }

      list();
    
  

          
```

[上一篇：授权访问（Browser.js SDK）](/zh/oss/developer-reference/authorize-access-6)[下一篇：上传文件（Browser.js SDK）](/zh/oss/developer-reference/upload-objects-17/)该文章对您有帮助吗？反馈
  
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