# 使用PHP SDK V2生成PUT预签名URL上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-object-using-a-presigned-url-for-php-sdk-v2

---

- 使用PHP SDK V2生成PUT预签名URL上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 使用预签名URL上传（PHP SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
默认情况下，OSS Bucket中的文件是私有的，仅文件拥有者可访问。本文介绍如何使用OSS PHP SDK生成带有过期时间的PUT方法预签名URL，以允许他人临时上传文件。在有效期内可多次访问，超期后需重新生成。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 预签名URL无需权限即可生成，但仅当您拥有`oss:PutObject`权限时，第三方才能通过该预签名URL成功上传文件。具体授权操作，请参见[为RAM用户授权自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-flo-x8e-e94)。
- 本文示例代码使用V4预签名URL，有效期最大为7天。更多信息，请参见[签名版本4（推荐）](https://help.aliyun.com/zh/oss/developer-reference/add-signatures-to-urls)。
- 本文以从环境变量读取访问凭证为例。更多配置访问凭证的示例，请参见[PHP配置访问凭证](https://help.aliyun.com/zh/oss/developer-reference/configure-access-credentials-for-php-v2)。

## 使用过程

使用PUT方式的预签名URL上传文件的过程如下：

## 示例代码
- 文件拥有者生成PUT方法的预签名URL。重要 在生成PUT方法的预签名URL时，如果指定了请求头，确保在通过该预签名URL发起PUT请求时也包含相应的请求头，以免出现不一致，导致请求失败和签名错误。
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

// 创建PutObjectRequest对象，用于上传对象
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key);

// 调用presign方法生成预签名URL
$result = $client->presign($request);

// 打印预签名结果
// 输出预签名URL，用户可以直接使用该URL进行上传操作
print(
    'put object presign result:' . var_export($result, true) . PHP_EOL . // 预签名结果的详细信息
    'put object url:' . $result->url . PHP_EOL                           // 预签名URL，用于直接上传对象
);

```
- 其他人使用PUT方法的预签名URL上传文件。
### curl

```
curl -X PUT -T /path/to/local/file "https://exampleobject.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T083238Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************%2F20241112%2Fcn-hangzhou%2Foss%2Faliyun_v4_request&x-oss-signature=ed5a******************************************************"
```

### Java

```
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.FileEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import java.io.*;
import java.net.URL;
import java.util.*;

public class SignUrlUpload {
    public static void main(String[] args) throws Throwable {
        CloseableHttpClient httpClient = null;
        CloseableHttpResponse response = null;

        // 将替换为授权URL。
        URL signedUrl = new URL("");

        // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        String pathName = "C:\\Users\\demo.txt";

        try {
            HttpPut put = new HttpPut(signedUrl.toString());
            System.out.println(put);
            HttpEntity entity = new FileEntity(new File(pathName));
            put.setEntity(entity);
            httpClient = HttpClients.createDefault();
            response = httpClient.execute(put);

            System.out.println("返回上传状态码："+response.getStatusLine().getStatusCode());
            if(response.getStatusLine().getStatusCode() == 200){
                System.out.println("使用网络库上传成功");
            }
            System.out.println(response.toString());
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            response.close();
            httpClient.close();
        }
    }
}       
```

### Go

```
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func uploadFile(signedUrl, filePath string) error {
	// 打开文件
	file, err := os.Open(filePath)
	if err != nil {
		return fmt.Errorf("无法打开文件: %w", err)
	}
	defer file.Close()

	// 创建一个新的HTTP客户端
	client := &http.Client{}

	// 创建一个PUT请求
	req, err := http.NewRequest("PUT", signedUrl, file)
	if err != nil {
		return fmt.Errorf("创建请求失败: %w", err)
	}

	// 发送请求
	resp, err := client.Do(req)
	if err != nil {
		return fmt.Errorf("发送请求失败: %w", err)
	}
	defer resp.Body.Close()

	// 读取响应
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Errorf("读取响应失败: %w", err)
	}

	fmt.Printf("返回上传状态码: %d\n", resp.StatusCode)
	if resp.StatusCode == 200 {
		fmt.Println("使用网络库上传成功")
	}
	fmt.Println(string(body))

	return nil
}

func main() {
	// 将替换为授权URL。
	signedUrl := ""

	// 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
	filePath := "C:\\Users\\demo.txt"

	err := uploadFile(signedUrl, filePath)
	if err != nil {
		fmt.Println("发生错误:", err)
	}
}

```

### python

```
import requests

def upload_file(signed_url, file_path):
    try:
        # 打开文件
        with open(file_path, 'rb') as file:
            # 发送PUT请求上传文件
            response = requests.put(signed_url, data=file)
     
        print(f"返回上传状态码：{response.status_code}")
        if response.status_code == 200:
            print("使用网络库上传成功")
        print(response.text)
 
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    # 将替换为授权URL。
    signed_url = ""
    
    # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    file_path = "C:\\Users\\demo.txt"

    upload_file(signed_url, file_path)

```

### Node.js

```
const fs = require('fs');
const axios = require('axios');

