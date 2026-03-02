# 使用PHP SDK V2在开启版本控制后上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-object-in-versioning-bucket-using-oss-sdk-for-php-v2

---

- 使用PHP SDK V2在开启版本控制后上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 上传文件（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何使用PHP SDK V2在开启版本控制的存储空间（Bucket）中上传文件（Object）。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要上传文件，您必须有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 示例代码

### 简单上传
说明 - 在已开启版本控制的Bucket中，OSS会为新添加的Object自动生成唯一的VersionId，并在响应header中通过x-oss-version-id形式返回。
- 在暂停了版本控制的Bucket中，新添加的Object的VersionId为“null”，上传同名Object，后一次会覆盖前一次上传的文件内容。OSS保证同一个Object只会有一个版本的ID为“null”。

您可以使用以下代码进行简单上传。

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 定义要上传的数据内容
$data = 'Hello OSS';

// 创建上传对象的请求对象
$request = new Oss\Models\PutObjectRequest(
                bucket: $bucket,
                key: $key,
            );

// 设置请求体为数据流
$request->body = Oss\Utils::streamFor($data);

// 调用putObject方法上传对象
$result = $client->putObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId . PHP_EOL . // 请求的唯一标识
    'etag:' . $result->etag . PHP_EOL // 对象的ETag值
);

```

### 追加上传

在受版本控制的Bucket中，仅支持对于当前版本为Appendable类型的Object执行追加（AppendObject）操作，不支持对于历史版本为Appendable类型的Object执行AppendObject操作。
说明 - 对当前版本为Appendable类型的Object执行AppendObject操作时，OSS不会为该Appendable类型的Object生成历史版本。
- 对当前版本为Appendable类型的Object执行PutObject或DeleteObject操作时，OSS会将该Appendable类型的Object保留为历史版本，且该Object不允许继续追加。
- 不支持对当前版本为非Appendable类型的Object（包括 Normal Object、Delete Marker等）执行AppendObject 操作。

您可以使用以下代码进行追加上传。

```
 ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名
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

// 如果提供了终端节点 则设置终端节点
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 定义要追加的数据内容
$data = 'Hello Append Object';

// 创建追加对象的请求对象
$request = new Oss\Models\AppendObjectRequest(bucket: $bucket, key: $key);

// 设置请求体为数据流
$request->body = Oss\Utils::streamFor($data);

// 设置追加位置为0 表示从对象开头追加
$request->position = 0;

// 调用appendObject方法追加对象
$result = $client->appendObject($request);

// 打印返回结果
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $result->requestId // 请求的唯一标识
);

```

### 分片上传
说明 
在受版本控制的Bucket中，调用CompleteMultipartUpload接口来完成整个文件的分片上传，OSS会为整个文件生成唯一的版本ID，并在响应header中以x-oss-version-id的形式返回。

您可以使用以下代码进行分片上传。

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
$request = new Oss\Models\InitiateMultipartUploadRequest(bucket: $bucket, key: $key);
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
        array_push($parts, $part); // 将分片信息添加到数组中
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

## 相关文档
- 关于简单上传的更多信息，请参见[PutObject](https://help.aliyun.com/zh/oss/developer-reference/putobject#reference-l5p-ftw-tdb)。
- 关于追加上传的更多信息，请参见[AppendObject](https://help.aliyun.com/zh/oss/developer-reference/appendobject#reference-fvf-xld-5db)。
- 关于分片上传的更多信息，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。

[上一篇：管理版本控制（PHP SDK V2）](/zh/oss/developer-reference/managing-version-control-using-oss-sdk-for-php-v2)[下一篇：下载文件（PHP SDK V2）](/zh/oss/developer-reference/download-object-in-versioning-bucket-using-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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