# Use mirroring-based back-to-origin to fetch files that do not exist in a bucket from an origin server

To prevent service interruptions from incomplete data migration, you can configure mirroring-based back-to-origin when migrating your business from a self-managed origin server or a third-party cloud storage service to Alibaba Cloud Object Storage Service (OSS). When this feature is configured, if a user requests an object that does not exist in OSS, OSS automatically fetches the object from the specified origin server. OSS then returns the object to the user and stores it in the bucket. This feature ensures uninterrupted access to all data during the migration and provides a seamless business transition.

## How it works


The core of the mirroring-based back-to-origin feature is server-side proxying. When a client sends a GET request for an object that does not exist in OSS, if the request triggers a back-to-origin rule, such as a matching object prefix and an HTTP 404 error, the OSS server automatically sends an HTTP request to the specified origin server to fetch the object. If the origin server returns a 200 status code, OSS returns the object's content to the client and stores the object in the OSS bucket. If the origin server returns a 404 or another error status code, OSS returns the corresponding error message to the client. In this process, OSS acts as a proxy to enable on-demand migration and one-time caching of objects. Note that after an object is stored in OSS, OSS does not automatically synchronize updates even if the source object on the origin server is updated.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/6947464671/CAEQTxiBgICQ.6K70hkiIGIyYjQyMGYxMGZjZTQ1OTdhNTkwY2U5ZmI1YWNkNTU43963382_20230830144006.372.svg)
## Fetch missing files from a specified website


This is the most basic scenario for mirroring-based back-to-origin. When a user requests an object that does not exist in OSS, the system automatically fetches the object from the specified origin server and stores it in OSS. The following example shows how to configure this feature to fetch missing objects from a specified website. When an object that does not exist in the `examplefolder/` directory of `examplebucket` is accessed, OSS automatically fetches the object from `https://example.com/`.

#### Step 1: Configure a mirroring-based back-to-origin rule


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the left-side navigation pane, choose Data Management > Mirroring-based Back-to-origin.

-

On the Mirroring-based Back-to-origin page, click Create Rule.

-

In the Create Rule panel, configure the parameters. Keep the default values for parameters that are not mentioned.


























| Parameter | Configuration |
| --- | --- |
| Method | Select Mirroring. |
| Condition | Select Object Name Prefix and enter examplefolder/. |
| Origin URL | In the first column (Protocol), select https. In the second column (Domain Name), enter example.com. Leave the third column (Path Prefix) empty. The path prefix is appended to the domain name to form the path part of the origin URL. |


-

Click OK.

#### Step 2: Verify the rule


-

Access `https://examplebucket.oss-cn-hangzhou.aliyuncs.com/examplefolder/example.txt`.

-

If the `examplefolder/example.txt` object does not exist in `examplebucket`, OSS sends a request to `https://example.com/examplefolder/example.txt` for the object.

-

After fetching the object, OSS saves it to `examplebucket` as `examplefolder/example.txt`, and returns the object to the requester.

## Replace a directory and verify file integrity during origin fetch


In some scenarios, the directory structure in OSS differs from that of the origin server. You may also need to ensure the integrity of objects fetched from the origin server. This scenario shows how to map directories and use MD5 validation to ensure reliable object transfer during an origin fetch:


-

When a requester accesses an object that does not exist in the `examplefolder` directory of `bucket-01` in the China (Hangzhou) region, the object can be fetched from the `destfolder` directory of the `https://example.com` site.

-

The MD5 hash of the fetched object must be verified. Objects with a mismatched MD5 hash are not saved in `bucket-01`.


Step 1: Configure a mirroring-based back-to-origin rule


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the left-side navigation pane, choose Data Management > Mirroring-based Back-to-origin.

-

On the Mirroring-based Back-to-origin page, click Create Rule.

-

In the Create Rule panel, configure the required parameters as described in the following table. Keep the default configurations for other parameters.


























> NOTE:

> NOTE: 


> NOTE: 
















-


-


