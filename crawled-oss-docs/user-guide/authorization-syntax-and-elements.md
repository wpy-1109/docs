# OSS authorization syntax and elements

OSS uses JSON-formatted authorization policies for fine-grained access control over resources. This topic provides a quick reference for the syntax and elements of authorization policies that you can use to configure complex permissions quickly and accurately.

## Authorization syntax


OSS authorization policies use the JSON format. They include two core fields: Version and Statement.

### Syntax structure


`json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow|Deny",
            "Action": ["oss:ActionName"],
            "Principal": ["UID|*"],
            "Resource": ["acs:oss:*:*:bucket-name/*"],
            "Condition": {
                "ConditionOperator": {
                    "ConditionKey": ["Value"]
                }
            }
        }
    ]
}
`


### Field descriptions




















| Field | Description | Required |
| --- | --- | --- |
| Version | The version of the access policy. The value is fixed to 1 and cannot be changed. | Yes |
| Statement | The main body of a policy statement. It contains one or more specific allow or deny rules. | Yes |


### Statement elements









































| Element | Description | Required |
| --- | --- | --- |
| Effect | The effect of the policy. Valid values are Allow or Deny. | Yes |
| Action | The specific operation to perform on a resource. You can use the wildcard character *. | Yes |
| Principal | The entity that the policy affects, such as a user, an account, or a role. When this field is set to an empty list , the behavior is the same as when it is set to ["*"]. Note: RAM policies do not include this field. | Required for bucket policies |
| Resource | The scope of resources that the policy affects. You can use the wildcard character *. | Yes |
| Condition | The conditions for the policy to take effect. If you configure multiple conditions, all conditions must be met (an AND relationship) for the policy to take effect. | No |


## Action


Actions are categorized into service-level, bucket-level, and object-level operations based on their scope.

### Service level


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbuckets#reference-ahf-k4t-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listuserdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletepublicaccessblock)


| API | Action | API description |
| --- | --- | --- |
| ListBuckets (GetService) | oss:ListBuckets | Lists all buckets that the requester owns. |
| ListUserDataRedundancyTransition | oss:ListUserDataRedundancyTransition | Lists all storage redundancy transition tasks for the requester. |
| None | oss:ActivateProduct | Activates OSS and the Content Moderation service. |
| None | oss:CreateOrder | Creates orders for OSS resource plans. |
| PutPublicAccessBlock | oss:PutPublicAccessBlock | Enables Block Public Access for all of OSS. |
| GetPublicAccessBlock | oss:GetPublicAccessBlock | Retrieves the configuration information for the global Block Public Access setting. |
| DeletePublicAccessBlock | oss:DeletePublicAccessBlock | Deletes the configuration information for the global Block Public Access setting. |


### Bucket level


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucket#reference-wdh-fj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects#reference-iwr-xlv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketinfo#reference-rwk-bwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlocation#reference-e11-qtv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketstat)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketversioning#reference-w2w-nm3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketversioning#reference-fhn-kt3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjectversions#reference-n2s-xy3-fhb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketacl#reference-zzr-hk5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketacl#reference-hgp-psv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucket#reference-o1j-rrw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initiatebucketworm#reference-2536872)


