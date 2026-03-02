# Call GetSymlink to obtain a symbolic link

You can call the GetSymlink operation to obtain a symbolic link. To call this operation, you must have read permission on the symbolic link.

## Versioning


By default, the GetSymlink operation obtains the current version of a symbolic link. You can specify the version ID in the request to query a specific version of a symbolic link. If the current version of the symbolic link is a delete marker, OSS returns 404 Not Found and includes x-oss-delete-marker = true and x-oss-version-id in the response header. A delete marker does not contain any data. Therefore, the information about the object to which the symbolic link points is not included in the response.

## Request syntax


`plaintext
GET /ObjectName?symlink HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


## Request headers


All headers in a DescribeRegions request are common request headers. For more information, see [Common request headers](https://www.alibabacloud.com/help/en/oss/developer-reference/common-http-headers#section-eq1-b2y-wdb).

## Response headers














| Name | Type | Example | Description |
| --- | --- | --- | --- |
| x-oss-symlink-target | string | example.jpg | The destination object to which the symbolic link points. |


## Examples


-

Sample request


`plaintext
GET /link-to-oss.jpg?symlink HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Fri, 24 Feb 2012 06:38:30 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Fri, 24 Feb 2012 06:38:30 GMT
Last-Modified: Fri, 24 Feb 2012 06:07:48 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5650BD72207FB30443962F9A
x-oss-symlink-target: example.jpg
ETag: "A797938C31D59EDD08D86188F6D5"
`


-

Sample request with a specified version ID


`plaintext
GET /link-to-oss.jpg?symlink&versionId=CAEQNRiBgMClj7qD0BYiIDQ5Y2QyMjc3NGZkODRlMTU5M2VkY2U3MWRiNGRh HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Tue, 09 Apr 2019 06:50:48 GMT
Authorization: OSS4-HMAC-SHA256 Credential=LTAI/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
`


Sample response


`plaintext
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 09 Apr 2019 06:50:48 GMT
Last-Modified: Tue, 09 Apr 2019 06:50:48 GMT
Content-Length: 0
Connection: keep-alive
x-oss-version-id: CAEQNRiBgMClj7qD0BYiIDQ5Y2QyMjc3NGZkODRlMTU5M2VkY2U3MWRiNGRh
x-oss-request-id: 5CAC40C8B7AEADE01700064D
x-oss-symlink-target: example.jpg
ETag: "40CF4D450730DCCD1A78566FAE35"
`


## SDK


The following SDKs provide the GetSymlink operation:


-

[Java](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-4#undefined)

-

Python V2

-

PHP V2

-

[Go V2](https://www.alibabacloud.com/help/en/oss/developer-reference/v2-manage-symbolic-links)

-

[C](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-5#undefined)

-

[C++](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-8#concept-90490-zh)

-

[.NET](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-16#undefined)

-

[Android](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-12#concept-2150666)

-

[iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links#concept-2056694)

-

[Node.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-14#concept-2341246)

-

[Browser.js](https://www.alibabacloud.com/help/en/oss/developer-reference/manage-symbolic-links-17)

## Command-line tool ossutil


For information about the ossutil command that corresponds to the GetSymlink operation, see [get-symlink](https://www.alibabacloud.com/help/en/oss/developer-reference/get-symlink).

## Error codes











| Error code | HTTP status code | Description |
| --- | --- | --- |
| NoSuchKey | 404 | The specified file does not exist. |
| NotSymlink | 400 | The symbolic link does not exist. |


Thank you! We've received your  feedback.