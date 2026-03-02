# 使用Android SDK分片上传大文件实现断点续传

Source: https://help.aliyun.com/zh/oss/developer-reference/multipart-upload-6

---

- 使用Android SDK分片上传大文件实现断点续传-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 分片上传（Android SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
OSS提供的分片上传（Multipart Upload）功能，将要上传的较大文件（Object）分成多个分片（Part）来分别上传，上传完成后再调用CompleteMultipartUpload接口将这些Part组合成一个Object来达到断点续传的效果。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

## 分片上传流程

分片上传（Multipart Upload）分为以下三个步骤：
- 初始化一个分片上传事件。 调用oss.initMultipartUpload方法返回OSS创建的全局唯一的uploadId。
- 上传分片。 调用oss.uploadPart方法上传分片数据。说明 对于同一个uploadId，分片号（PartNumber）标识了该分片在整个文件内的相对位置。如果使用同一个分片号上传了新的数据，则OSS上该分片已有的数据将会被覆盖。
- OSS将收到的分片数据的MD5值放在ETag头内返回给用户。
- OSS计算上传数据的[MD5](https://help.aliyun.com/zh/oss/user-guide/can-i-use-etag-values-as-oss-md5-hashes-to-check-data-consistency)值，并与SDK计算的MD5值比较，如果不一致则返回InvalidDigest错误码。
- 完成分片上传。 所有分片上传完成后，调用oss.CompleteMultipartUpload方法将所有Part合并成完整的文件。

## 分片上传完整示例

以下通过一个完整的示例对分片上传的流程进行逐步解析：

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写本地文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";

// 初始化分片上传。
InitiateMultipartUploadRequest init = new InitiateMultipartUploadRequest(bucketName, objectName);
InitiateMultipartUploadResult initResult = oss.initMultipartUpload(init);
// 返回uploadId。
String uploadId = initResult.getUploadId();
// 根据uploadId执行取消分片上传事件或者列举已上传分片的操作。
// 如果您需要根据您需要uploadId执行取消分片上传事件的操作，您需要在调用InitiateMultipartUpload完成初始化分片之后获取uploadId。 
// 如果您需要根据您需要uploadId执行列举已上传分片的操作，您需要在调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前获取uploadId。
// Log.d("uploadId", uploadId);

// 设置单个Part的大小，单位为字节。分片最小值为100 KB，最大值为5 GB。最后一个分片的大小允许小于100 KB。
int partCount = 100 * 1024;
// 分片上传。
List partETags = new ArrayList<>();
for (int i = 1; i () {
    @Override
    public int compare(PartETag lhs, PartETag rhs) {
        if (lhs.getPartNumber()  rhs.getPartNumber()) {
            return 1;
        } else {
            return 0;
        }
    }
});

// 完成分片上传。
CompleteMultipartUploadRequest complete = new CompleteMultipartUploadRequest(bucketName, objectName, uploadId, partETags);

// 上传回调。完成分片上传请求时可以设置CALLBACK_SERVER参数，请求完成后会向指定的Server Address发送回调请求。可通过返回结果的completeResult.getServerCallbackReturnBody()查看servercallback结果。
complete.setCallbackParam(new HashMap() {
    {
        put("callbackUrl", CALLBACK_SERVER); //修改为您的服务器地址。
        put("callbackBody", "test");
    }
});
CompleteMultipartUploadResult completeResult = oss.completeMultipartUpload(complete);
OSSLog.logError("-------------- serverCallback: " + completeResult.getServerCallbackReturnBody());
```

上述代码调用uploadPart来上传每一个Part。
- 每一个分片上传请求均需指定uploadId和PartNumber。PartNumber的范围是1~10000。如果超出该范围，OSS将返回InvalidArgument的错误码。
- uploadPart要求除最后一个Part外，其他的Part大小都要大于100 KB。uploadPart仅在完成分片上传时校验Part的大小。
- 每次上传Part时都要将流定位至此次上传片开头所对应的位置。
- 每次上传Part之后，OSS的返回结果会包含一个Part的ETag值，ETag值为Part数据的MD5值，您需要将ETag值和块编号组合成PartEtag并保存，用于后续完成分片上传。

## 本地文件分片上传

您可以通过同步方式或者异步方式分片上传本地文件到OSS。
说明 
分片上传完整示例是按照分片上传流程逐步实现的完整代码，本地文件分片上传的代码是将分片上传完整示例中的代码进行了封装，您只需要使用MultipartUploadRequest即可实现分片上传。
- 调用同步接口分片上传本地文件以下代码用于以同步方式分片上传examplefile.txt文件到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件。
```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写本地文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";

ObjectMetadata meta = new ObjectMetadata();
// 设置文件元数据等。
meta.setHeader("x-oss-object-acl", "public-read-write");
MultipartUploadRequest rq = new MultipartUploadRequest(bucketName, objectName, localFilepath, meta);
// 设置PartSize。PartSize默认值为256 KB，最小值为100 KB。
rq.setPartSize(1024 * 1024);
rq.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(MultipartUploadRequest request, long currentSize, long totalSize) {
        OSSLog.logDebug("[testMultipartUpload] - " + currentSize + " " + totalSize, false);
    }
});

CompleteMultipartUploadResult result = oss.multipartUpload(rq);
```
对于Android10及之后版本的分区存储，您可以使用文件的Uri上传文件到OSS。
```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";

ObjectMetadata meta = new ObjectMetadata();
// 设置文件元数据等。
meta.setHeader("x-oss-object-acl", "public-read-write");
MultipartUploadRequest rq = new MultipartUploadRequest(bucketName, objectName, fileUri, meta);
// 设置PartSize。PartSize默认值为256 KB，最小值为100 KB。
rq.setPartSize(1024 * 1024);
rq.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(MultipartUploadRequest request, long currentSize, long totalSize) {
        OSSLog.logDebug("[testMultipartUpload] - " + currentSize + " " + totalSize, false);
    }
});