async function uploadFile(signedUrl, filePath) {
    try {
        // 创建读取流
        const fileStream = fs.createReadStream(filePath);
        
        // 发送PUT请求上传文件
        const response = await axios.put(signedUrl, fileStream, {
            headers: {
                'Content-Type': 'application/octet-stream' // 根据实际情况调整Content-Type
            }
        });

        console.log(`返回上传状态码：${response.status}`);
        if (response.status === 200) {
            console.log('使用网络库上传成功');
        }
        console.log(response.data);
    } catch (error) {
        console.error(`发生错误：${error.message}`);
    }
}

// 主函数
(async () => {
    // 将替换为授权URL。
    const signedUrl = '';
    
    // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    const filePath = 'C:\\Users\\demo.txt';

    await uploadFile(signedUrl, filePath);
})();
```

### browser.js
重要 如果您使用 Browser.js 上传文件时遇到 403 签名不匹配错误，通常是因为浏览器会自动添加 Content-Type 请求头，而生成预签名 URL 时未指定该请求头，导致签名验证失败。为解决此问题，您需要在生成预签名 URL 时指定 Content-Type 请求头。
```

    
    
    File Upload Example

    
# File Upload Example

    
    
    Upload File

    
        // 请将此替换为步骤一生成的预签名 URL。
        const signedUrl = ""; 

        document.getElementById('uploadButton').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];

            if (!file) {
                alert('Please select a file to upload.');
                return;
            }

            try {
                await upload(file, signedUrl);
                alert('File uploaded successfully!');
            } catch (error) {
                console.error('Error during upload:', error);
                alert('Upload failed: ' + error.message);
            }
        });

        /**
         * 上传文件到 OSS
         * @param {File} file - 需要上传的文件
         * @param {string} presignedUrl - 预签名 URL
         */
        const upload = async (file, presignedUrl) => {
            const response = await fetch(presignedUrl, {
                method: 'PUT',
                body: file,  // 直接上传整个文件
            });

            if (!response.ok) {
                throw new Error(`Upload failed, status: ${response.status}`);
            }

            console.log('File uploaded successfully');
        };
    

```

### C#

```
using System.Net.Http.Headers;

// 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件
var filePath = "C:\\Users\\demo.txt";
// 将替换为授权URL
var presignedUrl = "";

// 创建HTTP客户端并打开本地文件流
using var httpClient = new HttpClient(); 
using var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);
using var content = new StreamContent(fileStream);
            
// 创建PUT请求
var request = new HttpRequestMessage(HttpMethod.Put, presignedUrl);
request.Content = content;

// 发送请求
var response = await httpClient.SendAsync(request);

// 处理响应
if (response.IsSuccessStatusCode)
{
    Console.WriteLine($"上传成功！状态码: {response.StatusCode}");
    Console.WriteLine("响应头部:");
    foreach (var header in response.Headers)
    {
        Console.WriteLine($"{header.Key}: {string.Join(", ", header.Value)}");
    }
}
else
{
    string responseContent = await response.Content.ReadAsStringAsync();
    Console.WriteLine($"上传失败！状态码: {response.StatusCode}");
    Console.WriteLine("响应内容: " + responseContent);
}
```

### C++

```
#include 
#include 
#include 

void uploadFile(const std::string& signedUrl, const std::string& filePath) {
    CURL *curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl) {
        // 设置URL
        curl_easy_setopt(curl, CURLOPT_URL, signedUrl.c_str());

        // 设置请求方法为PUT
        curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);

        // 打开文件
        FILE *file = fopen(filePath.c_str(), "rb");
        if (!file) {
            std::cerr 替换为授权URL。
    std::string signedUrl = "";

    // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    std::string filePath = "C:\\Users\\demo.txt";

    uploadFile(signedUrl, filePath);

    return 0;
}

```

### Android

```
package com.example.signurlupload;

import android.os.AsyncTask;
import android.util.Log;

import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class SignUrlUploadActivity {

    private static final String TAG = "SignUrlUploadActivity";

    public void uploadFile(String signedUrl, String filePath) {
        new UploadTask().execute(signedUrl, filePath);
    }

    private class UploadTask extends AsyncTask {

        @Override
        protected String doInBackground(String... params) {
            String signedUrl = params[0];
            String filePath = params[1];

            HttpURLConnection connection = null;
            DataOutputStream dos = null;
            FileInputStream fis = null;

            try {
                URL url = new URL(signedUrl);
                connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("PUT");
                connection.setDoOutput(true);
                connection.setRequestProperty("Content-Type", "application/octet-stream");

                fis = new FileInputStream(filePath);
                dos = new DataOutputStream(connection.getOutputStream());

                byte[] buffer = new byte[1024];
                int length;

                while ((length = fis.read(buffer)) != -1) {
                    dos.write(buffer, 0, length);
                }

                dos.flush();
                dos.close();
                fis.close();

                int responseCode = connection.getResponseCode();
                Log.d(TAG, "返回上传状态码: " + responseCode);

                if (responseCode == 200) {
                    Log.d(TAG, "使用网络库上传成功");
                }

                return "上传完成，状态码: " + responseCode;

            } catch (IOException e) {
                e.printStackTrace();
                return "上传失败: " + e.getMessage();
            } finally {
                if (connection != null) {
                    connection.disconnect();
                }
            }
        }

        @Override
        protected void onPostExecute(String result) {
            Log.d(TAG, result);
        }
    }

    public static void main(String[] args) {
        SignUrlUploadActivity activity = new SignUrlUploadActivity();
        // 将替换为授权URL。
        String signedUrl = "";
        // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        String filePath = "C:\\Users\\demo.txt";
        activity.uploadFile(signedUrl, filePath);
    }
}

