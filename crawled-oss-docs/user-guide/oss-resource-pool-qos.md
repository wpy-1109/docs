# Use resource pool QoS to guarantee bandwidth for critical services

By default, all buckets that belong to an Alibaba Cloud account in the same region share [bandwidth](https://www.alibabacloud.com/help/en/oss/user-guide/limits#481f9cdaa9cxq). When multiple buckets concurrently transfer large amounts of data, bandwidth contention may cause transmission delays for critical services. You can resolve this issue by configuring resource pool Quality of Service (QoS) throttling. Threshold-based throttling prevents a bucket from using too much bandwidth, and Priority-based throttling guarantees a minimum bandwidth for core services. These two methods complement each other to ensure the stable operation of important services.

## How it works

### Threshold-based throttling


You can set bandwidth limits for objects at different levels, such as buckets and BucketGroups, to prevent excessive resource usage.

#### Hierarchical relationships


Resource pool hierarchy: A resource pool can have a multi-level structure. The following are common hierarchical structures.


Scenario 1: Flat bucket structure
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3042585671/CAEQUBiBgMCX1_iT2RkiIGJiOWIyN2YyNjVmZTRhYTU5ZTE2YmY5ZjgzODUzYjBh5808935_20251021145900.199.svg)

Scenario 2: Nested BucketGroups
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3042585671/CAEQUBiBgICIqPqT2RkiIDIxMDkwZTQ1YzhiNzRhZjJiYzAzMTIyZDQ0NjQ0YWZh5808935_20251021145900.199.svg)

Scenario 3: Mixed BucketGroups and buckets
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3042585671/CAEQUBiBgIDE3PiT2RkiIDM4YWFjMGU2MDRiNjQ0NzQ5NzQ2MjMxNDMyZDM5OWE45808935_20251021145900.199.svg)

Requester throttling dimension (independent dimension): The requester is not a member of the resource pool hierarchy and is an independent throttling dimension.


Scenario 4: Requester throttling and resource pool hierarchy throttling take effect at the same time
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3042585671/CAEQUBiBgMC.wPuT2RkiIGJjNmRmYmZiMTgzYjQ2M2FiZjcxYTQ0MjViMmM4YjNh5808935_20251021145900.199.svg)
#### Throttling principles


Basic principle


`
Resource pool: Max 100 Gbps
├─ Bucket A: Max 40 Gbps ← Cannot exceed 40 Gbps even if idle
├─ Bucket B: Max 30 Gbps
└─ Bucket C: Unlimited ← Can use all remaining bandwidth
`


Constraint rules


-

Multiple levels of limits take effect at the same time: The actual bandwidth is the minimum of all active rules.

-

The sum of the bandwidths of lower-level objects cannot exceed the total bandwidth of the upper-level object.

-

The requester dimension is an independent constraint: It takes effect along with the resource pool hierarchy constraint. The minimum value is used.


Example


When a RAM user accesses a bucket, the access is subject to the following limits:


-

Requester limit (20 Gbps) ← Independent dimension

-

Bucket limit (30 Gbps) ← Resource pool level


Actual maximum bandwidth = min(20 Gbps, 30 Gbps) = 20 Gbps

### Priority-based throttling


You can configure 3 to 10 priority levels for a resource pool. A larger number indicates a higher priority. You can assign a minimum bandwidth commitment to objects with different priorities to ensure that high-priority services receive bandwidth first during resource competition. If you do not configure a priority level for an object, the default priority level is used. If you do not configure a minimum bandwidth commitment for a priority level, the default minimum bandwidth commitment is used.

#### Core mechanism


-

Minimum commitment guarantee: Each priority level has a minimum bandwidth commitment. This bandwidth is strictly guaranteed.

-

Preemption mechanism: High-priority objects can preempt the bandwidth that low-priority objects use beyond their minimum commitment. Higher-priority objects have precedence in preemption.

-

Idle resource utilization: Low-priority objects can use the idle minimum bandwidth commitment of high-priority objects. However, higher-priority objects have precedence in using these idle resources.

-

Configuration constraint: The sum of all minimum bandwidth commitments ≤ The total bandwidth of the resource pool.

#### Typical scenarios


In the following scenarios, the total bandwidth limit of the resource pool is 100 Gbps, and there are three priority levels: Priority 1 to Priority 3.


Scenario 1: A high-priority object preempts the bandwidth that a low-priority object uses beyond its minimum commitment


Each priority level has a minimum commitment of 20 Gbps. Priority 1 requires 10 Gbps, Priority 2 requires 30 Gbps, and Priority 3 requires 80 Gbps.

















| Priority | Minimum commitment | Required | Actual allocation | Description |
| --- | --- | --- | --- | --- |
| Priority 3 | 20 Gbps | 80 Gbps | 70 Gbps | Gets the 20 Gbps minimum commitment + preempts 10 Gbps of idle bandwidth from Priority 1 + gets the remaining 40 Gbps from the resource pool. |
| Priority 2 | 20 Gbps | 30 Gbps | 20 Gbps | Gets the 20 Gbps minimum commitment. The extra required bandwidth is preempted by Priority 3. |
| Priority 1 | 20 Gbps | 10 Gbps | 10 Gbps | Allocated 10 Gbps as required. The 10 Gbps of idle minimum commitment is preempted by Priority 3. |


Final allocation: 10 + 20 + 70 = 100 Gbps


Scenario 2: Higher-priority objects have precedence in preemption


Each priority level has a minimum commitment of 25 Gbps. Priority 1 requires 0 Gbps, Priority 2 requires 5 Gbps, Priority 3 requires 40 Gbps, and Priority 4 requires 60 Gbps.

















