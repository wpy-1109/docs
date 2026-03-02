# 使用PHP SDK V2创建存储空间

Source: https://help.aliyun.com/zh/oss/developer-reference/php-v2-create-bucket

---

- 使用PHP SDK V2创建存储空间-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 创建存储空间（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
存储空间（Bucket）是对象（Object）的容器，您上传的文件都将以对象的形式放在存储空间中。本文介绍如何创建存储空间。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要创建存储空间，您必须有`oss:PutBucket`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。
- 北京时间2025年10月13日10:00:00起，OSS逐步调整所有地域通过API、SDK、ossutil创建Bucket时默认开启[阻止公共访问](https://help.aliyun.com/zh/oss/user-guide/block-public-access)。各个地域的生效变更时间，请参见[公告说明](https://www.aliyun.com/notice/117116)。开启后，不允许创建公共访问权限，包括公共读或者公共读写ACL、以及公共访问语义的Bucket Policy。如果您的业务有公共访问需求，可在Bucket创建后关闭阻止公共访问。
说明 
本文以创建有地域属性Bucket为例。如果您希望通过以下代码创建无地域属性Bucket，需要将endpoint替换为`https://oss-rg-china-mainland.aliyuncs.com`。此外，无地域属性Bucket的存储类型仅支持标准存储，数据容灾类型仅支持本地冗余存储，且不支持配置资源组。关于无地域属性Bucket的更多信息，请参见[存储空间地域属性](https://help.aliyun.com/zh/oss/user-guide/region-attribute-of-buckets#main-2319370)。

## 示例代码

您可以使用以下代码创建存储空间。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项，存储空间所在的区域，例如 oss-cn-hangzhou。
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项，其他服务可以用来访问OSS的域名。
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项。
];

// 生成长选项数组，用于解析命令行参数
$longopts = \array_map(function ($key) {
    return "$key:"; // 每个参数后面加冒号，表示需要值
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts); 

// 检查必填参数是否缺失
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help"; // 提示用户缺少必填参数
        exit(1); 
    }
}

// 获取命令行参数值
$region = $options["region"]; // 存储空间所在区域
$bucket = $options["bucket"]; // 存储空间名称

// 使用环境变量加载凭证信息（AccessKeyId 和 AccessKeySecret）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); 

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault(); 
$cfg->setCredentialsProvider($credentialsProvider); //  设置凭证提供者
$cfg->setRegion($region); // 设置区域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 如果提供了终端节点，则设置终端节点
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg); //  创建OSS客户端实例

// 创建存储空间请求对象
$request = new Oss\Models\PutBucketRequest($bucket); //  创建存储空间请求对象

// 调用putBucket方法创建存储空间
$result = $client->putBucket($request); // 调用putBucket方法创建存储空间

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . //  HTTP响应状态码
    'request id:' . $result->requestId // Request ID. 请求的唯一标识
);

```

## 相关文档
- 关于创建存储空间的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucket.php)。
- 关于创建存储空间的API接口，请参见[PutBucket](https://help.aliyun.com/zh/oss/developer-reference/putbucket#doc-api-Oss-PutBucket)。

[上一篇：存储空间（PHP SDK V2）](/zh/oss/developer-reference/manage-buckets-using-oss-sdk-for-php-v2/)[下一篇：列举存储空间（PHP SDK V2）](/zh/oss/developer-reference/php-v2-list-buckets)该文章对您有帮助吗？反馈
  
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