# 使用PHP SDK管理存储空间日志转存

Source: https://help.aliyun.com/zh/oss/developer-reference/php-logging-2

---

- 使用PHP SDK管理存储空间日志转存-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 日志转存（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
访问OSS的过程中会产生大量的访问日 志。您可以通过日志转存功能将这些日志按照固定命名规则，以小时为单位生成日志文件写入您指定的存储空间（Bucket）。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要开启日志转存，您必须有`oss:PutBucketLogging`权限；要查看日志转存配置，您必须有`oss:GetBucketLogging`权限；要关闭日志转存，您必须有`oss:DeleteBucketLogging`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 示例代码

### 开启日志转存

以下代码用于开启日志转存功能。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名是可选项 其他服务可以用来访问OSS的域名
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项
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

// 创建设置存储空间日志功能的请求对象
$request = new Oss\Models\PutBucketLoggingRequest(
    bucket: $bucket, // 存储空间名称
    bucketLoggingStatus: new Oss\Models\BucketLoggingStatus(
        loggingEnabled: new Oss\Models\LoggingEnabled(
            targetBucket: $bucket, // 日志存储的目标存储空间
            targetPrefix: 'log/'   // 日志文件的前缀
        )
    )
);

// 调用putBucketLogging方法设置存储空间的日志功能
$result = $client->putBucketLogging($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId               // 请求的唯一标识
);

```

### 查看日志转存配置

以下代码用于查看日志转存配置。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名是可选项 其他服务可以用来访问OSS的域名
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项
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

// 创建获取存储空间日志功能的请求对象
$request = new Oss\Models\GetBucketLoggingRequest(
    bucket: $bucket // 存储空间名称
);

// 调用getBucketLogging方法获取存储空间的日志功能配置
$result = $client->getBucketLogging($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'logging status:' . var_export($result->bucketLoggingStatus, true) . PHP_EOL // 存储空间日志功能的配置状态
);

```

### 关闭日志转存

以下代码用于关闭日志转存功能。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名是可选项 其他服务可以用来访问OSS的域名
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项
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

// 创建删除存储空间日志功能的请求对象
$request = new Oss\Models\DeleteBucketLoggingRequest(
    bucket: $bucket // 存储空间名称
);

// 调用deleteBucketLogging方法删除存储空间的日志功能配置
$result = $client->deleteBucketLogging($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId               // 请求的唯一标识
);

```

### 配置用户自定义日志字段

您可以使用PutUserDefinedLogFieldsConfig接口为存储空间（Bucket）实时日志中的`user_defined_log_fields`字段进行个性化配置。您可以将OSS请求中用户关心的请求头或查询参数信息记录到该字段中去以便后续分析请求。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名是可选项 其他服务可以用来访问OSS的域名
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项
];
$longopts = array_map(function ($key) { return "$key:"; }, array_keys($optsdesc));
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

$region = $options["region"];
$bucket = $options["bucket"];

// 从环境变量加载AccessKey凭证（需提前设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 配置OSS客户端参数
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在地域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 设置Endpoint（如https://oss-cn-hangzhou.aliyuncs.com）
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 构建自定义日志字段配置请求
$request = new Oss\Models\PutUserDefinedLogFieldsConfigRequest(
    bucket: $bucket, 
    userDefinedLogFieldsConfiguration: new Oss\Models\UserDefinedLogFieldsConfiguration(
        new Oss\Models\LoggingParamSet(parameters: ['param1', 'params2']), // 自定义日志参数
        new Oss\Models\LoggingHeaderSet(headers: ['header1', 'header2']) // 自定义日志头部
    )
);

// 执行设置自定义日志字段配置操作
$result = $client->putUserDefinedLogFieldsConfig($request);

// 输出操作结果状态码和请求ID
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId
);

```

### 查询用户自定义日志字段

您可以使用GetUserDefinedLogFieldsConfig接口获取存储空间（Bucket）实时日志中`user_defined_log_fields`字段的个性化配置。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项，指定存储空间所在地域（如：cn-hangzhou）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名可选，需符合格式https://oss-.aliyuncs.com
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项
];
$longopts = array_map(function ($key) { return "$key:"; }, array_keys($optsdesc)); // 转换参数为命令行选项格式
$options = getopt("", $longopts); // 解析命令行参数

