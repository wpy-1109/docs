# 从PHP SDK V1升级到PHP SDK V2

Source: https://help.aliyun.com/zh/oss/developer-reference/php-sdk-v1-to-v2-migration-guide

---

- 从PHP SDK V1升级到PHP SDK V2-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# PHP SDK V1到V2迁移指南
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS PHP SDK V2版是对V1版的全面重构，简化了身份验证、请求重试和错误处理等底层操作，提供更灵活的参数配置和新的高级接口（如分页器、文件上传/下载管理器）。本文介绍如何从PHP SDK V1版本迁移到PHP SDK V2 版本。

## 完整迁移步骤

### 第一步：环境准备
- 评估现有代码：梳理现有代码中使用OSS SDK的位置
- 记录您使用了哪些OSS功能和接口
- 确定依赖关系，避免迁移过程中出现意外问题
- 更新PHP运行环境：V2版本要求PHP的运行环境版本最低为7.4。
- 保留V1版SDK以便逐步迁移，安装V2版SDK：通过 composer 安装如果您通过composer管理您的项目依赖，可以在你的项目根目录运行：
```
composer require alibabacloud/oss-v2
```
或者在`composer.json`中声明对Alibaba Cloud OSS SDK for PHP v2的依赖：
```
"require": {    "alibabacloud/oss-v2": "*"
}
```
然后通过`composer install`命令安装依赖
- ### 通过PHAR 文件安装

```
require_once '/path/to/alibabacloud-oss-php-sdk-v2-{version}.phar'
```
- 创建测试环境：建议创建独立的测试环境，而不是直接在生产环境修改
- 配置测试数据和测试用例，用于验证迁移后的代码

### 第二步：修改导入语句

#### 功能变更

PHP SDK V2版本启用了新的代码仓库（[alibabacloud-oss-php-sdk-v2](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/tree/master)），并对代码结构进行了优化调整。此次调整按照功能模块对代码进行了重新组织，旨在提升代码的可读性和维护性。以下是各个模块的路径及其相应说明：
| 模块路径 | 说明|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src | SDK核心，基础接口和高级接口实现|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Credentials | 访问凭证相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Retry | 重试相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Signer | 签名相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Annotation | tag，xml 转换相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Crypto | 客户端加密相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Models | 请求对象，返回对象相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Paginator | 列表分页器相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Exception | 异常类型相关|
| github.com/aliyun/alibabacloud-oss-php-sdk-v2/src/Types | 类型相关|

#### 代码示例

```
# V1版
require_once 'vendor/autoload.php';
use OSS\OssClient;

# V2版
require_once  'vendor/autoload.php';
use AlibabaCloud\Oss\V2 as Oss;

```

### 第三步：修改创建客户端代码

#### 功能变更
- V2 版本简化了配置设置方式，全部迁移到 [config](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/src/Config.php)下，并提供了以set为前缀的辅助函数，方便以编程方式覆盖缺省配置
- V2版本默认采用V4签名算法，因此在配置客户端时必须指定阿里云通用Region ID作为发起请求地域的标识。
- V2版本支持根据所选区域（Region）自动生成访问域名（Endpoint）。当您访问公网域名时，无需手动设置Endpoint，系统将自动依据您的区域信息进行构造。

#### 代码示例

#### V1版示例

```
require_once 'vendor/autoload.php';
use OSS\OssClient;
...

// 环境变量中获取访问凭证
$provider = new \OSS\Credentials\EnvironmentVariableCredentialsProvider();

// Endpoint
$endpoint = "http://oss-cn-hangzhou.aliyuncs.com";

$config = array(
       "provider" => $provider,
       "endpoint" => $endpoint,
       "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
       "region" => "cn-hangzhou"
   );
$ossClient = new OssClient($config);
// 不校验SSL证书校验
$ossClient->setUseSSL(false);
```

#### V2版示例

在V2版中，使用新的配置加载方式，需先创建cfg并注入region等信息。

