# iOS SDK异常响应错误码详解

Source: https://help.aliyun.com/zh/oss/developer-reference/handle-exceptions

---

- iOS SDK异常响应错误码详解-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 异常响应（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
iOS SDK 中发生的异常分为两类：ClientError 和 ServerError。

ClientError 指参数错误、网络错误等。ServerError 指 OSS Server 返回的异常响应。
| Error类型 | Error Domain | Code | UserInfo | 描述 | 解决方法|
| ClientError | com.aliyun.oss.clientError | 0 | OSSClientErrorCodeNetworkingFailWithResponseCode0 | 连接异常 | 请检查网络连接后重试。|
| 1 | OSSClientErrorCodeSignFailed | 签名失败 | 请参见[签名错误问题排查](https://help.aliyun.com/zh/oss/developer-reference/faq-24#concept-op3-h2s-xgb)进行排查。|
| 2 | OSSClientErrorCodeFileCantWrite | 文件无法写入 | 可能是指定的断点记录文件的路径或者下载的文件路径不合法。请修改对应的文件路径后重试。|
| 3 | OSSClientErrorCodeInvalidArgument | 参数非法 | 参数格式不符合要求，请参见[API概览](https://help.aliyun.com/zh/oss/developer-reference/list-of-operations-by-function#reference-wrz-l2q-tdb)中相应的API，填写正确的参数格式。|
| 4 | OSSClientErrorCodeNilUploadid | 未获取到断点续传任务的uploadId | 检查参数，例如objectMeta无误后，请尝试重新获取uploadId。|
| 5 | OSSClientErrorCodeTaskCancelled | 任务被取消 | 请检查代码中任务取消逻辑是否正确，或网络连接是否异常。|
| 6 | OSSClientErrorCodeNetworkError | 网络异常 | 请检查网络连接后重试。|
| 7 | OSSClientErrorCodeInvalidCRC | CRC校验失败 | 传输过程中数据不一致。请检查文件是否被修改。|
| 8 | OSSClientErrorCodeCannotResumeUpload | 断点续传上传失败，无法继续上传 | 上传过程中文件发生了更改、导致文件大小不一致。因此文件上传过程中请勿修改文件。|
| 9 | OSSClientErrorCodeExcpetionCatched | 异常捕获 | 请结合具体的报错信息进行排查。|
| ServerError | com.aliyun.oss.serverError | (-1 * httpResponse. statusCode) | dict | 解析响应XML得到的Dictionary | 可能是服务端遇到了错误无法完成请求，请参见[OSS错误码](https://help.aliyun.com/zh/oss/user-guide/overview-14#section-zzm-z5v-zi9)进行排查。|

[上一篇：授权访问（iOS SDK）](/zh/oss/developer-reference/authorize-access-4)[下一篇：常见问题（iOS SDK）](/zh/oss/developer-reference/faq-27)该文章对您有帮助吗？反馈
  
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