# 使用PHP SDK V2实现客户端加密上传下载Object

Source: https://help.aliyun.com/zh/oss/developer-reference/php-client-side-encryption

---

- 使用PHP SDK V2实现客户端加密上传下载Object-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 客户端加密（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS客户端加密是在数据上传至OSS之前，由用户在本地对数据进行加密处理，确保只有密钥持有者才能解密数据，增强数据在传输和存储过程中的安全性。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 使用客户端加密功能时，您需要对主密钥的完整性和正确性负责。
- 在对加密数据进行复制或者迁移时，您需要对加密元数据的完整性和正确性负责。

## 使用RSA主密钥

### 使用主密钥RSA简单上传和下载Object

使用主密钥RSA简单上传和下载Object示例代码如下：

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

// 创建主密钥加密器 使用RSA公钥和私钥进行加密解密
$masterCipher = new Oss\Crypto\MasterRsaCipher(
    publicKey: RSA_PUBLIC_KEY, // RSA公钥
    privateKey: RSA_PRIVATE_KEY, // RSA私钥
    matDesc: ['tag' => 'value'] // 加密附加标签
);

// 创建加密客户端实例
$eclient = new Oss\EncryptionClient(client: $client, masterCipher: $masterCipher);

// 创建简单上传对象的请求对象
$putObjRequest = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);

// 调用putObject方法上传对象
$putObjResult = $eclient->putObject(request: $putObjRequest);

// 打印返回结果
printf(
    'put object status code:' . $putObjResult->statusCode . PHP_EOL . // HTTP响应状态码
    'request id:' . $putObjResult->requestId . PHP_EOL // 请求的唯一标识
);

