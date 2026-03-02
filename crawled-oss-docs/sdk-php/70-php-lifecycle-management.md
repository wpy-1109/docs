# 使用PHP SDK管理存储空间生命周期规则

Source: https://help.aliyun.com/zh/oss/developer-reference/php-lifecycle-management

---

- 使用PHP SDK管理存储空间生命周期规则-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 生命周期管理（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何使用PHP SDK V2管理存储空间（Bucket）的生命周期功能。

## 背景信息

在OSS中，并非所有上传的数据都需要频繁访问，但出于数据合规性或归档需求，部分数据仍需以冷存储的形式保存。根据业务需求，您可以选择：
- 基于最后修改时间（Last Modified Time）的生命周期规则：当某些数据长时间未被修改且不再需要保留时，可以通过此规则批量删除它们，或将其转换为冷存储类型，从而释放存储空间。
- 基于最后访问时间（Last Access Time）的生命周期规则：如果希望OSS自动监测数据的访问模式来识别冷数据并动态转换存储类型，可启用此规则。OSS将自动识别长期未被访问的数据，将其转换为更经济的冷存储，从而实现冷热分层，降低存储成本。

## 注意事项
- 在配置基于最后一次修改时间或者最后一次访问时间的生命周期规则之前，请确保您已了解该功能。详情请参见[基于最后一次修改时间的生命周期规则](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time)和[基于最后一次访问时间的生命周期规则](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-access-time)。
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要设置生命周期规则，您必须有`oss:PutBucketLifecycle`权限；要查看生命周期规则，您必须有`oss:GetBucketLifecycle`权限；要清空生命周期规则，您必须有`oss:DeleteBucketLifecycle`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 设置生命周期规则

