# 使用PHP SDK V2上传管理器实现文件分片上传

Source: https://help.aliyun.com/zh/oss/developer-reference/file-uploader-with-oss-sdk-for-php-v2

---

- 使用PHP SDK V2上传管理器实现文件分片上传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 文件上传管理器（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文针对文件的传输场景，介绍如何使用PHP SDK V2新增的上传管理器Uploader模块进行文件上传。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要进行文件上传，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。
- 本文以从环境变量读取访问凭证为例。更多配置访问凭证的示例，请参见[PHP配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。

## 方法定义

#### 上传管理器功能简介

PHP SDK V2新增上传管理器Uploader提供了通用的上传接口，隐藏了底层接口的实现细节，提供便捷的文件上传能力。
- 上传管理器Uploader底层利用分片上传接口，把大文件或者流分成多个较小的分片并发上传，提升上传的性能。
- 上传管理器Uploader同时提供了断点续传的能力，即在上传过程中，记录已完成的分片状态，如果出现网络中断、程序异常退出等问题导致文件上传失败，甚至重试多次仍无法完成上传，再次上传时，可以通过断点记录文件恢复上传。

上传管理器Uploader的常用方法如下：

```
final class Uploader
{
	...
    public function __construct($client, array $args = [])

    public function uploadFile(Models\PutObjectRequest $request, string $filepath, array $args = []): Models\UploadResult

    public function uploadFrom(Models\PutObjectRequest $request, StreamInterface $stream, array $args = []): Models\UploadResult
	...
}
```

#### 请求参数列表
| 参数名 | 类型 | 说明|
| request | PutObjectRequest | 上传对象的请求参数，和 PutObject 接口的请求参数一致|
| stream | StreamInterface | 需要上传的流|
| filePath | string | 本地文件路径|
| args | array | （可选）配置选项|

其中，args常用参数说明列举如下：
| 参数名 | 类型 | 说明|
| part_size | int | 指定分片大小，默认值为 6MiB|
| parallel_num | int | 指定上传任务的并发数，默认值为 3。针对的是单次调用的并发限制，而不是全局的并发限制|
| leave_parts_on_error | bool | 当上传失败时，是否保留已上传的分片，默认不保留|

当使用NewUploader实例化实例时，您可以指定多个配置选项来自定义对象的上传行为。也可以在每次调用上传接口时，指定多个配置选项来自定义每次上传对象的行为。
- 设置Uploader的配置参数
```
$u = $client->newUploader(['part_size' => 10 * 1024 * 1024]);
```
- 设置每次上传请求的配置参数
```
$u->uploadFile(
    new Oss\Models\PutObjectRequest(
        bucket: 'bucket',
        key: 'key'
    ),
    filepath: '/local/dir/example',
    args: [
        'part_size' => 10 * 1024 * 1024,
    ]
);
```

## 示例代码

您可以通过以下代码使用上传管理器上传本地文件到存储空间。

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

// 定义要上传的本地文件路径
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径

// 创建上传器实例
$uploader = $client->newUploader();

// 执行分片上传操作
$result = $uploader->uploadFile(
    request: new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key), // 创建PutObjectRequest对象，指定Bucket和对象名称
    filepath: $filename, // 指定要上传的本地文件路径
);

// 打印分片上传结果
printf(
    'multipart upload status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'multipart upload request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'multipart upload result:' . var_export($result, true) . PHP_EOL  // 分片上传的详细结果
);

```

## 常见使用场景

### 使用上传管理器设置分片大小和并发数

您可以使用以下代码设置上传管理器Uploader的配置参数，设置分片大小和并发数。

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

// 定义分片上传的相关参数
$partSize = 100 * 1024; // 分片大小，单位为字节（此处设置为100KB）

// 定义要上传的本地文件路径
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径

// 创建上传器实例
$uploader = $client->newUploader();

// 执行分片上传操作
$result = $uploader->uploadFile(
    request: new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key), // 创建PutObjectRequest对象，指定Bucket和对象名称
    filepath: $filename, // 指定要上传的本地文件路径
    args: [ // 可选参数，用于自定义分片上传行为
        'part_size' => $partSize, // 自定义分片大小
        'parallel_num' => 1, // 并发上传的分片数量
    ]
);

// 打印分片上传结果
printf(
    'multipart upload status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'multipart upload request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'multipart upload result:' . var_export($result, true) . PHP_EOL  // 分片上传的详细结果
);

```

### 使用上传管理器上传本地文件流

您可以通过以下代码使用上传管理器上传本地文件流。

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

