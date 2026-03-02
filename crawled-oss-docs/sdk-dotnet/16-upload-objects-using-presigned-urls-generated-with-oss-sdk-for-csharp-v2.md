# 使用C# SDK V2生成预签名URL以上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-objects-using-presigned-urls-generated-with-oss-sdk-for-csharp-v2

---

- 使用C# SDK V2生成预签名URL以上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 使用预签名URL上传（C# SDK V2）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
默认情况下，OSS Bucket中的文件是私有的，仅文件拥有者拥有上传权限。您可以使用OSS C# SDK生成预签名URL，以允许他人通过该URL上传文件。在生成预签名URL时，可以自定义其过期时间以限制访问持续时长。在预签名URL有效期内，该URL可被多次访问。如果多次执行上传操作，会有文件覆盖的风险。超出有效期后，将无法进行上传，此时需要重新生成预签名URL。

## 注意事项
- 本文示例代码以华东1（杭州）的地域ID`cn-hangzhou`为例，默认使用外网Endpoint，如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[OSS地域和访问域名](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 预签名URL无需权限即可生成，但仅当您拥有`oss:PutObject`权限时，第三方才能通过该预签名URL成功上传文件。具体授权操作，请参见[为RAM用户授权自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-flo-x8e-e94)。

## 使用过程

使用PUT方式的预签名URL上传文件的过程如下：

## 示例代码
- 文件拥有者生成PUT方法的预签名URL。重要 在生成PUT方法的预签名URL时，如果指定了请求头，确保在通过该预签名URL发起PUT请求时也包含相应的请求头，以免出现不一致，导致请求失败和预签名错误。
```
using System.Text;
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var bucket = "your bucket name";  // 必须项，Bucket名称
var key = "your object key";  // 必须项，上传到OSS后的对象名称

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;   
// 若已指定了endpoint，则覆盖默认的endpoint 
if(endpoint != null) 
{
    cfg.Endpoint = endpoint;
} 

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg); 
// 调用Presign方法生成预签名URL
var result = client.Presign(new OSS.Models.PutObjectRequest()
{
    Bucket = bucket,
    Key = key,
});

// 要上传的内容
const string content = "hello oss!";
// 使用HttpClient通过预签名URL上传内容
using var hc = new HttpClient();
var httpResult = await hc.PutAsync(result.Url, new ByteArrayContent(Encoding.UTF8.GetBytes(content)));

Console.WriteLine("PutObject done");  // 打印操作完成提示
Console.WriteLine($"StatusCode: {httpResult.StatusCode}");  //HTTP响应状态码
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

### 使用预签名URL指定请求头和自定义元数据上传文件
- 文件拥有者生成指定请求头和自定义元数据的PUT方法的预签名URL。
```
using System.Text;
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用
using System.Globalization;
using System.Net.Http.Headers;

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var bucket = "your bucket name";  // 必须项，Bucket名称
var key = "your object key";  // 必须项，上传到OSS后的对象名称

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;   
// 若已指定了endpoint，则覆盖默认的endpoint 
if(endpoint != null) 
{ 
    cfg.Endpoint = endpoint;
} 

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg); 
// 调用Presign方法获取预签名上传URL
var result = client.Presign(new OSS.Models.PutObjectRequest()
    {
        Bucket = bucket,
        Key = key,
        StorageClass = "Standard",         // 设置存储类型为标准存储
        ContentType = "text/plain; charset=utf8",    // 设置内容类型
        Metadata = new Dictionary() {
            { "key1", "value1" },    // 添加自定义元数据
            { "key2", "value2" }
        }
    }
);

// 创建HTTP客户端实例
using var hc = new HttpClient();

// 准备要上传的内容
var content1 = "hello oss";
var requestMessage = new HttpRequestMessage(HttpMethod.Put, new Uri(result.Url));
requestMessage.Content = new ByteArrayContent(Encoding.UTF8.GetBytes(content1));

// 添加预签名URL中包含的HTTP头
foreach (var item in result.SignedHeaders!)
{
    switch (item.Key.ToLower())
    {
        case "content-disposition":
            // 设置内容的展示方式
            requestMessage.Content.Headers.ContentDisposition = ContentDispositionHeaderValue.Parse(item.Value);
            break;
        case "content-encoding":
            // 设置内容的编码方式
            requestMessage.Content.Headers.ContentEncoding.Add(item.Value);
            break;
        case "content-language":
            // 设置内容的语言
            requestMessage.Content.Headers.ContentLanguage.Add(item.Value);
            break;
        case "content-type":
            // 设置内容类型
            requestMessage.Content.Headers.ContentType = MediaTypeHeaderValue.Parse(item.Value);
            break;
        case "content-md5":
            // 设置内容的MD5校验值
            requestMessage.Content.Headers.ContentMD5 = Convert.FromBase64String(item.Value);
            break;
        case "content-length":
            // 设置内容长度
            requestMessage.Content.Headers.ContentLength = Convert.ToInt64(item.Value);
            break;
        case "expires":
            // 设置内容的过期时间
            if (DateTime.TryParse(
                    item.Value,
                    CultureInfo.InvariantCulture,
                    DateTimeStyles.None,
                    out var expires
                ))
                requestMessage.Content.Headers.Expires = expires;
            break;
        default:
            // 添加其他通用头信息
            requestMessage.Headers.Add(item.Key, item.Value);
            break;
    }
}
// 发送HTTP请求并获取响应
var httpResult = await hc.SendAsync(requestMessage);

