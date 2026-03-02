# Object-level operations

Use the PutObject API to upload a file to an Object Storage Service (OSS) bucket. The maximum size of a file that can be uploaded in a single operation is 5 GB.

Request syntax
 
PUT /ObjectName HTTP/1.1
Content-Length: ContentLength
Content-Type: ContentType
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
Usage notes

The maximum size of a file that can be uploaded in a single operation is 5 GB. To upload a file larger than 5 GB, use the multipart upload feature.

When you upload a file with the same name as an existing file, the existing file is overwritten by default and a 200 OK status code is returned. You can set a parameter to prevent overwrites to avoid accidentally overwriting important files.

OSS uses a flat storage structure and does not have directories like a traditional file system. You can simulate a folder structure by creating an empty object that ends with a forward slash (/).

Permissions
Versioning
Request parameters

OSS supports standard HTTP request headers such as Cache-Control, Expires, Content-Encoding, Content-Disposition, and Content-Type. If you set these request headers, their values are automatically applied when the file is downloaded.

Parameter

	

Type

	

Required

	

Example

	

Description




Authorization

	

String

	

No

	

OSS qn6q**************:77Dv****************

	

Indicates that the request has been authenticated and authorized. For more information about how to calculate the Authorization value, see Include a signature in the header.

The Authorization header is typically required. However, you do not need to include this header if you include the signature in the URL. For more information, see Include a signature in the URL.

Default value: none




Cache-Control

	

String

	

No

	

no-cache

	

Specifies the caching behavior when an object is downloaded. Valid values:

no-cache: The cache must re-validate the content with the origin server before serving it. If the content has changed, the server returns the new object. Otherwise, it confirms the cached version is still valid.

no-store: All content of the object is not cached.

public: All content of the object is cached.

private: All content of the object is cached only on the client.

max-age=<seconds>: The validity period of the cached content. Unit: seconds. This option is available only in HTTP 1.1.

Default value: none




Content-Disposition

	

String

	

No

	

attachment

	

Specifies how the object is displayed. Valid values:

Content-Disposition:inline: The object is displayed directly in the browser.

Content-Disposition:attachment: The object is downloaded to the specified download path of the browser with the original object name.

Content-Disposition:attachment; filename="yourFileName": The object is downloaded to the specified download path of the browser with a custom object name.

yourFileName specifies the custom name of the downloaded object, such as example.jpg.

If you want to download the object to the specified download path of the browser, take note of the following items:

Note

If the name of the object contains special characters such as asterisks (*) or forward slashes (/), the name of the downloaded object may be escaped. For example, if you download example*.jpg to your local computer, example*.jpg may be escaped as example_.jpg.

To ensure that object names containing non-ASCII characters (like Chinese) are correctly handled during download and do not result in garbled filenames, you must URL-encode the Chinese characters in the object name. For example, to ensure that the Test.txt object in OSS is downloaded as a local file that has the original object name Test.txt, you must set the Content-Disposition header to attachment;filename=%E6%B5%8B%E8%AF%95.txt;filename*=UTF-8''%E6%B5%8B%E8%AF%95.txt, which derives from "attachment;filename="+URLEncoder.encode("Test","UTF-8")+".txt;filename*=UTF-8''"+URLEncoder.encode("Test","UTF-8")+".txt".

Whether an object is previewed or downloaded as an attachment when the object is accessed by using the object URL is determined by the creation time of the bucket in which the object is stored, the activation time of OSS, and the domain name type. For more information, see What do I do if an image object is downloaded as an attachment but cannot be previewed when I access the image object by using its URL?

Default value: none




Content-Encoding

	

String

	

No

	

identity

	

Declares the codec of the object. You must specify the actual codec of the object. Otherwise, parsing or download failures may occur on the client. If the object is not encoded, leave this header empty. Valid values:

identity (default): OSS does not compress or encode the object.

gzip: OSS uses the LZ77 compression algorithm created by Lempel and Ziv in 1977 and 32-bit cyclic redundancy check (CRC) to encode the object.

compress: OSS uses the Lempel–Ziv–Welch (LZW) compression algorithm to encode the object.

deflate: OSS uses the zlib library and the deflate algorithm to encode the object.

