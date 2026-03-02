# Python SDK - Object Upload and Download

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/python-upload-download

## V1 SDK - Upload

### Upload a String

```python
bucket.put_object('example.txt', 'Hello OSS!')
```

### Upload a Local File

```python
bucket.put_object_from_file('example.txt', '/path/to/local/file.txt')
```

### Upload with Headers/Metadata

```python
headers = {
    'Content-Type': 'text/plain',
    'x-oss-object-acl': 'public-read',
    'x-oss-meta-author': 'example-user'
}
bucket.put_object('example.txt', 'content', headers=headers)
```

### Upload from Stream

```python
with open('/path/to/file.txt', 'rb') as f:
    bucket.put_object('example.txt', f)
```

## V1 SDK - Download

### Download to Memory

```python
result = bucket.get_object('example.txt')
content = result.read().decode('utf-8')
print(content)
```

### Download to Local File

```python
bucket.get_object_to_file('example.txt', '/path/to/local/file.txt')
```

### Range Download

```python
result = bucket.get_object('example.txt', byte_range=(0, 1023))
content = result.read()
```

### Conditional Download

```python
import datetime
result = bucket.get_object('example.txt',
    headers={'If-Modified-Since': 'Wed, 01 Jan 2025 00:00:00 GMT'})
```

## V2 SDK - Upload

### Upload from String

```python
result = client.put_object(oss.PutObjectRequest(
    bucket=bucket_name,
    key=object_name,
    body=b'Hello OSS V2!',
))
print(f'ETag: {result.etag}')
```

### Upload from File

```python
with open('/path/to/local/file.txt', 'rb') as f:
    result = client.put_object(oss.PutObjectRequest(
        bucket=bucket_name,
        key=object_name,
        body=f,
    ))
print(f'ETag: {result.etag}')
```

## V2 SDK - Download

```python
result = client.get_object(oss.GetObjectRequest(
    bucket=bucket_name,
    key=object_name,
))
content = result.body.read()
```

## List Objects

### V1

```python
# List all objects
for obj in oss2.ObjectIterator(bucket):
    print(f"Key: {obj.key}, Size: {obj.size}")

# List with prefix
for obj in oss2.ObjectIterator(bucket, prefix='photos/'):
    print(f"Key: {obj.key}")
```

## Delete Objects

### V1

```python
# Delete single object
bucket.delete_object('example.txt')

# Delete multiple objects
bucket.batch_delete_objects(['key1', 'key2', 'key3'])
```

## Copy Objects

```python
bucket.copy_object('source-bucket', 'source-key', 'dest-key')
```

## Object Metadata

### Get Object Metadata

```python
meta = bucket.get_object_meta('example.txt')
print(f"Content-Length: {meta.headers['Content-Length']}")
print(f"ETag: {meta.headers['ETag']}")

# Full metadata
head = bucket.head_object('example.txt')
print(f"Content-Type: {head.content_type}")
print(f"Last-Modified: {head.last_modified}")
```

### Set Object ACL

```python
bucket.put_object_acl('example.txt', oss2.OBJECT_ACL_PUBLIC_READ)

acl = bucket.get_object_acl('example.txt')
print(f"Object ACL: {acl.acl}")
```

## Symbolic Links

```python
# Create symlink
bucket.put_symlink('my-symlink', 'target-object')

# Get symlink target
result = bucket.get_symlink('my-symlink')
print(f"Target: {result.target_key}")
```