Console.WriteLine("PutObject done");  // 打印操作完成提示
Console.WriteLine($"StatusCode: {httpResult.StatusCode}");  //HTTP响应状态码
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

### 使用预签名URL分片上传文件

使用预签名URL分片上传文件需要配置分片大小并逐片生成预签名URL，示例代码如下：

```
using OSS = AlibabaCloud.OSS.V2;  // 为阿里云OSS SDK创建别名，简化后续使用

var region = "cn-hangzhou";  // 必须项，设置Bucket所在的区域（Region）。以华东1（杭州）为例，Region填写为cn-hangzhou
var endpoint = null as string;  // 可选项，指定访问OSS服务的域名。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com
var bucket = "you bucket name";  // 必须项，Bucket名称
var key = "your object key";  // 必须项，待上传的目标文件对象名称
var partSize = 512*1024;  // 必须项，每次上传文件的分片大小，以分片大小为512KB为例
var filePath = "filePath";  // 必须项，需上传的目标文件路径

// 加载OSS SDK的默认配置，此配置会自动从环境变量中读取凭证信息（如AccessKey）
var cfg = OSS.Configuration.LoadDefault();
// 显式设置使用环境变量获取凭证，用于身份验证（格式：OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET）
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
// 设置配置的Bucket区域
cfg.Region = region;   
// 若已指定了endpoint，则覆盖默认的endpoint 
if(endpoint != null) 
{
    cfg.Endpoint = endpoint;
} 

// 使用配置信息创建OSS客户端实例
using var client = new OSS.Client(cfg); 

// 初始化分片上传
var initResult = await client.InitiateMultipartUploadAsync(new()
{
    Bucket = bucket,
    Key = key
});

// 打开要上传的文件
using var hc = new HttpClient();
using var file = File.OpenRead(filePath);
long fileSize = file.Length;
long partNumber = 1;

// 分块上传文件
for (long offset = 0; offset ();
var paginator = client.ListPartsPaginator(new ()
{
    Bucket = bucket,
    Key = key,
    UploadId = initResult.UploadId,
});

// 分页获取所有分片信息
await foreach (var page in paginator.IterPageAsync())
{
    foreach (var part in page.Parts ?? [])
    {
        uploadParts.Add(new() { PartNumber = part.PartNumber, ETag = part.ETag });
    }
}

// 按分片号排序
uploadParts.Sort((left, right) => { return (left.PartNumber > right.PartNumber) ? 1 : -1; });

// 完成分片上传
var cmResult = await client.CompleteMultipartUploadAsync(new()
{
    Bucket = bucket,
    Key = key,
    UploadId = initResult.UploadId,
    CompleteMultipartUpload = new()
    {
        Parts = uploadParts
    }
});

// 打印上传结果
Console.WriteLine("MultipartUpload done");  // 提示操作完成
Console.WriteLine($"StatusCode: {cmResult.StatusCode}");  // HTTP状态码
Console.WriteLine($"RequestId: {cmResult.RequestId}");  // RequestId，用于阿里云排查问题
Console.WriteLine("Response Headers:");  // 响应头信息
cmResult.Headers.ToList().ForEach(x => Console.WriteLine(x.Key + " : " + x.Value));  // 遍历并打印所有响应头
```

## 常见问题

### 使用临时签名进行文件上传时，在上传过程中签名过期了，上传中的文件会失败吗？

上传时不会失败。

上传时使用的是预签名地址，该URL只要是在有效期里（取Token的有效期和预签名有效期最小值），都可以使用。

### 如果我在生成URL时未设置请求头和自定义元数据，在使用URL上传时还需要配置吗？

不需要配置。

请求头和自定义元数据为非必要参数，如果不设置请求头和自定义元数据可以将示例中相关代码去掉。

## 相关文档

关于使用预签名URL上传的完整示例代码，请参见[PresignPutObject.cs](https://github.com/aliyun/alibabacloud-oss-csharp-sdk-v2/blob/master/sample/PresignPutObject/Program.cs)。

[上一篇：表单上传（C# SDK V2）](/zh/oss/developer-reference/form-upload-using-oss-sdk-for-csharp-v2)[下一篇：下载文件（C# SDK V2）](/zh/oss/developer-reference/download-file-using-oss-sdk-for-c-v2/)该文章对您有帮助吗？反馈
  
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