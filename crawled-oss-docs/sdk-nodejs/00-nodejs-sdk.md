# OSS Node.js SDK

Source: https://help.aliyun.com/zh/oss/developer-reference/nodejs-sdk/

---

- OSS Node.js SDK-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# OSS Node.js SDK
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
为Node.js应用提供简单易用的OSS集成方案，支持文件上传下载、权限管理等核心功能，快速实现云端文件存储和管理能力。

## 快速接入

通过以下步骤快速接入OSS Node.js SDK。

### 准备环境

下载并安装[Node.js](https://nodejs.org/en/download)运行环境。建议使用Node.js 8.0及以上版本以获得更好的兼容性和性能表现。
- 执行`node -v`命令查看Node.js版本。
- 执行`npm -v`命令查看npm版本。

### 安装SDK

根据Node.js版本选择对应的SDK版本。
- Node.js 8.0及以上版本：使用最新的SDK 6.x版本。
- Node.js 8.0以下版本：使用SDK 4.x版本。

## 安装6.x版本（推荐）

```
npm install ali-oss@^6.x --save
```

## 安装4.x版本

```
npm install ali-oss@^4.x --save
```

安装完成后，执行`npm list ali-oss`命令验证SDK是否成功安装，成功时会显示对应的SDK版本信息。

### 配置访问凭证

使用 RAM 用户的 AccessKey 配置访问凭证。
- 在 [RAM 控制台](https://ram.console.aliyun.com/users/create)，创建使用永久 AccessKey 访问的 RAM 用户，保存 AccessKey，然后为该用户授予 `AliyunOSSFullAccess` 权限。
- 使用 RAM 用户的 AccessKey 配置环境变量。
#### Linux
在命令行界面执行以下命令，将环境变量设置追加到`~/.bashrc `文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```
- 执行以下命令使变更生效。
```
source ~/.bashrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

#### macOS
- 在终端中执行以下命令，查看默认Shell类型。
```
echo $SHELL
```
- 根据默认Shell类型进行操作。
##### Zsh
执行以下命令，将环境变量设置追加到 `~/.zshrc` 文件中。
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

##### Bash
- 执行以下命令，将环境变量设置追加到 `~/.bash_profile` 文件中。
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

#### Windows

##### CMD
- 在CMD中运行以下命令。
```
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```
- 运行以下命令，检查环境变量是否生效。
```
echo %OSS_ACCESS_KEY_ID%
echo %OSS_ACCESS_KEY_SECRET%
```

##### PowerShell
- 在PowerShell中运行以下命令。
```
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
- 运行以下命令，检查环境变量是否生效。
```
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

### 初始化客户端
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// OSS Node.js SDK初始化客户端示例

const OSS = require('ali-oss');

async function main() {
    
    // 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
    const client = new OSS({
        // 填写Bucket所在地域
        region: 'oss-',
        // 从环境变量中获取访问凭证
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
        // 启用V4签名
        authorizationV4: true,
    });

    try {
        // 列举所有Bucket
        const result = await client.listBuckets();
        
        // 输出Bucket列表信息
        console.log(`共找到 ${result.buckets.length} 个Bucket:`);
        
        for (const bucket of result.buckets) {
            console.log(bucket.name);
        }
        
    } catch (err) {
        console.log('列举Bucket失败，详细信息如下:');
        console.error(err);
        return;
    }
}

// 执行主函数
main().catch(console.error);

```

## 客户端配置

OSS客户端支持多种配置选项以适应不同的网络环境和性能需求。通过自定义Endpoint类型、设置超时时间和连接数等配置参数，可以优化客户端的访问性能和稳定性。完整配置选项详见[客户端配置项](https://github.com/ali-sdk/ali-oss?tab=readme-ov-file#create-a-bucket-instance)。

### 使用内网域名

通过内网域名访问OSS可以避免公网流量费用，同时获得更高的访问速度和安全性。初始化客户端时将Endpoint设置为内网访问域名即可启用内网访问。
运行示例代码前，请将代码中的 ``等占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
const client = new OSS({
    region: 'oss-',
    // 从环境变量中获取访问凭证
    accessKeyId: process.env.OSS_ACCESS_KEY_ID,
    accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
    // 启用V4签名
    authorizationV4: true,
    // 使用内网访问域名
    endpoint: '',
});
```

### 使用自定义域名

将Endpoint指定为自定义域名，并在初始化客户端时通过`cname: true`参数启用CNAME选项，即可实现自定义域名访问。
使用前需确保已将自定义域名绑定到Bucket。详见[通过自定义域名访问OSS](https://help.aliyun.com/zh/oss/user-guide/access-buckets-via-custom-domain-names)。说明 
使用自定义域名时无法调用`client.listBuckets()`方法。
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
const client = new OSS({
    region: 'oss-',
    // 从环境变量中获取访问凭证
    accessKeyId: process.env.OSS_ACCESS_KEY_ID,
    accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
    // 启用V4签名
    authorizationV4: true,
    // 使用自定义域名
    endpoint: 'http://example.com',
    // 填写Bucket名称，Bucket名称必须和自定义域名绑定
    bucket: 'example-bucket',
    // 开启CNAME选项
    cname: true,
});
```

### 使用传输加速域名

初始化OSS客户端时，将Endpoint指定为传输加速域名即可实现加速访问。
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
const client = new OSS({
    region: 'oss-',
    // 从环境变量中获取访问凭证
    accessKeyId: process.env.OSS_ACCESS_KEY_ID,
    accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
    // 启用V4签名
    authorizationV4: true,
    // 使用传输加速域名
    endpoint: 'https://oss-accelerate.aliyuncs.com',
    // 填写Bucket名称，Bucket必须开启传输加速功能
    bucket: 'example-bucket',
});
```

### 签名版本
重要 
阿里云对象存储 V1 签名将按以下时间表停止使用，建议尽快[升级为V4签名](https://help.aliyun.com/zh/oss/developer-reference/guidelines-for-upgrading-v1-signatures-to-v4-signatures)，确保服务不受影响。
- 自 2025 年 3 月 1 日起，新注册用户无法使用 V1 签名。
- 自 2025 年 9 月 1 日起，逐步停止 V1 签名的更新维护，且新创建的 Bucket 无法使用 V1 签名。

以下示例代码采用V1签名初始化客户端。V4签名客户端初始化示例代码参见[初始化客户端](#b47a499916w53)。

```
// OSS Node.js SDK初始化客户端示例

const OSS = require('ali-oss');

async function main() {
    
    // 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
    const client = new OSS({
        // 从环境变量中获取访问凭证
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
    });

    try {
        // 列举所有Bucket
        const result = await client.listBuckets();
        
        // 输出Bucket列表信息
        console.log(`共找到 ${result.buckets.length} 个Bucket:`);
        
        for (const bucket of result.buckets) {
            console.log(bucket.name);
        }
        
    } catch (err) {
        console.log('列举Bucket失败，详细信息如下:');
        console.error(err);
        return;
    }
}

// 执行主函数
main().catch(console.error);

```

## 示例代码

以下提供文件基本操作的示例代码，涵盖上传、下载、删除和列举文件等核心功能。通过这些示例可以快速掌握OSS Node.js SDK的基本用法，更多完整示例请参见[Github示例](https://github.com/ali-sdk/ali-oss/tree/master/test/node)或具体功能SDK参考文档。

### 上传文件

以下示例演示如何将本地文件上传至OSS Bucket，同时展示如何通过自定义请求头设置文件属性，实现存储类型、访问权限、标签等精细化控制。
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// OSS Node.js SDK上传文件示例

const OSS = require('ali-oss');
const path = require('path');

async function main() {
    
    // 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
    const client = new OSS({
        region: 'oss-',
        // 从环境变量中获取访问凭证
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
        // 启用V4签名
        authorizationV4: true,
        // 填写Bucket名称
        bucket: 'example-bucket',
    });

    // 自定义请求头
    const headers = {
        // 指定Object的存储类型
        'x-oss-storage-class': 'Standard',
        // 指定Object的访问权限
        'x-oss-object-acl': 'private',
        // 通过文件URL访问文件时，指定以附件形式下载文件
        'Content-Disposition': 'attachment',
        // 设置Object的标签，可同时设置多个标签
        'x-oss-tagging': 'Tag1=1&Tag2=2',
        // 指定PutObject操作时是否覆盖同名目标Object。此处设置为true，表示禁止覆盖同名Object
        'x-oss-forbid-overwrite': 'true',
    };

    try {
        // 配置文件信息
        const key = 'dest.jpg';                    // OSS中的文件路径
        const localFilePath = path.normalize('dest.jpg'); // 本地文件的完整路径
        
        // 将本地文件上传到OSS指定路径
        const result = await client.put(key, localFilePath, { headers });
        
        console.log(`文件上传完成: ${localFilePath} -> ${key}`);
        console.log('上传结果:', result);
        
    } catch (err) {
        console.log('上传失败，详细信息如下:');
        console.error(err);
        return;
    }
}

// 执行主函数
main().catch(console.error);

```

### 下载文件

以下示例演示如何从OSS Bucket下载文件至本地指定路径。
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// OSS Node.js SDK下载文件示例

const OSS = require('ali-oss');

async function main() {
    
    // 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
    const client = new OSS({
        region: 'oss-',
        // 从环境变量中获取访问凭证
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
        // 启用V4签名
        authorizationV4: true,
        // 填写Bucket名称
        bucket: 'example-bucket',
    });

    try {
        // 配置文件信息
        const key = 'dest.jpg';       // OSS中的文件路径
        const filePath = 'dest.jpg';  // 本地保存路径
        
        // 将OSS中的文件下载到本地指定路径
        const result = await client.get(key, filePath);
        
        console.log(`文件下载完成: ${key} -> ${filePath}`);
        
    } catch (err) {
        console.log('下载失败，详细信息如下:');
        console.error(err);
        return;
    }
}

// 执行主函数
main().catch(console.error);

```

### 删除文件

以下示例演示如何删除OSS Bucket中的指定文件。
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// OSS Node.js SDK删除文件示例

const OSS = require('ali-oss');

async function main() {
    
    // 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
    const client = new OSS({
        region: 'oss-',
        // 从环境变量中获取访问凭证
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
        // 启用V4签名
        authorizationV4: true,
        // 填写Bucket名称
        bucket: 'example-bucket',
    });

    try {
        // 配置文件信息
        const key = 'dest.jpg';  // OSS中要删除的文件路径
        
        // 删除OSS中的指定文件
        const result = await client.delete(key);
        
        console.log(`文件删除完成: ${key}`);
        console.log('删除结果:', result);
        
    } catch (err) {
        console.log('删除失败，详细信息如下:');
        console.error(err);
        return;
    }
}

// 执行主函数
main().catch(console.error);

```

### 列举文件

以下示例演示如何列举OSS Bucket中的文件，默认返回最多100个文件的详细信息。
运行示例代码前，请将代码中的 ``占位符替换为实际的[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints)，如 `cn-hangzhou`。
```
// OSS Node.js SDK列举文件示例

const OSS = require('ali-oss');

async function main() {
    
    // 从环境变量中获取访问凭证（需要设置OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET）
    const client = new OSS({
        region: 'oss-',
        // 从环境变量中获取访问凭证
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
        // 启用V4签名
        authorizationV4: true,
        // 填写Bucket名称
        bucket: 'example-bucket',
    });

    try {
        // 不带任何参数，默认最多返回100个文件
        const result = await client.list();
        
        console.log(`共找到 ${result.objects ? result.objects.length : 0} 个文件:`);
        
        // 输出文件列表信息
        if (result.objects && result.objects.length > 0) {
            for (const object of result.objects) {
                console.log(`文件名: ${object.name}, 大小: ${object.size} bytes, 修改时间: ${object.lastModified}`);
            }
        } else {
            console.log('Bucket中没有找到任何文件');
        }
        
    } catch (err) {
        console.log('列举文件失败，详细信息如下:');
        console.error(err);
        return;
    }
}

// 执行主函数
main().catch(console.error);

```

## 异常处理

使用OSS Node.js SDK访问OSS时出现错误，OSS会返回包含HTTP状态码、错误消息、请求ID等详细信息的错误响应。例如下载不存在的对象文件时，会返回以下错误信息（省略了部分信息）：

```
Error [NoSuchKeyError]: Object not exists {
  status: 404,
  code: 'NoSuchKey',
  requestId: '6904202CA7BABC37395E28AB'
}
```

通过错误码查找相应错误原因和解决方案，完整的错误码信息请参见[HTTP错误码](https://help.aliyun.com/zh/oss/user-guide/http-status-code/)。遇到问题时也可根据requestId寻求在线技术支持的帮助。

## 访问凭证配置

OSS 支持多种凭证初始化方式，需根据认证和授权需求选择合适的初始化方式。

单击查看如何选择访问凭证
| 凭证提供者初始化方式 | 适用场景 | 是否需要提供前置的AK或STS Token | 底层实现基于的凭证 | 凭证有效期 | 凭证轮转或刷新方式|
| [使用RAM用户的AK](#d8b62cd412p1e) | 部署运行在安全、稳定且不易受外部攻击的环境的应用程序，无需频繁轮转凭证就可以长期访问云服务 | 是 | AK | 长期 | 手动轮转|
| [使用STS临时访问凭证](#4e428b9fbdg88) | 部署运行在不可信的环境的应用程序，希望能控制访问的有效期、权限 | 是 | STS Token | 临时 | 手动刷新|
| [使用RAMRoleARN](#7084511a46rap) | 需要授权访问云服务，例如跨阿里云账号访问云服务的应用程序 | 是 | STS Token | 临时 | 自动刷新|
| [使用ECSRAMRole](#59ade624cafr3) | 部署运行在阿里云的ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中的应用程序 | 否 | STS Token | 临时 | 自动刷新|
| [使用OIDCRoleARN](#bd43c2d0c1u93) | 部署运行在阿里云的容器服务Kubernetes版的Worker节点中的不可信应用程序 | 否 | STS Token | 临时 | 自动刷新|
| [使用CredentialsURI](#a618115e4ff1w) | 需要通过外部系统获取访问凭证的应用程序 | 否 | STS Token | 临时 | 自动刷新|

### 使用RAM用户的AK

适用于应用程序部署运行在安全、稳定且不易受外部攻击的环境中，需要长期访问OSS且无法频繁轮转凭证的场景。通过阿里云主账号或RAM用户的AK（Access Key ID、Access Key Secret）初始化凭证提供者。该方式需要手动维护AK，存在安全性风险和维护复杂度增加的风险。
重要 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/create-an-accesskey-pair-1#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，如若遗忘请创建新的AK进行替换。
- 使用RAM用户AccessKey配置环境变量。
#### Linux
在命令行界面执行以下命令，将环境变量设置追加到`~/.bashrc `文件中。
```
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc
echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```
- 执行以下命令使变更生效。
```
source ~/.bashrc
```
- 执行以下命令检查环境变量是否生效。
```
echo $OSS_ACCESS_KEY_ID
echo $OSS_ACCESS_KEY_SECRET
```

#### macOS
- 在终端中执行以下命令，查看默认Shell类型。
```
echo $SHELL
```
- 根据默认Shell类型进行操作。
##### Zsh
执行以下命令，将环境变量设置追加到 `~/.zshrc` 文件中。
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

##### Bash
- 执行以下命令，将环境变量设置追加到 `~/.bash_profile` 文件中。
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

#### Windows

##### CMD
- 在CMD中运行以下命令。
```
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID"
setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```
- 运行以下命令，检查环境变量是否生效。
```
echo %OSS_ACCESS_KEY_ID%
echo %OSS_ACCESS_KEY_SECRET%
```

##### PowerShell
- 在PowerShell中运行以下命令。
```
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
- 运行以下命令，检查环境变量是否生效。
```
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User)
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```
- 参考上述方式修改系统环境变量后，需重启或刷新编译运行环境，包括IDE、命令行界面、其他桌面应用程序及后台服务，以确保最新的系统环境变量成功加载。
- 使用环境变量传递凭证信息。
```
const OSS = require("ali-oss");

// 初始化OSS
const client = new OSS({
  // 从环境变量中获取AccessKey ID的值
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  // 从环境变量中获取AccessKey Secret的值
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET
});

// listBuckets
const buckets = await client.listBuckets();
console.log(buckets);
```

### 使用STS临时访问凭证

适用于应用程序需要临时访问OSS的场景。通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token）初始化凭证提供者。该方式需要手动维护STS Token，存在安全性风险和维护复杂度增加的风险。如果需要多次临时访问OSS，需要手动刷新STS Token。
重要 - 通过OpenAPI方式简单快速获取STS临时访问凭证，请参见[AssumeRole - 获取扮演角色的临时身份凭证](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-assumerole)。
- 通过SDK方式获取STS临时访问凭证，请参见[使用STS临时访问凭证访问OSS](https://help.aliyun.com/zh/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss#section-rjh-18m-7kp)。
- 请注意，STS Token在生成的时候需要指定过期时间，过期后自动失效不能再使用。
- 获取关于STS服务的接入点列表，请参见[服务接入点](https://help.aliyun.com/zh/ram/developer-reference/api-sts-2015-04-01-endpoint)。
- 使用临时身份凭证设置环境变量。
## Mac OS/Linux/Unix
重要 请注意，此处使用的是通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token），而非RAM用户的Access Key和Access Key Secret。
- 请注意区分STS服务获取的Access Key ID以STS开头，例如“STS.****************”。

```
export OSS_ACCESS_KEY_ID=
export OSS_ACCESS_KEY_SECRET=
export OSS_SESSION_TOKEN=
```

## Windows
重要 - 请注意，此处使用的是通过STS服务获取的临时身份凭证（Access Key ID、Access Key Secret和Security Token），而非RAM用户的AK（Access Key ID、Access Key Secret）。
- 请注意区分STS服务获取的Access Key ID以STS开头，例如“STS.****************”。

```
set OSS_ACCESS_KEY_ID=
set OSS_ACCESS_KEY_SECRET=
set OSS_SESSION_TOKEN=
```
- 通过环境变量传递凭证信息。
```
const OSS = require("ali-oss");

// 初始化OSS
const client = new OSS({
  // 从环境变量中获取AccessKey ID的值
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  // 从环境变量中获取AccessKey Secret的值
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // 从环境变量中获取STS Token的值
  stsToken: process.env.OSS_SESSION_TOKEN
});

// listBuckets
const buckets = await client.listBuckets();
console.log(buckets);
```

### 使用RAMRoleARN

适用于应用程序需要授权访问OSS，例如跨阿里云账号访问OSS的场景。通过指定RAM角色的ARN（Alibabacloud Resource Name）初始化凭证提供者，底层实现基于STS Token。Credentials工具会前往STS服务获取STS Token，并在会话到期前调用AssumeRole接口申请新的STS Token。还可以通过为`policy`赋值来限制RAM角色到一个更小的权限集合。
重要 - 阿里云账号拥有资源的全部权限，AK一旦泄露，会给系统带来巨大风险，不建议使用。推荐使用最小化授权的RAM用户的AK。
- 如需创建RAM用户的AK，请直接访问[创建AccessKey](https://help.aliyun.com/zh/ram/user-guide/create-an-accesskey-pair#section-rjh-18m-7kp)。RAM用户的Access Key ID、Access Key Secret信息仅在创建时显示，请及时保存，如若遗忘请创建新的AK进行轮换。
- 如需获取RAMRoleARN，请直接访问[创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。
- 添加credentials依赖。
```
npm install @alicloud/credentials
```
- 配置AK和RAMRoleARN作为访问凭证。
```
const Credential = require("@alicloud/credentials");
const OSS = require("ali-oss");

// 使用RamRoleArn初始化Credentials Client。
const credentialsConfig = new Credential.Config({
  // 凭证类型。
  type: "ram_role_arn",
  // 从环境变量中获取AccessKey ID的值
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  // 从环境变量中获取AccessKey Secret的值
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  // 要扮演的RAM角色ARN，示例值：acs:ram::123456789012****:role/adminrole，可以通过环境变量ALIBABA_CLOUD_ROLE_ARN设置roleArn
  roleArn: '',
  // 角色会话名称，可以通过环境变量ALIBABA_CLOUD_ROLE_SESSION_NAME设置RoleSessionName
  roleSessionName: '',
  // 设置更小的权限策略，非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
  // policy: '',
  roleSessionExpiration: 3600
});
const credentialClient = new Credential.default(credentialsConfig);
const credential = await credentialClient.getCredential();

// 初始化OSS
const client = new OSS({
  accessKeyId:credential.accessKeyId,
  accessKeySecret: credential.accessKeySecret,
  stsToken: credential.securityToken,
  refreshSTSTokenInterval: 0, // 由Credential控制accessKeyId、accessKeySecret和stsToken值的更新
  refreshSTSToken: async () => {
    const { accessKeyId, accessKeySecret, securityToken } = await credentialClient.getCredential();
    return {
      accessKeyId,
      accessKeySecret,
      stsToken: securityToken,
    };
  }
});

// listBuckets
const buckets = await client.listBuckets();
console.log( buckets);
```

### 使用ECSRAMRole

适用于应用程序运行在ECS实例、ECI实例、容器服务Kubernetes版的Worker节点中的场景。建议使用ECSRAMRole初始化凭证提供者，底层实现基于STS Token。ECSRAMRole允许将一个角色关联到ECS实例、ECI实例或容器服务 Kubernetes 版的Worker节点，实现在实例内部自动刷新STS Token。该方式无需提供AK或STS Token，消除了手动维护AK或STS Token的风险。如何获取ECSRAMRole，请参见[创建角色](https://help.aliyun.com/zh/ram/developer-reference/api-ram-2015-05-01-createrole)。如何将一个角色关联到ECS实例，请参见[实例RAM角色](https://help.aliyun.com/zh/ecs/user-guide/attach-an-instance-ram-role-to-an-ecs-instance)。
- 添加credentials依赖。
```
npm install @alicloud/credentials
```
- 配置ECSRAMRole作为访问凭证。
```
const Credential = require("@alicloud/credentials");
const OSS = require("ali-oss");

// 使用RamRoleArn初始化Credentials Client。
const credentialsConfig = new Credential.Config({
  // 凭证类型。
  type: "ecs_ram_role",
  // 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置roleName
  roleName: ''
});
const credentialClient = new Credential.default(credentialsConfig);

const { accessKeyId, accessKeySecret, securityToken } = await credentialClient.getCredential();

// 初始化OSS Client
const client = new OSS({
  accessKeyId,
  accessKeySecret,
  stsToken: securityToken,
  refreshSTSTokenInterval: 0, // 由Credential控制accessKeyId、accessKeySecret和stsToken值的更新
  refreshSTSToken: async () => {
    const { accessKeyId, accessKeySecret, securityToken } = await credentialClient.getCredential();
    
    return {
      accessKeyId,
      accessKeySecret,
      stsToken: securityToken,
    };
  }
});

// listBuckets
const buckets = await client.listBuckets();
console.log(buckets);
```

### 使用OIDCRoleARN

在容器服务Kubernetes版中设置了Worker节点RAM角色后，对应节点内的Pod中的应用也可以像ECS上部署的应用一样，通过元数据服务（Meta Data Server）获取关联角色的STS Token。但如果容器集群上部署的是不可信的应用（比如部署客户提交的应用，代码也没有开放），可能并不希望它们能通过元数据服务获取Worker节点关联实例RAM角色的STS Token。为了避免影响云上资源的安全，同时又能让这些不可信的应用安全地获取所需的STS Token，实现应用级别的权限最小化，可以使用RRSA（RAM Roles for Service Account）功能。该方式底层实现基于STS Token。阿里云容器集群会为不同的应用Pod创建和挂载相应的服务账户OIDC Token文件，并将相关配置信息注入到环境变量中，Credentials工具通过获取环境变量的配置信息，调用STS服务的AssumeRoleWithOIDC接口换取绑定角色的STS Token。该方式无需提供AK或STS Token，消除了手动维护AK或STS Token的风险。详情请参见[通过RRSA配置ServiceAccount的RAM权限实现Pod权限隔离](https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services#task-2142941)。
- 添加credentials依赖。
```
npm install @alicloud/credentials
```
- 配置OIDC的RAM角色作为访问凭证。
```
const OSS = require("ali-oss");
const Credential = require("@alicloud/credentials");

const credentialsConfig = new Credential.Config({
  // 凭证类型。
  type: "oidc_role_arn",
  // RAM角色名称ARN，可以通过环境变量ALIBABA_CLOUD_ROLE_ARN设置roleArn
  roleArn: '',
  // OIDC提供商ARN，可以通过环境变量ALIBABA_CLOUD_OIDC_PROVIDER_ARN设置oidcProviderArn
  oidcProviderArn: '',
  // OIDC Token文件路径，可以通过环境变量ALIBABA_CLOUD_OIDC_TOKEN_FILE设置oidcTokenFilePath
  oidcTokenFilePath: '',
  // 角色会话名称，可以通过环境变量ALIBABA_CLOUD_ROLE_SESSION_NAME设置roleSessionName
  roleSessionName: '',
  // 设置更小的权限策略，非必填。示例值：{"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"}
  // policy: "",
  // 设置session过期时间
  roleSessionExpiration: 3600
});
const credentialClient = new Credential.default(credentialsConfig);
const { accessKeyId, accessKeySecret, securityToken } = await credentialClient.getCredential();
const client = new OSS({
  accessKeyId,
  accessKeySecret,
  stsToken: securityToken,
  refreshSTSTokenInterval: 0, // 由Credential控制accessKeyId、accessKeySecret和stsToken值的更新
  refreshSTSToken: async () => {
    const { accessKeyId, accessKeySecret, securityToken } = await credentialClient.getCredential();
    
    return {
      accessKeyId,
      accessKeySecret,
      stsToken: securityToken,
    };
  }
});
const buckets = await client.listBuckets();

console.log(buckets);
```

### 使用CredentialsURI

适用于应用程序需要通过外部系统获取阿里云凭证，从而实现灵活的凭证管理和无密钥访问的场景。可以使用CredentialsURI初始化凭证提供者，底层实现基于STS Token。Credentials工具通过提供的URI获取STS Token，完成凭证客户端初始化。该方式无需提供AK或STS Token，消除了手动维护AK或STS Token的风险。
重要 - CredentialsURI指获取STS Token的服务器地址。
- 提供CredentialsURI响应的后端服务需要实现STS Token的自动刷新逻辑，确保应用程序始终能获取到有效凭证。
- 为了使Credentials工具正确解析和使用STS Token，URI必须遵循以下响应协议：响应状态码：200
- 响应体结构：
```
{
    "Code": "Success",
    "AccessKeySecret": "AccessKeySecret",
    "AccessKeyId": "AccessKeyId",
    "Expiration": "2021-09-26T03:46:38Z",
    "SecurityToken": "SecurityToken"
}
```
- 添加credentials依赖。
```
npm install @alicloud/credentials
```
- 配置CredentialsURI作为访问凭证。
```
const OSS = require("ali-oss");
const Credential = require("@alicloud/credentials");

// 通过凭证的 URI 初始化Credentials Client。
const credentialsConfig = new Credential.Config({
  // 凭证类型。
  type: "credentials_uri",
  // 获取凭证的 URI，格式为http://local_or_remote_uri/，可以通过环境变量ALIBABA_CLOUD_CREDENTIALS_URI设置credentialsUri
  credentialsURI: ''
});
const credentialClient = new Credential.default(credentialsConfig);
const credential = await credentialClient.getCredential();

// 初始化OSS
const client = new OSS({
  accessKeyId: credential.accessKeyId,
  accessKeySecret: credential.accessKeySecret,
  stsToken: credential.securityToken,
  refreshSTSTokenInterval: 0, // 由Credential控制accessKeyId、accessKeySecret和stsToken值的更新
  refreshSTSToken: async () => {
    const { accessKeyId, accessKeySecret, securityToken } = await credentialClient.getCredential();

    return {
      accessKeyId,
      accessKeySecret,
      stsToken: securityToken,
    };
  }
});

// listBuckets
const buckets = await client.listBuckets();
console.log(buckets);
```

## 相关文档
- [常见问题（Node.js SDK）](https://help.aliyun.com/zh/oss/developer-reference/faq-21)

[上一篇：异常处理（C# SDK V1）](/zh/oss/developer-reference/exception-handling-2)[下一篇：快速入门（Node.js SDK）](/zh/oss/developer-reference/getting-started-with-oss-sdk-for-node-js)该文章对您有帮助吗？反馈
  
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