# Accelerate OSS access using EFC

Elastic File Client (EFC) is a solution that accelerates data access on the compute side. It mounts an OSS Bucket as a local file system and uses the memory and disks of compute nodes to build a high-speed, distributed, read-only cache. This process transforms remote OSS access into efficient peer-to-peer (P2P) internal network transfers, reducing access latency and improving data throughput for AI training and inference scenarios.
Note: The EFC cache feature is currently in the invitational preview stage and is free of charge during this period.
## How it works


EFC is a user-mode file system client that is deployed on compute nodes. When an application reads data through a mount target, EFC intercepts these requests and performs the following steps:


-

Cache query: EFC first searches for the data in the cache (memory or disk) of the local node and other peer nodes over the P2P network.

-

Cache hit: If the data exists in the cache, EFC returns the data directly to the application from the cache. This is a high-speed internal network operation.

-

Cache miss (origin fetch): If the data is not in the cache of any node, EFC pulls the data from the source OSS Bucket, stores it in the local cache, and then returns it to the application. Subsequent requests for this data result in a cache hit.


In this way, EFC aggregates frequent remote access to the same dataset into a single origin fetch and multiple high-speed internal cache accesses. The aggregate throughput capacity can scale linearly with the number of compute nodes.


Cache performance metrics: A single node can achieve up to 15 GB/s throughput and 200,000 input/output operations per second (IOPS). Performance scales linearly with the number of nodes and is subject to network bandwidth throttling.

## Core advantages


-

High-speed cache on the compute side: Builds a read cache using the memory and local disks of compute nodes. It supports data prefetching and a least recently used (LRU) eviction policy to reduce remote access latency.

-

P2P distributed acceleration: Nodes share cached data over a P2P network. The aggregate throughput scales linearly with the number of nodes, supporting clusters of hundreds to thousands of nodes. The P2P mechanism works as follows:
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/6702206671/CAEQUBiBgID934qs2RkiIDU0ZTJkMzdiODgzYzQ4YmE5YmUxMzkxN2JiZDlhNzU25458200_20250716135254.206.svg)
-

POSIX compatibility: Compatible with common POSIX file interfaces such as `open`, `read`, and `readdir`. Applications can access OSS data without modification.

## Limits


Before you use EFC, you must confirm that your business scenario and technical environment meet the following requirements.

#### Runtime environment


| Type | Requirement |
| --- | --- |
| Platform | Platform for AI (PAI) (Lingjun resources), Lingjun bare metal |
| Operating system | Alibaba Cloud Linux 3 (kernel 5.10.134-13+), Ubuntu 24.04 (kernel 6.8.0-79+) |


#### Hardware resource requirements


The EFC client consumes memory and disk resources on compute nodes. You can plan your resources based on whether you enable the cache feature.


-

Cache feature disabled


-

Memory: Resident memory usage is typically less than 1 GiB. You must reserve at least 5 GiB of available memory to handle burst workloads.

-

Disk: No special disk space is required. However, you must ensure that the system disk has enough space to store operational logs.

-

Cache feature enabled


When the cache is enabled, resource consumption mainly consists of the cache medium and index overhead.


-

Memory resources


-

Base consumption: Same as when the cache feature is disabled.

-

Memory cache: If you configure memory as the cache, an amount of memory equal to the configured size is consumed.

-

Index overhead: Whether you use a memory or disk cache, additional memory is required to maintain the data index. You must reserve an amount of memory equal to approximately 0.1% of the total cache capacity.

-

Formula: `Total memory consumption ≈ Base runtime memory + Memory cache size + (Memory cache size + Disk cache size) × 0.001`

-

Disk resources:


-

Disk cache: If you configure a disk as the cache medium, it consumes disk space equal to the configured size. For example, a 1 TiB disk cache configuration consumes 1 TiB of disk space.

#### Feature limitations


-

Access mode: Only read-only access to OSS data is supported. After mounting, the owner of the files is fixed as `root` with read-only permissions. `chmod` and `chown` are not supported.

-

POSIX compatibility: Supports operations such as `open`, `close`, `read`, `readdir`, `readdirplus`, `lookup`, and `getattr`. Does not support operations such as `readlink`, `write`, `rename`, `setattr`, `link`, or `symlink`.

-

