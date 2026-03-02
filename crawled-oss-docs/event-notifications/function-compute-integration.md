# Event Notification - Function Compute Integration

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/event-notification

## Overview

Alibaba Cloud OSS supports seamless, serverless integration with Function Compute (FC) via event notifications. When specific events occur in your OSS bucket (such as object creation or deletion), a Function Compute function is automatically triggered.

## How It Works

1. **Configure event notification rule** on your OSS bucket
2. **Specify Function Compute** as the notification endpoint
3. When a matching event occurs, OSS sends an event payload to Function Compute
4. Function Compute invokes the associated function with the event data

## Event Payload Format

OSS sends event data to Function Compute in a structured JSON format:

```json
{
  "events": [
    {
      "eventName": "ObjectCreated:PutObject",
      "eventSource": "acs:oss",
      "eventTime": "2024-01-15T10:30:00.000Z",
      "eventVersion": "1.0",
      "oss": {
        "bucket": {
          "arn": "acs:oss:cn-hangzhou:123456789:my-bucket",
          "name": "my-bucket",
          "ownerIdentity": "123456789"
        },
        "object": {
          "deltaSize": 1024,
          "eTag": "abc123def456",
          "key": "images/photo.jpg",
          "size": 1024
        },
        "ossSchemaVersion": "1.0",
        "ruleId": "my-rule"
      },
      "region": "cn-hangzhou",
      "requestParameters": {
        "sourceIPAddress": "10.0.0.1"
      },
      "responseElements": {
        "requestId": "58A2C1F3-XXX"
      },
      "userIdentity": {
        "principalId": "123456789"
      }
    }
  ]
}
```

## Configuration via Function Compute Console

1. Log in to the Function Compute Console
2. Create or select a function
3. Navigate to **Triggers**
4. Click **Create Trigger**
5. Select **OSS** as the trigger type
6. Configure:
   - **Bucket Name**: Select the OSS bucket
   - **Event Types**: Choose events to listen for (e.g., `oss:ObjectCreated:*`)
   - **Prefix Filter**: Optional prefix to filter objects (e.g., `images/`)
   - **Suffix Filter**: Optional suffix to filter objects (e.g., `.jpg`)
   - **Role**: Select or create a RAM role with OSS read permissions
7. Click **OK**

## Configuration via Terraform

```hcl
resource "alicloud_fc_trigger" "oss_trigger" {
  service  = alicloud_fc_service.example.name
  function = alicloud_fc_function.example.name
  name     = "oss-trigger"
  role     = alicloud_ram_role.fc_role.arn
  type     = "oss"

  config = jsonencode({
    "events" = ["oss:ObjectCreated:*"]
    "filter" = {
      "key" = {
        "prefix" = "images/"
        "suffix" = ".jpg"
      }
    }
    "bucketName" = "my-bucket"
  })
}
```

## Common Use Cases

### 1. Image Processing
Automatically resize, watermark, or transcode images upon upload:

```python
import oss2
from PIL import Image
import io

def handler(event, context):
    evt = json.loads(event)
    bucket_name = evt['events'][0]['oss']['bucket']['name']
    object_key = evt['events'][0]['oss']['object']['key']

    # Process the uploaded image
    auth = oss2.StsAuth(context.credentials.access_key_id,
                         context.credentials.access_key_secret,
                         context.credentials.security_token)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    # Download, process, and re-upload
    result = bucket.get_object(object_key)
    img = Image.open(io.BytesIO(result.read()))
    img.thumbnail((800, 600))

    output = io.BytesIO()
    img.save(output, format='JPEG')
    bucket.put_object(f"thumbnails/{object_key}", output.getvalue())
```

### 2. Data Pipeline / ETL
Trigger ETL processing when new data files land in OSS.

### 3. Log Processing
Process and analyze log files as they arrive.

### 4. Content Moderation
Scan uploaded content for compliance.

### 5. Backup / Replication
Copy or archive objects to other regions or services.

## Important Requirements

- OSS bucket and Function Compute must be in the **same region**
- A proper **RAM role** must be granted for FC to access OSS
- **Prefix/suffix filters** can narrow which objects trigger the function
- Supports both **synchronous and asynchronous** invocation modes
- Each bucket can have multiple event notification rules configured
