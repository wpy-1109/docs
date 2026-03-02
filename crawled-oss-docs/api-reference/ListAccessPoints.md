# ListAccessPoints

Queries information about user-level or bucket-level access points.

Usage notes

By default, an Alibaba Cloud account has the permissions to query information about access points. To query information about access points by using a RAM user or Security Token Service (STS), you must have the oss:ListAccessPoints permission.

Request syntax

The difference between querying information about user-level access points and querying information about bucket-level access points lies in the request host. The request host used for querying information about user-level access points is a public endpoint (example: oss-cn-hangzhou.aliyuncs.com) or an internal endpoint (example: oss-cn-hangzhou-internal.aliyuncs.com). The request host used for querying information about bucket-level access points is a bucket domain name (example: oss-example.oss-cn-hangzhou.aliyuncs.com).

Query information about user-level access pointsQuery information about bucket-level access points
 
GET /?accessPoint&max-keys=10&continuation-token=abcd HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com 
Authorization: SignatureValue
Request headers

All headers in a ListAccessPoints request are common request headers. For more information, see Common HTTP headers.

Request elements

Element

	

Type

	

Required

	

Example

	

Description




max-keys

	

String

	

No

	

10

	

The maximum number of access points that can be returned. Valid values:

For user-level access points: (0,1000].

For bucket-level access points: (0,100].

Note

If the list cannot be complete at a time due to the configurations of the max-keys element, the NextContinuationToken element is included in the response as the token for the next list.




continuation-token

	

String

	

No

	

abc

	

The token from which the list operation must start. You can obtain this token from the NextContinuationToken element in the response.

Response headers

The response to a ListAccessPoints request contains only common response headers. For more information, see Common HTTP headers.

Response elements

Element

	

Type

	

Example

	

Description




ListAccessPointsResult

	

Container

	

N/A

	

The container that stores the information about the list result.

Parent nodes: none

Child nodes: IsTruncated, NextContinuationToken, AccountId, and AccessPoints




IsTruncated

	

Boolean

	

true

	

Indicates whether the returned results are truncated. Valid values:

true: indicates that not all results are returned for the request.

false: indicates that all results are returned for the request.

Parent nodes: ListAccessPointsResult

Child nodes: none




NextContinuationToken

	

String

	

abc

	

Indicates that this ListAccessPoints request contains subsequent results. You must set NextContinuationToken to continuation-token to continue obtaining list results.

Parent nodes: ListAccessPointsResult

Child nodes: none




AccountId

	

String

	

111933544165****

	

The ID of the Alibaba Cloud account to which the access point belongs.

Parent nodes: ListAccessPointsResult

Child nodes: none




AccessPoints

	

Container

	

N/A

	

The container that stores the information about all access points.

Parent nodes: ListAccessPointsResult

Child nodes: AccessPoint




AccessPoint

	

Container

	

N/A

	

The container that stores the information about an access point.

Parent nodes: AccessPoints

Child nodes: Bucket, AccessPointName, Alias, NetworkOrigin, VpcConfiguration, and Status




Bucket

	

String

	

oss-example

	

The name of the bucket for which the access point is configured.

Parent nodes: AccessPoint

Child nodes: none




AccessPointName

	

String

	

ap-01

	

The name of the access point.

Parent nodes: AccessPoint

Child nodes: none




Alias

	

String

	

ap-01-ossalias

	

The alias of the access point.

Parent nodes: AccessPoint

Child nodes: none




NetworkOrigin

	

String

	

vpc

	

The network origin of the access point. Valid values:

vpc: You can use a specific virtual private cloud (VPC) ID to access the access point.

internet: You can use public endpoints and internal endpoints to access the access point.

Parent nodes: AccessPoint

Child nodes: none




VpcConfiguration

	

Container

	

N/A

	

The container that stores the information about the VPC.

Parent nodes: AccessPoint

Child nodes: VpcId




VpcId

	

String

	

vpc-t4nlw426y44rd3iq4****

	

The ID of the VPC.

Parent nodes: VpcConfiguration

Child nodes: none




Status

	

	

enable

	

The status of the access point. Valid values:

enable: The access point is created.

disable: The access point is disabled.

creating: The access point is being created.

deleting: The access point is deleted.

Parent nodes: AccessPoint

Child nodes: VpcId

Examples

Sample requests

Sample request for querying information about user-level access pointsSample request for querying information about bucket-level access points
 
GET /?accessPoint&max-keys=10&continuation-token=abc HTTP/1.1
Date: Mon, 19 Jun 2023 03:15:40 GMT
Content-Length: 36
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com 
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=content-length,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e    

Sample response

 
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessPointsResult>
  <IsTruncated>true</IsTruncated>
  <NextContinuationToken>abc</NextContinuationToken>
  <AccountId>111933544165****</AccountId>
  <AccessPoints>
    <AccessPoint>
      <Bucket>oss-example</Bucket>
      <AccessPointName>ap-01</AccessPointName>
      <Alias>ap-01-ossalias</Alias>
      <NetworkOrigin>vpc</NetworkOrigin>
      <VpcConfiguration>
        <VpcId>vpc-t4nlw426y44rd3iq4****</VpcId>
      </VpcConfiguration>
      <Status>enable</Status>
    </AccessPoint>
    ...
  </AccessPoints>
</ListAccessPointsResult>
ossutil

For information about the ossutil command that corresponds to the ListAccessPoints operation, see list-access-points.