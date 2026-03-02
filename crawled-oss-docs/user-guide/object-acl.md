# Set object ACLs to control access permissions for individual files

An object access control list (ACL) is a feature of Object Storage Service (OSS) that controls access at the object level. You can use an object ACL to set specific read/write permissions for an individual object, independent of the bucket's permissions.

## How it works


Object ACLs control access to individual objects using predefined permissions. OSS supports four types of permissions:











| Permission value | Description |
| --- | --- |
| default | Inherits the bucket ACL. The object's read/write permissions are the same as its bucket's. |
| private | Private. Only the object owner or authorized users can read or write the object. Other users cannot access it. |
| public-read | Public read. Only the object owner or authorized users can write to the object. Anyone, including anonymous users, can read it. |
| public-read-write | Public read-write. Anyone, including anonymous users, can read and write the object. |


Object ACLs have a higher priority than bucket ACLs. When an object's ACL is set to a value other than default, the system enforces access control based on the object ACL. For example, if an object's ACL is set to public-read, the object can be accessed anonymously, regardless of the bucket's ACL.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

-

public-read-write: Any user on the Internet can access and write to the object. This can lead to data leaks, increased costs, or the writing of malicious or illegal information. Do not configure this permission except for specific scenarios.

-

public-read: Any user on the Internet can access the object. This can lead to data leaks and increased costs. Use this permission with caution.


## Set an object ACL