```

### 使用主密钥RSA分片上传Object

使用主密钥RSA分片上传Object示例代码如下：

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

// 创建主密钥加密器 使用RSA公钥和私钥进行加密解密
$masterCipher = new Oss\Crypto\MasterRsaCipher(
    RSA_PUBLIC_KEY, // RSA公钥
    RSA_PRIVATE_KEY, // RSA私钥
    ['tag' => 'value'] // 加密附加标签
);

// 创建加密客户端实例
$eclient = new Oss\EncryptionClient($client, $masterCipher);

// 初始化分片上传请求 设置分片大小和数据总大小
$initRequest = new Oss\Models\InitiateMultipartUploadRequest(bucket: $bucket, key: $key);
$initRequest->cseDataSize = 500 * 1024; // 数据总大小为500KB
$initRequest->csePartSize = 200 * 1024; // 每个分片大小为200KB

// 调用initiateMultipartUpload方法初始化分片上传
$initResult = $eclient->initiateMultipartUpload(request: $initRequest);

// 创建上传分片请求对象
$uploadPartRequest = new Oss\Models\UploadPartRequest(bucket: $bucket, key: $key);

// 定义临时文件名和分片大小
$bigFileName = "upload.tmp"; // 临时文件名
$partSize = 200 * 1024; // 每个分片大小为200KB

// 生成一个500KB的临时文件用于测试
generateFile($bigFileName, 500 * 1024);

// 打开临时文件准备读取
$file = fopen(filename: $bigFileName, mode: 'r');

// 用于存储分片信息的数组
$parts = array();

// 如果文件成功打开 则逐片读取并上传
if ($file) {
    $i = 1; // 分片编号从1开始
    while (!feof(stream: $file)) {
        // 读取一个分片的数据
        $chunk = fread(stream: $file, length: $partSize);

        // 创建上传分片请求对象 并设置分片编号和上传ID
        $uploadPartRequest = new Oss\Models\UploadPartRequest(
            bucket: $bucket,
            key: $key,
            partNumber: $i,
            uploadId: $initResult->uploadId,
            contentLength: null,
            contentMd5: null,
            trafficLimit: null,
            requestPayer: null,
            body: Oss\Utils::streamFor(resource: $chunk) // 将分片数据转换为流
        );

        // 设置加密上下文
        $uploadPartRequest->encryptionMultipartContext = $initResult->encryptionMultipartContext;

        // 调用uploadPart方法上传分片
        $partResult = $eclient->uploadPart($uploadPartRequest);

        // 创建分片信息对象 并添加到分片数组中
        $part = new Oss\Models\UploadPart(
            partNumber: $i,
            etag: $partResult->etag, // 获取分片的ETag
        );
        array_push(array: $parts, values: $part);

        $i++; // 分片编号递增
    }
    fclose(stream: $file); // 关闭文件
}

// 调用completeMultipartUpload方法完成分片上传
$comResult = $eclient->completeMultipartUpload(
    request: new Oss\Models\CompleteMultipartUploadRequest(
        bucket: $bucket,
        key: $key,
        uploadId: $initResult->uploadId,
        acl: null,
        completeMultipartUpload: new Oss\Models\CompleteMultipartUpload(
            parts: $parts
        ),
    )
);

// 删除临时文件
unlink($bigFileName);

// 打印返回结果
printf(
    'complete multipart upload status code:' . $comResult->statusCode . PHP_EOL . // HTTP响应状态码
    'complete multipart upload request id:' . $comResult->requestId . PHP_EOL . // 请求的唯一标识
    'complete multipart upload result:' . var_export($comResult, true) // 完成分片上传的结果
);

// 生成指定大小的文件 用于测试分片上传
function generateFile($filename, $size)
{
    // 如果文件已存在且大小符合要求 则直接返回
    if (
        file_exists($filename) &&
        $size == sprintf('%u', filesize($filename))
    ) {
        return;
    }

    $part_size = 32; // 每次写入的块大小为32字节
    $fp = fopen($filename, "w"); // 打开文件以写入模式
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'; // 字符集

    $charactersLength = strlen($characters); // 字符集长度

    // 如果文件成功打开 则循环写入数据直到达到指定大小
    if ($fp) {
        while ($size > 0) {
            // 计算本次写入的大小
            if ($size 
## 使用自定义主密钥

### 使用自定义主密钥简单上传和下载Object

SDK提供了RSA默认实现， 当这个方式不满足用户的需求时，用户可以自己实现主密钥的加解密行为。以下示例代码以阿里云KMS 3.0为例，演示如何自定义主密钥加解密进行简单上传和下载Object。

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
$key = $options["key"]; // 对象名称

// 使用环境变量加载凭证信息 AccessKeyId 和 AccessKeySecret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 自定义KMS加密解密类 实现MasterCipherInterface接口
class KmsCipher implements Oss\Crypto\MasterCipherInterface
{
    private $matDesc;
    private ?KmsClient $kmsClient;
    private ?string $keyId;
    private ?string $algorithm;

    public function __construct(
        $matDesc = null,
        ?string $keyId = null,
        ?KmsClient $kmsClient = null,
        ?string $algorithm = null
    )
    {
        $this->keyId = $keyId;
        $this->matDesc = null;
        if (\is_array($matDesc)) {
            $val = json_encode($matDesc);
            if ($val !== false) {
                $this->matDesc = $val;
            }
        } else if (is_string($matDesc)) {
            $this->matDesc = $matDesc;
        }

        $this->kmsClient = $kmsClient;
        $this->algorithm = $algorithm;
    }

    // 加密方法
    public function encrypt(string $data): string
    {
        $encryptRequest = new \AlibabaCloud\Dkms\Gcs\Sdk\Models\AdvanceEncryptRequest();
        $encryptRequest->algorithm = $this->algorithm;
        $encryptRequest->keyId = $this->keyId;
        $encryptRequest->plaintext = \AlibabaCloud\Tea\Utils\Utils::toBytes($data);
        $runtimeOptions = new \AlibabaCloud\Dkms\Gcs\OpenApi\Util\Models\RuntimeOptions();
        $encryptResponse = $this->kmsClient->advanceEncryptWithOptions($encryptRequest, $runtimeOptions);
        return base64_decode((string)$encryptResponse->ciphertextBlob);
    }

    // 解密方法
    public function decrypt(string $data): string
    {
        $decryptRequest = new \AlibabaCloud\Dkms\Gcs\Sdk\Models\AdvanceDecryptRequest();
        $decryptRequest->keyId = $this->keyId;
        $decryptRequest->ciphertextBlob = $data;
        $decryptRequest->algorithm = $this->algorithm;
        $runtimeOptions = new \AlibabaCloud\Dkms\Gcs\OpenApi\Util\Models\RuntimeOptions();
        $decryptResponse = $this->kmsClient->advanceDecryptWithOptions($decryptRequest, $runtimeOptions);
        return base64_decode((string)$decryptResponse->plaintext);
    }

    // 获取包装算法
    public function getWrapAlgorithm(): string
    {
        return "KMS/ALICLOUD";
    }

    public function getMatDesc(): string
    {
        return $this->matDesc;
    }
}

/**
 * 构建专属KMS SDK Client对象
 * @return KmsClient
 */
function getDkmsGcsSdkClient()
{
    global $clientKeyFile, $password, $endpoint;
    // 构建专属KMS SDK Client配置
    $config = new \AlibabaCloud\Dkms\Gcs\OpenApi\Models\Config();
    $config->protocol = 'https';
    $config->clientKeyFile = $clientKeyFile;
    $config->password = $password;
    $config->endpoint = $endpoint;
    // 验证服务端证书
    $config->caFilePath = 'path/to/caCert.pem';
    // 构建专属KMS SDK Client对象
    return new \AlibabaCloud\Dkms\Gcs\Sdk\Client($config);
}

// 填写您在KMS应用管理获取的ClientKey文件路径
$clientKeyFile = '';
// 填写您在KMS应用管理创建ClientKey时输入的加密口令
$password = '';
// 填写您的专属KMS实例服务地址
$endpoint = '';
// 填写您在KMS创建的主密钥Id
$kmsKeyId = '';
// 加解密算法
$algorithm = '';

// 专属KMS SDK Client对象
$kmsClient = getDkmsGcsSdkClient();

$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);
if (isset($options["endpoint"])) {
    $cfg->setEndpoint($options["endpoint"]);
}

$client = new Oss\Client($cfg);
$materialDesc = ['desc' => 'your kms encrypt key material describe information'];
$masterKmsCipher = new KmsCipher($materialDesc, $kmsKeyId, $kmsClient, $algorithm);
$eClient = new \AlibabaCloud\Oss\V2\EncryptionClient($client, $masterKmsCipher);

$eClient->putObject(new Oss\Models\PutObjectRequest(
    bucket: $bucket,
    key: $key,
    body: Oss\Utils::streamFor('hi kms')
));

$result = $eClient->getObject(new Oss\Models\GetObjectRequest(
    bucket: $bucket,
    key: $key,
));

$data = $result->body->getContents();
echo "get object data: " . $data;

```

## 相关文档
- 关于OSS客户端加密实现的原理，请参见[客户端加密](https://help.aliyun.com/zh/oss/user-guide/client-side-encryption)。
- 关于使用主密钥RSA简单上传和下载Object的完整代码示例，请参见[Github示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/EncryptionClient.php)。

[上一篇：服务端加密（PHP SDK V2）](/zh/oss/developer-reference/php-server-side-encryption)[下一篇：数据管理（PHP SDK V2）](/zh/oss/developer-reference/data-management-using-oss-sdk-for-php-v2/)该文章对您有帮助吗？反馈
  
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