| Priority | Minimum commitment | Requirements | Actual allocation | Description |
| --- | --- | --- | --- | --- |
| Priority 4 | 25 Gbps | 60 Gbps | 60 Gbps | Gets the 25 Gbps minimum commitment + preempts 35 Gbps due to high priority. |
| Priority 3 | 25 Gbps | 40 Gbps | 35 Gbps | Gets the 25 Gbps minimum commitment + preempts the remaining 10 Gbps with the next highest priority. |
| Priority 2 | 25 Gbps | 5 Gbps | 5 Gbps | Required bandwidth is less than the minimum commitment. 5 Gbps is allocated as required. |
| Priority 1 | 25 Gbps | 0 Gbps | 0 Gbps | Required bandwidth is less than the minimum commitment. 0 Gbps is allocated as required. |


Final allocation: 0 + 5 + 35 + 60 = 100 Gbps


Scenario 3: The sum of minimum commitments is less than the total bandwidth


Each priority level has a minimum commitment of 10 Gbps (40 Gbps in total). Priority 1 requires 50 Gbps, Priority 2 requires 50 Gbps, Priority 3 requires 30 Gbps, and Priority 4 requires 20 Gbps.

















| Priority | Minimum commitment | Requirements | Actual allocation | Description |
| --- | --- | --- | --- | --- |
| Priority 4 | 10 Gbps | 20 Gbps | 20 Gbps | Highest priority. The required bandwidth is fully met. |
| Priority 3 | 10 Gbps | 30 Gbps | 30 Gbps | Next highest priority. The required bandwidth is fully met. |
| Priority 2 | 10 Gbps | 50 Gbps | 40 Gbps | Gets the 10 Gbps minimum commitment + the remaining 30 Gbps. |
| Priority 1 | 10 Gbps | 50 Gbps | 10 Gbps | Gets only the minimum commitment. The extra required bandwidth is preempted. |


Final allocation: 10 + 40 + 30 + 20 = 100 Gbps

### Using both throttling methods together


For each throttled resource, you must consider the combined effects of the threshold-based throttling limit, the priority-based minimum bandwidth commitment, and the actual bandwidth requirements.

#### Principles


-

The threshold-based throttling limit is a hard limit. The final bandwidth cannot exceed this limit, regardless of the minimum bandwidth commitment.

-

The priority-based minimum commitment is a soft guarantee. The system tries to meet the minimum commitment within the threshold-based limit.

#### Configuration examples


Normal configuration


Bucket A has the following configuration:


-

Priority-based throttling: Minimum commitment of 50 Gbps ← Priority dimension

-

Threshold-based throttling: Maximum of 80 Gbps ← Resource pool level


Result: The available bandwidth for Bucket A is 50 Gbps to 80 Gbps (at least 50 Gbps, at most 80 Gbps).


Configuration conflict


Bucket A has the following configuration:


-

Priority-based throttling: Minimum commitment of 80 Gbps ← Priority dimension

-

Threshold-based throttling: Maximum of 50 Gbps ← Resource pool level


Result: The actual available bandwidth for Bucket A is 50 Gbps (the threshold-based throttling limit takes precedence, not 80 Gbps).

## Request a resource pool


If the bandwidth of your Alibaba Cloud account in a region reaches 400 Gbps or more, you can contact [Technical Support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex) to request the creation of a resource pool and enable the resource pool and priority-based throttling features in the console.


Provide the following information when you submit a ticket:


`shell
Region: China (Hangzhou)
Resource pool name: qos-resource-pool-1
Bucket list: qos-examplebucket-1, qos-examplebucket-2
Total upload bandwidth: 300 Gbps
Internal network upload bandwidth: 100 Gbps
Public network upload bandwidth: 200 Gbps
Total download bandwidth: 100 Gbps
Internal network download bandwidth: 50 Gbps
Public network download bandwidth: 50 Gbps
Enable resource pool in console: Yes
Enable priority-based throttling: Yes
`


## Configure threshold-based throttling


This method is suitable for scenarios where you need to limit the maximum bandwidth to prevent an object from using too many resources.

### Configure a bandwidth limit for a bucket


You can prevent excessive traffic from one bucket from affecting other buckets.

#### Console


On the [Resource Pool QoS](https://oss.console.alibabacloud.com/resource-pool-qos) page, click the name of the target resource pool. For the target bucket, click Modify Throttling Configuration on the right and set the bandwidth as required.

#### ossutil


Before you begin, [install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2).


-

You can configure the bandwidth limit for a specific bucket using a local XML configuration file named qos.xml.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>20</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

To add the preceding bandwidth configuration to a specific bucket, run the following command. In this example, the bucket is named examplebucket.


`shell
ossutil api invoke-operation --op-name put-bucket-qos-info --method PUT --bucket examplebucket --parameters qosInfo --body=file://qos.xml
`


-

To view the bandwidth configuration of the bucket, run the following command.


`shell
ossutil api invoke-operation --op-name get-bucket-qos-info --method GET --bucket examplebucket --parameters qosInfo
`


#### SDK


Currently, you can set a bandwidth limit for a bucket only using Python SDK V2 and Go SDK V2.


-

You can configure the bandwidth limit for the bucket using a local qos.xml file.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>20</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

To set the preceding bandwidth configuration for a specific bucket, use the following code.


Python

`python
import alibabacloud_oss_v2 as oss

def PutBucketQoSInfo():
   # Obtain access credentials from environment variables for authentication
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load default configurations and obtain the configuration file.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = "cn-hangzhou"

    # Initialize the OSSClient instance by using the configuration file.
    client = oss.Client(cfg)

    # Set qos_xml_body to an empty string.
    qos_xml_body = ""

    # Open the file named qos.xml and read its content into the qos_xml_body variable.
    with open('qos.xml', 'r') as qos_file:
        qos_xml_body = qos_file.read()

    # Specify input parameters for the PutBucketQoSInfo operation to specify the QoS rules for the bucket.
    req = oss.OperationInput(
        op_name = 'PutBucketQoSInfo',  # Operation name, specifying the operation to set bucket QoS information
        method = 'PUT',  # The type of the HTTP method. In this example, PUT is used to update resources.
        parameters = {
            'qosInfo': '',  # The QoS-related parameters.
        },
        headers = None,  # The request headers. If you do not need to specify additional headers, leave the field empty.
        body = qos_xml_body,  # The request body, which contains the content read from the qos.xml file.
        bucket = 'examplebucket',  # The name of the bucket.
    )

    # Use the invoke_operation method of the client to run the request and obtain the response or error message.
    resp = client.invoke_operation(req)

    # Display the returned HTTP status code.
    print(resp.status_code)

    # Display the response headers.
    print(resp.headers)

if __name__ == "__main__":
    GetBucketQoSInfo()
`


#### API


You can call the [PutBucketQoSInfo](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketqosinfo) operation to limit the bucket bandwidth, as shown in the following example.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>20</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


### Configure a bandwidth limit for a bucket requester

#### RAM user


If multiple services share the same bucket, you may need to limit the bandwidth of a specific RAM user to prevent them from using too much bandwidth.

#### Console


-

First, view the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user).

