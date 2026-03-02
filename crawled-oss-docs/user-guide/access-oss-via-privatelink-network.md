# Access OSS over PrivateLink

PrivateLink establishes a secure, private connection between your Virtual Private Cloud (VPC) and Object Storage Service (OSS). This connection provides native network-layer traffic isolation, which mitigates security risks, prevents IP address conflicts, and simplifies network management. This helps you build a secure and manageable access architecture for your cloud storage.

## How it works


PrivateLink works by creating a dedicated private endpoint in your VPC that connects to OSS. This ensures that all access traffic remains within the Alibaba Cloud backbone network and is never exposed to the public internet. It also provides precise access control based on source IP addresses and VPC flow log auditing, helping you build an enterprise-grade data security system. Compared to the default internal endpoints that OSS provides, PrivateLink offers a higher level of native network security isolation and fine-grained control, making it ideal for these use cases:



































| Use case | Internal endpoint | PrivateLink |
| --- | --- | --- |
| Strict security and compliance requirements | Access is through a shared internal endpoint, exposing an attack surface within the cloud provider's network. Security control relies mainly on application-layer policies. | Reduces the attack surface. The endpoint is located inside your VPC, so other VPCs cannot discover or access it. Traffic is natively isolated at the network layer. |
| Fine-grained, network-level access control | You cannot use security groups to control access to OSS. Access control relies on a bucket policy. | Supports security groups. Add security group rules to the PrivateLink endpoint to precisely control which source IP addresses can access OSS. |
| Auditing of all network connection attempts | OSS access logs record only successful requests. They cannot be used to audit denied connection attempts at the network layer. | Supports VPC flow logs. Capture and audit all traffic that attempts to access the endpoint, whether successful or not. |
| Complex hybrid cloud network with potential IP conflicts | Alibaba Cloud services use the 100.64.0.0/10 CIDR block by default. This may conflict with the IP address scheme of your on-premises data center. | Avoids IP address conflicts. The endpoint uses an IP address from your VPC's CIDR block. This aligns with your custom IP plan and simplifies hybrid cloud routing configurations. |


## Supported regions


Japan (Tokyo), Indonesia (Jakarta), Thailand (Bangkok), Germany (Frankfurt), US (Silicon Valley), US (Virginia).


> NOTE:

> NOTE: 


> NOTE: Note 

To use this service, you must request activation from [technical support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex).


## Configure and use PrivateLink


Create an endpoint to establish a PrivateLink connection to securely access OSS resources from a VPC or an on-premises data center.

### Create and verify an endpoint


