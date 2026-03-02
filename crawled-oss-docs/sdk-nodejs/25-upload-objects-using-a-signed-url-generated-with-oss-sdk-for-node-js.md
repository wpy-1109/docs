# 使用预签名URL临时授权上传文件

Source: https://help.aliyun.com/zh/oss/developer-reference/upload-objects-using-a-signed-url-generated-with-oss-sdk-for-node-js

---

- 使用预签名URL临时授权上传文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 使用预签名URL上传（Node.js SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
默认情况下，OSS Bucket中的文件是私有的，仅文件拥有者拥有上传权限。您可以使用OSS Node.js SDK生成预签名URL，以允许他人通过该URL上传文件。在生成预签名URL时，可以自定义其过期时间以限制访问持续时长。在预签名URL有效期内，该URL可被多次访问。如果多次执行上传操作，会有文件覆盖的风险。超出有效期后，将无法进行上传，此时需要重新生成预签名URL。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以从环境变量读取访问凭证为例。如何配置访问凭证，请参见[配置访问凭证（Node.js SDK）](https://help.aliyun.com/zh/oss/node-js-configure-access-credentials)。
- 生成用于上传的预签名URL时，您必须具有`oss:PutObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。说明 生成预签名URL过程中，SDK利用本地存储的密钥信息，根据特定算法计算出签名（signature），然后将其附加到URL上，以确保URL的有效性和安全性。这一系列计算和构造URL的操作都是在客户端完成，不涉及网络请求到服务端。因此，生成预签名URL时不需要授予调用者特定权限。但是，为避免第三方用户无法对预签名URL授权的资源执行相关操作，需要确保调用生成预签名URL接口的身份主体被授予对应的权限。
- 本文以V4预签名URL为例，有效期最大为7天。更多信息，请参见[签名版本4（推荐）](https://help.aliyun.com/zh/oss/developer-reference/add-signatures-to-urls)。

## 使用过程

使用PUT方式的预签名URL上传文件的过程如下：

## 代码示例
- 文件拥有者生成PUT方法的预签名URL。
```
const OSS = require("ali-oss");

// 定义一个生成签名 URL 的函数
async function generateSignatureUrl(fileName) {
  // 获取预签名URL
  const client = await new OSS({
      accessKeyId: 'yourAccessKeyId',
      accessKeySecret: 'yourAccessKeySecret',
      bucket: 'examplebucket',
      region: 'oss-cn-hangzhou',
      authorizationV4: true
  });

  return await client.signatureUrlV4('PUT', 3600, {
      headers: {} // 请根据实际发送的请求头设置此处的请求头
  }, fileName);
}
// 调用函数并传入文件名
generateSignatureUrl('yourFileName').then(url => {
  console.log('Generated Signature URL:', url);
}).catch(err => {
  console.error('Error generating signature URL:', err);
});
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

## 其他场景

### 生成带图片处理参数的预签名URL

```
const OSS = require("ali-oss");

const client = await new OSS({
  accessKeyId: 'yourAccessKeyId',
  accessKeySecret: 'yourAccessKeySecret',
  stsToken: 'yourSecurityToken',
  bucket: 'yourBucket',
  region: 'yourRegion',
  // 设置secure为true，使用HTTPS，避免生成的下载链接被浏览器拦截
  secure: true,
});

// 生成签名的URL
const signedUrl = await client.signatureUrlV4('GET', 3600, {
  queries:{
    // 设置图片处理参数
    "x-oss-process": 'image/resize,w_200',
  }
}, 'demo.pdf');

```

### 生成带versionId的预签名URL

```
const OSS = require("ali-oss");

const client = await new OSS({
  accessKeyId: 'yourAccessKeyId',
  accessKeySecret: 'yourAccessKeySecret',
  stsToken: 'yourSecurityToken',
  bucket: 'yourBucket',
  region: 'yourRegion',
  // 设置secure为true，使用HTTPS，避免生成的下载链接被浏览器拦截
  secure: true,
});

// 生成签名的URL
const signedUrl = await client.signatureUrlV4('GET', 3600, {
  queries:{
    // 填写 Object 的 versionId
    "versionId":'yourVersionId'
  }
}, 'demo.pdf');
```

## 常见问题

### 使用临时签名进行文件上传时，在上传过程中签名过期了，上传中的文件会失败吗？

上传时不会失败。

上传时使用的是预签名地址，该URL只要是在有效期里（取Token的有效期和预签名有效期最小值），都可以使用。

### 生成预签名URL时是否支持使用POST方法？

不支持。

生成预签名URL时仅支持使用PUT和GET方法。如果您需要通过POST方法进行上传，您需要参考[PostObject](https://help.aliyun.com/zh/oss/developer-reference/postobject#reference-smp-nsw-wdb)自行构造POST请求。

## 相关文档
- 关于使用预签名URL上传文件的API接口说明，请参见[GeneratePresignedUrlRequest](https://javadoc.io/doc/com.aliyun.oss/aliyun-sdk-oss/3.14.0/com/aliyun/oss/model/GeneratePresignedUrlRequest.html)。

[上一篇：上传回调（Node.js SDK）](/zh/oss/developer-reference/upload-callbacks-4)[下一篇：下载文件（Node.js SDK）](/zh/oss/developer-reference/download-objects-6/)该文章对您有帮助吗？反馈
  
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