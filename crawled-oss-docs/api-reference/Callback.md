# Object-level operations

After an object is uploaded to Object Storage Service (OSS), OSS can automatically send a callback request to notify the application server to perform subsequent operations.

Usage notes

Limits on regions

Callbacks are supported in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Germany (Frankfurt), UK (London), and UAE (Dubai).

Callback logic

If a callback request does not receive a response within 5 seconds after OSS sends the request, OSS determines that the request times out.

The uploaded object is stored in OSS regardless of whether the upload callback request is successful or fails.

If a callback request fails, the callback request is not retried.

Supported operations

Only the PutObject, PostObject, and CompleteMultipartUpload operations support callbacks.

Callback process

Steps:

The client uploads an object with callback parameters specified

When the client uploads an object, specify the callback parameter, which includes the URL of the application server and the callback content. The client can configure custom parameters by using the callback-var parameter.

OSS stores the object and sends a callback request

After an object is uploaded, OSS sends a POST request to the URL of the application server. The request contains object information, such as the bucket name, object name, object size, object ETag, and custom parameters.

The application server processes the callback request and returns a response

After the application server receives the callback request, the application server verifies the request signature (optional) to ensure security, processes the callback request within 5 seconds, and returns a response in the JSON format. HTTP status code 200 indicates that the call is successful. Other HTTP status codes indicate that the call failed.

OSS returns the upload and callback results

After OSS receives the callback response, OSS returns the upload and callback results to the client.

Steps to configure upload callbacks

Upload callback debugging consists of two parts: upload an object from the client and process the callback request on the application server. We recommend that you debug the object upload, and then debug the callback request processing. After both parts are debugged, complete joint debugging.

Debug the object upload
The following section describes how to construct and process logic and process upload callback parameters. To quickly implement the upload callback feature, we recommend that you refer to the sample code provided for OSS SDKs.

To enable OSS to automatically trigger a callback after an object is uploaded, you must specify the following parameters in the upload request: callback and callback-var (optional).

Construct the callback parameter.

The callback parameter is used to specify the application server URL and request content format. It must be constructed in JSON format and encoded in Base64.

Simple configuration example:

 
{
"callbackUrl":"http://oss-demo.aliyuncs.com:23450",
"callbackBody":"bucket=${bucket}&object=${object}&my_var=${x:my_var}"
}

callbackUrl: the URL of the application server. http://oss-demo.aliyuncs.com:23450 is used in this example.

callbackBody: the callback request body. The callbackBody field supports system variables, such as ${bucket} and ${object}, and custom variables. For more information about the system variables, see System variables supported by callbackBody.

Advanced configuration example:

 
{
"callbackUrl":"http://oss-demo.aliyuncs.com:23450",
"callbackHost":"oss-cn-hangzhou.aliyuncs.com",
"callbackBody":"bucket=${bucket}&object=${object}&my_var=${x:my_var}",
"callbackBodyType":"application/x-www-form-urlencoded",
"callbackSNI":false
}

For more information about the preceding fields, see Fields supported by the callback parameter.

(Optional) Construct the callback-var parameter

This parameter is used to pass custom service information, such as the user ID and order number, to the application server. It must be in the JSON format. The key of each custom parameter must start with x: and contain lowercase letters. Example:

 
{
  "x:uid": "12345",
  "x:order_id": "67890"
}

The callback-var parameter must be used together with the callbackBody parameter. The user ID (uid) and order number (order_id) parameters in the preceding example must be referenced by placeholders ${x:xxx} in callbackBody. Example:

 
{
  "callbackUrl": "http://oss-demo.aliyuncs.com:23450",
  "callbackBody": "uid=${x:uid}&order=${x:order_id}"
}

During the actual callback request process, OSS sends the following content. In this example, the callbackBodyType field is set to application/x-www-form-urlencoded.

 
uid=12345&order=67890

After constructing the callback and callback-var parameters, you must Base64-encode them.

Example: Base64-encode the callback parameter

The callback parameter that is not Base64-encoded:

 
{
    "callbackUrl": "http://oss-demo.aliyuncs.com:23450",
    "callbackHost": "your.callback.com",
    "callbackBody": "bucket=${bucket}&object=${object}&uid=${x:uid}&order=${x:order_id}",
    "callbackBodyType": "application/x-www-form-urlencoded",
    "callbackSNI": false
}

