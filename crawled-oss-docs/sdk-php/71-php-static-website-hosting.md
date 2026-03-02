# 使用PHP SDK V2配置静态网站托管和镜像回源

Source: https://help.aliyun.com/zh/oss/developer-reference/php-static-website-hosting

---

- 使用PHP SDK V2配置静态网站托管和镜像回源-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 静态网站托管（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
您可以将存储空间（Bucket）设置为静态网站托管模式并设置镜像回源的跳转规则（RoutingRule）。静态网站托管模式配置生效后，访问网站相当于访问Bucket，并且能够自动跳转至指定的索引页面和错误页面。镜像回源的跳转规则配置生效后，可用于数据无缝迁移到OSS的场景。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要设置静态网站托管或者镜像回源，您必须有`oss:PutBucketWebsite`权限；要获取静态网站托管或者镜像回源，您必须有`oss:GetBucketWebsite`权限；要删除静态网站托管或者镜像回源，您必须有`oss:DeleteBucketWebsite`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 静态网站托管

静态网站是指所有的网页都由静态内容构成，包括客户端执行的脚本（例如JavaScript）。您可以通过静态网站托管功能将您的静态网站托管到Bucket，并使用Bucket的访问域名访问这个网站。

#### 设置静态网站托管

以下代码用于设置静态网站托管：

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

// 创建设置存储空间静态网站托管配置的请求对象
$request = new Oss\Models\PutBucketWebsiteRequest(bucket: $bucket,
    websiteConfiguration: new Oss\Models\WebsiteConfiguration(
        indexDocument: new Oss\Models\IndexDocument(
            suffix: 'index.html', // 静态网站的索引页面文件名
            supportSubDir: true, // 是否支持子目录
            type: 0 // 索引页面类型
        ),
        errorDocument: new Oss\Models\ErrorDocument(
            key: 'error.html', // 错误页面文件名
            httpStatus: 404 // 错误页面对应的HTTP状态码
        )
    )
);

// 调用putBucketWebsite方法设置存储空间的静态网站托管配置
$result = $client->putBucketWebsite($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId // 请求的唯一标识
);

```

#### 查看静态网站托管配置

以下代码用于查看静态网站托管配置：

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

// 创建获取存储空间静态网站托管配置的请求对象
$request = new Oss\Models\GetBucketWebsiteRequest(bucket: $bucket);

// 调用getBucketWebsite方法获取存储空间的静态网站托管配置
$result = $client->getBucketWebsite($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL . // 请求的唯一标识
    'website config:' . var_export($result->websiteConfiguration, true) . PHP_EOL // 静态网站托管配置内容
);

```

#### 删除静态网站托管配置

以下代码用于删除静态网站托管配置：

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

// 创建删除存储空间静态网站托管配置的请求对象
$request = new Oss\Models\DeleteBucketWebsiteRequest(bucket: $bucket);

// 调用deleteBucketWebsite方法删除存储空间的静态网站托管配置
$result = $client->deleteBucketWebsite($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId // 请求的唯一标识
);

