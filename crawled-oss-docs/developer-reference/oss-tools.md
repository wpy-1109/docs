# Overview of OSS management tools

Alibaba Cloud Object Storage Service (OSS) provides a variety of management tools for tasks like uploading large files, generating signed URLs, migrating data, and mounting buckets. In addition to the official tools, third-party tools and community-developed plugins are also available to enhance and simplify the use of OSS.

## Official tools

### Command-line tools


Use these tools when you need to manage OSS through a terminal or automated scripts.








(https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/)


-


-


-




(https://www.alibabacloud.com/help/en/oss/developer-reference/overview-59/#concept-cnr-3d4-vdb)


-


-


-


(https://www.alibabacloud.com/help/en/cli/what-is-alibaba-cloud-cli)


(https://www.alibabacloud.com/help/en/cloud-shell/use-alibaba-cloud-cli-to-manage-data-in-oss)


(https://www.alibabacloud.com/help/en/oss/overview-62#concept-jv4-ssb-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/)


-


-


-


-


| Tool | Description |
| --- | --- |
| ossutil 2.0 (Recommended) | The new version of the OSS command-line management tool. Supports multi-level commands (high-level and API-level) for managing buckets and objects, including concurrent file uploads, resumable uploads, and directory uploads/downloads.Supports external access credentials, OpenID Connect (OIDC) credentials, and automatically retrieves the role name when using an Instance RAM Role access credential.Use the --output-format option to change the output format from the default raw (XML or text) to JSON, YAML, or XML. |
| ossutil 1.0 | The command-line management tool for OSS.Provides commands for managing buckets and objects.Supports concurrent file uploads and resumable uploads.Supports uploading and downloading directories (folders). |
| Alibaba Cloud CLI | A unified Command Line Interface (CLI) for managing Alibaba Cloud resources. You can use the standardized command format of the Alibaba Cloud CLI to quickly manage your data in OSS. For specific operations, see Use Alibaba Cloud CLI to manage data in OSS. |
| osscmd (deprecated) | This CLI has been unavailable since July 31, 2019. Its features are now part of ossutil.Provided a complete set of commands for managing buckets and objects.Supported Windows and Linux platforms.Limitations: Only compatible with Python 2.5–2.7. Python 3.x is not supported.Lacks support for Infrequent Access (IA), Archive, Cold Archive, Deep Cold Archive, cross-region replication (CRR), or mirroring-based back-to-origin. |


### Graphical management tools


Use these tools to browse and manage objects through a graphical interface.








(https://www.alibabacloud.com/help/en/oss/developer-reference/ossbrowser-2-0-overview/)


-


-


-


-


-


(https://www.alibabacloud.com/help/en/oss/developer-reference/use-ossbrowser#concept-xmg-h33-wdb)


-


-


-


-


-


-


-



-


-


| Tool | Description |
| --- | --- |
| ossbrowser 2.0 (recommended) | A completely upgraded graphical management tool.As an upgrade to the legacy ossbrowser, ossbrowser 2.0 supports most of its features.Includes additional sign-in methods, such as scanning a QR code with the Alibaba Cloud app, Alipay, or DingTalk. Lets you add buckets to a favorites list.Lets you edit files while browsing.Features a redesigned UI and interaction model for easier file management and transfers. |
| ossbrowser | A graphical management tool. Provides features similar to Windows Explorer.Supports direct file browsing.Supports uploading and downloading directories (folders).Supports concurrent file uploads and resumable uploads.Supports graphical policy authorization for RAM users.Supports Windows, Linux, and Mac platforms.Limitations: Transfer speed and performance are lower than with ossutil.Only supports moving or copying objects smaller than 5 GB.The maximum size for a single file upload is 48.8 TB. |


### Data migration and synchronization tools 


Use these tools to migrate or synchronize data from other sources to OSS.








(https://www.alibabacloud.com/help/en/data-online-migration/product-overview/what-is-data-online-migration)


(https://www.alibabacloud.com/help/en/data-transport/product-overview/what-is-data-transport)


(https://www.alibabacloud.com/help/en/data-online-migration/user-guide/ossimport-overview)


-


-


-


-


-


| Tool | Description |
| --- | --- |
| Data Online Migration (Recommended) | A no-code, visual, and unified online migration service. You can efficiently and securely migrate large amounts of data from various sources to OSS with simple configurations.Supports various storage services, including AWS S3, Tencent Cloud COS, Huawei Cloud OBS, Volcengine TOS, Google Cloud GCS, Microsoft Azure Blob, and self-hosted object storage services compatible with the S3 protocol. You can submit migration jobs online and monitor the process without setting up a migration environment. |
| Offline migration (Data Transport) | A data migration service that uses customized migration devices, Data Transport, to migrate terabyte- to petabyte-scale local data to the cloud. It is designed to improve the efficiency of large-scale data transfers and solve data security challenges.Offline migration is suitable for scenarios such as migrating entire data centers to the cloud, or archiving files and historical image data for large enterprises. It is designed for terabyte- to petabyte-scale data migration, using physical media for data collection and transport to overcome public network bandwidth bottlenecks and significantly improve migration efficiency. |
| ossimport | A data synchronization tool for OSS. Synchronizes files from various third-party data sources to OSS. Supports distributed deployment, allowing you to use multiple servers to migrate data in batches. Supports migration of terabyte-scale data and above. Supports Windows and Linux platforms.Requires Java 7. |


### File system mounting tools


These tools mount a bucket as a local file system directory, letting you manage objects as if they were local files.








(https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-2-0/#fbd0fa1fc1w0w)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-2-0/#fbd0fa1fc1w0w)(https://www.alibabacloud.com/help/en/oss/developer-reference/oss-connector-overview/#ea05a4d314inl)


-


-


-


-


-


-


-

(https://www.alibabacloud.com/help/en/oss/developer-reference/mount-buckets-using-ossfs-2-0#2d5d0d7ad2zw0)

-


-


-

(https://www.alibabacloud.com/help/en/oss/developer-reference/mount-buckets-using-ossfs-2-0#2d5d0d7ad2zw0)

-


-

(https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs-2-0/#42610ceb86ega)


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossfs#concept-kkp-lmb-wdb)


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



-


-


| Tool | Description |
| --- | --- |
| ossfs 2.0 (Recommended) | ossfs 2.0 is a completely re-architected version designed for new, compute-intensive applications. It delivers comprehensive performance upgrades but has certain limitations on POSIX semantics, and is the primary version for future development. Use ossfs 2.0 (preview) if you are working on new applications such as AI training, inference, or autonomous driving simulation and find it inconvenient to use the OSS SDK or OSS Connector for AI/ML to accelerate model training.Provides basic POSIX compatibility, focusing on leveraging the server-side read/write capabilities of OSS. Offers high-performance sequential reading and writing of large objects through end-to-end optimizations. Provides efficient concurrent loading of small objects through efficient metadata management.Limitations:The following limitations apply when mapping a remote bucket to a local file system with ossfs 2.0: Permission requirements: Ensure that the AccessKey has full permissions for the target bucket or prefix-related resources. Otherwise, the mount may fail or some functions may not work correctly. Storage class limitations: Mounting buckets of the Archive, Cold Archive, or Deep Cold Archive storage class is not supported.Object name limitations: The maximum length of an object name is 255 characters (following Linux limitations). Objects or directories in OSS that exceed this limit are not visible in the mount point.Write limitations: Random writes are not supported. By default, writes create non-appendable objects. The default part size for writes is 8,388,608 bytes (8 MiB), which means the maximum file size for writes is 83,886,080,000 bytes (78.125 GiB). You can configure the shard size using the upload_buffer_size mount option.Rename operations (non-atomic)Files: The file is first copied, and then the remote source file is deleted.Directories: After all files are copied, the source files are deleted in a batch. When renaming a directory, the default limit for the number of descendant files is 2 million. You can configure this limit using the rename_dir_limit mount option.Concurrent write consistency: If multiple clients mount the same bucket and write to the same file simultaneously, data consistency cannot be guaranteed.POSIX API compatibility: Partially compatible. For more information, see Support for POSIX API operations. |
| ossfs 1.0 | A bucket mounting tool. ossfs 1.0 mounts an OSS bucket to the local file system of a Linux system. After mounting, you can operate on OSS objects through the local file system to access and share data. Supports most features of a POSIX file system, including file reads and writes, directories, link operations, permissions, UID, GID, and extended attributes.Supports uploading large files using the multipart upload feature of OSS.Supports MD5 validation to ensure data integrity.Limits:The following limits apply when you use ossfs 1.0 to map remote bucket data and features to a local file system:Not suitable for high-concurrency read and write scenarios.Note In the implementation of ossfs 1.0, both reads and writes require disk caching. In high-concurrency read and write scenarios, disk performance is a bottleneck for both operations.In the implementation of ossfs 1.0, there is contention between concurrent read and write requests, which affects bandwidth.Does not support hard links for files.Does not support mounting buckets of the Archive Storage, Cold Archive, or Deep Cold Archive storage class.Editing an uploaded file causes the file to be re-uploaded.Metadata operations, such as list directory, have poor performance because they require remote access to the OSS server.Renaming a file or folder may cause errors. If the operation fails, data inconsistency may occur.If multiple clients mount the same OSS bucket, you must maintain data consistency yourself. Plan your file usage to avoid situations where multiple clients write to the same file. |


### AI tools


Use these tools to efficiently access and store OSS data in AI scenarios.








(https://www.alibabacloud.com/help/en/oss/developer-reference/oss-connector-for-ai-ml)


-


-


-


-


-


-


-


-


| Tool | Description |
| --- | --- |
| OSS Connector for AI/ML | A Python library for efficiently accessing and storing OSS data in PyTorch training tasks.Supports building map-style datasets that are suitable for random access, making it easy to quickly retrieve specific data during training.Supports building iterable-style datasets that are suitable for sequential stream access and can also handle continuous data streams.Supports creating OssCheckpoint objects to directly load checkpoints from the training process to OSS.Limits:Operating system: Linux x86-64glibc: >=2.17Python: 3.8–3.12PyTorch: >=2.0Using the OSS Checkpoint feature requires the Linux kernel to support userfaultfd |


### FTP tools


(https://www.alibabacloud.com/help/en/oss/developer-reference/ossftp-overview/#concept-d4b-g2t-vdb)


-


-


-


-


| Tool | Description |
| --- | --- |
| ossftp | An FTP tool for managing objects. Use FTP clients such as FileZilla, WinSCP, and FlashFXP to operate on OSS.It is essentially an FTP server that receives FTP requests and maps file and folder operations to OSS operations.Based on Python 2.7 and later.Supports Windows, Linux, and macOS platforms. |


### Development and authorization tools


Use these tools for development integration and fine-grained permission management.








(https://www.alibabacloud.com/help/en/oss/ram-policy-editor#concept-mx2-yb4-vdb)


-


-


| Tool | Description |
| --- | --- |
| RAM Policy Editor | An automated generation tool for OSS authorization policies. Use this tool when you need to generate custom authorization policies.It can automatically generate authorization policies based on your requirements. You can also use these authorization policies in custom policies in RAM.Supports Chrome, Firefox, and Safari browsers. |


## Third-party tools and plugins


Contributed by community developers, these tools and plugins seamlessly integrate with common development tools and application frameworks to simplify the use of OSS.








(https://www.jetbrains.com/help/idea/big-data-tools-support.html)


-


-


-


-


-


-


(https://www.alibabacloud.com/help/en/oss/developer-reference/use-big-data-tools-to-connect-jetbrains-ides-to-oss)


(https://wordpress.com/it/plugins/hacklog-remote-attachment)


(https://www.alibabacloud.com/help/en/oss/developer-reference/how-to-store-remote-attachments-from-wordpress-websites-to-oss)


(https://filezilla-project.org/)


(https://www.alibabacloud.com/help/en/oss/developer-reference/use-filezilla-to-upload-files-from-local-sites-to-oss)


| Tool | Description |
| --- | --- |
| Big Data Tools | A JetBrains IDE plugin compatible with OSS that focuses on optimizing big data workflows.Provides a user interface for working with remote file systems, including OSS.Offers file operations similar to a file manager (copy, move, rename, delete, and download files).Allows you to preview files. For CSV files, you can switch between text and table views.Makes it easy to get additional file information, such as the modification time.Allows you to preview binary files, such as Parquet.Allows you to open buckets and folders in multiple tabs.For more information, see Connect JetBrains IDEs to OSS using Big Data Tools. |
| Hacklog Remote Attachment | A WordPress plugin that lets you store attachments and media files from your WordPress site on OSS instead of on your local server. This improves site loading speed and reduces the storage pressure on the host. For more information, see How to store remote attachments on OSS for WordPress. |
| FileZilla | An easy-to-use FTP client tool that lets you upload files from a local site to OSS. This improves file storage and access efficiency and reduces the local storage burden. For more information, see How to upload local site files to OSS using FileZilla. |


Thank you! We've received your  feedback.