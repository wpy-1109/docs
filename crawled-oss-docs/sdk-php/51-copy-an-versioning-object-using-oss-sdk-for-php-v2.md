# 使用PHPSDKV2对版本控制对象进行拷贝与分片拷贝

Source: https://help.aliyun.com/zh/oss/developer-reference/copy-an-versioning-object-using-oss-sdk-for-php-v2

---

- 使用PHPSDKV2对版本控制对象进行拷贝与分片拷贝-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 拷贝文件（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何在开启版本控制的存储空间（Bucket）中拷贝文件（Object）。您可以通过CopyObject的方法拷贝小于1 GB的文件，通过分片拷贝（UploadPartCopy）的方法拷贝大于1 GB的文件。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 要拷贝文件，您必须有`oss:GetObject`和`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 示例代码

### 拷贝对象
说明 
对于小于1 GB的文件，您可以通过CopyObject方法将文件从一个存储空间（源存储空间）复制到同一地域的另一个存储空间（目标存储空间）。
- x-oss-copy-source默认拷贝Object的当前版本。如果当前版本是删除标记，则返回404表示该Object不存在。您可以在x-oss-copy-source中加入versionId来拷贝指定的Object版本，删除标记不能被拷贝。
- 您可以将Object的早期版本拷贝到同一个Bucket中，拷贝Object的历史版本将会成为一个新的当前版本，达到恢复Object早期版本的目的。
- 如果目标Bucket已开启版本控制，OSS将会为新拷贝出来的Object自动生成唯一的versionId，此versionId将会在响应header的x-oss-version-id中返回。如果目标Bucket未曾开启或者暂停了版本控制，OSS将会为新拷贝的Object自动生成versionId为“null”的版本，且会覆盖原先versionId为“null”的版本。

您可以使用以下代码进行拷贝对象。

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
            sourceVersionId: "yourVersionId",//填写实际的源对象的版本ID
);

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

### 分片拷贝
说明 
对于大于1GB的文件，需要使用分片拷贝（UploadPartCopy）。
- UploadPartCopy默认从一个已存在的Object的当前版本中拷贝数据来上传一个Part。允许通过在UploadPartCopyRequest中附带SourceVersionId参数，实现从Object的指定版本进行拷贝。
- 如果未指定versionId且拷贝Object的当前版本为删除标记，OSS将返回404 Not Found。通过指定versionId来拷贝删除标记时，OSS将返回400 Bad Request。

您可以使用以下代码进行分片拷贝对象。

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
// 设置默认访问域名
$cfg->setEndpoint('http://oss-cn-hangzhou.aliyuncs.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 初始化分片拷贝任务
$initRequest = new Oss\Models\InitiateMultipartUploadRequest(bucket: $bucket, key: $key);
$initResult = $client->initiateMultipartUpload($initRequest);

// 确定源Bucket名称
if (!empty($options["src-bucket"])) {
    $sourceBucket = $options["src-bucket"];
} else {
    $sourceBucket = $bucket;
}

// 获取源对象的元数据信息
$headResult = $client->headObject(new Oss\Models\HeadObjectRequest(
    bucket: $sourceBucket,
    key: $srcKey
));

// 获取源对象的大小
$length = $headResult->contentLength;

// 定义分片大小和计算分片数量
$partSize = 1024 * 1024; // 分片大小，单位为字节（此处设置为1MB）
$partsNum = intdiv(num1: $length, num2: $partSize) + intval(1); // 计算分片数量，向上取整

// 初始化分片列表
$parts = array();

// 遍历每个分片并执行分片复制操作
for ($i = 1; $i uploadId,
        sourceVersionId:"yourVersionId",//填写实际的源对象的版本ID
    );

    // 设置分片的范围
    $partRequest->sourceRange = getPartRange(totalSize: $length, partSize: $partSize, partNumber: $i);

    // 设置源Bucket名称（如果提供了源Bucket）
    if (!empty($options["src-bucket"])) {
        $partRequest->sourceBucket = $options["src-bucket"];
    }

    // 设置源对象名称
    $partRequest->sourceKey = $srcKey;

    // 执行分片复制操作
    $partResult = $client->uploadPartCopy($partRequest);

    // 创建分片信息并添加到分片列表
    $part = new Oss\Models\UploadPart(
        partNumber: $i,
        etag: $partResult->etag,
    );
    array_push($parts, $part);
}

// 完成分片拷贝任务
$comResult = $client->completeMultipartUpload(
    new Oss\Models\CompleteMultipartUploadRequest(
        bucket: $bucket,
        key: $key,
        uploadId: $initResult->uploadId,
        completeMultipartUpload: new Oss\Models\CompleteMultipartUpload(
            parts: $parts
        ),
    )
);

// 打印完成分片拷贝的结果
printf(
    'status code:' . $comResult->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $comResult->requestId . PHP_EOL .   // 请求ID，用于调试或追踪请求
    'result:' . var_export($comResult, true) . PHP_EOL  // 完成分片拷贝的详细结果
);

/**
 * 获取分片的字节范围
 *
 * @param int $totalSize 对象的总大小
 * @param int $partSize 分片大小
 * @param int $partNumber 当前分片编号
 * @return string 返回分片的字节范围字符串
 */
function getPartRange(int $totalSize, int $partSize, int $partNumber): string
{
    $start = ($partNumber - 1) * $partSize; // 计算分片起始位置
    $end = min($partNumber * $partSize - 1, $totalSize - 1); // 计算分片结束位置
    return sprintf('bytes %d-%d', $start, $end); // 格式化为字节范围字符串
}

```

[上一篇：下载文件（PHP SDK V2）](/zh/oss/developer-reference/download-object-in-versioning-bucket-using-oss-sdk-for-php-v2)[下一篇：删除文件（PHP SDK V2）](/zh/oss/developer-reference/delete-an-versioning-object-using-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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