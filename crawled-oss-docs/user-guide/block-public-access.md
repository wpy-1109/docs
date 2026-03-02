# Prevent unauthorized access to OSS data by enabling Block Public Access

You can allow public access to Object Storage Service (OSS) resources by configuring bucket policies and access control lists (ACLs). Public access eliminates the need for permission verification and authentication, increasing the risks of data leaks and outbound Internet traffic. To mitigate risks associated with public access, OSS lets you to enable Block Public Access at the account level, and for individual buckets, access points, or Object FC Access Points. When enabled, this feature ignores existing public permissions and prevents new public permissions from being granted, ensuring the security of your data.

## Check whether public access is allowed in bucket policies and ACLs


To evaluate whether an OSS object is publicly accessible, you must review the bucket policy and ACLs (including the bucket ACL and object ACL). If any of the permission settings grants public access, your resource faces a security risk, and enabling Block Public Access is recommended.

### Bucket policy

#### (Recommended) Call the GetBucketPolicyStatus operation


You can call the GetBucketPolicyStatus operation to check whether a bucket policy grants public access.


-

If the value of the IsPublic response parameter is true, the bucket policy grants public access.

-

If the value of the IsPublic response parameter is false, the bucket policy does not grant public access.


For more information, see [GetBucketPolicyStatus](https://www.alibabacloud.com/help/en/oss/developer-reference/getbucketpolicystatus).

#### Manually review bucket policy settings

#### Conditions and examples for non-public access


-

A statement in a bucket policy is considered non-public if its Principal or Condition element meets any of the criteria in the following table.


> NOTE:

> NOTE: 


> NOTE: Note 

-

The Action and Resource elements do not determine whether a bucket policy grants public access.

-

If the value of the Effect element in the bucket policy is Deny, the bucket policy does not grant public access.











| Element | Field | Value |
| --- | --- | --- |
| Principal | N/A | Specifies one or more fixed values that do not contain the asterisk (*) wildcard. |
| Condition | acs:SourceVpcId | Specifies one or more fixed values that do not contain the asterisk (*) wildcard. |
| acs:SourceVpc | Specifies one or more fixed values that do not contain the asterisk (*) wildcard. |
| acs:AccessId | Specifies one or more fixed values that do not contain the asterisk (*) wildcard. |
| acs:SourceVpcIp | For IPv4 addresses, the mask must be greater than or equal to 8.For IPv6 addresses, the mask must be greater than or equal to 32. |
| acs:SourceIp | For IPv4 addresses, the mask must be greater than or equal to 8.For IPv6 addresses, the mask must be greater than or equal to 32. |


-

The following example bucket policy grants non-public access:


`json
{
    "Version":"1",
    "Statement":[
        {
            "Action":[
                "oss:GetObject",
                "oss:GetObjectAcl",
                "oss:GetObjectVersion",
                "oss:GetObjectVersionAcl"
            ],
            "Effect":"Allow",
            "Principal":[
                "20214760404935xxxx"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:examplebucket/hangzhou/2020/*",
                "acs:oss:*:174649585760xxxx:examplebucket/shanghai/2015/*"
            ]
        },
        {
            "Action":[
                "oss:ListObjects",
                "oss:ListObjectVersions"
            ],
            "Condition":{
                "StringLike":{
                    "oss:Prefix":[
                        "hangzhou/2020/*",
                        "shanghai/2015/*"
                    ]
                }
            },
            "Effect":"Allow",
            "Principal":[
                "20214760404935xxxx"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:examplebucket"
            ]
        }
    ]
}
`


#### Conditions and examples for public access


A bucket policy is considered to grant public access if it fails to meet the criteria for non-public access. Examples


-

Example 1


`json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "oss:GetObject",
            "Principal": "*",
            "Resource": "acs:oss:*:17464958576xxxx:examplebucket/*"
        }
    ]
}
`


-

Example 2


If a bucket policy contains both a public access statement that allows access from all virtual private clouds (VPCs) and a non-public access statement that allows access only from specific users, the bucket policy is considered to grant public access.


`json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "oss:GetObject",
            "Principal": "*",
            "Resource": "acs:oss:*:17464958576xxxx:examplebucket/*",
            "Condition": {
                "StringLike": {
                    "acs:SourceVpc": [
                        "vpc-*"
                        ]
                }
            }
        },
      	{
            "Effect": "Allow",
            "Action": "oss:*",
            "Principal": "27464958576xxxx",
            "Resource": "*"
        }
    ]
}
`


## ACL


-

If the bucket ACL or object ACL is set to public-read or public-read-write, public access is allowed.

-

If both the bucket ACL and the object ACL are set to private, public access is denied.

## Priorities of Block Public Access settings at different levels


OSS allows you to enable Block Public Access at the account level and for individual buckets, access points, and Object FC Access Points. If Block Public Access settings are configured at different levels, OSS will use the following priority order to determine the final access effect:


`shell
Account > Bucket > Access point > Object FC Access Point
`


Based on this priority, a setting at a higher level overrides any conflicting settings at a lower level. For example, if you enable Block Public Access at the account level, public access is blocked for all buckets, access points, and Object FC Access Points in your account, regardless of their individual settings.


-

To allow public access to a bucket, you must disable Block Public Access at the global level and for the bucket.

-

To allow public access to a bucket by using an access point, you must disable Block Public Access at the account level, for the bucket with which the access point is associated, and for the access point.

-

To allow public access through an Object FC Access Point, you must disable Block Public Access at the account level, for the bucket, for the access point used by the Object FC Access Point, and for the Object FC Access Point itself.

## Usage notes


-

A RAM user requires corresponding permissions to enable Block Public Access:


-

At the account level: `oss:PutPublicAccessBlock`, `oss:GetPublicAccessBlock`, and `oss:DeletePublicAccessBlock`

-

For individual buckets: `oss:PutBucketPublicAccessBlock`, `oss:GetBucketPublicAccessBlock`, and `oss:DeleteBucketPublicAccessBlock`

-

For individual access points: `oss:PutAccessPointPublicAccessBlock`, `oss:GetAccessPointPublicAccessBlock`, and `oss:DeleteAccessPointPublicAccessBlock`

-

For individual Object FC Access Points: `oss:PutAccessPointConfigForObjectProcess`, `oss:GetAccessPointConfigForObjectProcess`, and `oss:DeleteAccessPointForObjectProcess`

-

If you enable Block Public Access, existing public access permissions are ignored and you cannot configure public access permissions. After you disable Block Public Access, existing public access permissions take effect again and you can configure new public access permissions.

-

If you configure a bucket policy that allows all users to manage an access point of a bucket, users can change the status of Block Public Access of the access point by using the third-level domain name of the bucket even if Block Public Access is enabled for the access point. The configurations of the access point do not take effect on access requests created by using the subdomains of the bucket.

-

For cross-region replication (CRR) and same-region replication (SRR) tasks, the ACL of an object is preserved during replication, regardless of the public access blocking settings on the source and destination buckets. If Block Public Access is enabled for the destination bucket, public access to the objects that are replicated to the destination bucket is not allowed even if the ACL of the objects are public-read or public-read-write.

## Methods

### Use the OSS console

#### Enable Block Public Access at the global level


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, choose Data Service > Block Public Access.

-

On the Block Public Access page, turn on Block Public Access and follow the on-screen instructions to complete the setting.

#### Enable Block Public Access for a bucket


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left-side navigation tree, choose Permission Control > Block Public Access.

-

On the Block Public Access tab, turn on Block Public Access and follow the on-screen instructions to complete the setting.

#### Enable Block Public Access for an access point


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Access Points. On the Access Points page, click the name of the access point for which you want to enable Block Public Access.

-

In the Basic Information section, click Enable next to Block Public Access and follow the on-screen instructions to complete the setting.

#### Enable Block Public Access for an Object FC Access Point


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Object FC Access Points. On the Object FC Access Points page, click the Object FC Access Point for which you want to enable Block Public Access.

-

In the Basic Information section, click Enable next to Block Public Access and follow the on-screen instructions to complete the setting.

### Use ossutil


You can enable Block Public Access by using ossutil. For information about how to install ossutil, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


-

The following sample command enables Block Public Access at the account level:


`bash
ossutil api put-public-access-block --public-access-block-configuration "{\"BlockPublicAccess\":\"true\"}"
`


For more information, see [put-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/put-public-access-block).

-

The following sample command enables Block Public Access for `examplebucket`:


`bash
ossutil api put-bucket-public-access-block --bucket examplebucket --public-access-block-configuration "{\"BlockPublicAccess\":\"true\"}"
`


For more information, see [put-bucket-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-public-access-block).

-

The following sample command enables Block Public Access for the access point `ap-01`:


`bash
ossutil api put-access-point-public-access-block --bucket examplebucket --access-point-name ap-01 --public-access-block-configuration "{\"BlockPublicAccess\":\"true\"}"
`


For more information, see [put-access-point-public-access-block](https://www.alibabacloud.com/help/en/oss/developer-reference/put-access-point-public-access-block).

## Related API operations


If your business requires a high level of customization, you can directly call RESTful APIs. To directly call an API, you must include the signature calculation in your code.


-

Refer to [PutPublicAccessBlock](https://www.alibabacloud.com/help/en/oss/developer-reference/putpublicaccessblock) to block public access at the account level.

-

Refer to [PutBucketPublicAccessBlock](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpublicaccessblock) to block public access for a bucket.

-

Refer to [PutAccessPointPublicAccessBlock](https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpublicaccessblock) to block public access for an access point.

-

Refer to [PutAccessPointConfigForObjectProcess](https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointconfigforobjectprocess) to block public access for an Object FC Access Point.

## Related topics


Block Public Access settings manage access permissions at the account level, as well as for individual buckets, access points, and Object FC Access Points. To implement more granular access control on objects within a bucket, you can combine Block Public Access settings with [bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/) and [object ACLs](https://www.alibabacloud.com/help/en/oss/user-guide/object-acl).


Thank you! We've received your  feedback.