First, create an endpoint to establish a secure, private connection between your VPC and OSS. After creating the endpoint, use an ECS instance to verify its network connectivity and ability to access OSS.
Before you begin, ensure that you have [created a VPC and a vSwitch](https://www.alibabacloud.com/help/en/vpc/user-guide/create-and-manage-a-vpc#section-znz-rbv-vrx). The verification step requires an ECS instance. If you do not have an existing instance, see [Purchase an ECS instance](https://www.alibabacloud.com/help/en/ecs/user-guide/create-an-instance-by-using-the-wizard) to create a pay-as-you-go instance.
#### Step 1: Create an endpoint


-

Go to the [VPC Endpoints](https://vpc.console.alibabacloud.com/endpoint) page and click Create Endpoint. If this is your first time, follow the on-screen instructions to activate the PrivateLink service.

-

Configure the following parameters. Keep the default values for any unlisted parameters.


-

Region: Select the region of the target OSS bucket.

-

Endpoint Name: Enter a descriptive name for the endpoint, such as `privatelink-oss`.

-

Endpoint Type: Select Interface Endpoint.

-

Endpoint Service: Select Alibaba Cloud Service. In the service list, select the OSS endpoint service. The service name ends with `oss`.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8321170671/p1013663.png)

-

VPC: Select the target VPC where you want to create the endpoint. If no VPC is available, click Create VPC.

-

Security Groups: Select a security group to attach to the endpoint. The security group controls access permissions. If no suitable security group is available, click Create Security Group.

-

Zone and vSwitch: Select the zone where the endpoint will be deployed and the corresponding vSwitch. If no vSwitch is available, click Create vSwitch.

-

Click OK. The system automatically creates the endpoint. After creation, go to the endpoint details page to view and copy the Domain Name of Endpoint Service. You will use this domain name for subsequent access to OSS.


![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3972550671/p1013664.png)

#### Step 2: Verify endpoint connectivity


Verify the endpoint configuration by testing network connectivity and downloading a file from OSS. This ensures that the PrivateLink connection is working correctly.


-

Verify network connectivity


Use the `ping` command to test the network connectivity of the endpoint domain name. This verifies that DNS resolution and the network path are working.


`shell
ping -c 4 ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com
`


-

Verify file download


Use the ossutil tool on an ECS instance in the same region to download a file from OSS. This verifies that data can be transferred through the connection.


-

[Install and configure ossutil 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/).

-

Use the endpoint domain name, such as `ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com`, to access OSS resources. The following example shows how to download a file named `dest.jpg` from a bucket named `example-bucket`:


`shell
ossutil cp oss://example-bucket/dest.jpg /tmp/ -e ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com --addressing-style path
`


A successful command displays the following output, indicating the download is complete. Find the downloaded file in the `/tmp` directory.


`shell
Success: Total 1 object, size 134102 B, Download done:(1 files, 134102 B), avg 680.112 KiB/s

0.193189(s) elapsed
`


### Enhance security for VPC access


To further enhance security after verifying that PrivateLink is working, configure a [bucket policy](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/). The following example shows how to restrict access to the objects so that they can only be accessed from the VPC associated with the PrivateLink connection. This configuration provides access control at both the network and application layers.


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the navigation pane on the left, choose Permission Control > Bucket Policy.

-

Click Authorize and configure the following parameters. Keep the default values for other parameters.


-

Authorized User: Select All Accounts (*).

-

Authorized Operation: Select Advanced Settings.

-

Effect: Select Reject.

-

Actions: Select oss:GetObject.

-

Condition: Select VPC ≠ and select the VPC attached to the PrivateLink endpoint.

-

Click OK to save the bucket policy.

### Access from on-premises devices using an SSL-VPN


An SSL-VPN solution provides fast and flexible VPC access for individual on-premises devices, such as a developer's workstation or a mobile device. After you deploy an SSL-VPN Gateway in your VPC, a device can establish an encrypted tunnel and then use the configured PrivateLink endpoint to securely access OSS. This method is ideal for remote work, development and testing, and emergency access.

#### Step 1: Create an SSL-VPN gateway and configure the client


To establish an encrypted connection between your on-premises device and the VPC, deploy an SSL-VPN Gateway and complete the client configuration. For more information, see [Access a VPC from a client over an SSL-VPN connection](https://www.alibabacloud.com/help/en/vpn/sub-product-ssl-vpn/getting-started/connect-a-client-to-a-vpc).

#### Step 2: Verify PrivateLink access to OSS


To ensure the private access path is working correctly, verify the PrivateLink connection by testing connectivity and downloading a file from your on-premises device.


-

Verify connectivity


Use the `ping` command to test the network connectivity of the endpoint domain name. This verifies that DNS resolution and the network path are working.


`shell
ping -c 4 ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com
`


-

Verify file download

## ossutil


On your on-premises device, use ossutil to perform a file operation in OSS. This verifies the functionality and data transfer stability of the PrivateLink connection.


-

[Install and configure ossutil 2.0](https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/).

-

Use the endpoint domain name, such as `ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com`, to access OSS resources. The following example shows how to download a file named `dest.jpg` from a bucket named `example-bucket`:


`shell
ossutil cp oss://example-bucket/dest.jpg /tmp/ -e ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com --addressing-style path
`


A successful command displays the following output, indicating the download is complete. Find the downloaded file in the `/tmp` directory.


`shell
Success: Total 1 object, size 134102 B, Download done:(1 files, 134102 B), avg 680.112 KiB/s

0.193189(s) elapsed
`


## SDK


Using an SDK more closely simulates a real production environment. It supports complex business logic integration and exception handling. The following SDKs support accessing OSS over PrivateLink.

#### Java


When accessing over PrivateLink, use `setSLDEnabled(true)` to enable path-style access. When accessing over the public internet, set it to `setSLDEnabled(false)`.


`java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;
import com.aliyun.oss.model.GetObjectRequest;
import java.io.File;

/
 * OSS PrivateLink Access Demo.
 * This demo shows how to access OSS and download a file over PrivateLink.
 */
public class Test {

    public static void main(Stringargs) throws Exception {
        // The PrivateLink endpoint domain name.
        String endpoint = "https://ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com";

        // Specify the region that corresponds to the endpoint, for example, cn-hangzhou.
        String region = "cn-hangzhou";

        // Obtain access credentials from environment variables.
        // Before you run this code, make sure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
        EnvironmentVariableCredentialsProvider credentialsProvider =
                CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();

        // Specify the bucket name, for example, example-bucket.
        String bucketName = "example-bucket";

        // Specify the full path of the object, not including the bucket name.
        String objectName = "dest.jpg";

        // The name of the local file to save.
        String pathName = "dest.jpg";

        // Configure client parameters.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();

        // Enable path-style access for PrivateLink. Set this to false when accessing through the bucket's public endpoint.
        clientBuilderConfiguration.setSLDEnabled(true);

        // Explicitly declare the use of the V4 signature algorithm.
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);

        // Create an OSS client instance.
        OSS ossClient = OSSClientBuilder.create()
                .endpoint(endpoint)
                .credentialsProvider(credentialsProvider)
                .clientConfiguration(clientBuilderConfiguration)
                .region(region)
                .build();

        try {
            // Download the object to a local file and save it to the specified local path.
            // If the local file exists, it is overwritten. If it does not exist, it is created.
            // If no local path is specified, the downloaded file is saved to the project's default local path.
            ossClient.getObject(new GetObjectRequest(bucketName, objectName), new File(pathName));

        } catch (OSSException oe) {
            // Handle OSS server-side exceptions.
            System.out.println("Caught an OSSException, which means your request made it to the OSS server but was rejected with an error response.");
            System.out.println("Error Message: " + oe.getErrorMessage());
            System.out.println("Error Code: " + oe.getErrorCode());
            System.out.println("Request ID: " + oe.getRequestId());
            System.out.println("Host ID: " + oe.getHostId());

        } catch (ClientException ce) {
            // Handle client-side exceptions.
            System.out.println("Caught a ClientException, which means the client encountered a serious internal problem while trying to communicate with OSS, " +
                    "such as not being able to access the network.");
            System.out.println("Error Message: " + ce.getMessage());

        } finally {
            // Release resources.
            if (ossClient != null) {
                ossClient.shutdown();
            }
        }
    }
}
`


#### Python


When accessing over PrivateLink, use `is_path_style=True` to enable path-style access.


`python
# -*- coding: utf-8 -*-
"""
OSS PrivateLink Access Demo
Access OSS over PrivateLink and download a file to your local machine.
"""

import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider


def main():
    """Main function: Demonstrates how to access OSS and download a file over PrivateLink."""

    # Configure access credentials.
    # Note: The AccessKey pair of an Alibaba Cloud account has permissions on all API operations. This is a high-risk operation.
    # We recommend that you create and use a RAM user for API access or daily O&M. To create a RAM user, log on to the RAM console.
    auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())

    # The PrivateLink endpoint domain name.
    endpoint = 'https://ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com'

    # The bucket name.
    bucket_name = 'example-bucket'

    # Create a bucket object.
    # is_path_style=True enables path-style access, which is suitable for specific use cases such as PrivateLink.
    bucket = oss2.Bucket(auth, endpoint, bucket_name, is_path_style=True)

    # The OSS object path (full path without the bucket name).
    object_name = 'dest.jpg'

    # The local file path to save to.
    local_file_path = 'dest.jpg'

    # Download the object to a local file.
    # If the local file exists, it is overwritten. If it does not exist, it is created.
    bucket.get_object_to_file(object_name, local_file_path)

    print(f"File downloaded successfully: {object_name} -> {local_file_path}")


if __name__ == '__main__':
    main()
`


#### Go


When accessing over PrivateLink, use `ForcePathStyle(true)` to enable path-style access.


`go
package main

import (
	"fmt"
	"os"

	"github.com/aliyun/aliyun-oss-go-sdk/oss"
)

const (
	// The PrivateLink endpoint.
	endpoint = "https://ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com"

	// The bucket name.
	bucketName = "example-bucket"

	// The OSS object path (full path without the bucket name).
	objectName = "dest.jpg"

	// The local file path to save to.
	localFilePath = "dest.jpg"
)

func main() {
	// Initialize the credentials provider.
	// Obtain access credentials from environment variables.
	// Before you run this code, make sure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
	provider, err := oss.NewEnvironmentVariableCredentialsProvider()
	if err != nil {
		fmt.Printf("Failed to initialize credentials provider: %v\n", err)
		os.Exit(-1)
	}

	// Create an OSS client instance.
	// oss.ForcePathStyle(true) enables path-style access, which is suitable for specific use cases such as PrivateLink.
	client, err := oss.New(
		endpoint,
		"", // AccessKeyId is obtained through the credentials provider.
		"", // AccessKeySecret is obtained through the credentials provider.
		oss.SetCredentialsProvider(&provider),
		oss.ForcePathStyle(true),
	)
	if err != nil {
		fmt.Printf("Failed to create OSS client: %v\n", err)
		os.Exit(-1)
	}

	// Get the bucket object.
	bucket, err := client.Bucket(bucketName)
	if err != nil {
		fmt.Printf("Failed to get bucket object: %v\n", err)
		os.Exit(-1)
	}

	// Download the object to a local file.
	// If the local file exists, it is overwritten. If it does not exist, it is created.
	// If no local path is specified, the downloaded file is saved to the project's default local path.
	err = bucket.GetObjectToFile(objectName, localFilePath)
	if err != nil {
		fmt.Printf("Failed to download file: %v\n", err)
		os.Exit(-1)
	}

	fmt.Printf("File downloaded successfully: %s -> %s\n", objectName, localFilePath)
}

`


#### C++


When accessing over PrivateLink, use `conf.isPathStyle = true` to enable path-style access.


`c++
#include <alibabacloud/oss/OssClient.h>
#include <memory>
#include <fstream>
#include <iostream>

using namespace AlibabaCloud::OSS;

int main(void)
{
    // The PrivateLink endpoint domain name.
    std::string Endpoint = "https://ep-bp1i.oss.cn-hangzhou.privatelink.aliyuncs.com";

    // The bucket name.
    std::string BucketName = "example-bucket";

    // The OSS object path (full path without the bucket name).
    std::string ObjectName = "dest.jpg";

    // The local file path to save to.
    // If the local file exists, it is overwritten. If it does not exist, it is created.
    // If no local path is specified, the downloaded file is saved to the project's default local path.
    std::string FileNametoSave = "dest.jpg";

    // Initialize OSS SDK resources, such as the network.
    InitializeSdk();

    // Configure client parameters.
    ClientConfiguration conf;

    // Obtain access credentials from environment variables.
    // Before you run this code, make sure the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
    auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>();

    // Enable path-style access, which is suitable for specific use cases such as PrivateLink.
    conf.isPathStyle = true;

    // Create an OSS client instance.
    OssClient client(Endpoint, credentialsProvider, conf);

    // Build the GetObject request.
    GetObjectRequest request(BucketName, ObjectName);

    // Set the response stream factory to create a local file stream.
    request.setResponseStreamFactory([=]() {
        return std::make_shared<std::fstream>(
            FileNametoSave,
            std::ios_base::out | std::ios_base::in | std::ios_base::trunc | std::ios_base::binary
        );
    });

    // Run the download operation.
    auto outcome = client.GetObject(request);

    // Process the download result.
    if (outcome.isSuccess()) {
        std::cout << "File downloaded successfully, size: "
                  << outcome.result().Metadata().ContentLength()
                  << " bytes" << std::endl;
        std::cout << "File saved to: " << FileNametoSave << std::endl;
    }
    else {
        // Handle errors.
        std::cout << "File download failed" << std::endl
                  << "Error code: " << outcome.error().Code() << std::endl
                  << "Error message: " << outcome.error().Message() << std::endl
                  << "Request ID: " << outcome.error().RequestId() << std::endl;

        // Release resources and return an error code.
        ShutdownSdk();
        return -1;
    }

    // Release OSS SDK resources, such as the network.
    ShutdownSdk();
    return 0;
}
`


### Connect from an on-premises data center using an Express Connect circuit or VPN Gateway


To use PrivateLink for private access to OSS, an enterprise data center can connect to an Alibaba Cloud VPC through an Express Connect circuit or a VPN Gateway. Express Connect provides stable network performance and guaranteed bandwidth, while a VPN Gateway offers a flexible, encrypted connection. Both solutions are suitable for large-scale data transfer in production environments. For more information, see [Connect a VPC to a Data Center or Another Cloud](https://www.alibabacloud.com/help/en/vpc/connect-vpc-to-local-idc-office-terminal-other-cloud).

## Apply in production

#### Best practices


-

Optimize security group configurations


Configure [security group rules](https://www.alibabacloud.com/help/en/ecs/user-guide/security-group-rules) based on the principle of least privilege. Grant access to the endpoint ports only from necessary IP address ranges and establish a regular review process for your security rules. Precise source IP controls and port restrictions ensure that your access policies meet business needs while preventing unauthorized access.

-

Monitor network connectivity


Enable [VPC flow logs](https://www.alibabacloud.com/help/en/vpc/vpc-flow-logs) to monitor traffic patterns for anomalies and audit PrivateLink access behavior and data transmission status in real time.

-

Deploy across multiple zones


To build a fault-tolerant, high-availability service architecture in a production environment, deploy endpoints across multiple zones. Use load balancing or DNS round-robin for intelligent traffic distribution. If a single zone fails, traffic automatically fails over to healthy endpoints in other zones, which ensures service continuity and operational stability.

## Billing


PrivateLink is billed based on actual usage, and bills are generated hourly. Billable items include instance fees and data transfer fees. The service user and provider can be different Alibaba Cloud accounts, and charges can be billed to a designated account. For more information, see [Billing of PrivateLink](https://www.alibabacloud.com/help/en/privatelink/private-link-billing-description).


Thank you! We've received your  feedback.