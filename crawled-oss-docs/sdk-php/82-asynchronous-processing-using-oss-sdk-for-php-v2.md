# 使用PHPSDK异步处理多媒体文件

Source: https://help.aliyun.com/zh/oss/developer-reference/asynchronous-processing-using-oss-sdk-for-php-v2

---

- 使用PHPSDK异步处理多媒体文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 异步处理（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)

异步处理（x-oss-async-process）是指程序执行一个任务时，不需要等待该任务完成就能继续执行其他任务。本文介绍如何使用PHP SDK V2进行异步处理的场景，例如文档转换、视频转码、视频拼接等。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。

## 示例代码

以下代码展示了如何进行文档格式转换，将其转换为需要的输出类型。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 定义视频处理样式 将视频转换为指定格式
$style = "video/convert,f_avi,vcodec_h265,s_1920x1080,vb_2000000,fps_30,acodec_aac,ab_100000,sn_1";

// 构造异步处理指令 包括存储空间名称和对象名称的Base64编码
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s",
    $style,
    rtrim(base64_encode($bucket), '='), // Base64编码存储空间名称 去掉末尾的等号
    rtrim(base64_encode($key), '=')     // Base64编码对象名称 去掉末尾的等号
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucket, // 存储空间名称
    key: $key         // 对象名称
);

// 设置处理指令
$request->process = $process;

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

## 常见使用场景

### 视频转码

您可以使用视频转码功能，修改视频的编码格式、降低分辨率和码率以缩小视频文件体积、转换视频封装格式。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 指定转码后的视频名称
$targetObject = "dest.avi";

// 定义处理样式，包括格式、视频编解码器、分辨率、比特率、帧率、音频编解码器、音频比特率等参数
$style = "video/convert,f_avi,vcodec_h265,s_1920x1080,vb_2000000,fps_30,acodec_aac,ab_100000,sn_1";

// 构造异步处理指令 包括处理样式以及处理后文件的保存位置（存储桶和对象名经过Base64编码）
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s",
    $style,
    rtrim(base64_encode($bucketName), '='), // Base64编码存储空间名称并移除末尾的'='
    rtrim(base64_encode($targetObject), '=') // Base64编码对象名称并移除末尾的'='
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName, // 存储空间名称
    key: $objectName,    // 对象名称
    asyncProcess: $process // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 视频转动图

您可以通过视频转动图功能，将视频转换为GIF、WebP等格式的动图。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 指定处理后GIF动图文件名称
$targetKey = "destexample.gif";

// 定义视频转GIF动图的参数，包括GIF宽度、高度、间隔帧数等
$animationStyle = "video/animation,f_gif,w_100,h_100,inter_1000";

// 构造异步处理指令 包括保存路径和Base64编码的Bucket名称和目标文件名称
$bucketNameEncoded = base64_encode($bucketName); // Base64编码存储空间名称
$targetKeyEncoded = base64_encode($targetKey);   // Base64编码目标文件名称
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s/notify,topic_QXVkaW9Db252ZXJ0",
    $animationStyle,
    $bucketNameEncoded,
    $targetKeyEncoded
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName,      // 存储空间名称
    key: $objectName,         // 对象名称
    asyncProcess: $process    // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 视频截雪碧图

您可以通过视频截雪碧图功能，提取视频帧并按一定规则拼接为雪碧图。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 指定输出的雪碧图文件名称
$targetKey = "example.jpg";

// 构建视频转雪碧图参数 包括格式、宽度、高度、间隔帧数等
$animationStyle = "video/sprite,f_jpg,sw_100,sh_100,inter_10000,tw_10,th_10,pad_0,margin_0";

// 构造异步处理指令 包括保存路径和Base64编码的Bucket名称和目标文件名称
$bucketNameEncoded = base64_encode($bucketName); // Base64编码存储空间名称
$targetKeyEncoded = base64_encode($targetKey);   // Base64编码目标文件名称
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s/notify,topic_QXVkaW9Db252ZXJ0",
    $animationStyle,
    $bucketNameEncoded,
    $targetKeyEncoded
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName,      // 存储空间名称
    key: $objectName,         // 对象名称
    asyncProcess: $process    // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 视频截帧

您可以通过视频截帧功能，按一定规则提取视频帧并转换为需要的图片格式。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 指定按视频截帧处理后的文件名称
$targetKey = "dest.png";

// 构建视频截帧参数 包括格式、宽度、高度、裁剪方式、间隔帧数等
$animationStyle = "video/snapshots,f_jpg,w_100,h_100,scaletype_crop,inter_10000";

// 构造异步处理指令 包括保存路径和Base64编码的Bucket名称和目标文件名称
$bucketNameEncoded = base64_encode($bucketName); // Base64编码存储空间名称
$targetKeyEncoded = base64_encode($targetKey);   // Base64编码目标文件名称
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s/notify,topic_QXVkaW9Db252ZXJ0",
    $animationStyle,
    $bucketNameEncoded,
    $targetKeyEncoded
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName,      // 存储空间名称
    key: $objectName,         // 对象名称
    asyncProcess: $process    // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 视频拼接

