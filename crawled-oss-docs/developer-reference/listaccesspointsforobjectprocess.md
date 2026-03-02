# ListAccessPointsForObjectProcess

Lists information about Object FC Access Points in an Alibaba Cloud account.

## Usage notes


By default, an Alibaba Cloud account has the permissions to list information about Object FC Access Points. To list information about Object FC Access Points in an Alibaba Cloud account by using a RAM user or Security Token Service (STS), you must have the `oss:ListAccessPointsForObjectProcess` permission.

## Request syntax


`xml
GET /?accessPointForObjectProcess&max-keys=10&continuation-token=abcd HTTP/1.1
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: SignatureValue
`


## Request headers


All headers in a ListAccessPointsForObjectProcess request are common request headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Request elements

















> NOTE:

> NOTE: 


> NOTE: 




| Element | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| max-keys | String | No | 10 | The maximum number of Object FC Access Points to return. Valid values: 1 to 1000Note If the list cannot be complete at a time due to the configurations of the max-keys element, the NextContinuationToken element is included in the response as the token for the next list. |
| continuation-token | String | No | abc | The token from which the list operation must start. You can obtain this token from the NextContinuationToken element in the returned result. |


## Response headers


The response to a ListAccessPointsForObjectProcess request contains only common response headers. For more information, see [Common HTTP headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-hcd-m2y-wdb).

## Response elements














-


-


-


-


-


-


| Element | Type | Example | Description |
| --- | --- | --- | --- |
| ListAccessPointsForObjectProcessResult | Container | N/A | The container that stores information about the Object FC Access Points that are returned. Parent nodes: noneChild nodes: IsTruncated, NextContinuationToken, AccountId, and AccessPointsForObjectProcess |
| IsTruncated | Boolean | true | Indicates whether the returned results are truncated. Valid values:true: indicates that not all results are returned for the request. false: indicates that all results are returned for the request. Parent nodes: ListAccessPointsForObjectProcessResultChild nodes: none |
| NextContinuationToken | String | abc | Indicates that this ListAccessPointsForObjectProcess request contains subsequent results. You need to set the NextContinuationToken element to continuation-token for subsequent results. Parent nodes: ListAccessPointsForObjectProcessResultChild nodes: none |
| AccountId | String | 111933544165 | The UID of the Alibaba Cloud account to which the Object FC Access Points belong. Parent nodes: ListAccessPointsForObjectProcessResultChild nodes: none |
| AccessPointsForObjectProcess | Container | N/A | The container that stores information about all Object FC Access Points. Parent nodes: ListAccessPointsForObjectProcessResultChild nodes: AccessPointForObjectProcess |
| AccessPointForObjectProcess | Container | N/A | The container that stores information about a single Object FC Access Point. Parent nodes: AccessPointsForObjectProcessChild nodes: AccessPointNameForObjectProcess, AccessPointForObjectProcessAlias, AccessPointName, and Status |
| AccessPointNameForObjectProcess | String | fc-ap-01 | The name of the Object FC Access Point. Parent nodes: AccessPointForObjectProcessChild nodes: none |
| AccessPointForObjectProcessAlias | String | fc-ap-01-3b00521f653d2b3223680ec39dbbe2-opapalias | The alias of the Object FC Access Point. Parent nodes: AccessPointForObjectProcessChild nodes: none |
| AccessPointName | String | fc-01 | The name of the access point. Parent nodes: AccessPointForObjectProcessChild nodes: none |
| Status | Enumerated string | enable | The status of the Object FC Access Point. Valid values:enable: The Object FC Access Point is created. disable: The Object FC Access Point is disabled. creating: The Object FC Access Point is being created. deleting: The Object FC Access Point is deleted. Parent nodes: AccessPointForObjectProcessChild nodes: none |


## Examples


-

Sample request


`xml
GET /?accessPointForObjectProcess&max-keys=10&continuation-token=abcd HTTP/1.1
Date: Mon, 30 Oct 2023 03:15:40 GMT
Content-Length: 0
Content-Type: application/xml
Host: oss-cn-qingdao.aliyuncs.com
Authorization: OSS qn6q:77Dv
`


-

Sample response


`xml
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListAccessPointsForObjectProcessResult>
   <IsTruncated>true</IsTruncated>
   <NextContinuationToken>abc</NextContinuationToken>
   <AccountId>111933544165</AccountId>
   <AccessPointsForObjectProcess>
      <AccessPointForObjectProcess>
          <AccessPointNameForObjectProcess>fc-ap-01</AccessPointNameForObjectProcess>
          <AccessPointForObjectProcessAlias>fc-ap-01-3b00521f653d2b3223680ec39dbbe2-opapalias</AccessPointForObjectProcessAlias>
          <AccessPointName>fc-01</AccessPointName>
          <Status>enable</Status>
      </AccessPointForObjectProcess>
   </AccessPointsForObjectProcess>
</ListAccessPointsForObjectProcessResult>
`


Thank you! We've received your  feedback.