# Object-level operations

You can call this operation to query the tags of an object.

Versioning

By default, when you call GetObjectTagging to query the tags of an object, only the tags of the current version of the object are returned. You can specify the versionId parameter in the request to query the tags of a specified version of an object. If the current version of the object is a delete marker, OSS returns 404 Not Found.

Syntax
 
GET /objectname?tagging
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 20 Mar 2019 02:02:36 GMT
Authorization: SignatureValue
Request headers

All headers in a GetObjectTagging request are common request headers. For more information, see Common request headers.

Response headers

All headers in the response to a GetObjectTagging request are common response headers. For more information, see Common response headers.

Response elements

Element

	

Type

	

Description




Tagging

	

Container

	

The container used to store the collection of tags.

Child nodes: TagSet




TagSet

	

Container

	

The collection of tags.

Parent nodes: Tagging

Child nodes: Tag




Tag

	

Container

	

The collection of tags.

Parent nodes: TagSet

Child nodes: Key and Value




Key

	

String

	

The key of the object tag.

Parent nodes: Tag

Child nodes: none




Value

	

String

	

The value of the object tag.

Parent nodes: Tag

Child nodes: none

Examples

Query the tags of an object in an unversioned bucket.

In this example, an object named objectname is stored in an unversioned bucket named bucketname. A GetObjectTagging request is sent to query the {a:1} and {b:2} tags of objectname. After the tags of the object are obtained, 200 OK is returned.

Sample requests

 
GET /objectname?tagging
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 20 Mar 2019 02:02:36 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample responses

 
200 (OK)
content-length: 209
server: AliyunOSS
x-oss-request-id: 5C919F38461FB4282600****
date: Wed, 20 Mar 2019 02:02:32 GMT
content-type: application/xml
<?xml version="1.0" encoding="UTF-8"?>
<Tagging>
  <TagSet>
    <Tag>
      <Key>a</Key>
      <Value>1</Value>
    </Tag>
    <Tag>
      <Key>b</Key>
      <Value>2</Value>
    </Tag>
  </TagSet>
</Tagging>

Query the tags of an object in a versioned bucket.

In this example, an object named objectname is stored in a versioned bucket named bucketname. A GetObjectTagging request is sent to query the {age:18} tags of the specified version of objectname. After the tag of the specified version of the object is obtained, 200 OK is returned.

Sample requests

 
GET /objectname?tagging&versionId=CAEQExiBgID.jImWlxciIDQ2ZjgwODIyNDk5MTRhNzBiYmQwYTZkMTYzZjM0****
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 24 Jun 2020 08:50:28 GMT
Authorization: OSS qn6q**************:77Dv****************

Sample responses

 
200 (OK)
content-length: 161
server: AliyunOSS
x-oss-request-id: 5EF313D44506783438F3****
date: Wed, 24 Jun 2020 08:50:28 GMT
content-type: application/xml
x-oss-version-id: CAEQExiBgID.jImWlxciIDQ2ZjgwODIyNDk5MTRhNzBiYmQwYTZkMTYzZjM0****
<?xml version="1.0" encoding="UTF-8"?>
<Tagging>
  <TagSet>
    <Tag>
      <Key>age</Key>
      <Value>18</Value>
    </Tag>
  </TagSet>
</Tagging>
OSS SDKs

You can use OSS SDKs for the following programming languages to call GetObjectTagging operation:

Java

Python

Go V2

PHP

C++

.NET

Node.js

iOS

ossutil

For information about the ossutil command that corresponds to the GetObjectTagging operation, see get-object-tagging.

Error codes

Error code

	

HTTP status code

	

Description




FileAlreadyExists

	

409

	

The error message returned because the object whose tagging configurations you want to query is a directory within a bucket with the hierarchical namespace feature enabled.