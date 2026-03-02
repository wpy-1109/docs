# C++SDK客户端加密方法与示例

Source: https://help.aliyun.com/zh/oss/developer-reference/client-side-encryption-3

---

- C++SDK客户端加密方法与示例-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 客户端加密（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS客户端加密是在数据上传至OSS之前，由用户在本地对数据进行加密处理，确保只有密钥持有者才能解密数据，增强数据在传输和存储过程中的安全性。

## 免责声明
- 使用客户端加密功能时，您需要对主密钥的完整性和正确性负责。因您维护不当导致主密钥用错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由您自行承担。
- 在对加密数据进行复制或者迁移时，您需要对加密元数据的完整性和正确性负责。因您维护不当导致加密元数据出错或丢失，从而导致加密数据无法解密所引起的一切损失和后果均由您自行承担。

## 使用场景
- 高度敏感数据：对于包含极高敏感度信息的数据，如个人身份信息（PII）、金融交易记录、医疗健康数据等，用户可能希望在数据离开本地环境之前就对其进行加密处理，确保即使数据在传输过程中被截获，原始数据仍能得到有效保护。
- 合规要求：某些行业和法规（例如HIPAA、GDPR等）要求对存储在第三方平台上的数据进行严格的加密控制，客户端加密能够满足这些合规性要求，因为密钥由用户自己管理，不通过网络传递，也不由云服务商直接掌握。
- 更强的自主控制权：企业或者开发者可能希望对加密过程有完全的控制权，包括选择加密算法、管理和轮换密钥。通过客户端加密，可以实现这一目标，确保只有合法授权的用户才能解密和访问数据。
- 跨区域数据迁移安全性：在将数据从一个地区迁移到另一个地区的过程中，使用客户端加密可以在数据迁移前后保持数据始终处于加密状态，增强了数据在公网传输的安全性。

## 注意事项
- 本文以华东1（杭州）外网Endpoint为例。如果您希望通过与OSS同地域的其他阿里云产品访问OSS，请使用内网Endpoint。关于OSS支持的Region与Endpoint的对应关系，请参见[地域和Endpoint](https://help.aliyun.com/zh/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db)。
- 本文以OSS域名新建OSSClient为例。如果您希望通过自定义域名、STS等方式新建OSSClient，请参见[新建OssClient](https://help.aliyun.com/zh/oss/developer-reference/initialization-12#section-nqa-yww-gxo)。

## 背景信息

使用客户端加密时，会为每个Object生成一个随机数据加密密钥，用该随机数据加密密钥明文对Object的数据进行对称加密。主密钥用于生成随机的数据加密密钥，加密后的内容会作为Object的meta信息保存在服务端。解密时先用主密钥将加密后的随机密钥解密出来，再用解密出来的随机数据加密密钥明文解密Object的数据。主密钥只参与客户端本地计算，不会在网络上进行传输或保存在服务端，以保证主密钥的数据安全。
重要 - 客户端加密支持分片上传超过5 GB的文件。在使用分片方式上传文件时，需要指定上传文件的总大小和分片大小， 除了最后一个分片外，每个分片的大小要一致，且分片大小目前必须是16的整数倍。
- 调用客户端加密上传文件后，加密元数据会被保护，无法通过[CopyObject](https://help.aliyun.com/zh/oss/developer-reference/copyobject#reference-mvx-xxc-5db)修改Object meta信息。

## 加密方式

对于主密钥的使用，目前支持如下两种方式：
- 使用KMS托管用户主密钥 当使用KMS托管用户主密钥用于客户端数据加密时，需要将KMS用户主密钥ID（即CMK ID）传递给SDK。
- 使用用户自主管理的主密钥（RSA） 主密钥信息由用户提供，需要用户将主密钥的公钥、私钥信息作为参数传递给SDK。

使用以上两种加密方式能够有效地避免数据泄漏，保护客户端数据安全。即使数据泄漏，其他人也无法解密得到原始数据。

## 加密元数据
| 参数 | 描述 | 是否必需|
| x-oss-meta-client-side-encryption-key | 加密后的密钥。经过主密钥加密后再经过base64编码的字符串。 | 是|
| x-oss-meta-client-side-encryption-start | 随机产生的加密数据的初始值。经过主密钥加密后再经过base64编码的字符串。 | 是|
| x-oss-meta-client-side-encryption-cek-alg | 数据的加密算法。 | 是|
| x-oss-meta-client-side-encryption-wrap-alg | 数据密钥的加密算法。 | 是|
| x-oss-meta-client-side-encryption-matdesc | 主密钥的描述信息。JSON格式。
警告 
强烈建议为每个主密钥都配置描述信息，并保存好主密钥和描述信息之间的对应关系。否则不支持更换主密钥进行加密。 | 否|
| x-oss-meta-client-side-encryption-unencrypted-content-length | 加密前的数据长度。如未指定content-length则不生成该参数。 | 否|
| x-oss-meta-client-side-encryption-unencrypted-content-md5 | 加密前数据的MD5。如未指定MD5，则不生成该参数。 | 否|
| x-oss-meta-client-side-encryption-data-size | 若加密Multipart文件需要在init_multipart时传入整个大文件的总大小。 | 是（分片上传）|
| x-oss-meta-client-side-encryption-part-size | 若加密Multipart文件需要在init_multipart时传入分片大小。
说明 
目前分片大小必须是16的整数倍。 | 是（分片上传）|

以下提供了如何使用用户自主管理的主密钥（RSA）方式从内存中上传文件、上传本地文件、断点续传上传、分片上传、下载到本地文件等场景的完整示例代码。

## 从内存中上传文件

以下代码用于使用主密钥RSA加密内存中上传的文件：

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
    /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
    
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);
    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);
    std::shared_ptr content = std::make_shared();
    *content 
## 上传本地文件

以下代码用于使用主密钥RSA加密本地上传的文件：

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
    /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
    
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);
    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);
    /* 上传文件。*/
    auto outcome = client.PutObject(BucketName, ObjectName, "yourLocalFilename");
    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 断点续传上传

