# Rails应用使用Ruby SDK上传下载及列举文件

Source: https://help.aliyun.com/zh/oss/developer-reference/use-oss-sdk-for-ruby-in-rails-applications

---

- Rails应用使用Ruby SDK上传下载及列举文件-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# Rails应用（Ruby SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
本文主要介绍如何在Rails应用中使用OSS Ruby SDK来列举存储空间（Bucket）、上传文件（Object）、下载文件等。

## 准备工作

在Rails应用中使用OSS Ruby SDK，需要在`Gemfile`中添加以下依赖。

```
gem 'aliyun-sdk', '~> 0.3.0
            
```

然后在使用OSS时引入以下依赖。

```
require 'aliyun/oss'
            
```

## 与Rails集成

OSS Ruby SDK与Rails集成的流程如下。
- 创建项目 安装Rails，然后创建一个名为oss-manager的Rails应用。 
```
gem install rails
rails new oss-manager
                            
```
说明 本示例中的oss-manager是OSS的文件管理器，包含列举所有Bucket、按目录层级列举Bucket下所有文件、上传文件和下载文件等功能。
- 使用Git管理项目代码。 
```
cd oss-manager
git init
git add .
git commit -m "init project"
                            
```
- 添加SDK依赖 编辑`oss-manager/Gemfile`，并加入SDK的依赖。 
```
gem 'aliyun-sdk', '~> 0.3.0'
                            
```
- 在`oss-manager/`中执行`bundle install`。
- 保存更改。 
```
git add .
git commit -m "add aliyun-sdk dependency"
                            
```

## 初始化OSS Client

为了避免在项目中用到OSS Client时都需要初始化，建议在项目中添加一个初始化文件。

```
# oss-manager/config/initializers/aliyun_oss_init.rb
require 'aliyun/oss'

module OSS
  def self.client
    unless @client
      Aliyun::Common::Logging.set_log_file('./log/oss_sdk.log')

      @client = Aliyun::OSS::Client.new(
        endpoint:
          Rails.application.secrets.aliyun_oss['endpoint'],
        access_key_id:
          Rails.application.secrets.aliyun_oss['access_key_id'],
        access_key_secret:
          Rails.application.secrets.aliyun_oss['access_key_secret']
      )
    end

    @client
  end
end            
```

以上代码可以在SDK的rails/目录下找到。初始化后，可以在项目中方便地使用OSS Client。

```
buckets = OSS.client.list_buckets            
```

其中endpoint、access_key_id和access_key_secret都保存在`oss-manager/conf/secrets.yml`中。

```
development:
  secret_key_base: xxxx
  aliyun_oss:
    endpoint: xxxx
    access_key_id: aaaa
    access_key_secret: bbbb           
```

保存更改。

```
git add .
git commit -m "add aliyun-sdk initializer"            
```

## 列举所有的Bucket

您可以按照如下步骤列举所有的Bucket。
- 用Rails生成管理Bucket的controller。 
```
rails g controller buckets index
                    
```
- 在`oss-manager`中生成以下文件。 app/controller/buckets_controller.rb Buckets相关的逻辑代码
- app/views/buckets/index.html.erb Buckets相关的展示代码
- app/helpers/buckets_helper.rb辅助函数
- 编辑buckets_controller.rb，调用OSS Client将`list_buckets`的结果存放在`@buckets`变量中。 
```
class BucketsController 
## 按目录层级列举Bucket下的所有文件

按目录层级列举Bucket下的所有文件的步骤如下。
- 生成一个管理Object的controller。 
```
rails g controller objects index
                    
```
- 编辑app/controllers/objects_controller.rb。 
```
class ObjectsController  @prefix, :delimiter => '/')
  end
end
                    
```
您可以从URL的参数中获取Bucket名字。您需要添加一个前缀来实现只按目录层级列出Object，然后调用OSS Client的list_objects接口获取文件列表。 说明 这里获取的是指定前缀下并且以正斜线（/）为分界的文件。具体操作，请参见[管理文件](https://help.aliyun.com/zh/oss/developer-reference/overview-33#concept-32119-zh)。
- 编辑app/views/objects/index.html.erb。 
```