```
require_once 'vendor/autoload.php';
use AlibabaCloud\Oss\V2 as Oss;
...

// 环境变量中获取访问凭证
$provider = new \OSS\Credentials\EnvironmentVariableCredentialsProvider();

$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
// 设置HTTP连接超时时间为20秒
$cfg->setConnectTimeout(20);
// HTTP读取或写入超时时间为60秒
$cfg->setReadWriteTimeout(60);
// 不校验SSL证书校验
$cfg->setDisableSSL(true);
// 设置区域
$cfg->setRegion('cn-hangzhou');
$client = new Oss\Client($cfg);
```

关于V2版配置客户端的更多详细示例，请参见[配置客户端](https://help.aliyun.com/zh/oss/developer-reference/configure-client-using-oss-sdk-for-php-v2)。

关于V2版配置访问凭证的更多详细示例，请参见[配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。

### 第四步：修改基础API调用方式

#### 功能变更
- SDK V2版本提供了与REST API对应的接口，把这类接口叫做基础接口或者低级别API。您可以通过这些接口访问OSS的服务，例如创建存储空间，上传文件和下载文件等。
- 在V2版本中，各个基础API接口遵循一套标准化的命名规则。每个操作方法均命名为<OperationName>形式，其中，操作的请求参数类被定义为<OperationName>Request，而操作的结果返回值则定义为<OperationName>Result，如下所示。
```
public function (Models\Request $request, array $args = []): Models\Result
public function Async(Models\Request $request, array $args = []): \GuzzleHttp\Promise\Promise
```

关于基础API的更多详细说明，请参考[开发者指南-基础接口](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E5%9F%BA%E7%A1%80%E6%8E%A5%E5%8F%A3)。

#### 代码示例

V1版示例

```
require_once 'vendor/autoload.php';
use OSS\OssClient;
$provider = new \OSS\Credentials\EnvironmentVariableCredentialsProvider();
$endpoint = "http://oss-cn-hangzhou.aliyuncs.com";
$config = array(
    "provider" => $provider,
    "endpoint" => $endpoint,
    "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
    "region" => "cn-hangzhou"
);
$ossClient = new OssClient($config);
$ossClient->putObject('examplebucket','exampleobject.txt','example data');
```

V2版示例

```
require_once 'vendor/autoload.php';
use AlibabaCloud\Oss\V2 as Oss;

$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion('cn-hangzhou');
$ossClient = new Oss\Client($cfg);

$client->putObject(
    new Oss\Models\PutObjectRequest(
        bucket: 'examplebucket',
        key: 'exampleobject.txt',
        body:  Oss\Utils::streamFor('example data'),
    ),
);
```

关于V2版基础API的更多示例代码，请参见[对象/文件](https://help.aliyun.com/zh/oss/developer-reference/object-file-with-oss-sdk-for-php-v2/)。

### 第五步：修改高级API调用方式（可选）

#### 预签名接口

##### 功能变更点

V2版本把预签名接口名称从sign_url修改为presign，接口形式如下：

```
public function presign(request: $request,args: $options): Models\PresignResult
```

对于request参数，其类型与API接口中的'<OperationName>Request' 一致。

对于返回结果，除了返回预签名URL外，还返回HTTP方法，过期时间和被签名的请求头，如下：

```
final class PresignResult
{
    public ?string $method;
    
    public ?string $url;
    
    public ?\DateTime $expiration;
    
    public ?array $signedHeaders;
}
```

关于V2版预签名接口的详细使用说明，请参考[开发者指南-预签名接口](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E9%A2%84%E7%AD%BE%E5%90%8D)。

##### 代码示例

V1版示例

```
require_once 'vendor/autoload.php';
use OSS\OssClient;
$provider = new \OSS\Credentials\EnvironmentVariableCredentialsProvider();
$endpoint = "http://oss-cn-hangzhou.aliyuncs.com";
$config = array(
    "provider" => $provider,
    "endpoint" => $endpoint,
    "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4,
    "region" => "cn-hangzhou"
);
$ossClient = new OssClient($config);
$url = $ossClient->signUrl('examplebucket','exampleobject.txt',60,OssClient::OSS_HTTP_GET);

printf("Sign Url:%s\n", $url);
```

V2版示例

```
require_once 'vendor/autoload.php';
use AlibabaCloud\Oss\V2 as Oss;

$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion('cn-hangzhou');
$ossClient = new Oss\Client($cfg);

$result = $ossClient->presign(
    new Oss\Models\GetObjectRequest(
        bucket: 'examplebucket',
        key: 'exampleobject.txt',
    ),
    args: ['expiration' => (new \DateTime('now', new \DateTimeZone('UTC')))->add(new DateInterval('PT60S'))],
);
print(
    'sign url:' . $result->url . PHP_EOL .
    'sign method :' . $result->method . PHP_EOL .
    'sign expiration:' . var_export($result->expiration, true) . PHP_EOL .
    'sign headers:' . var_export($result->signedHeaders, true) . PHP_EOL
);
```

关于V2版使用预签名URL上传文件的完整示例代码，请参见[使用预签名URL上传](https://help.aliyun.com/zh/oss/developer-reference/upload-object-using-a-presigned-url-for-php-sdk-v2)。

关于V2版使用预签名URL下载文件的完整示例代码，请参见[使用预签名URL下载](https://help.aliyun.com/zh/oss/developer-reference/download-using-a-presigned-url-for-php-sdk-v2)。

#### 文件传输管理器

##### 变更点

V2版本使用传输管理器'Uploader'，'Downloader' 和'Copier'分别管理对象的上传，下载和拷贝。 关于V2版文件传输管理器的详细使用说明，请参考[开发者指南-传输管理器](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E4%BC%A0%E8%BE%93%E7%AE%A1%E7%90%86%E5%99%A8)。

##### 代码示例
- 文件上传管理器：
```
...
$client = new Oss\Client($cfg);
$u = $client->newUploader();
$result = $u->uploadFile(
    new Oss\Models\PutObjectRequest(
        bucket: 'bucket',
        key: 'key'
    ),
    filepath: '/local/dir/example',
);
printf(
    'upload file status code:' . $result->statusCode . PHP_EOL .
    'upload file request id:' . $result->requestId . PHP_EOL .
    'upload file result:' . var_export($result, true) . PHP_EOL
);
```
关于V2版文件上传管理器的更多详细说明，请参见[开发者指南-文件上传管理器](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E4%B8%8A%E4%BC%A0%E7%AE%A1%E7%90%86%E5%99%A8uploader)。关于V2版文件上传管理器的完整示例代码，请参见[文件上传管理器](https://help.aliyun.com/zh/oss/developer-reference/file-uploader-with-oss-sdk-for-php-v2)。
- 文件下载管理器：
```
...
$client = new Oss\Client($cfg);
$d = $client->newDownloader();
$d->downloadFile(
    new Oss\Models\GetObjectRequest(
        bucket: 'bucket',
        key: 'key'
    ),
    filepath: '/local/dir/example',
);
```
关于V2版文件下载管理器的更多详细说明，请参见[开发者指南-文件下载管理器](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E4%B8%8B%E8%BD%BD%E7%AE%A1%E7%90%86%E5%99%A8downloader)。关于V2版文件下载管理器的完整示例代码，请参见[文件下载管理器](https://help.aliyun.com/zh/oss/developer-reference/file-downloader-with-oss-sdk-for-php-v2)。
- 文件拷贝管理器：
```
...
$client = new Oss\Client($cfg);
$c = $client->newCopier();
$result = $c->copy(
    new Oss\Models\CopyObjectRequest(
        bucket: 'bucket',
        key: 'key',
        sourceBucket: 'src-bucket',
        sourceKey: 'src-key',
    )
);
printf(
    'status code:' . $result->statusCode . PHP_EOL .
    'request id:' . $result->requestId . PHP_EOL .
    'result:' . var_export($result, true)
);
```
关于V2版文件拷贝管理器的更多详细说明，请参见[开发者指南-文件拷贝管理器](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E6%8B%B7%E8%B4%9D%E7%AE%A1%E7%90%86%E5%99%A8copier)。关于V2版文件拷贝管理器的完整示例代码，请参见[文件拷贝管理器](https://help.aliyun.com/zh/oss/developer-reference/file-copy-manager-using-oss-sdk-for-php-v2)。

### 第六步：测试和验证
- 编写单元测试：为确保迁移后功能的正确性，您需要为每个迁移的功能编写详细的单元测试案例。这些测试应涵盖所有关键操作，并验证其行为与旧版SDK保持一致。重点包括：基础功能测试：如创建资源、查询状态、更新数据和删除资源等。
- 边界条件测试：测试极端情况下的应用行为，例如处理极大或极小的数据集、异常输入等。
- 错误处理测试：确保在出现错误时（如网络超时、无效输入），应用能够正确处理并给出合适的反馈。
- 增量测试：采用增量式的方法进行迁移和测试，可以有效降低风险：选择一个小模块开始：先从一个相对独立且不复杂的小模块开始迁移，并为其编写完整的测试案例。
- 进行全面测试：在确认该模块迁移成功且所有测试通过后，再逐步迁移到其他部分。这种方法有助于及时发现并解决问题，避免大规模回滚。
- 兼容性测试：确保新版本SDK与您的整个技术栈及其他依赖项兼容至关重要：内部系统兼容性：验证新版本是否与现有的内部系统和架构兼容。
- 第三方服务兼容性：如果您的应用依赖于第三方服务或API，请确保这些接口与V2 SDK兼容，并按照预期工作。
- 环境兼容性：在不同的操作系统和运行环境中测试您的应用，确保V2 SDK在各种环境下都能正常运行。
- 性能测试：在完成代码迁移后，必须对应用的性能进行全面评估：基准测试：建立性能基准，记录当前应用的响应时间、吞吐量等关键指标。
- 对比分析：迁移完成后，使用相同的负载进行测试，比较新旧版本之间的性能差异，确保性能没有显著下降。
- 调优：如果发现性能有所退步，可以通过调整配置参数、优化代码逻辑等方式进行改进。

## V1与V2版本差异汇总
| 差异点 | V1 | V2|
| PHP版本要求 | - 使用PHP 5.3及以上版本 | - 使用PHP 7.4及以上版本
- 对于Bucket类接口需要使用PHP 8.0及以上版本|
| SDK获取 | ```
composer require aliyuncs/oss-sdk-php
``` | ```
composer require alibabacloud/oss-v2
```|
| 签名算法 | - 默认使用V1签名算法 | - 默认使用V4签名算法
- 必须配置区域（Region）|
| 配置加载 | - 配置设置的方法分散在多处
- 默认使用V1签名算法，区域（Region）非必填
- 必须填写访问域名（Endpoint） | - 简化了配置设置方式，全部迁移到 [config](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/src/Config.php)下，可以以编程方式覆盖缺省配置
- 默认使用V4签名算法，必须配置区域（Region）
- 支持从区域（Region）信息构造访问域名（Endpoint）, 当访问的是公网域名时，可以不设置Endpoint|
| API 调用方式 | - API接口未统一接口命名规范 | - 各基础接口采用了统一命名规范，具体规则请参见[基础接口](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E5%9F%BA%E7%A1%80%E6%8E%A5%E5%8F%A3)|
| 预签名接口 | - 预签名接口：`$ossClient->signUrl()`
- 返回结果：预签名URL | - 预签名接口：`$client->presign()`
- 返回结果：预签名URL，HTTP方法，过期时间，被签名的请求头|
| 断点续传接口 | / | - 文件上传管理器：`$client->newUploader()`
- 文件下载管理器：`$client->newDownloader()`
- 文件拷贝管理器：`$client->newCopier()`|
| 重试机制 | 需要自定义重试逻辑 | 默认开启对HTTP请求的重试行为|

## 相关文档

关于PHP SDK V1迁移到V2的更多详细内容，请参见[开发者指南-迁移指南](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md#%E8%BF%81%E7%A7%BB%E6%8C%87%E5%8D%97)。

[上一篇：Bucket级别阻止公共访问（PHP SDK V2）](/zh/oss/developer-reference/blocking-public-access-at-the-bucket-level-using-oss-sdk-for-php-v2)[下一篇：OSS PHP SDK V1](/zh/oss/developer-reference/preface-3/)该文章对您有帮助吗？反馈
  
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