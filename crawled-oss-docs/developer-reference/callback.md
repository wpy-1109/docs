# Callback

After an object is uploaded to Object Storage Service (OSS), OSS can automatically send a callback request to notify the application server to perform subsequent operations.

## Usage notes


-

Limits on regions


Callbacks are supported in the following regions: China (Hangzhou), China (Shanghai), China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), China (Hong Kong), US (Silicon Valley), US (Virginia), Japan (Tokyo), Singapore, Malaysia (Kuala Lumpur), Indonesia (Jakarta), Philippines (Manila), Germany (Frankfurt), UK (London), and UAE (Dubai).

-

Callback logic


-

If a callback request does not receive a response within 5 seconds after OSS sends the request, OSS determines that the request times out.

-

The uploaded object is stored in OSS regardless of whether the upload callback request is successful or fails.

-

If a callback request fails, the callback request is not retried.

-

Supported operations


Only the [PutObject](https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb), [PostObject](https://www.alibabacloud.com/help/en/oss/developer-reference/postobject#reference-smp-nsw-wdb), and [CompleteMultipartUpload](https://www.alibabacloud.com/help/en/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb) operations support callbacks.

## Callback process
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0017467471/CAEQPxiBgMC7xMGftxkiIGQ2MWJjZjg3NjljMzQ3NTA5ZGI2MGI3ZjY4OTc4MDYz3963382_20230830144006.372.svg)

Steps:


-

The client uploads an object with callback parameters specified


When the client uploads an object, specify the callback parameter, which includes the URL of the application server and the callback content. The client can configure custom parameters by using the callback-var parameter.

-

OSS stores the object and sends a callback request


After an object is uploaded, OSS sends a POST request to the URL of the application server. The request contains object information, such as the bucket name, object name, object size, object ETag, and custom parameters.

-

The application server processes the callback request and returns a response


After the application server receives the callback request, the application server verifies the request signature (optional) to ensure security, processes the callback request within 5 seconds, and returns a response in the JSON format. HTTP status code 200 indicates that the call is successful. Other HTTP status codes indicate that the call failed.

-

OSS returns the upload and callback results


After OSS receives the callback response, OSS returns the upload and callback results to the client.

## Steps to configure upload callbacks


Upload callback debugging consists of two parts: upload an object from the client and process the callback request on the application server. We recommend that you debug the object upload, and then debug the callback request processing. After both parts are debugged, complete joint debugging.

### Debug the object upload
The following section describes how to construct and process logic and process upload callback parameters. To quickly implement the upload callback feature, we recommend that you refer to the sample code provided for [OSS SDKs].

To enable OSS to automatically trigger a callback after an object is uploaded, you must specify the following parameters in the upload request: callback and callback-var (optional).


-

Construct the callback parameter.


The callback parameter is used to specify the application server URL and request content format. It must be constructed in JSON format and encoded in Base64.


-

Simple configuration example:


`json
{
"callbackUrl":"http://oss-demo.aliyuncs.com:23450",
"callbackBody":"bucket=${bucket}&object=${object}&my_var=${x:my_var}"
}
`


-

callbackUrl: the URL of the application server. `http://oss-demo.aliyuncs.com:23450` is used in this example.

-

callbackBody: the callback request body. The callbackBody field supports system variables, such as ${bucket} and ${object}, and custom variables. For more information about the system variables, see [System variables supported by callbackBody].

-

Advanced configuration example:


`json
{
"callbackUrl":"http://oss-demo.aliyuncs.com:23450",
"callbackHost":"oss-cn-hangzhou.aliyuncs.com",
"callbackBody":"bucket=${bucket}&object=${object}&my_var=${x:my_var}",
"callbackBodyType":"application/x-www-form-urlencoded",
"callbackSNI":false
}
`


For more information about the preceding fields, see [Fields supported by the callback parameter].

-

(Optional) Construct the callback-var parameter


This parameter is used to pass custom service information, such as the user ID and order number, to the application server. It must be in the JSON format. The key of each custom parameter must start with x: and contain lowercase letters. Example:


`json
{
  "x:uid": "12345",
  "x:order_id": "67890"
}
`


