# 使用RubySDK的resumable_upload实现断点续传上传

Source: https://help.aliyun.com/zh/oss/developer-reference/resumable-download-1

---

- 使用RubySDK的resumable_upload实现断点续传上传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 断点续传上传（Ruby SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
通过断点续传上传的方式将文件上传到OSS前，您可以指定断点记录点。上传过程中，如果出现网络异常或程序崩溃导致文件上传失败时，将从断点记录处继续上传未上传完成的部分。

## 实现方法

断点续传上传将要上传的文件分成若干个分片（Part）分别上传，所有分片都上传完成后，将所有分片合并成完整的文件，完成整个文件的上传。

您可以通过`Bucket#resumable_upload`方法来实现断点续传上传。该方法包含以下参数：
| 参数 | 描述 | 是否必选 | 默认值|
| key | 上传至OSS的文件完整路径。 | 是 | 无|
| file | 待上传的本地文件完整路径。
说明 
上传过程中如果本地文件ETag值发生变化，会导致上传失败。 | 是 | 无|
| :cpt_file | 指定用于记录断点信息的文件，您需要对该文件有写入权限。
说明 - 如果上传过程中某一分片上传失败，再次上传时会从.cpt文件中记录的断点继续上传。再次调用Bucket#resumable_upload时需指定与上次相同的.cpt文件。上传完成后，.cpt文件被删除。
- .cpt文件不仅记录了上传的中间状态信息，还附带校验功能。.cpt文件不允许编辑。如果.cpt文件损坏，则无法继续上传。 | 否 | 本地文件同目录下的`file.cpt`，其中`file`表示本地文件名称|
| :disable_cpt | 上传过程中是否记录上传进度。取值如下：
- true：上传过程中不记录上传进度，失败后无法进行续传。
- false：上传过程中记录上传进度，失败后从断点记录处进行续传。 | 否 | false|
| :part_size | 指定每个分片的大小。 | 否 | 4 MB|
| &block | 调用时传递了block，则上传进度会交由block处理。 | 否 | 无|

## 示例代码

以下代码用于断点续传上传。

```
require 'aliyun/oss'

client = Aliyun::OSS::Client.new(
  # Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。
  endpoint: 'https://oss-cn-hangzhou.aliyuncs.com',
  # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
  access_key_id: ENV['OSS_ACCESS_KEY_ID'],
  access_key_secret: ENV['OSS_ACCESS_KEY_SECRET']
)
# 填写Bucket名称，例如examplebucket。
bucket = client.get_bucket('examplebucket')
# key填写Object完整路径，Object完整路径中不能包含Bucket名称，例如exampledir/example.zip。
# file填写本地文件的完整路径，例如/tmp/example.zip。
bucket.resumable_upload('exampledir/example.zip', '/tmp/example.zip') do |p|
  puts "Progress: #{p}"
end

bucket.resumable_upload(
  'exampledir/example.zip', '/tmp/example.zip',
  :part_size => 100 * 1024, :cpt_file => '/tmp/example.zip.cpt') { |p|
  puts "Progress: #{p}"
}
```

[上一篇：流式上传（Ruby SDK）](/zh/oss/developer-reference/streaming-upload)[下一篇：追加上传（Ruby SDK）](/zh/oss/developer-reference/append-upload-1)该文章对您有帮助吗？反馈
  
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