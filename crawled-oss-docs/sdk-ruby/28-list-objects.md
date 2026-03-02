# 使用RubySDK列举存储空间下的文件和目录

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects

---

- 使用RubySDK列举存储空间下的文件和目录-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 列举文件（Ruby SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何列举指定存储空间下（Bucket）的所有文件（Object）、指定前缀的文件、指定文件名后的文件等。

## 列举所有文件

以下代码用于列举目标存储空间examplebucket的所有文件。

```
require 'aliyun/oss'

client = Aliyun::OSS::Client.new(
  # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)

# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')
# 列举所有文件。
objects = bucket.list_objects
objects.each { |o| puts o.key }     
```

## 列举指定前缀的文件

以下代码用于通过prefix参数列举Bucket中包含指定前缀的文件。

```
require 'aliyun/oss'

client = Aliyun::OSS::Client.new(
  # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)

# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')
# 列出前缀为'my-'的所有文件。
objects = bucket.list_objects(:prefix => 'my-')
objects.each { |o| puts o.key }   
```

## 列举指定文件名后的文件

以下代码用于列举文件名称字典序排在指定字符串（marker）之后的文件。

```
require 'aliyun/oss'

client = Aliyun::OSS::Client.new(
  # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)

# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')
# 列出前缀为'my-'且字母序在'my-object'之后的所有文件。
objects = bucket.list_objects(:prefix => 'my-', :marker => 'my-object')
objects.each { |o| puts o.key }      
```

## 文件夹功能

OSS没有文件夹的概念，所有元素都是以文件来存储。创建文件夹本质上来说是创建了一个大小为0并以正斜线（/）结尾的文件。这个文件可以被上传和下载，控制台会对以正斜线（/）结尾的文件以文件夹的方式展示。

假设某个Bucket中有如下文件：

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

通过调用`list_dir`函数来列举指定目录下的文件和子目录：

```
require 'aliyun/oss'

def list_dir(dir, bucket)
  objects = bucket.list_objects(:prefix => dir, :delimiter => '/')
  objects.each do |obj|
    if obj.is_a?(Aliyun::OSS::Object) # object
      puts "Object: #{obj.key}"
    else # common prefix
      puts "SubDir: #{obj}"
      list_dir(obj, bucket) # 递归调用list_dir处理子目录。
    end
  end
end

client = Aliyun::OSS::Client.new(
  # Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)

# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')

list_dir('foo/', bucket)          
```

返回结果如下：

```
SubDir: foo/bar/
Object: foo/bar/
Object: foo/bar/3.txt
Object: foo/bar/oss.jpg
SubDir: foo/hello/
Object: foo/hello/
Object: foo/hello/001.avi
Object: foo/hello/007.avi
Object: foo/            
```

## 相关文档

关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)。

[上一篇：管理文件元数据（Ruby SDK）](/zh/oss/developer-reference/manage-object-metadata)[下一篇：拷贝文件（Ruby SDK）](/zh/oss/developer-reference/copy-objects)该文章对您有帮助吗？反馈
  
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