The callback-var parameter must be used together with the callbackBody parameter. The user ID (uid) and order number (order_id) parameters in the preceding example must be referenced by placeholders ${x:xxx} in callbackBody. Example:


`json
{
  "callbackUrl": "http://oss-demo.aliyuncs.com:23450",
  "callbackBody": "uid=${x:uid}&order=${x:order_id}"
}
`


During the actual callback request process, OSS sends the following content. In this example, the callbackBodyType field is set to application/x-www-form-urlencoded.


`plaintext
uid=12345&order=67890
`


-

After constructing the callback and callback-var parameters, you must Base64-encode them.


-

Example: Base64-encode the callback parameter


The callback parameter that is not Base64-encoded:


`json
{
    "callbackUrl": "http://oss-demo.aliyuncs.com:23450",
    "callbackHost": "your.callback.com",
    "callbackBody": "bucket=${bucket}&object=${object}&uid=${x:uid}&order=${x:order_id}",
    "callbackBodyType": "application/x-www-form-urlencoded",
    "callbackSNI": false
}
`


The callback parameter that is Base64-encoded:


`json
eyJjYWxsYmFja0hvc3QiOiAieW91ci5jYWxsYmFjay5jb20iLCAiY2FsbGJhY2tVcmwiOiAiaHR0cDovL29zcy1kZW1vLmFsaXl1bmNzLmNvbToyMzQ1MCIsICJjYWxsYmFja0JvZHkiOiAiYnVja2V0PSR7YnVja2V0fSZvYmplY3Q9JHtvYmplY3R9JnVpZD0ke3g6dWlkfSZvcmRlcj0ke3g6b3JkZXJfaWR9IiwgImNhbGxiYWNrQm9keVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgImNhbGxiYWNrU05JIjogZmFsc2V9
`


-

Example: Base64-encode the callback-var parameter


The callback-var parameter that is not Base64-encoded:


`json
{
  "x:uid": "12345",
  "x:order_id": "67890"
}
`


The callback-var parameter that is Base64-encoded:


`json
eyJ4OnVpZCI6ICIxMjM0NSIsICJ4Om9yZGVyX2lkIjogIjY3ODkwIn0=
`


-

Add the Base64-encoded parameters to the request.


You can use one of the following methods to add the Base64-encoded parameters to the request.

## (Recommended) Add the parameters to the request as headers


This method is suitable for scenarios in which you want to upload objects to OSS by using OSS SDKs or backend code, which provides high security. You can set the x-oss-callback header to the Base64-encoded callback parameter and x-oss-callback-var to the Base64-encoded callback-var parameter. This x-oss-callback-var header is optional.


-


-


Note: The x-oss-callback-var and x-oss-callback headers are included in canonical headers to calculate a signature.

Example


`json
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
Authorization: OSS qn6q:77Dv
Test
`


## Add the parameters to the form fields in the body of a POST request


