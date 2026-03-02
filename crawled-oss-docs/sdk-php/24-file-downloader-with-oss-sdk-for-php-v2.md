# 使用PHPSDKV2下载管理器实现文件并发下载和断点续传

Source: https://help.aliyun.com/zh/oss/developer-reference/file-downloader-with-oss-sdk-for-php-v2

---

- 使用PHPSDKV2下载管理器实现文件并发下载和断点续传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 文件下载管理器（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文针对文件的传输场景，介绍如何使用PHP SDK V2新增的下载管理器Downloader模块进行文件下载。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以从环境变量读取访问凭证为例。更多配置访问凭证的示例，请参见[PHP配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。
- 要进行文件下载，您必须有`oss:GetObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 方法定义

#### 下载管理器功能简介

PHP SDK V2新增下载管理器Downloader提供了通用的下载接口，隐藏了底层接口的实现细节，提供便捷的文件下载能力。
- 下载管理器Downloader底层利用范围下载，把文件自动分成多个较小的分片进行并发下载，提升下载的性能。
- 下载管理器Downloader同时提供了断点续传的能力，即在下载过程中，记录已完成的分片状态，如果出现网络中断、程序异常退出等问题导致文件下载失败，甚至重试多次仍无法完成下载，再次下载时，可以通过断点记录文件恢复下载。

下载管理器Downloader的常用方法如下：

```
final class Downloader
{
	...
    public function __construct($client, array $args = [])
    
    public function downloadFile(Models\GetObjectRequest $request, string $filepath, array $args = []): Models\DownloadResult   
    
    public function downloadTo(Models\GetObjectRequest $request, \Psr\Http\Message\StreamInterface $stream, array $args = []): Models\DownloadResult
}
```

#### 请求参数列表
| 参数名 | 类型 | 说明|
| request | GetObjectRequest | 下载对象的请求参数，和 GetObject 接口的 请求参数一致|
| filePath | string | 本地文件路径|
| args | array | （可选）配置选项|

其中，args常用参数说明列举如下：
| 参数名 | 类型 | 说明|
| part_size | int | 指定分片大小，默认值为 6MiB|
| parallel_num | int | 指定下载任务的并发数，默认值为 3。针对的是单次调用的并发限制，而不是全局的并发限制|
| use_temp_file | bool | 下载文件时，是否使用临时文件，默认使用。先下载到临时文件上，当成功后，再重命名为目标文件|

当使用Downloader实例化实例时，您可以指定多个配置选项来自定义对象的下载行为。也可以在每次调用下载接口时，指定多个配置选项来自定义每次下载对象的行为。
- 设置Downloader的配置参数：
```
$d = $client->newDownloader(['part_size' => 10 * 1024 * 1024]);
```
- 设置每次下载请求的配置参数：
```
$d->downloadFile(
    new Oss\Models\GetObjectRequest(
        bucket: 'bucket',
        key: 'key'
    ),
    filepath: '/local/dir/example',
    args: ['part_size' => 10 * 1024 * 1024]
);
```

## 示例代码

您可以使用以下代码将存储空间中的文件下载到本地。

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

// 创建下载器实例
$downloader = $client->newDownloader();

// 定义本地文件路径，用于保存下载的内容
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径
touch($filename); // 创建一个空文件，确保文件存在

// 执行分片下载操作
$result = $downloader->downloadFile(
    new Oss\Models\GetObjectRequest(
        bucket: $bucket,
        key: $key
    ),
    $filename
);

// 打印下载结果
printf(
    'download status code:' . $result->statusCode . PHP_EOL .
    'download request id:' . $result->requestId . PHP_EOL .
    'download result:' . var_export($result, true) . PHP_EOL
);

```

## 常见使用场景

### 使用下载管理器设置分片大小和并发数

您可以使用以下代码配置下载管理器，设置分片大小和并发数。

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

// 创建下载器实例
$downloader = $client->newDownloader();

// 定义分片下载的相关参数
$partSize = 100 * 1024; // 分片大小，单位为字节（此处设置为100KB）

// 定义本地文件路径，用于保存下载的内容
$filename = "/Users/yourLocalPath/yourFileName"; // 示例文件路径
touch($filename); // 创建一个空文件，确保文件存在

// 执行分片下载操作
$result = $downloader->downloadFile(
    new Oss\Models\GetObjectRequest(
        bucket: $bucket,
        key: $key
    ),
    $filename,
    args: [ // 可选参数，用于自定义分片下载行为
        'part_size' => $partSize, // 自定义分片大小
        'parallel_num' => 1,      // 并发下载的分片数量
    ]
);

// 打印下载结果
printf(
    'download status code:' . $result->statusCode . PHP_EOL .
    'download request id:' . $result->requestId . PHP_EOL .
    'download result:' . var_export($result, true) . PHP_EOL
);

```

### 使用下载管理器下载到流中

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

// 创建下载器实例
$downloader = $client->newDownloader();

// 定义一个缓冲流，用于存储下载的内容
$stream = new \GuzzleHttp\Psr7\BufferStream(1 * 1024 * 1024); // 缓冲区大小为1MB

// 执行下载操作，将对象内容下载到缓冲流中
$result = $downloader->downloadTo(
    request: new Oss\Models\GetObjectRequest(
        bucket: $bucket,
        key: $key // 指定要下载的对象名称
    ),
    stream: $stream, // 指定目标流，用于存储下载的内容
);

// 打印下载的内容
printf(
    'download to body:' . $stream->getContents() . PHP_EOL // 输出缓冲流中的内容
);

```

## 相关文档
- 关于下载管理器的完整示例，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Downloader.php)。

[上一篇：使用预签名URL下载（PHP SDK V2）](/zh/oss/developer-reference/download-using-a-presigned-url-for-php-sdk-v2)[下一篇：拷贝文件（PHP SDK V2）](/zh/oss/developer-reference/copy-file-using-oss-sdk-for-php-v2/)该文章对您有帮助吗？反馈
  
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