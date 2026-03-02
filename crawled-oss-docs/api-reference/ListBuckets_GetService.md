# ListBuckets (GetService)

Lists all buckets that belong to your Alibaba Cloud account. You can specify the prefix, marker, or max-keys parameter to list buckets that meet specific conditions.

## Usage notes

To list Object Storage Service (OSS) buckets, you must have the `oss:ListBuckets` permission.

For more information, see Attach a custom policy to a RAM user.

## Request syntax

```
GET / HTTP/1.1
Host: oss.example.com
Date: GMT Date
Authorization: SignatureValue
```

## Request headers

| Header | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| x-oss-resource-group-id | String | No | rg-aek27tc******** | The ID of the resource group. If you include this header and specify the ID of the resource group in the request, OSS returns all buckets that belong to the resource group. If the resource group ID is set to rg-default-id, OSS returns all buckets that belong to the default resource group. If you include this header in the request but do not specify the resource group ID in the request, OSS returns all buckets that belong to the default resource group. If this header is not included in the request, OSS returns all buckets that belong to your Alibaba Cloud account. |

For more information about other common request headers included in a ListBuckets (GetService) request, such as Host and Date, see Common request headers.

## Request parameters

| Parameter | Type | Required | Example | Description |
| --- | --- | --- | --- | --- |
| prefix | String | No | my | The prefix that the names of the buckets that you want to return must contain. If this parameter is not specified, prefixes are not used to filter returned buckets. By default, this parameter is left empty. |
| marker | String | No | mybucket10 | The name of the bucket after which the ListBuckets (GetService) operation starts. Buckets whose names are alphabetically greater than the value of the marker parameter are returned. If this parameter is not specified, all buckets are returned. By default, this parameter is left empty. |
| max-keys | Integer | No | 10 | The maximum number of buckets that can be returned for the request. Valid values: 1 to 1000. Default value: 100. |

## Response headers

All headers in the response to a ListBuckets (GetService) request are common response headers. For more information, see Common response headers.

## Response elements

> **Note:** When you call the ListBuckets (GetService) operation, the XML body of the response does not include the Prefix, Marker, MaxKeys, IsTruncated, or NextMarker parameter if all buckets are returned.

| Element | Type | Example | Description |
| --- | --- | --- | --- |
| ListAllMyBucketsResult | Container | N/A | The container that stores the results of the ListBuckets (GetService) request. Child nodes: Owner and Buckets. Parent nodes: none |
| Prefix | String | my | The prefix contained in the names of the returned buckets. Parent nodes: ListAllMyBucketsResult |
| Marker | String | mybucket | The name of the bucket after which the ListBuckets (GetService) operation starts. Parent nodes: ListAllMyBucketsResult |
| MaxKeys | String | 10 | The maximum number of buckets that can be returned for the request. Parent nodes: ListAllMyBucketsResult |
| IsTruncated | Enumerated string | true | Indicates whether all results are returned. Valid values: true: Only part of the results are returned for the request. false: All results are returned for the request. Parent nodes: ListAllMyBucketsResult |
| NextMarker | String | mybucket10 | The marker for the next ListBuckets (GetService) request, which can be used to return the remaining results. Parent nodes: ListAllMyBucketsResult |
| Owner | Container | N/A | The container that stores information about the bucket owner. Parent nodes: ListAllMyBucketsResult |
| ID | String | ut_test_put_bucket | The user ID of the bucket owner. Parent nodes: ListAllMyBucketsResult.Owner |
| DisplayName | String | ut_test_put_bucket | The name of the bucket owner. The name of the bucket owner is the same as the user ID. Parent nodes: ListAllMyBucketsResult.Owner |
| Buckets | Container | N/A | The container that stores information about multiple buckets. Child nodes: Bucket. Parent nodes: ListAllMyBucketsResult |
| Bucket | Container | N/A | The container that stores information about the bucket. Child nodes: Name, CreationDate, and Location. Parent nodes: ListAllMyBucketsResult.Buckets |
| Name | String | mybucket01 | The name of the bucket. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| CreationDate | Time | 2014-05-15T11:18:32.000Z | The time when the bucket was created. Format: yyyy-mm-ddThh:mm:ss.timezone. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| Location | String | oss-cn-hangzhou | The OSS region ID. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| ExtranetEndpoint | String | oss-cn-hangzhou.aliyuncs.com | The public endpoint of the bucket. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| IntranetEndpoint | String | oss-cn-hangzhou-internal.aliyuncs.com | The internal endpoint of the bucket. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| Region | String | cn-hangzhou | The Alibaba Cloud region ID. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| StorageClass | String | Standard | The storage class of the bucket. Valid values: Standard, IA, Archive, ColdArchive, and DeepColdArchive. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |
| ResourceGroupId | String | rg-aek27tc******** | The ID of the resource group to which the bucket belongs. If the bucket belongs to the default resource group, the resource group ID is rg-default-id. Parent nodes: ListAllMyBucketsResult.Buckets.Bucket |

## Examples

### Query all buckets that belong to your Alibaba Cloud account