(https://www.alibabacloud.com/help/en/oss/developer-reference/abortbucketworm#reference-2536930)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completebucketworm#reference-2536956)


(https://www.alibabacloud.com/help/en/oss/developer-reference/extendbucketworm#reference-2536974)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketworm#reference-2537016)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketwebsite#reference-hwb-yr5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketwebsite#reference-wvy-s4w-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketwebsite#reference-zrl-msw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketreferer#reference-prc-ys5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreferer#reference-bs5-rpw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlifecycle#reference-xlw-dbv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlifecycle#reference-zq5-grw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlifecycle#reference-wl1-xsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckettransferacceleration#reference-2076914)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbuckettransferacceleration#reference-2076915)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listmultipartuploads#reference-hj2-3wx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketcors#reference-wtg-ttc-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketcors#reference-m2w-ywc-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketcors#reference-fjn-szc-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy#reference-2424532)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicy#reference-2424982)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpolicy#reference-2424995)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckettags#concept-261782)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbuckettags#concept-261796)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebuckettags#concept-261821)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketencryption#concept-262214)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketencryption#concept-262215)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketencryption#concept-262216)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrequestpayment#reference-1340164)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketrequestpayment#reference-1340313)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketreplication#topic-1919274)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrtc)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreplication#topic-1919419)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketreplication#topic-1919465)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreplicationlocation#topic-1919571)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketreplicationprogress#reference-1940162)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketinventory#doc-api-Oss-PutBucketInventory)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketinventory#reference-2379122)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketinventory#reference-2379134)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketinventory#reference-2379150)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketaccessmonitor)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketaccessmonitor)


(https://www.alibabacloud.com/help/en/oss/developer-reference/openmetaquery)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getmetaquerystatus)


(https://www.alibabacloud.com/help/en/oss/developer-reference/dometaquery)


(https://www.alibabacloud.com/help/en/oss/developer-reference/closemetaquery)


(https://www.alibabacloud.com/help/en/oss/developer-reference/inituserantiddosinfo#main-2278045)


(https://www.alibabacloud.com/help/en/oss/developer-reference/updateuserantiddosinfo#main-2278428)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getuserantiddosinfo#main-2278430)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initbucketantiddosinfo#main-2278431)


(https://www.alibabacloud.com/help/en/oss/developer-reference/updatebucketantiddosinfo#main-2278432)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketantiddosinfo#main-2278433)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketresourcegroup#concept-2075804)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketresourcegroup#concept-2075789)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createcnametoken)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getcnametoken)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putcname)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listcname)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletecname)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putstyle#main-2277102)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getstyle#main-2277728)


(https://www.alibabacloud.com/help/en/oss/developer-reference/liststyle#main-2277730)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletestyle#main-2277731)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketarchivedirectread)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketarchivedirectread)


(https://www.alibabacloud.com/help/en/oss/developer-reference/createaccesspoint)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspoint)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspoint)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listaccesspoints)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpolicy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointpolicy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointpolicy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbuckethttpsconfig)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbuckethttpsconfig)


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


(https://www.alibabacloud.com/help/en/oss/developer-reference/createbucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listbucketdataredundancytransition)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointpublicaccessblock)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicystatus)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketoverwriteconfig)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketoverwriteconfig)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketoverwriteconfig)


| API | Action | API description |
| --- | --- | --- |
| PutBucket | oss:PutBucket | Creates a bucket. |
| GetBucket (ListObjects) | oss:ListObjects | Lists information about all objects in a bucket. |
| GetBucketInfo | oss:GetBucketInfo | Views information about a bucket. |
| GetBucketLocation | oss:GetBucketLocation | Views the location information of a bucket. |
| GetBucketStat | oss:GetBucketStat | Gets the storage capacity and number of files in a bucket. |
| PutBucketVersioning | oss:PutBucketVersioning | Sets the versioning state for a specified bucket. |
| GetBucketVersioning | oss:GetBucketVersioning | Gets the versioning state of a specified bucket. |
| ListObjectVersions (GetBucketVersions) | oss:ListObjectVersions | Lists version information for all objects in a bucket, including delete markers. |
| PutBucketAcl | oss:PutBucketAcl | Sets or modifies the ACL of a bucket. |
| GetBucketAcl | oss:GetBucketAcl | Gets the ACL of a bucket. |
| DeleteBucket | oss:DeleteBucket | Deletes a bucket. |
| InitiateBucketWorm | oss:InitiateBucketWorm | Creates a retention policy. |
| AbortBucketWorm | oss:AbortBucketWorm | Deletes an unlocked retention policy. |
| CompleteBucketWorm | oss:CompleteBucketWorm | Locks a retention policy. |
| ExtendBucketWorm | oss:ExtendBucketWorm | Extends the retention period in days for objects in a bucket that has a locked retention policy. |
| GetBucketWorm | oss:GetBucketWorm | Gets information about a retention policy. |
| PutBucketLogging | oss:PutBucketLogging | Enables log storage for a bucket. |
| oss:PutObject | When you enable log storage for a source bucket, this action sets the source bucket logs to be written to another destination bucket. |
| GetBucketLogging | oss:GetBucketLogging | Views the log storage configuration of a bucket. |
| DeleteBucketLogging | oss:DeleteBucketLogging | Disables log storage for a bucket. |
| PutBucketWebsite | oss:PutBucketWebsite | Configures a bucket for static website hosting and sets its redirection rules (RoutingRule). |
| GetBucketWebsite | oss:GetBucketWebsite | Views the static website hosting status and redirection rules of a bucket. |
| DeleteBucketWebsite | oss:DeleteBucketWebsite | Disables static website hosting for a bucket and clears its redirection rules. |
| PutBucketReferer | oss:PutBucketReferer | Configures hotlink protection for a bucket. |
| GetBucketReferer | oss:GetBucketReferer | Views the hotlink protection (Referer) configuration of a bucket. |
| PutBucketLifecycle | oss:PutBucketLifecycle | Sets a lifecycle rule for a bucket. |
| GetBucketLifecycle | oss:GetBucketLifecycle | Views the lifecycle rule of a bucket. |
| DeleteBucketLifecycle | oss:DeleteBucketLifecycle | Deletes the lifecycle rule of a bucket. |
| PutBucketTransferAcceleration | oss:PutBucketTransferAcceleration | Configures transfer acceleration for a bucket. |
| GetBucketTransferAcceleration | oss:GetBucketTransferAcceleration | Views the transfer acceleration configuration of a bucket. |
| ListMultipartUploads | oss:ListMultipartUploads | Lists all multipart upload events that are in progress. These are events that have been initiated but not yet completed or aborted. |
| PutBucketCors | oss:PutBucketCors | Sets the cross-origin resource sharing (CORS) rules for a specified bucket. |
| GetBucketCors | oss:GetBucketCors | Gets the current CORS rules for a specified bucket. |
| DeleteBucketCors | oss:DeleteBucketCors | Disables the CORS feature for a specified bucket and clears all rules. |
| PutBucketPolicy | oss:PutBucketPolicy | Sets the authorization policy for a specified bucket. |
| GetBucketPolicy | oss:GetBucketPolicy | Gets the authorization policy of a specified bucket. |
| DeleteBucketPolicy | oss:DeleteBucketPolicy | Deletes the authorization policy of a specified bucket. |
| PutBucketTags | oss:PutBucketTagging | Adds or modifies the tags of a specified bucket. |
| GetBucketTags | oss:GetBucketTagging | Gets the tags of a bucket. |
| DeleteBucketTags | oss:DeleteBucketTagging | Deletes the tags of a bucket. |
| PutBucketEncryption | oss:PutBucketEncryption | Configures the encryption rules for a bucket. |
| GetBucketEncryption | oss:GetBucketEncryption | Gets the encryption rules of a bucket. |
| DeleteBucketEncryption | oss:DeleteBucketEncryption | Deletes the encryption rules of a bucket. |
| PutBucketRequestPayment | oss:PutBucketRequestPayment | Configures the pay-by-requester mode. |
| GetBucketRequestPayment | oss:GetBucketRequestPayment | Gets the configuration information for the pay-by-requester mode. |
| PutBucketReplication | oss:PutBucketReplication | Sets the data replication rules for a bucket. |
| oss:ReplicateGet | Sets cross-account data replication rules for a bucket or specifies a RAM role for replication. |
| PutBucketRTC | oss:PutBucketRTC | Enables or disables replication time control (RTC) for an existing cross-region replication rule. |
| GetBucketReplication | oss:GetBucketReplication | Gets the configured data replication rules for a bucket. |
| DeleteBucketReplication | oss:DeleteBucketReplication | Stops data replication for a bucket and deletes its replication configuration. |
| GetBucketReplicationLocation | oss:GetBucketReplicationLocation | Gets the regions where destination buckets for replication can be located. |
| GetBucketReplicationProgress | oss:GetBucketReplicationProgress | Gets the data replication progress for a bucket. |
| PutBucketInventory | oss:PutBucketInventory | Configures inventory rules for a bucket. |
| GetBucketInventory | oss:GetBucketInventory | Views a specified inventory task in a bucket. |
| ListBucketInventory | oss:GetBucketInventory | Gets all inventory tasks in a bucket in a batch operation. |
| DeleteBucketInventory | oss:DeleteBucketInventory | Deletes a specified inventory task in a bucket. |
| PutBucketAccessMonitor | oss:PutBucketAccessMonitor | Configures the access tracking status for a bucket. |
| GetBucketAccessMonitor | oss:GetBucketAccessMonitor | Gets the access tracking status of a bucket. |
| OpenMetaQuery | oss:OpenMetaQuery | Enables the metadata management feature for a bucket. |
| GetMetaQueryStatus | oss:GetMetaQueryStatus | Gets the metadata index information for a bucket. |
| DoMetaQuery | oss:DoMetaQuery | Queries for objects that meet specified conditions and lists object information based on specified fields and sorting methods. |
| CloseMetaQuery | oss:CloseMetaQuery | Disables the metadata management feature for a bucket. |
| InitUserAntiDDosInfo | oss:InitUserAntiDDosInfo | Creates an Anti-DDoS for OSS instance. |
| UpdateUserAntiDDosInfo | oss:UpdateUserAntiDDosInfo | Changes the status of an Anti-DDoS for OSS instance. |
| GetUserAntiDDosInfo | oss:GetUserAntiDDosInfo | Queries for information about Anti-DDoS for OSS instances under a specified account. |
| InitBucketAntiDDosInfo | oss:InitBucketAntiDDosInfo | Initializes protection for a bucket. |
| UpdateBucketAntiDDosInfo | oss:UpdateBucketAntiDDosInfo | Updates the protection status of a bucket. |
| ListBucketAntiDDosInfo | oss:ListBucketAntiDDosInfo | Gets a list of protection information for a bucket. |
| PutBucketResourceGroup | oss:PutBucketResourceGroup | Sets the resource group to which a bucket belongs. |
| GetBucketResourceGroup | oss:GetBucketResourceGroup | Queries the ID of the resource group to which a bucket belongs. |
| CreateCnameToken | oss:CreateCnameToken | Creates a CnameToken required for domain name ownership verification. |
| GetCnameToken | oss:GetCnameToken | Gets a created CnameToken. |
| PutCname | oss:PutCname | Attaches a custom domain name to a bucket. |
| yundun-cert:DescribeSSLCertificatePrivateKeyyundun-cert:DescribeSSLCertificatePublicKeyDetailyundun-cert:CreateSSLCertificate | Attaches a certificate when you attach a custom domain name to a bucket. |
| ListCname | oss:ListCname | Gets a list of all custom domain names (Cnames) attached to a bucket. |
| DeleteCname | oss:DeleteCname | Deletes a Cname that is attached to a bucket. |
| PutStyle | oss:PutStyle | Sets an image style. |
| GetStyle | oss:GetStyle | Gets an image style. |
| ListStyle | oss:ListStyle | Lists image styles. |
| DeleteStyle | oss:DeleteStyle | Deletes an image style. |
| PutBucketArchiveDirectRead | oss:PutBucketArchiveDirectRead | Enables or disables real-time access of Archive objects for a bucket. |
| GetBucketArchiveDirectRead | oss:GetBucketArchiveDirectRead | Checks whether real-time access of Archive objects is enabled for a bucket. |
| CreateAccessPoint | oss:CreateAccessPoint | Creates an access point. |
| GetAccessPoint | oss:GetAccessPoint | Gets information about a single access point. |
| DeleteAccessPoint | oss:DeleteAccessPoint | Deletes an access point. |
| ListAccessPoints | oss:ListAccessPoints | Gets information about user-level and bucket-level access points. |
| PutAccessPointPolicy | oss:PutAccessPointPolicy | Configures an access point policy. |
| GetAccessPointPolicy | oss:GetAccessPointPolicy | Gets information about an access point policy. |
| DeleteAccessPointPolicy | oss:DeleteAccessPointPolicy | Deletes an access point policy. |
| PutBucketHttpsConfig | oss:PutBucketHttpsConfig | Enables or disables TLS version settings for a bucket. |
| GetBucketHttpsConfig | oss:GetBucketHttpsConfig | Views the TLS version settings for a bucket. |
| None | oss:ReplicateList | The list permission involved in the replication process. It lets OSS list the historical data of the source bucket and then replicate the historical data one by one. |
| CreateAccessPointForObjectProcess | oss:CreateAccessPointForObjectProcess | Creates an object FC access point. |
| GetAccessPointForObjectProcess | oss:GetAccessPointForObjectProcess | Gets basic information about an object FC access point. |
| DeleteAccessPointForObjectProcess | oss:DeleteAccessPointForObjectProcess | Deletes an object FC access point. |
| ListAccessPointsForObjectProcess | oss:ListAccessPointsForObjectProcess | Gets information about user-level object FC access points. |
| PutAccessPointConfigForObjectProcess | oss:PutAccessPointConfigForObjectProcess | Modifies the configuration of an object FC access point. |
| GetAccessPointConfigForObjectProcess | oss:GetAccessPointConfigForObjectProcess | Gets the configuration information of an object FC access point. |
| PutAccessPointPolicyForObjectProcess | oss:PutAccessPointPolicyForObjectProcess | Configures an access policy for an object FC access point. |
| GetAccessPointPolicyForObjectProcess | oss:GetAccessPointPolicyForObjectProcess | Gets the access policy configuration of an object FC access point. |
| DeleteAccessPointPolicyForObjectProcess | oss:DeleteAccessPointPolicyForObjectProcess | Deletes the access policy of an object FC access point. |
| WriteGetObjectResponse | oss:WriteGetObjectResponse | Customizes the returned data and response headers. |
| CreateBucketDataRedundancyTransition | oss:CreateBucketDataRedundancyTransition | Creates a storage redundancy transition task. |
| GetBucketDataRedundancyTransition | oss:GetBucketDataRedundancyTransition | Gets a storage redundancy transition task. |
| DeleteBucketDataRedundancyTransition | oss:DeleteBucketDataRedundancyTransition | Deletes a storage redundancy transition task. |
| ListBucketDataRedundancyTransition | oss:ListBucketDataRedundancyTransition | Lists all storage redundancy transition tasks in a bucket. |
| PutBucketPublicAccessBlock | oss:PutBucketPublicAccessBlock | Enables Block Public Access for a bucket. |
| GetBucketPublicAccessBlock | oss:GetBucketPublicAccessBlock | Gets the Block Public Access configuration of a bucket. |
| DeleteBucketPublicAccessBlock | oss:DeleteBucketPublicAccessBlock | Deletes the Block Public Access configuration of a bucket. |
| PutAccessPointPublicAccessBlock | oss:PutAccessPointPublicAccessBlock | Enables Block Public Access for an access point. |
| GetAccessPointPublicAccessBlock | oss:GetAccessPointPublicAccessBlock | Gets the Block Public Access configuration of an access point. |
| DeleteAccessPointPublicAccessBlock | oss:DeleteAccessPointPublicAccessBlock | Deletes the Block Public Access configuration of an access point. |
| GetBucketPolicyStatus | oss:GetBucketPolicyStatus | Checks whether the current bucket policy allows public access. |
| PutBucketOverwriteConfig | oss:PutBucketOverwriteConfig | Configures the disallow overwrite setting for a bucket. |
| GetBucketOverwriteConfig | oss:GetBucketOverwriteConfig | Gets the disallow overwrite configuration of a bucket. |
| DeleteBucketOverwriteConfig | oss:DeleteBucketOverwriteConfig | Deletes the disallow overwrite configuration of a bucket. |


### Object level


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/postobject#reference-smp-nsw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/appendobject#reference-fvf-xld-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initiatemultipartupload#reference-zgh-cnx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpart#reference-pnq-2px-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/abortmultipartupload#reference-txp-bvx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putsymlink#reference-qzz-qzw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobject#reference-ccf-rgd-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/headobject#reference-bgh-cbw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectmeta#reference-sg4-k2w-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/selectobject#reference-lz1-r1x-b2b)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getsymlink#reference-s3d-s1x-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject#reference-iqc-mqv-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletemultipleobjects#reference-ydg-25v-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject#reference-mvx-xxc-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpartcopy#reference-t4b-vpx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listparts#reference-hzm-1zx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjectacl#reference-fs3-gfw-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectacl#reference-lzc-24w-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/restoreobject#reference-mfr-5bx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjecttagging#reference-185784)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjecttagging#concept-185787)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobjecttagging#reference-185788)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putlivechannel#reference-d34-zcd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listlivechannel#reference-idb-smd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletelivechannel#reference-d4g-k12-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putlivechannelstatus#reference-r5k-kcd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getlivechannelinfo#reference-ekp-dkd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getlivechannelstat#reference-ov4-n3d-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getlivechannelhistory#reference-kjz-yld-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/postvodplaylist#reference-ry3-fhd-xdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvodplaylist#concept-rqq-gw2-cgb)


(https://www.alibabacloud.com/help/en/oss/user-guide/save-processed-images)


(https://www.alibabacloud.com/help/en/oss/user-guide/save-processed-images)


(https://www.alibabacloud.com/help/en/imm/developer-reference/api-imm-2020-09-30-createofficeconversiontask)


(https://www.alibabacloud.com/help/en/imm/developer-reference/api-imm-2020-09-30-generatewebofficetoken)


(https://www.alibabacloud.com/help/en/imm/developer-reference/api-imm-2020-09-30-refreshwebofficetoken)


> NOTE:

> NOTE: 


> NOTE: 




| API | Action | API description |
| --- | --- | --- |
| PutObject | oss:PutObject | Uploads an object. |
| oss:PutObjectTagging | When you upload an object, use x-oss-tagging to specify the object tag. |
| kms:GenerateDataKeykms:Decrypt | When you upload an object, specify that the object metadata contains X-Oss-Server-Side-Encryption: KMS. |
| PostObject | oss:PutObject | Uploads an object to a specified bucket using an HTML form. |
| AppendObject | oss:PutObject | Uploads an object by appending data. |
| oss:PutObjectTagging | When you upload an object by appending data, use x-oss-tagging to specify the object tag. |
| InitiateMultipartUpload | oss:PutObject | Initializes a multipart upload task. |
| oss:PutObjectTagging | When you initialize a multipart upload task, use x-oss-tagging to specify the object tag. |
| kms:GenerateDataKeykms:Decrypt | When you initialize a multipart upload task, specify that the object metadata contains X-Oss-Server-Side-Encryption: KMS. |
| UploadPart | oss:PutObject | Uploads data in parts based on the specified object name and uploadId. |
| CompleteMultipartUpload | oss:PutObject | After all data parts are uploaded, call this API to complete the multipart upload of the entire object. |
| oss:PutObjectTagging | After all data parts are uploaded, call this API to complete the multipart upload of the entire object and specify its tags. |
| AbortMultipartUpload | oss:AbortMultipartUpload | Cancels a multipart upload event and deletes the corresponding part data. |
| PutSymlink | oss:PutObject | Creates a symbolic link for a target object in OSS. |
| oss:PutObjectTagging | Creates a symbolic link with a specified object tag for a target object in OSS. |
| GetObject | oss:GetObject | Gets an object. |
| kms:Decrypt | You can download the specified KMS object. |
| oss:GetObjectVersion | Downloads a specified version of an object. |
| HeadObject | oss:GetObject | Gets the metadata of an object. |
| GetObjectMeta | oss:GetObject | Gets the metadata of an object, including its ETag, Size, and LastModified information. |
| SelectObject | oss:GetObject | Executes an SQL statement on a target object and returns the result. |
| GetSymlink | oss:GetObject | Gets the symbolic link of a target object. |
| DeleteObject | oss:DeleteObject | Deletes an object. |
| oss:DeleteObjectVersion | Deletes a specified version of an object. |
| DeleteMultipleObjects | oss:DeleteObject | Deletes multiple objects from the same bucket. |
| CopyObject | oss:GetObjectoss:PutObject | Copies an object between buckets in the same region. The buckets can be the same or different. |
| oss:GetObjectVersion | Copies a specified version of an object between buckets in the same region. The buckets can be the same or different. |
| oss:GetObjectTaggingoss:PutObjectTagging | Copies an object with specified tags between buckets in the same region. The buckets can be the same or different. |
| kms:GenerateDataKeykms:Decrypt | When you copy an object, specify that the metadata of the destination object contains X-Oss-Server-Side-Encryption: KMS. |
| oss:GetObjectVersionTagging | Copies a version of an object with specified tags between buckets in the same region. The buckets can be the same or different. |
| UploadPartCopy | oss:GetObjectoss:PutObject | Calls the UploadPartCopy API by adding the x-oss-copy-source request header to an UploadPart request. This copies data from an existing object to upload a part. |
| oss:GetObjectVersion | Calls the UploadPartCopy API by adding the x-oss-copy-source request header to an UploadPart request. This copies data from a specified version of an existing object to upload a part. |
| ListParts | oss:ListParts | Lists all successfully uploaded parts that belong to a specified Upload ID. |
| PutObjectACL | oss:PutObjectAcl | Modifies the ACL of an object in a bucket. |
| oss:PutObjectVersionAcl | Modifies the ACL of a specified version of an object in a bucket. |
| GetObjectACL | oss:GetObjectAcl | Gets the ACL of an object in a bucket. |
| oss:GetObjectVersionAcl | Gets the ACL of a specified version of an object in a bucket. |
| RestoreObject | oss:RestoreObject | Restores an object of the Archive Storage, Cold Archive, or Deep Cold Archive storage class. |
| oss:RestoreObjectVersion | Restores a specified version of an object of the Archive Storage, Cold Archive, or Deep Cold Archive storage class. |
| PutObjectTagging | oss:PutObjectTagging | Sets or updates the tagging information of an object. |
| oss:PutObjectVersionTagging | Sets or updates the tagging information of a specified version of an object. |
| GetObjectTagging | oss:GetObjectTagging | Gets the tagging information of an object. |
| oss:GetObjectVersionTagging | Gets the tagging information of a specified version of an object. |
| DeleteObjectTagging | oss:DeleteObjectTagging | Deletes the tagging information of a specified object. |
| oss:DeleteObjectVersionTagging | Deletes the tagging information of a specified version of an object. |
| PutLiveChannel | oss:PutLiveChannel | Before you upload audio and video data over RTMP, you must call this API to create a LiveChannel. |
| ListLiveChannel | oss:ListLiveChannel | Lists specified LiveChannels. |
| DeleteLiveChannel | oss:DeleteLiveChannel | Deletes a specified LiveChannel. |
| PutLiveChannelStatus | oss:PutLiveChannelStatus | Switches the status between enabled and disabled. |
| GetLiveChannelInfo | oss:GetLiveChannel | Gets the configuration information of a specified LiveChannel. |
| GetLiveChannelStat | oss:GetLiveChannelStat | Gets the stream ingest status of a specified LiveChannel. |
| GetLiveChannelHistory | oss:GetLiveChannelHistory | Gets the stream ingest records of a specified LiveChannel. |
| PostVodPlaylist | oss:PostVodPlaylist | Generates a playlist for video-on-demand for a specified LiveChannel. |
| GetVodPlaylist | oss:GetVodPlaylist | Views the playlist generated from stream ingest for a specified LiveChannel within a specified time period. |
| None | oss:PublishRtmpStream | Pushes audio and video data streams to RTMP. |
| None | oss:ProcessImm | The permission to use IMM for data processing through OSS. |
| PostProcessTask | oss:GetObject | The permission to use IMM for data processing through a POST request. |
| oss:PutObject | The permission to use IMM for Saveas data processing. |
| ImgSaveAs | oss:PostProcessTask | Saves the processed image to a specified bucket. |
| CreateOfficeConversionTask | imm:CreateOfficeConversionTask | The permission to use IMM for document conversion or snapshots. |
| GenerateWebofficeToken | imm: GenerateWebofficeToken | Used to obtain a Weboffice token. |
| RefreshWebofficeToken | imm:RefreshWebofficeToken | Used to refresh a Weboffice token. |
| None | oss:ReplicateGet | The read permission involved in the replication process. It lets OSS read data and metadata from the source and destination buckets, including objects, parts, and multipart uploads. |
| None | oss:ReplicatePut | The write permission involved in the replication process. It lets OSS perform write operations related to replication on the destination bucket. These operations include writing objects, multipart uploads, parts, and symbolic links, and modifying metadata. |
| None | oss:ReplicateDelete | The delete permission involved in the replication process. It lets OSS perform delete operations related to replication on the destination bucket. These operations include DeleteObject, AbortMultipartUpload, and DeleteMarker.Note This Action is required for the RAM role only when the data replication method is Add/Delete/Modify/Sync. |


### Resource pool QoS


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


| API | Action | API description |
| --- | --- | --- |
| PutBucketQoSInfo | oss:PutBucketQoSInfo | Sets throttling for a bucket in a resource pool. |
| GetBucketQoSInfo | oss:GetBucketQoSInfo | Gets the throttling configuration for a bucket in a resource pool. |
| DeleteBucketQosInfo | oss:DeleteBucketQoSInfo | Deletes the throttling configuration for a specified bucket in a resource pool. |
| PutBucketRequesterQoSInfo | oss:PutBucketRequesterQoSInfo | Sets bucket-level throttling for a requester. |
| GetBucketRequesterQoSInfo | oss:GetBucketRequesterQoSInfo | Gets the bucket-level throttling configuration for a specified requester. |
| ListBucketRequesterQoSInfos | oss:ListBucketRequesterQoSInfo | Gets the bucket-level throttling configurations for all requesters. |
| DeleteBucketRequesterQoSInfo | oss:DeleteBucketRequesterQoSInfo | Deletes the throttling configuration for a requester of a bucket. |
| ListResourcePools | oss:ListResourcePools | Gets information about all resource pools under the current account. |
| GetResourcePoolInfo | oss:GetResourcePoolInfo | Gets the throttling configuration of a specified resource pool. |
| ListResourcePoolBuckets | oss:ListResourcePoolBuckets | Gets the list of buckets included in a specified resource pool. |
| PutResourcePoolRequesterQoSInfo | oss:PutResourcePoolRequesterQoSInfo | Configures throttling for a requester of a resource pool. |
| GetResourcePoolRequesterQoSInfo | oss:GetResourcePoolRequesterQoSInfo | Gets the throttling configuration for a specified requester in a resource pool. |
| ListResourcePoolRequesterQoSInfos | oss:ListResourcePoolRequesterQoSInfos | Gets the throttling configurations for all requesters in a resource pool. |
| DeleteResourcePoolRequesterQoSInfo | oss:DeleteResourcePoolRequesterQoSInfo | Deletes the throttling configuration for a specified requester in a resource pool. |


### Vector bucket


(https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorbucket)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvectorbucket)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorbuckets)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectorbucket)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketlogging#reference-t1g-zj5-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketlogging#reference-mm3-zwv-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketlogging#reference-jrn-gsw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy#reference-2424532)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicy#reference-2424982)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletebucketpolicy#reference-2424995)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorindex)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvectorindex)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorindexes)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectorindex)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/queryvectors)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectors)


| API | Action | API description |
| --- | --- | --- |
| PutVectorBucket | oss:PutVectorBucket | Creates a vector bucket. |
| GetVectorBucket | oss:GetVectorBucket | Gets the details of a vector bucket. |
| ListVectorBuckets | oss:ListVectorBuckets | Lists all vector buckets that the requester owns. |
| DeleteVectorBucket | oss:DeleteVectorBucket | Deletes a vector bucket. |
| PutBucketLogging | oss:PutBucketLogging | Enables log storage for a vector bucket. |
| oss:PutObject | When you enable log storage for a source vector bucket, this action sets the source vector bucket logs to be written to another destination bucket. |
| GetBucketLogging | oss:GetBucketLogging | Views the log storage configuration of a vector bucket. |
| DeleteBucketLogging | oss:DeleteBucketLogging | Disables log storage for a vector bucket. |
| PutBucketPolicy | oss:PutBucketPolicy | Sets the authorization policy for a specified vector bucket. |
| GetBucketPolicy | oss:GetBucketPolicy | Gets the authorization policy of a specified vector bucket. |
| DeleteBucketPolicy | oss:DeleteBucketPolicy | Deletes the authorization policy of a specified vector bucket. |
| PutVectorIndex | oss:PutVectorIndex | Creates a vector index. |
| GetVectorIndex | oss:GetVectorIndex | Gets the details of a vector index. |
| ListVectorIndexes | oss:ListVectorIndexes | Lists all vector indexes in a vector bucket. |
| DeleteVectorIndex | oss:DeleteVectorIndex | Deletes a vector index. |
| PutVectors | oss:PutVectors | Writes vector data. |
| GetVectors | oss:GetVectors | Gets specified vector data. |
| ListVectors | oss:ListVectors | Lists all vector data in a vector index. |
| QueryVectors | oss:QueryVectors | Performs a vector similarity search. |
| DeleteVectors | oss:DeleteVectors | Deletes specified vector data from a vector index. |


## Resource


The Resource element specifies one or more resources. You can use the asterisk (`*`) as a wildcard character. A single bucket policy can include multiple resources.

### Bucket




















| Category | Format | Example |
| --- | --- | --- |
| Bucket level | acs:oss:{region}:{bucket_owner_id}:{bucket_name} | acs:oss:*:*:example-bucket |
| Object level | acs:oss:{region}:{bucket_owner_id}:{bucket_name}/{object_name} | acs:oss:*:*:example-bucket/abc.txt |
| Resource pool level | acs:oss:{region}:{account_id}:resourcepool/{resource_pool_name} | acs:oss:*:*:resourcepool/resource-pool-for-ai |


### Vector bucket


























| Resource level | Format | Example |
| --- | --- | --- |
| All vector resources | acs:ossvector:*:*:* | acs:ossvector:*:*:* |
| Vector bucket | acs:ossvector:{region}:{account_id}:{bucket_name} | acs:ossvector:*:*:my-vector-bucket |
| Vector index | acs:ossvector:{region}:{account_id}:{bucket_name}/{index_name} | acs:ossvector:*:*:my-vector-bucket/myindex |
| Vector data | acs:ossvector:{region}:{account_id}:{bucket_name}/{index_name}/* | acs:ossvector:*:*:my-vector-bucket/myindex/* |


> NOTE:

> NOTE: 


> NOTE: Note 

The region field currently supports only the wildcard asterisk (`*`).


## Condition


The Condition element specifies the conditions under which a policy takes effect. It consists of a condition operator, a condition key, and a condition value.

### Condition operators


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


| Condition operator type | Supported types |
| --- | --- |
| String | StringEqualsStringNotEqualsStringEqualsIgnoreCaseStringNotEqualsIgnoreCaseStringLikeStringNotLike |
| Number | NumericEqualsNumericNotEqualsNumericLessThanNumericLessThanEqualsNumericGreaterThanNumericGreaterThanEquals |
| Date and time | DateEqualsDateNotEqualsDateLessThanDateLessThanEqualsDateGreaterThanDateGreaterThanEquals |
| Boolean | Bool |
| IP Address Type | IpAddressNotIpAddressIpAddressIncludeBorder |


### Condition keys





> IMPORTANT:

> NOTE: 


> NOTE: 







> NOTE:

> NOTE: 


> NOTE: 

(https://www.alibabacloud.com/help/en/oss/oss-supported-gateway-endpoint-regions)


-



-







-



-



-




(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-acl)


-



-



-



-




(https://www.alibabacloud.com/help/en/oss/user-guide/object-acl)





-



-
















| Condition key | Description |
| --- | --- |
| acs:SourceIp | Specifies a standard IP CIDR block. The asterisk (*) wildcard is supported.Important When you configure a bucket policy or RAM policy, do so based on your network access architecture. Configure both the acs:SourceIp and acs:SourceVpc conditions for dual access control. Using only one condition can create security risks. For example, if you restrict access only by public IP address, a VPC can still gain unauthorized access using a matching egress IP address. |
| acs:SourceVpc | Specifies the VPC. The value can be a specific VPC ID or vpc-*.Note When you use acs:SourceVpc to restrict access by source VPC, ensure that the region of the selected VPC matches a region where OSS supports gateway endpoints. Otherwise, authentication requests cannot be associated with the correct VPC, and the requests fail. For more information about the regions where OSS supports gateway endpoints, see Regions where OSS supports gateway endpoints. |
| acs:UserAgent | Specifies the HTTP User-Agent header.Type: string. |
| acs:CurrentTime | The time when the request arrives at the OSS server.Format: ISO 8601. |
| acs:SecureTransport | The protocol type of the request. Valid values:true: Only HTTPS requests are allowed.false: Allows only HTTP requests.If acs:SecureTransport is not set, both HTTP and HTTPS requests are allowed. |
| oss:x-oss-acl | Restricts the type of bucket ACL. Valid values:private: Private.public-read: Public read.public-read-write: Public read-write.For more information, see Bucket ACL. |
| oss:x-oss-object-acl | Restricts the type of object ACL. Valid values:private: private.public-read: Public read.public-read-write: Public read-write.default: Inherits the Bucket ACL.For more information, see Object ACL. |
| oss:Prefix | Used in a ListObjects request to list objects with a specified prefix. |
| oss:Delimiter | Used in a ListObjects request as the character to group object names. |
| acs:AccessId | The AccessId included in the request. |
| oss:BucketTag | A bucket tag.A single BucketTag can be used as a Condition. When you set multiple BucketTags, you must add the oss:BucketTag/ prefix to each BucketTag to form multiple Conditions. |
| acs:MFAPresent | Specifies whether multi-factor authentication (MFA) is enabled.Values:true: MFA is enabled.false: Multi-factor authentication is not enabled. |
| oss:ExistingObjectTag | The requested object is already tagged.A single ObjectTag can be used as a condition. When you use multiple ObjectTags, you must add oss:ExistingObjectTag/ before each ObjectTag.This applies mainly to APIs for reading files, such as GetObject and HeadObject, and ObjectTagging APIs, such as PutObjectTagging and GetObjectTagging. |
| oss:RequestObjectTag | The object tags included in the request.A single object tag can be used as a condition. When multiple object tags are specified, you must add oss:RequestObjectTag/ before each object tag.This mainly applies to API operations for writing files, such as PutObject and PostObject, and ObjectTagging API operations, such as PutObjectTagging and GetObjectTagging. |


## References


-

[Authentication flow details](https://www.alibabacloud.com/help/en/oss/user-guide/authentication)

-

[Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/)

-

[RAM Policy](https://www.alibabacloud.com/help/en/oss/ram-policy-overview/)

Thank you! We've received your  feedback.