This method is supported only for the [PostObject](https://www.alibabacloud.com/help/en/oss/developer-reference/postobject#reference-smp-nsw-wdb) operation. The callback and callback-var parameters can be passed only by using the form fields in the body of the POST request.


-

The callback parameter: You must pass the parameter as a separate form item in the JSON format.


`json
--9431149156168
Content-Disposition: form-data; name="callback"
eyJjYWxsYmFja0hvc3QiOiAieW91ci5jYWxsYmFjay5jb20iLCAiY2FsbGJhY2tVcmwiOiAiaHR0cDovL29zcy1kZW1vLmFsaXl1bmNzLmNvbToyMzQ1MCIsICJjYWxsYmFja0JvZHkiOiAiYnVja2V0PSR7YnVja2V0fSZvYmplY3Q9JHtvYmplY3R9JnVpZD0ke3g6dWlkfSZvcmRlcj0ke3g6b3JkZXJfaWR9IiwgImNhbGxiYWNrQm9keVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgImNhbGxiYWNrU05JIjogZmFsc2V9
`


-

The callback-var parameter: A custom field must be passed in as a separate form item and cannot be encapsulated as a whole callback-var field. This form field is optional.


Sample uid and order_id parameters:


`json
{
  "x:uid": "12345",
  "x:order_id": "67890"
}
`


Convert the uid and order_id parameters to separate fields in the form:


`json
--9431149156168
Content-Disposition: form-data; name="x:uid"
12345
--9431149156168
Content-Disposition: form-data; name="x:order_id"
67890
`


-

(Optional) Verify the callback parameter: You can specify the verification conditions for the callback parameter in the policy. If you leave the conditions empty, the callback parameter is not verified when you upload an object to OSS. Example:


`json
{ "expiration": "2021-12-01T12:00:00.000Z",
  "conditions": [
    {"bucket": "examplebucket" },
    {"callback": "eyJjYWxsYmFja0hvc3QiOiAieW91ci5jYWxsYmFjay5jb20iLCAiY2FsbGJhY2tVcmwiOiAiaHR0cDovL29zcy1kZW1vLmFsaXl1bmNzLmNvbToyMzQ1MCIsICJjYWxsYmFja0JvZHkiOiAiYnVja2V0PSR7YnVja2V0fSZvYmplY3Q9JHtvYmplY3R9JnVpZD0ke3g6dWlkfSZvcmRlcj0ke3g6b3JkZXJfaWR9IiwgImNhbGxiYWNrQm9keVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgImNhbGxiYWNrU05JIjogZmFsc2V9"},
    ["starts-with", "$key", "user/eric/"],
  ]
}
`


## Add the parameters to the URL


-

This method is often used when you upload an object by using a presigned URL. You can encode the Base64-encoded callback and callback-var parameters and concatenate them in the URL to automate callback. However, the callback information is exposed in the URL, which increases security risks. We recommend that you use it only for temporary access or in low-sensitivity scenarios.

-

The `callback` parameter is required, and the `callback-var` parameter is optional. During signature calculation, these parameters must be used as part of the canonical query string. For more information, see [(Recommended) Include a V4 signature in a URL](https://www.alibabacloud.com/help/en/oss/developer-reference/add-signatures-to-urls#d3a828057bem1).


Example:


`plaintext
PUT /your_object?OSSAccessKeyId=LTAI&Signature=vjby*&Expires=1682484377&callback-var=eyJ4OnVpZCI6ICIxMjM0NSIsICJ4Om9yZGVyX2lkIjogIjY3ODkwIn0=&callback=eyJjYWxsYmFja0hvc3QiOiAieW91ci5jYWxsYmFjay5jb20iLCAiY2FsbGJhY2tVcmwiOiAiaHR0cDovL29zcy1kZW1vLmFsaXl1bmNzLmNvbToyMzQ1MCIsICJjYWxsYmFja0JvZHkiOiAiYnVja2V0PSR7YnVja2V0fSZvYmplY3Q9JHtvYmplY3R9JnVpZD0ke3g6dWlkfSZvcmRlcj0ke3g6b3JkZXJfaWR9IiwgImNhbGxiYWNrQm9keVR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwgImNhbGxiYWNrU05JIjogZmFsc2V9 HTTP/1.1
Host: callback-test.oss-cn-hangzhou.aliyuncs.com
Date: Wed, 26 Apr 2023 03:46:17 GMT
Content-Length: 5
Content-Type: text/plain
`


### Process the callback request on the application server
This section shows how the application server processes the callback request. For more information about the sample code for different programming languages, see [Sample code for different programming languages].

The application server must have the following capabilities:


-

Receive the POST request from OSS


After the object is uploaded, OSS automatically sends a POST request to the application server based on the callback parameters. Example:


`json
POST /test HTTP/1.1
Host: your.callback.com
Connection: close
Authorization: GevnM33j7AKluzWnubHSVWI4dY3VsIfUHYWnyw==
Content-MD5: iKU/O/JB*ZMd8Ftg==
Content-Type: application/x-www-form-urlencoded
Date: Tue, 07 May 2024 03:06:13 GMT
User-Agent: aliyun-oss-callback
x-oss-bucket: your_bucket
x-oss-pub-key-url: aHR0cHM6Ly9nb3NzcHVivY2FsbGJeV92MS5wZW0=
x-oss-request-id: 66399AA50*3334673EC2
x-oss-requester: 23313948342006
x-oss-signature-version: 1.0
x-oss-tag: CALLBACK
bucket=your_bucket&object=your_object&uid=12345&order_id=67890
`


-

(Optional) Verify the signature of the request to ensure data security


To ensure that the callback request is sent by OSS, we recommend that you verify the request signature on the application server. For more information, see [Recommended configurations].


> NOTE:

> NOTE: 


> NOTE: Note 

Signature verification is not required. You can enable it based on your business requirements.


-

Return a response for the callback request


After the application server receives the callback request, it must return a response to OSS. The response must meet the following requirements:


-

Normally, the application server returns HTTP/1.1 200 OK.

-

The response returned by the application server to OSS must contain the Content-Length header. The size of the header cannot exceed 3 MB.

-

The response body must be in the JSON format and cannot exceed 1 MB in size.


In this example, the application server returned {"Status": "OK"}.


`http
HTTP/1.0 200 OK
Server: BaseHTTP/0.3 Python/2.7.6
Date: Mon, 14 Sep 2015 12:37:27 GMT
Content-Type: application/json
Content-Length: 9
{"Status": "OK"}
`


OSS returns the response to the client. Example:


`http
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
`


> IMPORTANT:

> NOTE: 


> NOTE: Important 

For a `CompleteMultipartUpload` request, if the response body contains content such as information in the JSON format, the content is overwritten by the callback response after upload callback is enabled. In this example, the content is overwritten by `{"Status": "OK"}`.


## Recommended configurations

### Verify the signature in the callback request to ensure data security


After you configure the callback parameters, OSS sends a callback request to the application server after you upload an object to OSS based on the callbackUrl parameter. To ensure that the request is sent by OSS, you can verify the signature in the callback request. Verification steps:


-

OSS generates a signature on the client


OSS uses the RSA asymmetric encryption algorithm and MD5 hash to generate a signature for the request and adds the signature to the authorization request header.


-

Sample code for signature calculation:


`shell
authorization = base64_encode(rsa_sign(private_key, url_decode(path) + query_string + '\n' + body, md5))
`


> NOTE:

> NOTE: 


> NOTE: Note 

In the preceding code, private_key specifies a private key, path specifies the resource path that is included in the callback request, query_string specifies the query string, and body specifies the message body in the callback request.


-

Steps to generate a signature:


-

Create the string to sign. The string consists of the resource path that is obtained by decoding the URL, the original query string, a carriage return, and the callback message body.

-

Sign the created string by using the RSA encryption algorithm and the private key. The hash function that is used to calculate the signature is MD5.

-

Use Base64 to encode the signed result to obtain the final signature. Then, add the signature to the Authorization header in the callback request.

-

Sample code for signature generation:


`json
POST /index.php?id=1&index=2 HTTP/1.0
Host: 172.16.XX.XX
Connection: close
Content-Length: 18
authorization: kKQeGTRccDKyHB3H9vF+xYMSrmhMZj/kdD1ktNVgbWEfYTQG0G2SU/RaHBovRCE8OkQDjC3uG33esH2t
Content-Type: application/x-www-form-urlencoded
User-Agent: http-client/0.0.1
x-oss-pub-key-url: aHR0cDovL2dvc3NwdWJsaWMuYWxpY2RuLmNvbS9jYWxsYmFja19wdWJfa2V5X3YxLnsr
bucket=examplebucket
`


In the preceding code, the final signature is `kKQeGTRccDKyHB3H9vF+xYMSrmhMZjzzl2/kdD1ktNVgbWEfYTQG0G2SU/RaHBovRCE8OkQDjC3uG33esH2t`. The signature is generated from the `/index.php` path, the `?id=1&index=2` query string, and `bucket=examplebucket` body.

-

The application server verifies the signature


Your application server must verify the signature in the request to confirm the validity of the request source. Procedure:


-

Obtain the public key:


Obtain the Base64-encoded public key URL from the x-oss-pub-key-url request header and decode it.


`plaintext
public_key = urlopen(base64_decode(x-oss-pub-key-url header value))
`


The Base64-encoded public key URL:


`plaintext
aHR0cDovL2dvc3NwdWJsaWMuYWxpY2RuLmNvbS9jYWxsYmFja19wdWJfa2V5X3YxLnBlbQ==
`


The decoded public key URL:


`plaintext
http://gosspublic.alicdn.com/callback_pub_key_v1.pem
`


> NOTE:

> NOTE: 


> NOTE: Note 

The public key URL must start with `http://gosspublic.alicdn.com/` or `https://gosspublic.alicdn.com/`. The content of the public key URL remains unchanged. We recommend that you cache the public key to prevent service impacts due to network fluctuations.


-

Decode the signature.


Obtain the signature from the authorization request header and perform Base64 decoding:


`shell
signature = base64_decode(authorization header value)
`


-

Construct the string to be verified.


Concatenate resource paths, query strings, line breaks, and callback message body in the following format:


`shell
sign_str = url_decode(path) + query_string + '\n' + body
`


-

Verify the signature.


Use the MD5 hash and the RSA public key to verify the signature:


`shell
result = rsa_verify(public_key, md5(sign_str), signature)
`


-

Signature verification example


The following code provides an example on how an application server verifies a signature. Before you run the code in OSS SDK for Python, install the M2Crypto library:


`python
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
        pub_key_url = ''
        try:
            pub_key_url_base64 = self.headers['x-oss-pub-key-url']
            pub_key_url = pub_key_url_base64.decode('base64')
            if not pub_key_url.startswith("http://gosspublic.alicdn.com/") and not pub_key_url.startswith("https://gosspublic.alicdn.com/"):
                self.send_response(400)
                self.end_headers()
                return
            url_reader = urllib2.urlopen(pub_key_url)
            #you can cache it,recommend caching public key content based on the public key address
            pub_key = url_reader.read()
        except:
            print 'pub_key_url : ' + pub_key_url
            print 'Get pub key failed!'
            self.send_response(400)
            self.end_headers()
            return
        #get authorization
        authorization_base64 = self.headers['authorization']
        authorization = authorization_base64.decode('base64')
        #get callback body
        content_length = self.headers['content-length']
        callback_body = self.rfile.read(int(content_length))
        #compose authorization string
        auth_str = ''
        pos = self.path.find('?')
        if -1 == pos:
            auth_str = urllib2.unquote(self.path) + '\n' + callback_body
        else:
            auth_str = urllib2.unquote(self.path[0:pos]) + self.path[pos:] + '\n' + callback_body
        print auth_str
        #verify authorization
        auth_md5 = md5.new(auth_str).digest()
        bio = BIO.MemoryBuffer(pub_key)
        rsa_pub = RSA.load_pub_key_bio(bio)
        try:
            result = rsa_pub.verify(auth_md5, authorization, 'md5')
        except:
            result = False
        if not result:
            print 'Authorization verify failed!'
            print 'Public key : %s' % (pub_key)
            print 'Auth string : %s' % (auth_str)
            self.send_response(400)
            self.end_headers()
            return
        #do something according to callback_body
        #response to OSS
        resp_body = '{"Status":"OK"}'
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(resp_body)))
        self.end_headers()
        self.wfile.write(resp_body)
class MyHTTPServer(HTTPServer):
    def __init__(self, host, port):
        HTTPServer.__init__(self, (host, port), MyHTTPRequestHandler)
if '__main__' == __name__:
    server_ip = get_local_ip()
server_port = 23451
server = MyHTTPServer(server_ip, server_port)
server.serve_forever()
`


The following table describes the code that you can use to verify a signature on the server in other programming languages.








-

(https://gosspublic.alicdn.com/images/AppCallbackServer.zip)

-




-

(https://gosspublic.alicdn.com/images/callback_app_server.py.zip)

-




-

(https://gosspublic.alicdn.com/callback-php-demo.zip)

-


-

(https://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/attach/131396/intl_en/1597211267799/callback-server-dotnet-20200810.zip)

-




-

(https://gosspublic.alicdn.com/doc/oss-doc/callback-nodejs-demo.zip)

-




-

(https://github.com/rockuw/oss-callback-server)

-


| SDK programming language | Description |
| --- | --- |
| Java | Download link: OSS SDK for JavaRunning method: Decompress the package and run java -jar oss-callback-server-demo.jar 9000. You can replace 9000 with a different port number. |
| Python | Download link: OSS SDK for PythonRunning method: Decompress the package and run python callback_app_server.py. The RSA dependencies are required to run the code. |
| PHP | Download link: OSS SDK for PHPRunning method: Deploy the code to an Apache environment to ensure that specific headers in the code can use the environment as a dependency. You can modify the sample code based on the environment. |
| .NET | Download link: OSS SDK for .NETRunning method: Decompress the package and follow the instructions in README.md. |
| Node.js | Download link: OSS SDK for Node.jsRunning method: Decompress the package and run node example.js. |
| Ruby | Download link: OSS SDK for RubyRunning method: Run ruby aliyun_oss_callback_server.rb. |


## Fields supported by the callback parameter


The following table describes the fields supported by the callback parameter. The fields are used to configure the callback request content and behavior after an object is uploaded to OSS.











-


-


-


-




-



-




-


-


-


> NOTE:

> NOTE: 


> NOTE: 





-


-


| Field | Required | Description |
| --- | --- | --- |
| callbackUrl | Yes | The URL of the application server to which OSS sends a callback request. You can specify up to five URLs in a callback request. You must separate URLs with semicolons (;). OSS sends callback requests to each URL until a success response is returned. The URL supports the HTTPS protocol. You cannot enter an IPv6 address or a domain name that points to an IPv6 address. To ensure that Chinese characters can be correctly processed, you must encode the callback URL. |
| callbackBody | Yes | The callback request body. The format of the request body must be consistent with the callbackType field.When the callbackType field is set to the default value application/x-www-form-urlencoded, the callbackBody field must be in the key-value format. Example: bucket=${bucket}&object=${object}&my_var_1=${x:my_var1}&my_var_2=${x:my_var2}.When the callbackType field is set to application/json, the callbackBody field must be in JSON format. Example: {\"bucket\":${bucket},\"object\":${object},\"mimeType\":${mimeType},\"size\":${size},\"my_var1\":${x:my_var1},\"my_var2\":${x:my_var2}}.The callbackBody field supports OSS system parameters, custom parameters, and constants. For more information about the system variables, see System variables supported by callbackBody. |
| callbackHost | No | The value of the Host header in the callback request. The value must be a domain name or an IP address. If you do not configure the callbackHost field, the host values are resolved from the URLs in the callbackUrl field and are specified as the value of the callbackHost field. |
| callbackSNI | No | Specifies whether to specify Server Name Indication (SNI) in the callback request. If the callbackUrl parameter uses HTTPS, we recommend that you enable this parameter. Otherwise, the callback may fail due to certificate mismatch. For example, "502 callback failed" is returned. Valid values:true false (default) Note When a callback request is initiated in the UK (London) region, the SNI is sent regardless of the callbackSNI value. |
| callbackBodyType | No | The value of Content-Type in the callback request, which is the callbackBody data format. Valid values:application/x-www-form-urlencoded (default)If you set the callbackBodyType field to application/x-www-form-urlencoded, the parameters in the callbackBody field are replaced by URL-encoded values. application/jsonIf you set the callbackBodyType field to application/json, the parameters in the callbackBody field are replaced by values in the JSON format. |


## System variables supported by callbackBody


The callbackBody field in the callback parameter allows you to use multiple system parameters to pass the information about the uploaded object in the callback request. The following table describes the supported system parameters.








> IMPORTANT:

> NOTE: 


> NOTE: 


| System parameter | Description |
| --- | --- |
| bucket | The name of the bucket. |
| object | The full path of the object. |
| etag | The ETag field of the object. The ETag is returned to the requester. |
| size | The size of the object. The size is the size of the entire object when you call the CompleteMultipartUpload operation. |
| mimeType | The resource type. For example, the resource type of JPEG images is image/jpeg. |
| imageInfo.height | The height of the image. This parameter applies only to image objects. For other objects, this parameter is left empty. |
| imageInfo.width | The width of the image. This parameter applies only to image objects. For other objects, this parameter is left empty. |
| imageInfo.format | The format of the image. Examples: JPG and PNG. This parameter applies only to image objects. For other objects, this parameter is left empty. |
| crc64 | The CRC64 value. The value of this parameter is the same as that of the x-oss-hash-crc64ecma header returned after the object is uploaded. |
| contentMd5 | The MD5 value. The value of this parameter is the same as that of the Content-MD5 header returned after the object is uploaded. Important This parameter is required only if you call the PutObject or PostObject operation to upload an object. |
| vpcId | The ID of the virtual private cloud (VPC) in which the client that initiates the request resides. If the request is not initiated over a VPC, this parameter is left empty. |
| clientIp | The IP address of the client that initiates the request. |
| reqId | The ID of the request that is initiated. |
| operation | The API operation that is used to initiate the request, such as PutObject and PostObject. |


## SDK


The following table describes the OSS SDKs that you can use to configure callbacks.


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/completemultipartupload#reference-lq1-dtx-wdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/putobject#reference-l5p-ftw-tdb)


(https://www.alibabacloud.com/help/en/oss/developer-reference/upload-callbacks-11)


(https://www.alibabacloud.com/help/en/oss/developer-reference/upload-callbacks-11#bf40fed3a95o5)


(https://www.alibabacloud.com/help/en/oss/developer-reference/upload-an-object-using-a-signed-url-generated-with-oss-sdk-for-java#c70d9abfa09zs)


(https://www.alibabacloud.com/help/en/oss/developer-reference/simple-upload-using-oss-sdk-for-python-v2#c5dae89e32xfo)


(https://www.alibabacloud.com/help/en/oss/developer-reference/upload-an-object-using-a-signed-url-generated-with-oss-sdk-for-python-v2#655eb3b3a7elg)


(https://www.alibabacloud.com/help/en/oss/developer-reference/v2-simple-upload#16bf5fcc0bh6p)


(https://www.alibabacloud.com/help/en/oss/developer-reference/v2-multipart-upload#cad1c80985x85)


(https://www.alibabacloud.com/help/en/oss/developer-reference/v2-presign-upload#c70d9abfa09zs)


|  | Simple upload(PutObject) | Multipart upload(CompleteMultipartUpload) | Presigned URL-based upload(PutObject) |
| --- | --- | --- | --- |
| Java | demo | demo | demo |
| Python V2 | demo | - | demo |
| Go V2 | demo | demo | demo |


## Troubleshooting


If an error occurs during the callback process, an error message that contains an error code is returned by OSS. You can use the error code for troubleshooting. Each error code corresponds to a specific error cause. For information about the error codes related to callbacks, see [07-CALLBACK](https://www.alibabacloud.com/help/en/oss/user-guide/07-callback/).

## FAQ

### Does OSS send a callback request to the application server when an object fails to be uploaded?


No. OSS sends a callback request to the application server only if an object is uploaded. If the object fails to be uploaded, OSS does not send a callback request to the application server but returns an error message.

### What do I do if the "Response body is not valid json format" error message is returned?


-

The error message is returned because the application server throws an exception when the request is being processed. In this case, the response body that is returned to OSS is not in the JSON format. The following figure shows the response that is returned to OSS when this error occurs.![callback](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5544243761/p536785.png)


Solution:


-

Run the following command to confirm the content:


`shell
curl -d "<Content>" <CallbackServerURL> -v
`


-

Capture packets to confirm the content.


We recommend that you use the Wireshark tool in Windows or run the tcpdump command in Linux to capture packets.

-

The body of the response returned by the application server to OSS includes a BOM header.


This error is common among application servers that are written by using OSS SDK for PHP. OSS SDK for PHP returns the BOM header. As a result, OSS receives three additional bytes in the response body that is not in the JSON format. The following figure shows that the ef, bb, and bf bytes are the additional bytes in the response body.


![callback1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/5544243761/p536787.png)


Solution: Delete the BOM header from the response body that is returned by the application server to OSS.

Thank you! We've received your  feedback.