Storage class: Only supports access to objects of the Standard and Infrequent Access storage classes. Direct access to Archive, Cold Archive, or Deep Cold Archive storage classes is not supported.

-

Path compatibility:


-

Path conflicts: If an OSS Bucket contains both a file named `a/b` and a folder named `a/b/`, only the folder `a/b/` can be accessed after mounting.

-

Special paths: You cannot access objects whose keys start with `/`, contain consecutive slashes (`//`), or contain `.` or `..`.

-

Access permissions: Mounting and accessing OSS requires at least the `oss:GetBucketStat`, `oss:ListObjects`, and `oss:GetObject` permissions.

-

Data high availability: EFC is a read-only cache and does not guarantee data high availability. Cached data may be lost in situations such as a hardware failure or node replacement, which causes the cache to become invalid. When the corresponding data is accessed again, an origin fetch occurs. This can cause performance fluctuations.

## Deployment and mounting


This section guides you through deploying and mounting EFC. The process is designed to be progressive. First, you can complete a basic mount to verify the process, and then enable cache acceleration and a distributed cluster as needed.

### Step 1: Install the EFC client


You can install the EFC client software on the compute node.


-

Download the installation packages


`bash
# alinas-utils toolkit
wget https://aliyun-alinas-eac-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/cache/aliyun-alinas-utils.amd64.rpm

# EFC client main program
wget https://aliyun-alinas-eac-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/cache/alinas-efc-latest.amd64.rpm
`


-

Install the packages


`bash
sudo rpm -ivh aliyun-alinas-utils.amd64.rpm
sudo rpm -ivh alinas-efc-latest.amd64.rpm
`

After installation, the EFC client service is automatically registered but does not start immediately. You must complete the following configurations before you can use it.
### Step 2: Configure access credentials


EFC supports two authentication methods: AccessKey and STS temporary credential. For security reasons, we recommend that you use an STS temporary credential to avoid the risks of a leaked AccessKey.

#### Method 1: Use an STS temporary credential (Recommended)


Create a configuration file that contains the STS temporary credential:


`bash
# Create the STS configuration file
cat > /etc/passwd-sts << EOF
{
    "SecurityToken": "YourSecurityToken",
    "AccessKeyId": "YourSTSAccessKeyId",
    "AccessKeySecret": "YourSTSAccessKeySecret",
    "Expiration": "YourExpiration"
}
EOF

# Set file permissions to allow only root to read
chmod 600 /etc/passwd-sts
`


-

The STS configuration file supports real-time updates. EFC automatically loads the latest credential.

-

You are responsible for managing the validity period of the credential. You must ensure that you update it before it expires.

-

Example format for the `Expiration` field: `2025-12-11T08:37:51Z` (UTC)

#### Method 2: Use an AccessKey


Create a password file that contains the AccessKey:


`bash
# Create the password file (replace with your actual credential)
echo "YourAccessKeyId:YourAccessKeySecret" > /etc/passwd-oss

# Set file permissions to allow only root to read
chmod 600 /etc/passwd-oss
`


### Step 3: Mount an OSS Bucket


Choose one of the following configuration methods based on your scenario. We recommend that you first complete the basic mount to verify the process and then enable cache acceleration as needed.

#### Configuration 1: Basic mount (quick verification)


This configuration is used to quickly verify that EFC can access your OSS Bucket. It does not enable cache acceleration.


Mount using an STS credential (Recommended):


`bash
# Create a local mount target
mkdir -p /mnt/oss_data

# Execute the mount (replace with your Bucket domain name)
mount -t alinas \
  -o efc,protocol=oss,g_oss_STSFile=/etc/passwd-sts \
  your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data
`


Mount using an AccessKey:


`bash
# Create a local mount target
mkdir -p /mnt/oss_data

# Execute the mount (replace with your Bucket domain name)
mount -t alinas \
  -o efc,protocol=oss,passwd_file=/etc/passwd-oss \
  your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data
`


Command description:


-

`mount -t alinas`: Mounts the file system using the EFC client (alinas type).

-

`your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data`: The mount target configuration. `your-bucket.oss-cn-hangzhou.aliyuncs.com` is your OSS Bucket domain name, and `/mnt/oss_data` is the local mount target.

-

