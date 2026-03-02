# 使用PHP SDK V2设置和获取文件访问权限

Source: https://help.aliyun.com/zh/oss/developer-reference/manage-file-access

---

- 使用PHP SDK V2设置和获取文件访问权限-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 管理文件访问权限（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何使用PHP SDK V2设置并获取文件的访问权限（ACL）。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要设置Object访问权限，您必须具有`oss:PutObjectAcl`权限；要获取Object访问权限，您必须具有`oss:GetObjectAcl`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 读写权限类型

文件的访问权限（ACL）有以下四种：
| 访问权限 | 描述 | 访问权限值|
| 继承Bucket | 文件遵循存储空间的访问权限。 | oss.ObjectACLDefault|
| 私有 | 文件的拥有者和授权用户有该文件的读写权限，其他用户没有权限操作该文件。 | oss.ObjectACLPrivate|
| 公共读 | 文件的拥有者和授权用户有该文件的读写权限，其他用户只有文件的读权限。请谨慎使用该权限。 | ObjectACLPublicRead|
| 公共读写 | 所有用户都有该文件的读写权限。请谨慎使用该权限。 | oss.ObjectACLPublicReadWrite|

文件的访问权限优先级高于存储空间的访问权限。例如存储空间的访问权限是私有，而文件的访问权限是公共读写，则所有用户都有该文件的读写权限。如果某个文件没有设置过访问权限，则遵循存储空间的访问权限。

## 示例代码

1.设置文件的读写权限

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
    "key" => ['help' => 'The name of the object', 'required' => True],
];

// 构建长选项格式（如 --region:），供 getopt 解析使用
$longopts = array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 检查必填参数是否缺失
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        // 如果缺少必填参数，打印帮助信息并退出
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help\n";
        exit(1);
    }
}

// 提取参数值
$region = $options["region"];
$bucket = $options["bucket"];
$key = $options["key"];

// 从环境变量中加载凭证（AccessKey ID 和 AccessKey Secret）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载默认配置并设置凭证提供者、地域
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);

// 如果指定了 endpoint，则设置自访问地址
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 初始化 OSS 客户端
$client = new Oss\Client($cfg);

// 创建 PutObjectAclRequest 请求对象，设置 Bucket 名称、Object Key 和 ACL 权限类型
$request = new Oss\Models\PutObjectAclRequest($bucket, $key, Oss\Models\ObjectACLType::PUBLIC_READ);

// 发起请求，设置对象的 ACL 为 public-read（公共可读）
$result = $client->putObjectAcl($request);

// 打印响应结果中的状态码和请求 ID
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId
);

```

2.获取文件的读写权限

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 访问域名是可选项 其他服务可以用来访问OSS的域名
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称是必填项
];

// 生成长选项列表 用于解析命令行参数
$longopts = \array_map(function ($key) {
    return "$key:"; // 每个参数后面加冒号 表示需要值
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
$key = $options["key"]; // 对象名称

// 使用环境变量加载凭证信息 AccessKeyId 和 AccessKeySecret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者
$cfg->setCredentialsProvider($credentialsProvider);

// 设置区域
$cfg->setRegion($region);

// 如果提供了访问域名 则设置访问域名
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 创建获取对象ACL的请求对象
$request = new Oss\Models\GetObjectAclRequest(bucket: $bucket, key: $key);

// 调用getObjectAcl方法获取对象的ACL
$result = $client->getObjectAcl($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL . // 请求的唯一标识
    'acl:' . $result->accessControlList->grant // 对象的ACL权限
);

```

## 相关文档
- 关于设置文件读写权限的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutObjectAcl.php)。
- 关于设置文件读写权限的API接口，请参见[PutObjectACL](https://help.aliyun.com/zh/oss/developer-reference/putobjectacl#reference-fs3-gfw-wdb)。
- 关于获取文件读写权限的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetObjectAcl.php)。
- 关于获取文件读写权限的API接口，请参见[GetObjectACL](https://help.aliyun.com/zh/oss/developer-reference/getobjectacl#reference-lzc-24w-wdb)。

[上一篇：管理存储空间读写权限（PHP SDK V2）](/zh/oss/developer-reference/php-v2-manage-the-acl-of-a-bucket)[下一篇：Bucket Policy（PHP SDK V2）](/zh/oss/developer-reference/php-v2-configure-and-manage-bucket-policies)该文章对您有帮助吗？反馈
  
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