```

## 常见使用场景

### 使用预签名URL上传指定请求头和自定义元数据的文件
- 文件拥有者生成PUT方法的预签名URL。
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

// 设置内容类型为文本
$contentType = "text/plain; charset=utf-8";

// 设置自定义元数据
$metadata = [
    "key1" => "value1",
    "key2" => "value2",
];

// 创建PutObjectRequest对象，用于上传对象。请注意此处加上contentType和metadata参数用于签名计算。
$request = new Oss\Models\PutObjectRequest(bucket: $bucket, key: $key, contentType: $contentType, metadata: $metadata);

// 调用presign方法生成预签名URL
$result = $client->presign($request);

// 打印预签名结果
// 输出预签名URL，用户可以直接使用该URL进行上传操作
print(
    'put object presign result:' . var_export($result, true) . PHP_EOL . // 预签名结果的详细信息
    'put object url:' . $result->url . PHP_EOL                           // 预签名URL，用于直接上传对象
);

```
- 其他人使用PUT方法的预签名URL上传文件。
#### curl

```
curl -X PUT \
     -H "Content-Type: text/plain;charset=utf8" \
     -H "x-oss-storage-class: Standard" \
     -H "x-oss-meta-key1: value1" \
     -H "x-oss-meta-key2: value2" \
     -T "C:\\Users\\demo.txt" \
     "https://exampleobject.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T083238Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************%2F20241112%2Fcn-hangzhou%2Foss%2Faliyun_v4_request&x-oss-signature=ed5a******************************************************"
```

#### Java

```
import com.aliyun.oss.internal.OSSHeaders;
import com.aliyun.oss.model.StorageClass;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.FileEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import java.io.*;
import java.net.URL;
import java.util.*;

public class SignUrlUpload {
    public static void main(String[] args) throws Throwable {
        CloseableHttpClient httpClient = null;
        CloseableHttpResponse response = null;

        // 将替换为授权URL。
        URL signedUrl = new URL("");

        // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        String pathName = "C:\\Users\\demo.txt";

        // 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
        Map headers = new HashMap();
        //指定Object的存储类型。
        headers.put(OSSHeaders.STORAGE_CLASS, StorageClass.Standard.toString());
        //指定ContentType。
        headers.put(OSSHeaders.CONTENT_TYPE, "text/plain;charset=utf8");

        // 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
        Map userMetadata = new HashMap();
        userMetadata.put("key1","value1");
        userMetadata.put("key2","value2");

        try {
            HttpPut put = new HttpPut(signedUrl.toString());
            System.out.println(put);
            HttpEntity entity = new FileEntity(new File(pathName));
            put.setEntity(entity);
            // 如果生成预签名URL时设置了header参数，例如用户元数据，存储类型等，则调用预签名URL上传文件时，也需要将这些参数发送至服务端。如果签名和发送至服务端的不一致，会报签名错误。
            for(Map.Entry header: headers.entrySet()){
                put.addHeader(header.getKey().toString(),header.getValue().toString());
            }
            for(Map.Entry meta: userMetadata.entrySet()){
                // 如果使用userMeta，sdk内部会为userMeta拼接"x-oss-meta-"前缀。当您使用其他方式生成预签名URL进行上传时，userMeta也需要拼接"x-oss-meta-"前缀。
                put.addHeader("x-oss-meta-"+meta.getKey().toString(), meta.getValue().toString());
            }

            httpClient = HttpClients.createDefault();

            response = httpClient.execute(put);

            System.out.println("返回上传状态码："+response.getStatusLine().getStatusCode());
            if(response.getStatusLine().getStatusCode() == 200){
                System.out.println("使用网络库上传成功");
            }
            System.out.println(response.toString());
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            response.close();
            httpClient.close();
        }
    }
}       
```

#### Go