以下代码用于使用主密钥RSA加密断点续传上传的文件：

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
    /* 填写Object的完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。*/
    std::string UploadFilePath = "D:\\localpath\\examplefile.txt";
    /* 记录本地分片上传结果的文件。上传过程中的进度信息会保存在该文件中，如果某一分片上传失败，再次上传时会根据文件中记录的点继续上传。上传完成后，该文件会被删除。*/
    /* 如果未设置该值，默认与待上传的本地文件同路径。*/
    std::string CheckpointFilePath = "yourCheckpointFilepath"

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk(); 
  
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);
    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);

    /* 断点续传上传。*/
    UploadObjectRequest request(BucketName, ObjectName, UploadFilePath, CheckpointFilePath);
    auto outcome = client.ResumableUploadObject(request);

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 
## 分片上传

以下代码用于使用主密钥RSA加密分片上传的文件：

```
#include 
#include 
using namespace AlibabaCloud::OSS;

static int64_t getFileSize(const std::string& file)
{
    std::fstream f(file, std::ios::in | std::ios::binary);
    f.seekg(0, f.end);
    int64_t size = f.tellg();
    f.close();
    return size;
}

int main(void)
{
    /* 初始化OSS账号信息。*/
    
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写Object的完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    std::string fileToUpload = "yourLocalFilename";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
    
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);
    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);

    /* 初始化分片加密上下文。*/
    /* 需要16字节对齐。*/
    int64_t partSize = 100 * 1024;
    auto fileSize = getFileSize(fileToUpload);
    MultipartUploadCryptoContext cryptoCtx;
    cryptoCtx.setPartSize(partSize);
    cryptoCtx.setDataSize(fileSize);

    /* 初始化分片上传事件。*/
    InitiateMultipartUploadRequest initUploadRequest(BucketName, ObjectName);
    auto uploadIdResult = client.InitiateMultipartUpload(initUploadRequest, cryptoCtx);
    auto uploadId = uploadIdResult.result().UploadId();
    PartList partETagList;
    int partCount = static_cast (fileSize / partSize);
    /* 计算分片个数。*/
    if (fileSize % partSize != 0)  {
        partCount++;
    }
    /* 对每一个分片进行上传。*/
    for (int i = 1; i  content = std::make_shared(fileToUpload, std::ios::in|std::ios::binary);
        content->seekg(skipBytes, std::ios::beg);
        UploadPartRequest uploadPartRequest(BucketName, ObjectName, content);
        uploadPartRequest.setContentLength(size);
        uploadPartRequest.setUploadId(uploadId);
        uploadPartRequest.setPartNumber(i);
        auto uploadPartOutcome = client.UploadPart(uploadPartRequest, cryptoCtx);
        if (uploadPartOutcome.isSuccess()) {
            Part part(i, uploadPartOutcome.result().ETag());
            partETagList.push_back(part);
        }
        else {
            std::cout 
## 下载到本地文件

以下代码用于使用主密钥RSA解密下载到本地的文件：

```
#include 
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
    /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 下载Object到本地文件examplefile.txt，并保存到指定的本地路径中（D:\\localpath）。如果指定的本地文件存在会覆盖，不存在则新建。*/
    /* 如果未指定本地路径，则下载后的文件默认保存到示例程序所属项目对应本地路径中。*/
    std::string FileNametoSave = "D:\\localpath\\examplefile.txt";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
  
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);

    /* 如果需要解密不同主密钥加密的内容, 需要传对应的密钥信息。*/
    //std::string RSAPublicKey2 =  "your rsa public key";
    //std::string RSAPrivateKey2 = "your rsa private key";
    //std::map desc2;
    //desc2["comment"] = "your comment";
    //materials.addEncryptionMaterial(RSAPublicKey2, RSAPrivateKey2, desc2);

    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);

    /* 获取文件到本地文件。*/
    GetObjectRequest request(BucketName, ObjectName);
    request.setResponseStreamFactory([=]() {return std::make_shared(FileNametoSave, std::ios_base::out | std::ios_base::in | std::ios_base::trunc| std::ios_base::binary); });
    auto outcome = client.GetObject(request);
    if (outcome.isSuccess()) {    
        std::cout 
## 下载到本地内存

以下代码用于使用主密钥RSA解密下载到本地内存的文件：

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
    /* 填写不包含Bucket名称在内的Object的完整路径，例如desrfolder/exampleobject.txt。*/
    std::string ObjectName = "yourObjectName";
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
    
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);

    /* 如果需要解密不同主密钥加密的内容, 需要传对应的密钥信息。*/
    //std::string RSAPublicKey2 =  "your rsa public key";
    //std::string RSAPrivateKey2 = "your rsa private key";
    //std::map desc2;
    //desc2["comment"] = "your comment";
    //materials.addEncryptionMaterial(RSAPublicKey2, RSAPrivateKey2, desc2);

    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);

    /* 获取文件到本地内存。*/
    GetObjectRequest request(BucketName, ObjectName);
    auto outcome = client.GetObject(request);
    if (outcome.isSuccess()) {    
      std::cout > content;
        std::cout 
## 范围下载

以下代码用于使用主密钥RSA解密范围下载的文件：

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
    /* 填写不包含Bucket名称在内的Object的完整路径，例如desrfolder/exampleobject.txt。*/
    std::string ObjectName = "yourObjectName";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
    
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);

    /* 如果需要解密不同主密钥加密的内容, 需要传对应的密钥信息。*/
    //std::string RSAPublicKey2 =  "your rsa public key";
    //std::string RSAPrivateKey2 = "your rsa private key";
    //std::map desc2;
    //desc2["comment"] = "your comment";
    //materials.addEncryptionMaterial(RSAPublicKey2, RSAPrivateKey2, desc2);

    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);

    /* 设置下载范围。*/
    GetObjectRequest request(BucketName,  ObjectName);
    request.setRange(0, 1);
    auto outcome = client.GetObject(request);
    if (!outcome.isSuccess ()) {    
        /* 异常处理。*/
        std::cout 
## 断点续传下载

以下代码用于使用主密钥RSA解密断点续传下载的文件：

```
#include 
using namespace AlibabaCloud::OSS;

int main(void)
{
    /* 初始化OSS账号信息 */
    
    /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/
    std::string Endpoint = "yourEndpoint";
    /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/
    std::string Region = "yourRegion";
    /* 填写Bucket名称，例如examplebucket。*/
    std::string BucketName = "examplebucket";
    /* 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/
    std::string ObjectName = "exampledir/exampleobject.txt";
    /* 下载Object到本地文件examplefile.txt，并保存到指定的本地路径中（D:\\localpath）。如果指定的本地文件存在会覆盖，不存在则新建。*/
    /* 如果未指定本地路径，则下载后的文件默认保存到示例程序所属项目对应本地路径中。*/
    std::string DownloadFilePath = "D:\\localpath\\examplefile.txt";
    /* 设置断点记录文件的完整路径，例如D:\\localpath\\examplefile.txt.dcp。*/
    /* 只有当Object下载中断产生了断点记录文件后，如果需要继续下载该Object，才需要设置对应的断点记录文件。下载完成后，该文件会被删除。*/
    std::string CheckpointFilePath = "D:\\localpath\\examplefile.txt.dcp";

    /* 主密钥及描述信息。*/
    std::string RSAPublicKey = "your rsa public key";
    std::string RSAPrivateKey = "your rsa private key";
    std::map desc;
    desc["comment"] = "your comment";

    /* 初始化网络等资源。*/
    InitializeSdk();
  
    ClientConfiguration conf;
    conf.signatureVersion = SignatureVersionType::V4;
    /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/
    auto credentialsProvider = std::make_shared();
    OssClient client(Endpoint, credentialsProvider, conf);
    client.SetRegion(Region);
  
    CryptoConfiguration cryptoConf;
    auto materials = std::make_shared(RSAPublicKey, RSAPrivateKey, desc);

    /* 如果需要解密不同主密钥加密的内容, 需要传对应的密钥信息。*/
    //std::string RSAPublicKey2 =  "your rsa public key";
    //std::string RSAPrivateKey2 = "your rsa private key";
    //std::map desc2;
    //desc2["comment"] = "your comment";
    //materials.addEncryptionMaterial(RSAPublicKey2, RSAPrivateKey2, desc2);

    OssEncryptionClient client(Endpoint, credentialsProvider, conf, materials, cryptoConf);

    /* 断点续传下载。*/
    DownloadObjectRequest request(BucketName, ObjectName, DownloadFilePath, CheckpointFilePath);
    auto outcome = client.ResumableDownloadObject(request);

    if (!outcome.isSuccess()) {
        /* 异常处理。*/
        std::cout 

[上一篇：服务端加密（C++ SDK）](/zh/oss/developer-reference/server-side-encryption-1)[下一篇：数据校验（C++ SDK）](/zh/oss/developer-reference/data-verification-1)该文章对您有帮助吗？反馈
  
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