CompleteMultipartUploadResult result = oss.multipartUpload(rq);
```
- 调用异步接口分片上传本地文件以下代码用于以异步方式分片上传examplefile.txt文件到目标存储空间examplebucket中exampledir目录下的exampleobject.txt文件。
```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写本地文件完整路径，例如/storage/emulated/0/oss/examplefile.txt。
String localFilepath = "/storage/emulated/0/oss/examplefile.txt";

MultipartUploadRequest request = new MultipartUploadRequest(bucketName, objectName, localFilepath);

request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(MultipartUploadRequest request, long currentSize, long totalSize) {
        OSSLog.logDebug("[testMultipartUpload] - " + currentSize + " " + totalSize, false);
    }
});

OSSAsyncTask task = oss.asyncMultipartUpload(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(MultipartUploadRequest request, CompleteMultipartUploadResult result) {
        OSSLog.logInfo(result.getServerCallbackReturnBody());
    }

    @Override
    public void onFailure(MultipartUploadRequest request, ClientException clientException, ServiceException serviceException) {
        OSSLog.logError(serviceException.getRawMessage());
    }
});

//Thread.sleep(100);
// 取消分片上传。
//task.cancel();   

task.waitUntilFinished();
```
对于Android10及之后版本的分区存储，您可以使用文件的Uri上传文件到OSS。
```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";

MultipartUploadRequest request = new MultipartUploadRequest(bucketName, objectName, fileUri);

request.setProgressCallback(new OSSProgressCallback() {
    @Override
    public void onProgress(MultipartUploadRequest request, long currentSize, long totalSize) {
        OSSLog.logDebug("[testMultipartUpload] - " + currentSize + " " + totalSize, false);
    }
});

OSSAsyncTask task = oss.asyncMultipartUpload(request, new OSSCompletedCallback() {
    @Override
    public void onSuccess(MultipartUploadRequest request, CompleteMultipartUploadResult result) {
        OSSLog.logInfo(result.getServerCallbackReturnBody());
    }

    @Override
    public void onFailure(MultipartUploadRequest request, ClientException clientException, ServiceException serviceException) {
        OSSLog.logError(serviceException.getRawMessage());
    }
});

//Thread.sleep(100);
// 取消分片上传。
//task.cancel();   

task.waitUntilFinished();
```

## 列举已上传分片

调用oss.listParts方法获取某个上传事件所有已上传的分片。

以下代码用于列举已上传分片。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后，且在调用CompleteMultipartUpload完成分片上传之前的返回结果。
String uploadId = "0004B999EF518A1FE585B0C9****";

// 列举分片。
ListPartsRequest listParts = new ListPartsRequest(bucketName, objectName, uploadId);
ListPartsResult result = oss.listParts(listParts);

List partETagList = new ArrayList();
for (PartSummary part : result.getParts()) {
    partETagList.add(new PartETag(part.getPartNumber(), part.getETag()));
}
```
重要 
默认情况下，如果存储空间中的分片上传事件的数量大于1000，则OSS仅返回1000个Multipart Upload信息，且返回结果中IsTruncated的值为false，并返回NextPartNumberMarker作为下次读取的起点。

## 取消分片上传事件

调用oss.abortMultipartUpload方法来取消分片上传事件。当一个分片上传事件被取消后，无法再使用该uploadId进行任何操作，已上传的分片数据会被删除。

以下代码用于取消分片上传事件。

```
// 填写Bucket名称，例如examplebucket。
String bucketName = "examplebucket";
// 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。
String objectName = "exampledir/exampleobject.txt";
// 填写uploadId。uploadId来源于调用InitiateMultipartUpload完成初始化分片之后的返回结果。
String uploadId = "0004B999EF518A1FE585B0C9****";

// 取消分片上传。
AbortMultipartUploadRequest abort = new AbortMultipartUploadRequest(bucketName, objectName, uploadId);
AbortMultipartUploadResult abortResult = oss.abortMultipartUpload(abort);
```

## 相关文档
- 关于分片上传的完整示例代码，请参见[GitHub示例](https://github.com/aliyun/aliyun-oss-android-sdk/blob/master/oss-android-sdk/src/androidTest/java/com/alibaba/sdk/android/MultipartUploadTest.java)。
- 分片上传的完整实现涉及三个API接口，详情如下：关于初始化分片上传事件的API接口说明，请参见[InitiateMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)。
- 关于分片上传Part的API接口说明，请参见[UploadPart](https://help.aliyun.com/zh/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)。
- 关于完成分片上传的API接口说明，请参见[CompleteMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)。
- 关于取消分片上传事件的API接口说明，请参见[AbortMultipartUpload](https://help.aliyun.com/zh/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)。
- 关于列举已上传分片的API接口说明，请参见[ListParts](https://help.aliyun.com/zh/oss/developer-reference/listparts#reference-hzm-1zx-wdb)。
- 关于列举所有执行中的分片上传事件（即已初始化但尚未完成或已取消的分片上传事件）的API接口说明，请参见[ListMultipartUploads](https://help.aliyun.com/zh/oss/developer-reference/listmultipartuploads#reference-hj2-3wx-wdb)。
- 关于初始化OSSClient，请参见[如何初始化Android端OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-1#88938d5b6cvib)。

[上一篇：追加上传（Android SDK）](/zh/oss/developer-reference/append-upload-5)[下一篇：断点续传上传（Android SDK）](/zh/oss/developer-reference/resumable-upload-4)该文章对您有帮助吗？反馈
  
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