```
package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func uploadFile(signedUrl string, filePath string, headers map[string]string, metadata map[string]string) error {
	// 打开文件
	file, err := os.Open(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	// 读取文件内容
	fileBytes, err := ioutil.ReadAll(file)
	if err != nil {
		return err
	}

	// 创建请求
	req, err := http.NewRequest("PUT", signedUrl, bytes.NewBuffer(fileBytes))
	if err != nil {
		return err
	}

	// 设置请求头
	for key, value := range headers {
		req.Header.Set(key, value)
	}

	// 设置用户自定义元数据
	for key, value := range metadata {
		req.Header.Set(fmt.Sprintf("x-oss-meta-%s", key), value)
	}

	// 发送请求
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// 处理响应
	fmt.Printf("返回上传状态码：%d\n", resp.StatusCode)
	if resp.StatusCode == 200 {
		fmt.Println("使用网络库上传成功")
	} else {
		fmt.Println("上传失败")
	}
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(body))

	return nil
}

func main() {
	// 将替换为授权URL。
	signedUrl := ""

	// 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
	filePath := "C:\\Users\\demo.txt"

	// 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
	headers := map[string]string{
		"Content-Type": "text/plain;charset=utf8",
		"x-oss-storage-class": "Standard",
	}

	// 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
	metadata := map[string]string{
		"key1": "value1",
		"key2": "value2",
	}

	err := uploadFile(signedUrl, filePath, headers, metadata)
	if err != nil {
		fmt.Printf("发生错误：%v\n", err)
	}
}

```

#### Python

```
import requests
from requests.auth import HTTPBasicAuth
import os

def upload_file(signed_url, file_path, headers=None, metadata=None):
    """
    使用预签名的URL上传文件到OSS。

    :param signed_url: 预签名的URL。
    :param file_path: 要上传的文件的完整路径。
    :param headers: 可选，自定义HTTP头部。
    :param metadata: 可选，自定义元数据。
    :return: None
    """
    if not headers:
        headers = {}
    if not metadata:
        metadata = {}

    # 更新headers，添加元数据前缀
    for key, value in metadata.items():
        headers[f'x-oss-meta-{key}'] = value

    try:
        with open(file_path, 'rb') as file:
            response = requests.put(signed_url, data=file, headers=headers)
            print(f"返回上传状态码：{response.status_code}")
            if response.status_code == 200:
                print("使用网络库上传成功")
            else:
                print("上传失败")
            print(response.text)
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    # 将替换为授权URL。
    signed_url = ""
   
    # 填写本地文件的完整路径。如果未指定本地路径，则默认从脚本所在目录中上传文件。
    file_path = "C:\\Users\\demo.txt"

    # 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
    headers = {
         "Content-Type": "text/plain;charset=utf8",
         "x-oss-storage-class": "Standard"
    }

    # 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
    metadata = {
         "key1": "value1",
         "key2": "value2"
    }

    upload_file(signed_url, file_path, headers, metadata)

```

#### Node.js

```
const fs = require('fs');
const axios = require('axios');

async function uploadFile(signedUrl, filePath, headers = {}, metadata = {}) {
    try {
        // 更新headers，添加元数据前缀
        for (const [key, value] of Object.entries(metadata)) {
            headers[`x-oss-meta-${key}`] = value;
        }

        // 读取文件流
        const fileStream = fs.createReadStream(filePath);

        // 发送PUT请求
        const response = await axios.put(signedUrl, fileStream, {
            headers: headers
        });

        console.log(`返回上传状态码：${response.status}`);
        if (response.status === 200) {
            console.log("使用网络库上传成功");
        } else {
            console.log("上传失败");
        }
        console.log(response.data);
    } catch (error) {
        console.error(`发生错误：${error.message}`);
    }
}

// 主函数
(async () => {
    // 将替换为授权URL。
    const signedUrl = "";

    // 填写本地文件的完整路径。如果未指定本地路径，则默认从脚本所在目录中上传文件。
    const filePath = "C:\\Users\\demo.txt";

    // 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
    const headers = {
         "Content-Type": "text/plain;charset=utf8",
         "x-oss-storage-class": "Standard"
    };

    // 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
    const metadata = {
         "key1": "value1",
         "key2": "value2"
    };

    await uploadFile(signedUrl, filePath, headers, metadata);
})();

```

#### Browser.js
重要 如果您使用 Browser.js 上传文件时遇到 403 签名不匹配错误，通常是因为浏览器会自动添加 Content-Type 请求头，而生成预签名 URL 时未指定该请求头，导致签名验证失败。为解决此问题，您需要在生成预签名 URL 时指定 Content-Type 请求头。
```

    
    
    File Upload Example

    
# File Upload Example（Java SDK）

    
    Upload File

    
        // 请替换为实际的预签名URL
        const signedUrl = ""; 

        document.getElementById('uploadButton').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const file = fileInput.files[0];

            if (file) {
                try {
                    await upload(file, signedUrl);
                } catch (error) {
                    console.error('Error during upload:', error);
                    alert('Upload failed: ' + error.message);
                }
            } else {
                alert('Please select a file to upload.');
            }
        });

        const upload = async (file, presignedUrl) => {
            const headers = {
                "Content-Type": "text/plain;charset=utf8",
                'x-oss-storage-class': 'Standard',
                'x-oss-meta-key1': 'value1',
                'x-oss-meta-key2': 'value2'
            };

            const response = await fetch(presignedUrl, {
                method: 'PUT',
                headers: headers,
                body: file
            });

            if (!response.ok) {
                throw new Error(`Upload failed, status: ${response.status}`);
            }

            alert('File uploaded successfully');
            console.log('File uploaded successfully');
        };
    

```

#### C#

