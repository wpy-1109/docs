# Object-level operations

Adds tags to an object or updates the tags added to the object. Each tag added to an object is a key-value pair.

Usage notes

You can add up to 10 tags to an object. The tags added to an object must have unique tag keys.

A tag key can be up to 128 characters in length. A tag value can be up to 256 characters in length.

Tag keys and tag values are case-sensitive.

The key and value of a tag can contain letters, digits, spaces, and the following special characters:

+ - = . _ : /

If the tags of the HTTP header contain characters, you must perform URL encoding on the keys and values of the tags.

Changing tags of an object does not update the Last-Modified parameter of the object.

For more information about object tags, see Configure object tagging.

Versioning

By default, when you call PutObjectTagging to add tags to an object or update the tags configured for an object, the tags are added to the current version of the object or the tags configured for the current version of the object are updated. You can specify the versionId parameter in the request to add tags to a specified version of an object or update the tags configured for a specified version of an object. If the specified version is a delete marker, OSS returns 404 Not Found.

Request syntax
 
PUT /objectname?tagging
Content-Length: 114
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Mon, 18 Mar 2019 08:25:17 GMT
Authorization: SignatureValue
<Tagging>
  <TagSet>
    <Tag>
      <Key>Key</Key>
      <Value>Value</Value>
    </Tag>
  </TagSet>
</Tagging>            
Request elements

Element

	

Type

	

Required

	

Example

	

Description




Tagging

	

Container

	

Yes

	

N/A

	

The top-level container.

Child nodes: TagSet




TagSet

	

Container

	

Yes

	

N/A

	

The tags.

Parent nodes: Tagging

Child nodes: Tag




Tag

	

Container

	

No

	

N/A

	

The tag.

Parent nodes: TagSet

Child nodes: Key and Value




Key

	

String

	

No

	

a

	

The key of the tag.

Parent nodes: Tag

Child nodes: none




Value

	

String

	

No

	

1

	

The value of the tag.

Parent nodes: Tag

Child nodes: none

This operation also involves common request headers. For more information, see Common HTTP headers.

Examples

Add tags to an object in an unversioned bucket

In this example, an object named objectname is stored in an unversioned bucket named bucketname. A PutObjectTagging request is sent to add the {a:1} and {b:2} tags to an object named objectname. After the two tags are added to the object, 200 (OK) is returned.

Sample requests

 
PUT /objectname?tagging
Content-Length: 114
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Mon, 18 Mar 2019 08:25:17 GMT
Authorization: OSS qn6q**************:77Dv****************
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

Sample responses

 
200 (OK)
content-length: 0
server: AliyunOSS
connection: keep-alive
x-oss-request-id: 5C8F55ED461FB4A64C00****
date: Mon, 18 Mar 2019 08:25:17 GMT

Add tags to an object in a versioning-enabled bucket

In this example, an object named objectname is stored in a versioned bucket named bucketname. A PutObjectTagging request is sent to add the {age:18} tag to the specified version of objectname. After the tag is added to the object, 200 (OK) is returned.

Sample requests

 
PUT /objectname?tagging&versionId=CAEQExiBgID.jImWlxciIDQ2ZjgwODIyNDk5MTRhNzBiYmQwYTZkMTYzZjM0****
Content-Length: 90
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 24 Jun 2020 08:58:15 GMT
Authorization: OSS qn6q**************:77Dv****************
<Tagging>
  <TagSet>
    <Tag>
      <Key>age</Key>
      <Value>18</Value>
    </Tag>
  </TagSet>
</Tagging>

Sample responses

 
200 (OK)
content-length: 0
server: AliyunOSS
connection: keep-alive
x-oss-request-id: 5EF315A7FBD3EC3232B4****
date: Wed, 24 Jun 2020 08:58:15 GMT
x-oss-version-id: CAEQExiBgID.jImWlxciIDQ2ZjgwODIyNDk5MTRhNzBiYmQwYTZkMTYzZjM0****
OSS SDKs

You can use OSS SDKs for the following programming languages to call the PutObjectTagging operation:

Java

Python

Go V2

PHP

C++

.NET

Node.js

iOS

ossutil

For information about the ossutil command that corresponds to the PutObjectTagging operation, see put-object-tagging.

Error codes

Error code

	

HTTP status code

	

Description




FileAlreadyExists

	

409

	

The object for which you want to configure or update tags is a directory within a bucket that has the hierarchical namespace feature enabled.