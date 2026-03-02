# 使用Browser.js SDK列举存储空间的文件和目录

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects-16

---

- 使用Browser.js SDK列举存储空间的文件和目录-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 列举文件（Browser.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何列举指定存储空间下（Bucket）的所有文件（Object）以及指定目录下的文件和子目录。

## 注意事项
- 当您使用webpack或browserify等打包工具时，请通过npm install ali-oss的方式安装Browser.js SDK。
- 通过浏览器访问OSS时涉及跨域请求，如果未设置跨域规则，浏览器会拒绝跨域访问请求。如果您希望通过浏览器可以正常访问OSS，需要通过OSS设置跨域规则。具体操作，请参见[准备工作](https://help.aliyun.com/zh/oss/developer-reference/installation#section-lc9-9ju-8da)。
- 由于Browser.js SDK通常在浏览器环境下使用，为避免暴露阿里云账号访问密钥（AccessKey ID和AccessKey Secret），强烈建议您使用临时访问凭证的方式执行OSS相关操作。临时访问凭证包括临时访问密钥（AccessKey ID和AccessKey Secret）和安全令牌（SecurityToken）。获取临时访问凭证的具体操作，请参见[授权访问（Browser.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/authorize-access-6#section-iy3-bfe-7mn)。

## 列举Bucket下的所有文件

通过`list`函数列举当前Bucket下的所有文件：

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

## 列举指定目录下的文件和子目录

OSS没有文件夹的概念，所有元素都是以Object来存储。创建文件夹本质上是创建一个文件名以正斜线（/）结尾，大小为0 KB的Object。这个Object可以被上传和下载，只是控制台会对以正斜线（/）结尾的Object以文件夹的方式展示。您可以通过Delimiter和Prefix参数模拟文件夹功能：
- 如果把Prefix设为某个文件夹名，就可以列举以此Prefix开头的文件，即该文件夹下递归的所有的文件和子文件夹（目录）。
- 如果再把Delimiter设置为正斜线（/）时，返回值就只列举该文件夹下的文件和子文件夹（目录），该文件夹下的子文件名（目录）返回在SubDir部分，子文件夹下递归的文件和文件夹不被显示。

假设某个Bucket中存放了如下文件：

```
foo/x
foo/y
foo/bar/a
foo/bar/b
foo/hello/C/1
foo/hello/C/2
...
foo/hello/C/9999
            
```

通过`listDir`函数列举指定目录下的文件和子目录：

```

  
    
    
    Document
    
  
  
    
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

      async function listDir(dir) {
        try {
          let result = await client.list({
            prefix: dir,
            // 设置正斜线（/）为文件夹的分隔符。
            delimiter: "/",
          });

          result.prefixes.forEach(function (subDir) {
            console.log("SubDir: %s", subDir);
          });
          result.objects.forEach(function (obj) {
            console.log("Object: %s", obj.name);
          });
        } catch (e) {
          console.log(e);
        }
      }

      listDir();
    
  

```

返回的文件列表如下：

```
> listDir('foo/')
=> SubDir: foo/bar/
   SubDir: foo/hello/
   Object: foo/x
   Object: foo/y

> listDir('foo/bar/')
=> Object: foo/bar/a
   Object: foo/bar/b

> listDir('foo/hello/C/')
=> Object: foo/hello/C/1
   Object: foo/hello/C/2
   ...
   Object: foo/hello/C/9999            
```

## 相关文档

关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)。

[上一篇：判断文件是否存在（Browser.js SDK）](/zh/oss/developer-reference/determine-whether-an-object-exists-4)[下一篇：重命名文件（Browser.js SDK）](/zh/oss/developer-reference/rename-an-object)该文章对您有帮助吗？反馈
  
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