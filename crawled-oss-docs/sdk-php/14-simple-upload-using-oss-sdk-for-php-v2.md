# 使用PHPSDKV2实现简单上传

Source: https://help.aliyun.com/zh/oss/developer-reference/simple-upload-using-oss-sdk-for-php-v2

---

- 使用PHPSDKV2实现简单上传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 简单上传（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何通过简单上传方法将本地文件快速上传到OSS，此方法操作简便，适合快速将本地文件上传到云端存储。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要进行简单上传，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。
- 本文以从环境变量读取访问凭证为例。更多配置访问凭证的示例，请参见[PHP配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。

## 示例代码

您可以使用以下代码将本地文件上传到目标存储空间。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
    "file" => ['help' => 'Local path to the file you want to upload.', 'required' => True], // 本地文件路径（必填）
];

// 将参数描述转换为getopt所需的长选项格式
// 每个参数后面加上":"表示该参数需要值
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help']; // 获取参数的帮助信息
        echo "Error: the following arguments are required: --$key, $help" . PHP_EOL;
        exit(1); // 如果必填参数缺失，则退出程序
    }
}

// 从解析的参数中提取值
$region = $options["region"]; // Bucket所在的地域
$bucket = $options["bucket"]; // Bucket名称
$key = $options["key"];       // 对象名称
$file = $options["file"];     // 本地文件路径

// 加载环境变量中的凭证信息
// 使用EnvironmentVariableCredentialsProvider从环境变量中读取Access Key ID和Access Key Secret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 如果提供了访问域名，则设置endpoint
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 检查文件是否存在
if (!file_exists($file)) {
    echo "Error: The specified file does not exist." . PHP_EOL; // 如果文件不存在，输出错误信息并退出
    exit(1);
}

// 打开文件并准备上传
// 使用fopen以只读模式打开文件，并通过Utils::streamFor将文件内容转换为流
$body = Oss\Utils::streamFor(fopen($file, 'r'));

// 创建PutObjectRequest对象，用于上传文件
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);
$request->body = $body; // 设置请求体为文件流

// 执行上传操作
$result = $client->putObject($request);

// 打印上传结果
// 输出HTTP状态码、请求ID和ETag，用于验证上传是否成功
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'etag:' . $result->etag . PHP_EOL               // 对象的ETag，用于标识对象的唯一性
);

```

## 常见使用场景

### 上传字符串

您可以使用以下代码将字符串上传至目标存储空间。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
];

// 将参数描述转换为getopt所需的长选项格式
$longopts = \array_map(function ($key) {
    return "$key:"; // 每个参数后面加上":"表示需要值
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help']; // 获取参数的帮助信息
        echo "Error: the following arguments are required: --$key, $help" . PHP_EOL;
        exit(1); // 如果必填参数缺失，则退出程序
    }
}

// 从解析的参数中提取值
$region = $options["region"]; // Bucket所在的地域
$bucket = $options["bucket"]; // Bucket名称
$key = $options["key"];       // 对象名称

// 加载环境变量中的凭证信息
// 使用EnvironmentVariableCredentialsProvider从环境变量中读取Access Key ID和Access Key Secret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 如果提供了访问域名，则设置endpoint
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 要上传的数据内容
$data = 'Hello OSS';

// 创建PutObjectRequest对象，用于上传对象
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);
$request->body = Oss\Utils::streamFor($data); // 设置请求体为数据流

// 执行上传操作
$result = $client->putObject($request);

// 打印上传结果
printf(
    'status code: %s' . PHP_EOL . // HTTP状态码
    'request id: %s' . PHP_EOL .  // 请求ID
    'etag: %s' . PHP_EOL,         // 对象的ETag
    $result->statusCode,
    $result->requestId,
    $result->etag
);

```

### 上传Byte数组

您可以使用以下代码将Byte数组上传至目标存储空间。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
];

