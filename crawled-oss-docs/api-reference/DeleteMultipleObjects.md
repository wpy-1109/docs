# Object-level operations

The DeleteMultipleObjects operation deletes multiple objects from the same bucket.

Notes

A single DeleteMultipleObjects request can delete up to 1,000 objects.

If a bucket has a data replication rule and the replication policy is set to Sync Additions, Deletions, And Modifications, when you call DeleteMultipleObjects to delete objects in the bucket, the corresponding objects in the target bucket are also deleted. These objects cannot be recovered after they are deleted. If versioning is also enabled for the bucket, when you call DeleteMultipleObjects, OSS creates a delete marker for each deleted object in the bucket. This action is replicated to the target bucket, and a corresponding delete marker is created.

Deleted objects cannot be recovered. Proceed with caution. For more information about how to delete objects, see Delete objects.

Versioning

You can also use the DeleteMultipleObjects operation to delete multiple objects from a versioning-enabled bucket. If you do not specify a version ID in the delete request, a delete marker is inserted. If you specify a version ID, the specified version of the object is permanently deleted.

Permissions

By default, an Alibaba Cloud account has full permissions. RAM users or RAM roles under an Alibaba Cloud account do not have any permissions by default. The Alibaba Cloud account or account administrator must grant operation permissions through RAM policies or Bucket Policy.

API

	

Action

	

Definition




DeleteMultipleObjects

	

oss:DeleteObject

	

Deletes multiple objects from a bucket.

Request syntax
 
POST /?delete HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Content-Length: ContentLength
Content-MD5: MD5Value
Authorization: SignatureValue
<?xml version="1.0" encoding="UTF-8"?>
<Delete>
  <Quiet>true</Quiet>
  <Object>
    <Key>key</Key>
  </Object>
…
</Delete>
Request headers

OSS verifies the message body based on the following request headers before the delete operation is performed.

Name

	

Type

	

Required

	

Example

	

Description




Encoding-type

	

String

	

No

	

url2

	

The key of the object must be UTF-8 encoded. If the key contains control characters that are not supported by XML 1.0, set Encoding-type to url2 and URL-encode the key in the request. OSS then encodes the Key field in the response.

Default value: none

Valid value: url2




Content-Length

	

String

	

Yes

	

151

	

The length of the HTTP message body.

OSS verifies the received message body based on this request header. The delete operation is performed only after the message body is verified.




Content-MD5

	

String

	

Yes

	

ohhnqLBJFiKkPSBO1eNaUA==

	

The Content-MD5 header is a value generated using the MD5 algorithm. This header is used to check whether the message content is the same as the content that was sent. After you specify the Content-MD5 request header, OSS calculates the Content-MD5 value of the message body and checks whether the value is consistent with the value of the Content-MD5 request header.

Note

To obtain the value of the Content-MD5 field, encrypt the message body of the DeleteMultipleObjects request using the MD5 algorithm to obtain a 128-bit byte array. Then, encode the byte array in Base64. The encoded string is the value of the Content-MD5 field.

Request elements

Name

	

Type

	

Required

	

Example

	

Description




Delete

	

Container

	

Yes

	

N/A

	

The container for the DeleteMultipleObjects request.

Child nodes: one or more Object elements and the Quiet element

Parent node: None




Object

	

Container

	

Yes

	

N/A

	

The container for information about an object.

Child node: Key

Parent node: Delete




Key

	

String

	

Yes

	

test.jpg

	

The name of the object to delete.

Parent node: Object




Quiet

	

Enumeration string

	

No

	

false

	

Specifies whether to enable the simple response mode.

DeleteMultipleObjects provides the following response modes:

Simple mode (quiet): OSS does not return a message body.

Verbose mode (verbose): The message body returned by OSS contains the results for all deleted objects. Verbose mode is used by default.

Valid values: true (enables simple mode) and false (enables verbose mode)

Default value: false

Parent node: Delete




VersionId

	

String

	

No

	

CAEQNRiBgIDyz.6C0BYiIGQ2NWEwNmVhNTA3ZTQ3MzM5ODliYjM1ZTdjYjA4****

	

The version number of the object to delete.

Parent node: Object

Response elements

Name

	

Type

	

Example

	

Description




DeleteResult

	

Container

	

N/A

	

The container for the result of the DeleteMultipleObjects request.

Child node: Deleted

Parent node: None