// 定义分片上传的相关参数
$partSize = 100 * 1024; // 分片大小，单位为字节（此处设置为100KB）

// 定义要上传的本地文件路径
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径

// 创建上传器实例
$uploader = $client->newUploader();

// 执行分片上传操作
// 使用LazyOpenStream以流的形式打开文件，避免一次性加载整个文件到内存
$result = $uploader->uploadFrom(
    request: new Oss\Models\PutObjectRequest(
        bucket: $bucket,
        key: $key
    ),
    stream: new \GuzzleHttp\Psr7\LazyOpenStream($filename, 'rb'), // 以只读模式打开文件流
    args: [
        'part_size' => $partSize, // 自定义分片大小
    ]
);

// 打印上传结果
printf(
    'upload from status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'upload from request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'upload from result:' . var_export($result, true) . PHP_EOL  // 上传的详细结果
);

```

### 使用上传管理器设置显示上传进度

您可以通过以下代码使用上传管理器上传本地文件时显示上传进度。

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

// 定义分片上传的相关参数
$partSize = 100 * 1024; // 分片大小，单位为字节（此处设置为100KB）

// 定义要上传的本地文件路径
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径

// 创建上传器实例
$uploader = $client->newUploader();

$request = new \AlibabaCloud\Oss\V2\Models\PutObjectRequest(bucket: $bucket, key: $key);

# 设置上传进度回调函数，用于显示上传进度
$request->progressFn = function (int $increment, int $transferred, int $total) {
    echo sprintf("已经上传：%d" . PHP_EOL, $transferred);
    echo sprintf("本次上传：%d" . PHP_EOL, $increment);
    echo sprintf("数据总共：%d" . PHP_EOL, $total);
    echo '-------------------------------------------' . PHP_EOL;
};

// 执行分片上传操作
$result = $uploader->uploadFile(request: $request,filepath: $filename);

// 打印分片上传结果
printf(
    'multipart upload status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'multipart upload request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'multipart upload result:' . var_export($result, true) . PHP_EOL  // 分片上传的详细结果
);

```

### 使用上传管理器设置上传回调

如果您希望在文件上传后通知应用服务器，可参考以下代码示例。

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

// 定义分片上传的相关参数
$partSize = 100 * 1024; // 分片大小，单位为字节（此处设置为100KB）

// 定义要上传的本地文件路径
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径

// 创建上传器实例
$uploader = $client->newUploader();

// 添加x-oss-callback和x-oss-callback-var头部信息
// 定义回调地址
 $call_back_url = "http://www.example.com/callback";

// 构造回调参数（callback）：指定回调地址和回调请求体，使用 Base64 编码
// 使用占位符 {var1} 和 {var2} 替代 ${x:var1} 和 ${x:var2}
$callback_body_template = "bucket={bucket}&object={object}&my_var_1={var1}&my_var_2={var2}";
$callback_body_replaced = str_replace(
    ['{bucket}', '{object}', '{var1}', '{var2}'],
    [$bucket, $key, 'value1', 'value2'],
    $callback_body_template
);
$callback = base64_encode(json_encode([
    "callbackUrl" => $call_back_url,
    "callbackBody" => $callback_body_replaced
]));

// 构造自定义变量（callback-var），使用 Base64 编码
$callback_var = base64_encode(json_encode([
    "x:var1" => "value1",
    "x:var2" => "value2"
]));

// 执行分片上传操作
$result = $uploader->uploadFile(
    request: new Oss\Models\PutObjectRequest(
                    bucket: $bucket,
                    key: $key,
                    callback: $callback,
                    callbackVar: $callback_var,), // 创建PutObjectRequest对象，指定Bucket和对象名称
    filepath: $filename, // 指定要上传的本地文件路径
);

// 打印分片上传结果
printf(
    'multipart upload status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'multipart upload request id:' . $result->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'multipart upload result:' . var_export($result, true) . PHP_EOL  // 分片上传的详细结果
);

```

## 相关文档
- 关于上传管理器的更多信息，请参见[开发者指南](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E4%B8%8A%E4%BC%A0%E7%AE%A1%E7%90%86%E5%99%A8uploader)。
- 关于上传管理器的完整示例，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Uploader.php)。

[上一篇：使用预签名URL上传（PHP SDK V2）](/zh/oss/developer-reference/upload-object-using-a-presigned-url-for-php-sdk-v2)[下一篇：下载文件](/zh/oss/developer-reference/download-file-using-oss-sdk-for-php-v2/)该文章对您有帮助吗？反馈
  
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