# what is an object

In Object Storage Service (OSS), an object is the basic unit of data storage and is similar to a file. Any file, such as a document, image, or video, is stored as an object in a [bucket](https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-overview) for management.

## Components of an object


-

Key: The name of the object. It is used to query the object and must be unique.

-

Data: The actual data of the object. It consists of a sequence of bytes.

-

Object Meta: The metadata of the object. Metadata is a set of key-value pairs that describe the object's properties, such as its last modification time and size. You can also use metadata to store custom information.

-

Version ID: If you enable the [versioning](https://www.alibabacloud.com/help/en/oss/user-guide/manage-objects-in-a-versioning-enabled-bucket) feature, you can save multiple versions of an object. Each time you upload an object with a name that already exists, OSS creates a new version and assigns it a unique version ID. This ID is used to access and manage specific versions of the object.

## Object naming (Key)


Each object has a unique name, called a Key. For example, the key "exampledir/example.jpg" represents the file example.jpg in the exampledir folder.
In SDK documentation, the Key is also referred to as ObjectKey, ObjectName, or object name. These terms have the same meaning.
#### Naming conventions


-

Use UTF-8 encoding.

-

The length must be between 1 and 1,023 bytes.

-

Do not start with a forward slash (/) or a backslash (\).

-

Keys are case-sensitive.

#### Naming recommendations


-

Use meaningful names, such as filenames, dates, or user IDs, to make objects easier to search for and understand.

-

Use prefixes to organize data. You can create a hierarchy using prefixes such as dates, user IDs, or regions.

-

Ensure name uniqueness. You can include random numbers or UUIDs in object names to avoid conflicts.

#### Naming examples








| Object location in the bucket | Key representation |
| --- | --- |
| An object named exampleobject.txt is stored in the root directory of the examplebucket bucket. | exampleobject.txt |
| An object named exampleobject.jpg is stored in the destdir directory within the root directory of the examplebucket bucket. | destdir/exampleobject.jpg |


## Display of OSS directories


In OSS, traditional file system concepts like files and folders do not exist. To enhance user experience, forward slashes (/) are used in object keys to mimic a folder structure, such as exampledir/example.jpg. The given example simulates exampledir as a folder and example.jpg as a file within exampledir. This folder-like structure is visible in the OSS console and graphical tools like ossbrowser. However, the object key remains exampledir/example.jpg. For more information, see [Manage directories](https://www.alibabacloud.com/help/en/oss/user-guide/manage-directories).

## Object types


Objects can be categorized into four types based on their creation methods. The following table describes these four types.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Objects cannot be converted from one type to another. For example, a Normal object cannot be converted to a Multipart or Appendable object.











(https://www.alibabacloud.com/help/en/oss/user-guide/simple-upload#concept-bws-3bb-5db)
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1823704671/CAEQThiBgIDp0JyvzhkiIGNmN2RjZjhiYTk0NTRkOWQ4MTQ2M2FjZmE0OGY1NTU04940965_20250220112557.441.svg)

-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload#concept-wzs-2gb-5db)


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/append-upload-11#concept-ls5-yhb-5db)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putsymlink)


(https://www.alibabacloud.com/help/en/oss/user-guide/configure-symbolic-links)


| Type | Definition | Description |
| --- | --- | --- |
| Normal | Objects of this type are created using simple upload. | If multiple users upload objects with identical name to a bucket that has versioning disabled or suspended, the most recently uploaded object overwrites the previous one. Only the last uploaded object is stored. For example, if User A uploads an object after User B, the object from User A is retained and replaces the object from User B. If multiple users upload objects with identical names to a versioning-enabled bucket, OSS creates a new version of the object for each upload operation and assigns a unique version ID to the new version. OSS identifies the latest version of an object based on the upload start time. For example, if User A and User B upload objects with identical name to a versioning-enabled bucket, and User B begins the upload after User A, the object uploaded by User B will be designated as the latest version. |
| Multipart | Objects of this type are created using multipart upload. | If you combine uploaded parts into a complete object with identical name to an existing object in a bucket that has versioning disabled or suspended, the new object replaces the existing one. Only the most recently combined object is retained. If you combine uploaded parts into a complete object with identical name to an existing object in a versioning-enabled bucket, OSS creates a new version of the object and assigns it a unique version ID. The most recently combined object is designated as the latest version. |
| Appendable | Objects of this type are created using append upload. | When data is appended to an appendable object, OSS does not create a new version of the object, regardless of the versioning status. The data is directly appended to the original object. |
| Symlink | Objects of this type are created using symbolic links created by calling the PutSymlink operation. | You can use symbolic links to access objects that are frequently accessed. |


Delete markers


OSS uses a special type of object marker called delete marker. When you call the [DeleteObject](https://www.alibabacloud.com/help/en/oss/developer-reference/deleteobject) operation to delete an object in a versioning-enabled or versioning-suspended bucket, OSS generates a delete marker for the object. If no version ID is specified during deletion, OSS assigns the delete marker as the latest version of the object. This ensures the data in the object is preserved and can be restored even after deletion. However, if a version ID is specified, OSS deletes the specific version and does not generate a delete marker.

## Features

## Upload objects








(https://www.alibabacloud.com/help/en/oss/user-guide/simple-upload)


(https://www.alibabacloud.com/help/en/oss/user-guide/multipart-upload)


(https://www.alibabacloud.com/help/en/oss/user-guide/resumable-upload)


(https://www.alibabacloud.com/help/en/oss/user-guide/upload-callbacks-12)


(https://www.alibabacloud.com/help/en/oss/user-guide/uploading-objects-to-oss-directly-from-clients/)


(https://www.alibabacloud.com/help/en/oss/user-guide/form-upload)


(https://www.alibabacloud.com/help/en/oss/user-guide/append-upload-11)


(https://www.alibabacloud.com/help/en/oss/developer-reference/rtmp-based-stream-ingest)


| Procedure | Description |
| --- | --- |
| Simple upload | Use the PutObject API operation to upload a single file smaller than 5 GB. This method is suitable for uploads that can be completed in a single HTTP request. |
| Multipart upload | Split a file into multiple parts and upload them separately. After all parts are uploaded, call the CompleteMultipartUpload API operation to combine the parts into a single object. |
| Resumable upload | Specify a checkpoint in a checkpoint file. If an upload fails due to a network error or program crash, the upload resumes from the recorded checkpoint to transfer the remaining parts. |
| Upload callback | OSS can send a callback to an application server after a file upload is complete. To implement a callback, include the corresponding callback parameters in the request sent to OSS. |
| Direct client upload | Upload files directly from a client to OSS. This method avoids routing files through your application server, which improves upload speed and saves server resources. |
| Form upload | Use the PostObject API operation to upload a file from an HTML form. The uploaded file cannot exceed 5 GB. |
| Append upload | Append content directly to the end of an existing Appendable object. |
| RTMP-based stream ingest | You can use the Real-Time Messaging Protocol (RTMP) to ingest H.264-encoded video streams and AAC-encoded audio streams into OSS. The uploaded audio and video data can be played on demand or utilized for livestreaming in scenarios where latency is not a critical factor. |


## Download objects








(https://www.alibabacloud.com/help/en/oss/user-guide/simple-download-1)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-resumable-download)


(https://www.alibabacloud.com/help/en/oss/user-guide/share-objects-by-url)


(https://www.alibabacloud.com/help/en/oss/user-guide/conditional-download)


| Procedure | Description |
| --- | --- |
| Simple download | Use the GetObject API operation to download an uploaded file. This method is suitable for downloads that can be completed in a single HTTP request. |
| Resumable download | Download a file starting from a specified position. When downloading large files, you can download them in multiple parts. If the download is interrupted, you can resume it from where it left off. |
| Use a signed URL to download an object | After a file is uploaded to a bucket, you can share its URL with third parties for preview or download. |
| Conditional download | Objects are downloaded only if their content has changed, determined by the last modified time or ETag. This feature ensures downloads are triggered solely when updates occur, avoiding unnecessary repeated downloads. |


## Manage objects








(https://www.alibabacloud.com/help/en/oss/user-guide/list-objects-18)


(https://www.alibabacloud.com/help/en/oss/user-guide/copy-objects-16)


(https://www.alibabacloud.com/help/en/oss/user-guide/rename-objects)


(https://www.alibabacloud.com/help/en/oss/user-guide/search-for-objects)


(https://www.alibabacloud.com/help/en/oss/user-guide/restore-objects-for-access)


(https://www.alibabacloud.com/help/en/oss/user-guide/delete-objects-18)


(https://www.alibabacloud.com/help/en/oss/user-guide/object-tagging-8)


(https://www.alibabacloud.com/help/en/oss/user-guide/configure-symbolic-links)


(https://www.alibabacloud.com/help/en/oss/user-guide/manage-object-metadata-10/)


(https://www.alibabacloud.com/help/en/oss/user-guide/single-connection-bandwidth-throttling-4)


(https://www.alibabacloud.com/help/en/oss/user-guide/query-objects)


(https://www.alibabacloud.com/help/en/oss/user-guide/delete-parts)


(https://www.alibabacloud.com/help/en/oss/user-guide/use-csg-to-attach-oss-buckets-to-ecs-instances)


| Procedure | Description |
| --- | --- |
| List objects | Objects in a bucket are listed in alphabetical order by default. You can list all objects in the current bucket, objects with a specific prefix, or a specific number of objects, as needed. |
| Copy objects | Copy a file from a source bucket to a destination bucket in the same region without changing the file content. |
| Rename objects | You can rename an object in a bucket. |
| Search for objects | When a bucket contains many objects, OSS supports searching for and locating a target file quickly by specifying a filename prefix. |
| Restore files | Before accessing an object in Cold Archive or Deep Cold Archive, you must initiate a restoration process for the object. |
| Delete objects | Delete objects that you no longer need to keep in a bucket using various methods. |
| Tag objects | OSS supports using tags to classify objects in a bucket. You can set lifecycle rules and access permissions for objects with the same tag. |
| Create symbolic links | The symbolic link feature is used for quick access to frequently used objects in a bucket. After you set up a symbolic link, you can open the object quickly using the symbolic link file. |
| Manage object metadata | Object metadata describes the properties of a file. It includes standard HTTP headers and user-defined metadata (User Meta). You can set file HTTP headers to customize HTTP request policies, such as cache policies and forced download policies. You can also set user-defined metadata to identify the purpose or properties of an object. |
| Single-connection bandwidth throttling | When a client accesses files in OSS, it can consume a large amount of bandwidth, which may affect other applications. You can use the single-connection bandwidth throttling feature provided by OSS to control traffic during operations such as uploading and downloading files. This ensures sufficient network bandwidth for other applications. |
| Querying files | Use SelectObject to execute an SQL statement on a target file and return the execution result. |
| Delete parts | During a multipart upload, if some parts are no longer needed, you can call the AbortMultipartUpload API operation to delete these incomplete parts. |
| Use CSG to attach OSS buckets to ECS instances | To enable multiple users to access resources in an OSS bucket from different locations and devices, you can use Cloud Storage Gateway (CSG) to map the OSS bucket to a shared file storage system. This allows users to perform operations on OSS resources as they would with local files and disks. |


## FAQ


-

[FAQs about uploading objects](https://www.alibabacloud.com/help/en/oss/usage-query/)

-

[FAQs about object downloads](https://www.alibabacloud.com/help/en/oss/download-file-faq/)

-

[FAQs about direct client uploads](https://www.alibabacloud.com/help/en/oss/direct-transmission-faq/)

-

[FAQs about object management](https://www.alibabacloud.com/help/en/oss/manage-files-faq/)

Thank you! We've received your  feedback.