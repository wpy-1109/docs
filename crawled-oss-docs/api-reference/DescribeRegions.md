# DescribeRegions

Queries the endpoints of all regions supported by Object Storage Service (OSS) or a specific region, including public endpoints, internal endpoints, and acceleration endpoints.

## Usage notes

- To query the endpoints of a region, you must have the `oss:DescribeRegions` permission.
- Requests initiated by calling the DescribeRegions operation can contain only second-level domains, such as `oss-cn-hangzhou.aliyuncs.com`.

## Request syntax

### Query the endpoints of all supported regions

```
GET /?regions HTTP/1.1
Host: oss.example.com
Date: GMT Date
Authorization: SignatureValue
```

### Query the endpoints of a specific region

> **Note:** You can query the endpoints of a specific region only by using the OSS region ID.

```
GET /?regions=oss-cn-hangzhou HTTP/1.1
Host: oss.example.com
Date: GMT Date
Authorization: SignatureValue
```

## Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

## Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

## Response elements

| Element | Type | Example | Description |
| --- | --- | --- | --- |
| RegionInfoList | Container | N/A | The list of regions. Child nodes: RegionInfo. Parent nodes: none |
| RegionInfo | Container | N/A | The region information. Child nodes: Region, InternetEndpoint, InternalEndpoint, and AccelerateEndpoint. Parent nodes: RegionInfoList |
| Region | String | oss-cn-hangzhou | The OSS region ID. Parent nodes: RegionInfo |
| InternetEndpoint | String | oss-cn-hangzhou.aliyuncs.com | The public endpoint of the region. Parent nodes: RegionInfo |
| InternalEndpoint | String | oss-cn-hangzhou-internal.aliyuncs.com | The internal endpoint of the region. Parent nodes: RegionInfo |
| AccelerateEndpoint | String | oss-accelerate.aliyuncs.com | The acceleration endpoint of the region. The value is fixed as oss-accelerate.aliyuncs.com. Parent nodes: RegionInfo |

## Examples

### Query the endpoints of all supported regions

**Sample request**

```http
GET /?regions HTTP/1.1
Host: oss-cn-hangzhou.aliyuncs.com
Date: Fri, 20 Aug 2021 06:38:30 GMT
Authorization: SignatureValue
```

**Sample success response**

```xml
HTTP/1.1 200 OK
x-oss-request-id: 3a8f-2e2d-7965-3ff9-51c875b*****
Date: Fri, 20 Aug 2021 06:38:30 GMT
Content-Type: application/xml
Content-Length: 344606
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<RegionInfoList>
  <RegionInfo>
     <Region>oss-cn-hangzhou</Region>
     <InternetEndpoint>oss-cn-hangzhou.aliyuncs.com</InternetEndpoint>
     <InternalEndpoint>oss-cn-hangzhou-internal.aliyuncs.com</InternalEndpoint>
     <AccelerateEndpoint>oss-accelerate.aliyuncs.com</AccelerateEndpoint>
  </RegionInfo>
  <RegionInfo>
     <Region>oss-cn-shanghai</Region>
     <InternetEndpoint>oss-cn-shanghai.aliyuncs.com</InternetEndpoint>
     <InternalEndpoint>oss-cn-shanghai-internal.aliyuncs.com</InternalEndpoint>
     <AccelerateEndpoint>oss-accelerate.aliyuncs.com</AccelerateEndpoint>
  </RegionInfo>
</RegionInfoList>
```

### Query the endpoints of a specific region

**Sample request**

```http
GET /?regions=oss-cn-hangzhou HTTP/1.1
Host: oss-cn-hangzhou.aliyuncs.com
Date: Fri, 20 Aug 2021 06:40:30 GMT
Authorization: SignatureValue
```

**Sample success response**

```xml
HTTP/1.1 200 OK
x-oss-request-id: 3a8f-2e2d-7965-3ff9-51c875b*****
Date: Fri, 20 Aug 2021 06:40:30 GMT
Content-Type: application/xml
Content-Length: 3446
Server: AliyunOSS

<?xml version="1.0" encoding="UTF-8"?>
<RegionInfoList>
  <RegionInfo>
    <Region>oss-cn-hangzhou</Region>
    <InternetEndpoint>oss-cn-hangzhou.aliyuncs.com</InternetEndpoint>
    <InternalEndpoint>oss-cn-hangzhou-internal.aliyuncs.com</InternalEndpoint>
    <AccelerateEndpoint>oss-accelerate.aliyuncs.com</AccelerateEndpoint>
  </RegionInfo>
</RegionInfoList>
```

## Error codes

| Error code | HTTP status code | Description |
| --- | --- | --- |
| AccessDenied | 403 | The information that is required for user authentication is not passed to or is incorrect in the DescribeRegions request. Or you do not have the oss:DescribeRegions permission. |
| InvalidArgument | 400 | One or more specified parameters are invalid. |
| NoSuchRegion | 404 | The region does not exist. |
