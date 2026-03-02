# 使用PHP SDK V2管理数据复制

Source: https://help.aliyun.com/zh/oss/developer-reference/data-replication-using-oss-sdk-for-php-v2

---

- 使用PHP SDK V2管理数据复制-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 数据复制（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
数据复制是以异步（近实时）方式将源Bucket中的文件（Object）以及对Object的创建、更新和删除等操作自动复制到目标Bucket。OSS支持跨区域复制（Cross-Region Replication）和同区域复制（Same-Region Replication）。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 阿里云账号默认拥有数据复制的相关权限。如果您希望通过RAM用户或者STS的方式执行数据复制相关操作，例如：开启数据复制，您必须拥有`oss:PutBucketReplication`权限。
- 开启或关闭数据复制时间控制（RTC）功能，您必须拥有`oss:PutBucketRtc`权限。
- 查看数据复制规则，您必须拥有`oss:GetBucketReplication`权限。
- 查看可复制的目标地域，您必须拥有`oss:GetBucketReplicationLocation`权限。
- 查看数据复制进度，您必须拥有`oss:GetBucketReplicationProgress`权限。
- 关闭数据复制，您必须拥有`oss:DeleteBucketReplication`权限

## 示例代码

### 开启数据复制
重要 
开启数据复制前，请确保源存储空间与目标存储空间同时处于非版本化或已启用版本控制状态。

以下代码用于开启数据复制，将源Bucket中的数据复制到相同或不同地域下的目标Bucket。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
    "target-bucket" => ['help' => 'The name of the target bucket', 'required' => True],
    "target-location" => ['help' => 'The location of the target bucket', 'required' => True],
];

// 构建 getopt 所需的长选项数组格式：如 ["region:", "endpoint:", ...]
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 获取命令行传入的参数
$options = getopt("", $longopts);

// 检查所有必填参数是否都已提供，若缺失则输出错误信息并退出
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

// 提取命令行参数值
$region = $options["region"];
$bucket = $options["bucket"];
$targetBucket = $options["target-bucket"];
$targetLocation = $options["target-location"];

// 使用环境变量中的凭证信息（例如 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者、区域和可选的 Endpoint
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 构造 PutBucketReplication 请求对象
$request = new Oss\Models\PutBucketReplicationRequest(
    bucket: $bucket,
    replicationConfiguration: new Oss\Models\ReplicationConfiguration(
        rules: array(
            new Oss\Models\ReplicationRule(
                destination: new Oss\Models\ReplicationDestination(
                    bucket: $targetBucket,
                    location: $targetLocation,
                ),
                rtc: new Oss\Models\ReplicationTimeControl(
                    status: 'enabled' // 启用复制时间控制（RTC）
                )
            )
        )
    )
);

// 执行请求并获取结果
$result = $client->putBucketReplication($request);

// 输出响应的状态码、请求ID和复制规则ID
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId . PHP_EOL .
    'replication rule id:' . $result->replicationRuleId
);
```

### 查看数据复制规则

以下代码用于查看Bucket的数据复制规则。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
];

// 将参数键转换为 getopt 所需的格式（如："region:"）
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 获取命令行传入的长选项参数
$options = getopt("", $longopts);

// 遍历所有参数定义，检查必填项是否都已提供
foreach ($optsdesc as $key => $value) {
    // 如果是必填项且未提供，则输出错误信息并退出
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

// 提取命令行参数中的 region 和 bucket 名称
$region = $options["region"];
$bucket = $options["bucket"];

// 从环境变量中加载访问凭证（如 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载 SDK 默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证、区域以及可选的自定义 Endpoint
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 构建 GetBucketReplication 请求对象
$request = new Oss\Models\GetBucketReplicationRequest(bucket: $bucket);

// 发送请求并获取响应结果
$result = $client->getBucketReplication($request);

// 输出响应的状态码、请求 ID 和复制规则
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId . PHP_EOL .
    'replication config:' . var_export($result->replicationConfiguration, true)
);
```

### 设置数据复制时间控制（RTC）

以下代码用于为已有的跨区域复制规则开启或关闭数据复制时间控制（RTC）功能。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
    "rule-id" => ['help' => 'The replication rule id of the bucket', 'required' => True],
];

// 将参数键转换为 getopt 所需的格式（带冒号表示需要值）
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 获取命令行传入的长选项参数
$options = getopt("", $longopts);

// 检查所有必填参数是否都已提供
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

// 提取命令行参数中的 region、bucket 和 rule-id
$region = $options["region"];
$bucket = $options["bucket"];
$ruleId = $options["rule-id"];

