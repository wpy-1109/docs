# Grant the same permissions on multiple buckets by using a resource group

A resource group is a resource-based access control method. You can add the buckets to which you want to grant the same permissions to the same resource group and then grant permissions to the resource group. This improves the efficiency of authorization.

## Background information


Enterprise users may create multiple Alibaba Cloud accounts to isolate resources for different projects, subsidiaries, and departments. However, this makes it difficult for enterprise users to manage, monitor, and audit the resources that reside in these Alibaba Cloud accounts in a centralized manner.


![account](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/6023421761/p268036.png)


Object Storage Service (OSS) allows users to create resource groups to classify resources in an Alibaba Cloud account based on business scenarios. This way, the users within an enterprise can use resource groups to efficiently manage resources in their projects.


![rg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/6023421761/p268039.png)

## Notes


-

A resource group can contain buckets in different regions. A bucket can belong only to one resource group.

-

Buckets can be transferred only between resource groups that are created by the same owner.

## Methods

### Use the OSS console


In the following example, test data of different departments in your company is stored in 20 buckets. You want to allow all your employees to write and read data stored in 10 of the buckets and only read data stored in other 10 buckets. If you do not use resource groups, you must separately configure required permissions for each bucket. If you use resource groups, you can add buckets that require the same permissions to a resource group and configure the required permissions for the resource group.


You also need to create user groups to grant the same permissions to multiple RAM users (your employees). A user group functions similarly to a resource group.


-

Create a user group and add RAM users to the user group.