以下代码分别提供了设置基于最后一次修改时间和基于最后一次访问时间的生命周期规则的示例。设置完成后，如果您希望修改其中的一条或多条生命周期规则，请参见[如何修改其中一条或多条生命周期规则配置？](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#66e3fe0b87hr7)。

### 基于最后一次修改时间策略执行转换文件存储类型

以下代码用于为Bucket设置基于最后一次修改时间策略，以执行转换文件存储类型的操作。

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 定义生命周期规则 将前缀为log/的对象在30天后转换为低频存储类型
$lifecycleRule = new Oss\Models\LifecycleRule(
    prefix: 'log/', // 对象前缀
    transitions: array(
        new Oss\Models\LifecycleRuleTransition(
            days: 30, // 转换时间为30天
            storageClass: 'IA' // 转换为目标存储类型为低频访问
        )
    ),
    id: 'rule', // 规则ID
    status: 'Enabled' // 规则状态为启用
);

// 创建生命周期配置对象 并添加生命周期规则
$lifecycleConfiguration = new LifecycleConfiguration(
    rules: array($lifecycleRule)
);

// 创建设置存储空间生命周期的请求对象 并将生命周期配置传入
$request = new Oss\Models\PutBucketLifecycleRequest(
    bucket: $bucket,
    lifecycleConfiguration: $lifecycleConfiguration
);

// 调用putBucketLifecycle方法设置存储空间的生命周期规则
$result = $client->putBucketLifecycle($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL // 请求的唯一标识
);

```

### 基于最后一次修改时间策略限制除指定前缀、标签以外的文件执行转换存储类型操作

以下代码用于指定Bucket中除前缀为log、包含key为key1，value为value1标签且符合指定大小以外的文件在距离最后一次修改时间30天后转低频存储，过期时间为100天。

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 定义生命周期规则 将前缀为log/的对象在30天后转换为低频存储类型
$lifecycleRule = new Oss\Models\LifecycleRule(
    id: 'rule', // 规则ID
    status: 'Enabled', // 规则状态为启用
    prefix: 'logs', // 对象前缀
    transitions: array(
        new Oss\Models\LifecycleRuleTransition(
            days: 30, // 转换时间为30天
            storageClass: 'IA', // 转换为目标存储类型为低频存储
            isAccessTime: false // 设置为false，基于最后一次修改时间策略
        )
    ),
    filter: new Oss\Models\LifecycleRuleFilter( // 定义过滤条件
        objectSizeGreaterThan: 500, // 设置大于500字节
        objectSizeLessThan: 1000, // 设置小于1000字节
        not: new Oss\Models\LifecycleRuleNot( // 定义排除条件
            prefix: 'logs/log', // 排除前缀为log的对象
            tag: new Oss\Models\Tag( // 定义标签条件
                key: 'key1',
                value: 'value1'
            )
        )
    ),
    expiration: new Oss\Models\LifecycleRuleExpiration(
        days: 100 // 过期时间为100天
    )
);

// 创建生命周期配置对象 并添加生命周期规则
$lifecycleConfiguration = new LifecycleConfiguration(
    rules: array($lifecycleRule)
);

// 创建设置存储空间生命周期的请求对象 并将生命周期配置传入
$request = new Oss\Models\PutBucketLifecycleRequest(
    bucket: $bucket,
    lifecycleConfiguration: $lifecycleConfiguration
);

// 调用putBucketLifecycle方法设置存储空间的生命周期规则
$result = $client->putBucketLifecycle($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL // 请求的唯一标识
);

```

### 基于最后一次访问时间策略转换文件存储类型

以下代码用于为Bucket设置基于最后一次访问时间策略，以执行转换存储类型的操作。

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 定义生命周期规则 将前缀为log/的对象在30天后转换为低频存储类型
$lifecycleRule = new Oss\Models\LifecycleRule(
    prefix: 'log/', // 对象前缀
    transitions: array(
        new Oss\Models\LifecycleRuleTransition(
            days: 30, // 转换时间为30天
            storageClass: 'IA', // 转换为目标存储类型为低频访问
            IsAccessTime: 'true', // 是否基于访问时间触发转换
            ReturnToStdWhenVisit: 'false' // 再次访问时仍保留为低频存储
        )
    ),
    id: 'rule', // 规则ID
    status: 'Enabled' // 规则状态为启用
);

// 创建生命周期配置对象 并添加生命周期规则
$lifecycleConfiguration = new LifecycleConfiguration(
    rules: array($lifecycleRule)
);

// 创建设置存储空间生命周期的请求对象 并将生命周期配置传入
$request = new Oss\Models\PutBucketLifecycleRequest(
    bucket: $bucket,
    lifecycleConfiguration: $lifecycleConfiguration
);

// 调用putBucketLifecycle方法设置存储空间的生命周期规则
$result = $client->putBucketLifecycle($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL // 请求的唯一标识
);

```

## 查看生命周期规则

以下代码用于查看生命周期规则中包含的信息。

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 创建获取存储空间生命周期的请求对象
$request = new Oss\Models\GetBucketLifecycleRequest(bucket: $bucket);

// 调用getBucketLifecycle方法获取存储空间的生命周期规则
$result = $client->getBucketLifecycle($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL . // 请求的唯一标识
    'lifecycle:' . var_export($result->lifecycleConfiguration, true) . PHP_EOL // 生命周期规则内容
);

```

## 清空生命周期规则

以下代码用于清空examplebucket的所有生命周期规则。如果您需要删除其中一条或者多条生命周期规则，请参见[如何删除其中一条或多条生命周期规则？](https://help.aliyun.com/zh/oss/user-guide/lifecycle-rules-based-on-the-last-modified-time#80811cc9cawfo)。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 创建删除存储空间生命周期规则的请求对象
$request = new Oss\Models\DeleteBucketLifecycleRequest(bucket: $bucket);

// 调用deleteBucketLifecycle方法删除存储空间的生命周期规则
$result = $client->deleteBucketLifecycle($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL // 请求的唯一标识
);

```

## 相关文档
- 关于设置生命周期规则的API接口说明，请参见[PutBucketLifecycle](https://help.aliyun.com/zh/oss/developer-reference/putbucketlifecycle#reference-xlw-dbv-tdb)。
- 关于查看生命周期规则的API接口说明，请参见[GetBucketLifecycle](https://help.aliyun.com/zh/oss/developer-reference/getbucketlifecycle#reference-zq5-grw-tdb)。
- 关于清空生命周期规则的API接口说明，请参见[DeleteBucketLifecycle](https://help.aliyun.com/zh/oss/developer-reference/deletebucketlifecycle#reference-wl1-xsw-tdb)。

[上一篇：访问跟踪（PHP SDK V2）](/zh/oss/developer-reference/php-access-tracking)[下一篇：静态网站托管（PHP SDK V2）](/zh/oss/developer-reference/php-static-website-hosting)该文章对您有帮助吗？反馈
  
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