`g_oss_STSFile=/etc/passwd-sts`: Specifies the path of the configuration file that contains the STS credential.

-

`passwd_file=/etc/passwd-oss`: Specifies the path of the password file that contains the OSS AccessKey.


For more information about the parameters, see [Detailed mount parameters].


Verify the mount result:


`bash
# Check if the mount was successful
df -h | grep /mnt/oss_data
# List the files in OSS
ls /mnt/oss_data
`


If you can view the files in your OSS Bucket, the basic mount is successful. You can now enable cache acceleration as needed.

#### Configuration 2: Single-node cache mode


Enable the memory and disk cache on the current node. This configuration builds on the basic mount and is suitable for single-node tasks or quick tests.
Note: If you have already completed the basic mount, you must first unmount it: `umount /mnt/oss_data`

`bash
# Create the disk cache folder
mkdir -p /mnt/cache/

# Mount and enable single-node cache (using an STS credential)
mount -t alinas \
  -o efc,protocol=oss,g_oss_STSFile=/etc/passwd-sts \
  -o g_tier_DadiIsDistributed=false \
  -o g_tier_DadiMemCacheCapacityMB=1024 \
  -o g_tier_DadiDiskCacheCapacityMB=10240 \
  -o g_tier_DadiDiskCachePath=/mnt/cache/ \
  -o g_server_Port=17871 \
  your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data
`


Command description:


-

`mount -t alinas ... your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data`: Mounts the OSS Bucket to the local `/mnt/oss_data` folder using the EFC client.

-

`g_oss_STSFile=/etc/passwd-sts`: Specifies the path of the configuration file that contains the STS credential.

-

`g_tier_DadiIsDistributed=false`: Single-node cache mode. The node does not communicate with other nodes.

-

`g_tier_DadiMemCacheCapacityMB=1024`: Allocates 1 GB of memory for data caching.

-

`g_tier_DadiDiskCacheCapacityMB=10240`: Allocates 10 GB of disk space for data caching.

-

`g_tier_DadiDiskCachePath=/mnt/cache/`: The folder where disk cache files are stored.

-

`g_server_Port=17871`: Opens port 17871 to allow you to use command-line tools to view the cache hit ratio or perform data prefetching.


For more information about the parameters, see [Detailed mount parameters].

#### Configuration 3: Distributed cache cluster mode


This mode combines multiple nodes into a cache cluster to share cached data and accelerate data distribution over a P2P network. This mode is suitable for large-scale training and inference in a production environment.


1. Configure the cache node list


On all nodes, create the `/etc/efc/rootlist` file and add the information for all nodes in the cluster:


`plaintext
# Format: <Unique_ID>:<Node_Internal_IP>:<P2P_Port>
1:192.168.1.1:17980
2:192.168.1.2:17980
3:192.168.1.3:17980
`

Warning: The `rootlist` file must be identical across the entire cluster. Inconsistencies can prevent some nodes from joining the cache network and can lower the cache hit ratio.

2. Execute the mount command on all nodes


`bash
# Create the disk cache folder
mkdir -p /mnt/cache/

# Mount and enable distributed cache (using an STS credential)
mount -t alinas \
  -o efc,protocol=oss,g_oss_STSFile=/etc/passwd-sts \
  -o g_tier_EnableClusterCache=true \
  -o g_tier_DadiIsDistributed=true \
  -o g_tier_DadiAddr=/etc/efc/rootlist \
  -o g_tier_DadiMemCacheCapacityMB=1024 \
  -o g_tier_DadiDiskCacheCapacityMB=10240 \
  -o g_tier_DadiDiskCachePath=/mnt/cache/ \
  -o g_server_Port=17871 \
  your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data
`


Command description:


-

`mount -t alinas ... your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data`: Mounts the OSS Bucket to the local `/mnt/oss_data` folder using the EFC client.

-

`g_oss_STSFile=/etc/passwd-sts`: Specifies the path of the configuration file that contains the STS credential.

-

`g_tier_EnableClusterCache=true`, `g_tier_DadiIsDistributed=true`: Enables the core feature of EFC: distributed cache acceleration.

-

`g_tier_DadiAddr=/etc/efc/rootlist`: Specifies the path of the cluster node configuration file, which is used to build the P2P cache network.

-

`g_tier_DadiMemCacheCapacityMB=1024`: Allocates 1 GB of memory for data caching.