br: OSS uses the Brotli algorithm to encode the object.

Default value: none




Content-MD5

	

String

	

No

	

eB5eJF1ptWaXm4bijSPyxw==

	

Used to check the integrity of the message content. Content-MD5 is a value generated by the MD5 algorithm. If you set this header, OSS calculates the Content-MD5 hash of the message body and checks for consistency. For more information, see How to calculate Content-MD5.

To ensure data integrity, OSS provides multiple methods to verify the MD5 hash of data. To perform MD5 verification using Content-MD5, add the Content-MD5 header to the request.

Default value: none




Content-Length

	

String

	

No

	

344606

	

The size of the HTTP message body to be transferred, in bytes.

If the value of the Content-Length header is smaller than the actual size of the data transferred in the request body, OSS still creates the object. However, the object size will be equal to the size defined in Content-Length, and the excess data is discarded.




Expires

	

String

	

No

	

Wed, 08 Jul 2015 16:57:01 GMT

	

Specifies the expiration time of the object. For more information, see RFC2616.

Default value: none




x-oss-forbid-overwrite

	

String

	

No

	

false

	

Specifies whether to overwrite an object that has the same name during a PutObject operation. If the destination bucket has versioning enabled or suspended, the x-oss-forbid-overwrite request header is invalid. This means that an object with the same name can be overwritten.

If you do not specify x-oss-forbid-overwrite or set x-oss-forbid-overwrite to false, an object with the same name can be overwritten.

If you set x-oss-forbid-overwrite to true, an object with the same name cannot be overwritten.

Setting the x-oss-forbid-overwrite request header affects QPS performance. If many operations (QPS>1000) require the x-oss-forbid-overwrite request header, contact technical support to prevent impacts on your business operations.

Default value: false




x-oss-server-side-encryption

	

String

	

No

	

AES256

	

Specifies the server-side encryption method when you create an object.

Valid values: AES256, KMS,

If you specify this header, it is returned in the response header. OSS encrypts and stores the uploaded object. When you download the object, the response header includes x-oss-server-side-encryption, and its value is set to the encryption algorithm of the object.




x-oss-server-side-encryption-key-id

	

String

	

No

	

9468da86-3509-4f8d-a61e-6eab1eac****

	

The ID of the customer master key (CMK) that is managed by KMS.

This header is valid only when x-oss-server-side-encryption is set to KMS.




x-oss-object-acl

	

String

	

No

	

default

	

Specifies the access permissions of the object when it is created in OSS.

Valid values:

default: The object inherits the access permissions of the bucket.

private: The object is a private resource. Only the object owner and authorized users have read and write permissions on the object. Other users cannot access the object.

public-read: The object is a public-read resource. Only the object owner and authorized users have read and write permissions on the object. Other users have only read permissions. Use this permission with caution.

public-read-write: The object is a public-read-write resource. All users have read and write permissions on the object. Use this permission with caution.

For more information about access permissions, see Object ACL.




x-oss-storage-class

	

String

	

No

	

Standard

	

Specifies the storage class of the object.

For a bucket of any storage class, if you specify this parameter when you upload an object, the object is stored in the specified class. For example, if you set x-oss-storage-class to Standard when you upload an object to an Infrequent Access (IA) bucket, the object is stored as a Standard object.

Valid values:

Standard: Standard

IA: Infrequent Access

Archive: Archive Storage

ColdArchive: Cold Archive

DeepColdArchive: Deep Cold Archive

Important

Setting the storage class to Deep Cold Archive during upload incurs higher PUT request fees. We recommend that you set the storage classes of the objects to Standard when you upload the objects, and configure lifecycle rules to convert the storage classes of the Standard objects to Deep Cold Archive. This reduces PUT request fees.

For more information, see Storage classes.




x-oss-meta-*

	

String

	

No

	

x-oss-meta-location

	

When you use the PutObject API, parameters prefixed with x-oss-meta- are considered user-defined metadata, such as x-oss-meta-location. An object can have multiple such parameters, but the total size of all metadata cannot exceed 8 KB.

Metadata supports hyphens (-), numbers, and lowercase letters (a-z). Uppercase letters are converted to lowercase. Other characters, including underscores (_), are not supported.




