# Configure bucket policies

A bucket policy is an access policy attached to a bucket. You can use bucket policies to grant access to other Alibaba Cloud accounts, RAM users, or anonymous users. Bucket policies support cross-account authorization, anonymous access control, and access restrictions based on IP addresses or VPCs.

## How it works


Bucket policies use a resource-based authorization model. A policy is attached directly to a bucket and defines which principals, such as users, accounts, or roles, can perform which actions on which resources under specific conditions.


When a user sends an access request, OSS evaluates all relevant policies, including bucket policies and RAM policies, and applies the explicit deny takes precedence rule. Any explicit Deny statement immediately blocks the request, overriding all Allow statements. If no Deny or Allow statement applies, the request is denied by default.


Bucket policies apply to the bucket owner according to the following special rules:


-

If the Principal is set to the wildcard character (*) and no Condition is specified, the policy applies only to users other than the bucket owner.

-

If the Principal is set to the wildcard character (*) and a Condition is specified, the policy applies to all users, including the bucket owner.


If you configure multiple bucket policy statements for the same user, the user’s effective permissions are the union of all statements, following the deny takes precedence rule.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

-

If you configure a bucket policy that includes `acs:SourceIp`, you must also include `acs:SourceVpc`.


## Configure bucket policies


OSS supports two configuration methods: graphical and syntax-based. You can choose the method that best fits your scenario.


-

Graphical method: Provides an intuitive, form-based experience for common authorization scenarios and simplifies policy configuration.

-

Syntax method: Uses JSON to write complete policies. This method supports all advanced features and complex condition combinations, and offers maximum flexibility.

## Graphical method


-