-

`g_tier_DadiDiskCacheCapacityMB=10240`: Allocates 10 GB of disk space for data caching. The cache files are stored in the `/mnt/cache/` folder.

-

`g_server_Port=17871`: Opens port 17871 to allow you to use command-line tools to view the cache hit ratio or perform data prefetching.


For more information about the parameters, see [Detailed mount parameters].

#### Configuration 4: Agent mode (access only, no data caching)


If you want a node to only access the distributed cache and not cache any data itself, which is suitable for lightweight nodes with limited compute resources, you can use the Agent mode to mount:


`line
mount -t alinas \
  -o efc,protocol=oss,passwd_file=/etc/passwd-sts \
  -o g_tier_EnableClusterCache=true \
  -o g_tier_DadiIsDistributed=true \
  -o g_tier_DadiRootClientType=2 \
  -o g_tier_DadiAddr=/etc/efc/rootlist \
  -o g_server_Port=17871 \
  your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data

`


Command description:


-

`mount -t alinas ... your-bucket.oss-cn-hangzhou.aliyuncs.com:/ /mnt/oss_data`: Mounts the OSS Bucket to the local `/mnt/oss_data` folder using the EFC client.

-

`g_oss_STSFile=/etc/passwd-sts`: Specifies the path of the configuration file that contains the STS credential.

-

`g_tier_EnableClusterCache=true`, `g_tier_DadiIsDistributed=true`: Enables distributed cache acceleration.

-

`g_tier_DadiRootClientType=2`: Sets the mode to Agent. This node only accesses the cache of other nodes and does not provide caching services.


-

Default value `0`: Root/Agent mode. The node both provides and accesses the cache.

-

Value `1`: Root mode. The node only provides cache services.

-

Value `2`: Agent mode. The node only accesses the cache.

-

`g_tier_DadiAddr=/etc/efc/rootlist`: Specifies the path of the cluster node configuration file.

-

`g_server_Port=17871`: Opens port 17871 for O&M.


For more information about the parameters, see [Detailed mount parameters].

## Cache O&M


After a successful mount, you can manage the cache using the O&M interfaces provided by EFC. Before you perform O&M operations, you must ensure that you enabled the management port using `-o g_server_Port=<port_number>` during the mount. This topic uses the default port `17871` as an example.

### Data prefetching


This feature loads data from OSS into the cache in advance to eliminate the latency of the first access. This is especially important for scenarios such as model inference.


-

Path requirement: The prefetch path must be a relative path under the mount target.

-

Task status: `running`, `completed`, `canceled`, `failed`.

-

Passive task eviction policy: Prefetch tasks are not retained indefinitely. The system automatically evicts historical task records based on the following rules:


-

Tasks in the `running` state: Can be actively canceled only using the `cancel` command and cannot be passively evicted.

-

Tasks that are completed, canceled, or have failed are automatically evicted when either of the following conditions is met:


-

The total number of historical prefetch tasks exceeds 10,000.

-

The task record is more than 7 days old.

## Use the HTTP interface


-

Parameters














| Parameter name | Required | Description |
| --- | --- | --- |
| target_path | Yes | The relative path to prefetch. Separate multiple paths with commas (,). |
| pattern | No | A regular expression to filter matching filenames. |
| preceding_time | No | Filters tasks created within the last N seconds (for queries only). Default: 86400 (1 day). |


-

Start a prefetch task


Prefetch the `file100G` file under the `/mnt/oss_data` mount target.


`bash
curl -s "http://localhost:17871/v1/warmup/load?target_path=file100G"
`


Sample response:


`plaintext
$ curl -s "http://localhost:17871/v1/warmup/load?target_path=file100G"
{
    "ErrorCode": 0,
    "ErrorMessage": "Request processed",
    "Results": [{
            "ErrorCode": 0,
            "ErrorMessage": "The warm up (file100G) is processing in the background. Use the 'stat' command to get status.",
            "Location": "127.0.0.1:17871",
            "Path": "file100G"}]}
`


-

Check the prefetch status of the `file100G` file.
After a successful prefetch, the file status changes to completed.If the prefetch fails, the file status changes to failed, and an error code and error message are returned.`/mnt/oss_data/file1G` and `mnt/oss_data/file1G` are parsed incorrectly because they include the mount target path. This causes the prefetch to fail.

