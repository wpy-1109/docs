# Initiating RESTful API requests

 If your business requires a high level of customization, you can directly call RESTful APIs. To directly call an API, you must include the signature calculation in your code. Object Storage Service (OSS) supports only virtual hosted-style URLs in RESTful API requests.

## Format


All requests to OSS over OSS domain names, except the GetService (ListBuckets) and DescribeRegions requests, contain bucket information in the domain names.


The domain name used to access a bucket is in the `BucketName.Endpoint` format, where BucketName is the name of your bucket and Endpoint is the endpoint for the region in which your bucket is located.


OSS endpoints include internal endpoints, public endpoints, and acceleration endpoints.


> NOTE:

> NOTE: 


> NOTE: Note 

-

OSS uses RESTful API operations to provide services. Different regions are accessed by using different endpoints. For more information, see [Regions and endpoints](https://www.alibabacloud.com/help/en/oss/user-guide/regions-and-endpoints#concept-zt4-cvy-5db).

-

You can use internal endpoints and public endpoints without additional configurations.

-

Before you use an acceleration endpoint, you must enable the transfer acceleration feature. For more information, see [Enable transfer acceleration](https://www.alibabacloud.com/help/en/oss/enable-transfer-acceleration-131313#task-1813962).

-

You can also replace a public endpoint with a custom domain name to access OSS resources. For more information, see [Map custom domain names](https://www.alibabacloud.com/help/en/oss/manage-a-domain-map-custom-domain-names#concept-ozw-m2r-5fb) or [Map an acceleration endpoint](https://www.alibabacloud.com/help/en/oss/map-an-acceleration-endpoint#task-2347343).


For example, the following endpoints are used to access buckets located in the China (Hangzhou) region:

## Request style


For security reasons, you can use only virtual hosted-style URLs instead of path-style URLs when you initiate RESTful API requests. A virtual hosted-style URL contains the bucket name.


Format of virtual hosted-style URLs:


`plaintext
https://BucketName.Endpoint/objectName
`


Example of a virtual hosted-style URL:


`plaintext
https://examplebucket.oss-cn-hangzhou.aliyuncs.com/demo.png
`


## Request header format


The following code shows the request header format of a RESTful API request that is sent to OSS:


`plaintext
GET / HTTP/1.1
Host: BucketName.Endpoint
Date: GMT Date
Authorization: SignatureValue
`














| Header | Type | Description |
| --- | --- | --- |
| Date | String | The GMT time specified in the HTTP/1.1 protocol. Example: Sun, 05 Sep 2021 23:00:00 GMT. This header is empty by default. |
| Host | String | The access domain name. Format: BucketName.Endpoint. This header is empty by default. |
| Authorization | String | The authentication information used to verify the validity of the request. This header is empty by default.Scenario: non-anonymous requests. |


## Sample requests

### Sample request for a virtual hosted-style URL


Sample OSS resources:


-

Bucket name: examplebucket

-

Region: oss-cn-hangzhou

-

Object name: demo.png


Sample URL:


`plaintext
https://examplebucket.oss-cn-hangzhou.aliyuncs.com/demo.png
`


Sample requests:


`plaintext
GET /demo.png HTTP/1.1
Host: examplebucket.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue
`


### Sample request for a custom domain name


Sample custom domain name:


www.example.com


Sample OSS resources:


-

Bucket name: examplebucket

-

Object name: demo.png


Sample URL:


`plaintext
https://www.example.com/demo.png
`


Sample requests:


`plaintext
GET /demo.png HTTP/1.1
Host: example.com
Date: GMT Date
Authorization: SignatureValue
`


## Signature methods


You can use one of the following methods to calculate signatures and add the signatures to the RESTful API requests:


-

Add signatures to request headers: In most cases, we recommend that you use this method. For more information, see [Include signatures in the Authorization header](https://www.alibabacloud.com/help/en/oss/developer-reference/include-signatures-in-the-authorization-header#concept-aml-vv2-xdb).

-

Add signatures to URLs: If you use a signed URL to share data, the data can be obtained by all users over the Internet within the validity period of the signed URL. This causes security risks. If you want to provide a URL with signature information to a third-party user for authorized access, you can use this method. For more information, see [Add signatures to URLs](https://www.alibabacloud.com/help/en/oss/developer-reference/ddd-signatures-to-urls#concept-xqh-2df-xdb).


The following table describes the differences between the two signature methods.











> IMPORTANT:

> NOTE: 


> NOTE: 


> IMPORTANT:

> NOTE: 


> NOTE: 


| Item | Add signatures to request headers | Add signatures to URLs |
| --- | --- | --- |
| Configuration of the Expires parameter | No | Yes |
| Common request methods | GET, POST, PUT, and DELETE | GET and PUT |
| Time format | The Date request header is used to specify the request time in the GMT format. Important If the difference between the time specified by the Date header in a request and the time on the server when the request is received is greater than 15 minutes, OSS rejects the request and returns HTTP status code 403. | The Expires parameter is used to specify the time when the signed URL expires in the Unix timestamp format. Important If the time when OSS receives the URL request is later than the value of the Expires parameter that is included in the signature, a request timeout error is returned. |
| URL-encoded signatures | No | Yes |


## API operations


For more information about the API operations that are provided by OSS, see [List of operations by function](https://www.alibabacloud.com/help/en/oss/developer-reference/list-of-operations-by-function#reference-wrz-l2q-tdb).

## References for subsequent operations


-

[Include a signature in the Authorization header](https://www.alibabacloud.com/help/en/oss/developer-reference/include-signature-in-header/#44ecb8159bib4)

-

[Add signatures to URLs](https://www.alibabacloud.com/help/en/oss/developer-reference/include-signature-in-url/#e35f6dc3cb4t0)

-

[Include a signature in a PostObject request](https://www.alibabacloud.com/help/en/oss/developer-reference/post-signature/#a334108de1dzm)

-

[Troubleshoot signature errors](https://www.alibabacloud.com/help/en/oss/developer-reference/faq-24#title-psn-xdj-l8m)

Thank you! We've received your  feedback.