// 验证必填参数是否存在（确保region和bucket参数已提供）
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

$region = $options["region"]; // 获取区域参数值
$bucket = $options["bucket"]; // 获取存储空间名称

// 从环境变量加载AccessKey凭证（需提前设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // 使用环境变量凭证提供器

// 配置OSS客户端参数（设置区域、凭证及可选访问域名）
$cfg = Oss\Config::loadDefault(); // 加载默认配置
$cfg->setCredentialsProvider($credentialsProvider); // 绑定凭证提供器
$cfg->setRegion($region); // 设置Bucket所在区域（如：cn-hangzhou）
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 设置自定义访问域名（如https://oss-cn-hangzhou.aliyuncs.com）
}

// 创建OSS客户端实例（用于执行API调用）
$client = new Oss\Client($cfg);

// 构建获取自定义日志字段配置请求
$request = new Oss\Models\GetUserDefinedLogFieldsConfigRequest(bucket: $bucket); // 指定要查询的Bucket名称

// 执行获取自定义日志字段配置操作（需oss:GetUserDefinedLogFieldsConfig权限）
$result = $client->getUserDefinedLogFieldsConfig($request); // 调用接口获取配置信息

// 输出操作结果状态码、请求ID及配置详情
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId . PHP_EOL .
    'user defined log fields config:' . var_export($result->userDefinedLogFieldsConfiguration, true) // 使用var_export输出配置对象结构
);

```

### 删除用户自定义日志字段

您可以使用DeleteUserDefinedLogFieldsConfig接口删除存储空间（Bucket）实时日志中`user_defined_log_fields`字段的个性化配置。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域参数：存储空间所在地域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 可选访问域名参数
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 必填存储空间名称参数
];
$longopts = \array_map(function ($key) { return "$key:"; }, array_keys($optsdesc)); // 转换参数为命令行格式
$options = getopt("", $longopts); // 解析命令行参数

// 参数校验：检查必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help'];
        echo "Error: the following arguments are required: --$key, $help";
        exit(1);
    }
}

$region = $options["region"]; // 获取区域参数值
$bucket = $options["bucket"]; // 获取存储空间名称

// 加载环境变量中的AccessKey凭证
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // 使用环境变量凭证

// 客户端配置初始化
$cfg = Oss\Config::loadDefault(); // 加载默认配置模板
$cfg->setCredentialsProvider($credentialsProvider); // 绑定凭证提供器
$cfg->setRegion($region); // 设置存储空间所在区域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 设置自定义访问域名（可选）
}

$client = new Oss\Client($cfg); // 创建OSS客户端实例
$request = new Oss\Models\DeleteUserDefinedLogFieldsConfigRequest(bucket: $bucket); // 构建删除配置请求
$result = $client->deleteUserDefinedLogFieldsConfig($request); // 执行删除操作

// 输出结果信息
printf(
    'status code:' . $result->statusCode . PHP_EOL . // 返回HTTP状态码
    'request id:' . $result->requestId // 请求唯一标识
);

```

## 相关文档
- 关于开启日志转存功能的API接口说明，请参见[PutBucketLogging](https://help.aliyun.com/zh/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)。
- 关于查看日志转存配置的API接口说明，请参见[GetBucketLogging](https://help.aliyun.com/zh/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)。
- 关于关闭日志转存功能的API接口说明，请参见[DeleteBucketLogging](https://help.aliyun.com/zh/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)。
- 关于配置用户自定义日志字段的API接口说明，请参见[PutUserDefinedLogFieldsConfig](https://help.aliyun.com/zh/oss/developer-reference/putuserdefinedlogfieldsconfig)。
- 关于查询用户自定义日志字段的API接口说明，请参见[GetUserDefinedLogFieldsConfig](https://help.aliyun.com/zh/oss/developer-reference/getuserdefinedlogfieldsconfig)。
- 关于删除用户自定义日志字段的API接口说明，请参见[DeleteUserDefinedLogFieldsConfig](https://help.aliyun.com/zh/oss/developer-reference/deleteuserdefinedlogfieldsconfig)。

[上一篇：静态网站托管（PHP SDK V2）](/zh/oss/developer-reference/php-static-website-hosting)[下一篇：归档直读（PHP SDK V2）](/zh/oss/developer-reference/real-time-access-to-archive-objects-using-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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