// 从环境变量中加载访问凭证（如 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载 SDK 默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者、区域和可选的自定义 Endpoint
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 构建 PutBucketRtcRequest 请求对象
$request = new Oss\Models\PutBucketRtcRequest(
    bucket: $bucket,
    rtcConfiguration: new Oss\Models\RtcConfiguration(
        rtc: new Oss\Models\ReplicationTimeControl(
            status: 'disabled' // 禁用 RTC 功能
        ),
        id: $ruleId // 指定要修改的复制规则ID
    )
);

$result = $client->putBucketRtc($request);

// 输出响应的状态码和请求ID
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId
);
```

### 查看可复制的目标地域

以下代码用于查看Bucket的数据可复制的目标地域列表。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
];

// 将参数键转换为 getopt 所需的格式，如 "region:"
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 获取命令行传入的长选项参数
$options = getopt("", $longopts);

// 遍历参数定义，检查所有必填项是否已提供
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

// 提取命令行参数中的 region 和 bucket 名称
$region = $options["region"];
$bucket = $options["bucket"];

// 从环境变量中加载访问凭证（如 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载 SDK 默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者、区域和可选的自定义 Endpoint
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 构建 GetBucketReplicationLocation 请求对象，用于获取可用的复制目标区域列表
$request = new Oss\Models\GetBucketReplicationLocationRequest(bucket: $bucket);

// 发送请求并获取响应结果
$result = $client->getBucketReplicationLocation($request);

// 输出响应的状态码、请求 ID 和返回的复制区域信息
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId . PHP_EOL .
    'replication location:' . var_export($result->replicationLocation, true)
);
```

### 查看数据复制进度
说明 
数据复制进度分为历史数据复制进度和新写入数据复制进度。
- 历史数据复制进度用百分比表示，仅对开启了历史数据复制的存储空间有效。
- 新写入数据复制进度用新写入数据的时间点表示，代表这个时间点之前的数据已复制完成。

以下代码用于查看Bucket中指定规则ID的数据复制进度。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
    "rule-id" => ['help' => 'The replication rule id of the bucket', 'required' => True],
];

// 将参数键转换为 getopt 所需的格式（带冒号表示需要值）
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 获取命令行传入的长选项参数
$options = getopt("", $longopts);

// 遍历参数定义，检查所有必填项是否已提供
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

// 提取命令行参数中的 region、bucket 和 rule-id
$region = $options["region"];
$bucket = $options["bucket"];
$ruleId = $options["rule-id"];

// 从环境变量中加载访问凭证（如 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载 SDK 默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者、区域和可选的自定义 Endpoint
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 构建 GetBucketReplicationProgress 请求对象，用于查询指定复制规则的同步进度
$request = new Oss\Models\GetBucketReplicationProgressRequest(bucket: $bucket, ruleId: $ruleId);

// 发送请求并获取复制进度信息
$result = $client->getBucketReplicationProgress($request);

// 输出响应的状态码、请求 ID和复制进度详情
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId . PHP_EOL .
    'replication progress:' . var_export($result->replicationProgress, true)
);
```

### 关闭数据复制

通过删除存储空间的复制规则，您可以关闭源存储空间到目标存储空间的数据复制关系。

以下代码用于删除Bucket中指定规则ID的数据复制关系。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True],
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False],
    "bucket" => ['help' => 'The name of the bucket', 'required' => True],
    "rule-id" => ['help' => 'The replication rule id of the bucket', 'required' => True],
];

// 将参数键转换为 getopt 所需的格式（带冒号表示需要值）
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 获取命令行传入的长选项参数
$options = getopt("", $longopts);

// 遍历参数定义，检查所有必填项是否已提供
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

// 提取命令行参数中的 region、bucket 和 rule-id
$region = $options["region"];
$bucket = $options["bucket"];
$ruleId = $options["rule-id"];

// 从环境变量中加载访问凭证（如 OSS_ACCESS_KEY_ID 和 OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载 SDK 默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者、区域以及可选的自定义 Endpoint
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 构建 DeleteBucketReplication 请求对象，用于删除指定复制规则
$request = new Oss\Models\DeleteBucketReplicationRequest(
    bucket: $bucket,
    replicationRules: new Oss\Models\ReplicationRules(
        ids: [$ruleId] // 指定要删除的复制规则 ID 列表
    )
);

// 发送请求以删除指定的复制规则
$result = $client->deleteBucketReplication($request);

// 输出响应的状态码和请求 ID
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId
);
```

[上一篇：数据管理（PHP SDK V2）](/zh/oss/developer-reference/data-management-using-oss-sdk-for-php-v2/)[下一篇：访问跟踪（PHP SDK V2）](/zh/oss/developer-reference/php-access-tracking)该文章对您有帮助吗？反馈
  
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