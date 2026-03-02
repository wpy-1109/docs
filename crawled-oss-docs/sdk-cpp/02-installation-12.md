# 多平台安装C++ SDK及编译选项说明

Source: https://help.aliyun.com/zh/oss/developer-reference/installation-12

---

- 多平台安装C++ SDK及编译选项说明-对象存储-阿里云
  
  
  
  
  
  
  
  
  
  
  

  
  

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
# 安装（C++ SDK）
更新时间：
复制 MD 格式[产品详情](https://www.aliyun.com/product/oss)[我的收藏](/my_favorites.html)
如果您需要管理OSS存储空间、上传下载文件、管理数据、进行图片处理等，可以先安装OSS C++ SDK。本文介绍如何在不同的操作系统中安装OSS C++ SDK以及编译选项的使用说明。

## 前提条件
- C++11及以上版本的编译器
- Visual Studio 2013及以上版本
- GCC 4.8及以上版本
- Clang 3.3及以上版本

## 下载SDK
- [下载SDK安装包](https://github.com/aliyun/aliyun-oss-cpp-sdk/archive/refs/tags/1.10.0.zip)
- [通过GitHub下载](https://github.com/aliyun/aliyun-oss-cpp-sdk.git)

## 安装SDK

您可以通过Linux、Windows、Android及macOS系统安装SDK。

### Linux系统
- 安装CMake并通过CMake生成目标平台的构建脚本。下载CMake安装包。以下以安装CMake 3.21.1版本为例，如需下载其他版本，请对应替换版本号。
```
wget https://cmake.org/files/v3.21/cmake-3.21.1.tar.gz
```
- 解压CMake安装包文件。
```
tar xvf cmake-3.21.1.tar.gz
```
- 进入CMake安装目录。
```
cd cmake-3.21.1/
```
- 执行自动化构建和配置过程，用于检查系统环境、生成Makefile文件、配置编译选项等。
```
./bootstrap
```
- 根据Makefile文件中的规则，逐个编译源代码文件，生成目标可执行文件或库文件。
```
make
```
- 安装编译生成的文件。
```
sudo make install
```
- 添加环境变量。编辑bash配置文件。
```
vim .bashrc
```
- 配置环境变量。
```
CMAKE_PATH=/usr/local/cmake
export PATH=$CMAKE_PATH/bin:$PATH
```
- 使bash配置文件更改生效。
```
source .bashrc
```
- 查找并显示在当前系统中可执行`cmake`命令的路径。
```
which cmake
```
- 安装依赖。
```
yum -y install libcurl-devel openssl-devel unzip
```
- 安装C++ SDK。下载C++ SDK安装包。
```
wget -O aliyun-oss-cpp-sdk-master.zip "https://github.com/aliyun/aliyun-oss-cpp-sdk/archive/refs/tags/1.10.0.zip"
```
- 解压安装包文件。
```
unzip aliyun-oss-cpp-sdk-master.zip
```
- 进入安装目录。
```
cd aliyun-oss-cpp-sdk-master
```
- 安装C++ SDK。创建用于编译和构建项目的目标目录。
```
mkdir build
```
- 切换至目标目录。
```
cd build
```
- 通过CMake工具生成项目的构建系统。
```
cmake ..
```
- 执行项目的编译过程。
```
make
```
- 将编译生成的文件安装到系统指定的目录中。
```
make install
```
- 编译示例文件。
```
g++ test.cpp -std=c++11 -fno-rtti -lalibabacloud-oss-cpp-sdk -lcurl -lcrypto -lpthread -o test.bin
```
重要 C++ SDK默认关闭rtti属性。因此使用g++编译运行时，请添加-std=c++11、-fno-rtti、-lalibabacloud-oss-cpp-sdk、-lcurl、-lcrypto和-lpthread。

### Windows系统
- 安装CMake并通过CMake生成目标平台的构建脚本。安装CMake3.1及以上版本后，打开cmd进入SDK文件目录，创建build文件夹，运行cmake ..生成所需文件，如下图所示。说明 下载的SDK中不直接提供alibabacloud-oss-cpp-sdk.sln工程文件，您需要通过cmake生成所需的工程文件。
- 如果要构建x64体系结构，可以使用命令cmake -A x64 ..来实现。
- 请以管理员身份运行VS开发人员命令提示符，在build目录文件下运行以下命令进行编译安装。 
```
msbuild ALL_BUILD.vcxproj
msbuild INSTALL.vcxproj
```
或者用Visual Studio打开alibabacloud-oss-cpp-sdk.sln生成解决方案。

### Android系统

Linux环境下，基于android-ndk-r16工具链构建工程。您需要在$ANDROID_NDK/sysroot路径下安装libcurl和libopenssl第三方库，并运行以下命令进行编译安装。

```
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake  \
      -DANDROID_NDK=$ANDROID_NDK    \
      -DANDROID_ABI=armeabi-v7a     \
      -DANDROID_TOOLCHAIN=clang     \
      -DANDROID_PLATFORM=android-21 \
      -DANDROID_STL=c++_shared ..
make
```

### macOS系统

在macOS系统中，您可以使用brew方式来安装依赖库。

在macOS系统中需要指定OpenSSL安装路径。假设OpenSSL安装在/usr/local/Cellar/openssl/1.0.2p目录中，运行以下命令进行编译安装。

```
cmake -DOPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2p  \
      -DOPENSSL_LIBRARIES=/usr/local/Cellar/openssl/1.0.2p/lib  \
      -DOPENSSL_INCLUDE_DIRS=/usr/local/Cellar/openssl/1.0.2p/include/ ..
make
```

## 编译选项

您可以根据具体的业务场景，设置不同的编译选项，编译选项格式为cmake -D${OptionName}=ON|OFF ..。

可选的编译选项请参见下表。
| 选项名称 | 描述|
| BUILD_SHARED_LIBS | 构建动态库，默认值为OFF。打开此选项时，会同时构建静态库和动态库， 且静态库名字增加-static后缀。

结合编译选项格式，如果要构建动态库，则使用cmake -DBUILD_SHARED_LIBS=ON ..。|
| ENABLE_RTTI | 支持的实时类型信息，默认值为ON。|
| OSS_DISABLE_BUCKET | 不构建Bucket相关设置接口，默认值为OFF。如果需要裁剪代码大小，可将其置为ON。|
| OSS_DISABLE_LIVECHANNEL | 不构建LiveChannel接口，默认值为OFF。如果需要裁剪代码大小，可将其置为ON。|
| OSS_DISABLE_RESUAMABLE | 不构建断点续传接口，默认值为OFF。如果需要裁剪代码大小，可将其置为ON。|
| OSS_DISABLE_ENCRYPTION | 不构建客户端加密接口，默认值为OFF。如果需要裁剪代码大小，可将其置为ON。|

[上一篇：前言（C++ SDK）](/zh/oss/developer-reference/introduction-4)[下一篇：配置访问凭证（C++ SDK）](/zh/oss/developer-reference/c-configure-access-credentials)该文章对您有帮助吗？反馈
  
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