```
using System.Net.Http.Headers;

// 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件
var filePath = "C:\\Users\\demo.txt";
// 将替换为授权URL
var presignedUrl = "";

// 创建HTTP客户端并打开本地文件流
using var httpClient = new HttpClient(); 
using var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);
using var content = new StreamContent(fileStream);
            
// 创建PUT请求
var request = new HttpRequestMessage(HttpMethod.Put, presignedUrl);
request.Content = content;

// 如果生成预签名URL时设置了header参数，例如用户元数据，存储类型等，则调用预签名URL上传文件时，也需要将这些参数发送至服务端。如果签名和发送至服务端的不一致，会报签名错误。
// 设置请求头，这里的请求头信息需要与生成URL时的信息一致
request.Content.Headers.ContentType = new MediaTypeHeaderValue("text/plain") { CharSet = "utf8" };  // 指定ContentType       
// 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
request.Content.Headers.Add("x-oss-meta-key1", "value1");
request.Content.Headers.Add("x-oss-meta-key2", "value2");
// 指定Object的存储类型
request.Content.Headers.Add("x-oss-storage-class", "Standard");

// 输出请求头部
Console.WriteLine("请求头部:");
foreach (var header in request.Content.Headers)
{
    Console.WriteLine($"{header.Key}: {string.Join(", ", header.Value)}");
}

// 发送请求
var response = await httpClient.SendAsync(request);

// 处理响应
if (response.IsSuccessStatusCode)
{
    Console.WriteLine($"上传成功！状态码: {response.StatusCode}");
    Console.WriteLine("响应头部:");
    foreach (var header in response.Headers)
    {
        Console.WriteLine($"{header.Key}: {string.Join(", ", header.Value)}");
    }
}
else
{
    string responseContent = await response.Content.ReadAsStringAsync();
    Console.WriteLine($"上传失败！状态码: {response.StatusCode}");
    Console.WriteLine("响应内容: " + responseContent);
}
```

#### C++

```
#include 
#include 
#include 
#include 
#include 

// 回调函数，用于处理HTTP响应
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* output) {
    size_t totalSize = size * nmemb;
    output->append((char*)contents, totalSize);
    return totalSize;
}

void uploadFile(const std::string& signedUrl, const std::string& filePath, const std::map& headers, const std::map& metadata) {
    CURL* curl;
    CURLcode res;
    std::string readBuffer;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl) {
        // 设置URL
        curl_easy_setopt(curl, CURLOPT_URL, signedUrl.c_str());

        // 设置请求方法为PUT
        curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);

        // 打开文件
        FILE* file = fopen(filePath.c_str(), "rb");
        if (!file) {
            std::cerr 替换为授权URL。
    std::string signedUrl = "";

    // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
    std::string filePath = "C:\\Users\\demo.txt";

    // 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
    std::map headers = {
         {"Content-Type", "text/plain;charset=utf8"},
         {"x-oss-storage-class", "Standard"}
    };

    // 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
    std::map metadata = {
         {"key1", "value1"},
         {"key2", "value2"}
    };

    uploadFile(signedUrl, filePath, headers, metadata);

    return 0;
}

```

#### Android

```
import android.os.AsyncTask;
import android.util.Log;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class SignUrlUploadActivity extends AppCompatActivity {

    private static final String TAG = "SignUrlUploadActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // 将替换为授权URL。
        String signedUrl = "";

        // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        String pathName = "/storage/emulated/0/demo.txt";

        // 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
        Map headers = new HashMap<>();
        headers.put("Content-Type", "text/plain;charset=utf8");
        headers.put("x-oss-storage-class", "Standard");

        // 设置用户自定义元数据，这里的用户自定义元数据需要与生成URL时的信息一致。
        Map userMetadata = new HashMap<>();
        userMetadata.put("key1", "value1");
        userMetadata.put("key2", "value2");

        new UploadTask().execute(signedUrl, pathName, headers, userMetadata);
    }

    private class UploadTask extends AsyncTask {
        @Override
        protected Integer doInBackground(Object... params) {
            String signedUrl = (String) params[0];
            String pathName = (String) params[1];
            Map headers = (Map) params[2];
            Map userMetadata = (Map) params[3];

            try {
                URL url = new URL(signedUrl);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("PUT");
                connection.setDoOutput(true);
                connection.setUseCaches(false);

                // 设置请求头
                for (Entry header : headers.entrySet()) {
                    connection.setRequestProperty(header.getKey(), header.getValue());
                }

                // 设置用户自定义元数据
                for (Entry meta : userMetadata.entrySet()) {
                    connection.setRequestProperty("x-oss-meta-" + meta.getKey(), meta.getValue());
                }

                // 读取文件
                File file = new File(pathName);
                FileInputStream fileInputStream = new FileInputStream(file);
                DataOutputStream dos = new DataOutputStream(connection.getOutputStream());

                byte[] buffer = new byte[1024];
                int count;
                while ((count = fileInputStream.read(buffer)) != -1) {
                    dos.write(buffer, 0, count);
                }

                fileInputStream.close();
                dos.flush();
                dos.close();

                // 获取响应
                int responseCode = connection.getResponseCode();
                Log.d(TAG, "返回上传状态码：" + responseCode);
                if (responseCode == 200) {
                    Log.d(TAG, "使用网络库上传成功");
                } else {
                    Log.d(TAG, "上传失败");
                }

                InputStream is = connection.getInputStream();
                byte[] responseBuffer = new byte[1024];
                StringBuilder responseStringBuilder = new StringBuilder();
                while ((count = is.read(responseBuffer)) != -1) {
                    responseStringBuilder.append(new String(responseBuffer, 0, count));
                }
                Log.d(TAG, responseStringBuilder.toString());

                return responseCode;
            } catch (IOException e) {
                e.printStackTrace();
                return -1;
            }
        }

        @Override
        protected void onPostExecute(Integer result) {
            super.onPostExecute(result);
            if (result == 200) {
                Toast.makeText(SignUrlUploadActivity.this, "上传成功", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(SignUrlUploadActivity.this, "上传失败", Toast.LENGTH_SHORT).show();
            }
        }
    }
}

```