Deleted

	

Container

	

N/A

	

The container for the successfully deleted objects.

Important

The Deleted response element contains only the objects that are successfully deleted. It does not contain the objects that failed to be deleted. To obtain the names of the objects that failed to be deleted, compare the list of objects in the request with the list of objects in the `Deleted` element of the response.

Child node: Key

Parent node: DeleteResult




Key

	

String

	

demo.jpg

	

The name of the deleted object.

Parent node: Deleted




VersionId

	

String

	

version_20211101141621_d137

	

The version ID.

Parent node: Deleted




DeleteMarker

	

Boolean

	

true

	

Indicates whether the version is a delete marker. Valid values: true and false.

Note

This element is returned with a value of true only when a delete marker is created or a delete marker is permanently deleted.

Parent node: Deleted




DeleteMarkerVersionId

	

String

	

THUQNRiBgICEoPiC0BYiIGMxZWJmYmMzYjE0OTQ0ZmZhYjgzNzkzYjc2NjZk****

	

The version ID of the delete marker.

Parent node: Deleted




EncodingType

	

String

	

url2

	

The encoding type used for the object names in the response. If you specify the Encoding-type parameter in the request, OSS encodes the Key in the response.

Parent node: DeleteResult

Examples

Sample request with simple response mode disabled

 
POST /?delete HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 29 Feb 2012 12:26:16 GMT
Content-Length:151
Content-MD5: ohhnqLBJFiKkPSBO1eNaUA==
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<Delete> 
  <Quiet>false</Quiet>  
  <Object> 
    <Key>multipart.data</Key> 
  </Object>  
  <Object> 
    <Key>test.jpg</Key> 
  </Object>  
  <Object> 
    <Key>demo.jpg</Key> 
  </Object> 
</Delete>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 78320852-7eee-b697-75e1-b6db0f4849e7
Date: Wed, 29 Feb 2012 12:26:16 GMT
Content-Length: 244
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<DeleteResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Deleted>
       <Key>multipart.data</Key>
    </Deleted>
    <Deleted>
       <Key>test.jpg</Key>
    </Deleted>
    <Deleted>
       <Key>demo.jpg</Key>
    </Deleted>
</DeleteResult>

Sample request with simple response mode enabled

 
POST /?delete HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 29 Feb 2012 12:33:45 GMT
Content-Length:151
Content-MD5: ohhnqLBJFiKkPSBO1eNaUA==
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<Delete> 
  <Quiet>true</Quiet>  
  <Object> 
    <Key>multipart.data</Key> 
  </Object>  
  <Object> 
    <Key>test.jpg</Key> 
  </Object>  
  <Object> 
    <Key>demo.jpg</Key> 
  </Object> 
</Delete>

Sample response

 
HTTP/1.1 200 OK
x-oss-request-id: 559CC9BDC755F95A64485981
Date: Wed, 29 Feb 2012 12:33:45 GMT
Content-Length: 0
Connection: keep-alive
Server: AliyunOSS

Sample request to call the DeleteMultipleObjects operation without specifying a version ID

 
POST /?delete HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 04:20:03 GMT
Content-MD5: xSLOYWaPC86RPwWXNiFeXg==
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<Delete> 
  <Quiet>false</Quiet>  
  <Object> 
    <Key>multipart.data</Key>
  </Object>  
  <Object> 
    <Key>test.jpg</Key> 
  </Object>
</Delete>

Sample response

In the following example, the version IDs of the two objects to delete (multipart.dat and test.jpg) are not specified. Therefore, OSS inserts delete markers for the two objects and returns <DeleteMarker>true</DeleteMarker> and <DeleteMarkerVersionId>XXXXXX</DeleteMarkerVersionId>.

 
HTTP/1.1 200 OK
x-oss-request-id: 5CAC1D73B7AEADE01700****
Date: Tue, 09 Apr 2019 04:20:03 GMT
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<DeleteResult>
    <Deleted>
       <Key>multipart.data</Key>
       <DeleteMarker>true</DeleteMarker>
       <DeleteMarkerVersionId>CAEQMhiBgIDXiaaB0BYiIGQzYmRkZGUxMTM1ZDRjOTZhNjk4YjRjMTAyZjhl****</DeleteMarkerVersionId>
    </Deleted>
    <Deleted>
       <Key>test.jpg</Key>
       <DeleteMarker>true</DeleteMarker>
       <DeleteMarkerVersionId>CAEQMhiBgIDB3aWB0BYiIGUzYTA3YzliMzVmNzRkZGM5NjllYTVlMjYyYWEy****</DeleteMarkerVersionId>
    </Deleted>
