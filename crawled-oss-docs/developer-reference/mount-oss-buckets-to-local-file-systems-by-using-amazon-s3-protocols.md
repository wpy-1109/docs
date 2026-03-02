# Mount OSS buckets to local file systems in various operating systems by using s3fs, goofys, and Rclone

This topic describes how to mount Object Storage Service (OSS) buckets to local file systems in various operating systems by using s3fs, goofys, and Rclone. This way, you can perform operations on OSS objects in the same manner that you perform operations on local files and data can be shared.

## Prerequisites


-

A Resource Access Management (RAM) user is created and an AccessKey pair is obtained. For more information, see [Create a RAM user](https://www.alibabacloud.com/help/en/ram/create-a-ram-user-1).

-

System permissions or custom permissions are granted to the RAM user.


-

System permissions: You can attach the AliyunOSSFullAccess policy to the RAM user to allow the RAM user to manage OSS or attach the AliyunOSSReadOnlyAccess policy to the RAM user to allow the RAM user only to access OSS objects.

-

Custom permissions: You can grant the RAM user custom permissions to implement fine-grained OSS permission control based on business scenarios. For more information, see [Common examples of RAM policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-ram-policies).

## s3fs


s3fs can be used to mount an OSS bucket to a local file system in Linux or macOS. After you mount an OSS bucket to the local file system, you can perform operations on OSS objects in the same manner that you perform operations on local files and data can be shared. For more information about s3fs, visit [GitHub](https://github.com/s3fs-fuse/s3fs-fuse/wiki). For information about how to resolve issues that you may encounter when you use s3fs to mount an OSS bucket to a local file system, see [FAQ](https://github.com/s3fs-fuse/s3fs-fuse/wiki/FAQ).

### Key features


-

Supports most features of the POSIX file system. For example, you can upload and download objects and directories, and configure symbolic links and user permissions.

-

Supports the random write feature and allows you to append data to an existing object.

-

Does not support hard links.

-

Uploads large objects by using multipart upload.

-

Uses local files as caches.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

When you use s3fs to upload or download an object, the object must be locally cached. The download or upload speed depends on the read/write performance of the disk. The size of the local cache can indefinitely grow. We recommend that you periodically clear the local cache.


### Procedure


To mount an OSS bucket to a local file system by using s3fs, perform the following steps:


-

Install s3fs.


The following items provide examples on how to run commands to install s3fs in Ubuntu, CentOS, and macOS. For more information about how to run commands to install s3fs in other operating systems, visit [Installation](https://github.com/s3fs-fuse/s3fs-fuse#installation).


-

Ubuntu


`shell
sudo apt install s3fs
`


-

 CentOS


`shell
sudo yum install epel-release
sudo yum install s3fs-fuse
`


-

Mac


`shell
brew install --cask macfuse
brew install gromgit/fuse/s3fs-mac
`


-

Configure account information that is used to access the bucket.


Store the AccessKey pair that can be used to access the bucket in the /.passwd-s3fs file.


`shell
echo ACCESS_KEY_ID:ACCESS_KEY_SECRET > ${HOME}/.passwd-s3fs
`


-

Set the permissions of the /.passwd-s3fs file to 600.


`shell
chmod 600 ${HOME}/.passwd-s3fs
`


-

Mount the bucket.


-

Run the following command to create a mount target:


`shell
mkdir /tmp/oss-bucket
`


-

Run the following command to mount the examplebucket bucket in the China (Hangzhou) region to /tmp/oss-bucket:


`shell
s3fs examplebucket /tmp/oss-bucket -o passwd_file=$HOME/.passwd-s3fs -ourl=http://oss-cn-hangzhou.aliyuncs.com
`


> NOTE:

> NOTE: 


> NOTE: Note 

-

If an Elastic Compute Service (ECS) instance is located in the same region as the OSS bucket, you can use the internal endpoint oss-cn-hangzhou-internal.aliyuncs.com to access the OSS bucket from the ECS instance. For more information, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints).

-

For more information about the parameters supported by s3fs, visit [Options](https://github.com/s3fs-fuse/s3fs-fuse/wiki/Fuse-Over-Amazon).


## goofys


goofys allows you to mount a bucket to a local file system in Linux or macOS. goofys supports only specific features of POSIX. For more information, visit [GitHub](https://github.com/kahing/goofys/blob/master/README.md).

### Key features


-

Supports only the sequential write feature.

-

Does not save object permissions and attributes.

-

Does not support symbolic links and hard links.

-

The creation time (ctime), access time (atime), and modification time (mtime) are the same.

-

Does not depend on local caches.


Operations on object metadata are not supported. In specific scenarios that depend on object metadata, goofys has usage limits.


Compared with s3fs, goofys does not depend on local caches. In this case, goofys has better read and write performance on operations, such as cp and mv. For more information, visit [Benchmark](https://github.com/kahing/goofys#Benchmark).


Random write is not supported. goofys is more suitable for read-only scenarios.


You can use goofys based on your business requirements.

### Procedure


To mount an OSS bucket to a local file system by using goofys, perform the following steps:


-

Install goofys.


 The following items provide examples on how to run commands to install goofys in Linux and macOS. For more information about how to run commands to install goofys in other operating systems, visit [Installation](https://github.com/kahing/goofys#Installation).


-

Linux


`shell
curl -SL "https://github.com/kahing/goofys/releases/latest/download/goofys" -o $HOME/goofys
chmod u+x $HOME/goofys
`


-

Mac


`shell
brew cask install osxfuse
brew install goofys
`


-

Configure account information that is used to access the bucket.


-

Run the following command to create a configuration file:


`shell
mkdir ~/.aws
`


-

Run the following command to open the configuration file:


`shell
vi ~/.aws/credentials
`


-

Specify the AccessKey pair. The AccessKey pair consists of an AccessKey ID and an AccessKey secret.


`shell
[default]
aws_access_key_id =  The AccessKey ID that is used to access OSS.
aws_secret_access_key = The AccessKey secret that is used to access OSS.
`


-

Mount the bucket.


In the following example, the examplebucket bucket in the China (Hangzhou) region is mounted to /mnt/oss-bucket.


-

Run the following command to create a mount target:


`shell
mkdir /mnt/oss-bucket
`


-

Run the following command to mount the examplebucket bucket to /mnt/oss-bucket:


`shell
$HOME/goofys --endpoint http://oss-cn-hangzhou.aliyuncs.com --subdomain examplebucket /mnt/oss-bucket
`


> NOTE:

> NOTE: 


> NOTE: Note 

-

The -- subdomain option in the preceding example is required to enable the virtual domain name. Other options, such as the bucket that you want to mount, the endpoint of the region in which the bucket is located, and the mount target, can be replaced based on your requirements.

-

If an ECS instance is located in the same region as the OSS bucket, you can use the internal endpoint oss-cn-hangzhou-internal.aliyuncs.com to access the OSS bucket from the ECS instance.


## Rclone


Rclone is a command line program that is used to manage data in the cloud and supports data synchronization among more than 50 cloud storage services. Rclone allows you to mount buckets to local file systems in Windows. This way, you can use the buckets in the same manner that you use local disks to share data.

### Key features


-

Supports file synchronization, file transfer, file encryption, and bucket mounting.

-

Allows you to mount a bucket to a local file system in various operating systems, and provides services by using various protocols.


For more information, visit [Rclone syncs your files to cloud storage](https://rclone.org/).

### Procedure


To mount an OSS bucket to a local file system in Windows by using Rclone, perform the following steps:


-

Follow on-screen instructions to download and install Winfsp.


 In this example, winfsp-1.12.22339 is downloaded. To download winfsp-1.12.22339, visit [WinFsp 2023t](https://github.com/winfsp/winfsp/releases).

-

Download Rclone.


In this example, rclone-v1.60.1-windows-amd64 is downloaded. To download rclone-v1.60.1-windows-amd64, visit [Downloads](https://rclone.org/downloads/). Rclone is a command line program. After you download the installation package, you need to only decompress it to a local directory, such as D:\Rclone.

-

Configure Rclone.


-

Add D:\Rclone to environment variables.

-

Open a command-line interface (CLI), enter rclone --version, and then press Enter.


If rclone 1.60.1 is returned, Rclone is installed.

-

Enter the rclone config command, and press Enter.

-

Enter n, press Enter, and then create a new remote.


In this example, the new remote is named test-remote.

-

Enter a disk name, such as oss-disk, and press Enter.

-

Select the option that contains Amazon S3 Compliant Storage or enter 5, and press Enter.

-

Select the option that contains Alibaba Cloud Object Storage System (OSS) or enter 2, and press Enter.

-

After env_auth> is displayed on the CLI, press Enter.

-

After access_key_id> is displayed on the CLI, enter the AccessKey ID that is used to access OSS and press Enter.

-

After secret_access_key> is displayed on the CLI, enter the AccessKey secret that is used to access OSS and press Enter.

-

After endpoint> is displayed on the CLI, enter the endpoint that is used to access OSS and press Enter.


For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to oss-cn-hangzhou.aliyuncs.com. If an ECS instance that runs Windows is located in the same region as the OSS bucket, you can use the internal endpoint oss-cn-hangzhou-internal.aliyuncs.com to access the OSS bucket from the ECS instance.

-

After acl> is displayed on the CLI, select the object access control list (ACL) and press Enter.


This option is available only for newly uploaded objects. You can select the object ACL based on your requirements. In this example, 1 is entered to set the object ACL to default. default indicates that the object ACL is private.

-

After storage_class> is displayed on the CLI, select the object storage class and press Enter.


In this example, 1 is entered to set the object storage class to default. default indicates that the object storage class is inherited from the bucket.

-

After Edit advanced config?(y/n) is displayed on the CLI, enter n and press Enter.

-

Enter q to complete the configurations.

-

Mount the bucket.


The following sample code provides an example on how to mount a bucket named examplebucket to E: and use D:\disk-cache as the cache directory:


`shell
rclone mount oss-disk:/examplebucket E: --cache-dir D:\disk-cache --vfs-cache-mode writes
`


If the "The service rclone has been started" message is returned, the examplebucket is mounted to E:. In this case, you can view examplebucket(E:).

Thank you! We've received your  feedback.