### 如何使用预签名URL分片上传文件

使用预签名URL分片上传文件需要配置分片大小并逐片生成预签名URL，示例代码如下：

```
 ['help' => 'The region in which the bucket is located.', 'required' => true],
    "bucket" => ['help' => 'The name of the bucket', 'required' => true],
    "key" => ['help' => 'The name of the object', 'required' => true],
];

// 构建 getopt 需要的长选项格式（如 --region:）
$longopts = array_map(function ($key) {
    return "$key:";
}, array_keys($optsdesc));

// 解析命令行参数
$options = getopt("", $longopts);

// 检查必填参数是否缺失
foreach ($optsdesc as $key => $value) {
    if ($value['required'] === true && empty($options[$key])) {
        echo "Error: the following arguments are required: --$key, " . $value['help'] . "\n";
        exit(1);
    }
}

// 提取参数值
$region = $options["region"];
$bucket = $options["bucket"];
$key = $options["key"];

// 设置本地大文件路径
$bigFileName = "/Users/localpath/yourfilename"; // 替换为你的实际文件路径
$partSize = 1 * 1024 * 1024; // 每个分片大小：1MB
$fileSize = filesize($bigFileName); // 获取文件总大小
$partsNum = intdiv($fileSize, $partSize) + (int)($fileSize % $partSize > 0 ? 1 : 0); // 计算分片数量

// 加载环境变量中的访问密钥
$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

// 使用默认配置初始化客户端，并设置凭证、区域等信息
$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion($region);

// 创建 OSS 客户端实例
$client = new Oss\Client($cfg);

// Step 1: 初始化分片上传任务
// 发起 InitiateMultipartUpload 请求以开始分片上传，并获取 uploadId
$initResult = $client->initiateMultipartUpload(
    new Oss\Models\InitiateMultipartUploadRequest(
        bucket: $bucket,
        key: $key
    )
);

// 保存初始化返回的 uploadId，用于后续操作
$uploadId = $initResult->uploadId;

// Step 2: 循环处理每个分片，生成 Presigned URL 并上传
$parts = []; // 存储每个分片的 ETag 和编号

for ($i = 1; $i presign($request);

    // 提取签名后的 URL 和请求方法
    $signedUrl = $signedResult->url;
    $method = $signedResult->method;

    // 计算当前分片的起始偏移量和长度
    $offset = ($i - 1) * $partSize;
    $length = min($partSize, $fileSize - $offset);

    // 打开大文件流，定位到当前分片位置并读取内容
    $file = new LazyOpenStream($bigFileName, 'rb');
    $file->seek($offset);
    $content = $file->read($length);

    // 使用 HTTP 客户端发送 PUT 请求，上传分片数据
    $http = new Client();
    $response = $http->request($method, $signedUrl, [
        'body' => $content
    ]);

    // 从响应头中提取 ETag（用于最终合并分片）
    $etag = $response->getHeaderLine('ETag');

    // 将分片信息存入数组，用于最后的 CompleteMultipartUpload 请求
    $parts[] = new Oss\Models\UploadPart(
        partNumber: $i,
        etag: $etag
    );

    // 输出上传进度（可选）
    echo "Upload part {$i} success. ETag: {$etag}\n";
}

// Step 3: 完成分片上传
// 创建 CompleteMultipartUpload 请求对象，提交所有分片的信息
$completeRequest = new Oss\Models\CompleteMultipartUploadRequest(
    bucket: $bucket,
    key: $key,
    uploadId: $uploadId,
    completeMultipartUpload: new Oss\Models\CompleteMultipartUpload(
        parts: $parts
    )
);

// 发起完成请求
$comResult = $client->completeMultipartUpload($completeRequest);

// 输出结果信息
printf(
    'status code: %s' . PHP_EOL .
    'request id: %s' . PHP_EOL .
    'complete multipart upload result: %s' . PHP_EOL,
    $comResult->statusCode,
    $comResult->requestId,
    var_export($comResult, true)
);

```

### 使用预签名URL上传文件并设置上传回调参数
- 文件拥有者生成指定上传回调参数的PUT方法的预签名URL。
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

