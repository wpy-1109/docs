# Signature methods

When you initiate requests to OSS, include a V4 signature in the Authorization request header. This ensures successful authentication. You can use the OSS SDK to initiate requests, because it implements the complex V4 signature algorithm. Only implement the V4 signature algorithm yourself if you cannot use the SDK. For more information, see this document.

SDK Signature Implementation

If you implement the V4 signature algorithm yourself, refer to the SDK’s V4 signature implementation first.

SDK

	

V4 Signature Implementation




Java

	

OSSV4Signer.java




Python

	

v4.py




Go

	

v4.go




JavaScript

	

client.js




PHP

	

SignerV4.php




C#

	

SignerV4.cs




Android

	

OSSV4Signer.java




Swift

	

SignerV4.swift




Objective-C

	

OSSV4Signer.m




C++

	

SignerV4.cc




C

	

oss_auth.c

Authorization Request Header

When you initiate a request to OSS, include a signature in the Authorization request header to verify the request.

The format of the Authorization request header is as follows:

 
Authorization: OSS4-HMAC-SHA256 Credential=<AccessKeyId>/<SignDate>/<SignRegion>/oss/aliyun_v4_request, AdditionalHeaders=<AdditionalHeadersVal>, Signature=<SignatureVal>

The following table describes the Authorization request header:

Components

	

Description




OSS4-HMAC-SHA256

	

Specifies the algorithm for signature calculation. This string defines the OSS V4 signature version (OSS4) and the signature algorithm (HMAC-SHA256). Provide this value when using V4 signatures for authentication.




Credential

	

AccessKey ID and scope information (including the date, region, and cloud product used for signature calculation). Provide this field when using V4 signatures for authentication.

Format is as follows:

 
<AccessKeyId>/<SignDate>/<SignRegion>/oss/aliyun_v4_request

Where:

AccessKeyId: Your AccessKey ID. This unique identifier verifies the requester's identity.

SignDate: The signature date, in YYYYMMDD format.

SignRegion: The region ID used for the request, such as cn-hangzhou.

oss: A fixed string. It identifies the requested service as Alibaba Cloud Object Storage Service (OSS).

aliyun_v4_request: A fixed string. It specifies the request's signature version as V4.




AdditionalHeaders

	

Specify optional request headers for signature calculation (do not specify required headers). Include only lowercase header names, sorted lexicographically and separated by semicolons (;).

Example:

 
content-disposition;content-length



Signature

	

The calculated signature. Provide this field when using V4 signatures for authentication.

Example of a 256-bit signature value, represented by 64 lowercase hexadecimal digits:

 
3938**********************************dcdc
Signature Calculation

After OSS receives a request, it calculates the signature and compares it with the signature in the Authorization request header. If the signatures match, the request succeeds. Otherwise, the request fails.

Signature Calculation Process

The following figure shows the signature calculation process:

The signature calculation process consists of three steps:

Construct a canonical request: Format the request according to the OSS signature specifications to create a canonical request.

Construct a string-to-sign: Process the canonical request to generate a string-to-sign.

Calculate the signature: Perform multiple hash operations on the AccessKey Secret to generate a derived key. Then, use the derived key to calculate the string-to-sign, which yields the final signature.

1. Construct a Canonical Request

The format of the canonical request is as follows:

 
HTTP Verb + "\n" +
Canonical URI + "\n" +
Canonical Query String + "\n" +
Canonical Headers + "\n" +
Additional Headers + "\n" +
Hashed PayLoad

The canonical request is defined as follows:

Parameter

	

Description




HTTP Verb

	

The HTTP request method, such as PUT, GET, POST, HEAD, DELETE, and OPTIONS.




Canonical URI

	

The URI-encoded resource path. The resource path does not include the query string. Do not encode forward slashes (/).

If the request target is the OSS service, the resource path is /, and the URI-encoded resource path is UriEncode("/").

If the request target is a bucket, the resource path is /examplebucket/, and the URI-encoded resource path is UriEncode("/examplebucket/").

If the request target is an object in a bucket, the resource path is /examplebucket/exampleobject, and the URI-encoded resource path is UriEncode("/examplebucket/exampleobject")




Canonical Query String

	

URI-encoded query parameters, sorted lexicographically.

If query parameters include both names and values, URI-encode each parameter's name and value separately. Then, sort the parameters lexicographically by their encoded names. Note that sorting occurs after encoding. Use = to connect the encoded name and value. Use & to concatenate different parameters.

Query parameters: prefix=somePrefix&marker=someMarker&max-keys=20

Canonical query parameters:

 
UriEncode("marker")+"="+UriEncode("someMarker")+"&"+UriEncode("max-keys")+"="+UriEncode("20")+"&"+UriEncode("prefix")+"="+UriEncode("somePrefix")

If a query parameter contains only a name, URI-encode the parameter name.

Query parameter: ?acl

Canonical query parameter: UriEncode("acl")

If no query parameters exist (the request URI does not contain a ?), set the canonical query string to an empty string ("").




Canonical Headers

	