**Sample request**

```http
GET / HTTP/1.1
Date: Thu, 15 May 2014 11:18:32 GMT
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=host,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
```

**Sample success response**

```xml
HTTP/1.1 200 OK
Date: Thu, 15 May 2014 11:18:32 GMT
Content-Type: application/xml
Content-Length: 556
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300****

<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyBucketsResult>
  <Owner>
    <ID>512**</ID>
    <DisplayName>51264</DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <CreationDate>2014-02-17T18:12:43.000Z</CreationDate>
      <ExtranetEndpoint>oss-cn-shanghai.aliyuncs.com</ExtranetEndpoint>
      <IntranetEndpoint>oss-cn-shanghai-internal.aliyuncs.com</IntranetEndpoint>
      <Location>oss-cn-shanghai</Location>
      <Name>app-base-oss</Name>
      <Region>cn-shanghai</Region>
      <StorageClass>Standard</StorageClass>
    </Bucket>
    <Bucket>
      <CreationDate>2014-02-25T11:21:04.000Z</CreationDate>
      <ExtranetEndpoint>oss-cn-hangzhou.aliyuncs.com</ExtranetEndpoint>
      <IntranetEndpoint>oss-cn-hangzhou-internal.aliyuncs.com</IntranetEndpoint>
      <Location>oss-cn-hangzhou</Location>
      <Name>mybucket</Name>
      <Region>cn-hangzhou</Region>
      <StorageClass>IA</StorageClass>
    </Bucket>
  </Buckets>
</ListAllMyBucketsResult>
```

### Query buckets by specifying a prefix and the maximum number of returned buckets

**Sample request**

```http
GET /?prefix=my&max-keys=10 HTTP/1.1
Date: Thu, 15 May 2014 11:18:32 GMT
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=host,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
```

**Sample success response**

```xml
HTTP/1.1 200 OK
Date: Thu, 15 May 2014 11:18:32 GMT
Content-Type: application/xml
Content-Length: 545
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300****

<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyBucketsResult>
  <Prefix>my</Prefix>
  <Marker>mybucket</Marker>
  <MaxKeys>10</MaxKeys>
  <IsTruncated>true</IsTruncated>
  <NextMarker>mybucket10</NextMarker>
  <Owner>
    <ID>ut_test_put_bucket</ID>
    <DisplayName>ut_test_put_bucket</DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <CreationDate>2014-05-14T11:18:32.000Z</CreationDate>
      <ExtranetEndpoint>oss-cn-hangzhou.aliyuncs.com</ExtranetEndpoint>
      <IntranetEndpoint>oss-cn-hangzhou-internal.aliyuncs.com</IntranetEndpoint>
      <Location>oss-cn-hangzhou</Location>
      <Name>mybucket01</Name>
      <Region>cn-hangzhou</Region>
      <StorageClass>Standard</StorageClass>
    </Bucket>
  </Buckets>
</ListAllMyBucketsResult>
```

### Query all buckets that belong to a specific resource group

**Sample request**

```http
GET / HTTP/1.1
Date: Thu, 15 May 2014 11:18:32 GMT
Host: oss-cn-hangzhou.aliyuncs.com
Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,AdditionalHeaders=host,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
x-oss-resource-group-id: rg-aek27tc********
```

**Sample success response**

```xml
HTTP/1.1 200 OK
Date: Thu, 15 May 2014 11:18:32 GMT
Content-Type: application/xml
Content-Length: 556
Connection: keep-alive
Server: AliyunOSS
x-oss-request-id: 5374A2880232A65C2300****

<?xml version="1.0" encoding="UTF-8"?>
<ListAllMyBucketsResult>
  <Owner>
    <ID>512**</ID>
    <DisplayName>51264</DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <CreationDate>2014-02-07T18:12:43.000Z</CreationDate>
      <ExtranetEndpoint>oss-cn-shanghai.aliyuncs.com</ExtranetEndpoint>
      <IntranetEndpoint>oss-cn-shanghai-internal.aliyuncs.com</IntranetEndpoint>
      <Location>oss-cn-shanghai</Location>
      <Name>test-bucket-1</Name>
      <Region>cn-shanghai</Region>
      <StorageClass>Standard</StorageClass>
      <ResourceGroupId>rg-aek27tc********</ResourceGroupId>
    </Bucket>
    <Bucket>
      <CreationDate>2014-02-05T11:21:04.000Z</CreationDate>
      <ExtranetEndpoint>oss-cn-hangzhou.aliyuncs.com</ExtranetEndpoint>
      <IntranetEndpoint>oss-cn-hangzhou-internal.aliyuncs.com</IntranetEndpoint>
      <Location>oss-cn-hangzhou</Location>
      <Name>test-bucket-2</Name>
      <Region>cn-hangzhou</Region>
      <StorageClass>IA</StorageClass>
      <ResourceGroupId>rg-aek27tc********</ResourceGroupId>
    </Bucket>
  </Buckets>
</ListAllMyBucketsResult>
```

## Error codes

| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | The request is from an anonymous user and does not include user authentication information. |
