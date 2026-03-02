# BrowserJS分片上传全流程操作实践

Source: https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-11

---

- BrowserJS分片上传全流程操作实践-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 分片上传（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS提供的分片上传（MultipartUpload）功能，将要上传的较大文件（Object）分成多个分片（Part）来分别上传，上传完成后再调用CompleteMultipartUpload接口将这些Part组合成一个Object来达到断点续传的效果。

## 注意事项
- 在分片上传之前，请确保您已了解该功能。更多信息，请参见[分片上传](https://help.aliyun.com/zh/oss/user-guide/multipart-upload)。
- 当您使用webpack或browserify等打包工具时，请通过npm install ali-oss的方式安装Browser.js SDK。
- 通过浏览器访问OSS时涉及跨域请求，如果未设置跨域规则，浏览器会拒绝跨域访问请求。如果您希望通过浏览器可以正常访问OSS，需要通过OSS设置跨域规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。
- 由于Browser.js SDK通常在浏览器环境下使用，为避免暴露阿里云账号访问密钥（AccessKey ID和AccessKey Secret），强烈建议您使用临时访问凭证的方式执行OSS相关操作。临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。获取临时访问凭证的具体操作，请参见[授权访问（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-6#section-iy3-bfe-7mn)。

## 分片上传完整示例代码

当需要上传的文件大小较大时，您可以通过[MultipartUpload](https://help.aliyun.com/zh/oss/introduction-2#concept-eg1-jmx-wdb)接口进行分片上传。分片上传是指将要上传的文件分成多个数据块（Part）来分别上传。当其中一些分片上传失败后，OSS将保留上传进度记录，再次重传时只需要上传失败的分片，而不需要重新上传整个文件。
重要 
通常在文件大于100 MB的情况下，建议采用分片上传的方法，通过断点续传和重试，提高上传成功率。如果在文件小于100 MB的情况下使用分片上传，且partSize设置不合理的情况下，可能会出现无法完整显示上传进度的情况。对于小于100 MB的文件，建议使用简单上传的方式。

以下代码以分片上传的方式将文件上传至examplebucket下的exampleobject.txt文件。

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

在使用MultipartUpload接口时，如果遇到`ConnectionTimeoutError`超时问题，业务方需自行处理超时逻辑。例如通过缩小分片大小、增加超时时间、重试请求或者捕获`ConnectionTimeoutError`错误等方法处理超时。更多信息，请参见[网络错误处理](https://help.aliyun.com/zh/oss/network-connection-timeout-handling#concept-lhz-qvt-4fb)。

## 取消分片上传事件

您可以调用`client.abortMultipartUpload`方法来取消分片上传事件。当一个分片上传事件被取消后，无法再使用该uploadId进行任何操作，已上传的分片数据会被删除。

以下代码用于取消分片上传事件：

```

  
    
    Document
  

  
    上传
    中断
    
    
    
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
      // 生成用于分片上传的100 MB大小的文件。
      const fileContent = Array(1024 * 1024 * 100)
        .fill("a")
        .join("");
      const file = new File([fileContent], "multipart-upload-file");
      // 设置上传到examplebucket的Object名称，例如exampleobject.txt。
      const name = "exampleobject.txt";
      // 设置中断点。
      let abortCheckpoint;
      // 获取DOM。
      const submit = document.getElementById("submit");
      const abort = document.getElementById("abort");

      // 监听上传按钮，单击“上传”后开始分片上传。
      submit.addEventListener("click", async () => {
        try {
          const res = await client.multipartUpload(name, file, {
            progress: (p, cpt, res) => {
              // 为中断点赋值。
              abortCheckpoint = cpt;
              // 获取上传进度。
              console.log(p);
            },
          });
        } catch (err) {
          console.log(err);
        }
      });
      // 监听中断按钮。
      abort.addEventListener("click", () => {
        // 中断分片上传。
        client.abortMultipartUpload(
          abortCheckpoint.name,
          abortCheckpoint.uploadId
        );
      });
    
  

```

## 列举已上传的分片

调用`client.listParts`方法列举出指定uploadId下所有已经上传成功的分片。

以下代码用于列举已上传的分片：

```

  
    
    Document
  

  
    上传
    列举已上传的分片
    
    
    
      const client = new OSS({
         // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
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
      // 生成用于分片上传的100 MB大小的文件。
      const fileContent = Array(1024 * 1024 * 100)
        .fill("a")
        .join("");
      const file = new File([fileContent], "multipart-upload-file");
      // 设置上传到examplebucket的Object名称，例如exampleobject.txt。
      const name = "exampleobject.txt";
      // 设置中断点。
      let abortCheckpoint;

      // 获取DOM。
      const submit = document.getElementById("submit");
      const check = document.getElementById("check");

      // 监听按钮。
      submit.addEventListener("click", async () => {
        try {
          const res = await client.multipartUpload(name, file, {
            progress: (p, cpt, res) => {
              // 为中断点赋值。
              abortCheckpoint = cpt;
              // 获取上传进度。
              console.log("progress=====", p);
            },
          });
        } catch (err) {
          console.log(err);
        }
      });
      // 监听按钮。
      check.addEventListener("click", async () => {
        // 列举已上传的分片。
        const result = await client.listParts(name, abortCheckpoint.uploadId);
        console.log(result);
      });
    
  

```

## 列举分片上传事件

调用`client.listUploads`方法列举出所有执行中的分片上传事件，即已初始化但尚未完成或已取消的分片上传事件。

以下代码用于列举分片上传事件：

```

  
    
    Document
  

  
    列举分片上传事件
    
    
    
      const client = new OSS({
         // yourRegion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。
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
      // 获取DOM。
      const check = document.getElementById("check");

      // 监听按钮。
      check.addEventListener("click", async () => {
        // 获取所有已初始化但尚未完成或已取消的分片上传事件。
        const result = await client.listUploads({ "max-uploads": 100 });
        console.log("uploads", result.uploads);
      });
    
  

```

## 相关文档
- 关于分片上传的完整示例代码，请参见[GitHub示例](https://github.com/ali-sdk/ali-oss#multipartuploadname-file-options)。
- Browser.js SDK分片上传调用的方法`multipartUpload`中封装了三个API接口，详情如下：关于初始化分片上传事件的API接口说明，请参见[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)。
- 关于分片上传Part的API接口说明，请参见[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)。
- 关于完成分片上传的API接口说明，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。
- 关于取消分片上传事件的API接口说明，请参见[AbortMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)。
- 关于列举已上传分片的API接口说明，请参见[ListParts](https://help.aliyun.com/zh/oss/developer-reference/listparts#reference-hzm-1zx-wdb)。
- 关于列举所有执行中的分片上传事件（即已初始化但尚未完成或已取消的分片上传事件）的API接口说明，请参见[ListMultipartUploads](https://help.aliyun.com/zh/oss/developer-reference/listmultipartuploads#reference-hj2-3wx-wdb)。

## 常见问题

### 报错PLease set the etag of expose-headers in Oss.如何处理？
- 问题原因未正确设置跨域。
- 解决方法您需要为当前Bucket设置跨域。设置跨域规则时需要暴露常见Header（x-oss-request-id和ETag）。具体步骤，请参见[跨域设置](https://help.aliyun.com/zh/oss/user-guide/cors-settings#concept-bwn-tjd-5db)。

### 报错The operation is not supported for this resource.如何处理？
- 问题原因您在调用CompleteMultipartUpload接口时设置了Object存储类型。
- 解决方法不支持在分片上传过程中调用CompleteMultipartUpload时设置Object存储类型。如果您需要在分片上传过程中指定Object存储类型，您需要在调用InitiateMultipartUpload时进行设置。

[上一篇：追加上传（Browser.js SDK）](/zh/oss/developer-reference/append-upload-3)[下一篇：断点续传上传（Browser.js SDK）](/zh/oss/developer-reference/resumable-upload-9)该文章对您有帮助吗？反馈
  
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