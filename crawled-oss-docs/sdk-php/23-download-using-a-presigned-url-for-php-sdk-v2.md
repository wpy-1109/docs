# 使用PHP SDK生成用于下载文件的预签名URL

Source: https://help.aliyun.com/zh/oss/developer-reference/download-using-a-presigned-url-for-php-sdk-v2

---

- 使用PHP SDK生成用于下载文件的预签名URL-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 使用预签名URL下载（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
默认情况下，OSS Bucket中的文件是私有的，仅文件拥有者可访问。本文介绍如何使用OSS PHP SDK生成带有过期时间的GET方法预签名URL，以允许他人临时下载文件。在有效期内可多次访问，超期后需重新生成。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以从环境变量读取访问凭证为例。更多配置访问凭证的示例，请参见[PHP配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。
- 预签名URL无需权限即可生成，但仅当您拥有`oss:GetObject`权限时，第三方才能通过该预签名URL成功下载文件。具体授权操作，请参见[为RAM用户授权自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-flo-x8e-e94)。
- 本文示例代码使用V4预签名URL，有效期最大为7天。更多信息，请参见[签名版本4（推荐）](https://help.aliyun.com/zh/oss/developer-reference/add-signatures-to-urls)。

## 使用过程

使用预签名URL下载文件的过程如下：

## 参数说明
| 参数 | 是否必填 | 说明 | 示例|
| `--region` | 是 | Bucket所在的地域 | `cn-hangzhou`|
| `--bucket` | 是 | Bucket名称 | `examplebucket`|
| `--key` | 是 | 文件名称（含路径） | `my-object.txt`|
| `--expire` | 否 | 过期时间（秒），默认900秒 | `600`|
| `--endpoint` | 否 | 访问域名，默认会根据region自动使用对应的外网Endpoint。 | `oss-cn-hangzhou.aliyuncs.com`|

## 示例代码
- 文件拥有者生成GET方法的预签名URL。
```
 ['help' => 'The region in which the bucket is located.', 'required' => True], // Bucket所在的地域（必填）
    "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 访问域名（可选）
    "bucket" => ['help' => 'The name of the bucket', 'required' => True], // Bucket名称（必填）
    "key" => ['help' => 'The name of the object', 'required' => True], // 对象名称（必填）
    "expire" => ['help' => 'The expiration time in seconds (default: 900)', 'required' => False], // 过期时间（可选，默认900秒）
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
$expire = isset($options["expire"]) ? (int)$options["expire"] : 900; // 过期时间，默认900秒

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

try {
    // 创建OSS客户端实例
    $client = new Oss\Client($cfg);

    // 创建GetObjectRequest对象，用于下载对象
    $request = new Oss\Models\GetObjectRequest(bucket:$bucket, key:$key);

    // 调用presign方法生成预签名URL，设置过期时间
    $result = $client->presign($request, [
        'expires' => new \DateInterval("PT{$expire}S") // PT表示Period Time，S表示秒
    ]);

    // 输出预签名URL
    echo "预签名URL: " . $result->url . PHP_EOL;
} catch (Exception $e) {
    echo "错误: " . $e->getMessage() . PHP_EOL;
    exit(1);
}
```
- 其他人使用GET方法的预签名URL下载文件。
### curl

```
curl -SO "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************"
```

### Java

```
import java.io.BufferedInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class Demo {
    public static void main(String[] args) {
        // 替换为生成的GET方法的预签名URL。
        String fileURL = "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************";
        // 填写文件保存的目标路径，包括文件名和扩展名。
        String savePath = "C:/downloads/myfile.txt";

        try {
            downloadFile(fileURL, savePath);
            System.out.println("Download completed!");
        } catch (IOException e) {
            System.err.println("Error during download: " + e.getMessage());
        }
    }

    private static void downloadFile(String fileURL, String savePath) throws IOException {
        URL url = new URL(fileURL);
        HttpURLConnection httpConn = (HttpURLConnection) url.openConnection();
        httpConn.setRequestMethod("GET");

        // 检查响应代码
        int responseCode = httpConn.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
            // 输入流
            InputStream inputStream = new BufferedInputStream(httpConn.getInputStream());
            // 输出流
            FileOutputStream outputStream = new FileOutputStream(savePath);

            byte[] buffer = new byte[4096]; // 缓冲区
            int bytesRead;
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
            }

            outputStream.close();
            inputStream.close();
        } else {
            System.out.println("No file to download. Server replied HTTP code: " + responseCode);
        }
        httpConn.disconnect();
    }
}
```

### Node.js

```
const https = require('https');
const fs = require('fs');

const fileURL = "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************";
const savePath = "C:/downloads/myfile.txt";

https.get(fileURL, (response) => {
    if (response.statusCode === 200) {
        const fileStream = fs.createWriteStream(savePath);
        response.pipe(fileStream);
        
        fileStream.on('finish', () => {
            fileStream.close();
            console.log("Download completed!");
        });
    } else {
        console.error(`Download failed. Server responded with code: ${response.statusCode}`);
    }
}).on('error', (err) => {
    console.error("Error during download:", err.message);
});
```

### Python

```
import requests

file_url = "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************"
save_path = "C:/downloads/myfile.txt"

try:
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(4096):
                f.write(chunk)
        print("Download completed!")
    else:
        print(f"No file to download. Server replied HTTP code: {response.status_code}")
except Exception as e:
    print("Error during download:", e)
```

### Go

```
package main

import (
    "io"
    "net/http"
    "os"
)

func main() {
    fileURL := "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************"
    savePath := "C:/downloads/myfile.txt"

    response, err := http.Get(fileURL)
    if err != nil {
        panic(err)
    }
    defer response.Body.Close()

    if response.StatusCode == http.StatusOK {
        outFile, err := os.Create(savePath)
        if err != nil {
            panic(err)
        }
        defer outFile.Close()

        _, err = io.Copy(outFile, response.Body)
        if err != nil {
            panic(err)
        }
        println("Download completed!")
    } else {
        println("No file to download. Server replied HTTP code:", response.StatusCode)
    }
}
```

### JavaScript

```
const fileURL = "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************";
const savePath = "C:/downloads/myfile.txt"; // 文件将在下载时使用的文件名

fetch(fileURL)
    .then(response => {
        if (!response.ok) {
            throw new Error(`Server replied HTTP code: ${response.status}`);
        }
        return response.blob(); // 将响应转换为 blob
    })
    .then(blob => {
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = savePath; // 设置下载文件的名字
        document.body.appendChild(link); // 此步骤确保链接存在于文档中
        link.click(); // 模拟点击下载链接
        link.remove(); // 完成后移除链接
        console.log("Download completed!");
    })
    .catch(error => {
        console.error("Error during download:", error);
    });
```

### Android-Java

```
import android.os.AsyncTask;
import android.os.Environment;
import java.io.BufferedInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class DownloadTask extends AsyncTask {
    @Override
    protected String doInBackground(String... params) {
        String fileURL = params[0];
        String savePath = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS) + "/myfile.txt"; // 修改后的保存路径
        try {
            URL url = new URL(fileURL);
            HttpURLConnection httpConn = (HttpURLConnection) url.openConnection();
            httpConn.setRequestMethod("GET");
            int responseCode = httpConn.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                InputStream inputStream = new BufferedInputStream(httpConn.getInputStream());
                FileOutputStream outputStream = new FileOutputStream(savePath);
                byte[] buffer = new byte[4096];
                int bytesRead;
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    outputStream.write(buffer, 0, bytesRead);
                }
                outputStream.close();
                inputStream.close();
                return "Download completed!";
            } else {
                return "No file to download. Server replied HTTP code: " + responseCode;
            }
        } catch (Exception e) {
            return "Error during download: " + e.getMessage();
        }
    }
}
```

### Objective-C

```
#import 

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // 定义文件 URL 和保存路径（修改为有效的路径）
        NSString *fileURL = @"https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T092756Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************/20241112/cn-hangzhou/oss/aliyun_v4_request&x-oss-signature=ed5a******************************************************";
        NSString *savePath = @"/Users/your_username/Desktop/myfile.txt"; // 请替换为您的用户名
        
        // 创建 URL 对象
        NSURL *url = [NSURL URLWithString:fileURL];
        
        // 创建下载任务
        NSURLSessionDataTask *task = [[NSURLSession sharedSession] dataTaskWithURL:url completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
            // 错误处理
            if (error) {
                NSLog(@"Error during download: %@", error.localizedDescription);
                return;
            }
            
            // 检查数据
            if (!data) {
                NSLog(@"No data received.");
                return;
            }
            
            // 保存文件
            NSError *writeError = nil;
            BOOL success = [data writeToURL:[NSURL fileURLWithPath:savePath] options:NSDataWritingAtomic error:&writeError];
            if (success) {
                NSLog(@"Download completed!");
            } else {
                NSLog(@"Error saving file: %@", writeError.localizedDescription);
            }
        }];
        
        // 启动任务
        [task resume];
        
        // 让主线程继续运行以便异步请求能够完成
        [[NSRunLoop currentRunLoop] run];
    }
    return 0;
}
```

## 常见使用场景

### 生成指定版本的文件的GET方法的预签名URL

以下代码示例在生成GET方法的预签名URL时，指定了文件的版本，以允许他人下载指定版本的文件。

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

$versionId = "yourVersionId"; // 版本号，此处仅为示例值，实际使用时请替换为真实的版本ID

// 创建GetObjectRequest对象，用于下载对象
$request = new Oss\Models\GetObjectRequest(bucket:$bucket, key:$key, versionId: $versionId);

// 调用presign方法生成预签名URL
$result = $client->presign($request);

// 打印预签名结果
// 输出预签名URL，用户可以直接使用该URL进行下载操作
print(
    'get object presign result:' . var_export($result, true) . PHP_EOL . // 预签名结果的详细信息
    'get object url:' . $result->url . PHP_EOL                           // 预签名URL，用于直接下载对象
);

```

### 使用预签名URL下载指定请求头的文件

在生成GET方式的预签名URL时，如果您指定了请求头，确保在通过该预签名URL发起GET请求时也包含相应的请求头，以免出现不一致，导致请求失败和签名错误。
- 生成带请求头的GET方法签名URL。
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

// 指定rangeBehavior请求头，此处设置为'standard'
$rangeBehavior = 'standard';

// 创建GetObjectRequest对象，用于下载对象
$request = new Oss\Models\GetObjectRequest(bucket:$bucket, key:$key, rangeBehavior: $rangeBehavior);

// 调用presign方法生成预签名URL
$result = $client->presign($request);

// 打印预签名结果
// 输出预签名URL，用户可以直接使用该URL进行下载操作
print(
    'get object presign result:' . var_export($result, true) . PHP_EOL . // 预签名结果的详细信息
    'get object url:' . $result->url . PHP_EOL                           // 预签名URL，用于直接下载对象
);

```
- 使用预签名URL并指定请求头下载文件。curl
```
curl -X GET "https://examplebucket.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241113T093321Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI5tKHJzUF3wMmACXgf1aH****************&x-oss-signature=f1746f121783eed5dab2d665da95fbca08505263e27476a46f88dbe3702af8a9***************************************" \
-H "x-oss-range-behavior: standard" \
-o "myfile.txt"
```

### 使用自定义域名生成用于下载的预签名URL

以下代码示例使用自定义域名生成用于下载的预签名URL。
警告 
您需要先将自定义域名绑定至Bucket默认域名，否则将引发报错！关于绑定自定义域名的详细操作，请参见[通过自定义域名访问OSS](https://help.aliyun.com/zh/oss/user-guide/access-buckets-via-custom-domain-names#concept-zt4-cvy-5db)。

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
$cfg->setEndpoint(endpoint: "http://static.example.com"); // 请设置为您的自定义endpoint
$cfg->setUseCname(true); // 设置为使用CNAME

// 创建OSS客户端实例
$client = new Oss\Client($cfg);

// 创建GetObjectRequest对象，用于下载对象
$request = new Oss\Models\GetObjectRequest(bucket:$bucket, key:$key);

// 调用presign方法生成预签名URL
$result = $client->presign($request);

// 打印预签名结果
// 输出预签名URL，用户可以直接使用该URL进行下载操作
print(
    'get object presign result:' . var_export($result, true) . PHP_EOL . // 预签名结果的详细信息
    'get object url:' . $result->url . PHP_EOL                           // 预签名URL，用于直接下载对象
);

```

## 相关文档
- 关于预签名URL的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Presign.php)。
- 关于预签名URL的API接口，请参见[Presign](https://pkg.go.dev/github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss#Client.Presign)。

[上一篇：范围下载（PHP SDK V2）](/zh/oss/developer-reference/scope-download-using-oss-sdk-for-php-v2)[下一篇：文件下载管理器（PHP SDK V2）](/zh/oss/developer-reference/file-downloader-with-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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