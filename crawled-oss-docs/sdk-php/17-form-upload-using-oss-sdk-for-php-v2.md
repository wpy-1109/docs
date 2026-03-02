# 使用PHP SDK表单上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/form-upload-using-oss-sdk-for-php-v2

---

- 使用PHP SDK表单上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 表单上传（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS表单上传允许网页应用通过标准HTML表单直接将文件上传至OSS。本文介绍如何使用PHP SDK V2生成Post签名和Post Policy等信息，并调用HTTP Post方法上传文件到OSS。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 通过表单上传的方式上传的Object大小不能超过5 GB。
- 本文以从环境变量读取访问凭证为例。更多配置访问凭证的示例，请参见[PHP配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。

## 示例代码

以下代码示例实现了表单上传的完整过程，主要步骤如下：
- 创建Post Policy：定义上传请求的有效时间和条件，包括存储桶名称、签名版本、凭证信息、请求日期和请求体长度范围。
- 序列化并编码Policy：将Policy序列化为JSON字符串，并进行Base64编码。
- 生成签名密钥：使用HMAC-SHA256算法生成签名密钥，包括日期、区域、产品和请求类型。
- 计算签名：使用生成的密钥对Base64编码后的Policy字符串进行签名，并将签名结果转换为十六进制字符串。
- 构建请求体：创建一个multipart表单写入器，添加对象键、策略、签名版本、凭证信息、请求日期和签名到表单中，并将要上传的数据写入表单。
- 创建并执行请求：创建一个HTTP POST请求，设置请求头，并发送请求，检查响应状态码确保请求成功。

```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
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
$product = 'oss';             // 固定为OSS服务

// 加载环境变量中的凭证信息
// 使用EnvironmentVariableCredentialsProvider从环境变量中读取Access Key ID和Access Key Secret
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();
$cred = $credentialsProvider->getCredentials();

// 要上传的数据内容
$data = 'hi oss'; // 示例数据，实际使用时可以替换为其他内容

// 获取当前UTC时间并格式化
$utcTime = new DateTime('now', new DateTimeZone('UTC'));
$date = $utcTime->format('Ymd'); // 当前日期，用于签名计算
$expiration = clone $utcTime;
$expiration->add(new DateInterval('PT1H')); // 设置过期时间为1小时后

// 构建Policy文档
$policyMap = [
    "expiration" => $expiration->format('Y-m-d\TH:i:s.000\Z'), // Policy的过期时间
    "conditions" => [
        ["bucket" => $bucket], // 指定Bucket名称
        ["x-oss-signature-version" => "OSS4-HMAC-SHA256"], // 签名版本
        ["x-oss-credential" => sprintf("%s/%s/%s/%s/aliyun_v4_request",
            $cred->getAccessKeyId(), $date, $region, $product)], // 凭证信息
        ["x-oss-date" => $utcTime->format('Ymd\THis\Z')], // 当前时间戳
        // 其他条件
        ["content-length-range", 1, 1024], // 文件大小范围限制
        // ["eq", "$success_action_status", "201"], // 可选：指定成功状态码
        // ["starts-with", "$key", "user/eric/"], // 可选：指定对象Key的前缀
        // ["in", "$content-type", ["image/jpg", "image/png"]], // 可选：指定允许的内容类型
        // ["not-in", "$cache-control", ["no-cache"]], // 可选：排除某些缓存控制头
    ],
];

// 将Policy文档编码为JSON字符串
$jsonOptions = JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE; // 防止转义斜杠和Unicode字符
$policy = json_encode($policyMap, $jsonOptions);
if (json_last_error() !== JSON_ERROR_NONE) {
    error_log("json_encode fail, err: " . json_last_error_msg()); // 检查JSON编码是否失败
    exit(1);
}

// 计算签名所需的信息
$stringToSign = base64_encode($policy); // 对Policy进行Base64编码
$signingKey = "aliyun_v4" . $cred->getAccessKeySecret(); // 构造签名密钥
$h1Key = hmacSign($signingKey, $date); // 第一步：对日期签名
$h2Key = hmacSign($h1Key, $region);   // 第二步：对区域签名
$h3Key = hmacSign($h2Key, $product);  // 第三步：对产品签名
$h4Key = hmacSign($h3Key, "aliyun_v4_request"); // 第四步：对请求签名

// 计算最终签名
$signature = hash_hmac('sha256', $stringToSign, $h4Key);

// 构建POST请求的表单数据
$bodyWriter = new CURLFileUpload(); // 创建表单构建器实例

// 添加字段到表单
$bodyWriter->addField('key', $key); // 对象名称
$bodyWriter->addField('policy', $stringToSign); // Base64编码后的Policy
$bodyWriter->addField('x-oss-signature-version', 'OSS4-HMAC-SHA256'); // 签名版本
$bodyWriter->addField('x-oss-credential', sprintf("%s/%s/%s/%s/aliyun_v4_request",
    $cred->getAccessKeyId(), $date, $region, $product)); // 凭证信息
$bodyWriter->addField('x-oss-date', $utcTime->format('Ymd\THis\Z')); // 时间戳
$bodyWriter->addField('x-oss-signature', $signature); // 最终签名

// 添加文件内容到表单
$bodyWriter->addFileFromString('file', $data); // 上传的文件内容
$postData = $bodyWriter->getFormData(); // 获取完整的表单数据

// 发送POST请求
$client = new \GuzzleHttp\Client(); // 创建HTTP客户端
$response = $client->post(
    sprintf("http://%s.oss-%s.aliyuncs.com/", $bucket, $region), // OSS的上传地址
    [
        'headers' => [
            'content-type' => $bodyWriter->getContentType(), // 设置Content-Type
        ],
        'body' => $postData // 设置请求体
    ]
);

// 检查响应状态码
if ($response->getStatusCode() getStatusCode() >= 300) {
    echo "Post Object Fail, status code:" . $response->getStatusCode() . ", reason: " . $response->getReasonPhrase() . PHP_EOL;
    exit(1); // 如果状态码不在2xx范围内，则退出程序
}

// 打印上传结果
echo "post object done, status code:" . $response->getStatusCode() . ", request id:" . $response->getHeaderLine('x-oss-request-id') . PHP_EOL;

/**
 * HMAC签名函数
 * @param string $key 签名密钥
 * @param string $data 待签名数据
 * @return string 返回签名结果
 */
function hmacSign($key, $data)
{
    return hash_hmac('sha256', $data, $key, true); // 使用SHA256算法生成HMAC签名
}

/**
 * 表单构建器类，用于生成multipart/form-data格式的请求体
 */
class CURLFileUpload
{
    private $fields = []; // 存储普通字段
    private $files = [];  // 存储文件字段
    private $boundary;    // 分隔符

    public function __construct()
    {
        $this->boundary = uniqid(); // 生成唯一的分隔符
    }

    /**
     * 添加普通字段
     * @param string $name 字段名称
     * @param string $value 字段值
     */
    public function addField($name, $value)
    {
        $this->fields[$name] = $value;
    }

    /**
     * 添加文件字段
     * @param string $name 字段名称
     * @param string $content 文件内容
     */
    public function addFileFromString($name, $content)
    {
        $this->files[$name] = [
            'content' => $content,
            'filename' => $name,
            'type' => 'application/octet-stream' // 默认MIME类型
        ];
    }

    /**
     * 获取完整的表单数据
     * @return string 返回multipart/form-data格式的请求体
     */
    public function getFormData()
    {
        $data = '';
        foreach ($this->fields as $name => $value) {
            $data .= "--{$this->boundary}\r\n";
            $data .= "Content-Disposition: form-data; name=\"$name\"\r\n\r\n";
            $data .= $value . "\r\n";
        }
        foreach ($this->files as $name => $file) {
            $data .= "--{$this->boundary}\r\n";
            $data .= "Content-Disposition: form-data; name=\"$name\"; filename=\"{$file['filename']}\"\r\n";
            $data .= "Content-Type: {$file['type']}\r\n\r\n";
            $data .= $file['content'] . "\r\n";
        }
        $data .= "--{$this->boundary}--\r\n";
        return $data;
    }

    /**
     * 获取Content-Type头部
     * @return string 返回Content-Type值
     */
    public function getContentType()
    {
        return "multipart/form-data; boundary={$this->boundary}";
    }
}

```

## 相关文档
- 关于表单上传的完整示例，请参见[Github示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PostObject.php)。

[上一篇：分片上传（PHP SDK V2）](/zh/oss/developer-reference/multipart-upload-using-oss-sdk-for-php-v2)[下一篇：使用预签名URL上传（PHP SDK V2）](/zh/oss/developer-reference/upload-object-using-a-presigned-url-for-php-sdk-v2)该文章对您有帮助吗？反馈
  
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