// 将参数描述转换为getopt所需的长选项格式
$longopts = \array_map(function ($key) {
    return "$key:"; // 每个参数后面加上":"表示需要值
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help']; // 获取参数的帮助信息
        echo "Error: the following arguments are required: --$key, $help" . PHP_EOL;
        exit(1); // 如果必填参数缺失，则退出程序
    }
}

// 从解析的参数中提取值
$region = $options["region"]; // Bucket所在的地域
$bucket = $options["bucket"]; // Bucket名称
$key = $options["key"];       // 对象名称

// 加载环境变量中的凭证信息
// 使用EnvironmentVariableCredentialsProvider从环境变量中读取Access Key ID和Access Key Secret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 如果提供了访问域名，则设置endpoint
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 要上传的byte数据内容
$dataBytes = [72, 101, 108, 108, 111, 32, 79, 83, 83]; // 'Hello OSS' 的 ASCII 值
$dataString = implode(array_map('chr', $dataBytes)); // 将byte数组转换为字符串

// 创建PutObjectRequest对象，用于上传对象
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);
$request->body = Oss\Utils::streamFor($dataString); // 设置请求体为数据流

// 执行上传操作
$result = $client->putObject($request);

// 打印上传结果
printf(
    'status code: %s' . PHP_EOL . // HTTP状态码
    'request id: %s' . PHP_EOL .  // 请求ID
    'etag: %s' . PHP_EOL,         // 对象的ETag
    $result->statusCode,
    $result->requestId,
    $result->etag
);

```

### 上传网络流

您可以使用以下代码将网络上传至目标存储空间。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
];

// 将参数描述转换为getopt所需的长选项格式
$longopts = \array_map(function ($key) {
    return "$key:"; // 每个参数后面加上":"表示需要值
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help']; // 获取参数的帮助信息
        echo "Error: the following arguments are required: --$key, $help" . PHP_EOL;
        exit(1); // 如果必填参数缺失，则退出程序
    }
}

// 从解析的参数中提取值
$region = $options["region"]; // Bucket所在的地域
$bucket = $options["bucket"]; // Bucket名称
$key = $options["key"];       // 对象名称

// 加载环境变量中的凭证信息
// 使用EnvironmentVariableCredentialsProvider从环境变量中读取Access Key ID和Access Key Secret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 如果提供了访问域名，则设置endpoint
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 获取网络文件的内容
$url = 'https://www.aliyun.com/';
$response = file_get_contents($url);

// 创建PutObjectRequest对象，用于上传对象
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);
$request->body = Oss\Utils::streamFor($response); // 设置请求体为数据流

// 执行上传操作
$result = $client->putObject($request);

// 打印上传结果
printf(
    'status code: %s' . PHP_EOL . // HTTP状态码
    'request id: %s' . PHP_EOL .  // 请求ID
    'etag: %s' . PHP_EOL,         // 对象的ETag
    $result->statusCode,
    $result->requestId,
    $result->etag
);

```

### 上传文件时显示上传进度

您可以使用以下代码在上传文件时设置显示上传进度。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket 所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket 名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
];

// 将参数描述转换为 getopt 所需的长选项格式
// 每个参数后面加上 ":" 表示该参数需要值
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help']; // 获取参数的帮助信息
        echo "Error: the following arguments are required: --$key, $help";
        exit(1); // 如果必填参数缺失，则退出程序
    }
}

// 从解析的参数中提取值
$region = $options["region"]; // Bucket 所在的地域
$bucket = $options["bucket"]; // Bucket 名称
$key = $options["key"];       // 对象名称

// 使用 EnvironmentVariableCredentialsProvider 从环境变量中加载访问凭证
// 确保环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET 已正确设置
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 加载 SDK 的默认配置
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置 Bucket 所在的地域

// 如果命令行提供了 endpoint 参数，则使用指定的访问域名
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 定义要上传的数据内容
$data = 'Hello OSS';

// 创建 PutObjectRequest 对象，指定 Bucket 和对象 Key
$request = new Oss\Models\PutObjectRequest($bucket, $key);