x-oss-tagging

	

String

	

No

	

TagA=A&TagB=B

	

Specifies tags for the object in a key-value format. You can set multiple tags at the same time, such as TagA=A&TagB=B.

Note

The key and value must be URL-encoded. The key is required, but the value is optional. For example, you can set the object tags to TagA&TagB=B.

For more information, see Common Response Headers.

Response parameters

Parameter

	

Type

	

Example

	

Description




Content-MD5

	

String

	

1B2M2Y8AsgTpgAmY7PhC****

	

The MD5 hash of the uploaded file.

Important

The MD5 hash is the hash of the file obtained after the client completes the upload, not the MD5 hash of the response body.




x-oss-hash-crc64ecma

	

String

	

316181249502703****

	

The CRC-64 value of the uploaded file.




x-oss-version-id

	

String

	

CAEQNhiBgMDJgZCA0BYiIDc4MGZjZGI2OTBjOTRmNTE5NmU5NmFhZjhjYmY0****

	

The version ID of the file. This response header is returned only when the file is uploaded to a bucket with versioning enabled.

For more information, see Common Response Headers.

Examples
Simple upload

Request example

 
PUT /test.txt HTTP/1.1
Host: test.oss-cn-zhangjiakou.aliyuncs.com
User-Agent: aliyun-sdk-python/2.6.0(Windows/7/AMD64;3.7.0)
Accept: */*
Connection: keep-alive
Content-Type: text/plain
Date: Tue, 04 Dec 2018 15:56:37 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
Transfer-Encoding: chunked

Response example

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 04 Dec 2018 15:56:38 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5C06A3B67B8B5A3DA422299D
ETag: "D41D8CD98F00B204E9800998ECF8****"
x-oss-hash-crc64ecma: 316181249502703****
Content-MD5: 1B2M2Y8AsgTpgAmY7PhC****
x-oss-server-time: 7
Set the storage class

Request example

 
PUT /oss.jpg HTTP/1.1 
Host: oss-example.oss-cn-hangzhou.aliyuncs.com 
Cache-control: no-cache 
Expires: Fri, 28 Feb 2012 05:38:42 GMT 
Content-Disposition: attachment;filename=oss_download.jpg 
Date: Fri, 24 Feb 2012 06:03:28 GMT 
Content-Type: image/jpg 
Content-Length: 344606 
x-oss-storage-class: Archive
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-disposition;content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e 
[344606 bytes of object data]

Response example

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Sat, 21 Nov 2015 18:52:34 GMT
Content-Type: image/jpg
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5650BD72207FB30443962F9A
ETag: "A797938C31D59EDD08D86188F6D5B872"
Enable versioning

Request example

 
PUT /test HTTP/1.1
Content-Length: 362149
Content-Type: text/html
Host: versioning-put.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 02:53:24 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e

Response example

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 09 Apr 2019 02:53:24 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5CAC0A3DB7AEADE01700****
x-oss-version-id: CAEQNhiBgMDJgZCA0BYiIDc4MGZjZGI2OTBjOTRmNTE5NmU5NmFhZjhjYmY0****
ETag: "4F345B1F066DB1444775AA97D5D2****"
Error codes

Error code

	

HTTP status code

	

Description




MissingContentLength

	

411

	

The request header does not use chunked encoding or the Content-Length parameter is not set.




InvalidEncryptionAlgorithmError

	

400

	

The value specified for x-oss-server-side-encryption is invalid.

Valid values: AES256, KMS, .




AccessDenied

	

403

	

The user does not have the required access permissions for the specified bucket when adding the object.




NoSuchBucket

	

404

	

The specified bucket does not exist when adding the object.




InvalidObjectName

	

400

	

The object name is invalid. This can be because the object name is not specified, exceeds the length limit, or is invalid.




InvalidArgument

	

400

	

This error can be returned for the following reasons:

The size of the object to be added exceeds 5 GB.

The value of a parameter such as x-oss-storage-class is invalid.




RequestTimeout

	

400

	

Content-Length is specified, but no message body is sent, or the sent message body is smaller than the specified size. In this case, the server waits until the request times out.




Bad Request

	

400

	

If you specify Content-MD5 in the request, OSS calculates the MD5 hash of