// 添加x-oss-callback和x-oss-callback-var头部信息
// 定义回调地址
$call_back_url = "http://www.example.com/callback";

// 构造回调参数（callback）：指定回调地址和回调请求体，使用 Base64 编码
// 使用占位符 {var1} 和 {var2} 替代 ${x:var1} 和 ${x:var2}
$callback_body_template = "bucket={bucket}&object={object}&my_var_1={var1}&my_var_2={var2}";
$callback_body_replaced = str_replace(
    ['{bucket}', '{object}', '{var1}', '{var2}'],
    [$bucket, $key, 'value1', 'value2'],
    $callback_body_template
);
$callback = base64_encode(json_encode([
    "callbackUrl" => $call_back_url,
    "callbackBody" => $callback_body_replaced
]));

// 构造自定义变量（callback-var），使用 Base64 编码
$callback_var = base64_encode(json_encode([
    "x:var1" => "value1",
    "x:var2" => "value2"
]));

// 创建PutObjectRequest对象，用于上传对象。
// 注意：此处添加了contentType、metadata和headers参数，用于签名计算。
$request = new Oss\Models\PutObjectRequest(
    bucket: $bucket,
    key: $key,
    callback:$callback,
    callbackVar:$callback_var,
);

// 调用presign方法生成预签名URL
$result = $client->presign($request);

// 打印预签名结果，输出预签名URL，用户可以直接使用该URL进行上传操作
print(
    'put object presign result:' . var_export($result, true) . PHP_EOL .
    'put object url:' . $result->url . PHP_EOL
);

```
- 其他人使用PUT方法的预签名URL上传文件。
#### curl

```
curl -X PUT \
     -H "x-oss-callback: eyJjYWxsYmFja1VybCI6Imh0dHA6Ly93d3cuZXhhbXBsZS5jb20vY2FsbGJhY2siLCJjYWxsYmFja0JvZHkiOiJidWNrZXQ9JHtidWNrZXR9Jm9iamVjdD0ke29iamVjdH0mbXlfdmFyXzE9JHt4OnZhcjF9Jm15X3Zhcl8yPSR7eDp2YXIyfSJ9" \
     -H "x-oss-callback-var: eyJ4OnZhcjEiOiJ2YWx1ZTEiLCJ4OnZhcjIiOiJ2YWx1ZTIifQ==" \
     -T "C:\\Users\\demo.txt" \
     "https://exampleobject.oss-cn-hangzhou.aliyuncs.com/exampleobject.txt?x-oss-date=20241112T083238Z&x-oss-expires=3599&x-oss-signature-version=OSS4-HMAC-SHA256&x-oss-credential=LTAI****************%2F20241112%2Fcn-hangzhou%2Foss%2Faliyun_v4_request&x-oss-signature=ed5a******************************************************"
```

#### Python

```
import requests

def upload_file(signed_url, file_path, headers=None):
    """
    使用预签名的URL上传文件到OSS。

    :param signed_url: 预签名的URL。
    :param file_path: 要上传的文件的完整路径。
    :param headers: 可选，自定义HTTP头部。
    :return: None
    """
    if not headers:
        headers = {}

    try:
        with open(file_path, 'rb') as file:
            response = requests.put(signed_url, data=file, headers=headers)
            print(f"返回上传状态码：{response.status_code}")
            if response.status_code == 200:
                print("使用网络库上传成功")
            else:
                print("上传失败")
            print(response.text)
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    # 将替换为授权URL。
    signed_url = ""

    # 填写本地文件的完整路径。如果未指定本地路径，则默认从脚本所在目录中上传文件。
    file_path = "C:\\Users\\demo.txt"

    headers = {
        "x-oss-callback": "eyJjYWxsYmFja1VybCI6Imh0dHA6Ly93d3cuZXhhbXBsZS5jb20vY2FsbGJhY2siLCJjYWxsYmFja0JvZHkiOiJidWNrZXQ9JHtidWNrZXR9Jm9iamVjdD0ke29iamVjdH0mbXlfdmFyXzE9JHt4OnZhcjF9Jm15X3Zhcl8yPSR7eDp2YXIyfSJ9",
        "x-oss-callback-var": "eyJ4OnZhcjEiOiJ2YWx1ZTEiLCJ4OnZhcjIiOiJ2YWx1ZTIifQ==",
    }

    upload_file(signed_url,  file_path, headers)
```

#### Go

```
package main

import (
	"bytes"
	"fmt"
	"io"

	"net/http"
	"os"
)

func uploadFile(signedUrl string, filePath string, headers map[string]string) error {
	// 打开文件
	file, err := os.Open(filePath)
	if err != nil {
		return err
	}
	defer file.Close()

	// 读取文件内容
	fileBytes, err := io.ReadAll(file)
	if err != nil {
		return err
	}

	// 创建请求
	req, err := http.NewRequest("PUT", signedUrl, bytes.NewBuffer(fileBytes))
	if err != nil {
		return err
	}

	// 设置请求头
	for key, value := range headers {
		req.Header.Add(key, value)
	}

	// 发送请求
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// 处理响应
	fmt.Printf("返回上传状态码：%d\n", resp.StatusCode)
	if resp.StatusCode == 200 {
		fmt.Println("使用网络库上传成功")
	} else {
		fmt.Println("上传失败")
	}
	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))

	return nil
}