The callback parameter that is Base64-encoded:

 
eyJjYWxsYmFja0hvc3QiOiAieW91ci5jYWxsYmFjay5jb20iLCAiY2FsbGJhY2tVcmwiOiAiaHR0cDovL29zcy1kZW1vLmFsaXl1bmNzLmNvbToyMzQ1MCIsICJjYWxsYmFja0JvZHkiOiAiYnVja2V0PSR7YnVja2V0fSZvYmplY3Q9JHtvYmplY3R9JnVpZD0ke3g6dWlkfSZvcmRlcj0ke3g6b3JkZXJfaWR9IiwgImNhbGxiYWNrQm9keVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgImNhbGxiYWNrU05JIjogZmFsc2V9

Example: Base64-encode the callback-var parameter

The callback-var parameter that is not Base64-encoded:

 
{
  "x:uid": "12345",
  "x:order_id": "67890"
}

The callback-var parameter that is Base64-encoded:

 
eyJ4OnVpZCI6ICIxMjM0NSIsICJ4Om9yZGVyX2lkIjogIjY3ODkwIn0=

Add the Base64-encoded parameters to the request.

You can use one of the following methods to add the Base64-encoded parameters to the request.

(Recommended) Add the parameters to the request as headersAdd the parameters to the form fields in the body of a POST requestAdd the parameters to the URL

This method is suitable for scenarios in which you want to upload objects to OSS by using OSS SDKs or backend code, which provides high security. You can set the x-oss-callback header to the Base64-encoded callback parameter and x-oss-callback-var to the Base64-encoded callback-var parameter. This x-oss-callback-var header is optional.

Note: The x-oss-callback-var and x-oss-callback headers are included in canonical headers to calculate a signature.

Example

 
PUT /your_object HTTP/1.1
Host: callback-test.oss-test.aliyun-inc.com
Accept-Encoding: identity
Content-Length: 5
x-oss-callback-var: eyJ4OnVpZCI6ICIxMjM0NSIsICJ4Om9yZGVyX2lkIjogIjY3ODkwIn0=
User-Agent: aliyun-sdk-python/0.4.0 (Linux/2.6.32-220.23.2.ali1089.el5.x86_64/x86_64;2.5.4)
x-oss-callback: eyJjYWxsYmFja0hvc3QiOiAieW91ci5jYWxsYmFjay5jb20iLCAiY2FsbGJhY2tVcmwiOiAiaHR0cDovL29zcy1kZW1vLmFsaXl1bmNzLmNvbToyMzQ1MCIsICJjYWxsYmFja0JvZHkiOiAiYnVja2V0PSR7YnVja2V0fSZvYmplY3Q9JHtvYmplY3R9JnVpZD0ke3g6dWlkfSZvcmRlcj0ke3g6b3JkZXJfaWR9IiwgImNhbGxiYWNrQm9keVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgImNhbGxiYWNrU05JIjogZmFsc2V9
Host: callback-test.oss-test.aliyun-inc.com
Expect: 100-Continue
Date: Wed, 26 Apr 2023 03:46:17 GMT
Content-Type: text/plain
Authorization: OSS qn6q**************:77Dv****************
Test
Process the callback request on the application server
This section shows how the application server processes the callback request. For more information about the sample code for different programming languages, see Sample code for different programming languages.

The application server must have the following capabilities:

Receive the POST request from OSS

After the object is uploaded, OSS automatically sends a POST request to the application server based on the callback parameters. Example:

 
POST /test HTTP/1.1
Host: your.callback.com
Connection: close
Authorization: GevnM3**********3j7AKluzWnubHSVWI4dY3VsIfUHYWnyw==
Content-MD5: iKU/O/JB***ZMd8Ftg==
Content-Type: application/x-www-form-urlencoded
Date: Tue, 07 May 2024 03:06:13 GMT
User-Agent: aliyun-oss-callback
x-oss-bucket: your_bucket
x-oss-pub-key-url: aHR0cHM6Ly9nb3NzcHVi**********vY2FsbGJeV92MS5wZW0=
x-oss-request-id: 66399AA50*****3334673EC2
x-oss-requester: 23313******948342006
x-oss-signature-version: 1.0
x-oss-tag: CALLBACK
bucket=your_bucket&object=your_object&uid=12345&order_id=67890

(Optional) Verify the signature of the request to ensure data security

To ensure that the callback request is sent by OSS, we recommend that you verify the request signature on the application server. For more information, see Recommended configurations.

Note

Signature verification is not required. You can enable it based on your business requirements.

Return a response for the callback request

After the application server receives the callback request, it must return a response to OSS. The response must meet the following requirements:

Normally, the application server returns HTTP/1.1 200 OK.

The response returned by the application server to OSS must contain the Content-Length header. The size of the header cannot exceed 3 MB.

The response body must be in the JSON format and cannot exceed 1 MB in size.