| Parameter | Configuration |
| --- | --- |
| Method | Select Mirroring. |
| Condition | Select Object Name Prefix and set it to examplefolder/. |
| Replace or Delete File Prefix | Select Replace or Delete File Prefix and set it to destfolder/.Note This option appears only after you set Object Name Prefix in the Origin Fetch Condition section. |
| Origin URL | Set the first column to https, the second column to example.com, and leave the third column empty. |
| MD5 Verification | Select Perform MD5 verification. When the response to the back-to-origin request contains the Content-MD5 field, OSS checks whether the MD5 hash of the fetched file matches the value of the Content-MD5 field.Match: The client gets the file, and OSS saves the fetched file.Mismatch: The client receives the object because the data is streamed directly. However, if the checksum calculation, which requires the complete object data, fails, OSS does not store the object in the bucket. |


-

Click OK.

#### Step 2: Verify the rule


-

Access `https://bucket-01.oss-cn-hangzhou.aliyuncs.com/examplefolder/example.txt`.

-

If the `examplefolder/example.txt` object does not exist in `bucket-01`, OSS sends a request to `https://example.com/destfolder/example.txt` for the object.

-

After fetching the object, OSS performs the following operations:


-

If the back-to-origin response contains the Content-MD5 field, OSS calculates the MD5 hash of the fetched object and compares it with the value of the Content-MD5 field. If the MD5 hash matches, OSS renames the object to `examplefolder/example.txt`, saves it to `bucket-01`, and returns the object to the requester. If the MD5 hash does not match, OSS returns the object to the user but does not save it to `bucket-01`.

-

If the back-to-origin response does not contain the Content-MD5 field, OSS renames the object to `examplefolder/example.txt`, saves it to `bucket-01`, and returns the object to the requester.

## Fetch from different sites based on different directories


If your business involves multiple origin servers, you can route requests to different origin servers based on the requested directory path. This scenario is suitable for migrating data from multiple origin servers or a distributed storage architecture. For example, you have two origin servers with the same directory structure: Origin Server A (`https://example.com`) and Origin Server B (`https://example.org`). You need to implement the following scenario:


-

When a requester accesses an object that does not exist in the `bucket-02/dir1` directory in the China (Beijing) region, the object is fetched from the `example1` directory of the `https://example.com` site.

-

When a requester accesses an object that does not exist in the `bucket-02/dir2` directory, the object is fetched from the `example2` directory of the `https://example.org` site.

-

Depending on whether redirection policies are set for Origin Server A and Origin Server B, OSS decides whether to request the object from the address specified in the redirection.


Step 1: Configure mirroring-based back-to-origin rules


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the left-side navigation pane, choose Data Management > Mirroring-based Back-to-origin.

-

On the Mirroring-based Back-to-origin page, click Create Rule.

-

In the Create Rule panel, configure two mirroring-based back-to-origin rules as described below. Keep the default configurations for other parameters.


-

Rule 1


> NOTE:

> NOTE: 


> NOTE: 
















> NOTE:

> NOTE: 


> NOTE: 




| Parameter | Configuration |
| --- | --- |
| Method | Select Mirroring. |
| Condition | Select Object Name Prefix and set it to dir1/. |
| Replace or Delete File Prefix | Select Replace or Delete File Prefix and set it to example1/.Note This option appears only after you set Object Name Prefix in the Origin Fetch Condition section. |
| Origin URL | Set the first column to https, the second column to example.com, and leave the third column empty. |
| 3xx Response | Select Follow Origin to Redirect Request.Note If Follow Origin to Redirect Request is not selected, OSS directly returns the address specified by the origin server's redirection rule to the requester. |


-

Rule 2


> NOTE:

> NOTE: 


> NOTE: 
















| Parameter | Configuration |
| --- | --- |
| Method | Select Mirroring. |
| Condition | Select Object Name Prefix and set it to dir2/. |
| Replace or Delete File Prefix | Select Replace or Delete File Prefix and set it to example2/.Note This option appears only after you set Object Name Prefix in the Origin Fetch Condition section. |
| Origin URL | Set the first column to https, the second column to example.org, and leave the third column empty. |
| 3xx Response | Select Follow Origin to Redirect Request. |


-

Click OK.


Step 2: Verify the rules


-

Access `https://bucket-02.oss-cn-beijing.aliyuncs.com/dir1/example.txt`.

-