func main() {
	// 将替换为授权URL。
	signedUrl := ""
	// 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
	filePath := "C:\\Users\\demo.txt"

	// 设置请求头，这里的请求头信息需要与生成URL时的信息一致。
	headers := map[string]string{
		"x-oss-callback":     "eyJjYWxsYmFja1VybCI6Imh0dHA6Ly93d3cuZXhhbXBsZS5jb20vY2FsbGJhY2siLCJjYWxsYmFja0JvZHkiOiJidWNrZXQ9JHtidWNrZXR9Jm9iamVjdD0ke29iamVjdH0mbXlfdmFyXzE9JHt4OnZhcjF9Jm15X3Zhcl8yPSR7eDp2YXIyfSJ9",
		"x-oss-callback-var": "eyJ4OnZhcjEiOiJ2YWx1ZTEiLCJ4OnZhcjIiOiJ2YWx1ZTIifQ==",
	}

	err := uploadFile(signedUrl, filePath, headers)
	if err != nil {
		fmt.Printf("发生错误：%v\n", err)
	}
}

```

#### Java

```
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.FileEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import java.io.*;
import java.net.URL;
import java.util.*;

public class SignUrlUpload {
    public static void main(String[] args) throws Throwable {
        CloseableHttpClient httpClient = null;
        CloseableHttpResponse response = null;

        // 将替换为授权URL。
        URL signedUrl = new URL("");

        // 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
        String pathName = "C:\\Users\\demo.txt";

        // 设置请求头，包括x-oss-callback和x-oss-callback-var。
        Map headers = new HashMap();
        headers.put("x-oss-callback", "eyJjYWxsYmFja1VybCI6Imh0dHA6Ly93d3cuZXhhbXBsZS5jb20vY2FsbGJhY2siLCJjYWxsYmFja0JvZHkiOiJidWNrZXQ9JHtidWNrZXR9Jm9iamVjdD0ke29iamVjdH0mbXlfdmFyXzE9JHt4OnZhcjF9Jm15X3Zhcl8yPSR7eDp2YXIyfSJ9");
        headers.put("x-oss-callback-var", "eyJ4OnZhcjEiOiJ2YWx1ZTEiLCJ4OnZhcjIiOiJ2YWx1ZTIifQ==");

        try {
            HttpPut put = new HttpPut(signedUrl.toString());
            System.out.println(put);
            HttpEntity entity = new FileEntity(new File(pathName));
            put.setEntity(entity);
            // 如果生成预签名URL时设置了header参数，则调用预签名URL上传文件时，也需要将这些参数发送至服务端。如果签名和发送至服务端的不一致，会报签名错误。
            for(Map.Entry header: headers.entrySet()){
                put.addHeader(header.getKey().toString(),header.getValue().toString());
            }

            httpClient = HttpClients.createDefault();

            response = httpClient.execute(put);

            System.out.println("返回上传状态码："+response.getStatusLine().getStatusCode());
            if(response.getStatusLine().getStatusCode() == 200){
                System.out.println("使用网络库上传成功");
            }
            System.out.println(response.toString());
        } catch (Exception e){
            e.printStackTrace();
        } finally {
            response.close();
            httpClient.close();
        }
    }
}       
```

#### PHP

```
替换为授权URL。
$signedUrl = "";

// 填写本地文件的完整路径。如果未指定本地路径，则默认从脚本所在目录中上传文件。
$filePath = "C:\\Users\\demo.txt";

$headers = [
    "x-oss-callback" => "eyJjYWxsYmFja1VybCI6Imh0dHA6Ly93d3cuZXhhbXBsZS5jb20vY2FsbGJhY2siLCJjYWxsYmFja0JvZHkiOiJidWNrZXQ9JHtidWNrZXR9Jm9iamVjdD0ke29iamVjdH0mbXlfdmFyXzE9JHt4OnZhcjF9Jm15X3Zhcl8yPSR7eDp2YXIyfSJ9",
    "x-oss-callback-var" => "eyJ4OnZhcjEiOiJ2YWx1ZTEiLCJ4OnZhcjIiOiJ2YWx1ZTIifQ==",
];

uploadFile($signedUrl, $filePath, $headers);

?>
```

## 相关文档
- 关于预签名URL的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/alibabacloud-oss-php-sdk-v2/blob/master/sample/Presign.php)。
- 关于预签名URL的API接口，请参见[Presign](https://pkg.go.dev/github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss#Client.Presign)。

[上一篇：表单上传（PHP SDK V2）](/zh/oss/developer-reference/form-upload-using-oss-sdk-for-php-v2)[下一篇：文件上传管理器（PHP SDK V2）](/zh/oss/developer-reference/file-uploader-with-oss-sdk-for-php-v2)该文章对您有帮助吗？反馈
  
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