# Anti-DDoS Pro

Queries the protection list of an Anti-DDoS instance of a bucket.

Usage notes

By default, an Alibaba Cloud account has the permissions to query the protection list of an Anti-DDoS instance of a bucket. To query the protection list of an Anti-DDoS instance of a bucket by using a RAM user or Security Token Service (STS), you must have the oss:ListBucketAntiDDosInfo permission. For more information, see Common examples of RAM policies.

Request syntax
 
GET /?bucketAntiDDos?marker=&max-keys=100 HTTP/1.1
Date:  GMT Date
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
Request headers

All headers in a ListBucketAntiDDosInfo request are common request headers. For more information, see Common HTTP headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




marker

	

String

	

No

	

	

The name of the Anti-DDoS instance after which the list starts. If this element is specified, Anti-DDoS instances whose names are alphabetically after the marker value are returned.

Note

You can set the marker to an empty string for the first request. If the value of the IsTruncated element is true in the response, you must use the marker value in the response to perform the next request.




max-keys

	

String

	

Yes

	

100

	

The maximum number of Anti-DDoS instances that can be returned.

Valid values: 1 to 100

Default value: 100

For more information about other common request headers that are included in a ListBucketAntiDDosInfo request, such as Host and Date, see Common HTTP headers.

Response headers

All headers in the response to a ListBucketAntiDDosInfo request are common response headers. For more information, see Common HTTP headers.

Response elements

Element

	

Type

	

Example

	

Description




AntiDDOSListConfiguration

	

Container

	

N/A

	

The container that stores the protection list of an Anti-DDoS instance of a bucket.

Parent nodes: none

Child nodes: Marker, IsTruncated, and AntiDDOSConfiguration




Marker

	

String

	

nextMarker

	

The Anti-DDoS instances whose names are alphabetically after the specified marker.

Parent node: AntiDDOSListConfiguration

Child nodes: none




IsTruncated

	

String

	

true

	

Indicates whether all Anti-DDoS instances are returned.

true: All Anti-DDoS instances are returned.

false: Not all Anti-DDoS instances are returned.

Parent node: AntiDDOSListConfiguration

Child nodes: none




AntiDDOSConfiguration

	

Container

	

N/A

	

The container that stores information about the Anti-DDoS instance.

Parent node: AntiDDOSListConfiguration

Child nodes: InstanceId, Bucket, Owner, Ctime, Mtime, Status, Type, and Cnames




InstanceId

	

String

	

cbcac8d2-4f75-4d6d-9f2e-c3447f73****

	

The ID of the Anti-DDoS instance.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Bucket

	

String

	

examplebucket

	

The name of the bucket for which Anti-DDoS instances are created.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Owner

	

String

	

114893010724****

	

The ID of the bucket owner.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Ctime

	

String

	

1626769503

	

The time when the Anti-DDoS instance was created. The value is a timestamp.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Mtime

	

String

	

1626769840

	

The time when the Anti-DDoS instance was last updated. The value is a timestamp.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




ActiveTime

	

String

	

1626769845

	

The time when the Anti-DDoS instance was activated. The value is a timestamp.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Status

	

String

	

Defending

	

The status of the Anti-DDoS instance.

Init

Defending

HaltDefending

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Type

	

String

	

AntiDDosPremimum

	

The type of the Anti-DDoS instance. The value of this element is AntiDDosPremimum.

Parent nodes: AntiDDOSConfiguration

Child nodes: none




Cnames

	

Container

	

N/A

	

The container that stores the custom domain names.

Parent nodes: AntiDDOSConfiguration

Child nodes: Domain




Domain

	

String

	

abc1.example.cn

	

The custom domain names.

Examples

Sample requests

 
GET /?bucketAntiDDos?marker=&max-keys=100 HTTP/1.1
Date: Thu, 17 Apr 2025 05:34:24 GMT
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218

Sample responses

 
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Thu, 17 Apr 2025 05:34:24 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 534B371674E88A4D8906****
<?xml version="1.0" encoding="utf-8"?>

<AntiDDOSListConfiguration> 
  <Marker>nextMarker</Marker>
  <IsTruncated>true</IsTruncated>
  <AntiDDOSConfiguration>      
    <InstanceId>cbcac8d2-4f75-4d6d-9f2e-c3447f73****</InstanceId>  
    <Owner>114893010724****</Owner>  
    <Bucket>examplebucket</Bucket>  
    <Ctime>1626769503</Ctime>  
    <Mtime>1626769840</Mtime>  
    <ActiveTime>1626769845</ActiveTime>  
    <Status>Defending</Status>  
    <Type>AntiDDosPremimum</Type>  
    <Cnames> 
      <Domain>abc1.example.cn</Domain>  
      <Domain>abc2.example.cn</Domain> 
    </Cnames> 
  </AntiDDOSConfiguration>  
  <AntiDDOSConfiguration>      
    <InstanceId>cbcae8u6-4f75-4d6d-9f2e-c3446g89****</InstanceId>  
    <Owner>1148930107246818</Owner>  
    <Bucket>test-antiddos2</Bucket>  
    <Ctime>1626769993</Ctime>  
    <Mtime>1626769993</Mtime>  
    <ActiveTime>0</ActiveTime>  
    <Status>Init</Status>  
    <Type>AntiDDosPremimum</Type>  
    <Cnames> 
      <Domain>abc3.example.cn</Domain>  
      <Domain>abc4.example.cn</Domain> 
    </Cnames> 
  </AntiDDOSConfiguration> 
</AntiDDOSListConfiguration>