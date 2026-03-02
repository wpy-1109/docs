# Event Notification

> Source: https://www.alibabacloud.com/help/en/oss/user-guide/event-notification

## Overview

Alibaba Cloud OSS supports event notification rules that allow you to be notified when specific operations occur on objects in your bucket. When a specified event occurs, a notification message is sent to a designated endpoint such as an MNS (Message Service) queue or topic, or Function Compute.

## Prerequisites

1. **OSS Bucket** created in a supported region
2. **Message Service (MNS)** or **Function Compute** service activated (depending on your chosen notification endpoint)
3. Appropriate **RAM permissions** configured

## Supported Event Types

### ObjectCreated Events (New or Updated Objects)

| Event Type | Description |
|-----------|-------------|
| `ObjectCreated:*` | Any object creation event |
| `ObjectCreated:PutObject` | Triggered when a file is uploaded via the PutObject operation |
| `ObjectCreated:PostObject` | Triggered when a file is uploaded via the PostObject operation |
| `ObjectCreated:CopyObject` | Triggered when a file is copied via the CopyObject operation |
| `ObjectCreated:CompleteMultipartUpload` | Triggered when a multipart upload is completed |
| `ObjectCreated:AppendObject` | Triggered when data is appended to an object |

### ObjectRemoved Events (Deleted Objects)

| Event Type | Description |
|-----------|-------------|
| `ObjectRemoved:DeleteObject` | Triggered when an object is deleted |
| `ObjectRemoved:DeleteObjects` | Triggered when multiple objects are deleted |

### Other Events

| Event Type | Description |
|-----------|-------------|
| `ObjectReplication:ObjectCreated` | Triggered when an object is created via cross-region replication |
| `ObjectReplication:ObjectRemoved` | Triggered when an object is removed via cross-region replication |
| `ObjectDownload:GetObject` | Triggered when an object is downloaded |
| `ObjectModified:Overwritten` | Triggered when an object is overwritten |
| `LifecycleTransition` | Triggered when an object transitions storage class due to lifecycle rules |
| `LifecycleExpiration` | Triggered when an object expires due to lifecycle rules |
| `LifecycleExpiration:ObjectDeleteMarkerCreated` | Triggered when a delete marker is created due to lifecycle rules |

## Notification Endpoints

| Endpoint Type | Description |
|--------------|-------------|
| **MNS Queue** | Messages pushed to an MNS queue for pull-based consumption |
| **MNS Topic** | Messages pushed to an MNS topic for pub/sub notification |
| **Function Compute** | Triggers a serverless function in Alibaba Cloud Function Compute |

## Configuration via OSS Console

1. Log in to the [OSS Console](https://oss.console.aliyun.com)
2. Click on the target **Bucket** name
3. In the left navigation pane, go to **Basic Settings** > **Event Notification**
4. Click **Create Rule** and configure:

| Parameter | Description |
|-----------|-------------|
| **Rule Name** | A unique name for the event notification rule |
| **Events** | Select the event types to monitor |
| **Resource Description (Prefix/Suffix)** | Filter objects by prefix and/or suffix (e.g., prefix: `images/`, suffix: `.jpg`) |
| **Endpoint** | Choose the notification destination: MNS Queue, MNS Topic, or Function Compute |

5. Click **OK** to save the rule.

## Configuration via API

You can configure event notifications programmatically using:

- **PutBucketNotification** API
- **GetBucketNotification** API
- **DeleteBucketNotification** API

### PutBucketNotification Request Body (XML)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<NotificationConfiguration>
  <TopicConfiguration>
    <Id>example-rule</Id>
    <Filter>
      <S3Key>
        <FilterRule>
          <Name>prefix</Name>
          <Value>images/</Value>
        </FilterRule>
        <FilterRule>
          <Name>suffix</Name>
          <Value>.jpg</Value>
        </FilterRule>
      </S3Key>
    </Filter>
    <Topic>acs:mns:<region>:<account-id>:/topics/<topic-name></Topic>
    <Event>ObjectCreated:PutObject</Event>
    <Event>ObjectCreated:PostObject</Event>
  </TopicConfiguration>
</NotificationConfiguration>
```

## Configuration via SDK (Python)

```python
import oss2
from oss2.models import BucketNotification, NotificationRule

auth = oss2.Auth('<AccessKeyId>', '<AccessKeySecret>')
bucket = oss2.Bucket(auth, '<Endpoint>', '<BucketName>')

rule = NotificationRule(
    rule_id='example-rule',
    events=['ObjectCreated:PutObject'],
    prefix='images/',
    suffix='.jpg',
    topic_list=['acs:mns:<region>:<account-id>:/topics/<topic-name>']
)

notification = BucketNotification([rule])
bucket.put_bucket_notification(notification)
```

## Important Notes

- You can configure **up to 10 event notification rules** per bucket.
- Prefix and suffix filters cannot overlap across rules for the same event type.
- Event notifications are **near real-time** but not guaranteed to be instantaneous.
- Ensure the target MNS queue/topic or Function Compute function exists and has the correct permissions.
- MNS is now referred to as **Lightweight Message Queue (SMQ)** in newer documentation.