</DeleteResult>

Sample request to delete a specific version of an object by specifying a version ID

Note

You must specify both the Key and VersionId.

 
POST /?delete HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:09:34 GMT
Content-Length:151
Content-MD5: 2Tpk+dL/tGyuSA+YCEuSVg==
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<Delete> 
  <Quiet>false</Quiet>  
  <Object> 
    <Key>multipart.data</Key>
    <VersionId>CAEQNRiBgIDyz.6C0BYiIGQ2NWEwNmVhNTA3ZTQ3MzM5ODliYjM1ZTdjYjA4****</VersionId>
  </Object>
</Delete>

Sample response

The following example shows that the key and version ID of the deleted object are returned.

 
HTTP/1.1 200 OK
x-oss-request-id: 5CAC371EB7AEADE01700****
Date: Tue, 09 Apr 2019 06:09:34 GMT
Content-Length: 244
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<DeleteResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Deleted>
       <Key>multipart.data</Key>
       <VersionId>CAEQNRiBgIDyz.6C0BYiIGQ2NWEwNmVhNTA3ZTQ3MzM5ODliYjM1ZTdjYjA4****</VersionId>
    </Deleted>
</DeleteResult>

Sample request to delete a delete marker by specifying a version ID

 
POST /?delete HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:14:50 GMT
Content-Length: 178
Content-MD5: dX9IFePFgYhmINvAhG30Bg==
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

<?xml version="1.0" encoding="UTF-8"?>
<Delete> 
  <Quiet>false</Quiet>  
  <Object> 
    <Key>multipart.data</Key>
    <VersionId>CAEQNRiBgICEoPiC0BYiIGMxZWJmYmMzYjE0OTQ0ZmZhYjgzNzkzYjc2NjZk****</VersionId>
  </Object>
</Delete>

Sample response

The returned Key and VersionId represent the key and version ID of the deleted object.

The DeleteMarker and DeleteMarkerVersionId elements indicate that the deleted item is a delete marker and its corresponding version ID. In this case, the values of VersionId and DeleteMarkerVersionId are the same, and the DeleteMarker and DeleteMarkerVersionId elements are returned together.

 
HTTP/1.1 200 OK
x-oss-request-id: 5CAC385AB7AEADE01700****
Date: Tue, 09 Apr 2019 06:14:50 GMT
Content-Length: 364
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<DeleteResult xmlns=”http://doc.oss-cn-hangzhou.aliyuncs.com”>
    <Deleted>
       <Key>demo.jpg</Key>
       <VersionId>CAEQNRiBgICEoPiC0BYiIGMxZWJmYmMzYjE0OTQ0ZmZhYjgzNzkzYjc2NjZk****</VersionId>
       <DeleteMarker>true</DeleteMarker>
       <DeleteMarkerVersionId>THUQNRiBgICEoPiC0BYiIGMxZWJmYmMzYjE0OTQ0ZmZhYjgzNzkzYjc2NjZk****</DeleteMarkerVersionId>
    </Deleted>
</DeleteResult>
SDK

SDKs for the DeleteMultipleObjects operation are available in the following languages:

Java

Python V2

PHP V2

Go V2

Harmony

C

C++

.NET

iOS

Node.js

Browser.js

Ruby

Android

ossutil command-line tool

For information about the ossutil command for the DeleteMultipleObjects operation, see delete-multiple-objects.

References

To delete a single file, see DeleteObject.

For formation about how to automatically delete objects, see Lifecycle.

Error codes

Error code

	

HTTP status code

	

Description




InvalidDigest

	

400

	

After you specify the Content-MD5 request header, OSS calculates the Content-MD5 value of the message body and checks whether the value is consistent with the value of the Content-MD5 request header. If the values are inconsistent, this error is returned.




MalformedXML

	

400

	

The message body cannot exceed 2 MB in size. Otherwise, this error is returned.

You can delete a maximum of 1,000 objects in a single DeleteMultipleObjects request. If you specify more than 1,000 objects in a request, this error is returned.




FileImmutable

	

409

	

This error is returned if you attempt to delete or modify data in a bucket that is under protection.