Go to the [bucket list](https://oss.console.alibabacloud.com/bucket) and click the target bucket.

-

In the navigation pane on the left, click Permission Control > Bucket Policy.

-

Click Add in GUI, click Authorize, and then configure the settings.

















-



-







-



-






-







-




> NOTE:

> NOTE: 


> NOTE: 




-







-



-



-



-



-







| Configuration Item | Description |
| --- | --- |
| Applied To | Select whether to grant permissions on the Whole Bucket or on Specific Resources. |
| Resource Paths | If you select Applied To = Whole Bucket, the Resource Paths is bucket-name/*.If you set Applied To to Specific Resources, enter the folder or individual Object to authorize. You can add multiple records. |
| Authorized User | Specify the user or account to authorize.All Accounts (*): Authorizes anyone, including anonymous users.RAM User: Select a RAM user from the current Alibaba Cloud account.You must be signed in as an Alibaba Cloud account or as a RAM user who has both bucket management permissions and the ListUsers permission in the RAM console. Otherwise, you cannot view the list of RAM users for the current account.Other Accounts: Enter the UID of another Alibaba Cloud account or RAM user, or the ARN of a temporary role in the format arn:sts (for example, arn:sts::1798:assumed-role/role-name/session-name). You can authorize multiple users—one per line.If you authorize a RAM role, that role cannot access the bucket through the OSS console. Use ossutil, SDKs, or APIs instead. |
| Authorized Operation | Basic Settings: Choose from common permission combinations: Read-Only (excluding ListObject), Read-Only (including ListObject), Read/Write, Full Access, or Deny Access.Note To ensure OSS-HDFS service users can access the .dlsdata/ directory and its objects, do not select Deny Access when configuring a bucket policy for a bucket with OSS-HDFS enabled.Advanced Settings: Customize the Effect (Allow or Reject) and Actions. |
| Condition (optional) | Set conditions under which the policy applies.Access Method: Choose HTTPS or HTTP. The policy applies only when requests use the selected method.IP =: Enter a list of allowed IP addresses or CIDR blocks. The policy applies only when requests originate from one of these IPs.IP ≠: Enter a list of blocked IP addresses or CIDR blocks. The policy applies only when requests originate from outside this list.VPC =: Select a VPC from the current account or enter a VPC ID from another account. The policy applies only when requests come from the specified VPC.VPC ≠: Select a VPC from the current account or enter a VPC ID from another account. The policy applies only when requests do not come from the specified VPC.When you specify multiple conditions, all conditions must be met (AND logic) for the policy to apply. |


-

After you confirm the settings, click OK to apply the bucket policy.

## Syntax method


-

Go to the [bucket list](https://oss.console.alibabacloud.com/bucket) and click the target bucket.

-

In the navigation pane on the left, click Permission Control > Bucket Policy.

-

Click Add by Syntax, click Edit, and then enter a JSON-formatted policy in the editor.


Example policy: Deny all operations on `example-bucket` for user `20214760404935xxxx` if the request does not originate from VPC `vpc-t4nlw426y44rd3iq4xxxx`.


`json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "oss:*",
            "Principal": [
                "20214760404935xxxx"
            ],
            "Resource": [
                "acs:oss:*:174649585760xxxx:example-bucket",
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition": {
                "StringNotEquals": {
                    "acs:SourceVpc": "vpc-t4nlw426y44rd3iq4xxxx"
                }
            }
        }
    ]
}
`


A complete policy contains Version and Statement.


-

Version: The policy version. The value is fixed at `1` and cannot be modified.

-

Statement: The main body of the policy, which contains one or more allow or deny rules. Each statement includes the Effect, Action, Principal, Resource, and Condition elements.


















































| Policy element | Description | Meaning in the example authorization policy |
| --- | --- | --- |
| Effect | The effect of the policy. Valid values: Allow or Deny. | Deny the request. |
| Action | The operation on the resource. The wildcard character * is supported. | Deny all OSS operations (oss:*). |
| Principal | The entity to which the policy applies, such as a user, account, or role.An empty list (Principal:) behaves identically to Principal:["*"]. | The policy applies only to RAM user 20214760404935xxxx. |
| Resource | The resources to which the policy applies. | The policy applies to example-bucket and all objects within it. |
| Condition | The condition for the policy to take effect.If you specify multiple conditions, the policy applies only if all conditions are met (AND logic). | The Deny rule applies only when the request originates from a VPC other than vpc-t4nlw426y44rd3iq4xxxx. |


For a complete list of policy elements, see [Policy syntax and elements](https://www.alibabacloud.com/help/en/oss/user-guide/authorization-syntax-and-elements).

-

After you confirm the policy, click Save and follow the on-screen instructions.

## Configure bucket policies for vector buckets


Vector buckets support only the syntax method for bucket policy configuration.


-

Go to the [vector bucket list](https://oss.console.alibabacloud.com/vector-bucket-list) and click the target vector bucket.

-

In the navigation pane on the left, click Permission Control > Bucket Policy.

-

Click Edit and enter a JSON-formatted policy in the editor.


Example policy: This example grants read and write access to vector data in the `indextest` index table within the `vector-bucket-example` bucket for the user `20816353761158`.


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:PutVectors",
      "oss:GetVectors"
    ],
    "Principal": [
      "20816353761158"
    ],
    "Resource": [
      "acs:ossvector:*:*:vector-bucket-example/indextest"
    ]
  }]
}
`


A complete policy contains Version and Statement.


-

Version: The policy version. The value is fixed at `1` and cannot be modified.

-

Statement: The main body of the policy, which contains one or more allow or deny rules. Each statement includes the Effect, Action, Principal, Resource, and Condition elements.












































| Policy element | Description | Explanation of the example authorization policy |
| --- | --- | --- |
| Effect | The effect of the policy. Valid values are Allow and Deny. | Allow the request. |
| Action | The operation on the resource. The wildcard character * is supported. | Read and write vector data. |
| Principal | The entity to which the policy applies, such as a user, account, or role.An empty list (Principal:) behaves identically to Principal:["*"]. | The policy applies only to RAM user 20816353761158. |
| Resource | The resources to which the policy applies. | The policy applies to the indextest index table in the vector-bucket-example bucket. |
| Condition | The condition for the policy to take effect.If you specify multiple conditions, the policy applies only if all conditions are met (AND logic). | None. |


For a complete list of policy elements, see [Policy syntax and elements](https://www.alibabacloud.com/help/en/oss/user-guide/authorization-syntax-and-elements).

-

After you confirm the policy, click Save and follow the on-screen instructions.

## Common authorization scenarios


The following scenarios show typical real-world uses of bucket policies. They cover permission grants, access restrictions, and security controls. Each scenario includes a complete policy example that you can adapt to your needs.

### Scenario 1: Grant read/write permissions to specific RAM users


You can grant read/write permissions to team members or partners using bucket policies. This example grants read/write access to the `example-bucket` bucket for RAM users with the UIDs `27737962156157xxxx` and `20214760404935xxxx`.


> NOTE:

> NOTE: 


> NOTE: Note 

This policy does not grant the RAM users permission to list buckets. As a result, the users cannot view all buckets on the [bucket list](https://oss.console.alibabacloud.com/bucket) page or click the target bucket. Instead, they can add and access the bucket by clicking Favorite Paths > + in the navigation pane on the left.


`json
{
    "Version":"1",
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
                "oss:GetObject",
                "oss:PutObject",
                "oss:GetObjectAcl",
                "oss:PutObjectAcl",
                "oss:AbortMultipartUpload",
                "oss:ListParts",
                "oss:RestoreObject",
                "oss:GetVodPlaylist",
                "oss:PostVodPlaylist",
                "oss:PublishRtmpStream",
                "oss:ListObjectVersions",
                "oss:GetObjectVersion",
                "oss:GetObjectVersionAcl",
                "oss:RestoreObjectVersion"
            ],
            "Principal":[
                "27737962156157xxxx",
                "20214760404935xxxx"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ]
        },
        {
            "Effect":"Allow",
            "Action":[
                "oss:ListObjects"
            ],
            "Principal":[
                "27737962156157xxxx",
                "20214760404935xxxx"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket"
            ],
            "Condition":{
                "StringLike":{
                    "oss:Prefix":[
                        "*"
                    ]
                }
            }
        }
    ]
}
`


### Scenario 2: Grant read-only permissions to specific RAM users for specific directories


You can protect project files from modification while allowing authorized users to read them. This example grants read-only access to the `example-bucket` bucket for the RAM user `20214760404935xxxx`. The access is limited to directories with the prefixes `hangzhou/2020` and `shanghai/2015`.


> NOTE:

> NOTE: 


> NOTE: Note 

This policy does not grant the RAM users permission to list buckets. As a result, the users cannot view all buckets on the [bucket list](https://oss.console.alibabacloud.com/bucket) page or click the target bucket. Instead, they can add and access the bucket by clicking Favorite Paths > + in the navigation pane on the left.


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
                "acs:oss:*:174649585760xxxx:example-bucket/hangzhou/2020/*",
                "acs:oss:*:174649585760xxxx:example-bucket/shanghai/2015/*"
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
                "acs:oss:*:174649585760xxxx:example-bucket"
            ]
        }
    ]
}
`


### Scenario 3: Grant permission to list bucket contents to specific RAM users


You can allow team members or partners to view all bucket information and list the bucket's contents. This example grants a RAM user the permissions to view all bucket information and list the contents of the `example-bucket` bucket.


> NOTE:

> NOTE: 


> NOTE: Note 

This policy does not grant the RAM users permission to list buckets. As a result, the users cannot view all buckets on the [bucket list](https://oss.console.alibabacloud.com/bucket) page or click the target bucket. Instead, they can add and access the bucket by clicking Favorite Paths > + in the navigation pane on the left.


`json
{
    "Version":"1",
    "Statement":[
        {
            "Action":[
                "oss:Get*",
                "oss:ListObjects",
                "oss:ListObjectVersions"
            ],
            "Effect":"Allow",
            "Principal":[
                "20214760404935xxxx"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket"
            ]
        }
    ]
}
`


### Scenario 4: Grant read-only access to specific RAM roles


You can allow RAM users or applications to temporarily access bucket objects. To do this, create a RAM role and assign permissions. Users or applications can then assume the role to obtain temporary credentials for reading objects. This example grants read access to all objects in the `example-bucket` bucket for all sessions of one RAM role and for a specific session of another RAM role.


> NOTE:

> NOTE: 


> NOTE: Note 

When you authorize a RAM role, the `Principal` must follow this format: `arn:sts::<uid>:assumed-role/<role-name>/<session-name>`. The values for `<role-name>` and `<session-name>` are case-sensitive.


`json
{
    "Version": "1",
    "Statement": [
        {
            "Action": [
                "oss:GetObject"
            ],
            "Effect": "Allow",
            "Principal": [
                "arn:sts::10323xxxxx72056:assumed-role/role-name/session-name",
                "arn:sts::10323xxxxx72056:assumed-role/role2-name/*"
            ],
            "Resource": [
                "acs:oss:*:10323xxxxx72056:example-bucket/*"
            ]
        }
    ]
}
`


### Scenario 5: Grant list permissions to all users


If a bucket is used for public resource sharing, you may want to allow all visitors to list filenames without accessing the file content. To do this, you can set the Principal to the wildcard asterisk (`*`) and grant permission to list all files. The following example grants all visitors permission to list all files in the `example-bucket` bucket.


`json
{
    "Version":"1",
    "Statement":[
        {
            "Action":[
                "oss:ListObjects",
                "oss:ListObjectVersions"
            ],
            "Effect":"Allow",
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket"
            ]
        }
    ]
}
`


### Scenario 6: Restricted from public network access


You can block all non-VPC access to a bucket. To do this, use the `acs:SourceVpc` condition to create a Deny statement that rejects requests that do not originate from a VPC. Internet requests fail because they do not have a VPC prefix. This example denies all access to the `example-bucket` bucket except for access from VPC networks.


`json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "oss:*",
      "Principal": [
        "*"
      ],
      "Resource": [
        "acs:oss:*:174649585760xxxx:example-bucket/*",
        "acs:oss:*:174649585760xxxx:example-bucket"
      ],
      "Condition": {
        "StringNotLike": {
          "acs:SourceVpc": [
            "vpc-*"
          ]
        }
      }
    }
  ]
}
`


### Scenario 7: Allow access only from a specific VPC


You can restrict bucket access to a single VPC. To do this, use the `acs:SourceVpc` condition to create a Deny statement that blocks requests from other VPCs or the internet. Requests from other VPCs or the internet fail because they do not match the specified VPC ID. This example denies read access to objects in the `example-bucket` bucket for all users except for those in VPC `t4nlw426y44rd3iq4xxxx`.


> NOTE:

> NOTE: 


> NOTE: Note 

-

Because the Principal in the following deny policy statement is a wildcard asterisk (`*`) and the statement includes a Condition, this deny policy statement applies to all users, including the bucket owner.

-

This Deny statement only restricts access. It does not grant any permissions. If the principal does not have permissions, you must add an Allow statement to grant access.


`json
{
    "Version":"1",
    "Statement":[
        {
            "Effect":"Deny",
            "Action":[
                "oss:GetObject"
            ],
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition":{
                "StringNotEquals":{
                    "acs:SourceVpc":[
                        "vpc-t4nlw426y44rd3iq4xxxx"
                    ]
                }
            }
        }
    ]
}
`


### Scenario 8: Allow access only from a specific public IP address


You can restrict bucket access to a single public IP address. To do this, use the `acs:SourceIp` condition to create a Deny statement that blocks requests from other IP addresses. Requests from other IP addresses fail because they do not match the specified IP address. This example denies read access to the `example-bucket` bucket for all users except for those with the IP address `203.0.113.5`.


> NOTE:

> NOTE: 


> NOTE: Note 

-

Because the Principal in the following deny policy statement is a wildcard asterisk (`*`) and the statement includes a Condition, this deny policy statement applies to all users, including the bucket owner.

-

This Deny statement only restricts access. It does not grant any permissions. If the principal does not have permissions, you must add an Allow statement to grant access.


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Deny",
    "Action": [
      "oss:GetObject"
    ],
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:174649585760xxxx:example-bucket/*"
    ],
    "Condition": {
      "NotIpAddress": {
        "acs:SourceIp": [
          "203.0.113.5"
        ]
      },
      "StringNotLike": {
        "acs:SourceVpc": [
          "vpc-*"
        ]
      }
    }
  },
    {
      "Effect": "Deny",
      "Action": [
        "oss:GetObject"
      ],
      "Principal": [
        "*"
      ],
      "Resource": [
        "acs:oss:*:174649585760xxxx:example-bucket/*"
      ],
      "Condition": {
        "StringLike": {
          "acs:SourceVpc": [
            "vpc-*"
          ]
        }
      }
    }
  ]
}
`


### Scenario 9: Allow access only from a specific IP range in a specific VPC


You can restrict bucket access to a specific IP range within a specific VPC. To do this, create two Deny statements:


-

Use the `acs:SourceVpc` condition key to create a deny policy statement that blocks requests from other VPCs or the Internet. Requests from other public IP addresses or VPCs do not meet the specified IP condition and therefore trigger the deny rule.

-

Use the `acs:SourceIp` and `acs:SourceVpc` conditions to block requests from outside the specified IP range in the VPC.


A rejection is triggered if either Deny statement is met. This example denies read access to objects in the `example-bucket` bucket for all users except for those in VPC `t4nlw426y44rd3iq4xxxx` with IP addresses in the `192.168.0.0/16` range.


> NOTE:

> NOTE: 


> NOTE: Note 

-

Because the Principal in the following deny policy statement is a wildcard asterisk (`*`) and the statement includes a Condition, this deny policy statement applies to all users, including the bucket owner.

-

This Deny statement only restricts access. It does not grant any permissions. If the principal does not have permissions, you must add an Allow statement to grant access.


`json
{
    "Version":"1",
    "Statement":[
        {
            "Effect":"Deny",
            "Action":[
                "oss:GetObject"
            ],
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition":{
                "StringNotEquals":{
                    "acs:SourceVpc":[
                        "vpc-t4nlw426y44rd3iq4xxxx"
                    ]
                }
            }
        },
        {
            "Effect":"Deny",
            "Action":[
                "oss:GetObject"
            ],
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition":{
                "StringEquals":{
                    "acs:SourceVpc":[
                        "vpc-t4nlw426y44rd3iq4xxxx"
                    ]
                },
                "NotIpAddress":{
                    "acs:SourceIp":[
                        "192.168.0.0/16"
                    ]
                }
            }
        }
    ]
}
`


### Scenario 10: Allow access only from a specific public IP address or a specific VPC


You can restrict bucket access to either a specific public IP address or a specific VPC. To do this, create two Deny statements:


-

Use the `acs:SourceIp` condition to block requests from other public IPs, and use `StringNotLike` with `acs:SourceVpc` to exclude the specified VPC.

-

Use the `acs:SourceVpc` condition to block requests from other VPCs, and use `StringLike` with `acs:SourceVpc` to exclude the specified public IP address. This avoids false denials due to missing VPC IDs.


A rejection is triggered if either Deny statement is met. This example denies read access to objects in the `example-bucket` bucket for all users except for those with the IP address `203.0.113.5` or the VPC ID `t4nlw426y44rd3iq4xxxx`.


> NOTE:

> NOTE: 


> NOTE: Note 

-

Because the Principal in the following deny policy statement is a wildcard asterisk (`*`) and the statement includes a Condition, this deny policy statement applies to all users, including the bucket owner.

-

This Deny statement only restricts access. It does not grant any permissions. If the principal does not have permissions, you must add an Allow statement to grant access.


`json
{
    "Version":"1",
    "Statement":[
        {
            "Effect":"Deny",
            "Action":[
                "oss:GetObject"
            ],
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition":{
                "StringNotLike":{
                    "acs:SourceVpc":[
                        "vpc-*"
                    ]
                },
                "NotIpAddress":{
                    "acs:SourceIp":[
                        "203.0.113.5"
                    ]
                }
            }
        },
        {
            "Effect":"Deny",
            "Action":[
                "oss:GetObject"
            ],
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition":{
                "StringLike":{
                    "acs:SourceVpc":[
                        "vpc-*"
                    ]
                },
                "StringNotEquals":{
                    "acs:SourceVpc":[
                        "vpc-t4nlw426y44rd3iq4xxxx"
                    ]
                }
            }
        }
    ]
}
`


### Scenario 11: Configure an IP blacklist


You can block specific IP addresses or IP address ranges from accessing a bucket and its objects. To do this, use a Deny policy in the bucket policy to reject all requests from the specified IP addresses.


> NOTE:

> NOTE: 


> NOTE: Note 

-

Because the Principal in the following deny policy statement is a wildcard asterisk (`*`) and the statement includes a Condition, this deny policy statement applies to all users, including the bucket owner.

-

You can specify multiple IP addresses or IP address ranges, separated by commas.


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Deny",
    "Action": "oss:*",
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:174649585760xxxx:example-bucket/*",
      "acs:oss:*:174649585760xxxx:example-bucket"
    ],
    "Condition": {
      "IpAddress": {
        "acs:SourceIp": [
          "101.*.*.100"
        ]
      },
      "StringLike": {
        "acs:SourceVpc": [
          "*"
        ]
      }
    }
  }]
}
`


### Scenario 12: Require temporary credentials for API calls


You can require temporary credentials for API access. To do this, use the `acs:AccessId` condition to create a Deny statement that blocks long-term credentials, such as those from an Alibaba Cloud account or RAM user. Requests that use long-term credentials trigger the Deny rule. This example denies all Get and List operations on the `example-bucket` bucket for all users except for those who use temporary credentials that start with `TMP.` or `STS.`.


`json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Deny",
            "Action":[
                "oss:Get*",
                "oss:ListObjects",
                "oss:ListObjectVersions"
            ],
            "Principal":[
                "*"
            ],
            "Resource":[
                "acs:oss:*:174649585760xxxx:example-bucket/*"
            ],
            "Condition": {
                "StringNotLike": {
                    "acs:AccessId": [
                        "TMP.*",
                        "STS.*"
                 ]
                }
            }
        }
    ]
}
`


### Scenario 13: Prevent public ACL settings for buckets and objects


You can prevent public-read or public-read-write Access Control List (ACL) settings for buckets and objects. To do this, create two Deny statements:


-

Use the `oss:x-oss-acl` condition to block bucket ACL settings other than `private`. An attempt to set the ACL to public-read or public-read-write triggers the Deny rule.

-

Use the `oss:x-oss-object-acl` condition to block object ACL settings other than `private` or `default`.


A rejection is triggered if either Deny statement is met. This example denies public ACL settings for the `example-bucket` bucket.


`json
{
    "Version": "1",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "oss:PutBucketAcl"
            ],
            "Principal": [
                "*"
            ],
            "Resource": [
                "acs:oss:*:*:example-bucket"
            ],
            "Condition": {
                "StringNotEquals": {
                    "oss:x-oss-acl": "private"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": [
                "oss:PutObjectAcl"
            ],
            "Principal": [
                "*"
            ],
            "Resource": [
                "acs:oss:*:*:example-bucket/*"
            ],
            "Condition": {
                "StringNotEquals": {
                    "oss:x-oss-object-acl": [
                        "private",
                        "default"
                    ]
                }
            }
        }
    ]
}
`


## Development and tool integration


In addition to configuring policies in the console, you can manage bucket policies using graphical tools, command-line tools, SDKs, or direct API calls.


-

Use ossbrowser


You can perform bucket-level policy operations with a visual interface that is similar to the console. Install and sign in to [ossbrowser](https://www.alibabacloud.com/help/en/oss/developer-reference/installing-the-ossbrowser-2-0), and then follow the on-screen instructions to configure bucket policies.

-

Use ossutil


You can call the [put-bucket-policy](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-policy) operation to configure policies.


> NOTE:

> NOTE: 


> NOTE: Note 

To configure policies for vector buckets, use the `ossutil vectors-api put-bucket-policy` command.


-

Use SDKs


You can configure policies using SDKs for [Java](https://www.alibabacloud.com/help/en/oss/developer-reference/configure-and-manage-bucket-policies), [Python](https://www.alibabacloud.com/help/en/oss/developer-reference/bucket-policy-using-oss-sdk-for-python-v2), [Go](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-bucket-policies), [Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-bucket-policies), and other languages. For more information about SDK options, see [SDK Reference](https://www.alibabacloud.com/help/zh/oss/developer-reference/sdk-code-samples).

-

Call the API directly


You can call the [PutBucketPolicy](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy) operation to configure bucket policies.

## Quotas and limits


-

Policy size: A bucket can have multiple bucket policies. The total size of all policies cannot exceed 16 KB.

-

Field length: Each field in a bucket policy cannot exceed 4095 bytes.

## References


-

[Authentication flow](https://www.alibabacloud.com/help/en/oss/user-guide/authentication)

-

[Policy syntax and elements](https://www.alibabacloud.com/help/en/oss/user-guide/authorization-syntax-and-elements)

-

[Dual access control with VPC and bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/dual-access-control-with-vpc-and-bucket-policy)

-

[Share data across departments using bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/cross-departmental-data-sharing-based-on-bucket-policy)

Thank you! We've received your  feedback.