If the `example.txt` object does not exist in the `dir1` directory of `bucket-02`, OSS sends a request to `https://example.com/example1/example.txt` for the object.


-

If Origin Server A has a redirection rule for `example1/example.txt`, OSS sends a new request to the address specified in the redirection rule. After fetching the object, OSS saves it to `bucket-02` as `dir1/example1/example.txt` and returns it to the requester.

-

If Origin Server A does not have a redirection rule for `example1/example.txt`, OSS fetches the object, saves it to `bucket-02` as `dir1/example1/example.txt`, and returns it to the requester.

-

If a requester accesses `https://bucket-02.oss-cn-beijing.aliyuncs.com/dir2/example.txt`, the object fetched by the mirroring-based back-to-origin rule is stored in the `dir2/example2` directory of `bucket-02`.

## Fetch from a private bucket and pass through specified parameters


When the origin server is a private OSS bucket, you need to configure the required access permissions. You may also need to pass specific parameters from the client request to the origin server. This scenario shows how to configure mirroring-based back-to-origin for a private OSS origin server and pass through parameters. For example, you have two buckets in the China (Shanghai) region: `bucket-03` (public-read) and `bucket-04` (private). You need to implement the following scenario:


-

When a requester accesses an object that does not exist in the `examplefolder` directory within the root directory of `bucket-03`, the object is fetched from the `examplefolder` directory of `bucket-04`.

-

The query string in the request URL is passed to the origin server.

-

The HTTP headers `header1`, `header2`, and `header3` in the request URL are passed to the origin server.


Step 1: Configure a mirroring-based back-to-origin rule


-

