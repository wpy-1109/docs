# Search for objects based on metadata and semantic content

You can create a data index and use the metadata and semantic content of objects as index conditions to quickly search for images, videos, documents, and audio files in Object Storage Service (OSS).

## Why use data indexing?


Traditional file search methods exhibit significant limitations, which OSS Data Indexing effectively addresses:


























| Traditional Search | OSS Data Indexing |
| --- | --- |
| Complex operations: Requires using ListObject to traverse data and extract metadata for building custom databases, resulting in time-consuming and cumbersome workflows. | Simplified operations: Eliminates the need for data migration or custom search systems by enabling direct filtering and statistics via automatically built OSS indexes. |
| Low retrieval performance: Slow speed and inefficiency when handling massive data. | High-performance retrieval: Supports second-level indexing and aggregation, scaling to multi-billion-file index libraries. |
| Limited retrieval capabilities: Restricted to OSS metadata-based searches. | Multi-modal support: Satisfies diverse requirements through advanced methods such as content semantics and file characterization. |


## Supported data indexing methods


OSS supports MetaSearch and AISearch. The following table describes the preceding data indexing methods.











![query.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8278996371/p849375.png)


![apple.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8278996371/p849366.png)


![标量检索.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8278996371/p849404.png)


![向量检索.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8278996371/p849444.png)


| Item | MetaSearch | AISearch |
| --- | --- | --- |
| Description | Search for specific objects based on metadata attributes, such as object metadata, ETags, and tags. | Search for specific objects based on the information about documents, images, videos, and audio files. You can specify semantic content as index conditions, and OSS compares the semantic content with objects in OSS. |
| Scenario | Object query and statistics | Multimodal search and complex object search |
| Sample index condition | Search for Standard objects whose access control list (ACL) is private and which are uploaded on September 14, 2024 | Search for images related to the semantic content "apple" |
| Sample result | Return Standard objects whose ACL is private and which are uploaded on September 14, 2024 | Return images related to the semantic content "apple" |


## Instructions on selecting a data indexing method

### Comparison of search conditions


| Search condition | MetaSearch | AISearch |
| --- | --- | --- |
| OSS metadata | ✅ | ✅ |
| Object tags and ETags | ✅ | ✅ |
| User metadata | ❌ | ✅ |
| Multimedia metadata | ❌ | ✅ |
| Semantic content | ❌ | ✅ |


-

For more information about the fields and operators supported by MetaSearch, see [Appendix: Fields and operators supported in scalar search](https://www.alibabacloud.com/help/en/oss/developer-reference/appendix-supported-fields-and-operators).

-

For more information about the fields and operators supported by AISearch, see [Appendix: Fields and operators supported by AISearch](https://www.alibabacloud.com/help/en/oss/developer-reference/appendix-list-of-fields-and-operators-for-vector-retrieval).

### Typical scenarios


-

Cost Optimization Analytics
Identify non-critical or cold data by using OSS metadata such as timestamps to reduce storage costs.


MetaSearch is recommended.

-

Data Validation
Verify data cleansing results by comparing metrics such as data amount and file size via OSS metadata after data processing or data cleansing.


MetaSearch is recommended.

-

Data Auditing
Perform deep statics and auditing for file content by integrating OSS metadata with vector semantics to meet compliance requirements.


Vector search is recommended.

-

Multi-modal Search
Perform search based on multimedia data and vector semantics for advanced search scenarios, such as search in chat history, media asset, and semantics.


Vector search is recommended.

## Process


The following figures show how MetaSearch and AISearch work.

### How MetaSearch works


The following figure shows how to use MetaSearch to search for objects based on metadata attributes.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3401541571/CAEQMRiBgMCzpofPnhkiIDZjMGQ5NjIzYjc1MjQwMTViMTBkMTBlYzQzM2M2MTAx4668973_20240911184610.007.svg)

-

You upload files, such as images, videos, documents, and audio files, from an application to an OSS bucket.

-

You use a RAM user that has the permissions to manage OSS to enable data indexing for the bucket and select MetaSearch.

-

OSS uses the default index table structure to automatically create data indexes that contain OSS metadata, object ETags, and object tags.

-

The application calls the [DoMetaQuery](https://www.alibabacloud.com/help/en/oss/developer-reference/dometaquery) operation to search for objects based on metadata attributes.

-

OSS returns the objects that meet the search conditions.

### How AISearch works


The following figure shows to use AISearch to search for objects based on metadata attributes and semantic content.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/3401541571/CAEQMRiBgMD2h4vPnhkiIDExMzY1NDIyZDljOTQ5MDZhMTQzMDYwYzBkNWVlZGUz4668973_20240911184610.007.svg)

-

You upload files, such as images, videos, documents, and audio files, from an application to an OSS bucket.

-

You use a RAM user that has the permissions to manage OSS to enable data indexing for the bucket and select AISearch.

-

OSS uses the default index table structure and Embedding model to automatically create data indexes that contain OSS metadata, object ETags, object tags, user metadata, multimedia metadata, and semantic content.

-

The application calls the [DoMetaQuery](https://www.alibabacloud.com/help/en/oss/developer-reference/dometaquery) operation to search for objects based on metadata attributes and semantic content.

-

OSS returns the objects that meet the search conditions.

## Get started


For more information about how to use MetaSearch and AISearch, see:


-

[Use MetaSearch to search for OSS objects based on metadata attributes](https://www.alibabacloud.com/help/en/oss/user-guide/scalar-retrieval/)

-

[Use AISearch to quickly search for objects based on semantic content and multimedia metadata](https://www.alibabacloud.com/help/en/oss/user-guide/vector-retrieval/)


For further instructions in different use cases, see:


-

Statics scenarios: [Tutorial: Use data indexing to search for objects that meet specific conditions in large volumes of data](https://www.alibabacloud.com/help/en/oss/user-guide/tutorial-of-using-data-indexing-for-large-scale-statistical-analysis)

-

Multimodal search: [Tutorial: Use data indexing to search for multimodal data](https://www.alibabacloud.com/help/en/oss/user-guide/tutorial-oss-data-indexing-used-in-multimodal-retrieval)

-

AI scenarios: [Create an intelligent semantic indexing system for IP cameras](https://www.alibabacloud.com/help/en/oss/user-guide/build-an-intelligent-semantic-retrieval-system-for-ipc-devices)

## References


For details of the performance of different indexing methods, see:


-

[Use MetaSearch to search for OSS objects based on metadata attributes](https://www.alibabacloud.com/help/en/oss/user-guide/scalar-retrieval/#3cc0cef9b4tvi)

-

[Use AISearch to quickly search for objects based on semantic content and multimedia metadata](https://www.alibabacloud.com/help/en/oss/user-guide/vector-retrieval/#5192db862ewk5)

Thank you! We've received your  feedback.