`bash
curl -s "http://localhost:17871/v1/warmup/stat?target_path=file100G"
`


Sample response:


`plaintext
$ curl -s "http://localhost:17871/v1/warmup/stat?target_path=file100G"
{
    "ErrorCode": 0,
    "ErrorMessage": "Request processed",
    "Results": [{
            "ErrorCode": 0,
            "ErrorMessage": "Successfully stat the warm up",
            "Location": "127.0.0.1:17871",
            "Path": "file100G",
            "TaskInfos": [{
                    "CompletedSize": 13898874880,
                    "ErrorCode": 0,
                    "ErrorMessage": "",
                    "IsDir": false,
                    "Path": "file100G",
                    "Pattern": "",
                    "Status": "running",
                    "SubmitTime": 1765274023424073,
                    "TotalSize": 107374182400}]}]}
`


-

Cancel a prefetch task


Cancel the prefetch task for the `file100G` file.
Only tasks that are in the running state can be canceled.

`bash
curl -s "http://localhost:17871/v1/warmup/cancel?target_path=file100G"
`


Sample response:


`plaintext
$ curl -s "http://localhost:17871/v1/warmup/cancel?target_path=file100G"
{
    "ErrorCode": 0,
    "ErrorMessage": "Request processed",
    "Results": [{
            "ErrorCode": 0,
            "ErrorMessage": "Successfully canceled the warm up tasks",
            "Location": "127.0.0.1:17871",
            "Path": "file100G"}]}
`


## Use the command-line interface


-

Parameters























| Parameter name | Required | Description |
| --- | --- | --- |
| -m | Yes | The mount target path. |
| -r | Yes | The operation type: warmup/load (prefetch), warmup/stat (query), warmup/cancel (cancel). |
| --path | Yes | The relative path under the mount target. To specify the root directory, pass "". Separate multiple paths with commas (,). |
| --pattern | No | A regular expression to filter matching filenames. |
| --preceding_time | No | Filters tasks created within the last N seconds (for queries only). Default: 86400 (1 day). |


-

Start a prefetch task


Prefetch the files in the `testDir` folder under the `/mnt/oss_data` mount target.


`bash
/usr/bin/aliyun-alinas-efc-cli -m /mnt/oss_data -r warmup/load --path "testDir" --pattern ".*_2$"
`


Example response:


`plaintext
$ /usr/bin/aliyun-alinas-efc-cli -m /mnt/oss_data -r warmup/load --path "testDir"
{
    "ErrorCode": 0,
    "ErrorMessage": "Request processed",
    "Results": [{
            "ErrorCode": 0,
            "ErrorMessage": "The warm up (testDir) is processing in the background. Use the 'stat' command to get status.",
            "Location": "",
            "Path": "testDir"}]}
`


-

Check the prefetch status


Query the prefetch progress for the `testDir` folder.


`bash
/usr/bin/aliyun-alinas-efc-cli -m /mnt/oss_data -r warmup/stat --path "testDir"
`


Prefetch task status:


-

running: The prefetch task is running.

-

completed: The prefetch task is complete.

-

cancel: The prefetch task was canceled. It cannot be resumed. You must start a new prefetch task.

-

failed: If the prefetch fails, the task status changes to failed, and an error code and related error information are returned.


Example response:


`plaintext
$ /usr/bin/aliyun-alinas-efc-cli -m /mnt/oss_data -r warmup/stat --path "testDir"
{
    "ErrorCode": 0,
    "ErrorMessage": "Request processed",
    "Results": [{
            "ErrorCode": 0,
            "ErrorMessage": "Successfully stat the warm up",
            "Location": "",
            "Path": "testDir",
            "TaskInfos": [{
                    "CompletedSize": 11875394560,
                    "ErrorCode": 0,
                    "ErrorMessage": "",
                    "IsDir": true,
                    "Path": "testDir",
                    "Pattern": "",
                    "Status": "running",
                    "SubmitTime": 1765273087321936,
                    "TotalSize": 107872527360}]}]}
`


-

Cancel Prefetch


Cancel the prefetch task for `testDir` (only for tasks in the `running` state).
Tasks that are completed or have failed cannot be canceled. Attempting to cancel a completed task fails.

