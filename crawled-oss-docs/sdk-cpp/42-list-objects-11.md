# 使用C++ SDK列举存储空间的文件及目录

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects-11

---

- 使用C++ SDK列举存储空间的文件及目录-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 列举文件（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何列举指定存储空间（Bucket）的所有文件、指定个数的文件以及指定目录下的文件大小等。

## 背景信息

OSS 文件按照字母顺序排列。您可以通过OssClient.ListObjects列出存储空间下的文件。ListObjects有以下三类参数格式：
- ListObjectOutcome ListObjects(const std::string& bucket) const：列举存储空间下的文件。最多列举1000个文件。
- ListObjectOutcome ListObjects(const std::string& bucket, const std::string& prefix) const： 列举存储空间下指定前缀的文件。最多列举 1000 个文件。
- ListObjectOutcome ListObjects(const ListObjectsRequest& request) const：提供多种过滤功能，实现灵活的查询功能。

主要参数及说明如下：
| 参数 | 描述|
| delimiter | 对文件名称进行分组的一个字符。所有名称包含指定的前缀且第一次出现delimiter字符之间的文件作为一组（commonPrefixes）。|
| prefix | 限定返回的文件必须以prefix作为前缀。|
| maxKeys | 限定此次列举文件的最大个数。默认值为100，最大值为1000。|
| marker | 列举指定marker之后的文件。|

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。
- 要列举文件，您必须有`oss:ListObjects`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 简单列举文件