# Objects in

 

  
    Key
    Type
    Size
    LastModified
  

  
    
    Directory
    N/A
    N/A
  

  
  
    
    
    
    
    
    
    
    Directory
    N/A
    N/A
    
  
  

                    
```
将文件按目录结构显示的实现逻辑是：总是在第一个出现'../'时，指向上级目录。
- 对于Common prefix，显示为目录。
- 对于Object，显示为文件。

上面的代码中使用了`with_prefix`、`remove_prefix`等辅助函数，这些辅助函数定义在app/helpers/objects_helper.rb中。

```
module ObjectsHelper
  def with_prefix(prefix)
    "?prefix=#{prefix}"
  end

  def remove_prefix(key, prefix)
    key.sub(/^#{prefix}/, '')
  end

  def upper_dir(dir)
    dir.sub(/[^\/]+\/$/, '') if dir
  end

  def new_object_path(bucket_name, prefix = nil)
    "/buckets/#{bucket_name}/objects/new/#{with_prefix(prefix)}"
  end

  def objects_path(bucket_name, prefix = nil)
    "/buckets/#{bucket_name}/objects/#{with_prefix(prefix)}"
  end
end
                    
```
- 完成之后运行`rails s`，然后在浏览器中输入地址`http://localhost:3000/buckets/my-bucket/objects/`即可查看文件列表。
- 保存更改。 
```
git add .
git commit -m "add list objects feature"                    
```

## 下载文件

在上述显示文件列表步骤中已为每个文件添加了URL，您可以直接使用该文件URL来下载文件。

```
|                 
```

您还可以使用`bucket.object_url`为文件生成临时的URL。具体操作，请参见[下载文件](https://help.aliyun.com/zh/oss/developer-reference/overview-35#concept-32118-zh)。

## 上传文件

在Rails服务端应用中，您可以通过以下两种方式上传文件。
- 第一种上传方式与普通上传文件类似。您需要先将文件上传到Rails服务器，服务器再将文件上传到OSS。
- 第二种上传方式是使用服务器生成的表单和临时凭证将文件直接上传到OSS。 在app/controllers/objects_controller.rb中增加`#new`方法，用于生成上传表单。 
```
def new
  @bucket_name = params[:bucket_id]
  @prefix = params[:prefix]
  @bucket = OSS.client.get_bucket(@bucket_name)
  @options = {
    :prefix => @prefix,
    :redirect => 'http://localhost:3000/buckets/'
  }
end
                                
```
- 编辑app/views/objects/new.html.erb。 
```

## Upload object

  
    
      Bucket:
      
    
    
      Prefix:
      
    

    
      Select file:
      
    

    
      
        
          
        
      
    
  

                                
```
说明 `upload_form`是SDK提供的一个便于生成上传表单的辅助函数，该辅助函数存放在rails/aliyun_oss_helper.rb中。您需要将其拷贝到app/helpers/目录下，完成后运行`rails s`，然后通过访问`http://localhost:3000/buckets/my-bucket/objects/new`即可将文件上传到OSS。
- 保存更改。 
```
git add .
git commit -m "add upload object feature"                               
```

## 添加样式

您可以按照如下步骤为界面添加样式。
- 下载[bootstrap](http://getbootstrap.com/)，解压后将 `bootstrap.min.css`拷贝到`app/assets/stylesheets/`下。
- 修改`app/views/layouts/application.html.erb`，并将`yield`这一行改成。 
```
  
    
  
                        
```
- 为每个页面添加一个ID为main的``，然后修改 `app/assets/stylesheets/application.css`，并添加以下内容。 
```
body {
    text-align: center;
}

div#main {
    text-align: left;
    width: 1024px;
    margin: 0 auto;
}
                        
```

完整的demo代码请参见[OSS Rails Demo](https://github.com/aliyun/alicloud-oss-rails-demo)。

[上一篇：异常处理（Ruby SDK）](/zh/oss/developer-reference/handle-exceptions-4)[下一篇：OSS Browser.js SDK](/zh/oss/developer-reference/browser-js/)该文章对您有帮助吗？反馈
  
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