The list of request headers.

Request headers fall into three categories:

Headers that must exist in the request and participate in signature calculation:

x-oss-content-sha256: Only UNSIGNED-PAYLOAD is currently supported.

Headers that participate in signature calculation if they exist in the request:

Content-Type

Content-MD5

x-oss-*: Other request headers that start with x-oss-. For example, when accessing via the STS AccessKey, the SecurityToken is specified using x-oss-security-token:security-token. For example, the request time is specified using x-oss-date, and the format must conform to the ISO 8601 standard time format, such as 20231203T121212Z.

Optional request headers specified in AdditionalHeaders.

Format is as follows:

 
Lowercase(<HeaderName1>) + ":" + Trim(<value>) + "\n"
Lowercase(<HeaderName2>) + ":" + Trim(<value>) + "\n"
...
Lowercase(<HeaderNameN>) + ":" + Trim(<value>) + "\n"

Example:

 
content-disposition:attachment
content-length:3
content-md5:ICy5YqxZB1uWSwcVLSNLcA==
content-type:text/plain
x-oss-content-sha256:UNSIGNED-PAYLOAD
x-oss-date:20250328T101048Z



Additional Headers

	

Specify optional request headers for signature calculation (do not specify required headers). Include only lowercase header names, sorted lexicographically and separated by semicolons (;). This must be consistent with AdditionalHeaders.

Example:

 
content-disposition;content-length



Hashed PayLoad

	

The hexadecimal representation of the SHA256 hash value of the request payload. Only UNSIGNED-PAYLOAD is currently supported.

2. Construct a String-to-Sign

The format of the string-to-sign is as follows:

 
"OSS4-HMAC-SHA256" + "\n" +
TimeStamp + "\n" +
Scope + "\n" +
Hex(SHA256Hash(<CanonicalRequest>))

The following table describes the string-to-sign:

Parameter

	

Description




OSS4-HMAC-SHA256

	

The signature hash algorithm. Its value must be OSS4-HMAC-SHA256.




TimeStamp

	

The current UTC time. Its format must be ISO8601, such as 20250320T083322Z.




Scope

	

The parameter set for deriving the key. This set specifies the date, region, and service. Therefore, a signature calculated with the derived key is valid only for the specified date, region, and service.

Format is as follows:

 
<SignDate>/<SignRegion>/oss/aliyun_v4_request

Description is as follows:

SignDate: The date participating in the signature, in YYYYMMDD format.

SignRegion: The region ID used for the signature, such as cn-hangzhou.

oss: The service name participating in the signature, fixed as oss.

aliyun_v4_request: The version participating in the signature, fixed as aliyun_v4_request.




CanonicalRequest

	

The constructed canonical request.

3. Calculate the Signature

Signature calculation consists of two steps:

Calculate the SigningKey.

 
DateKey = HMAC-SHA256("aliyun_v4" + SK, Date);
DateRegionKey = HMAC-SHA256(DateKey, Region);
DateRegionServiceKey = HMAC-SHA256(DateRegionKey, "oss");
SigningKey = HMAC-SHA256(DateRegionServiceKey, "aliyun_v4_request");

SK: The AccessKey Secret used in the signature.

Date: The date used in the signature, in YYYYMMDD format. It must match the SignDate in the string-to-sign.

Region: The region ID used for the signature, such as cn-hangzhou. It must match the SignRegion in the string-to-sign.

Use the SigningKey and the string-to-sign to calculate the Signature.

 
Signature = HEX(HMAC-SHA256(SigningKey, StringToSign))
Signature Calculation Example

This example uses PutObject to demonstrate signature calculation.

Signature Calculation Parameters

Parameter

	

Value




AccessKeyId

	

LTAI****************




AccessKeySecret

	

yourAccessKeySecret




Timestamp

	

20250411T064124Z




Bucket

	

examplebucket




Object

	

exampleobject




Region

	

cn-hangzhou

Signature Calculation Process Example

Construct a canonical request.

 
PUT
/examplebucket/exampleobject

content-disposition:attachment
content-length:3
content-md5:ICy5YqxZB1uWSwcVLSNLcA==
content-type:text/plain
x-oss-content-sha256:UNSIGNED-PAYLOAD
x-oss-date:20250411T064124Z

content-disposition;content-length
UNSIGNED-PAYLOAD

Construct a string-to-sign.

 
OSS4-HMAC-SHA256
20250411T064124Z
20250411/cn-hangzhou/oss/aliyun_v4_request
c46d96390bdbc2d739ac9363293ae9d710b14e48081fcb22cd8ad54b63136eca

Calculate the signature.

Calculate the SigningKey.

Note

For readability, the SigningKey is shown in hexadecimal format below.

Different combinations of signature parameters produce different SigningKey values. This example is for reference only. Use your actual calculation results.

 
3543b7686e65eda71e5e5ca19d548d78423c37e8ddba4dc9d83f90228b457c76

Calculate the Signature.

 
053edbf550ebd239b32a9cdfd93b0b2b3f2d223083aa61f75e9ac16856d61f23