`bash
/usr/bin/aliyun-alinas-efc-cli -m /mnt/oss_data -r warmup/cancel --path "testDir"
`


The following is a sample response:


`plaintext
$ /usr/bin/aliyun-alinas-efc-cli -m /mnt/oss_data -r warmup/cancel --path "testDir"
{
    "ErrorCode": 0,
    "ErrorMessage": "Request processed",
    "Results": [{
            "ErrorCode": 0,
            "ErrorMessage": "Successfully canceled the warm up tasks",
            "Location": "",
            "Path": "testDir"}]}
`


### Cache monitoring


This feature lets you view the real-time running status of the cache, such as the hit rate and throughput. This information is key for performance tuning.

##### View monitoring data


-

HTTP method (Recommended, returns JSON format)


`bash
curl -s "http://localhost:17871/v1/tier"
`


-

Command-line method (Returns text format)


`bash
aliyun-alinas-efc-cli -m <mount_target> -r tier
`


##### Clear monitoring data


Reset the monitoring counters (for example, metrics such as `tier_read_hit` are reset to zero).


-

HTTP method


`bash
curl -s "http://localhost:17871/v1/tier/clear"
`


-

Command-line method


`bash
aliyun-alinas-efc-cli -m <mount_target> -r tier -c
`


##### Key metric descriptions


The following metrics describe the possible paths when client A accesses the cache of client B (where B provides the root service):









































| Metric name | Description | Corresponding path |
| --- | --- | --- |
| tier_read | Total number of read requests that passed through the cache path. | i |
| tier_read_bytes | Total data volume of read requests that passed through the cache path. | i |
| tier_read_hit | Number of successful read requests from a distributed node that resulted in a cache hit. | ii |
| tier_read_hit_bytes | Total data volume of successful read requests from a distributed node that resulted in a cache hit (may include read amplification). | ii |
| tier_read_miss | Number of successful read requests from a distributed node that resulted in a cache miss (origin fetch). This triggers the distributed node to read from the backend. | iii |
| tier_read_miss_bytes | Total data volume of successful read requests from a distributed node that resulted in a cache miss. | iii |
| tier_direct_read | Number of requests where a read from a distributed node failed, and the client successfully read directly from the backend OSS. | v |
| tier_direct_read_bytes | Total data volume of requests where a read from a distributed node failed, and the client successfully read directly from the backend OSS. | v |
| tier_root_read_source | Number of requests to the backend when the client acts as a distributed node and a cache miss occurs. | iv |
| tier_root_read_source_bytes | Total data volume read from the backend when the client acts as a distributed node and a cache miss occurs. | iv |


### Scaling the cache

##### Add or remove nodes online


This operation dynamically adjusts the number of nodes in the distributed cache cluster without service interruption.


-

Scale-out: In the `rootlist` file on all nodes, add the IP addresses of the new nodes.

-

Scale-in: In the `rootlist` file on all nodes, delete the IP addresses of the target nodes.
When a node is removed, the system uses an LRU mechanism to evict cached data. This ensures that frequently accessed hot spot data is prioritized for retention to maintain the cache hit ratio.
-

Effective mechanism: The EFC process periodically (every 5 seconds by default) rereads the `rootlist` file and automatically applies the changes.

##### Adjust the cache capacity of a single nodeImportant: EFC does not support dynamic adjustment of a single node's cache capacity. To make adjustments, you must unmount and remount the file system. You can perform this operation during off-peak hours.

When you remount, you can modify the following parameters to adjust the cache capacity:




















| Parameter name | Description | Unit | Default value |
| --- | --- | --- | --- |
| g_tier_DadiMemCacheCapacityMB | The total memory cache capacity of a single node. | MB | 0 |
| g_tier_DadiDiskCacheCapacityMB | The total disk cache capacity of a single node. | MB | 0 |


### Dynamically adjust mount parameters