When you create a bucket, [Block Public Access](https://www.alibabacloud.com/help/en/oss/user-guide/block-public-access) is enabled by default. The object ACL can only be set to private or default. To set the ACL to public-read or public-read-write, you must first disable Block Public Access.

## Console


-

Go to the [Bucket List](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the Actions column of the object file, click Details, and then click Set ACL.

-

Set the ACL (Access Control List) as needed, and then click OK.

## ossutil command line interface


You can use the [put-object-acl](https://www.alibabacloud.com/help/en/oss/developer-reference/put-object-acl) command of [ossutil V2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/#DAS) to set an object ACL.


`bash
ossutil api put-object-acl --bucket examplebucket --key exampleobject --acl private
`


## SDK


The following code provides examples of how to set an object ACL using common SDKs. For code examples for other SDKs, see the SDK Reference.
Java

`java
// This example shows how to set the access control list (ACL) for an object.
// Before you start, configure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables.

import com.aliyun.sdk.service.oss2.OSSClient;
import com.aliyun.sdk.service.oss2.credentials.CredentialsProvider;
import com.aliyun.sdk.service.oss2.credentials.StaticCredentialsProvider;
import com.aliyun.sdk.service.oss2.models.*;

public class SetObjectAcl {

    public static void main(Stringargs) {
        String bucketName = "example-bucket";
        String objectName = "example.txt";

        String accessKeyId = System.getenv("OSS_ACCESS_KEY_ID");
        String accessKeySecret = System.getenv("OSS_ACCESS_KEY_SECRET");
        CredentialsProvider provider = new StaticCredentialsProvider(accessKeyId, accessKeySecret);

        try (OSSClient client = OSSClient.newBuilder()
                .credentialsProvider(provider)
                .region("<region-id>")
                .build()) {

            // Set the object ACL to private.
            // Valid values: "private", "public-read", "public-read-write", and "default".
            PutObjectAclRequest putRequest = PutObjectAclRequest.newBuilder()
                    .bucket(bucketName)
                    .key(objectName)
                    .objectAcl("private")
                    .build();
            PutObjectAclResult putResult = client.putObjectAcl(putRequest);
            System.out.println("Object ACL set successfully. RequestId: " + putResult.requestId());

            // Get the object ACL.
            GetObjectAclRequest getRequest = GetObjectAclRequest.newBuilder()
                    .bucket(bucketName)
                    .key(objectName)
                    .build();
            GetObjectAclResult getResult = client.getObjectAcl(getRequest);
            System.out.println("Current Object ACL: " + getResult.accessControlPolicy().accessControlList().grant());

        } catch (Exception e) {
            System.err.println("Operation failed: " + e.getMessage());
        }
    }
}

`

Python

`python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This example shows how to set the access control list (ACL) for an object.
# Before you start, configure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables.

import alibabacloud_oss_v2 as oss


def main() -> None:
    bucket_name = "example-bucket"
    object_name = "example.txt"

    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = "<region-id>"

    client = oss.Client(cfg)

    # Set the object ACL to private.
    # Valid values: "private", "public-read", "public-read-write", and "default".
    put_result = client.put_object_acl(oss.PutObjectAclRequest(
        bucket=bucket_name,
        key=object_name,
        acl="private"
    ))
    print(f"Object ACL set successfully. RequestId: {put_result.request_id}")

    # Get the object ACL.
    get_result = client.get_object_acl(oss.GetObjectAclRequest(
        bucket=bucket_name,
        key=object_name
    ))
    print(f"Current Object ACL: {get_result.acl}")


if __name__ == "__main__":
    main()

`

Go

`go
// This example shows how to set the access control list (ACL) for an object.
// Before you start, configure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables.

package main

import (
	"context"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

func main() {
	bucketName := "example-bucket"
	objectName := "example.txt"

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion("<region-id>")

	client := oss.NewClient(cfg)

	// Set the object ACL to private.
	// Valid values: oss.ObjectACLPrivate, oss.ObjectACLPublicRead, oss.ObjectACLPublicReadWrite, and oss.ObjectACLDefault.
	putResult, err := client.PutObjectAcl(context.TODO(), &oss.PutObjectAclRequest{
		Bucket: oss.Ptr(bucketName),
		Key:    oss.Ptr(objectName),
		Acl:    oss.ObjectACLPrivate,
	})
	if err != nil {
		log.Fatalf("Failed to set object ACL: %v", err)
	}
	log.Printf("Object ACL set successfully. RequestId: %s", putResult.Headers.Get("X-Oss-Request-Id"))

	// Get the object ACL.
	getResult, err := client.GetObjectAcl(context.TODO(), &oss.GetObjectAclRequest{
		Bucket: oss.Ptr(bucketName),
		Key:    oss.Ptr(objectName),
	})
	if err != nil {
		log.Fatalf("Failed to get object ACL: %v", err)
	}
	log.Printf("Current Object ACL: %s", *getResult.ACL)
}

`

PHP

`php
<?php
// This example shows how to set the access control list (ACL) for an object.
// Before you start, configure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables.

require_once __DIR__ . '/vendor/autoload.php';

use AlibabaCloud\Oss\V2 as Oss;

$bucketName = 'example-bucket';
$objectName = 'example.txt';

$credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider();

$cfg = Oss\Config::loadDefault();
$cfg->setCredentialsProvider($credentialsProvider);
$cfg->setRegion('<region-id>');

$client = new Oss\Client($cfg);

try {
    // Set the object ACL to private.
    // Valid values: ObjectACLType::PRIVATE, ObjectACLType::PUBLIC_READ, ObjectACLType::PUBLIC_READ_WRITE, and ObjectACLType::DEFAULT.
    $putResult = $client->putObjectAcl(new Oss\Models\PutObjectAclRequest(
        bucket: $bucketName,
        key: $objectName,
        acl: Oss\Models\ObjectACLType::PRIVATE
    ));
    printf("Object ACL set successfully. RequestId: %s\n", $putResult->requestId);

    // Get the object ACL.
    $getResult = $client->getObjectAcl(new Oss\Models\GetObjectAclRequest(
        bucket: $bucketName,
        key: $objectName
    ));
    printf("Current Object ACL: %s\n", $getResult->accessControlList->grant);
} catch (Exception $e) {
    printf("Operation failed: %s\n", $e->getMessage());
}

`

C#

`csharp
// This example shows how to set the access control list (ACL) for an object.
// Before you start, configure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables.

using OSS = AlibabaCloud.OSS.V2;

var bucketName = "example-bucket";
var objectName = "example.txt";
var region = "<region-id>";

var cfg = OSS.Configuration.LoadDefault();
cfg.CredentialsProvider = new OSS.Credentials.EnvironmentVariableCredentialsProvider();
cfg.Region = region;

using var client = new OSS.Client(cfg);

try
{
    // Set the object ACL to private.
    // Valid values: "private", "public-read", "public-read-write", and "default".
    var putResult = await client.PutObjectAclAsync(new OSS.Models.PutObjectAclRequest()
    {
        Bucket = bucketName,
        Key = objectName,
        Acl = "private"
    });
    Console.WriteLine($"Object ACL set successfully. RequestId: {putResult.RequestId}");

    // Get the object ACL.
    var getResult = await client.GetObjectAclAsync(new OSS.Models.GetObjectAclRequest()
    {
        Bucket = bucketName,
        Key = objectName
    });
    Console.WriteLine($"Current Object ACL: {getResult.AccessControlPolicy?.AccessControlList?.Grant}");
}
catch (Exception ex)
{
    Console.WriteLine($"Operation failed: {ex.Message}");
}

`

Node.js

`nodejs
// This example shows how to set the access control list (ACL) for an object.
// Before you start, configure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables.

const OSS = require('ali-oss');

async function main() {
    const bucketName = 'example-bucket';
    const objectName = 'example.txt';

    const client = new OSS({
        region: 'oss-<region-id>',
        accessKeyId: process.env.OSS_ACCESS_KEY_ID,
        accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
        bucket: bucketName,
        authorizationV4: true,
    });

    try {
        // Set the object ACL to private.
        // Valid values: 'private', 'public-read', 'public-read-write', 'default'
        await client.putACL(objectName, 'private');
        console.log('Object ACL set successfully');

        // Get the object ACL.
        const result = await client.getACL(objectName);
        console.log(`Current Object ACL: ${result.acl}`);
    } catch (err) {
        console.error('Operation failed:', err.message);
    }
}

main();

`


## FAQ

#### How do I temporarily share a private object with other users?


You can generate a [signed URL](https://www.alibabacloud.com/help/en/oss/user-guide/how-to-obtain-the-url-of-a-single-object-or-the-urls-of-multiple-objects) and share it with other users. This allows them to access the private object for a specified period without changing the object ACL.

## References


-

If your scenario requires extensive customization, you can make REST API requests directly. Note that you must manually write code to calculate the signature when you make direct REST API requests. For more information, see [PutObjectACL](https://www.alibabacloud.com/help/en/oss/developer-reference/putobjectacl#reference-fs3-gfw-wdb).

-

To grant long-term, fine-grained permissions to other users, such as read-only or write-only permissions on files with a specified prefix in a bucket, you can use a [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/) or a [RAM policy](https://www.alibabacloud.com/help/en/oss/user-guide/ram-policy/).

-

To temporarily grant fine-grained permissions to other users, you can use Security Token Service (STS) temporary authorization. For more information, see [Use STS temporary access credentials to access OSS](https://www.alibabacloud.com/help/en/oss/developer-reference/use-temporary-access-credentials-provided-by-sts-to-access-oss).

Thank you! We've received your  feedback.