Create a user group and name the group UserGroup1 in the [RAM console](https://ram.console.alibabacloud.com/). For more information, see [Create a RAM user group](https://www.alibabacloud.com/help/en/ram/user-guide/create-a-user-group#task-187540). After you create the user group, add all the RAM users that need to access data in your buckets to the user group. For more information, see [Add a RAM user to a RAM user group](https://www.alibabacloud.com/help/en/ram/user-guide/add-a-ram-user-to-a-ram-user-group#task-187540).

-

Create resource groups.


-

Log on to the [Resource Management console](https://resourcemanager.console.alibabacloud.com/).

-

In the left-side navigation pane, choose Resource Group > Resource Group.

-

On the Resource Group page, click Create Resource Group.

-

In the Create Resource Group panel, configure the Resource Group Name and Resource Group Identifier parameters. In this example, Resource Group Name is set to ResourcegroupA and Resource Group Identifier is set to Group1.

-

Click OK.


The status of the resource group becomes Creating. Wait for approximately 3 seconds and click the ![资源组_刷新列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5064812261/p80945.png) icon. If the status of the resource group becomes Available, ResourcegroupA is created.

-

Repeat the preceding steps to create a resource group named ResourcegroupB.

-

Select resource groups for your buckets.


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

Click Buckets, and then click the examplebucket1 bucket.

-

Choose Bucket Settings > Resource Group.

-

On the Resource Group page, click Settings.

-

Select ResourcegroupA for Resource Group and click Save.

-

Repeat the preceding steps to select ResourcegroupA for the buckets that you want to authorize all your employees only to read and select ResourcegroupB for the buckets that you want to authorize all your employees to read and write.

-

Configure the required permissions to access resource groups.


-

Log on to the Resource Management console. In the left-side navigation pane, choose Resource Group > Resource Group.

-

Find the resource group in the list and click Manage Permission in the Actions column.

-

On the Permissions tab, click Grant Permission.

-

In the Grant Permission panel, configure the parameters. The following table describes the parameters.














| Parameter | Description |
| --- | --- |
| Authorized Scope | Select Specific Resource Group. Then, select ResourcegroupA from the drop-down list. |
| Principal | Enter UserGroup1. |
| Select Policy | Select System Policy. In the Authorization Policy Name column, click AliyunOSSReadOnlyAccess to authorize RAM users in UserGroup1 to only read objects in buckets in ResourcegroupA. |


-

Click OK.

-

Click Complete.

-

Repeat the preceding steps to attach the `AliyunOSSFullAccess` policy to RAM users in UserGroup1 to authorize the RAM users to read and write objects in buckets in ResourcegroupB.

### Use OSS SDKs


Only OSS SDKs for Java, Python and Go can be used to configure resource groups. For more information, see [Overview](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-21#concept-dcn-tp1-kfb).
Java

`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.SetBucketResourceGroupRequest;

public class Demo {
    public static void main(Stringargs) throws Throwable {
        // In this example, the endpoint of the China (Hangzhou) region is used. Specify your actual endpoint.
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        // Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the name of the bucket. Example: examplebucket.
        String bucketName = "examplebucket";
        // Specify the ID of the resource group. If you do not specify a resource group ID, the bucket belongs to the default resource group.
        String rgId = "rg-aekz";
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Create an OSSClient instance.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
        .endpoint(endpoint)
        .credentialsProvider(credentialsProvider)
        .clientConfiguration(clientBuilderConfiguration)
        .region(region)
        .build();

        try {
            // Create a setBucketResourceGroupRequest object.
            SetBucketResourceGroupRequest setBucketResourceGroupRequest = new SetBucketResourceGroupRequest(bucketName,rgId);
            // Configure the resource group to which the bucket belongs.
            ossClient.setBucketResourceGroup(setBucketResourceGroupRequest);
        } catch (OSSException oe) {
            System.out.println("Caught an OSSException, which means your request made it to OSS, "
                    + "but was rejected with an error response for some reason.");
            System.out.println("Error Message:" + oe.getErrorMessage());
            System.out.println("Error Code:" + oe.getErrorCode());
            System.out.println("Request ID:" + oe.getRequestId());
            System.out.println("Host ID:" + oe.getHostId());
        } catch (ClientException ce) {
            System.out.println("Caught an ClientException, which means the client encountered "
                    + "a serious internal problem while trying to communicate with OSS, "
                    + "such as not being able to access the network.");
            System.out.println("Error Message:" + ce.getMessage());
        } finally {
            if (ossClient != null) {
                ossClient.shutdown();
            }
        }
    }
}
`

Go

`go
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

// Specify the global variables.
var (
	region     string // The region in which the bucket is located.
	bucketName string // The name of the bucket.
)

// Specify the init function used to initialize command line parameters.
func init() {
	flag.StringVar(&region, "region", "", "The region in which the bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.")
}

func main() {
	// Parse command line parameters.
	flag.Parse()

	// Specify the ID of the resource group. If you do not specify a resource group ID, the bucket belongs to the default resource group.
	var groupId string = "rg-aekz"

	// Check whether the bucket name is empty.
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	// Check whether the region is empty.
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	// Load the default configurations and specify the credential provider and region.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region)

	// Create an OSSClient instance.
	client := oss.NewClient(cfg)

	// Create a request to configure the resource group for the bucket.
	request := &oss.PutBucketResourceGroupRequest{
		Bucket: oss.Ptr(bucketName), // The name of the bucket.
		BucketResourceGroupConfiguration: &oss.BucketResourceGroupConfiguration{
			ResourceGroupId: oss.Ptr(groupId),
		},
	}

	// Execute the request to configure the resource group for the bucket.
	result, err := client.PutBucketResourceGroup(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put bucket resource group %v", err)
	}

	// Display the result of the request.
	log.Printf("put bucket resource group result:%#v\n", result)
}

`

Python

`python
import argparse
import alibabacloud_oss_v2 as oss

# Create a command line argument parser and describe the purpose of the script: configure the resource group for a bucket.
parser = argparse.ArgumentParser(description="put bucket resource group sample")

# Define the command-line arguments, including the required parameters - region and bucket name - as well as the optional parameters - endpoint and resource group ID.
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--resource_group_id',
                    help='The ID of the resource group to which the bucket belongs. (Optional, default is an empty string)',
                    default='')

def main():
    # Parse command line arguments to obtain the values entered.
    args = parser.parse_args()

    # Load access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Use the default configuration to create a cfg object and specify the credential provider.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider

    # Set the region attribute of the cfg object to the region provided in the command line.
    cfg.region = args.region

    # If a custom endpoint is provided, update the endpoint attribute of the cfg object with the provided endpoint.
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    # Use the preceding settings to initialize the OSSClient instance.
    client = oss.Client(cfg)

    # Send a request to configure the resource group for the specified bucket.
    result = client.put_bucket_resource_group(oss.PutBucketResourceGroupRequest(
            bucket=args.bucket,  # Name of the bucket.
            bucket_resource_group_configuration=oss.BucketResourceGroupConfiguration(
                resource_group_id=args.resource_group_id,  # Resource group ID.
            ),
    ))

    # Display the HTTP status code of the operation and request ID to check the request status.
    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
          )

# Call the main function to start the processing logic when the script is directly run.
if __name__ == "__main__":
    main()  # Entry point of the script. The control flow starts here.
`


### Use ossutil


You can use ossutil to configure resource groups. For information about its installation, see [Install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2#DAS).


Run the following command to configure a resource group whose ID is `rg-123` for `examplebucket`.


`bash
ossutil api put-bucket-resource-group --bucket examplebucket --resource-group-configuration "{\"ResourceGroupId\":\"rg-123\"}"
`


For more information about this command, see [put-bucket-resource-group](https://www.alibabacloud.com/help/en/oss/developer-reference/put-bucket-resource-group).

## Related API operation


The methods described above are fundamentally implemented based on the RESTful API, which you can directly call if your business requires a high level of customization. To directly call an API, you must include the signature calculation in your code. For more information, see [PutBucketResourceGroup](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketresourcegroup#concept-2075804).

Thank you! We've received your  feedback.