-

On the [Resource Pool QoS](https://oss.console.alibabacloud.com/resource-pool-qos) page, click the name of the target resource pool. Then, click Configure Requester Throttling to the right of the target bucket. Set the required bandwidth for the RAM user to access the bucket.

## ossutil


Before you begin, [install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2).


The following example shows how to limit the bandwidth for a RAM user to access a bucket in a resource pool:


-

You can configure the bandwidth limit for a specific RAM user to access a bucket in the resource pool using a local XML configuration file named qos.xml.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user).

-

To add the preceding bandwidth configuration for the RAM user (UID 266xxxx) who accesses the bucket, run the following command. In this example, the bucket is named examplebucket.


`shell
ossutil api invoke-operation --op-name put-bucket-requester-qos-info --method PUT --bucket=examplebucket --parameters requesterQosInfo --parameters qosRequester=266xxxx --body file://qos.xml
`


-

(Optional) To retrieve the bandwidth configuration for the RAM user to access a bucket in the resource pool, run the following command.


`shell
ossutil api invoke-operation --op-name get-bucket-requester-qos-info --method GET --bucket=examplebucket --parameters requesterQosInfo --parameters qosRequester=266xxxx
`


#### SDK


Currently, you can limit the bandwidth for a RAM user to access a bucket only using Python SDK V2 and Go SDK V2.


-

You can configure the bandwidth limit for a specific RAM user to access a bucket in the resource pool using a local qos.xml file.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user).

-

Set the preceding bandwidth configuration for the RAM user who accesses the bucket.


Python

`python
import alibabacloud_oss_v2 as oss

def PutBucketRequesterQoSInfo():
    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load default configurations and obtain the configuration file.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = "cn-hangzhou"

    # Initialize the OSSClient instance by using the configuration file.
    client = oss.Client(cfg)

    # Set qos_xml_body to an empty string.
    qos_xml_body = ""

    # Open a file named qos.xml and read its content into the qos_xml_body variable.
    with open('qos.xml', 'r') as qos_file:
        qos_xml_body = qos_file.read()

    # Specify input parameters for the PutBucketRequesterQoSInfo operation to configure throttling rules for a requester accessing a bucket.
    req = oss.OperationInput(
        op_name = 'PutBucketRequesterQoSInfo',  # The name of the operation.
        method = 'PUT',  # The type of the HTTP method. In this example, PUT is used.
        parameters = {
            'requesterQosInfo': '',  # The QoS-related parameters.
            'qosRequester': '2598732222222xxxx',  # The unique identifier for the requester, which is used to distinguish different requesters.
        },
        headers = None,  # The request headers. If you do not need to specify additional headers, leave the field empty.
        body = qos_xml_body,  # The request body, which contains the content read from the qos.xml file.
        bucket = 'examplebucket',  # The name of the bucket.
    )

    # Use the invoke_operation method of the client to execute the request and obtain the response.
    resp = client.invoke_operation(req)

    # Display the returned HTTP status code.
    print(resp.status_code)

    # Display the response headers.
    print(resp.headers)

    # Display the response body, which typically contains the specific data returned by the request.
    print(resp.http_response.content)

if __name__ == "__main__":
    PutBucketRequesterQoSInfo()
`


#### API


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user).

-

Call the [PutBucketRequesterQoSInfo](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrequesterqosinfo) operation to limit the bandwidth for a RAM user to access a bucket, as shown in the following example.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>-1</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>-1</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


#### RAM role


You can use a bucket to store static resources and enable CDN acceleration. To allow CDN to fetch files from a private bucket, you must enable back-to-origin for the private bucket. CDN accesses the bucket through the RAM role `AliyunCDNAccessingPrivateOSSRole`. You may need to limit its origin bandwidth.

#### Console


-