// 将数据内容转换为流对象
$request->body = Oss\Utils::streamFor($data);

// 设置上传进度回调函数
$request->progressFn = function (int $increment, int $transferred, int $total) {
    echo sprintf("已经上传：%d" . PHP_EOL, $transferred); // 当前已上传的字节数
    echo sprintf("本次上传：%d" . PHP_EOL, $increment);   // 本次上传的字节数增量
    echo sprintf("数据总共：%d" . PHP_EOL, $total);       // 数据总大小
    echo '-------------------------------------------' . PHP_EOL; // 分隔线
};

// 调用 putObject 方法上传对象
$result = $client->putObject($request);

// 输出上传结果
printf(
    'status code: %s' . PHP_EOL, $result->statusCode . // HTTP 响应状态码
    'request id: %s' . PHP_EOL, $result->requestId .   // 请求 ID
    'etag: %s' . PHP_EOL, $result->etag                // 对象的 ETag
);

```

### 上传文件时设置回调函数

OSS在完成简单上传时可以提供回调（Callback）给应用服务器。您只需要在发送给OSS的请求中携带相应的Callback参数，即可实现回调。

您可以使用以下代码在上传文件时设置回调函数。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
];

// 将参数描述转换为getopt所需的长选项格式
// 每个参数后面加上":"表示该参数需要值
$longopts = \array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 验证必填参数是否存在
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === True && empty($options[$key])) {
        $help = $value['help']; // 获取参数的帮助信息
        echo "Error: the following arguments are required: --$key, $help" . PHP_EOL;
        exit(1); // 如果必填参数缺失，则退出程序
    }
}

// 从解析的参数中提取值
$region = $options["region"]; // Bucket所在的地域
$bucket = $options["bucket"]; // Bucket名称
$key = $options["key"];       // 对象名称

// 加载环境变量中的凭证信息
// 使用EnvironmentVariableCredentialsProvider从环境变量中读取Access Key ID和Access Key Secret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用SDK的默认配置
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]); // 如果提供了访问域名，则设置endpoint
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 定义回调服务器的相关信息
// 回调URL：接收回调请求的服务器地址
// 回调Host：回调服务器的主机名
// 回调Body：定义回调内容的模板，支持动态占位符替换
// 回调BodyType：指定回调内容的格式
$callback = base64_encode(json_encode(array(
    'callbackUrl' => 'yourCallbackServerUrl', // 替换为实际的回调服务器URL
    'callbackHost' => 'yourCallbackServerHost', // 替换为实际的回调服务器主机名
    'callbackBody' => 'bucket=${bucket}&object=${object}&etag=${etag}&size=${size}&mimeType=${mimeType}&imageInfo.height=${imageInfo.height}&imageInfo.width=${imageInfo.width}&imageInfo.format=${imageInfo.format}&my_var1=${x:var1}&my_var2=${x:var2}',
    'callbackBodyType' => "application/x-www-form-urlencoded", // 回调内容的格式
)));

// 定义自定义变量，用于在回调中传递额外信息
$callbackVar = base64_encode(json_encode(array(
    'x:var1' => "value1", // 自定义变量1
    'x:var2' => 'value2', // 自定义变量2
)));

// 创建PutObjectRequest对象，用于上传对象
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);
$request->callback = $callback; // 设置回调信息
$request->callbackVar = $callbackVar; // 设置自定义变量

// 执行上传操作
$result = $client->putObject($request);

// 打印上传结果
// 输出HTTP状态码、请求ID以及回调结果，用于验证上传是否成功
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'callback result:' . var_export($result->callbackResult, true) . PHP_EOL // 回调结果的详细信息
);

```

## 相关文档
- 关于简单上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutObject.php)。

[上一篇：上传文件（PHP SDK V2）](/zh/oss/developer-reference/upload-file-using-oss-sdk-for-php-v2/)[下一篇：追加上传（PHP SDK V2）](/zh/oss/developer-reference/append-upload-using-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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