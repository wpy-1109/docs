# 使用iOSSDK按前缀或分页等方式列举存储空间文件

Source: https://help.aliyun.com/zh/oss/developer-reference/list-objects-13

---

- 使用iOSSDK按前缀或分页等方式列举存储空间文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 列举文件（iOS SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文介绍如何列举存储空间下（Bucket）中的所有文件（Object）、指定个数的文件、指定前缀的文件等。

## 注意事项
- 使用本文示例前您需要先通过自定义域名、STS等方式新建OSSClient，具体请参见[初始化](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。说明 所创建存储空间的所属地域取决于初始化配置的endpoint地域信息。
- 要列举文件，您必须有`ossGetObject`权限。具体操作，请参见[为RAM用户授予自定义的权限策略](https://help.aliyun.com/zh/oss/user-guide/common-examples-of-ram-policies#section-ucu-jv0-zip)。

## 列举指定个数的文件

以下代码用于列举examplebucket中最多20个文件。

```
OSSGetBucketRequest * getBucket = [OSSGetBucketRequest new];
// 填写Bucket名称，例如examplebucket。
getBucket.bucketName = @"examplebucket";
// 填写返回文件的最大个数。如果不设置此参数，则默认值为100，maxkeys的取值不能大于1000。
getBucket.maxKeys = 20;

OSSTask * getBucketTask = [client getBucket:getBucket];
[getBucketTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        OSSGetBucketResult * result = task.result;
        NSLog(@"get bucket success!");
        for (NSDictionary * objectInfo in result.contents) {
            NSLog(@"list object: %@", objectInfo);
        }
    } else {
        NSLog(@"get bucket failed, error: %@", task.error);
    }
    return nil;
}];
// 实现同步阻塞等待任务完成。
// [getBucketTask waitUntilFinished];
```

## 列举指定前缀的文件

以下代码用于列举examplebucket中以file为前缀的文件。

```
OSSGetBucketRequest * getBucket = [OSSGetBucketRequest new];
// 填写Bucket名称，例如examplebucket。
getBucket.bucketName = @"examplebucket";
// 填写前缀。
getBucket.prefix = @"file";

OSSTask * getBucketTask = [client getBucket:getBucket];
[getBucketTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        OSSGetBucketResult * result = task.result;
        NSLog(@"get bucket success!");
        for (NSDictionary * objectInfo in result.contents) {
            NSLog(@"list object: %@", objectInfo);
        }
    } else {
        NSLog(@"get bucket failed, error: %@", task.error);
    }
    return nil;
}];
// 实现同步阻塞等待任务完成。
// [getBucketTask waitUntilFinished]
```

## 列举指定marker之后的文件

以下代码用于列举examplebucket中exampleobject.txt之后的文件。

```
OSSGetBucketRequest * getBucket = [OSSGetBucketRequest new];
// 填写Bucket名称，例如examplebucket。
getBucket.bucketName = @"examplebucket";
// 填写marker。从marker之后按字母排序的第一个开始返回文件。
// 如果marker在存储空间中不存在，则会从符合marker字母排序的下一个开始返回文件。
getBucket.marker = @"exampleobject.txt";

OSSTask * getBucketTask = [client getBucket:getBucket];
[getBucketTask continueWithBlock:^id(OSSTask *task) {
    if (!task.error) {
        OSSGetBucketResult * result = task.result;
        NSLog(@"get bucket success!");
        for (NSDictionary * objectInfo in result.contents) {
            NSLog(@"list object: %@", objectInfo);
        }
    } else {
        NSLog(@"get bucket failed, error: %@", task.error);
    }
    return nil;
}];
// 实现同步阻塞等待任务完成。
// [getBucketTask waitUntilFinished]
```

## 分页列举

首先，声明相关的全局变量：

```
@interface ... {
    NSString *_marker;
    BOOL _isCompleted;
}
@end
```

以下代码用于在 examplebucket 中分页列举，每页最多显示 20 个文件。

```
 do {
    OSSGetBucketRequest *getBucket = [OSSGetBucketRequest new];
    getBucket.bucketName = @"examplebucket";
    getBucket.marker = _marker;  // Accessing the _marker instance variable
    getBucket.maxKeys = 20;

    OSSTask *getBucketTask = [client getBucket:getBucket];
    [getBucketTask continueWithBlock:^id(OSSTask *task) {
        if (!task.error) {
            OSSGetBucketResult *result = task.result;
            NSLog(@"Get bucket success!");
            NSLog(@"objects: %@", result.contents);
            if (result.isTruncated) {
                _marker = result.nextMarker;  // Update the _marker instance variable
                _isCompleted = NO;
            } else {
                _isCompleted = YES;
            }
        } else {
            _isCompleted = YES;
            NSLog(@"Get bucket failed, error: %@", task.error);
        }
        return nil;
    }];
    // 实现同步阻塞等待任务完成。
    [getBucketTask waitUntilFinished];
} while (!_isCompleted);
```

## 分页列举指定前缀的文件

首先，声明相关的全局变量：

```
@interface ... {
    NSString *_marker;
    BOOL _isCompleted;
}
@end
```

以下代码用于在 examplebucket 中分页列举以 file 为前缀的文件，每页最多显示 20 个文件。

```
do {
    OSSGetBucketRequest *getBucket = [OSSGetBucketRequest new];
    getBucket.bucketName = @"examplebucket";
    getBucket.marker = _marker;  // Accessing the _marker instance variable
    getBucket.maxKeys = 20;
    getBucket.prefix = @"file";

    OSSTask *getBucketTask = [client getBucket:getBucket];
    [getBucketTask continueWithBlock:^id(OSSTask *task) {
        if (!task.error) {
            OSSGetBucketResult *result = task.result;
            NSLog(@"Get bucket success!");
            NSLog(@"objects: %@", result.contents);

            if (result.isTruncated) {
                _marker = result.nextMarker;  // Update the _marker instance variable
                _isCompleted = NO;
            } else {
                _isCompleted = YES;
            }
        } else {
            _isCompleted = YES;
            NSLog(@"Get bucket failed, error: %@", task.error);
        }
        return nil;
    }];
    // 实现同步阻塞等待任务完成。
    [getBucketTask waitUntilFinished];
} while (!_isCompleted);
```

## 相关文档
- 关于列举文件的API接口说明，请参见[GetBucket (ListObjects)](https://help.aliyun.com/zh/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)。
- 关于初始化OSSClient，请参见[如何初始化OSSClient实例](https://help.aliyun.com/zh/oss/developer-reference/initialization-8#concept-32057-zh)。

[上一篇：获取文件元数据（iOS SDK）](/zh/oss/developer-reference/query-object-metadata-6)[下一篇：重命名文件（iOS SDK）](/zh/oss/developer-reference/rename-objects-1)该文章对您有帮助吗？反馈
  
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