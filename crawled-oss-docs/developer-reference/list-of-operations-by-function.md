# API overview

This topic outlines the Object Storage Service (OSS) APIs. It helps you understand the core concepts and resource model of OSS and quickly find the APIs that you need. For custom development, use software development kits (SDKs) in your production environment. SDKs encapsulate complex logic, such as signing, retries, and concurrency. This topic serves as a reference for the underlying implementation of SDKs and is useful for advanced customization or for understanding the communication mechanism.


Before you begin, take note of the following:


-

API calls must comply with the [Limits](https://www.alibabacloud.com/help/en/oss/user-guide/limits#concept-pzk-crg-tdb).

-

Before you use the APIs, make sure that you understand the [billing methods](https://www.alibabacloud.com/help/en/oss/billing-overview#concept-n4t-mwg-tdb) of OSS. For more information about pricing, see [OSS Pricing](https://www.alibabacloud.com/product/oss/pricing).

## Quick start: Call your first API


This section uses the creation of a bucket (`PutBucket`) as an example to describe the complete process of making an API call.

#### 1. Preparations


Before you start, obtain the following information:


-

AccessKey: For security, all OSS API requests except for anonymous access requests must be signed for authentication. OSS uses a signature mechanism that is based on an AccessKey pair, which consists of an AccessKey ID and an AccessKey secret, to verify requests. The signature information must be included in the `Authorization` field of the HTTP request header. For more information about how to calculate a signature, see [Signature V4 (recommended)](https://www.alibabacloud.com/help/en/oss/developer-reference/recommend-to-use-signature-version-4).

-

Endpoint: API requests must be sent to the endpoint of the region where the destination bucket is located. An endpoint is the access address of an OSS service. For more information about the endpoints of different regions, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

#### 2. Construct and send a request


`bash
PUT / HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 17 Apr 2025 03:15:40 GMT
x-oss-acl: private
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration>
    <StorageClass>Standard</StorageClass>
    <DataRedundancyType>LRS</DataRedundancyType>
</CreateBucketConfiguration>
`


#### 3. Understand the response


-

Successful response: If the request is successful, the server returns a `2xx` status code. For operations that return content, the response body is in XML format.


`xml
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906
Date: Fri, 24 Feb 2017 03:15:40 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS
Location: /oss-example
`


-

Error handling: If the request fails, the server returns a `4xx` or `5xx` status code. The response body is also in XML format and contains a specific error code (`Code`) and an error message (`Message`). For more information, see [Error codes](https://www.alibabacloud.com/help/en/oss/user-guide/overview-14) to troubleshoot the issue.

## API list

### Service operations


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbuckets#reference-ahf-k4t-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listuserdataredundancytransition)


| API | Description |
| --- | --- |
| ListBuckets (GetService) | Returns all buckets that are owned by the requester. |
| ListUserDataRedundancyTransition | Lists all data redundancy transition tasks of the requester. |


### Region operations


(https://www.alibabacloud.com/help/en/oss/developer-reference/describeregions#concept-2103055)


| API | Description |
| --- | --- |
| DescribeRegions | Queries the endpoints of all supported regions or a specified region. |


### Bucket operations


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#reference-wdh-fj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucket#reference-o1j-rrw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects-v2#reference-2520881)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketinfo#reference-rwk-bwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlocation#reference-e11-qtv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketstat#reference-2205923)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initiatebucketworm#reference-2536872)


(https://www.alibabacloud.com/help/en/oss/developer-reference/abortbucketworm#reference-2536930)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completebucketworm#reference-2536956)


(https://www.alibabacloud.com/help/en/oss/developer-reference/extendbucketworm#reference-2536974)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketworm#reference-2537016)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketacl#reference-zzr-hk5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketacl#reference-hgp-psv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlifecycle#reference-xlw-dbv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlifecycle#reference-zq5-grw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlifecycle#reference-wl1-xsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckettransferacceleration#reference-2076914)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbuckettransferacceleration#reference-2076915)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketversioning#reference-w2w-nm3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketversioning#reference-fhn-kt3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjectversions#reference-n2s-xy3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketreplication#topic-2598460)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrtc#reference-2251722)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreplication#topic-2611071)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreplicationlocation#topic-2577424)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreplicationprogress#reference-1940162)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketreplication#topic-2624080)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy#reference-2424532)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicy#reference-2424982)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicystatus)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpolicy#reference-2424995)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketinventory#reference-2379014)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketinventory#reference-2379122)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketinventory#reference-2379134)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketinventory#reference-2379150)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putuserdefinedlogfieldsconfig)





(https://www.alibabacloud.com/help/en/oss/developer-reference/getuserdefinedlogfieldsconfig)





(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteuserdefinedlogfieldsconfig)





(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketwebsite#reference-hwb-yr5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketwebsite#reference-wvy-s4w-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketwebsite#reference-zrl-msw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketreferer#reference-prc-ys5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreferer#reference-bs5-rpw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckettags#concept-261782)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbuckettags#concept-261796)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebuckettags#concept-261821)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketencryption#concept-262214)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketencryption#concept-262215)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketencryption#concept-262216)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrequestpayment#reference-1340164)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketrequestpayment#reference-1340313)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketcors#reference-wtg-ttc-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketcors#reference-m2w-ywc-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketcors#reference-fjn-szc-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/options#reference-jyf-j1d-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketaccessmonitor#concept-2114625)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketaccessmonitor#concept-2114879)


(https://www.alibabacloud.com/help/en/oss/developer-reference/openmetaquery#concept-2127469)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getmetaquerystatus#concept-2127483)


(https://www.alibabacloud.com/help/en/oss/developer-reference/dometaquery#concept-2127484)


(https://www.alibabacloud.com/help/en/oss/developer-reference/closemetaquery#concept-2127481)


(https://www.alibabacloud.com/help/en/oss/developer-reference/inituserantiddosinfo#main-2278045)


(https://www.alibabacloud.com/help/en/oss/developer-reference/updateuserantiddosinfo#main-2278428)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getuserantiddosinfo#main-2278430)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initbucketantiddosinfo#main-2278431)


(https://www.alibabacloud.com/help/en/oss/developer-reference/updatebucketantiddosinfo#main-2278432)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketantiddosinfo#main-2278433)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketresourcegroup#concept-2075804)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketresourcegroup#concept-2075789)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createcnametoken#reference-2210351)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getcnametoken#reference-2210536)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putcname#reference-2210550)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listcname#reference-2213388)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletecname#reference-2213407)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putstyle#main-2277102)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getstyle#main-2277728)


(https://www.alibabacloud.com/help/en/oss/developer-reference/liststyle#main-2277730)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletestyle#main-2277731)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckethttpsconfig)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbuckethttpsconfig)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createbucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listuserdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createaccesspoint#main-2355594)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspoint#main-2355616)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspoint#main-2355705)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listaccesspoints#main-2355706)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpolicy#main-2355809)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointpolicy#main-2355906)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointpolicy#main-2355926)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createaccesspointforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listaccesspointsforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointconfigforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointconfigforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpolicyforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointpolicyforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointpolicyforobjectprocess)


(https://www.alibabacloud.com/help/en/oss/developer-reference/write-get-object-response)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletepublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketarchivedirectread#main-2356189)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketarchivedirectread#main-2356191)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketdataaccelerator)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketdataaccelerator)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketdataaccelerator)


| Classification | API | Description |
| --- | --- | --- |
| Basic operations | PutBucket | Creates a bucket. |
| DeleteBucket | Deletes a bucket. |
| ListObjects (GetBucket) | Lists information about all objects in a bucket. |
| ListObjectsV2 (GetBucketV2) |
| GetBucketInfo | Queries bucket information. |
| GetBucketLocation | Queries the location of a bucket. |
| GetBucketStat | Queries the storage usage and the number of objects in a bucket. |
| Retention policy | InitiateBucketWorm | Creates a retention policy. |
| AbortBucketWorm | Deletes an unlocked retention policy. |
| CompleteBucketWorm | Locks a retention policy. |
| ExtendBucketWorm | Extends the retention period of objects in a bucket for which a retention policy is locked. |
| GetBucketWorm | Queries the retention policy of a bucket. |
| Access control | PutBucketAcl | Sets the access permissions of a bucket. |
| GetBucketAcl | Queries the access permissions of a bucket. |
| Lifecycle | PutBucketLifecycle | Sets lifecycle rules for objects in a bucket. |
| GetBucketLifecycle | Queries the lifecycle rules for objects in a bucket. |
| DeleteBucketLifecycle | Deletes the lifecycle rules for objects in a bucket. |
| Transfer acceleration | PutBucketTransferAcceleration | Configures transfer acceleration for a bucket. |
| GetBucketTransferAcceleration | Queries the transfer acceleration configuration of a bucket. |
| Versioning | PutBucketVersioning | Sets the versioning state of a bucket. |
| GetBucketVersioning | Queries the versioning state of a bucket. |
| ListObjectVersions (GetBucketVersions) | Lists the versions of all objects in a bucket. |
| Cross-region replication | PutBucketReplication | Sets data replication rules for a bucket. |
| PutBucketRTC | Enables or disables replication time control (RTC) for existing cross-region replication rules. |
| GetBucketReplication | Queries the data replication rules that are set for a bucket. |
| GetBucketReplicationLocation | Queries the destination regions to which data can be replicated. |
| GetBucketReplicationProgress | Queries the data replication progress of a bucket. |
| DeleteBucketReplication | Stops data replication tasks and deletes the replication configuration of a bucket. |
| Authorization policy | PutBucketPolicy | Sets a bucket policy. |
| GetBucketPolicy | Queries a bucket policy. |
| GetBucketPolicyStatus | Checks whether the current bucket policy allows public access. |
| DeleteBucketPolicy | Deletes a bucket policy. |
| Inventory | PutBucketInventory | Sets an inventory rule for a bucket. |
| GetBucketInventory | Queries a specified inventory task in a bucket. |
| ListBucketInventory | Queries all inventory tasks in a bucket. |
| DeleteBucketInventory | Deletes a specified inventory task from a bucket. |
| Log Management | PutBucketLogging | Enables the access log recording feature for a bucket. |
| GetBucketLogging | Queries the access log configuration of a bucket. |
| DeleteBucketLogging | Disables the access log recording feature for a bucket. |
| PutUserDefinedLogFieldsConfig | Configures the user_defined_log_fields field in the real-time logs of a bucket. |
| GetUserDefinedLogFieldsConfig | Queries the configuration of the user_defined_log_fields field in the real-time logs of a bucket. |
| DeleteUserDefinedLogFieldsConfig | Deletes the configuration of the user_defined_log_fields field in the real-time logs of a bucket. |
| Static website | PutBucketWebsite | Sets a bucket to the static website hosting mode. |
| GetBucketWebsite | Queries the static website hosting status of a bucket. |
| DeleteBucketWebsite | Disables the static website hosting mode for a bucket. |
| Hotlink protection | PutBucketReferer | Sets a hotlink protection rule for a bucket. |
| GetBucketReferer | Queries the hotlink protection rule of a bucket. |
| Tags | PutBucketTags | Adds or modifies bucket tags. |
| GetBucketTags | Queries bucket tags. |
| DeleteBucketTags | Deletes bucket tags. |
| Encryption | PutBucketEncryption | Configures encryption rules for a bucket. |
| GetBucketEncryption | Queries the encryption rules of a bucket. |
| DeleteBucketEncryption | Deletes the encryption rules of a bucket. |
| Pay by requester | PutBucketRequestPayment | Sets a bucket to the pay-by-requester mode. |
| GetBucketRequestPayment | Queries the pay-by-requester configuration of a bucket. |
| Cross-origin resource sharing | PutBucketCors | Sets cross-origin resource sharing (CORS) rules for a specified bucket. |
| GetBucketCors | Queries the current CORS rules of a specified bucket. |
| DeleteBucketCors | Disables the CORS feature and clears all CORS rules for a specified bucket. |
| Options | Before a browser sends a cross-origin request, it sends a preflight request (OPTIONS) that carries information such as the source origin, HTTP method, and headers to OSS to determine whether to send the actual request. |
| Access tracking | PutBucketAccessMonitor | Configures the access tracking state of a bucket. |
| GetBucketAccessMonitor | Queries the access tracking state of a bucket. |
| Data Indexing | OpenMetaQuery | Enables the metadata management feature for a bucket. |
| GetMetaQueryStatus | Queries the metadata index library of a specified bucket. |
| DoMetaQuery | Queries objects that meet specified conditions and lists object information based on specified fields and sorting methods. |
| CloseMetaQuery | Disables the metadata management feature for a bucket. |
| DDoS Protection | InitUserAntiDDosInfo | Creates an Anti-DDoS for OSS instance. |
| UpdateUserAntiDDosInfo | Changes the status of an Anti-DDoS for OSS instance. |
| GetUserAntiDDosInfo | Queries information about the Anti-DDoS for OSS instances that belong to a specified account. |
| InitBucketAntiDDosInfo | Initializes protection for a bucket. |
| UpdateBucketAntiDDosInfo | Updates the protection status of a bucket. |
| ListBucketAntiDDosInfo | Queries the list of protection information for a bucket. |
| Resource group | PutBucketResourceGroup | Configures a resource group for a bucket. |
| GetBucketResourceGroup | Queries the ID of the resource group to which a bucket belongs. |
| Custom domain name | CreateCnameToken | Creates a CNAME token that is required to verify the ownership of a domain name. |
| GetCnameToken | Queries a created CNAME token. |
| PutCname | Binds a CNAME record to a bucket. |
| ListCname | Queries the list of all CNAME records that are bound to a bucket. |
| DeleteCname | Deletes a bound CNAME record. |
| Image style | PutStyle | Adds an image style. |
| GetStyle | Queries information about a specified image style in a bucket. |
| ListStyle | Queries all image styles that are created in a bucket. |
| DeleteStyle | Deletes a specified image style from a bucket. |
| Transport-layer security | PutBucketHttpsConfig | Enables or disables TLS version settings for a bucket. |
| GetBucketHttpsConfig | Queries the TLS version settings of a bucket. |
| Redundancy transition | CreateBucketDataRedundancyTransition | Creates a data redundancy transition task. |
| GetBucketDataRedundancyTransition | Queries a data redundancy transition task. |
| DeleteBucketDataRedundancyTransition | Deletes a data redundancy transition task. |
| ListUserDataRedundancyTransition | Lists all data redundancy transition tasks of the requester. |
| ListBucketDataRedundancyTransition | Lists all data redundancy transition tasks in a bucket. |
| Access point | CreateAccessPoint | Creates an access point. |
| GetAccessPoint | Queries the information about an access point. |
| DeleteAccessPoint | Deletes an access point. |
| ListAccessPoints | Queries the information about user-level or bucket-level access points. |
| PutAccessPointPolicy | Configures an access point policy. |
| GetAccessPointPolicy | Queries the configuration of an access point policy. |
| DeleteAccessPointPolicy | Deletes an access point policy. |
| Object FC access point | CreateAccessPointForObjectProcess | Creates an Object FC access point. |
| GetAccessPointForObjectProcess | Queries basic information about an Object FC access point. |
| DeleteAccessPointForObjectProcess | Deletes an Object FC access point. |
| ListAccessPointsForObjectProcess | Queries information about user-level Object FC access points. |
| PutAccessPointConfigForObjectProcess | Modifies the configuration of an Object FC access point. |
| GetAccessPointConfigForObjectProcess | Queries the configuration of an Object FC access point. |
| PutAccessPointPolicyForObjectProcess | Configures an access policy for an Object FC access point. |
| GetAccessPointPolicyForObjectProcess | Queries the access policy configuration of an Object FC access point. |
| DeleteAccessPointPolicyForObjectProcess | Deletes the access policy of an Object FC access point. |
| WriteGetObjectResponse | Customizes returned data and response headers. |
| Block Public Access | PutPublicAccessBlock | Globally enables Block Public Access for OSS. |
| GetPublicAccessBlock | Queries the global Block Public Access configuration for OSS. |
| DeletePublicAccessBlock | Deletes the global Block Public Access configuration for OSS. |
| PutBucketPublicAccessBlock | Enables Block Public Access for a bucket. |
| GetBucketPublicAccessBlock | Queries the Block Public Access configuration of a specified bucket. |
| DeleteBucketPublicAccessBlock | Deletes the Block Public Access configuration of a specified bucket. |
| PutAccessPointPublicAccessBlock | Enables Block Public Access for an access point. |
| GetAccessPointPublicAccessBlock | Queries the Block Public Access configuration of a specified access point. |
| DeleteAccessPointPublicAccessBlock | Deletes the Block Public Access configuration of a specified access point. |
| Real-time access of Archive objects | PutBucketArchiveDirectRead | Enables or disables real-time access of Archive objects. |
| GetBucketArchiveDirectRead | Queries whether real-time access of Archive objects is enabled. |
| OSS accelerator | PutBucketDataAccelerator | Creates an OSS accelerator or modifies its configuration. |
| GetBucketDataAccelerator | Queries the information about an OSS accelerator. |
| DeleteBucketDataAccelerator | Deletes an OSS accelerator. |


### Object operations


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobject#reference-ccf-rgd-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject#reference-mvx-xxc-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/appendobject#reference-fvf-xld-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/sealappendobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject#reference-iqc-mqv-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletemultipleobjects#reference-ydg-25v-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/headobject#reference-bgh-cbw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectmeta#reference-sg4-k2w-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/postobject#reference-smp-nsw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/callback#reference-zkm-311-hgb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/restoreobject#reference-mfr-5bx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/cleanrestoredobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/selectobject#reference-lz1-r1x-b2b)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createselectobjectmeta)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createdirectory#concept-2057571)


(https://www.alibabacloud.com/help/en/oss/developer-reference/rename#concept-2057575)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletedirectory#concept-2057577)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpartcopy#reference-t4b-vpx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listmultipartuploads#reference-hj2-3wx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listparts#reference-hzm-1zx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjectacl#reference-fs3-gfw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectacl#reference-lzc-24w-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putsymlink#reference-qzz-qzw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getsymlink#reference-s3d-s1x-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjecttagging#reference-185784)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjecttagging#concept-185787)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobjecttagging#reference-185788)


| Classification | API | Description |
| --- | --- | --- |
| Basic operations | PutObject | Uploads an object. |
| GetObject | Queries an object. |
| CopyObject | Copies an object. |
| AppendObject | Uploads an object using append upload. |
| SealAppendObject | Prevents data from being appended to an Appendable object. |
| DeleteObject | Deletes a single object. |
| DeleteMultipleObjects | Deletes multiple objects. |
| HeadObject | Returns only the metadata of an object, not the content of the object. |
| GetObjectMeta | Returns the basic metadata of an object, such as the ETag, size, and last modified time of the object, but does not return the content of the object. |
| PostObject | Uploads an object using an HTML form. |
| Callback | You can implement a callback by including the callback parameters in a request that you send to OSS. |
| RestoreObject | Restores an Archive Storage, Cold Archive, or Deep Cold Archive object. |
| CleanRestoredObject | Ends the restored state of an object in advance. |
| SelectObject | Executes an SQL statement on an object file and returns the execution result. |
| CreateSelectObjectMeta | Queries the total number of rows, total number of columns (for CSV files), and number of splits of an object file. |
| Folder management | CreateDirectory | Creates a folder. |
| Rename | Renames a folder or an object. |
| DeleteDirectory | Deletes a folder. |
| Multipart upload | InitiateMultipartUpload | Initiates a multipart upload event. |
| UploadPart | Uploads data in parts based on the specified object name and upload ID. |
| UploadPartCopy | Calls the UploadPartCopy operation to copy data from an existing object to upload a part by adding the x-oss-copy-source request header to an UploadPart request. |
| CompleteMultipartUpload | After all parts of a file are uploaded, you must call the CompleteMultipartUpload operation to complete the multipart upload of the file. |
| AbortMultipartUpload | Cancels a multipart upload event and deletes the uploaded parts. |
| ListMultipartUploads | Lists all multipart upload events that are in progress. In-progress multipart upload events are multipart upload events that are initiated but not completed or aborted. |
| ListParts | Lists all successfully uploaded parts that belong to a specified upload ID. |
| Access control | PutObjectACL | Modifies the access permissions of an object. |
| GetObjectACL | Queries the access permissions of an object. |
| Symbolic link | PutSymlink | Creates a symbolic link. |
| GetSymlink | Queries a symbolic link. |
| Tagging | PutObjectTagging | Sets or updates object tags. |
| GetObjectTagging | Queries object tags. |
| DeleteObjectTagging | Deletes specified object tags. |


### Vector bucket operations


| Classification | API | Description |
| --- | --- | --- |
| Vector bucket | PutVectorBucket | Creates a vector bucket. |
| GetVectorBucket | Queries the details of a vector bucket. |
| ListVectorBuckets | Lists all vector buckets that belong to the current account. |
| DeleteVectorBucket | Deletes a vector bucket. |
| Index | PutVectorIndex | Creates a vector index in a vector bucket. |
| GetVectorIndex | Queries the details of a vector index. |
| ListVectorIndexes | Lists all vector indexes in a vector bucket. |
| DeleteVectorIndex | After you upload all data parts, you must call the CompleteMultipartUpload API to complete the multipart upload. |
| Vectors | PutVectors | Writes vector data to an index. |
| GetVectors | Queries specified vector data. |
| ListVectors | Lists all vector data in a vector index. |
| DeleteVectors | Deletes specified vector data from a vector index. |
| QueryVectors | Performs a vector similarity search. |


### Resource group QoS operations


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/api-delete-bucket-qos-info)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrequesterqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketrequesterqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketrequesterqosinfos)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketrequesterqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listresourcepools)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getresourcepoolinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listresourcepoolbuckets)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putresourcepoolrequesterqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getresourcepoolrequesterqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listresourcepoolrequesterqosinfos)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteresourcepoolrequesterqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketresourcepoolbucketgroup)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listresourcepoolbucketgroups)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putresourcepoolbucketgroupqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getresourcepoolbucketgroupqosinfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listresourcepoolbucketgroupqosinfos)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteresourcepoolbucketgroupqosinfo)


| API | Description |
| --- | --- |
| PutBucketQoSInfo | Sets throttling for a bucket in a resource pool. |
| GetBucketQoSInfo | Queries the throttling configuration of a bucket in a resource pool. |
| DeleteBucketQosInfo | Deletes the throttling configuration of a specified bucket in a resource pool. |
| PutBucketRequesterQoSInfo | Sets bucket-level throttling for a requester. |
| GetBucketRequesterQoSInfo | Queries the bucket-level throttling configuration for a specified requester. |
| ListBucketRequesterQoSInfos | Queries the bucket-level throttling configurations for all requesters. |
| DeleteBucketRequesterQoSInfo | Deletes the throttling configuration of a requester for a bucket. |
| ListResourcePools | Queries information about all resource pools that belong to the current account. |
| GetResourcePoolInfo | Queries the throttling configuration of a specified resource pool. |
| ListResourcePoolBuckets | Queries the list of buckets that are included in a specified resource pool. |
| PutResourcePoolRequesterQoSInfo | Configures throttling for a requester of a resource pool. |
| GetResourcePoolRequesterQoSInfo | Queries the throttling configuration of a specified requester for a resource pool. |
| ListResourcePoolRequesterQoSInfos | Queries the throttling configurations of all requesters for a resource pool. |
| DeleteResourcePoolRequesterQoSInfo | Deletes the throttling configuration of a specified requester for a resource pool. |
| PutBucketResourcePoolBucketGroup | Adds a bucket in a resource pool to a bucket group. |
| ListResourcePoolBucketGroups | Lists the bucket groups in a specified resource pool. |
| PutResourcePoolBucketGroupQoSInfo | Configures or modifies the throttling settings for a bucket group in a resource pool. |
| GetResourcePoolBucketGroupQoSInfo | Queries the throttling configuration of a bucket group in a resource pool. |
| ListResourcePoolBucketGroupQoSInfos | Lists the throttling configurations of bucket groups in a resource pool. |
| DeleteResourcePoolBucketGroupQoSInfo | Deletes the throttling configuration of a bucket group in a resource pool. |


### LiveChannel operations


(https://www.alibabacloud.com/help/en/oss/developer-reference/putlivechannelstatus#reference-r5k-kcd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putlivechannel#reference-d34-zcd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvodplaylist#concept-rqq-gw2-cgb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/postvodplaylist#reference-ry3-fhd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getlivechannelstat#reference-ov4-n3d-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getlivechannelinfo#reference-ekp-dkd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getlivechannelhistory#reference-kjz-yld-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listlivechannel#reference-idb-smd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletelivechannel#reference-d4g-k12-xdb)


| API | Description |
| --- | --- |
| PutLiveChannelStatus | Switches the status of a LiveChannel. |
| PutLiveChannel | Creates a LiveChannel. |
| GetVodPlaylist | Queries a playlist. |
| PostVodPlaylist | Generates a playlist. |
| GetLiveChannelStat | Queries the stream ingest status of a LiveChannel. |
| GetLiveChannelInfo | Queries the configuration of a LiveChannel. |
| GetLiveChannelHistory | Queries the stream ingest records of a LiveChannel. |
| ListLiveChannel | Lists LiveChannels. |
| DeleteLiveChannel | Deletes a LiveChannel. |


## Appendix


-

[Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers)

-

[Error codes](https://www.alibabacloud.com/help/en/oss/user-guide/overview-14)

-

[Service operations](https://www.alibabacloud.com/help/en/oss/developer-reference/service-operations/)

-

[Region operations](https://www.alibabacloud.com/help/en/oss/developer-reference/region-operations/)

-

[Bucket operations](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-operations/)

-

[Object operations](https://www.alibabacloud.com/help/en/oss/developer-reference/object-operations/)

-

[Vector bucket operations](https://www.alibabacloud.com/help/en/oss/developer-reference/apis-for-operations-on-vector-buckets/)

-

[Resource group QoS operations](https://www.alibabacloud.com/help/en/oss/developer-reference/resource-pool-qos-operations/)

-

[LiveChannel operations](https://www.alibabacloud.com/help/en/oss/developer-reference/livechannel-related-operations)


Thank you! We've received your  feedback.