# OSS PHP SDK V2

Source: https://help.aliyun.com/zh/oss/developer-reference/manual-for-php-v2/

---

- OSS PHP SDK V2-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# OSS PHP SDK V2
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
[GitHub](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2)｜[OSS PHP SDK V2开发者指南](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/DEVGUIDE-CN.md)｜[SDK Releases](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/releases)

## 快速接入

接入OSS PHP SDK V2的流程如下：

### 环境准备

要求 PHP 7.4 及以上版本，同时请参考[composer](https://getcomposer.org/download/)官网下载包管理工具composer。
可以通过 `php -version` 命令查看 php 版本。如果当前环境没有 php 或版本低于 php 7.4，请[下载安装PHP](https://www.php.net/downloads.php)。
### 安装SDK
- 创建项目目录，使用包管理工具composer执行以下命令获取OSS PHP SDK V2。请根据需求选择合适的OSS PHP SDK V2版本，推荐使用最新的版本，确保本文中的代码示例可以正常运行。关于版本功能的更多信息，请参见[Releases](https://help.aliyun.com/redirect?targetUrl=https%3A%2F%2Fgithub.com%2Faliyun%2Falibabacloud-oss-php-sdk-v2%2Freleases)。
```
mkdir oss-php-example && cd oss-php-example && composer require alibabacloud/oss-v2
```
- 使用以下代码引入OSS PHP SDK V2包。
```
require_once __DIR__ . '/../vendor/autoload.php';

use AlibabaCloud\Oss\V2 as Oss;
```

### 配置访问凭证

使用 RAM 用户的 AccessKey 配置访问凭证。
- 在 [RAM 控制台](https://ram.console.aliyun.com/users/create)，创建使用永久 AccessKey 访问的 RAM 用户，保存 AccessKey，然后为该用户授予 `AliyunOSSFullAccess` 权限。
- 使用 RAM 用户 AccessKey 配置环境变量。
## Linux
在命令行界面执行以下命令来将环境变量设置追加到`~/.bashrc `文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```
执行以下命令使变更生效。
```
source ~/.bashrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

## macOS
- 在终端中执行以下命令，查看默认Shell类型。
```
echo $SHELL
```
根据默认Shell类型进行操作。
#### Zsh
执行以下命令来将环境变量设置追加到 `~/.zshrc` 文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
```
- 执行以下命令使变更生效。
```
source ~/.zshrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

#### Bash
- 执行以下命令来将环境变量设置追加到 `~/.bash_profile` 文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile
```
- 执行以下命令使变更生效。
```
source ~/.bash_profile
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

## Windows

## CMD
- 在CMD中运行以下命令。
```
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```
运行以下命令，检查环境变量是否生效。
```
echo %OSS_ACCESS_KEY_ID%
echo %OSS_ACCESS_KEY_SECRET%
```

## PowerShell
- 在PowerShell中运行以下命令。
```
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
运行以下命令，检查环境变量是否生效。
```
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

### 初始化客户端

使用[地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)初始化 OSSClient，并运行测试代码。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider);

// 方式一：只填写Region（推荐）- SDK自动构造HTTPS域名
// 华东1（杭州）：cn-hangzhou
$cfg->setRegion(region: "cn-hangzhou");

// // 方式二：同时填写Region和Endpoint
// $cfg->setRegion(region: 'cn-hangzhou')->setEndpoint(endpoint: 'https://oss-cn-hangzhou.aliyuncs.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 要上传的数据内容
$data = 'Hello OSS';

// 创建PutObjectRequest对象，用于上传对象
$request = new Oss\Models\PutObjectRequest(
                bucket: "Your Bucket Name",
                key: "Your Object Key",
            );
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

运行后将会输出上传文件成功的结果：

```
status code: 200
request id: 687F2BEEDC44E0313527BA07
etag: "F0F18C2C66AE1DD512BDCD4366F76DA3"
```

## 客户端配置

客户端支持哪些配置？
| 参数名 | 说明 | 示例|
| region | (必选)请求发送的区域, 必选 | setRegion("cn-hangzhou")|
| credentialsProvider | (必选)设置访问凭证 | setCredentialsProvider(provider)|
| endpoint | 访问域名 | setEndpoint("oss-cn-hanghzou.aliyuncs.com")|
| retryMaxAttempts | HTTP请求时的最大尝试次数, 默认值为 3 | setRetryMaxAttempts(5)|
| retryer | HTTP请求时的重试实现 | setRetryer(customRetryer)|
| connectTimeout | 建立连接的超时时间, 默认值为 10 秒 | setConnectTimeout(5* time.Second)|
| readWriteTimeout | 应用读写数据的超时时间, 默认值为 20 秒 | setReadWriteTimeout(30 * time.Second)|
| insecureSkipVerify | 是否跳过SSL证书校验，默认检查SSL证书 | setInsecureSkipVerify(true)|
| enabledRedirect | 是否开启HTTP重定向, 默认不开启 | setEnabledRedirect(true)|
| proxyHost | 设置代理服务器 | setProxyHost(‘http://user:passswd@proxy.example-***.com’)|
| signatureVersion | 签名版本，默认值为v4 | setSignatureVersion("v1")|
| disableSSL | 不使用https请求，默认使用https | setDisableSSL(true)|
| usePathStyle | 使用路径请求风格，即二级域名请求风格，默认为bucket托管域名 | setUsePathStyle(true)|
| useCName | 是否使用自定义域名访问，默认不使用 | setUseCName(true)|
| useDualStackEndpoint | 是否使用双栈域名访问，默认不使用 | setUseDualStackEndpoint(true)|
| useAccelerateEndpoint | 是否使用传输加速域名访问，默认不使用 | setUseAccelerateEndpoint(true)|
| useInternalEndpoint | 是否使用内网域名访问，默认不使用 | setUseInternalEndpoint(true)|
| additionalHeaders | 指定额外的签名请求头，V4签名下有效 | setAdditionalHeaders([‘content-length’])|
| userAgent | 指定额外的User-Agent信息 | setUserAgent(‘user identifier’)|

### 使用自定义域名

使用OSS默认域名访问时，可能会出现文件禁止访问、文件无法预览等问题；通过[通过自定义域名访问OSS](https://help.aliyun.com/zh/oss/user-guide/access-buckets-via-custom-domain-names#concept-zt4-cvy-5db)，不仅支持浏览器直接预览文件，还可结合CDN加速分发。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
// 填写您的自定义域名。例如www.example-***.com，请注意，setUseCname设置true开启CNAME选项，否则无法使用自定义域名
// 调用putcname接口需要8以上的php版本
$cfg->setRegion('cn-hangzhou')->setEndpoint('www.example-***.com')->setUseCname(true);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 超时控制

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
$cfg->setRegion(region: "cn-hangzhou");

# 设置建立连接的超时时间
$cfg->setConnectTimeout(connectTimeout: 30);

# 设置应用读写数据的超时时间
$cfg->setReadwriteTimeout(readwriteTimeout:30);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 最大错误重试次数

请求异常时，OSSClient 默认重试 3 次。

高并发或网络不稳定时，使用 `setRetryMaxAttempts` 增加重试次数。这能提升请求成功率。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider);

// 华东1（杭州）：cn-hangzhou
$cfg->setRegion(region: "cn-hangzhou");

// 设置HTTP请求时的最大尝试次数, 默认值为 3
$cfg->setRetryMaxAttempts(5);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### HTTP/HTTPS 协议

使用 `setDisableSSL(true)` 设置不使用HTTPS协议。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider);

// 华东1（杭州）：cn-hangzhou
$cfg->setRegion(region: "cn-hangzhou");

// 禁用SSL
$cfg->setDisableSSL(true);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### Swoole框架下使用协程

以下代码演示了基于swoole框架下创建支持协程的 OSS 客户端示例。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者
$cfg->setRegion(region: $region); // 设置区域
$cfg->setEndpoint(endpoint: 'http://oss-cn-hangzhou.aliyuncs.com'); // 设置访问域名

// 创建支持协程的 OSS 客户端
$client = new Oss\Client(config: $cfg, options: ['handler' => HandlerStack::create(handler: new CoroutineHandler())]);

// 协程任务 1：上传 swoole.txt
co(function () use ($client, $bucket) {
    try {
        $key = 'swoole.txt'; // 对象名称
        $data = 'Hello OSS'; // 对象内容
        $request = new Oss\Models\PutObjectRequest($bucket, $key); // 创建上传请求
        $request->body = Oss\Utils::streamFor($data); // 设置请求体
        $result = $client->putObject(request: $request); // 执行上传
        echo "Task 1 Result:\n" . var_export($result, true) . "\n"; // 输出结果
    } catch (\Exception $e) {
        echo "Task 1 Error: " . $e->getMessage() . "\n"; // 捕获异常
    }
});

// 协程任务 2：上传 hyperf.txt
co(function () use ($client, $bucket) {
    try {
        $key = 'hyperf.txt'; // 对象名称
        $data = 'Hello OSS'; // 对象内容
        $request = new Oss\Models\PutObjectRequest($bucket, $key); // 创建上传请求
        $request->body = Oss\Utils::streamFor($data); // 设置请求体
        $result = $client->putObject($request); // 执行上传
        echo "Task 2 Result:\n" . var_export($result, true) . "\n"; // 输出结果
    } catch (\Exception $e) {
        echo "Task 2 Error: " . $e->getMessage() . "\n"; // 捕获异常
    }
});

```

### 使用内网域名

当您的应用部署在阿里云的ECS实例上，并且需要频繁访问同地域的OSS资源时，使用内网域名可以降低流量成本并提高访问速度。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// 方式一： 填写Region并设置setUseInternalEndpoint为true
// 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
$cfg->setRegion('cn-hangzhou')->setUseInternalEndpoint(true);

// // 方式二： 直接填写Region和Endpoint
// // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
// // 填写Bucket所在地域对应的内网Endpoint。以华东1（杭州）为例，Endpoint填写为'https://oss-cn-hangzhou-internal.aliyuncs.com',
// // 如需指定为http协议，请在指定域名时填写为'http://oss-cn-hangzhou-internal.aliyuncs.com'
// $cfg->setRegion('cn-hangzhou')->setEndpoint('https://oss-cn-hanghzou-internal.aliyuncs.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用传输加速域名

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// 方式一： 填写Region并设置setUseAccelerateEndpoint为true
// 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
$cfg->setRegion('cn-hangzhou')->setUseAccelerateEndpoint(true);

// // 方式二： 直接填写Region和Endpoint
// // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
// // 填写Bucket所在地域对应的传输加速Endpoint。以华东1（杭州）为例，Endpoint填写为'https://oss-accelerate.aliyuncs.com',
// $cfg->setRegion('cn-hangzhou')->setEndpoint('https://oss-accelerate.aliyuncs.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用专有域

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou
// 填写您的专有域。例如：https://service.corp.example.com
$cfg->setRegion('cn-hangzhou')->setEndpoint('https://service.corp.example.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...

```

### 使用金融云域名

以下是使用[金融云](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#dbe294402aq6j)域名配置OSSClient的示例代码。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// 填写Bucket所在地域。以华东1 金融云为例，Region填写为cn-hangzhou-finance
// 填写Bucket所在地域对应的内网Endpoint。以华东1 金融云为例，Endpoint填写为'https://oss-cn-hzjbp-a-internal.aliyuncs.com',
// 如需指定为http协议，请在指定域名时填写为'http://oss-cn-hzjbp-a-internal.aliyuncs.com'
$cfg->setRegion('cn-hangzhou-finance')->setEndpoint('https://oss-cn-hzjbp-a-internal.aliyuncs.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用政务云域名

以下是使用[政务云](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#3e2a1817f0pps)域名配置OSSClient的示例代码。

```
setCredentialsProvider(credentialsProvider: $credentialsProvider); // 设置凭证提供者

// Region填写Bucket所在地域。以华北2 阿里政务云1为例，Region填写为cn-north-2-gov-1
// 填写Bucket所在地域对应的内网Endpoint。以华北2 阿里政务云1为例，Endpoint填写为'https://oss-cn-north-2-gov-1-internal.aliyuncs.com',
// 如需指定为http协议，请在指定域名时填写为'http://oss-cn-north-2-gov-1-internal.aliyuncs.com'
$cfg->setRegion('cn-north-2-gov-1')->setEndpoint('https://oss-cn-north-2-gov-1-internal.aliyuncs.com');

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

## 访问凭证配置

OSS 提供多种凭证初始化方式。请根据您的认证和授权需求选择合适的初始化方式。

如何选择访问凭证？
| 凭证提供者初始化方式 | 适用场景 | 是否需要提供前置的AK或STS Token | 底层实现基于的凭证 | 凭证有效期 | 凭证轮转或刷新方式|
| 使用RAM用户的AK | 部署运行在安全、稳定且不易受外部攻击的环境的应用程序，无需频繁轮转凭证就可以长期访问云服务 | 是 | AK | 长期 | 手动轮转|
| 使用STS临时访问凭证 | 部署运行在不可信的环境的应用程序，希望能控制访问的有效期、权限 | 是 | STS Token | 临时 | 手动刷新|
| 使用RAMRoleARN | 需要授权访问云服务，例如跨阿里云账号访问云服务的应用程序 | 是 | STS Token | 临时 | 自动刷新|
| 使用ECSRAMRole | 部署运行在阿里云的ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中的应用程序 | 否 | STS Token | 临时 | 自动刷新|
| 使用OIDCRoleARN | 部署运行在阿里云的容器服务Kubernetes版的Worker节点中的不可信应用程序 | 否 | STS Token | 临时 | 自动刷新|
| 自定义凭证提供者 | 如果以上凭证配置方式都不满足要求时，您可以自定义获取凭证的方式 | 自定义 | 自定义 | 自定义 | 自定义|

### 使用RAM用户的AK

如果您的应用程序部署运行在安全、稳定且不易受外部攻击的环境中，需要长期访问您的OSS，且不能频繁轮转凭证时，您可以使用阿里云主账号或RAM用户的AK（Access Key ID、Access Key Secret）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个AK，存在安全性风险和维护复杂度增加的风险。
警告 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请考虑创建新的AK进行轮换。

## 环境变量
- 使用RAM用户AccessKey配置环境变量。
### Linux
在命令行界面执行以下命令来将环境变量设置追加到`~/.bashrc `文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```
执行以下命令使变更生效。
```
source ~/.bashrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

### macOS
- 在终端中执行以下命令，查看默认Shell类型。
```
echo $SHELL
```
根据默认Shell类型进行操作。
#### Zsh
执行以下命令来将环境变量设置追加到 `~/.zshrc` 文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
```
- 执行以下命令使变更生效。
```
source ~/.zshrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

#### Bash
- 执行以下命令来将环境变量设置追加到 `~/.bash_profile` 文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile
```
- 执行以下命令使变更生效。
```
source ~/.bash_profile
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

### Windows

#### CMD
- 在CMD中运行以下命令。
```
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```
运行以下命令，检查环境变量是否生效。
```
echo %OSS_ACCESS_KEY_ID%
echo %OSS_ACCESS_KEY_SECRET%
```

#### PowerShell
- 在PowerShell中运行以下命令。
```
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
运行以下命令，检查环境变量是否生效。
```
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
- 参考上述方式修改系统环境变量后，请重启或刷新您的编译运行环境，包括IDE、命令行界面、其他桌面应用程序及后台服务，以确保最新的系统环境变量成功加载。
- 使用环境变量来传递凭证信息。
```
setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

## 静态凭证

以下示例代码展示了如何对访问凭据直接进行硬编码，显式设置要使用的访问密钥。
警告 
请勿将访问凭据嵌入到生产环境的应用程序中，此方法仅用于测试目的。

```
setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用STS临时访问凭证

如果您的应用程序需要临时访问OSS，您可以使用通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token）初始化凭证提供者。需要注意的是，该方式需要您手动维护一个STS Token，存在安全性风险和维护复杂度增加的风险。此外，如果您需要多次临时访问OSS，您需要手动刷新STS Token。
重要 - 如果您希望通过OpenAPI的方式简单快速获取到STS临时访问凭证，请参见[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)。
- 如果您希望通过SDK的方式获取STS临时访问凭证，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#section-rjh-18m-7kp)。
- 请注意，STS Token在生成的时候需要指定过期时间，过期后自动失效不能再使用。
- 如果您希望获取关于STS服务的接入点列表，请参见[服务接入点](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-endpoint)。

## 环境变量
- 使用临时身份凭证设置环境变量。
## Mac OS X/Linux/Unix
警告 请注意，此处使用的是通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token），而非RAM用户的Access Key和Access Key Secret。
- 请注意区分STS服务获取的Access Key ID以STS开头，例如“STS.****************”。

```
export OSS_ACCESS_KEY_ID=
export OSS_ACCESS_KEY_SECRET=
export OSS_SESSION_TOKEN=
```

## Windows
警告 - 请注意，此处使用的是通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token），而非RAM用户的AK（Access Key ID、Access Key Secret）。
- 请注意区分STS服务获取的Access Key ID以STS开头，例如“STS.****************”。

```
set OSS_ACCESS_KEY_ID=
set OSS_ACCESS_KEY_SECRET=
set OSS_SESSION_TOKEN=
```
- 通过环境变量来传递凭证信息。
```
setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

## 静态凭证

您可以在应用程序中对凭据直接进行硬编码，显式设置要使用的临时访问密钥。
警告 
请勿将访问凭据嵌入到生产环境的应用程序中，此方法仅用于测试目的。

```
setCredentialsProvider($credentialsProvider); // 设置凭证提供者
$cfg->setRegion($region); // 设置Bucket所在的地域

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用RAMRoleARN

如果您的应用程序需要授权访问OSS，例如跨阿里云账号访问OSS，您可以使用RAMRoleARN初始化凭证提供者。该方式底层实现是STS Token。通过指定RAM角色的ARN（Alibabacloud Resource Name），Credentials工具会前往STS服务获取STS Token，并在会话到期前调用AssumeRole接口申请新的STS Token。此外，您还可以通过为`policy`赋值来限制RAM角色到一个更小的权限集合。
重要 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请考虑创建新的AK进行轮换。
- 如需获取RAMRoleARN，请直接访问[CreateRole - 创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 添加阿里云凭证库[credentials-php](https://github.com/aliyun/credentials-php)。
```
composer require alibabacloud/credentials
```
- 配置AK和RAMRoleARN作为访问凭证。
```
 'ram_role_arn',

    // AccessKeyId 是阿里云账号的访问密钥 ID
    'accessKeyId' => 'AccessKeyId',

    // AccessKeySecret 是阿里云账号的访问密钥
    'accessKeySecret' => 'AccessKeySecret',

    // RoleArn 是 RAM 角色的 ARN 格式，例如：acs:ram::USER_Id:role/ROLE_NAME
    'roleArn' => 'RoleArn',

    // RoleSessionName 是角色会话名称，用于标识当前会话
    'roleSessionName' => 'yourRoleSessionName',

    // 可选参数，用于限制 STS Token 的权限范围
    'policy' => 'Policy',
]);

// 使用配置对象初始化凭证实例
$credential = new Credential($config);

// 加载SDK默认配置
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者，通过回调函数动态生成凭证
$cfg->setCredentialsProvider(new Oss\Credentials\CredentialsProviderFunc(function () use ($credential) {
    // 获取临时凭证（STS Token）
    $cred = $credential->getCredential();

    // 返回包含 AccessKeyId、AccessKeySecret 和 SecurityToken 的凭证对象
    return new Oss\Credentials\Credentials(
        accessKeyId: $cred->getAccessKeyId(),       // 临时访问密钥 ID
        accessKeySecret: $cred->getAccessKeySecret(),   // 临时访问密钥
        securityToken: $cred->getSecurityToken()      // 安全令牌（STS Token）
    );
}));

// 设置 OSS 客户端的地域信息，以华东1（杭州）为例，Region 填写为 cn-hangzhou
$region = 'cn-hangzhou';
$cfg->setRegion($region);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用ECSRAMRole

如果您的应用程序运行在ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中，建议您使用ECSRAMRole初始化凭证提供者。该方式底层实现是STS Token。ECSRAMRole允许您将一个角色关联到ECS实例、ECI实例或容器服务 Kubernetes 版的Worker节点，实现在实例内部自动刷新STS Token。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。如何获取ECSRAMRole，请参见[CreateRole - 创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 添加阿里云凭证库[credentials-php](https://github.com/aliyun/credentials-php)。
```
composer require alibabacloud/credentials
```
- 配置ECSRAMRole作为访问凭证。
```
 'ecs_ram_role',

    // 填写 ECS 实例绑定的 RAM 角色名称
    'roleName' => "",  // 替换为实际的 RAM 角色名称
]);

// 使用配置对象初始化凭证实例
$credential = new Credential($config);

// 加载默认配置并获取 OSS 配置对象
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者，通过回调函数动态生成凭证
$cfg->setCredentialsProvider(new Oss\Credentials\CredentialsProviderFunc(function () use ($credential) {
    // 获取临时凭证（STS Token）
    $cred = $credential->getCredential();

    // 返回包含 AccessKeyId、AccessKeySecret 和 SecurityToken 的凭证对象
    return new Oss\Credentials\Credentials(
        accessKeyId: $cred->getAccessKeyId(),       // 临时访问密钥 ID
        accessKeySecret: $cred->getAccessKeySecret(), // 临时访问密钥
        securityToken: $cred->getSecurityToken()   // 安全令牌（STS Token）
    );
}));

// 设置 OSS 客户端的地域信息，以华东1（杭州）为例，Region 填写为 cn-hangzhou
$region = 'cn-hangzhou';
$cfg->setRegion($region);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...

```

### 使用OIDCRoleARN

在容器服务Kubernetes版中设置了Worker节点RAM角色后，对应节点内的Pod中的应用也就可以像ECS上部署的应用一样，通过元数据服务（Meta Data Server）获取关联角色的STS Token。但如果容器集群上部署的是不可信的应用（比如部署您的客户提交的应用，代码也没有对您开放），您可能并不希望它们能通过元数据服务获取Worker节点关联实例RAM角色的STS Token。为了避免影响云上资源的安全，同时又能让这些不可信的应用安全地获取所需的STS Token，实现应用级别的权限最小化，您可以使用RRSA（RAM Roles for Service Account）功能。该方式底层实现是STS Token。阿里云容器集群会为不同的应用Pod创建和挂载相应的服务账户OIDC Token文件，并将相关配置信息注入到环境变量中，Credentials工具通过获取环境变量的配置信息，调用STS服务的AssumeRoleWithOIDC接口换取绑定角色的STS Token。该方式无需您提供一个AK或STS Token，消除了手动维护AK或STS Token的风险。详情请参见[通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services#task-2142941)。
- 添加阿里云凭证库[credentials-php](https://github.com/aliyun/credentials-php)。
```
composer require alibabacloud/credentials
```
- 配置OIDCRoleArn作为访问凭证。
```
 'oidc_role_arn',

    // 指定 OIDC 身份提供商的 ARN（可以通过环境变量 ALIBABA_CLOUD_OIDC_PROVIDER_ARN 设置）
    'oidcProviderArn' => '',  // 替换为实际的 OIDC 提供商 ARN

    // 指定 OIDC Token 文件路径（可以通过环境变量 ALIBABA_CLOUD_OIDC_TOKEN_FILE 设置）
    'oidcTokenFilePath' => '',  // 替换为实际的 OIDC Token 文件路径

    // 指定 RAM 角色的 ARN（可以通过环境变量 ALIBABA_CLOUD_ROLE_ARN 设置）
    'roleArn' => '',  // 替换为实际的 RAM 角色 ARN

    // 指定角色会话名称（可以通过环境变量 ALIBABA_CLOUD_ROLE_SESSION_NAME 设置）
    'roleSessionName' => '',  // 替换为实际的角色会话名称

    // 可选参数：指定 RAM 角色的权限策略，限制其权限范围
    // 示例策略：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
    'policy' => '',  // 如果需要限制权限，请替换为实际的策略 JSON 字符串

    // 可选参数：指定会话的有效期（单位为秒，默认值为 3600 秒）
    'roleSessionExpiration' => 3600,  // 如果需要调整有效期，请修改此值
]);

// 使用配置对象初始化凭证实例
$credential = new Credential($config);

// 加载默认配置并获取 OSS 配置对象
$cfg = Oss\Config::loadDefault();

// 设置凭证提供者，通过回调函数动态生成凭证
$cfg->setCredentialsProvider(new Oss\Credentials\CredentialsProviderFunc(function () use ($credential) {
    // 获取临时凭证（STS Token）
    $cred = $credential->getCredential();

    // 返回包含 AccessKeyId、AccessKeySecret 和 SecurityToken 的凭证对象
    return new Oss\Credentials\Credentials(
        accessKeyId: $cred->getAccessKeyId(),       // 临时访问密钥 ID
        accessKeySecret: $cred->getAccessKeySecret(), // 临时访问密钥
        securityToken: $cred->getSecurityToken()   // 安全令牌（STS Token）
    );
}));

// 设置 OSS 客户端的地域信息，以华东1（杭州）为例，Region 填写为 cn-hangzhou
$region = 'cn-hangzhou';
$cfg->setRegion($region);

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的client执行后续操作...
```

### 使用自定义访问凭证

当以上凭证配置方式不满足要求时，您可以自定义获取凭证的方式。SDK 支持多种实现方式。
- 通过 Oss\Credentials\CredentialsProviderFuncOss\Credentials\CredentialsProviderFunc 是 Oss\Credentials\CredentialsProvider 的易用性封装。
```
setCredentialsProvider($provider);

// 设置 OSS 客户端的地域信息，以华东1（杭州）为例，Region 填写为 cn-hangzhou
$region = 'cn-hangzhou';
$cfg->setRegion($region);

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的 client 执行后续操作...

```
- 实现 Oss\Credentials\CredentialsProvider
```
setCredentialsProvider($provider);

// 设置 OSS 客户端的地域信息，以华东1（杭州）为例，Region 填写为 cn-hangzhou
$region = 'cn-hangzhou';
$cfg->setRegion($region);

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// 使用创建好的 client 执行后续操作...

```

## 错误自助排查

使用PHP SDK V2访问OSS出现错误时，OSS会返回HTTP Code、Message、RequestId、EC错误码等信息，其中EC码对应一个具体的错误原因，可以使用EC码自助进行错误排查。
- 例如，当您使用以下代码下载一个并不存在的文件时。
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

// 创建GetObjectRequest对象，用于获取指定对象的内容
$request = new Oss\Models\GetObjectRequest(bucket: $bucket, key: $key);

// 执行获取对象操作
$result = $client->getObject($request);

// 定义要保存的本地文件路径
$localFilePath = './test/file.txt'; // 请替换为实际的文件路径

// 将内容写入本地文件
file_put_contents( $localFilePath, $result->body->getContents());

// 打印获取结果
// 输出HTTP状态码、请求ID以及对象的内容
printf(
    'status code:' . $result->statusCode . PHP_EOL . // HTTP状态码，例如200表示成功
    'request id:' . $result->requestId . PHP_EOL  // 请求ID，用于调试或追踪请求
);

```
- 返回示例如下，返回结果中包含'EC': '0026-00000001'，作为该错误原因的唯一标识。
- 通过以上错误请求示例返回的EC错误码查找问题原因及对应解决方法的操作步骤如下。打开[OpenAPI问题自助诊断平台](https://api.aliyun.com/troubleshoot?q=&requestId=&product=)。
- 在搜索框中，输入EC错误码，例如0026-00000001。
- 在搜索结果中查找问题原因及对应解决方案。

## 示例代码

OSS PHP SDK V2提供丰富的示例代码供参考或直接使用。
| 示例内容 | GitHub示例文件|
| [创建存储空间（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-create-bucket) | [PutBucket.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucket.php)|
| [列举存储空间（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-list-buckets) | [ListBuckets.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/ListBuckets.php)|
| [判断存储空间是否存在（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-determine-whether-a-bucket-exists) | [IsBucketExist.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/IsBucketExist.php)|
| [获取存储空间的地域（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-query-the-region-of-a-bucket) | [GetBucketLocation.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketLocation.php)|
| [获取存储空间的信息（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-query-bucket-information) | [GetBucketInfo.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketInfo.php)|
| [获取存储空间的存储容量（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-query-the-storage-capacity-of-a-bucket) | [GetBucketStat.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketStat.php)|
| [删除存储空间（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-delete-a-bucket) | [DeleteBucket.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucket.php)|
| [存储空间标签（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-bucket-tagging) | - [PutBucketTags.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketTags.php)
- [GetBucketTags.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketTags.php)
- [DeleteBucketTags.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketTags.php)|
| [请求者付费模式（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-pay-by-requester) | - [PutBucketRequestPayment.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketRequestPayment.php)
- [GetBucketRequestPayment.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketRequestPayment.php)|
| [简单上传（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/simple-upload-using-oss-sdk-for-php-v2) | [PutObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutObject.php)|
| [追加上传（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/append-upload-using-oss-sdk-for-php-v2) | [AppendObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/AppendObject.php)|
| [分片上传（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-using-oss-sdk-for-php-v2) | [CompleteMultipartUpload.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/CompleteMultipartUpload.php)|
| [表单上传（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/form-upload-using-oss-sdk-for-php-v2) | [PostObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PostObject.php)|
| [使用预签名URL上传（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/upload-object-using-a-presigned-url-for-php-sdk-v2) | [Presign.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Presign.php)|
| [文件上传管理器（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/file-uploader-with-oss-sdk-for-php-v2) | [Uploader.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Uploader.php)|
| [简单下载（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/simple-download-using-oss-sdk-for-php-v2) | [GetObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetObject.php)|
| [范围下载（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/scope-download-using-oss-sdk-for-php-v2) | [GetObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetObject.php)|
| [使用预签名URL下载（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/download-using-a-presigned-url-for-php-sdk-v2) | [Presign.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Presign.php)|
| [文件下载管理器（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/file-downloader-with-oss-sdk-for-php-v2) | [Downloader.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Downloader.php)|
| [拷贝对象（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/copy-object-using-oss-sdk-for-php-v2) | [CopyObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/CopyObject.php)|
| [分片拷贝（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/fragment-copy-using-oss-sdk-for-php-v2) | [UploadPartCopy.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/UploadPartCopy.php)|
| [文件拷贝管理器（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/file-copy-manager-using-oss-sdk-for-php-v2) | [Copier.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Copier.php)|
| [判断文件是否存在（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/determine-whether-the-file-exists-using-oss-sdk-for-php-v2) | [IsObjectExist.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/IsObjectExist.php)|
| [列举文件（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/list-objects-using-oss-sdk-for-php-v2) | [ListObjectsV2.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/ListObjectsV2.php)|
| [删除文件（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/delete-objects-using-oss-sdk-for-php-v2) | [DeleteObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteObject.php)|
| [解冻文件](https://help.aliyun.com/zh/oss/developer-reference/restore-object-using-oss-sdk-for-php-v2) | [RestoreObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/RestoreObject.php)|
| [管理文件元数据（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-object-metadata-using-oss-sdk-for-php-v2) | [HeadObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/HeadObject.php)|
| [转换文件存储类型（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/convert-object-storage-type-using-oss-sdk-for-php-v2) | [CopyObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/CopyObject.php)|
| [重命名文件（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/rename-object-using-oss-sdk-for-python-v2) | [CopyObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/CopyObject.php)|
| [管理软链接（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-soft-links-using-oss-sdk-for-php-v2) | - [PutSymlink.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutSymlink.php)
- [GetSymlink.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetSymlink.php)|
| [设置对象标签（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/set-object-tags-using-oss-sdk-for-php-v2)

[获取对象标签（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/get-object-tags-using-oss-sdk-for-php-v2)

[删除对象标签（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/delete-object-tags-using-oss-sdk-for-php-v2) | - [PutObjectTagging.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutObjectTagging.php)
- [GetObjectTagging.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetObjectTagging.php)
- [DeleteObjectTagging.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteObjectTagging.php)|
| [管理存储空间读写权限（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-manage-the-acl-of-a-bucket) | - [PutBucketAcl.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketAcl.php)
- [GetBucketAcl.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketAcl.php)|
| [管理文件访问权限（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/manage-file-access) | - [PutObjectAcl.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutObjectAcl.php)
- [GetObjectAcl.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetObjectAcl.php)|
| [Bucket Policy（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-configure-and-manage-bucket-policies) | - [PutBucketPolicy.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketPolicy.php)
- [GetBucketPolicy.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketPolicy.php)
- [DeleteBucketPolicy.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketPolicy.php)|
| [管理版本控制（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/managing-version-control-using-oss-sdk-for-php-v2) | - [PutBucketVersioning.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketVersioning.php)
- [GetBucketVersioning.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketVersioning.php)|
| [防盗链（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-hotlink-protection) | - [PutBucketReferer.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketReferer.php)
- [GetBucketReferer.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketReferer.php)|
| [跨域资源共享（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/cross-domain-resource-sharing-for-php-sdk-v2) | - [PutBucketCors.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketCors.php)
- [GetBucketCors.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketCors.php)
- [DeleteBucketCors.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketCors.php)|
| [合规保留策略（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-compliance-reserved-resources) | - [GetBucketWorm.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketWorm.php)
- [InitiateBucketWorm.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/InitiateBucketWorm.php)
- [AbortBucketWorm.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/AbortBucketWorm.php)
- [ExtentBucketWorm.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/ExtentBucketWorm.php)|
| [服务端加密（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-server-side-encryption) | - [put_bucket_encryption.py](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketEncryption.php)
- [get_bucket_encryption.py](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketEncryption.php)
- [delete_bucket_encryption.py](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketEncryption.php)|
| [客户端加密（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-client-side-encryption) | [EncryptionClient.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/EncryptionClient.php)|
| [数据复制（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/data-replication-using-oss-sdk-for-php-v2) | - [GetBucketReplication.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketReplication.php)
- [PutBucketReplication.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketReplication.php)
- [DeleteBucketReplication.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketReplication.php)|
| [访问跟踪（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-access-tracking) | - [PutBucketAccessMonitor.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketAccessMonitor.php)
- [GetBucketAccessMonitor.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketAccessMonitor.php)|
| [生命周期管理（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-lifecycle-management) | - [PutBucketLifecycle.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketLifecycle.php)
- [GetBucketLifecycle.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketLifecycle.php)
- [DeleteBucketLifecycle.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketLifecycle.php)|
| [静态网站托管（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-static-website-hosting) | - [PutBucketWebsite.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketWebsite.php)
- [GetBucketWebsite.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketWebsite.php)
- [DeleteBucketWebsite.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketWebsite.php)|
| [日志转存（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-logging-2) | - [PutBucketLogging.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketLogging.php)
- [GetBucketLogging.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketLogging.php)
- [DeleteBucketLogging.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteBucketLogging.php)|
| [归档直读（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/real-time-access-to-archive-objects-using-oss-sdk-for-php-v2) | [PutBucketArchiveDirectRead.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketArchiveDirectRead.php)|
| [标量检索（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/data-indexing-using-oss-sdk-for-php-v2)

[向量检索（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/vector-retrieval-using-oss-sdk-for-php-v2) | - [OpenMetaQuery.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/OpenMetaQuery.php)
- [CloseMetaQuery.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/CloseMetaQuery.php)
- [DoMetaQuery.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DoMetaQuery.php)
- [GetMetaQueryStatus.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetMetaQueryStatus.php)|
| [绑定自定义域名（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-map-custom-domain-names) | - [CreateCnameToken.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/CreateCnameToken.php)
- [PutCname.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutCname.php)
- [DeleteCname.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/DeleteCname.php)
- [GetCnameToken.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetCnameToken.php)|
| [传输加速（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/php-v2-transfer-acceleration) | - [PutBucketTransferAcceleration.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketTransferAcceleration.php)
- [GetBucketTransferAcceleration.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/GetBucketTransferAcceleration.php)|
| [同步处理（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/synchronous-processing-using-oss-sdk-for-php-v2) | [ProcessObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/ProcessObject.php)|
| [异步处理（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/asynchronous-processing-using-oss-sdk-for-php-v2) | [AsyncProcessObject.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/AsyncProcessObject.php)|
| [OSS全局阻止公共访问（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/oss-global-block-public-access-using-oss-sdk-for-php-v2) | [PutPublicAccessBlock.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutPublicAccessBlock.php)|
| [Bucket级别阻止公共访问（PHP SDK V2）](https://help.aliyun.com/zh/oss/developer-reference/blocking-public-access-at-the-bucket-level-using-oss-sdk-for-php-v2) | [PutBucketPublicAccessBlock.php](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/PutBucketPublicAccessBlock.php)|

[上一篇：视频转码（Go SDK V1）](/zh/oss/developer-reference/go-video-transcoding)[下一篇：存储空间（PHP SDK V2）](/zh/oss/developer-reference/manage-buckets-using-oss-sdk-for-php-v2/)该文章对您有帮助吗？反馈
  
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