您可以通过视频拼接功能，将多个视频拼接为一个视频并转换为需要的格式。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 填写拼接后的视频文件名称
$targetObject = "dest.mp4";

// 指定需要拼接的视频文件名称
$video1 = "concat1.mp4";
$video2 = "concat2.mp4";

// 构建视频处理的样式字符串以及视频拼接处理参数
$style = sprintf(
    "video/concat,ss_0,f_mp4,vcodec_h264,fps_25,vb_1000000,acodec_aac,ab_96000,ar_48000,ac_2,align_1/pre,o_%s/sur,o_%s,t_0",
    rtrim(base64_encode($video1), '='), // Base64编码第一个视频文件名称并移除末尾的'='
    rtrim(base64_encode($video2), '=')  // Base64编码第二个视频文件名称并移除末尾的'='
);

// 构建异步处理指令
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s/notify,topic_QXVkaW9Db252ZXJ0",
    $style,
    rtrim(base64_encode($bucketName), '='),   // Base64编码存储空间名称并移除末尾的'='
    rtrim(base64_encode($targetObject), '=')  // Base64编码目标文件名称并移除末尾的'='
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 音频转码

您可以通过音频转码功能，将音频转换为需要的格式。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

// 指定转码后的音频文件名称
$targetKey = "dest.aac";

// 构建音频处理样式字符串以及音频转码处理参数
$animationStyle = "audio/convert,ss_10000,t_60000,f_aac,ab_96000";

// 构造异步处理指令 包括保存路径和Base64编码的Bucket名称和目标文件名称
$bucketNameEncoded = base64_encode($bucketName); // Base64编码存储空间名称
$targetKeyEncoded = base64_encode($targetKey);   // Base64编码目标文件名称
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s/notify,topic_QXVkaW9Db252ZXJ0",
    $animationStyle,
    $bucketNameEncoded,
    $targetKeyEncoded
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName,      // 存储空间名称
    key: $objectName,         // 对象名称
    asyncProcess: $process    // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 音频拼接

您可以通过音频拼接功能，将多个音频拼接为一个音频并转换为需要的格式。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

setCredentialsProvider($credentialsProvider);

// 设置区域
$cfg->setRegion($region);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 需要拼接的音频文件名称
$audio1 = "src1.mp3";
$audio2 = "src2.mp3";

// 指定拼接后的音频文件名称
$targetAudio = "dest.aac";

// 构建音频处理的样式字符串以及音频拼接处理参数
$audio1Encoded = base64_encode($audio1); // Base64编码第一个音频文件名称
$audio2Encoded = base64_encode($audio2); // Base64编码第二个音频文件名称
$style = sprintf(
    "audio/concat,f_aac,ac_1,ar_44100,ab_96000,align_2/pre,o_%s/pre,o_%s,t_0",
    $audio1Encoded,
    $audio2Encoded
);

// 构造异步处理指令 包括保存路径和Base64编码的Bucket名称和目标文件名称
$bucketEncoded = base64_encode($bucketName); // Base64编码存储空间名称
$targetEncoded = base64_encode($targetAudio); // Base64编码目标文件名称
$process = sprintf(
    "%s|sys/saveas,b_%s,o_%s/notify,topic_QXVkaW9Db252ZXJ0",
    $style,
    $bucketEncoded,
    $targetEncoded
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName,      // 存储空间名称
    asyncProcess: $process    // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

### 解析图片盲水印

以下代码展示了如何解析图片中的盲水印。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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
$key = $options["key"];       // 对象名称

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

setCredentialsProvider($credentialsProvider);

// 设置区域
$cfg->setRegion($region);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 指定水印图文件名称
$sourceKey = $objectName; // 指定要处理的图片对象名称

// 指定MNS消息的topic
$topic = "imm-blindwatermark-test";

// 提取指定图片中的水印内容
$style = "image/deblindwatermark,s_low,t_text";
$encodedTopic = rtrim(base64_encode($topic), '='); // Base64编码并移除末尾的'='
$process = sprintf(
    "%s|sys/notify,topic_%s",
    $style,
    $encodedTopic
);

// 创建异步处理对象的请求对象
$request = new Oss\Models\AsyncProcessObjectRequest(
    bucket: $bucketName,      // 存储空间名称
    key: $sourceKey,          // 指定要处理的图片名称
    asyncProcess: $process    // 异步处理指令
);

// 调用asyncProcessObject方法异步处理对象
$result = $client->asyncProcessObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL .   // 请求的唯一标识
    'async process result:' . var_export($result, true) . PHP_EOL // 异步处理结果
);

```

## 相关文档
- 关于异步处理功能的更多信息，请参见[异步处理](https://help.aliyun.com/zh/oss/user-guide/asynchronous-processing)。
- 关于异步处理功能的代码示例，请参见[AsyncProcessObject](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/AsyncProcessObject.php)。

[上一篇：同步处理（PHP SDK V2）](/zh/oss/developer-reference/synchronous-processing-using-oss-sdk-for-php-v2)[下一篇：阻止公共访问（PHP SDK V2）](/zh/oss/developer-reference/block-public-access-using-oss-sdk-for-php-v2/)该文章对您有帮助吗？反馈
  
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