Go to the [Buckets](https://oss.console.alibabacloud.com/bucket) page and click the name of the target bucket.

-

In the left-side navigation pane, choose Data Management > Mirroring-based Back-to-origin.

-

On the Mirroring-based Back-to-origin page, click Create Rule.

-

In the Create Rule panel, configure the required parameters as described in the following table. Keep the default configurations for other parameters.
































-


-






















> IMPORTANT:

> NOTE: 


> NOTE: 


| Parameter | Configuration |
| --- | --- |
| Method | Select Mirroring. |
| Condition | Select Object Name Prefix and set it to examplefolder/. |
| Origin Type | Select OSS Private Bucket and select bucket-04 from the Source Bucket drop-down list.After you configure this option, when a user accesses an object that does not exist, OSS uses the default role AliyunOSSMirrorDefaultRole to fetch data from the specified private origin bucket. The data retrieval process requires the AliyunOSSReadOnlyAccess permission. This permission ensures that OSS can only access the origin server data in read-only mode, preventing modification or deletion of the data.When a Resource Access Management (RAM) user configures mirroring-based back-to-origin for a private OSS bucket, the RAM user must have the ram:GetRole permission. This permission is used to check whether the AliyunOSSMirrorDefaultRole role exists.If the role exists, it is used directly.If the role does not exist, we recommend that the Alibaba Cloud account associated with the RAM user creates the AliyunOSSMirrorDefaultRole role in advance and grants the AliyunOSSReadOnlyAccess permission to this role. This avoids granting high-risk permissions to the RAM user, such as creating roles (ram:CreateRole) and granting permissions to roles (ram:AttachPolicyToRole). After the authorization is complete, the RAM user can directly reuse the created role, which reduces permission configuration risks. |
| Origin URL | Set the first column to https and leave the others empty. |
| Origin Parameter | Select Transfer with Query String.OSS passes the query string from the URL request to the origin server. |
| Set Transmission Rule of HTTP Header | Select Transmit Specific HTTP Headers and add the HTTP headers header1, header2, and header3. Back-to-origin rules do not support passing some standard HTTP headers, such as authorization, authorization2, range, and content-length, date, or HTTP headers that start with x-oss-, oss-, or x-drs-.Important When fetching from a private bucket, do not select to pass all HTTP header parameters. Otherwise, the origin fetch will fail. |


-

Click OK.


Step 2: Verify the rule


-

Access `https://bucket-03.oss-cn-shanghai.aliyuncs.com/examplefolder/example.png?caller=lucas&production=oss`.

-

If the `examplefolder/example.png` object does not exist in `bucket-03`, OSS sends a request to `https://bucket-04.oss-cn-shanghai.aliyuncs.com/examplefolder/example.png?caller=lucas&production=oss` for the object.

-

`bucket-04` processes the request by using the passed query string `?caller=lucas&production=oss` and returns the `example.png` object to OSS.

-

OSS renames the fetched object to `examplefolder/example.png` and stores it in `bucket-03`.


If the request also carries the HTTP headers `header1`, `header2`, and `header3`, they are also passed to `bucket-04`.

## Apply in production

#### Seamless data migration


For more information about this migration solution, see [Seamlessly migrate services to Alibaba Cloud OSS using mirroring-based back-to-origin](https://www.alibabacloud.com/help/en/data-online-migration/user-guide/seamless-business-migration-to-alibaba-cloud-oss).

#### Refresh objects fetched from the origin server


Because mirroring-based back-to-origin is a one-time caching mechanism, OSS does not automatically refresh or re-fetch an object even if the source object on the origin server is updated. Use the following methods to refresh objects that are already stored in OSS.


-

Manual deletion: Delete the object in OSS using the console or an API. The next time the object is accessed, the back-to-origin rule is triggered again.

-

Lifecycle rule: Configure a lifecycle rule for objects fetched from the origin server so that they are automatically deleted after a fixed period for periodic refreshing.

-

Object name versioning: When updating an object on the origin server, use a new name, such as `style.v2.css`. This fundamentally avoids caching issues and is the recommended practice.

#### Risk prevention and fault tolerance


-

Origin server load: Ensure that your origin server has sufficient bandwidth and processing capacity to handle back-to-origin requests. During the initial phase of migration, the volume of back-to-origin requests may be large. We recommend that you monitor the origin server load and prefetch data during off-peak hours.

-

Cost control: To prevent unexpectedly high costs, we recommend that you set up cost alerts in the Alibaba Cloud Management Center to monitor the volume of back-to-origin requests.

-

Security configuration: Ensure that OSS can access the origin server. If the origin URL uses the HTTPS protocol, make sure that the origin server's certificate is issued by a trusted certificate authority (CA), the domain name matches, and the certificate has not expired.

-

Log query: Use the [real-time log query](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/) feature to view back-to-origin logs. The User-Agent for back-to-origin requests contains the string `aliyun-oss-mirror`.

## Quotas and limitations


-

Number and order of rules: You can configure up to 20 back-to-origin rules for each bucket. The rules are matched in ascending order of their [RuleNumber](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketwebsite#table-fjp-2as-60m). When a rule is matched, it is executed, and subsequent rules are ignored. You can adjust the matching priority using the Up or Down operations to the right of a rule.

-

QPS and traffic:


-

Regions in the Chinese mainland: The default total QPS is 2,000, and the total bandwidth is 2 Gbit/s.

-

Regions outside the Chinese mainland: The default total QPS is 1,000, and the total bandwidth is 1 Gbit/s.

-

This limit is the total mirroring-based back-to-origin capacity for all buckets under a single Alibaba Cloud account in the corresponding region. If the limit is exceeded, requests are throttled, and a 503 error is returned. If you need a higher quota, contact Technical Support.

-

Origin server address: The address must be a domain name or IP address that can be accessed over the Internet and complies with RFC 3986 encoding standards. Internal network addresses are not supported.

-

Timeout period: The default timeout period for mirroring-based back-to-origin is 10 seconds.

## FAQ

#### Why is the size of the file fetched from the origin server different from the size of the source file?


If the size of an object fetched from the origin server differs from the size of the source object, perform the following troubleshooting steps.


-

Check the `Last-Modified` timestamps of the fetched object and the source object.


`python
import oss2
import requests
from datetime import datetime
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Obtain access credentials from environment variables. Before you run this sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the Endpoint for the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the Endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"

# Specify the region information that corresponds to the Endpoint, for example, cn-hangzhou. Note that this parameter is required for V4 signatures.
region = "cn-hangzhou"

# Set yourBucketName to the name of the bucket for which you configured the mirroring-based back-to-origin rule.
bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region)
# Specify the full path of the object file.
object_key = 'yourObjectKey'
# Specify the full path of the source file.
source_url = 'yourSourceUrl'

# Get the Last-Modified timestamp of the fetched file.
oss_object_info = bucket.get_object_meta(object_key)
oss_last_modified = oss_object_info.headers['last-modified']
print(f"OSS Last-Modified: {oss_last_modified}")

# Get the Last-Modified timestamp of the source file.
response = requests.head(source_url)
source_last_modified = response.headers.get('last-modified')
print(f"Source Last-Modified: {source_last_modified}")

# Convert the timestamp strings to datetime objects for comparison.
oss_time = datetime.strptime(oss_last_modified, '%a, %d %b %Y %H:%M:%S %Z')
source_time = datetime.strptime(source_last_modified, '%a, %d %b %Y %H:%M:%S %Z')

if oss_time < source_time:
    print("The source file has been updated.")
elif oss_time > source_time:
    print("The fetched file is newer.")
else:
    print("The timestamps of the two files are the same.")
`


-

If the `Last-Modified` timestamp of the source object is later than the `Last-Modified` timestamp of the fetched object, the source object may have been updated after the object was fetched.


> NOTE:

> NOTE: 


> NOTE: Note 

When OSS fetches an object from an origin server and writes it to the destination bucket, it does not preserve the `Last-Modified` timestamp of the source object (the time the source object was last modified). Instead, OSS sets the `Last-Modified` timestamp of the fetched object to the time it was created or updated in OSS through the mirroring-based back-to-origin feature.


-

If the `Last-Modified` timestamp of the source object is earlier than or the same as the `Last-Modified` timestamp of the fetched object, the source object has not been updated since the fetched object was generated. Proceed to the next step to check their MD5 or 64-bit cyclic redundancy check (CRC-64) values.

-

Compare the MD5 or CRC-64 values of the fetched object and the source object.


`python
# -*- coding: utf-8 -*-
import oss2
import hashlib
import requests
# To compare CRC-64, because the Python standard library does not support CRC-64, you can use a third-party library such as crcmod.
# Install crcmod: pip install crcmod
import crcmod
from oss2.credentials import EnvironmentVariableCredentialsProvider

# Obtain access credentials from environment variables. Before you run this sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the Endpoint for the region where the bucket is located. For example, if the bucket is in the China (Hangzhou) region, set the Endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"

# Specify the region information that corresponds to the Endpoint, for example, cn-hangzhou. Note that this parameter is required for V4 signatures.
region = "cn-hangzhou"

# Set yourBucketName to the name of the bucket for which you configured the mirroring-based back-to-origin rule.
bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region)
# Specify the full path of the object file.
object_key = 'yourObjectKey'
# Specify the full path of the source file.
source_url = 'yourSourceUrl'

# Get the metadata of the fetched file.
oss_object_info = bucket.get_object_meta(object_key)

oss_md5 = oss_object_info.headers.get('etag', '').strip('"')  # ETag is usually the MD5 hash
oss_crc64 = oss_object_info.headers.get('x-oss-hash-crc64ecma', '')

print(f"OSS MD5: {oss_md5}")
print(f"OSS CRC64: {oss_crc64}")

# Get the content of the source file and calculate its MD5 and CRC-64.
response = requests.get(source_url)
if response.status_code == 200:
    source_content = response.content
    source_md5 = hashlib.md5(source_content).hexdigest()
    print(f"Source MD5: {source_md5}")

    crc64_func = crcmod.predefined.mkCrcFun('crc-64')
    source_crc64 = hex(crc64_func(source_content))[2:].upper().zfill(16)  # Convert to a hex string and format it
    print(f"Source CRC64: {source_crc64}")

    # Compare the MD5 values.
    if oss_md5 == source_md5:
        print("MD5 values match.")
    else:
        print("MD5 values do not match.")

    # Compare the CRC-64 values.
    if oss_crc64.upper() == source_crc64:
        print("CRC-64 values match.")
    else:
        print("CRC-64 values do not match.")
else:
    print(f"Failed to fetch source file. HTTP Status Code: {response.status_code}")

`


-

If their MD5 or CRC-64 values match, the content of the two objects is the same. In this case, the sizes of the two objects should be the same.

-

If their MD5 or CRC-64 values do not match, the content of the two objects is different. Proceed to the next step to check for special request headers.

-

Check for special request headers.


![screenshot_2025-02-18_17-04-03](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8063700471/p917892.png)


-

Check whether the mirroring-based back-to-origin request contains special HTTP request headers, such as `Accept-Encoding: gzip, deflate, br`. This header indicates that the client can accept compressed data formats.

-

If the mirroring-based back-to-origin request uses HTTP compression logic and the requested object meets the compression conditions, the sizes of the two objects will also be different.

-

If the `Accept-Encoding` header is present, you must prohibit it from being passed.


-

If you configured the rule to pass all HTTP headers, you must add `accept-encoding` to the list of prohibited HTTP headers.


![p917892](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8063700471/p918270.png)

-

If you configured the rule to pass specified HTTP headers, make sure that `accept-encoding` is not included in the list of specified headers.


![screenshot_2025-02-19_14-30-45](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8063700471/p918276.png)

#### How do I troubleshoot an origin fetch failure?


If an origin fetch fails and returns an error such as `424 MirrorFailed`, perform the following troubleshooting steps.


-

Check the reachability of the origin server.


`bash
# Replace the URL with your actual origin server address and file path
curl -I "https://www.example.com/images/test.jpg"
`


-

Check the DNS resolution.


`bash
# Replace the domain name with your actual origin server domain name
nslookup www.example.com
`


-

Check the HTTPS certificate (if the origin server uses HTTPS).


`bash
# Replace the domain name with your actual origin server domain name
openssl s_client -connect www.example.com:443 -servername www.example.com
`


-

Analyze the issue using the OSS [real-time log query](https://www.alibabacloud.com/help/en/oss/user-guide/real-time-log-query/) feature.

#### Why is a file not generated through mirroring-based back-to-origin?


A client sends a HEAD request to retrieve object metadata, such as its size and type, without downloading the actual object content. A HEAD request does not trigger a mirroring-based back-to-origin rule. Therefore, the object is not fetched from the origin server or written to the destination bucket.

#### Why does a mirroring-based back-to-origin request return an unexpected status code?


If a back-to-origin request is triggered and the origin server returns a status code other than 404, 200, or 206, you must analyze the origin server's response.


-

The origin server is OSS: Check the following configuration items.


-

Prohibit specified HTTP headers from being passed: Prohibit the `host` header from being passed. This prevents the exposure of origin server information and ensures that back-to-origin requests are processed as expected. If the `host` header is passed through, the origin request uses the Host header of the destination bucket. Because each bucket's Host header is unique, this will not match the origin server's expected Host, causing the origin to return a 403 error. OSS then translates this failure into a 424 MirrorFailed error for the client.


![screenshot_2025-02-19_14-31-42](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/8063700471/p918280.png)

-

Private OSS bucket for origin fetch: If no permissions are configured, check whether the ACL of the destination bucket and its objects is set to public-read. If permissions are configured, check whether the authorization policy of the role used for mirroring-based back-to-origin was changed, which may result in insufficient permissions. The default role used for mirroring-based back-to-origin is `AliyunOSSMirrorDefaultRole`, and its default system policy is `AliyunOSSReadOnlyAccess`.

-

The origin server is not OSS: Check the server-side logs and configurations such as Server Name Indication (SNI), back-to-origin parameters, and header pass-through to analyze the specific cause of the origin server exception. The origin server might return status codes such as 401 (Unauthorized), 403 (Forbidden), or 5xx (Server Internal Error).

#### What is the matching order of back-to-origin rules?


Rules are matched in ascending order of their rule number (`RuleNumber`). When the first matching rule is found, it is executed, and the matching process stops.

#### Can I fetch from a service in a VPC or an internal IP address?


No. The origin server must have a publicly accessible address. To access a service within a VPC, you can expose it to the Internet using a NAT Gateway or an Internet-facing SLB instance.

#### After a source file is updated, why is the file in OSS not updated?



Mirroring-based back-to-origin is a one-time pull mechanism and does not automatically synchronize updates from the origin server. You must manually delete the fetched object in OSS or use a file name versioning strategy to retrieve the new object.


Thank you! We've received your  feedback.