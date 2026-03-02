# Regions and endpoints

When deploying Object Storage Service (OSS) across multiple regions, choosing the right region and endpoint is critical for performance, cost, and compliance. Understanding these factors helps you improve access performance, optimize resource allocation, and meet data compliance requirements.


A region is the physical location of an Alibaba Cloud data center. Consider the following factors when you select a region:


-

Connectivity with other Alibaba Cloud services: When your other cloud services are in the same region as OSS, they can communicate over the internal network. This setup eliminates public network traffic charges and provides a more stable, low-latency connection.

-

Cost considerations: Because product prices and discount policies vary by region, you can control costs by selecting a region with more favorable pricing. For more information, see [OSS Pricing](https://www.alibabacloud.com/product/oss/pricing).

-

Compliance requirements: Different regions and industries have different data compliance requirements. Select a region that meets the compliance requirements of your business.

-

Product features: New features are often released for public preview in specific regions. To use the latest features, you can create a bucket in a supported region. For more information about feature releases, see [Release notes](https://www.alibabacloud.com/help/en/oss/release-notes#concept-185831).

-

Geographic proximity: To minimize network latency and improve the user experience, choose the region closest to your applications and primary user base.

##### How to quickly test network latency to different regions


Use the `curl` command to quickly test the network latency from your client's location to different OSS regional endpoints. This test helps you choose a region. Lower values for `time_connect` and `time_starttransfer` usually indicate better network quality.


`shell
# Test the latency to China (Hangzhou)
curl -o /dev/null -s -w "Connect: %{time_connect}s\nStart Transfer: %{time_starttransfer}s\nTotal: %{time_total}s\n" "https://oss-cn-hangzhou.aliyuncs.com"

# Test the latency to China (Beijing)
curl -o /dev/null -s -w "Connect: %{time_connect}s\nStart Transfer: %{time_starttransfer}s\nTotal: %{time_total}s\n" "https://oss-cn-beijing.aliyuncs.com"
`


## Public cloud


The names of some regions outside the Chinese mainland may differ between the OSS pricing page and the resource plan purchase page. However, these different names refer to the same physical location. For example, the US (Silicon Valley) region may be displayed as US West 1 or US West. For more information, see [OSS Pricing](https://www.alibabacloud.com/product/oss/pricing) or [Purchase a resource plan](https://common-buy-intl.alibabacloud.com/?spm=5176.8465980.bucket-list.2.11df6765PslE4M&commodityCode=oss_bag_intl#/buy).


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Due to a [policy change](https://www.alibabacloud.com/en/notice/oss_update_notice_policy_change_in_calling_data_api_operations_via_the_default_public_domain_name_45a) to improve compliance and security, starting March 20, 2025, new OSS users must [use a custom domain name](https://www.alibabacloud.com/help/en/oss/user-guide/access-buckets-via-custom-domain-names) (CNAME) to perform data API operations on OSS buckets located in Chinese mainland regions. Default public endpoints are restricted for these operations. Refer to the [official announcement](https://www.alibabacloud.com/en/notice/oss_update_notice_policy_change_in_calling_data_api_operations_via_the_default_public_domain_name_45a) for a complete list of the affected operations. If you access your data via HTTPS, you must [bind a valid SSL Certificate](https://www.alibabacloud.com/help/en/oss/user-guide/access-oss-by-https-protocol) to your custom domain. This is mandatory for OSS Console access, as the console enforces HTTPS.


### Asia-Pacific - China


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


-


| Region | Region ID | Public endpoint | Internal endpoint | Dual-stack endpoint | Internal VIP CIDR blocks |
| --- | --- | --- | --- | --- | --- |
| China (Hangzhou) | cn-hangzhou | oss-cn-hangzhou.aliyuncs.com | oss-cn-hangzhou-internal.aliyuncs.com | cn-hangzhou.oss.aliyuncs.com | 100.118.28.0/24100.114.102.0/24100.98.170.0/24100.118.31.0/24 |
| China (Shanghai) | cn-shanghai | oss-cn-shanghai.aliyuncs.com | oss-cn-shanghai-internal.aliyuncs.com | cn-shanghai.oss.aliyuncs.com | 100.98.35.0/24100.98.110.0/24100.98.169.0/24100.118.102.0/24 |
| China (Nanjing - Local Region) (Closing Down) | cn-nanjing | oss-cn-nanjing.aliyuncs.com | oss-cn-nanjing-internal.aliyuncs.com | Not supported | 100.114.142.0/24 |
| China (Qingdao) | cn-qingdao | oss-cn-qingdao.aliyuncs.com | oss-cn-qingdao-internal.aliyuncs.com | cn-qingdao.oss.aliyuncs.com | 100.115.173.0/24100.99.113.0/24100.99.114.0/24100.99.115.0/24 |
| China (Beijing) | cn-beijing | oss-cn-beijing.aliyuncs.com | oss-cn-beijing-internal.aliyuncs.com | cn-beijing.oss.aliyuncs.com | 100.118.58.0/24100.118.167.0/24100.118.170.0/24100.118.171.0/24100.118.172.0/24100.118.173.0/24 |
| China (Zhangjiakou) | cn-zhangjiakou | oss-cn-zhangjiakou.aliyuncs.com | oss-cn-zhangjiakou-internal.aliyuncs.com | cn-zhangjiakou.oss.aliyuncs.com | 100.118.90.0/24100.98.159.0/24100.114.0.0/24100.114.1.0/24 |
| China (Hohhot) | cn-huhehaote | oss-cn-huhehaote.aliyuncs.com | oss-cn-huhehaote-internal.aliyuncs.com | cn-huhehaote.oss.aliyuncs.com | 100.118.195.0/24100.99.110.0/24100.99.111.0/24100.99.112.0/24 |
| China (Ulanqab) | cn-wulanchabu | oss-cn-wulanchabu.aliyuncs.com | oss-cn-wulanchabu-internal.aliyuncs.com | cn-wulanchabu.oss.aliyuncs.com | 100.114.11.0/24100.114.12.0/24100.114.100.0/24100.118.214.0/24 |
| China (Shenzhen) | cn-shenzhen | oss-cn-shenzhen.aliyuncs.com | oss-cn-shenzhen-internal.aliyuncs.com | cn-shenzhen.oss.aliyuncs.com | 100.118.78.0/24100.118.203.0/24100.118.204.0/24100.118.217.0/24 |
| China (Heyuan) | cn-heyuan | oss-cn-heyuan.aliyuncs.com | oss-cn-heyuan-internal.aliyuncs.com | cn-heyuan.oss.aliyuncs.com | 100.98.83.0/24100.118.174.0/24 |
| China (Guangzhou) | cn-guangzhou | oss-cn-guangzhou.aliyuncs.com | oss-cn-guangzhou-internal.aliyuncs.com | cn-guangzhou.oss.aliyuncs.com | 100.115.33.0/24100.114.101.0/24 |
| China (Chengdu) | cn-chengdu | oss-cn-chengdu.aliyuncs.com | oss-cn-chengdu-internal.aliyuncs.com | cn-chengdu.oss.aliyuncs.com | 100.115.155.0/24100.99.107.0/24100.99.108.0/24100.99.109.0/24 |
| China (Hong Kong) | cn-hongkong | oss-cn-hongkong.aliyuncs.com | oss-cn-hongkong-internal.aliyuncs.com | cn-hongkong.oss.aliyuncs.com | 100.115.61.0/24100.99.103.0/24100.99.104.0/24100.99.106.0/24 |


### Asia-Pacific - Other


-


-


-


-


-


-


-


-


-


-


| Region | Region ID | Public endpoint | Internal endpoint | Dual-stack endpoint | Internal VIP CIDR blocks |
| --- | --- | --- | --- | --- | --- |
| Japan (Tokyo) | ap-northeast-1 | oss-ap-northeast-1.aliyuncs.com | oss-ap-northeast-1-internal.aliyuncs.com | Not supported | 100.114.211.0/24100.114.114.0/25 |
| South Korea (Seoul) | ap-northeast-2 | oss-ap-northeast-2.aliyuncs.com | oss-ap-northeast-2-internal.aliyuncs.com | Not supported | 100.99.119.0/24 |
| Singapore | ap-southeast-1 | oss-ap-southeast-1.aliyuncs.com | oss-ap-southeast-1-internal.aliyuncs.com | Not supported | 100.118.219.0/24100.99.213.0/24100.99.116.0/24100.99.117.0/24 |
| Malaysia (Kuala Lumpur) | ap-southeast-3 | oss-ap-southeast-3.aliyuncs.com | oss-ap-southeast-3-internal.aliyuncs.com | Not supported | 100.118.165.0/24100.99.125.0/24100.99.130.0/24100.99.131.0/24 |
| Indonesia (Jakarta) | ap-southeast-5 | oss-ap-southeast-5.aliyuncs.com | oss-ap-southeast-5-internal.aliyuncs.com | Not supported | 100.114.98.0/24 |
| Philippines (Manila) | ap-southeast-6 | oss-ap-southeast-6.aliyuncs.com | oss-ap-southeast-6-internal.aliyuncs.com | Not supported | 100.115.16.0/24 |
| Thailand (Bangkok) | ap-southeast-7 | oss-ap-southeast-7.aliyuncs.com | oss-ap-southeast-7-internal.aliyuncs.com | Not supported | 100.98.249.0/24 |


### Europe and Americas


-


-


-


-


| Region | Region ID | Public endpoint | Internal endpoint | Dual-stack endpoint | Internal VIP CIDR blocks |
| --- | --- | --- | --- | --- | --- |
| Germany (Frankfurt) | eu-central-1 | oss-eu-central-1.aliyuncs.com | oss-eu-central-1-internal.aliyuncs.com | eu-central-1.oss.aliyuncs.com | 100.115.154.0/24 |
| UK (London) | eu-west-1 | oss-eu-west-1.aliyuncs.com | oss-eu-west-1-internal.aliyuncs.com | Not supported | 100.114.114.128/25 |
| US (Silicon Valley) | us-west-1 | oss-us-west-1.aliyuncs.com | oss-us-west-1-internal.aliyuncs.com | Not supported | 100.115.107.0/24 |
| US (Virginia) | us-east-1 | oss-us-east-1.aliyuncs.com | oss-us-east-1-internal.aliyuncs.com | Not supported | 100.115.60.0/24100.99.100.0/24100.99.101.0/24100.99.102.0/24 |
| Mexico | na-south-1 | oss-na-south-1.aliyuncs.com | oss-na-south-1-internal.aliyuncs.com | Not supported | 100.115.112.0/27 |


### Middle East


| Region | Region ID | Public endpoint | Internal endpoint | Dual-stack endpoint | Internal VIP CIDR blocks |
| --- | --- | --- | --- | --- | --- |
| UAE (Dubai) | me-east-1 | oss-me-east-1.aliyuncs.com | oss-me-east-1-internal.aliyuncs.com | Not supported | 100.99.235.0/24 |
| SAU (Riyadh - Partner Region) | me-central-1 | oss-me-central-1.aliyuncs.com | oss-me-central-1-internal.aliyuncs.com | Not supported | 100.99.121.0/24 |


Thank you! We've received your  feedback.