以下代码用于列举指定存储空间下的文件，默认列举100个文件。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 列举文件。*/
    ListObjectsRequest request(BucketName);
    auto outcome = client.ListObjects(request);

    if (!outcome.isSuccess())  {    
        /* 异常处理。*/
        std::cout 
## 列举指定个数的文件

以下代码用于列举指定个数的文件。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
    
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

     /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    /* 列举文件。*/
    ListObjectsRequest request(BucketName);
    /* 设置列举文件的最大个数为200。*/
    request.setMaxKeys(200);
    auto outcome = client.ListObjects(request);

    if (!outcome.isSuccess( )) {    
        /* 异常处理。*/
        std::cout 
## 列举指定目录下的文件和子目录

以下代码用于列举指定目录下的文件和子目录：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写列举的文件前缀（Prefix）。*/
    std::string keyPrefix = "yourkeyPrefix";

     /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    std::string nextMarker = "";
    bool isTruncated = false;  
    do {
        /* 列举文件。*/
        ListObjectsRequest request(BucketName);
         /* 设置正斜线（/）为文件夹的分隔符 */
        request.setDelimiter("/");
        request.setPrefix(keyPrefix);
        request.setMarker(nextMarker);
        auto outcome = client.ListObjects(request);

        if (!outcome.isSuccess ()) {    
            /* 异常处理。*/
            std::cout 
## 列举指定目录下的文件大小

以下代码用于获取指定目录下的文件大小：

```
#include 
#include 

using namespace AlibabaCloud::OSS;

static int64_t calculateFolderLength(const OssClient &client, const std::string &bucketName, const std::string &folder)
{
    std::string nextMarker = "";
    bool isTruncated = false; 
    int64_t size = 0;
    do {
        /* 列举文件。*/
        ListObjectsRequest request(bucketName);
        request.setPrefix(folder);
        request.setMarker(nextMarker);
        auto outcome = client.ListObjects(request);
        if (!outcome.isSuccess()) {    
            /* 异常处理 */
            std::cout ();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
    std::string nextMarker = "";
    bool isTruncated = false; 
    do {
        /* 列举文件。*/
        ListObjectsRequest request(BucketName);
        /* 设置正斜线（/）为文件夹的分隔符。*/
        request.setDelimiter("/");
        request.setPrefix(keyPrefix);
        request.setMarker(nextMarker);
        auto outcome = client.ListObjects(request);
        if (!outcome.isSuccess()) {    
            /* 异常处理。*/
            std::cout 
## 列举指定前缀的文件

以下代码用于列举包含指定前缀（prefix）的文件。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
     /* 初始化OSS账号信息。*/
               
     /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
     std::string Endpoint = "yourEndpoint";
     /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
     std::string Region = "yourRegion";
     /* 填写Bucket名称，例如examplebucket。*/
     std::string BucketName = "examplebucket";
     /* 填写列举的文件前缀（Prefix）。*/
     std::string keyPrefix = "yourkeyPrefix";

      /* 初始化网络等资源。*/
      InitializeSdk();

      ClientConfiguration conf;
      conf.signatureVersion = SignatureVersionType::V4;
      /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
      std::string nextMarker = "";
      bool isTruncated = false; 
      do {
              /* 列举文件。*/
              ListObjectsRequest request(BucketName);              
              request.setPrefix(keyPrefix);
              request.setMarker(nextMarker);
              auto outcome = client.ListObjects(request);

              if (!outcome.isSuccess()) {    
                    /* 异常处理。*/
                    std::cout 
## 列举指定marker之后的文件

参数marker代表文件名称。以下代码用于列举指定marker之后的文件。

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
      /* 初始化OSS账号信息。*/
                  
      /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
      std::string Endpoint = "yourEndpoint";
      /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
      std::string Region = "yourRegion";
      /* 填写Bucket名称，例如examplebucket。*/
      std::string BucketName = "examplebucket";
      /* 设置marker。*/
      std::string YourMarker = "yourMarker";

      /* 初始化网络等资源。*/
      InitializeSdk();

      ClientConfiguration conf;
      conf.signatureVersion = SignatureVersionType::V4;
      /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
      
    ListObjectOutcome outcome;
      do {
              /* 列举文件 */
              ListObjectsRequest request(BucketName);
              /* 列举指定marker之后的文件 */
              request.setMarker(YourMarker);
              outcome = client.ListObjects(request);

              if (!outcome.isSuccess()) {    
                    /* 异常处理 */
                    std::cout 
## 指定文件名称编码

如果文件名称含有以下特殊字符，需要进行编码传输。OSS目前仅支持URL编码。
- 单引号（''）
- 双引号（""）
- and符号（&）
- 尖括号（< >）
- 顿号（、）
- 中文

以下代码用于指定文件名称编码：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

    /* 初始化网络等资源 */
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    std::string nextMarker = "";
    bool isTruncated = false; 
    do {
        /* 列举文件。*/
        ListObjectsRequest request(BucketName) ;
        /* 指定文件名称编码。*/
        request.setEncodingType("url");
        request.setMarker(nextMarker);
        auto outcome = client.ListObjects(request);

        if (!outcome.isSuccess() ) {    
            /* 异常处理。*/
            std::cout 
## 文件夹功能

OSS没有文件夹的概念，所有元素都是以文件来存储。创建文件夹本质上来说是创建了一个大小为0并以正斜线（/）结尾的文件。这个文件可以被上传和下载，控制台会对以正斜线（/）结尾的文件以文件夹的方式展示。

通过delimiter和prefix两个参数可以模拟文件夹功能：
- 如果设置prefix为某个文件夹名称，则会列举以此prefix开头的文件，即该文件夹下所有的文件和子文件夹（目录）均显示为objects。
- 如果在设置了prefix的情况下，将delimiter设置为正斜线（/），则只列举该文件夹下的文件和子文件夹（目录），该文件夹下的子文件夹（目录）显示为CommonPrefixes，子文件夹下的文件和文件夹不显示。

假设存储空间中包含文件`oss.jpg`、`fun/test.jpg`、`fun/movie/001.avi`和`fun/movie/007.avi`，以正斜线（/）作为文件夹的分隔符。以下示例说明了如何通过模拟文件夹的方式列举文件。
- 列举存储空间下所有文件以下代码用于列举指定存储空间下的所有文件。
```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    std::string nextMarker = "";
    bool isTruncated = false; 
    do {
        /* 列举文件。*/
        ListObjectsRequest request(BucketName);
        request.setMarker(nextMarker);
        auto outcome = client.ListObjects(request);

        if (!outcome.isSuccess()) {    
            /* 异常处理。*/
            std::cout 返回结果如下：
```
Objects:
fun/movie/001.avi
fun/movie/007.avi
fun/test.jpg
oss.jpg

CommonPrefixes:
```
- 列举指定目录下所有文件以下代码用于列举指定目录下的所有文件。
```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    std::string nextMarker = "";
    bool isTruncated = false; 
    do {
            /* 列举文件。*/
            ListObjectsRequest request(BucketName);
            request.setPrefix("fun/");
            request.setMarker(nextMarker);
            auto outcome = client.ListObjects(request);

            if (!outcome.isSuccess()) {    
                /* 异常处理。*/
                std::cout 返回结果如下：
```
Objects:
fun/movie/001.avi
fun/movie/007.avi
fun/test.jpg

CommonPrefixes:
```
- 列举目录下的文件和子目录以下代码用于列举指定目录下的文件和子目录。
```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息。*/
            
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";

    /* 初始化网络等资源。*/
    InitializeSdk();

    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    std::string nextMarker = "";
    bool isTruncated = false;
    do {
            /* 列举文件。*/
            ListObjectsRequest request(BucketName);
            /* 设置正斜线（/）为文件夹的分隔符 */
            request.setDelimiter("/");
            request.setPrefix("fun/");
            request.setMarker(nextMarker);
            auto outcome = client.ListObjects(request);

            if (!outcome.isSuccess()) {    
                /* 异常处理。*/
                std::cout 返回结果如下：
```
Objects:
fun/test.jpg

CommonPrefixes:
fun/movie/
```
- 列举指定目录下的文件大小 以下代码用于获取指定目录下的文件大小：
```
#include 
using namespace AlibabaCloud::OSS;

static int64_t calculateFolderLength (const OssClient &client, const std::string &bucketName, const std::string &folder)
{
    std::string nextMarker = "";
    bool isTruncated = false;
    int64_t size = 0;
    do {
            /* 列举文件。*/
            ListObjectsRequest request(bucketName);
            request.setPrefix(folder);
            request.setMarker(nextMarker);
            auto outcome = client.ListObjects(request);

            if (!outcome.isSuccess()) {    
                /* 异常处理。*/
                std::cout ();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);

    std::string nextMarker = "";
    bool isTruncated = false;
    do {
        /* 列举文件。*/
        ListObjectsRequest request(BucketName);
        /* 设置正斜线（/）为文件夹的分隔符。*/
        request.setDelimiter("/");
        request.setPrefix("fun/");
        request.setMarker(nextMarker);
        auto outcome = client.ListObjects(request);

        if (!outcome.isSuccess()) {    
            /* 异常处理。*/
            std::cout 
## 相关文档
- 关于列举文件的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-cpp-sdk/blob/16a995a66b14f236e7fed9787e2dc0bb463d6e47/sample/src/bucket/BucketSample.cc?spm=a2c4g.11186623.0.0.13723e061yNWI4#L261)。
- 关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)和[ListObjectsV2（GetBucketV2）](https://help.aliyun.com/zh/oss/developer-reference/listobjects-v2#reference-2520881)。

[上一篇：转换文件存储类型（C++ SDK）](/zh/oss/developer-reference/convert-the-storage-classes-of-objects-1)[下一篇：删除文件（C++ SDK）](/zh/oss/developer-reference/delete-objects-10)该文章对您有帮助吗？反馈
  
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