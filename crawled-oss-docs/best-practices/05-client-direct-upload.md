# Client-Side Direct Upload Best Practices

Source: https://help.aliyun.com/zh/oss/user-guide/uploading-objects-to-oss-directly-from-clients/

## Overview

Client-side direct upload allows clients to upload files directly to OSS without routing through your application server. Compared to server-side proxy upload, direct upload:
- Avoids file relay through business servers
- Improves upload speed
- Saves server resources

## Why Client-Side Direct Upload?

In typical server-client architectures, the common upload flow is server-proxy upload: the client uploads the file to the business server, which then uploads it to OSS. This means data traverses the network twice, wasting bandwidth and increasing server overhead.

With direct upload, the client connects directly to OSS, eliminating the intermediary.

## Implementation Challenges

### 1. Cross-Origin Access (CORS)

For Web and Mini Program clients, browsers and containers restrict cross-origin access for security. Configure your OSS Bucket's CORS rules to allow specified domains to access OSS directly.

### 2. Security Authorization

Uploading to OSS requires RAM user AccessKeys for signature authentication. Using long-lived AccessKeys in clients risks key leakage. Three secure approaches:

## Approach 1: STS Temporary Credentials (Recommended)

Best for most upload scenarios, including multipart upload and resumable upload.

### Flow
1. Client requests temporary credentials from business server
2. Business server uses STS SDK to call `AssumeRole` API
3. STS generates and returns temporary credentials
4. Business server returns credentials to client
5. Client uses OSS SDK with temporary credentials to upload
6. OSS returns success response

### Server-Side Code (Python)
```python
import json
from alibabacloud_tea_openapi.models import Config
from alibabacloud_sts20150401.client import Client as Sts20150401Client
from alibabacloud_sts20150401 import models as sts_20150401_models
from alibabacloud_credentials.client import Client as CredentialClient

role_arn_for_oss_upload = '<YOUR_ROLE_ARN>'
region_id = '<YOUR_REGION_ID>'

def get_sts_token():
    config = Config(region_id=region_id, credential=CredentialClient())
    sts_client = Sts20150401Client(config=config)
    assume_role_request = sts_20150401_models.AssumeRoleRequest(
        role_arn=role_arn_for_oss_upload,
        role_session_name='<YOUR_ROLE_SESSION_NAME>'
    )
    response = sts_client.assume_role(assume_role_request)
    token = json.dumps(response.body.credentials.to_map())
    return token
```

### Client-Side Code (JavaScript)
```javascript
let credentials = null;
const form = document.querySelector("form");
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  // Only refresh credentials when expired
  if (isCredentialsExpired(credentials)) {
    const response = await fetch("/get_sts_token_for_oss_upload", {
      method: "GET",
    });
    credentials = await response.json();
  }
  const client = new OSS({
    bucket: "<YOUR_BUCKET>",
    region: "oss-<YOUR_REGION>",
    accessKeyId: credentials.AccessKeyId,
    accessKeySecret: credentials.AccessKeySecret,
    stsToken: credentials.SecurityToken,
  });

  const fileInput = document.querySelector("#file");
  const file = fileInput.files[0];
  const result = await client.put(file.name, file);
  console.log(result);
});

function isCredentialsExpired(credentials) {
  if (!credentials) return true;
  const expireDate = new Date(credentials.Expiration);
  const now = new Date();
  return expireDate.getTime() - now.getTime() <= 60000;
}
```

### Best Practices for STS
- **Cache STS credentials** to avoid frequent STS service calls (rate limiting)
- **Refresh before expiration** to maintain continuous access
- **Add extra permission policies** to STS credentials to further restrict permissions
- **Set reasonable expiration times** (recommended: 900-3600 seconds)

## Approach 2: Server-Generated PostObject Signature

Best for scenarios requiring upload file attribute restrictions. Use HTML form-based upload.

### Flow
1. Server generates PostObject signature, Post Policy, and related information
2. Client uploads directly to OSS using these credentials without OSS SDK
3. Post Policy restricts file attributes (size, type, etc.)

### Limitations
- Does NOT support multipart upload
- Does NOT support resumable upload

## Approach 3: Server-Generated Signed URL (PutObject)

Best for simple file upload scenarios.

### Flow
1. Server uses OSS SDK to generate a signed URL for PutObject
2. Client uploads directly using the signed URL without OSS SDK

### Limitations
- Does NOT support multipart upload for large files
- Does NOT support resumable upload
- Generating signed URLs per part increases server interaction complexity
- Client could modify part content or order, causing incorrect final merged files

## Platform-Specific Implementation Guides

- **Web direct upload**: Browser-based upload using JavaScript SDK
- **Mini Program direct upload**: WeChat/Alipay mini programs
- **Mobile app direct upload**: iOS and Android native apps
- **HarmonyOS direct upload**: Huawei HarmonyOS environment

## Server-Side Signature Direct Upload Flow

For production environments, the recommended architecture is:

```
┌──────────┐     1. Request credentials      ┌──────────────┐
│  Client   │ ──────────────────────────────> │  App Server   │
│  (Web/    │ <────────────────────────────── │  (Your API)   │
│  Mobile)  │     2. Return STS token         │               │
│           │                                  │   ┌────────┐  │
│           │     3. Direct upload             │   │STS SDK │  │
│           │ ──────────────────────────────> └───┘────────┘──┘
│           │                 ┌──────────┐          │
│           │ ──────────────> │   OSS    │          │ AssumeRole
│           │ <────────────── │  Bucket  │          │
└──────────┘  4. Success      └──────────┘     ┌────┴─────┐
                                                │   STS    │
                                                │ Service  │
                                                └──────────┘
```