View the [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

On the [Resource Pool QoS](https://oss.console.alibabacloud.com/resource-pool-qos) page, click the name of the target resource pool. Then, click Configure Requester Throttling for the target bucket and set the required bandwidth.

## ossutil


Before you begin, [install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2).


-

You can configure the bandwidth limit for this role to access a specific bucket using a local XML configuration file named qos.xml.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>40</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

View the [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

To add the bandwidth configuration for this role (role ID 362xxxx) to access a specific bucket, run the following command. In this example, the bucket is named examplebucket.


`shell
ossutil api invoke-operation --op-name put-bucket-requester-qos-info --method PUT --bucket=examplebucket --parameters requesterQosInfo --parameters qosRequester=362xxxx --body file://qos.xml
`


-

(Optional) To list the bandwidth configurations of all RAM roles in the resource pool, run the following command.


`shell
ossutil api invoke-operation --op-name list-resource-pool-requester-qos-infos --method GET --parameters resourcePool=examplePool  --parameters requesterQosInfo
`


## SDK


Currently, you can limit the bandwidth for a RAM role to access a bucket only using Python SDK V2 and Go SDK V2.


-

You can configure the bandwidth limit for a specific RAM user to access a bucket in the resource pool using a local qos.xml file.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>40</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

View the [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

Set the preceding bandwidth configuration for the RAM role.


Python

`python
import alibabacloud_oss_v2 as oss

def PutBucketRequesterQoSInfo():
    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load default configurations and obtain the configuration file.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = "cn-hangzhou"

    # Initialize the OSSClient instance by using the configuration file.
    client = oss.Client(cfg)

    # Set qos_xml_body to an empty string.
    qos_xml_body = ""

    # Open a file named qos.xml and read its content into the qos_xml_body variable.
    with open('qos.xml', 'r') as qos_file:
        qos_xml_body = qos_file.read()

    # Specify input parameters for the PutBucketRequesterQoSInfo operation to configure throttling rules for a requester accessing a bucket.
    req = oss.OperationInput(
        op_name = 'PutBucketRequesterQoSInfo',  # The name of the operation.
        method = 'PUT',  # The type of the HTTP method. In this example, PUT is used.
        parameters = {
            'requesterQosInfo': '',  # The QoS-related parameters.
            'qosRequester': '2598732222222xxxx',  # The unique identifier for the requester, which is used to distinguish different requesters.
        },
        headers = None,  # The request headers. If you do not need to specify additional headers, leave the field empty.
        body = qos_xml_body,  # The request body, which contains the content read from the qos.xml file.
        bucket = 'examplebucket',  # The name of the bucket.
    )

    # Use the invoke_operation method of the client to execute the request and obtain the response.
    resp = client.invoke_operation(req)

    # Display the returned HTTP status code.
    print(resp.status_code)

    # Display the response headers.
    print(resp.headers)

    # Display the response body, which typically contains the specific data returned by the request.
    print(resp.http_response.content)

if __name__ == "__main__":
    PutBucketRequesterQoSInfo()
`


#### API


-

View the [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

Call the [PutBucketRequesterQoSInfo](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketrequesterqosinfo) operation to limit the bandwidth for a RAM role to access a bucket, as shown in the following example.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>40</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


### Configure a bandwidth limit for a BucketGroup


You can add low-priority buckets to a BucketGroup for unified management and limit their total bandwidth.

#### Console


-

On the [Resource Pool QoS](https://oss.console.alibabacloud.com/resource-pool-qos) page, click the name of the target resource pool. Then, click Create BucketGroup, enter a name for the BucketGroup, and set the required bandwidth.

-

On the target resource pool page, click Configure BucketGroup to the right of the target bucket to add the low-priority bucket to the group.

## ossutil


Before you begin, [install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2).


-

To add the `scheduled-posts` and `archived-comments` buckets to a BucketGroup:


-

To add the `scheduled-posts` bucket to the BucketGroup, run the following command.


`shell
ossutil api invoke-operation --op-name put-bucket-resource-pool-bucket-group --method PUT --bucket scheduled-posts --parameters resourcePool=pool-for-ai --parameters resourcePoolBucketGroup=test-group
`


-

To add the `archived-comments` bucket to the BucketGroup, run the following command.


`shell
ossutil api invoke-operation --op-name put-bucket-resource-pool-bucket-group --method PUT --bucket archived-comments --parameters resourcePool=pool-for-ai --parameters resourcePoolBucketGroup=test-group
`


-

(Optional) To retrieve the list of buckets added to the BucketGroup, run the following command.


`shell
ossutil api invoke-operation --op-name list-resource-pool-bucket-groups --method GET --parameters resourcePool=pool-for-ai --parameters resourcePoolBucketGroup
`


-

You can configure the bandwidth limit for a specific BucketGroup in the resource pool using a local XML configuration file named qos.xml.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>20</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>10</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>30</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>20</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

To configure the bandwidth for the BucketGroup, run the following command.


`shell
ossutil api invoke-operation --op-name put-resource-pool-bucket-group-qos-info --method PUT --parameters resourcePoolBucketGroupQosInfo --parameters resourcePool pool-for-ai --parameters resourcePoolBucketGroup offline-group --body=file://qos.xml
`


-

(Optional) To retrieve the bandwidth configuration of the BucketGroup, run the following command.


`shell
ossutil api invoke-operation --op-name get-resource-pool-bucket-group-qos-info --method GET --parameters resourcePool=pool-for-ai --parameters resourcePoolBucketGroup=offline-group --parameters resourcePoolBucketGroupQoSInfo
`


#### SDK


Currently, you can limit the bandwidth of a BucketGroup only using Python SDK V2 and Go SDK V2.


-

Add two buckets from the resource pool to a BucketGroup.


Python

`python
import alibabacloud_oss_v2 as oss

def PutBucketResourcePoolBucketGroup():
    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load default configurations and obtain the configuration file.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = "cn-hangzhou"

    # Initialize the OSSClient instance by using the configuration file.
    client = oss.Client(cfg)

    # Specify input parameters for the PutBucketResourcePoolBucketGroup operation.
    req = oss.OperationInput(
        op_name = 'PutBucketResourcePoolBucketGroup',  # The name of the operation.
        method = 'PUT',  # The type of the HTTP method type. In this example, PUT is used.
        parameters = {
            'resourcePoolBucketGroup': 'example-group',  # The name of the bucket group in the resource pool.
            'resourcePool': 'example-resource-pool',               # The name of the resource pool.
        },
        headers = None,  # The request headers. If you do not need to specify additional headers, leave the field empty.
        body = None,  # The request body, which is typically not required for PUT requests.
        bucket = 'examplebucket',  # The name of the bucket.
    )

    # Use the invoke_operation method of the client to execute the request and obtain the response.
    resp = client.invoke_operation(req)

    # Display the returned HTTP status code.
    print(resp.status_code)

    # Display the response headers.
    print(resp.headers)

    # Display the response body, which typically contains the specific data returned by the request.
    print(resp.http_response.content)

if __name__ == "__main__":
    PutBucketResourcePoolBucketGroup()
`


-

You can configure the bandwidth limit for a specific BucketGroup in the resource pool using a local XML configuration file named qos.xml.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>20</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>10</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>30</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>20</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

Configure the bandwidth for the BucketGroup.


Python

`python
import alibabacloud_oss_v2 as oss

def PutResourcePoolBucketGroupQoSInfo():
    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load default configurations and obtain the configuration file.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = "cn-hangzhou"

    # Initialize the OSSClient instance by using the configuration file.
    client = oss.Client(cfg)

    # Set qos_xml_body to an empty string.
    qos_xml_body = ""

    # Open and read the qos.xml file and write its content into the qos_xml_body variable.
    with open('qos.xml', 'r') as qos_file:
        qos_xml_body = qos_file.read()

    # Specify input parameters for the PutResourcePoolBucketGroupQoSInfo operation.
    req = oss.OperationInput(
        op_name = 'PutResourcePoolBucketGroupQoSInfo',  # The name of the operation.
        method = 'PUT',  # The type of the HTTP method type. In this example, PUT is used.
        parameters = {
            'resourcePoolBucketGroupQosInfo': '',  # The QoS-related parameters.
            'resourcePool': 'example-resource-pool',           #  The name of the resource pool
            'resourcePoolBucketGroup': 'example-group',  # The name of the bucket group.
        },
        headers = None,  # The request headers. If you do not need to specify additional headers, leave the field empty.
        body = qos_xml_body,  # The request body, which contains the content read from the qos.xml file.
        bucket = None,  # The name of the bucket, which is not required for PUT requests. This operation is not performed on a specific bucket.
    )

    # Use the invoke_operation method of the client to execute the request and obtain the response.
    resp = client.invoke_operation(req)

    # Display the returned HTTP status code.
    print(resp.status_code)

    # Display the response headers.
    print(resp.headers)

    # Display the response body, which typically contains the specific data returned by the request.
    print(resp.http_response.content)

if __name__ == "__main__":
    PutResourcePoolBucketGroupQoSInfo()
`


#### API


Call the [PutResourcePoolBucketGroupQoSInfo](https://www.alibabacloud.com/help/en/oss/developer-reference/putresourcepoolbucketgroupqosinfo) operation to limit the bandwidth of a BucketGroup, as shown in the following example.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>20</TotalUploadBandwidth>
  <IntranetUploadBandwidth>-1</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>10</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>30</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>-1</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>20</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


### Configure a bandwidth limit for a resource pool requester


If multiple RAM users access different buckets in the same resource pool, you may need to limit the maximum bandwidth for each user to prevent a single user from monopolizing the resource pool's bandwidth.

#### Console


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user) or [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

On the [Resource Pool QoS](https://oss.console.alibabacloud.com/resource-pool-qos) page, click the name of the target resource pool. On the Resource Pool Requester List tab, click Modify Throttling Configuration for the target RAM user or RAM role to set the bandwidth for the resource pool requester.

## ossutil


Before you begin, [install ossutil](https://www.alibabacloud.com/help/en/oss/install-ossutil2).


-

You can configure the bandwidth limit for a RAM user or RAM role to access the resource pool using a local XML configuration file named qos.xml.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>50</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>50</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>200</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>150</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>50</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user) or [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

To add the preceding bandwidth configuration for the RAM user (UID 266xxxx), run the following command.


`shell
ossutil api invoke-operation --op-name put-resource-pool-requester-qos-info --method PUT --parameters resourcePool=examplepool --parameters qosRequester=266xxxx --parameters requesterQosInfo --body=file://qos.xml
`


-

(Optional) To list the bandwidth configurations of all RAM users in the resource pool, run the following command.


`shell
ossutil api invoke-operation --op-name list-resource-pool-requester-qos-infos --method GET --parameters resourcePool=examplePool  --parameters requesterQosInfo
`


#### SDK


Currently, you can limit the bandwidth for a RAM user or RAM role to access a resource pool only using Python SDK V2 and Go SDK V2.


-

You can configure the bandwidth limit for a specific RAM user or RAM role to access the resource pool using a local qos.xml file.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>50</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>50</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>200</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>150</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>50</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user) or [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

Set the preceding bandwidth configuration for the RAM user or RAM role.


Python

`python
import alibabacloud_oss_v2 as oss

def PutResourcePoolRequesterQoSInfo():
    # Obtain access credentials from environment variables for authentication.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Load default configurations and obtain the configuration file.
    cfg = oss.config.load_default()

    # Specify the credential provider.
    cfg.credentials_provider = credentials_provider

    # Specify the region in which the bucket is located. For example, if your bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
    cfg.region = "cn-hangzhou"

    # Initialize the OSSClient instance by using the configuration file.
    client = oss.Client(cfg)

    # Initialize qos_xml_body as an empty string
    qos_xml_body = ""

    # Open a file named qos.xml and read its content into the qos_xml_body variable.
    with open('qos.xml', 'r') as qos_file:
        qos_xml_body = qos_file.read()

    # Specify input parameters for the PutResourcePoolRequesterQoSInfo operation.
    req = oss.OperationInput(
        op_name = 'PutResourcePoolRequesterQoSInfo',  # The name of the operation.
        method = 'PUT',  # The type of the HTTP method type. In this example, PUT is used.
        parameters = {
            'requesterQosInfo': '',  # The QoS-related parameters.
            'resourcePool': 'example-resource-pool',  # The name of the resource pool.
            'qosRequester': '2598732222222xxxx',  # The ID of the requester.
        },
        headers = None,  # The request headers. If you do not need to specify additional headers, leave the field empty.
        body = qos_xml_body,  # The request body, which contains the content read from the qos.xml file.
        bucket = None,  # The name of the bucket, which is not required for PUT requests. The operation is not performed on a specific bucket.
    )

    # Use the invoke_operation method of the client to execute the request and obtain the response.
    resp = client.invoke_operation(req)

    # Display the returned HTTP status code.
    print(resp.status_code)

    # Display the response headers.
    print(resp.headers)

    # Display the response body, which typically contains the specific data returned by the request.
    print(resp.http_response.content)

if __name__ == "__main__":
    PutResourcePoolRequesterQoSInfo()
`


#### API


-

View the [RAM user ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-basic-information-about-a-ram-user) or [RAM role ID](https://www.alibabacloud.com/help/en/ram/user-guide/view-the-information-about-a-ram-role).

-

Call the [PutResourcePoolRequesterQoSInfo](https://www.alibabacloud.com/help/en/oss/developer-reference/putresourcepoolrequesterqosinfo) operation to limit the bandwidth for a RAM user or RAM role to access the resource pool, as shown in the following example.


`xml
<QoSConfiguration>
  <TotalUploadBandwidth>100</TotalUploadBandwidth>
  <IntranetUploadBandwidth>50</IntranetUploadBandwidth>
  <ExtranetUploadBandwidth>50</ExtranetUploadBandwidth>
  <TotalDownloadBandwidth>200</TotalDownloadBandwidth>
  <IntranetDownloadBandwidth>150</IntranetDownloadBandwidth>
  <ExtranetDownloadBandwidth>50</ExtranetDownloadBandwidth>
</QoSConfiguration>
`


## Configure priority-based throttling


This method is suitable for scenarios where you need to guarantee a minimum bandwidth for core services and prioritize high-priority objects during resource competition.

### Configure resource pool priorities


If a resource pool contains multiple buckets, you may need to ensure that core service buckets can still obtain sufficient bandwidth when bandwidth is limited.

## ossutil


-

First, create a priority configuration file named `priority-qos.xml`.


`xml
<PriorityQosConfiguration>
  <PriorityCount>3</PriorityCount>
  <DefaultPriorityLevel>1</DefaultPriorityLevel>

  <DefaultGuaranteedQosConfiguration>
    <TotalUploadBandwidth>10</TotalUploadBandwidth>
    <IntranetUploadBandwidth>5</IntranetUploadBandwidth>
    <ExtranetUploadBandwidth>5</ExtranetUploadBandwidth>
    <TotalDownloadBandwidth>20</TotalDownloadBandwidth>
    <IntranetDownloadBandwidth>10</IntranetDownloadBandwidth>
    <ExtranetDownloadBandwidth>10</ExtranetDownloadBandwidth>
  </DefaultGuaranteedQosConfiguration>

  <QosPriorityLevelConfiguration>
    <PriorityLevel>3</PriorityLevel>
    <GuaranteedQosConfiguration>
      <TotalUploadBandwidth>50</TotalUploadBandwidth>
      <TotalDownloadBandwidth>80</TotalDownloadBandwidth>
      <ExtranetUploadBandwidth>30</ExtranetUploadBandwidth>
      <IntranetUploadBandwidth>20</IntranetUploadBandwidth>
      <ExtranetDownloadBandwidth>50</ExtranetDownloadBandwidth>
      <IntranetDownloadBandwidth>30</IntranetDownloadBandwidth>
    </GuaranteedQosConfiguration>
    <Subjects>
      <Bucket>critical-bucket</Bucket>
      <BucketGroup>core-group</BucketGroup>
    </Subjects>
  </QosPriorityLevelConfiguration>

  <QosPriorityLevelConfiguration>
    <PriorityLevel>2</PriorityLevel>
    <GuaranteedQosConfiguration>
      <TotalUploadBandwidth>30</TotalUploadBandwidth>
      <TotalDownloadBandwidth>50</TotalDownloadBandwidth>
      <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
      <IntranetUploadBandwidth>10</IntranetUploadBandwidth>
      <ExtranetDownloadBandwidth>30</ExtranetDownloadBandwidth>
      <IntranetDownloadBandwidth>20</IntranetDownloadBandwidth>
    </GuaranteedQosConfiguration>
    <Subjects>
      <Bucket>important-bucket</Bucket>
    </Subjects>
  </QosPriorityLevelConfiguration>
</PriorityQosConfiguration>
`


-

Application configuration


`shell
ossutil api invoke-operation --op-name put-resource-pool-priority-qos-configuration --method PUT --parameters resourcePool=hz-rp-03 --parameters priorityQos --body=file://priority-qos.xml
`


-

You can retrieve and verify the configuration.


`shell
ossutil api invoke-operation --op-name get-resource-pool-priority-qos-configuration --method GET --parameters resourcePool=hz-rp-03 --parameters priorityQos
`


## SDK


`go
package main

import (
	"bytes"
	"context"
	"crypto/md5"
	"encoding/base64"
	"fmt"
	"os"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

func PutResourcePoolPriorityQosConfiguration() {
	// Specify the region where the bucket is located. For example, set the region to cn-hangzhou for China (Hangzhou).
	var region = "cn-hangzhou"

	// Load the default configurations and set the credential provider and region.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region)

	// Create an OSS client.
	client := oss.NewClient(cfg)

	// Define the resource pool name.
	resourcePool := "hz-rp-01"

	// Read the content of the priority QoS configuration file.
	qosConf, err := os.ReadFile("priority-qos.xml")
	if err != nil {
		// If an error occurs when reading the QoS configuration file, print the error message and exit the program.
		fmt.Printf("failed to read qos.xml: %v\n", err)
		os.Exit(1)
	}

	// Calculate the MD5 hash of the input data and convert it to a Base64-encoded string.
	calcMd5 := func(input byte) string {
		if len(input) == 0 {
			return "1B2M2Y8AsgTpgAmY7PhCfg=="
		}
		h := md5.New()
		h.Write(input)
		return base64.StdEncoding.EncodeToString(h.Sum(nil))
	}

	// Create the input parameters for the operation, including the action, method type, and parameters.
	input := &oss.OperationInput{
		OpName: "PutResourcePoolPriorityQoSConfiguration", // Action
		Method: "PUT",                                     // HTTP method
		Parameters: map[string]string{
			"priorityQos":  "",           // Priority QoS-related parameters.
			"resourcePool": resourcePool, // Resource pool name
		},
		Headers: map[string]string{
			"Content-MD5": calcMd5(qosConf), // Set the Content-MD5 header for the request body to ensure data integrity.
		},
		Body:   bytes.NewReader(qosConf), // Request body that contains the QoS configuration.
		Bucket: nil,                      // This operation does not target a specific bucket.
	}

	// Execute the operation and receive the response or an error.
	res, err := client.InvokeOperation(context.TODO(), input)
	if err != nil {
		// If an error occurs, print the error message and exit the program.
		fmt.Printf("invoke operation got error: %v\n", err)
		os.Exit(1)
	}

	// Print the operation result.
	fmt.Println("The result of PutResourcePoolPriorityQoSConfiguration:", res.Status)
}
`


## API


[PutResourcePoolPriorityQosConfiguration](https://www.alibabacloud.com/help/en/oss/developer-reference/putresourcepoolpriorityqosconfiguration)

### Configure resource pool requester priorities


In a multi-tenant Software as a Service (SaaS) platform, customers of different levels may access the same resource pool. You may need to guarantee bandwidth for VIP customers, while regular customers share the remaining resources.

## ossutil


-

First, create a requester priority configuration file named `requester-priority-qos.xml`.


`xml
<PriorityQosConfiguration>
  <PriorityCount>3</PriorityCount>
  <DefaultPriorityLevel>1</DefaultPriorityLevel>

  <DefaultGuaranteedQosConfiguration>
    <TotalUploadBandwidth>10</TotalUploadBandwidth>
    <IntranetUploadBandwidth>5</IntranetUploadBandwidth>
    <ExtranetUploadBandwidth>5</ExtranetUploadBandwidth>
    <TotalDownloadBandwidth>20</TotalDownloadBandwidth>
    <IntranetDownloadBandwidth>10</IntranetDownloadBandwidth>
    <ExtranetDownloadBandwidth>10</ExtranetDownloadBandwidth>
  </DefaultGuaranteedQosConfiguration>

  <QosPriorityLevelConfiguration>
    <PriorityLevel>3</PriorityLevel>
    <GuaranteedQosConfiguration>
      <TotalUploadBandwidth>60</TotalUploadBandwidth>
      <TotalDownloadBandwidth>100</TotalDownloadBandwidth>
      <ExtranetUploadBandwidth>40</ExtranetUploadBandwidth>
      <IntranetUploadBandwidth>20</IntranetUploadBandwidth>
      <ExtranetDownloadBandwidth>60</ExtranetDownloadBandwidth>
      <IntranetDownloadBandwidth>40</IntranetDownloadBandwidth>
    </GuaranteedQosConfiguration>
    <Subjects>
      <Requester>123456789012</Requester>
      <Requester>234567890123</Requester>
    </Subjects>
  </QosPriorityLevelConfiguration>

  <QosPriorityLevelConfiguration>
    <PriorityLevel>2</PriorityLevel>
    <GuaranteedQosConfiguration>
      <TotalUploadBandwidth>30</TotalUploadBandwidth>
      <TotalDownloadBandwidth>50</TotalDownloadBandwidth>
      <ExtranetUploadBandwidth>20</ExtranetUploadBandwidth>
      <IntranetUploadBandwidth>10</IntranetUploadBandwidth>
      <ExtranetDownloadBandwidth>30</ExtranetDownloadBandwidth>
      <IntranetDownloadBandwidth>20</IntranetDownloadBandwidth>
    </GuaranteedQosConfiguration>
    <Subjects>
      <Requester>345678901234</Requester>
    </Subjects>
  </QosPriorityLevelConfiguration>
</PriorityQosConfiguration>
`


-

Application Configuration


`shell
ossutil api invoke-operation --op-name put-resource-pool-requester-priority-qos-configuration --method PUT --parameters resourcePool=hz-rp-03 --parameters requesterPriorityQos --body=file://requester-priority-qos.xml
`


-

(Optional) To retrieve and verify the configuration, run the following command.


`shell
ossutil api invoke-operation --op-name get-resource-pool-requester-priority-qos-configuration --method GET --parameters resourcePool=hz-rp-03 --parameters requesterPriorityQos
`


## SDK


`go
package main

import (
	"bytes"
	"context"
	"crypto/md5"
	"encoding/base64"
	"fmt"
	"os"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
)

func PutResourcePoolRequesterPriorityQosConfiguration() {
	// Specify the region where the bucket is located. For example, set the region to cn-hangzhou for China (Hangzhou).
	var region = "cn-hangzhou"

	// Load the default configurations and set the credential provider and region.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region)

	// Create an OSS client.
	client := oss.NewClient(cfg)

	// Define the resource pool name.
	resourcePool := "hz-rp-01"

	// Read the content of the requester priority QoS configuration file.
	qosConf, err := os.ReadFile("requester-priority-qos.xml")
	if err != nil {
		// If an error occurs when reading the QoS configuration file, print the error message and exit the program.
		fmt.Printf("failed to read qos.xml: %v\n", err)
		os.Exit(1)
	}

	// Calculate the MD5 hash of the input data and convert it to a Base64-encoded string.
	calcMd5 := func(input byte) string {
		if len(input) == 0 {
			return "1B2M2Y8AsgTpgAmY7PhCfg=="
		}
		h := md5.New()
		h.Write(input)
		return base64.StdEncoding.EncodeToString(h.Sum(nil))
	}

	// Create the input parameters for the operation, including the action, method type, and parameters.
	input := &oss.OperationInput{
		OpName: "PutResourcePoolRequesterPriorityQoSConfiguration", // Action
		Method: "PUT",                                              // HTTP method
		Parameters: map[string]string{
			"requesterPriorityQos": "", // Requester priority QoS-related parameters.
			"resourcePool":         resourcePool, // Resource pool name
		},
		Headers: map[string]string{
			"Content-MD5": calcMd5(qosConf), // Set the Content-MD5 header for the request body to ensure data integrity.
		},
		Body:   bytes.NewReader(qosConf), // Request body that contains the QoS configuration.
		Bucket: nil,                      // This operation does not target a specific bucket.
	}

	// Execute the operation and receive the response or an error.
	res, err := client.InvokeOperation(context.TODO(), input)
	if err != nil {
		// If an error occurs, print the error message and exit the program.
		fmt.Printf("invoke operation got error: %v\n", err)
		os.Exit(1)
	}

	// Print the operation result.
	fmt.Println("The result of PutResourcePoolRequesterPriorityQoSConfiguration:", res.Status)
}
`


## API


[PutResourcePoolRequesterPriorityQosConfiguration](https://www.alibabacloud.com/help/en/oss/developer-reference/putresourcepoolrequesterpriorityqosconfiguration)

## Monitoring and alerting

### Monitor bandwidth usage


During business operations, you can go to the [CloudMonitor - Object Storage Service Resource Pool](https://cloudmonitor.console.alibabacloud.com/productMonitorChart?spm=a2c4g.11186623.0.0.6aead226ireeZj&category=oss_resourcepool) page to view the real-time bandwidth usage of critical services in the resource pool. This helps ensure that resources are allocated reasonably and services run stably.

### Set bandwidth alerts


To ensure the stable operation of critical services, you can [create alert rules in the CloudMonitor service](https://www.alibabacloud.com/help/en/oss/user-guide/use-cloudmonitor-to-monitor-oss-throttling-information-in-real-time). For example, you can configure a rule to automatically trigger an alert when bandwidth usage exceeds 80%. This lets you promptly adjust bandwidth configurations to handle peak business traffic.

## Going live

### Capacity planning recommendations


1. The sum of minimum bandwidth commitments should be less than 50% of the total resource pool bandwidth.


Reserve more than 50% of the bandwidth as elastic space for dynamic scheduling. This can effectively improve the overall bandwidth utilization of the resource pool.


`shell
Recommended configuration:
Total resource pool bandwidth: 100 Gbps
Priority 3 minimum commitment: 20 Gbps
Priority 2 minimum commitment: 20 Gbps
Priority 1 minimum commitment: 10 Gbps
Total: 50 Gbps (50 Gbps of elastic space reserved)
`


2. We recommend 3 to 5 priority levels.


Too many priority levels increase management complexity. We recommend dividing services into 3 to 5 levels based on their importance:


-

Core services (Priority 4-5)

-

Important services (Priority 3)

-

Regular services (Priority 1-2)


3. The threshold-based throttling limit should be higher than the priority-based minimum commitment.


Ensure that high-priority objects can use more bandwidth when resources are sufficient:


`shell
Recommended configuration:
Priority-based throttling: Bucket A minimum commitment of 50 Gbps
Threshold-based throttling: Bucket A maximum of 80 Gbps
Actual available bandwidth: 50-80 Gbps (at least 50, at most 80)
`


### Best practices


Scenario 1: Video-on-demand platform


-

Live streams: Priority 3, minimum commitment of 50 Gbps.

-

On-demand content: Priority 1, minimum commitment of 20 Gbps.

-

CDN back-to-origin: Threshold-based throttling limit of 100 Gbps.


Scenario 2: Multi-tenant SaaS platform


-

Enterprise Edition customers: Priority 3, with an allocated minimum bandwidth commitment.

-

Free Edition customers: Priority 1, sharing the remaining resources.

-

Single-tenant limit: Use threshold-based throttling to prevent a single tenant from using too many resources.


Scenario 3: Data lake analytics


-

Real-time analytics: Priority 2, minimum commitment of 30 Gbps.

-

Offline analytics: Priority 1, minimum commitment of 20 Gbps.

-

Archived data: Threshold-based throttling limit of 10 Gbps.

### Risk prevention


1. Regularly review quota usage


You can use CloudMonitor to view the bandwidth usage trends of each object and adjust quotas promptly:


-

If the minimum bandwidth commitment for high-priority objects is consistently met less than 95% of the time, consider increasing the minimum commitment or decreasing the minimum commitment for low-priority objects.

-

If low-priority objects are unable to use bandwidth for a long time, consider decreasing the minimum commitment for high-priority objects or scaling out the resource pool.


2. Set multi-level alerts


-

Warning level (80%): Provides an early warning to prepare a scale-out plan.

-

Critical level (90%): Requires immediate action to start the emergency plan.


3. Avoid configuration conflicts


-

The sum of minimum bandwidth commitments cannot exceed the total bandwidth of the resource pool.

-

The threshold-based throttling limit should be higher than the priority-based minimum commitment.

-

If a bucket belongs to a BucketGroup, the priority of the BucketGroup takes effect.


4. Changes and rollbacks


-

Before you make important changes, verify the configurations in a staging environment.

-

You should save the current configuration for quick rollbacks.

-

You should perform changes during off-peak hours.

## Quotas and limits























| Limits | Quota/Limit |
| --- | --- |
| Resource pool | Each region is limited to 100 resource pools. |
| You can create a maximum of 100 buckets in each resource pool. |
| Each resource pool can contain a maximum of 100 BucketGroups. |
| You can configure throttling for up to 300 requesters per resource pool. |
| BucketGroup | The name must be 3 to 30 characters long. |
| Only lowercase letters, digits, and hyphens (-) are allowed. |
| Priority-based throttling | The number of priority levels can be an integer from 3 to 10. |
| Priority level: An integer from 1 to the total number of priority levels. |
| The sum of minimum bandwidth commitments cannot exceed the total bandwidth of the resource pool. |
| If a default minimum bandwidth commitment is not set, you must configure one for each priority level. |
| The minimum bandwidth commitment must be at least MIN[5, (Threshold of the corresponding resource in the upper-level resource pool) / (2 × Number of priority levels)] Gbps. |
| Bandwidth parameter | Positive integer: Specifies the limit in Gbps. |
| -1: Unlimited (uses the shared resource pool bandwidth). |
| 0: Prohibits this type of traffic. Use with caution. |
| Delay for configuration to take effect | Within 5 minutes. |


Thank you! We've received your  feedback.