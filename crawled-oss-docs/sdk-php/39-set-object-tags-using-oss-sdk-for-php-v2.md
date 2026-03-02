# 使用PHP SDK V2在上传时设置及修改已有对象标签

Source: https://help.aliyun.com/zh/oss/developer-reference/set-object-tags-using-oss-sdk-for-php-v2

---

- 使用PHP SDK V2在上传时设置及修改已有对象标签-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 设置对象标签（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS支持使用对象标签（Object Tagging）对存储空间（Bucket）中的文件（Object）进行分类，本文介绍如何使用PHP SDK V2设置对象标签。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要设置对象标签，您必须具有`oss:PutObjectTagging`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 上传对象时设置标签

### 简单上传时设置对象标签

您可以使用以下代码在上传Object时添加对象标签。

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
$request = new Oss\Models\PutObjectRequest(
            bucket: $bucket,
            key: $key,
            tagging: "key1=value1&key2=value2"); // 设置标签信息

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

### 分片上传时设置对象标签

您可以使用以下代码在分片上传Object时添加对象标签。

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

// 初始化分片上传请求
$request = new Oss\Models\InitiateMultipartUploadRequest(
                bucket: $bucket,
                key: $key,
                tagging:" key1=value1&key2=value2");

$result = $client->initiateMultipartUpload($request);

// 获取分片上传的uploadId
$uploadId = $result->uploadId;

// 创建分片上传请求对象
$request = new Oss\Models\UploadPartRequest(bucket: $bucket, key: $key);

// 定义大文件路径和分片大小
$bigFileName = "/Users/localpath/yourfilename"; // 填写大文件路径
$partSize = 1 * 1024 * 1024; // 分片大小，单位为字节（此处设置为1MB）

// 打开大文件并准备分片上传
$file = fopen($bigFileName, 'r');
$parts = []; // 用于存储每个分片的信息
if ($file) {
    $i = 1; // 分片编号从1开始
    while (!feof($file)) {
        $chunk = fread($file, $partSize); // 读取指定大小的数据块
        // 执行分片上传操作
        $partResult = $client->uploadPart(
            new Oss\Models\UploadPartRequest(
                bucket: $bucket,
                key: $key,
                partNumber: $i, // 分片编号
                uploadId: $uploadId, // 分片上传的uploadId
                contentLength: null,
                contentMd5: null,
                trafficLimit: null,
                requestPayer: null,
                body: Oss\Utils::streamFor(resource: $chunk) // 将数据块转换为流
            )
        );
        // 创建UploadPart对象，记录分片编号和ETag
        $part = new Oss\Models\UploadPart(
            partNumber: $i,
            etag: $partResult->etag,
        );
        array_push(array: $parts, values: $part); // 将分片信息添加到数组中
        $i++; // 分片编号递增
    }
    fclose($file); // 关闭文件句柄
}

// 完成分片上传操作
$comResult = $client->completeMultipartUpload(
    new Oss\Models\CompleteMultipartUploadRequest(
        bucket: $bucket,
        key: $key,
        uploadId: $uploadId, // 分片上传的uploadId
        acl: null,
        completeMultipartUpload: new Oss\Models\CompleteMultipartUpload(
            parts: $parts // 传入所有分片的信息
        ),
    )
);

// 打印完成分片上传的结果
printf(
    'status code:' . $comResult->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $comResult->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'complete multipart upload result:' . var_export($comResult, true) // 完成分片上传的详细结果
);

```

### 追加上传时设置对象标签

您可以使用以下代码在追加上传Object时添加对象标签。

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

// 要追加的数据内容
$data = 'Hello Append Object'; // 示例数据，实际使用时可以替换为其他内容

// 创建AppendObjectRequest对象，用于追加数据到指定对象
$request = new Oss\Models\AppendObjectRequest(
                bucket: $bucket,
                key: $key,
                tagging: "key1=value1&key2=value2");
$request->body = Oss\Utils::streamFor($data); // 设置请求体为数据流
$request->position = 0; // 设置追加操作的起始位置（0表示从头开始）

// 执行追加操作
$result = $client->appendObject($request);

// 打印追加结果
// 输出HTTP状态码和请求ID，用于验证追加是否成功
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $result->requestId . PHP_EOL .    // 请求ID，用于调试或追踪请求
    'next append position:' . $result->nextPosition . PHP_EOL // 下次追加操作的起始位置
);

```

### 拷贝对象时设置对象标签

您可以使用以下代码在拷贝Object时添加对象标签。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 目标Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 目标对象名称（必填）
    "src-bucket" => ['help' => 'The name of the source bucket', 'required' => False], // 源Bucket名称（可选）
    "src-key" => ['help' => 'The name of the source object', 'required' => True], // 源对象名称（必填）
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
$bucket = $options["bucket"]; // 目标Bucket名称
$key = $options["key"];       // 目标对象名称
$srcKey = $options["src-key"]; // 源对象名称

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

// 创建CopyObjectRequest对象，用于复制对象
$request = new Oss\Models\CopyObjectRequest(
            bucket: $bucket,
            key: $key,
            sourceKey: $srcKey,
            sourceBucket: $sourceBucket,
            taggingDirective: "Replace", // copy object时直接替换源object的标签
            tagging:"key1=value1&key2=value2"); // 填写标签值

if (!empty($options["src-bucket"])) {
    $request->sourceBucket = $options["src-bucket"]; // 如果提供了源Bucket名称，则设置sourceBucket
}
$request->sourceKey = $srcKey; // 设置源对象名称

// 执行复制对象操作
$result = $client->copyObject($request);

// 打印复制结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $result->requestId . PHP_EOL     // 请求ID，用于调试或追踪请求
);

```

## 对上传的对象添加或修改标签

### 对已上传对象添加或修改标签

如果上传Object时未添加对象标签或者添加的对象标签不满足使用需求，您可以在上传Object后为Object添加或更改对象标签。

您可以使用以下代码对已上传Object添加或更改对象标签。

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

// 创建PutObjectTaggingRequest对象，用于设置对象的标签信息
$request = new Oss\Models\PutObjectTaggingRequest(
    bucket: $bucket,
    key: $key,
    tagging: new Oss\Models\Tagging(
        tagSet: new Oss\Models\TagSet(
            tags: [
                new Oss\Models\Tag('k1', 'v1'), // 标签键值对：k1=v1
                new Oss\Models\Tag('k2', 'v2')  // 标签键值对：k2=v2
            ]
        )
    )
);

// 执行设置对象标签的操作
$result = $client->putObjectTagging($request);

// 打印设置对象标签的结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $result->requestId . PHP_EOL     // 请求ID，用于调试或追踪请求
);

```

[上一篇：对象标签（PHP SDK V2）](/zh/oss/developer-reference/object-tagging-using-oss-sdk-for-php-v2/)[下一篇：获取对象标签（PHP SDK V2）](/zh/oss/developer-reference/get-object-tags-using-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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