```

## 镜像回源

镜像回源主要用于数据无缝迁移到OSS的场景。例如某服务已经在用户建立的源站或者在其他云产品上运行，现因业务发展，需要将服务迁移至OSS，迁移时需保证服务的正常运行。您可以在迁移过程中使用镜像回源规则获取未迁移至OSS的部分数据，保证服务的正常运行。

#### 设置镜像回源

例如，当请求者访问目标Bucket中不存在的文件时，可以通过指定回源条件和回源地址，从源站中获取目标文件。例如您在华东1（杭州）有名为examplebucket的Bucket，您希望请求者访问Bucket根目录下examplefolder目录中不存在的文件时，可以从www.example.com站点的examplefolder目录获取目标文件。

以下代码用于设置符合上述场景的镜像回源规则：

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

// 定义镜像回源规则
$ruleOk = new Oss\Models\RoutingRule(
    ruleNumber: 1, // 规则编号
    condition: new Oss\Models\RoutingRuleCondition(
        keyPrefixEquals: 'myobject', // 匹配对象前缀
        httpErrorCodeReturnedEquals: 404 // 回源条件为HTTP状态码404
    ),
    redirect: new Oss\Models\RoutingRuleRedirect(
        redirectType: 'Mirror', // 重定向类型为镜像
        mirrorURL: 'http://www.test.com/', // 回源地址
        mirrorHeaders: new Oss\Models\MirrorHeaders(
            passAll: false, // 是否传递所有头部
            passs: ['myheader-key1', 'myheader-key2'], // 允许传递的HTTP Header参数
            removes: ['myheader-key3', 'myheader-key4'], // 禁止传递的HTTP Header参数
            sets: [
                new Oss\Models\MirrorHeadersSet(
                    key: 'myheader-key5', // 设置指定HTTP Header参数的名称
                    value: 'myheader-value' // 设置指定HTTP Header参数的值
                ),
            ]
        )
    )
);

// 创建设置镜像回源的请求
$request = new Oss\Models\PutBucketWebsiteRequest(
    bucket: $bucketName, // 存储空间名称
    websiteConfiguration: new Oss\Models\WebsiteConfiguration(
        indexDocument: new Oss\Models\IndexDocument(
            suffix: 'index.html', // 镜像回源的默认页面
            supportSubDir: true,
            type: 0
        ),
        errorDocument: new Oss\Models\ErrorDocument(
            key: 'error.html', // 镜像回源的错误页面
            httpStatus: 404
        ),
        routingRules: new Oss\Models\RoutingRules(
            routingRules: [$ruleOk] // 镜像回源规则
        )
    )
);

// 执行设置镜像回源的请求
$result = $client->putBucketWebsite($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL . // 请求的唯一标识
    'website config:' . var_export($result->websiteConfiguration, true) . PHP_EOL // 静态网站托管配置内容
);

```

#### 获取镜像回源配置

以下代码用于获取镜像回源配置：

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

// 创建获取镜像回源配置的请求
$request = new Oss\Models\GetBucketWebsiteRequest(
    bucket: $bucketName // 存储空间名称
);

// 执行获取镜像回源的请求
$result = $client->getBucketWebsite($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL . // 请求的唯一标识
    'website config:' . var_export($result->websiteConfiguration, true) . PHP_EOL // 静态网站托管配置内容
);

```

#### 删除镜像回源配置

以下代码用于删除镜像回源配置：

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

// 创建删除镜像回源配置的请求
$request = new Oss\Models\DeleteBucketWebsiteRequest(
    bucket: $bucketName // 存储空间名称
);

// 调用deleteBucketWebsite方法删除存储空间的静态网站托管配置
$result = $client->deleteBucketWebsite($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId // 请求的唯一标识
);

```

## 相关文档
- 关于静态网站托管以及镜像回源的完整示例代码，请参见[put_bucket_website](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketWebsite.php)、[get_bucket_website](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketWebsite.php)和[delete_bucket_website](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketWebsite.php)。
- 关于设置静态网站托管或者镜像回源的API接口说明，请参见[PutBucketWebsite](https://help.aliyun.com/zh/oss/developer-reference/putbucketwebsite#reference-hwb-yr5-tdb)。
- 关于获取静态网站托管或者镜像回源的API接口说明，请参见[GetBucketWebsite](https://help.aliyun.com/zh/oss/developer-reference/getbucketwebsite#reference-wvy-s4w-tdb)。
- 关于删除静态网站托管或者镜像回源的API接口说明，请参见[DeleteBucketWebsite](https://help.aliyun.com/zh/oss/developer-reference/deletebucketwebsite#reference-zrl-msw-tdb)。

[上一篇：生命周期管理（PHP SDK V2）](/zh/oss/developer-reference/php-lifecycle-management)[下一篇：日志转存（PHP SDK V2）](/zh/oss/developer-reference/php-logging-2)该文章对您有帮助吗？反馈
  
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