In this example, the application server returned {"Status": "OK"}.

 
HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 14 Sep 2015 12:37:27 GMT
Content-Type: application/json
Content-Length: 9
{"Status": "OK"}

OSS returns the response to the client. Example:

 
HTTP/1.1 200 OK
Date: Mon, 14 Sep 2015 12:37:27 GMT
Content-Type: application/json
Content-Length: 9
Connection: keep-alive
ETag: "D8E8FCA2DC0F896FD7CB4CB0031BA249"
Server: AliyunOSS
x-oss-bucket-version: 1442231779
x-oss-request-id: 55F6BF87207FB30F2640C548
{"Status": "OK"}
Important

For a CompleteMultipartUpload request, if the response body contains content such as information in the JSON format, the content is overwritten by the callback response after upload callback is enabled. In this example, the content is overwritten by {"Status": "OK"}.

Recommended configurations
Verify the signature in the callback request to ensure data security

After you configure the callback parameters, OSS sends a callback request to the application server after you upload an object to OSS based on the callbackUrl parameter. To ensure that the request is sent by OSS, you can verify the signature in the callback request. Verification steps:

OSS generates a signature on the client

OSS uses the RSA asymmetric encryption algorithm and MD5 hash to generate a signature for the request and adds the signature to the authorization request header.

Sample code for signature calculation:

 
authorization = base64_encode(rsa_sign(private_key, url_decode(path) + query_string + '\n' + body, md5))
Note

In the preceding code, private_key specifies a private key, path specifies the resource path that is included in the callback request, query_string specifies the query string, and body specifies the message body in the callback request.

Steps to generate a signature:

Create the string to sign. The string consists of the resource path that is obtained by decoding the URL, the original query string, a carriage return, and the callback message body.

Sign the created string by using the RSA encryption algorithm and the private key. The hash function that is used to calculate the signature is MD5.

Use Base64 to encode the signed result to obtain the final signature. Then, add the signature to the Authorization header in the callback request.

Sample code for signature generation:

 
POST /index.php?id=1&index=2 HTTP/1.0
Host: 172.16.XX.XX
Connection: close
Content-Length: 18
authorization: kKQeGTRccDKyHB3H9vF+xYMSrmhMZj****/kdD1ktNVgbWEfYTQG0G2SU/RaHBovRCE8OkQDjC3uG33esH2t****
Content-Type: application/x-www-form-urlencoded
User-Agent: http-client/0.0.1
x-oss-pub-key-url: aHR0cDovL2dvc3NwdWJsaWMuYWxpY2RuLmNvbS9jYWxsYmFja19wdWJfa2V5X3YxLnsr****
bucket=examplebucket

In the preceding code, the final signature is kKQeGTRccDKyHB3H9vF+xYMSrmhMZjzzl2/kdD1ktNVgbWEfYTQG0G2SU/RaHBovRCE8OkQDjC3uG33esH2t****. The signature is generated from the /index.php path, the ?id=1&index=2 query string, and bucket=examplebucket body.

The application server verifies the signature

Your application server must verify the signature in the request to confirm the validity of the request source. Procedure:

Obtain the public key:

Obtain the Base64-encoded public key URL from the x-oss-pub-key-url request header and decode it.

 
public_key = urlopen(base64_decode(x-oss-pub-key-url header value))

The Base64-encoded public key URL:

 
aHR0cDovL2dvc3NwdWJsaWMuYWxpY2RuLmNvbS9jYWxsYmFja19wdWJfa2V5X3YxLnBlbQ==

The decoded public key URL:

 
http://gosspublic.alicdn.com/callback_pub_key_v1.pem
Note

The public key URL must start with http://gosspublic.alicdn.com/ or https://gosspublic.alicdn.com/. The content of the public key URL remains unchanged. We recommend that you cache the public key to prevent service impacts due to network fluctuations.

Decode the signature.

Obtain the signature from the authorization request header and perform Base64 decoding:

 
signature = base64_decode(authorization header value)

Construct the string to be verified.

Concatenate resource paths, query strings, line breaks, and callback message body in the following format:

 
sign_str = url_decode(path) + query_string + '\n' + body

Verify the signature.

Use the MD5 hash and the RSA public key to verify the signature:

 
result = rsa_verify(public_key, md5(sign_str), signature)

Signature verification example

The following code provides an example on how an application server verifies a signature. Before you run the code in OSS SDK for Python, install the M2Crypto library:

 
import httplib
import base64
import md5
import urllib2
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from M2Crypto import RSA
from M2Crypto import BIO
def get_local_ip():
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return ""
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    '''
    def log_message(self, format, *args):
        return
    '''
    def do_POST(self):
        #get public key
        pub_key_url = '