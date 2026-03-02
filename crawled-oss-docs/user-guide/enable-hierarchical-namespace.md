# Hierarchical namespace

Hierarchical namespace organizes objects in an OSS bucket into a directory tree. Directories become real entities, enabling atomic rename operations without listing or processing individual objects by prefix.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

Hierarchical namespace cannot be disabled after enablement. This change is permanent. Test in a non-production bucket first.


## How it works


By default, OSS uses a flat namespace. Directories are simulated by objects whose names end with a forward slash (`/`). With hierarchical namespace enabled, directories become real entities. Directory-level operations such as rename complete as a single atomic operation, regardless of object count.

### Atomic directory operations


In a flat namespace, applications may need to process millions of objects for a directory-level task. Hierarchical namespace completes these tasks in a single atomic operation on the parent directory.

### Faster data analytics


Hierarchical namespace eliminates the need to replicate or convert data before analysis. Big data analytics frameworks such as Hive and Spark write output to a temporary directory during task execution, then rename the directory after the task completes. In a flat namespace, the rename operation often takes longer than the task itself.

## Use cases


-

Data lake analytics -- Hive, Spark, or similar frameworks that rename output directories after job completion

-

Large-scale data pipelines -- workflows that reorganize directories containing many objects

-

Directory-heavy applications -- applications that create, rename, or delete directories as part of core logic

## Supported regions


Hierarchical namespace is available in the following regions only:


| Region | Region ID |
| --- | --- |
| US (Silicon Valley) | us-west-1 |
| Japan (Tokyo) | ap-northeast-1 |
| UK (London) | eu-west-1 |
| Malaysia (Kuala Lumpur) | ap-southeast-3 |


## Prerequisites


Before you begin, make sure that you have:


-

An Alibaba Cloud account with OSS activated

-

The `oss:PutBucket` permission to create buckets

## Enable hierarchical namespace


Hierarchical namespace can only be enabled when creating a bucket. It cannot be enabled on an existing bucket or disabled after enablement.


Select the hierarchical namespace option during bucket creation. For detailed steps, see [Create buckets](https://www.alibabacloud.com/help/en/oss/manage-buckets-create-buckets#task-bcz-sbz-5db).

## Directory operations


After enabling hierarchical namespace, the following directory operations are available:
(https://www.alibabacloud.com/help/en/oss/user-guide/manage-directories#section-l8o-x8m-ri6)(https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories#concept-2058101)(https://www.alibabacloud.com/help/en/oss/user-guide/manage-directories#section-sjw-h1w-hls)(https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories#concept-2058101)(https://www.alibabacloud.com/help/en/oss/user-guide/manage-directories#section-ul9-bg2-9ua)(https://www.alibabacloud.com/help/en/oss/developer-reference/manage-directories#concept-2058101)

| Operation | OSS console | Java SDK |
| --- | --- | --- |
| Create a directory | Create a directory | Java SDK |
| Rename a directory | Rename a directory | Java SDK |
| Delete a directory | Delete a directory | Java SDK |


### Create directories


-

Directory names cannot contain consecutive forward slashes (`/`).

-

Directories cannot store data. The Content-Length of a directory must be `0`.

-

The Content-Type of a directory must be `application/x-directory`.

### Rename directories or objects


-

The new name cannot match an existing directory or object name in the same bucket.

-

The parent directory in the new path must already exist. For example, to rename a directory to `destfolder/examplefolder/test`, the parent directory `destfolder/examplefolder` must exist.

### Delete directories


Recursive delete


Recursive delete removes a directory and all objects and subdirectories within it. This requires the DeleteObject permission on the directory and all its contents.


For example, to recursively delete `dest/testfolder` and its objects, grant the DeleteObject permission on both `dest/testfolder` and `dest/testfolder/*`.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

If a concurrent write request targets a directory during a recursive delete, the delete may fail.


Non-recursive delete


Non-recursive delete removes only empty directories. This requires the DeleteObject permission on the directory.

## Unsupported features


Buckets with hierarchical namespace enabled do not support the following features. Review this list before enabling hierarchical namespace.

### Bucket-level features


-

Cross-region replication (CRR)

-

Versioning

-

Bucket inventory

-

Cross-origin resource sharing (CORS)

-

Static website hosting

-

Lifecycle rules

-

Retention policies

-

Transfer acceleration

### Object-level features


-

Symbolic links

-

Append upload

-

Access control list (ACL) and tagging

-

Image processing (IMG)

-

Archive and Cold Archive objects

-

Callback

-

The RestoreObject operation for restoring Archive and Cold Archive objects

-

The `x-oss-forbid-overwrite` parameter for preventing an object from being overwritten by another object with the same name

-

The `response-content-*` parameter in GetObject requests for directories

-

LiveChannel operations

-

The DeleteMultipleObjects operation for batch deleting objects

-

The SelectObject operation for selecting content from objects

Thank you! We've received your  feedback.