EFC provides a [Python script tool](https://aliyun-alinas-eac-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/cache/efc_runtime_ops.latest.py) that you can use to modify mount parameters without manually unmounting the file system. The tool works by modifying the EFC `state` file, which stores the startup command, and then terminating the current EFC process. The process automatically loads the new parameters upon restart.


-

Download the tool


`bash
wget https://aliyun-alinas-eac-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/cache/efc_runtime_ops.latest.py
`


-

Modify mount parameters


`bash
python3 efc_runtime_ops.py update <local_mount_path> [-o <update_parameters,...>]...
`


Example:


`bash
python3 update_state_file.py update /mnt/oss_data \
          -o g_tier_EnableClusterCache=true,g_tier_tier_DadiP2PPort=23456 \
          -o g_tier_BlockSize=1048576
`


-

Roll back


When you modify parameters, the tool automatically backs up the old `state` file. If EFC fails after the modification, you can roll back to recover the previous state:


`bash
python3 efc_runtime_ops.py rollback <local_mount_path> [backup_path]
`


Example: Restore the `state` file using the default backup file path.


`bash
python3 efc_runtime_ops.py rollback /mnt/oss_data
`


### Directory cache management


EFC enables directory caching by default to accelerate directory traversal operations such as `ls`. If the directory structure on the OSS side changes and EFC does not detect it promptly, you can manually clear the directory cache.


Directory cache parameters (specified at mount time):























| Parameter name | Default value | Description |
| --- | --- | --- |
| g_readdircache_Enable | true | Specifies whether to enable the readdir cache. |
| g_readdircache_MaxCount | 20000 | The maximum number of entries in the readdir cache. |
| g_readdircache_MaxSize | 100 MiB | The amount of memory that the readdir cache can use. Unit: bytes. |
| g_readdircache_RemainTime | 3600 | The cache validity period. Unit: seconds. Default: 1 hour. |


Clear the directory cache:


-

HTTP method


`bash
curl -s "http://localhost:17871/v1/action/clear_readdir_cache"
`


-

Command-line method


`bash
aliyun-alinas-efc-cli -m <mount_target> -r action -k clear_readdir_cache
`


## Detailed mount parameters

### Basic parameters


















































| Parameter name | Default value | Sample value | Required | Description |
| --- | --- | --- | --- | --- |
| efc | - | efc | Yes | You must include this parameter to identify the mount as an EFC mount. |
| protocol | - | oss | Yes | The backend storage protocol. Set to oss when mounting OSS. |
| passwd_file | - | /etc/passwd-oss | Required if g_oss_STSFile is not specified. | The absolute path of the password file that contains the AccessKeyId:AccessKeySecret. The format is AK:SK. |
| g_oss_STSFile | - | /etc/passwd-sts | Required if passwd_file is not specified. | The absolute path of the configuration file that contains the STS temporary credential. It supports real-time updates. You are responsible for ensuring its validity. |
| trybind | yes | no | No | Specifies whether to attempt a bind mount. Set to no when using mirroring-based back-to-origin. |


### Cache configuration parameters


































































































| Parameter name | Default value | Sample value | Required | Description |
| --- | --- | --- | --- | --- |
| g_tier_EnableClusterCache | true | true | No | Specifies whether to enable the EFC cache acceleration feature. If set to false, EFC degrades to a simple protocol conversion mount. |
| g_tier_DadiIsDistributed | true | true | No | Specifies whether to enable the distributed cache. true indicates distributed mode. false indicates single-node cache mode. |
| g_tier_DadiAddr | - | /etc/efc/rootlist | No | The absolute path of the rootlist file. This is required in distributed mode. |
| g_tier_DadiRootClientType | 0 | 2 | No | The EFC mount type. 0: Root/Agent mode (default). 1: Root mode (provides cache only). 2: Agent mode (accesses cache only, does not store data). |
| g_tier_DadiMemCacheCapacityMB | 0 | 1024 | No | The memory cache capacity in MB. The default value is 0, which means the memory cache is disabled. |
| g_tier_DadiDiskCacheCapacityMB | 0 | 10240 | No | The disk cache capacity in MB. The default value is 0, which means the disk cache is disabled. |
| g_tier_DadiDiskCachePath | - | /mnt/cache/ | No | The absolute path of the disk cache folder. It must end with a forward slash (/). This is required when the disk cache is enabled. |
| g_tier_DadiP2PPort | 17980 | 17980 | No | The P2P cache communication port. Keep the default value and ensure it is allowed by the security group. |
| g_tier_DadiSdkGetTrafficLimit | 3 GB/s | 3221225472 | No | The read traffic limit for origin fetches from OSS. Unit: B/s. |
| g_tier_DadiCachePageSizeKB | 16 | 16 | No | The cache page size in KB. You do not typically need to modify this. |


### Metadata and directory cache parameters















































| Parameter name | Default value | Sample value | Required | Description |
| --- | --- | --- | --- | --- |
| g_metadata_CacheEnable | false | true | No | Specifies whether to enable metadata caching. Enabling this can reduce the number of HEAD requests to OSS. |
| g_readdircache_Enable | true | true | No | Specifies whether to enable the readdir cache. |
| g_readdircache_MaxCount | 20000 | 20000 | No | The maximum number of entries in the readdir cache. |
| g_readdircache_MaxSize | 100 MiB | 104857600 | No | The amount of memory that the readdir cache can use. Unit: bytes. |
| g_readdircache_RemainTime | 3600 | 3600 | No | The readdir cache validity period in seconds. Default: 1 hour. |


### O&M and advanced parameters











| Parameter name | Default value | Sample value | Required | Description |
| --- | --- | --- | --- | --- |
| g_server_Port | 0 | 17871 | No | The cache management port. Set to a non-zero value, such as 17871, to enable the HTTP O&M interface. |


## Best practices


#### Permissions and security


-

Protect the password file: Set the permissions for the password file to `600` and store it in a secure location to prevent credential leaks.

-

Prioritize STS: For security reasons, we recommend that you use STS temporary credentials instead of long-term AccessKeys to reduce the risk of key leakage.

-

Minimize security group exposure: Open the P2P communication port `17980` only between cluster nodes, and strictly limit the access sources for the management port `17871`.

#### Scenario-specific configuration recommendationsAI model training


-

Characteristics: Typically involves repeated, sequential reads of large datasets, which may contain many small files.

-

Recommendations:


-

Configure a disk cache large enough to hold the entire hot spot dataset, or most of it.

-

Before the training task starts, perform data prefetching on the core dataset to handle the overhead of the first read in advance.


AI model inference


-

Characteristics: Many compute nodes need to load the same model files simultaneously.

-

Recommendations:


-

Enable the distributed cluster mode to fully utilize the P2P network for distributing model files. This avoids creating a single point of pressure on OSS.

-

When the service goes online or when you update a model, perform data prefetching for the model files.

#### Data consistency management


-

Understand eventual consistency: EFC is a read-only cache. Changes to the OSS backend are not synchronized in real time. Therefore, your application design must tolerate a certain degree of data latency.

-

Proactive refresh: For scenarios that require frequent updates and immediate reads, you can add a step in your application logic to call the interface for clearing the directory cache.

-

Enable metadata caching: For scenarios in which metadata does not change often, you can enable metadata caching using `-o g_metadata_CacheEnable`. This can reduce the number of `GetObjectMeta` requests to OSS.

## Billing


-

EFC client: The EFC client itself is free of charge during the invitational preview period.

-

OSS fees: The number of requests, outbound traffic over the Internet, and other resources that are generated by accessing OSS through EFC are charged based on the [standard billing rules](https://www.alibabacloud.com/help/en/oss/billing-overview) of OSS. Using the EFC cache can effectively reduce origin requests and traffic, which in turn can lower your OSS costs.

## FAQ

#### Q: After data in OSS is updated, does the EFC cache detect the changes immediately?A: EFC's ability to detect data updates in OSS depends on the status of the metadata cache configuration.


-

When metadata caching is disabled: File updates are detected immediately. When new files are added, they may not be visible immediately because of the readdir cache mechanism. You must clear the readdir cache to view the new files.

-

When metadata caching is enabled: File updates are not detected immediately. You must clear the metadata cache. When new files are added, you must clear both the readdir cache and the metadata cache to view them.


Solution:


To immediately detect data changes in OSS, you can manually clear the cache as follows:


-

Clear the directory cache (for cases in which new files are not visible)


`bash
curl -s "http://localhost:17871/v1/action/clear_readdir_cache"
`


-

Clear the metadata cache (required only when metadata caching is enabled):


`bash
curl -s "http://localhost:17871/v1/action/clear_metadata_cache"
`

If metadata caching is enabled, we recommend that you run both of the preceding clear commands to fully synchronize with the latest data in OSS.


Thank you! We've received your  feedback.