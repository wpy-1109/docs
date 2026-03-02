# Access OSS by using access points

An access point provides a dedicated entry point for accessing a bucket. When a bucket needs to be accessed by multiple applications or teams with different permissions, you can create a separate access point for each. You can then use an access point policy (AP Policy) to manage permissions for each access point. This avoids the complexity of maintaining intricate permission rules in a single bucket policy.

## How it works


An access point acts as a proxy layer for bucket access. When you create an access point, Object Storage Service (OSS) generates a unique access point alias. Use this alias instead of the bucket name in your requests. Each access point can have its own AP Policy, which defines allowed actions, resources, and identities, and network origin, which can be the Internet or a specified VPC. This enables isolated access based on different business scenarios.


When a user accesses a resource through an access point, the system evaluates the [RAM policy](https://www.alibabacloud.com/help/en/oss/user-guide/ram-policy/), [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/), and AP Policy. A request is allowed only if the combined result of the RAM policy and bucket policy is Allow, and the AP Policy result is also Allow. For more information about the detailed evaluation logic, see [Permission evaluation logic].


By default, an access point cannot access bucket resources. You must first configure permission delegation in the bucket policy. You can use condition keys such as `oss:DataAccessPointArn`, `oss:DataAccessPointAccount`, or `oss:AccessPointNetworkOrigin` to explicitly grant access to the bucket for specific access points.

## Get started


The following three steps guide you through creating an access point, delegating permissions, and using the access point to access resources.

### Step 1: Create an access point


Create an access point and configure its AP Policy. The policy defines which identities can perform what actions on which OSS resources under what conditions.


-

Go to the [Access Points](https://oss.console.alibabacloud.com/access-point) list and click Create Access Point.

-

Enter an Access Point Name, select the associated bucket and network origin, and then click Next.


> NOTE:

> NOTE: 


> NOTE: Note 

-

If you set Network Origin to VPC, you must enter a VPC ID. You can obtain the VPC ID from the [VPC console](https://vpc.console.alibabacloud.com/vpc).

-

The VPC region that you enter must be one of the [regions that support OSS gateway endpoints](https://www.alibabacloud.com/help/en/oss/oss-supported-gateway-endpoint-regions). If the regions do not match, authentication requests cannot be correctly associated with the specified VPC, which causes authentication to fail.


-

Turn off the Block Public Access option and configure the access point policy.

## Add a policy using the visual editor

















-



-







-






-







-



-




| Configuration item | Description |
| --- | --- |
| Applied To | Select whether to grant permissions on the Whole Bucket or Specific Resources. |
| Resource Paths | If you set Applied To to Whole Bucket, the Resource Paths is accesspoint/{access-point-name}/*.If you set Applied To to Specific Resources, enter the folder or individual object to which you want to grant permissions. You can add multiple records. |
| Authorized User | Specify the authorization object.RAM User: Select a RAM user that belongs to the current Alibaba Cloud account.The current logon account must be an Alibaba Cloud account or a RAM user that has management permissions on the bucket and the ListUsers permission in the RAM console. Otherwise, you cannot view the list of RAM users for the current account.Other Account: Enter the UID of another account or RAM user to grant permissions to, or enter a temporary authorized user that starts with arn:sts, such as arn:sts::1798:assumed-role/role-name/session-name. You can grant permissions to multiple users. Enter one user per line. |
| Authorized Operation | Basic Settings: Select a common combination of authorized operations. Options include Read-Only (excluding ListObject), Read-Only (including ListObject), Read/Write, Full Access, and Deny Access.Advanced Settings: Customize the Effect (Allow or Reject) and the authorized Operations. |


## Add a policy using JSON


Enter the authorization policy in JSON format in the editor.
Example policy: Grant read/write permissions to user `20816353761158`.

`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:GetObject",
      "oss:PutObject",
      "oss:GetObjectAcl",
      "oss:PutObjectAcl",
      "oss:ListObjects",
      "oss:AbortMultipartUpload",
      "oss:ListParts",
      "oss:RestoreObject",
      "oss:ListObjectVersions",
      "oss:GetObjectVersion",
      "oss:GetObjectVersionAcl",
      "oss:RestoreObjectVersion"
    ],
    "Principal": [
      "20816353761158"
    ],
    "Resource": [
      "acs:oss:{region-id}:179882766168:accesspoint/{ap-name}/object/*"
    ]
  }, {
    "Effect": "Allow",
    "Action": [
      "oss:ListObjects",
      "oss:GetObject"
    ],
    "Principal": [
      "20816353761158"
    ],
    "Resource": [
      "acs:oss:{region-id}:179882766168:accesspoint/{ap-name}"
    ],
    "Condition": {
      "StringLike": {
        "oss:Prefix": [
          "*"
        ]
      }
    }
  }]
}
`


A complete authorization policy includes Version and Statement.


-

Version: The version of the access policy. The value is fixed at `1` and cannot be changed.

-

Statement: The main body of the policy, which contains one or more specific grant or deny rules. Each statement includes Effect, Action, Principal, Resource, and Condition.
































| Policy element | Description |
| --- | --- |
| Effect | The effect of the policy. Valid values are Allow and Deny. |
| Action | The specific operation to be performed on a resource. You can use the wildcard character *. |
| Principal | The entity to which the policy applies, such as a user, account, or role. |
| Resource | The scope of resources to which the policy applies. |
| Condition | The conditions under which the policy takes effect.If you configure multiple conditions, all conditions must be met (AND relationship) for the policy to take effect. |


For a complete list of authorization elements, see [Authorization syntax and elements](https://www.alibabacloud.com/help/en/oss/user-guide/authorization-syntax-and-elements).

-

Click Submit and wait for the access point to be created.

### Step 2: Delegate permissions to the access point


After you create an access point, you must also delegate permissions to it using a bucket policy. This defines which access points can access the bucket. Three types of permission delegation are available:


-

`oss:DataAccessPointArn`: Delegates access permissions to a specific access point.

-

`oss:DataAccessPointAccount`: Delegates access permissions to all access points under the current Alibaba Cloud account.

-

`oss:AccessPointNetworkOrigin`: Delegates access permissions to all access points from a specified network origin.

## Delegate permissions to a specific access point


-

Go to the [Bucket list](https://oss.console.alibabacloud.com/bucket) and click the target bucket.

-

In the navigation pane on the left, choose Permission Control > Bucket Policy, and then select Add JSON Policy.

-

Click Edit and enter the authorization policy in JSON format in the editor.


> NOTE:

> NOTE: 


> NOTE: Note 

When you configure the policy, replace the UID, bucket name, region ID, and access point name in the example with your actual information. If the bucket policy is not empty, append a new element to the existing `Statement` array.


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:*"
    ],
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:179882766168:example-bucket",
      "acs:oss:*:179882766168:example-bucket/*"
    ],
    "Condition": {
      "StringEquals": {
        "oss:DataAccessPointArn": [
          "acs:oss:oss-{region-id}:179882766168:accesspoint/{ap-name}"
        ]
      }
    }
  }]
}
`


-

Click Save to complete the bucket policy configuration.

## Delegate permissions to all access points


-

Go to the [Bucket list](https://oss.console.alibabacloud.com/bucket) and click the target bucket.

-

In the navigation pane on the left, choose Permission Control > Bucket Policy, and then select Add JSON Policy.

-

Click Edit and enter the authorization policy in JSON format in the editor.


> NOTE:

> NOTE: 


> NOTE: Note 

When you configure the policy, replace the UID and bucket name in the example with your actual information. If the bucket policy is not empty, append a new element to the existing `Statement` array.


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:*"
    ],
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:179882766168:example-bucket",
      "acs:oss:*:179882766168:example-bucket/*"
    ],
    "Condition": {
      "StringEquals": {
        "oss:DataAccessPointAccount": [
          "179882766168"
        ]
      }
    }
  }]
}
`


-

Click Save to complete the bucket policy configuration.

## Delegate permissions based on network origin


-

Go to the [Bucket list](https://oss.console.alibabacloud.com/bucket) and click the target bucket.

-

In the navigation pane on the left, choose Permission Control > Bucket Policy, and then select Add JSON Policy.

-

Click Edit and enter the authorization policy in JSON format in the editor.


> NOTE:

> NOTE: 


> NOTE: Note 

-

When you configure the policy, replace the UID and bucket name in the example with your actual information. If the bucket policy already contains content, append a new element to the existing `Statement` array.

-

When `oss:AccessPointNetworkOrigin` is set to `internet`, permissions are delegated to all access points whose network origin is the Internet. This configuration allows access from both the public network and VPCs. To restrict access to only VPCs, change this value to `vpc`.


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:*"
    ],
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:179882766168:example-bucket",
      "acs:oss:*:179882766168:example-bucket/*"
    ],
    "Condition": {
      "StringEquals": {
        "oss:AccessPointNetworkOrigin": [
          "internet"
        ]
      }
    }
  }]
}
`


-

Click Save to complete the bucket policy configuration.


> NOTE:

> NOTE: 


> NOTE: Note 

If you receive a message indicating that the bucket policy contains public access semantics, first disable the Block Public Access option for the bucket, and then delegate permissions to the access point.


### Step 3: Use the access point to access resources


After you create an access point, OSS automatically generates an access point alias. Use an authorized identity, such as a RAM user, to access the corresponding OSS resources through this alias.


Click to view operations compatible with access points


(https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpolicy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getaccesspointpolicy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteaccesspointpolicy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjects-v2)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listobjectversions)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/copyobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/appendobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deletemultipleobjects)


(https://www.alibabacloud.com/help/en/oss/developer-reference/headobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectmeta)


(https://www.alibabacloud.com/help/en/oss/developer-reference/postobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/restoreobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/selectobject)


(https://www.alibabacloud.com/help/en/oss/developer-reference/initiatemultipartupload)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpart)


(https://www.alibabacloud.com/help/en/oss/developer-reference/uploadpartcopy)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completemultipartupload)


(https://www.alibabacloud.com/help/en/oss/developer-reference/abortmultipartupload)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listmultipartuploads)


(https://www.alibabacloud.com/help/en/oss/developer-reference/listparts)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjectacl)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjectacl)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putsymlink)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getsymlink)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobjecttagging)


(https://www.alibabacloud.com/help/en/oss/developer-reference/getobjecttagging)


(https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobjecttagging)


| Interface | Description |
| --- | --- |
| PutAccessPointPolicy | Configures an access point policy. |
| GetAccessPointPolicy | Obtains the configuration of an access point policy. |
| DeleteAccessPointPolicy | Deletes an access point policy. |
| ListObjects (GetBucket) | Lists information about all objects in a bucket. |
| ListObjectsV2 (GetBucketV2) |
| ListObjectVersions (GetBucketVersions) | Lists all versions of objects in a bucket, including delete markers. |
| PutObject | Uploads an object. |
| GetObject | Obtains an object. |
| CopyObject | Copies an object. |
| AppendObject | Uploads an object by appending data. |
| DeleteObject | Deletes a single object. |
| DeleteMultipleObjects | Deletes multiple objects. |
| HeadObject | Returns all metadata of an object without returning its content. |
| GetObjectMeta | Returns partial metadata of an object, including its ETag, Size, and LastModified, without returning its content. |
| PostObject | Uploads an object using an HTML form. |
| RestoreObject | Restores an object of the Archive Storage, Cold Archive, or Deep Cold Archive storage class. |
| SelectObject | Executes an SQL statement on an object and returns the result. |
| InitiateMultipartUpload | Initializes a multipart upload event. |
| UploadPart | Uploads data in parts based on the specified object name and upload ID. |
| UploadPartCopy | Calls the UploadPartCopy operation by adding the x-oss-copy-source request header to an UploadPart request. This lets you copy data from an existing object to upload a part. |
| CompleteMultipartUpload | After all data parts are uploaded, you must call this operation to complete the multipart upload. |
| AbortMultipartUpload | Cancels a multipart upload event and deletes the corresponding part data. |
| ListMultipartUploads | Lists all multipart upload events that are in progress. These are events that have been initiated but not yet completed or aborted. |
| ListParts | Lists all successfully uploaded parts for a specified upload ID. |
| PutObjectACL | Modifies the access permissions of an object. |
| GetObjectACL | Views the access permissions of an object. |
| PutSymlink | Creates a symbolic link. |
| GetSymlink | Obtains a symbolic link. |
| PutObjectTagging | Sets or updates object tags. |
| GetObjectTagging | Obtains object tag information. |
| DeleteObjectTagging | Deletes specified object tags. |


## SDK


Currently, only Java SDK and Python SDK support accessing OSS resources using access point aliases.
Java

`java
import com.aliyun.sdk.service.oss2.OSSClient;
import com.aliyun.sdk.service.oss2.credentials.CredentialsProvider;
import com.aliyun.sdk.service.oss2.credentials.StaticCredentialsProvider;
import com.aliyun.sdk.service.oss2.models.GetObjectRequest;

import java.io.File;

/
 * OSS Java SDK V2 example: Use an access point to download an object to a local file.
 */
public class DownloadObjectWithAccessPoint {

    public static void main(Stringargs) {
        // Create an OSS client.
        String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID");
        String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET");
        CredentialsProvider provider = new StaticCredentialsProvider(accessKeyId, accessKeySecret);
        OSSClient client = OSSClient.newBuilder()
                .credentialsProvider(provider)
                .region("<region-id>")
                .build();

        // Use the access point alias to download the object to a local file.
        String bucket = "example-ap-b156d01070a10322664d6704cd1d47-ossalias";
        String key = "example.jpg";
        File file = new File("example.jpg");
        client.getObjectToFile(GetObjectRequest.newBuilder()
                .bucket(bucket)
                .key(key)
                .build(), file);
        System.out.println("File downloaded: " + key + " -> " + file.getPath());

        // Close the client.
        try {
            client.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

`

Python

`python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OSS Python SDK V2 example: Use an access point to download an object to a local file."""

import alibabacloud_oss_v2 as oss


def main() -> None:
    """Main function"""
    # Create an OSS client.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()
    config = oss.config.load_default()
    config.credentials_provider = credentials_provider
    config.region = "<region-id>"
    config.endpoint = "oss-<region-id>.aliyuncs.com"
    client = oss.Client(config)

    # Use the access point alias to download the object to a local file.
    bucket = "example-ap-b156d01070a10322664d6704cd1d47-ossalias"
    key = "example.jpg"
    file_path = "example.jpg"
    request = oss.GetObjectRequest(bucket, key)
    client.get_object_to_file(request, file_path)
    print(f"File downloaded: {key} -> {file_path}")


if __name__ == "__main__":
    main()

`


## ossutil


When you use ossutil to access OSS resources, use the access point alias as the bucket name.


`bash
ossutil cp oss://example-ap-b156d01070a10322664d6704cd1d47-ossalias/example.jpg /tmp
`


## REST API


When you use a REST API to access OSS resources, use the access point alias in the Host header. The following example shows the format:


`http
GET /ObjectName HTTP/1.1
Host: example-ap-b156d01070a10322664d6704cd1d47-ossalias.oss-{region-id}.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Example scenario


The following example shows how to design an access point solution for a big data analytics scenario. This solution uses fine-grained access control to achieve secure, isolated access for multiple departments.

### Scenario description


A company (Alibaba Cloud account UID: `137918634953`) stores all collected data in a bucket named `examplebucket`. This bucket needs to be accessed by 10 different business departments with the following requirements:




















| Department | Access scope | Permission requirements | Network origin |
| --- | --- | --- | --- |
| Departments 1–3 | dir1/ folder | Read-only | The Internet |
| Department 4 | Entire bucket | Read/write | The Internet |
| Departments 5–10 | dir2/ folder | Read/write | VPC only |


### Solution design


Based on the business isolation and security boundary requirements, this solution uses three access points for the different access scenarios. AP Policies are used to implement precise permission control and network access restrictions.















































| Access point | Name | Network origin | Authorized user | Authorized resource | Permission |
| --- | --- | --- | --- | --- | --- |
| Access Point 1 | ap-01 | The Internet | RAM users from Departments 1–3 (UID: 26571698800555) | dir1/* | Read-only |
| Access Point 2 | ap-02 | The Internet | RAM user from Department 4 (UID: 25770968794578) | * (entire bucket) | Read/write |
| Access Point 3 | ap-03 | VPC | RAM users from Departments 5–10 (UID: 26806658794579) | dir2/* | Read/write |


### AP Policy configuration

## ap-01 (read-only access for Departments 1–3)


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:GetObject",
      "oss:GetObjectAcl",
      "oss:ListObjects",
      "oss:RestoreObject",
      "oss:ListObjectVersions",
      "oss:GetObjectVersion",
      "oss:GetObjectVersionAcl",
      "oss:RestoreObjectVersion"
    ],
    "Principal": [
      "26571698800555"
    ],
    "Resource": [
      "acs:oss:{region-id}:137918634953:accesspoint/ap-01/object/dir1/*"
    ]
  },{
    "Effect": "Allow",
    "Action": [
      "oss:ListObjects",
      "oss:GetObject"
    ],
    "Principal": [
      "26571698800555"
    ],
    "Resource": [
      "acs:oss:{region-id}:137918634953:accesspoint/ap-01"
    ],
    "Condition": {
      "StringLike": {
        "oss:Prefix": [
          "dir1/*"
        ]
      }
    }
  }]
}
`


## ap-02 (read/write access to the entire bucket for Department 4)


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:GetObject",
      "oss:PutObject",
      "oss:GetObjectAcl",
      "oss:PutObjectAcl",
      "oss:ListObjects",
      "oss:AbortMultipartUpload",
      "oss:ListParts",
      "oss:RestoreObject",
      "oss:ListObjectVersions",
      "oss:GetObjectVersion",
      "oss:GetObjectVersionAcl",
      "oss:RestoreObjectVersion"
    ],
    "Principal": [
      "25770968794578"
    ],
    "Resource": [
      "acs:oss:{region-id}:137918634953:accesspoint/ap-02/object/*"
    ]
  },{
    "Effect": "Allow",
    "Action": [
      "oss:ListObjects",
      "oss:GetObject"
    ],
    "Principal": [
      "25770968794578"
    ],
    "Resource": [
      "acs:oss:{region-id}:137918634953:accesspoint/ap-02"
    ],
    "Condition": {
      "StringLike": {
        "oss:Prefix": [
          "*"
        ]
      }
    }
  }]
}
`


## ap-03 (read/write access through VPC for Departments 5–10)


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:GetObject",
      "oss:PutObject",
      "oss:GetObjectAcl",
      "oss:PutObjectAcl",
      "oss:ListObjects",
      "oss:AbortMultipartUpload",
      "oss:ListParts",
      "oss:RestoreObject",
      "oss:ListObjectVersions",
      "oss:GetObjectVersion",
      "oss:GetObjectVersionAcl",
      "oss:RestoreObjectVersion"
    ],
    "Principal": [
      "26806658794579"
    ],
    "Resource": [
      "acs:oss:{region-id}:137918634953:accesspoint/ap-03/object/dir2/*"
    ]
  },{
    "Effect": "Allow",
    "Action": [
      "oss:ListObjects",
      "oss:GetObject"
    ],
    "Principal": [
      "26806658794579"
    ],
    "Resource": [
      "acs:oss:{region-id}:137918634953:accesspoint/ap-03"
    ],
    "Condition": {
      "StringLike": {
        "oss:Prefix": [
          "dir2/*"
        ]
      }
    }
  }]
}
`


### Bucket Policy permission delegation


Because this scenario involves multiple access points under the same account, we recommend using `oss:DataAccessPointAccount` for unified delegation to simplify the bucket policy configuration. For more fine-grained control, you can also use `oss:DataAccessPointArn` to delegate permissions for each access point individually.

## Unified delegation


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:*"
    ],
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:137918634953:examplebucket",
      "acs:oss:*:137918634953:examplebucket/*"
    ],
    "Condition": {
      "StringEquals": {
        "oss:DataAccessPointAccount": [
          "137918634953"
        ]
      }
    }
  }]
}
`


## Individual delegation


`json
{
  "Version": "1",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "oss:*"
    ],
    "Principal": [
      "*"
    ],
    "Resource": [
      "acs:oss:*:137918634953:examplebucket",
      "acs:oss:*:137918634953:examplebucket/*"
    ],
    "Condition": {
      "StringEquals": {
        "oss:DataAccessPointArn": [
          "acs:oss:oss-{region-id}:137918634953:accesspoint/ap-01",
          "acs:oss:oss-{region-id}:137918634953:accesspoint/ap-02",
          "acs:oss:oss-{region-id}:137918634953:accesspoint/ap-03"
        ]
      }
    }
  }]
}
`


## Permission evaluation logic











| Combined result of RAM Policy and Bucket Policy | AP Policy result | Final result |
| --- | --- | --- |
| Allow | Allow | Allow |
| Allow | Deny | Deny |
| Allow | Ignore | Ignore |
| Deny | Allow | Deny |
| Deny | Deny | Deny |
| Deny | Ignore | Deny |
| Ignore | Allow | Ignore |
| Ignore | Deny | Deny |
| Ignore | Ignore | Ignore |


-

Allow: The access request matches an Allow statement in the access policy and does not match any Deny statements.

-

Deny (explicit deny): The access request matches a Deny statement in the access policy. Even if it also matches an Allow statement, the result is an explicit deny due to the deny precedence principle.

-

Ignore (implicit deny): The access request does not match any Allow or Deny statements. By default, a RAM identity has no permissions. Operations that are not explicitly allowed are implicitly denied.

## Quotas and limits


-


-


| Limitations | Description |
| --- | --- |
| Creation methods | You can create access points using the OSS console, API, or ossutil. You cannot create access points using SDKs. |
| Quantity | You can create up to 1,000 access points within a single Alibaba Cloud account.You can create up to 100 access points for a single bucket. |
| Modification rules | After an access point is created, you can only modify its access point policy. You cannot modify its basic information, such as the access point name or alias. |
| Access methods | Anonymous access is not supported. |


## FAQ

#### Do access point permissions support IP address whitelists?


Yes. You can add an access point policy using JSON and include a condition such as `"IpAddress": {"acs:SourceIp": ["xxx"]}` to restrict access.

#### What permissions are required for a RAM user to create an access point?


The following permissions are required: `oss:CreateAccessPoint`, `oss:GetAccessPoint`, `oss:DeleteAccessPoint`, `oss:ListAccessPoints`, `oss:PutAccessPointPolicy`, `oss:GetAccessPointPolicy`, `oss:DeleteAccessPointPolicy`, `oss:PutBucketPolicy`, `oss:GetBucketPolicy`, and `oss:DeleteBucketPolicy`.

## References


-

[CreateAccessPoint](https://www.alibabacloud.com/help/en/oss/developer-reference/createaccesspoint), [PutAccessPointPolicy](https://www.alibabacloud.com/help/en/oss/developer-reference/putaccesspointpolicy), and [PutBucketPolicy](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketpolicy)

-

[Authorization syntax and elements](https://www.alibabacloud.com/help/en/oss/user-guide/authorization-syntax-and-elements)

-

[RAM Policy](https://www.alibabacloud.com/help/en/oss/user-guide/ram-policy/)

-

[Bucket Policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/)

Thank you! We've received your  feedback.