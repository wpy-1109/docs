# ossutil 2.0 Command Reference

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/

## Command Structure

```bash
ossutil command [argument] [flags]
ossutil command subcommand [argument] [flags]
```

---

## cp - Upload, Download, and Copy Objects

The `cp` command is the unified, high-level utility for transferring objects between local filesystem and OSS, or between OSS locations.

### Basic Syntax

```bash
ossutil cp <source> <destination> [flags]
```

### Three Core Operations

#### Upload (Local to OSS)
```bash
# Upload a single file
ossutil cp localfile oss://bucket/path/

# Upload a directory recursively
ossutil cp -r localdir/ oss://bucket/path/
```

#### Download (OSS to Local)
```bash
# Download a single object
ossutil cp oss://bucket/path/object localfile

# Download objects recursively
ossutil cp -r oss://bucket/path/ localdir/
```

#### Copy (OSS to OSS)
```bash
# Copy a single object
ossutil cp oss://src-bucket/object oss://dest-bucket/object

# Copy objects recursively
ossutil cp -r oss://src-bucket/path/ oss://dest-bucket/path/
```

### General Options

| Flag | Description |
|------|-------------|
| `-r, --recursive` | Recursively copy files/objects (required for directories) |
| `-f, --force` | Force overwrite without confirmation |
| `-u, --update` | Only copy when source is newer than destination |
| `--only-current-dir` | Only copy files in the current directory |
| `--include <pattern>` | Include files matching a pattern (e.g., `*.jpg`) |
| `--exclude <pattern>` | Exclude files matching a pattern |
| `--disable-ignore-error` | Abort on any error instead of continuing |
| `--start-time` | Only transfer objects modified after this time |
| `--end-time` | Only transfer objects modified before this time |
| `--dry-run` | Simulate the operation without transferring |

### Multipart Upload/Download Options

| Flag | Description |
|------|-------------|
| `--part-size <size>` | Part size for multipart upload/download (e.g., `10485760` for 10MB) |
| `--parallel <num>` | Number of concurrent parts in parallel |
| `--multipart-threshold <size>` | File size threshold for multipart upload |
| `--disable-multipart` | Disable multipart upload entirely |

### Resumable Transfer Options

| Flag | Description |
|------|-------------|
| `--checkpoint-dir <dir>` | Directory for checkpoint files |
| `--enable-resume-upload` | Enable resumable upload |
| `--enable-resume-download` | Enable resumable download |
| `--disable-resume` | Disable resumable transfer |

### Performance / Concurrency

| Flag | Description |
|------|-------------|
| `--jobs <num>` | Number of concurrent file-level transfer tasks |
| `--parallel <num>` | Number of concurrent parts per file |
| `--bandwidth-limit <KB/s>` | Limit transfer bandwidth |

### Metadata & Storage Options

| Flag | Description |
|------|-------------|
| `--meta <key:value>` | Set user-defined metadata |
| `--content-type <type>` | Set Content-Type header |
| `--cache-control <value>` | Set Cache-Control header |
| `--content-disposition <value>` | Set Content-Disposition header |
| `--content-encoding <value>` | Set Content-Encoding header |
| `--content-language <value>` | Set Content-Language header |
| `--expires <value>` | Set Expires header |
| `--storage-class <class>` | Set storage class (Standard, IA, Archive, ColdArchive, DeepColdArchive) |
| `--acl <acl>` | Set object ACL (private, public-read, public-read-write) |
| `--tagging <key=value>` | Set object tags |

### Encryption Options

| Flag | Description |
|------|-------------|
| `--encryption` | Enable server-side encryption |
| `--sse-algorithm <alg>` | SSE algorithm (AES256, KMS, SM4) |
| `--sse-kms-key-id <id>` | KMS key ID for SSE-KMS |
| `--sse-data-encryption <alg>` | Data encryption algorithm |

### Other cp Options

| Flag | Description |
|------|-------------|
| `--version-id <id>` | Specify object version (versioned buckets) |
| `--payer <requester>` | Set request payer |
| `--disable-crc` | Disable CRC64 integrity check |
| `--disable-all-symlink` | Do not follow symbolic links |
| `--snapshot-path <path>` | Path for incremental upload snapshots |
| `--output-dir <dir>` | Directory for output reports |

### cp Examples

```bash
# Upload a single file
ossutil cp /local/file.txt oss://mybucket/file.txt

# Upload a directory recursively
ossutil cp /local/dir/ oss://mybucket/dir/ -r

# Download with resumable transfer
ossutil cp oss://mybucket/largefile.zip /local/ --enable-resume-download

# Multipart upload with 100MB part size
ossutil cp /local/bigfile.tar oss://mybucket/bigfile.tar --part-size 104857600

# Copy between buckets with storage class change
ossutil cp oss://srcbucket/obj oss://destbucket/obj --storage-class IA

# Upload only .jpg files, skip existing
ossutil cp /photos/ oss://mybucket/photos/ -r -u --include "*.jpg"

# Bandwidth-limited upload
ossutil cp /data/ oss://mybucket/data/ -r --bandwidth-limit 10240
```

---

## ls - List Buckets or Objects

### Syntax
```bash
ossutil ls [oss://bucket[/prefix]] [flags]
```

### Examples
```bash
# List all buckets
ossutil ls oss://

# List objects in a bucket
ossutil ls oss://bucket-name

# List objects with a prefix
ossutil ls oss://bucket-name/prefix

# List with details
ossutil ls oss://bucket-name --all
```

### Common Flags
| Flag | Description |
|------|-------------|
| `--prefix` | Filter by prefix |
| `--marker` | Pagination marker |
| `--limit` | Limit number of results |
| `--all` | Show detailed information |
| `--directory` | List directories only |
| `-r, --recursive` | List recursively |

---

## rm - Remove/Delete Objects

### Syntax
```bash
ossutil rm oss://bucket/object [flags]
```

### Examples
```bash
# Delete a single object
ossutil rm oss://bucket-name/object-key

# Recursively delete all objects with a prefix
ossutil rm oss://bucket-name/prefix -r

# Delete incomplete multipart uploads
ossutil rm oss://bucket-name -m -r

# Force delete
ossutil rm oss://bucket-name/object-key -f
```

### Common Flags
| Flag | Description |
|------|-------------|
| `-r, --recursive` | Delete recursively |
| `-f, --force` | Force delete without confirmation |
| `-m` | Delete multipart uploads |
| `--include` | Include pattern |
| `--exclude` | Exclude pattern |
| `--version-id` | Delete specific version |

---

## mb - Create Bucket

### Syntax
```bash
ossutil mb oss://bucket-name [flags]
```

### Examples
```bash
# Create a bucket
ossutil mb oss://new-bucket-name

# Create with specific storage class and ACL
ossutil mb oss://new-bucket-name --storage-class IA --acl private

# Create in a specific region
ossutil mb oss://new-bucket-name --region cn-hangzhou
```

### Common Flags
| Flag | Description |
|------|-------------|
| `--storage-class` | Storage class (Standard, IA, Archive) |
| `--acl` | Access control (private, public-read, public-read-write) |
| `--region` | Region for the bucket |
| `--redundancy-type` | Redundancy type (LRS, ZRS) |

---

## rb - Delete Bucket

### Syntax
```bash
ossutil rb oss://bucket-name [flags]
```

### Examples
```bash
# Delete an empty bucket
ossutil rb oss://bucket-name

# Force delete bucket and all contents
ossutil rb oss://bucket-name -f
```

### Common Flags
| Flag | Description |
|------|-------------|
| `-f, --force` | Force delete (removes all objects and the bucket) |

---

## stat - Display Bucket/Object Information

### Syntax
```bash
ossutil stat oss://bucket[/object] [flags]
```

### Examples
```bash
# Get bucket information
ossutil stat oss://bucket-name

# Get object metadata
ossutil stat oss://bucket-name/object-key

# Human-readable output
ossutil stat oss://bucket-name --human-readable
```

Returns: creation date, location, storage class, ACL, ETag, Content-Type, size, last modified, etc.

---

## sync - Synchronize Files/Objects

### Syntax
```bash
ossutil sync <source> <destination> [flags]
```

### Examples
```bash
# Sync local directory to OSS
ossutil sync /local/path oss://bucket-name/prefix

# Sync OSS to local
ossutil sync oss://bucket-name/prefix /local/path

# Sync between OSS locations
ossutil sync oss://source-bucket/prefix oss://dest-bucket/prefix

# Sync with delete (remove destination files not in source)
ossutil sync /local/path oss://bucket-name/prefix --delete

# Dry run
ossutil sync /local/path oss://bucket-name/prefix --dry-run
```

### Common Flags
| Flag | Description |
|------|-------------|
| `--delete` | Remove files at destination not in source |
| `--force` | Force without confirmation |
| `--dry-run` | Preview without executing |
| `--include` | Include pattern |
| `--exclude` | Exclude pattern |
| `--jobs` | Concurrent tasks |
| `--parallel` | Parallel parts |

---

## du - Display Storage Usage

### Syntax
```bash
ossutil du oss://bucket[/prefix] [flags]
```

### Examples
```bash
# Show bucket storage usage
ossutil du oss://bucket-name

# Show usage for prefix
ossutil du oss://bucket-name/path/

# Include all versions
ossutil du oss://bucket-name --all-versions

# Human-readable output
ossutil du oss://bucket-name --human-readable
```

---

## presign - Generate Pre-signed URL

### Syntax
```bash
ossutil presign oss://bucket/object [flags]
```

### Examples
```bash
# Generate download URL (default GET, expires in 3600s)
ossutil presign oss://bucket/object

# Generate with custom expiration (7200 seconds)
ossutil presign oss://bucket/object --expires 7200

# Generate upload URL (PUT method)
ossutil presign oss://bucket/object --method PUT
```

### Common Flags
| Flag | Description |
|------|-------------|
| `--expires` | Expiration time in seconds |
| `--method` | HTTP method (GET, PUT) |

---

## set-props - Set Object Properties

### Syntax
```bash
ossutil set-props oss://bucket/object [headers] [flags]
```

### Examples
```bash
# Set content type
ossutil set-props oss://bucket/object --content-type "text/html"

# Set cache control
ossutil set-props oss://bucket/object --cache-control "max-age=3600"

# Set custom metadata
ossutil set-props oss://bucket/object --meta "user=jack,email=test@example.com"

# Recursively set properties
ossutil set-props oss://bucket/prefix -r --content-type "image/jpeg" --include "*.jpg"
```

---

## restore - Restore Archived Objects

### Syntax
```bash
ossutil restore oss://bucket/object [flags]
```

### Examples
```bash
# Restore an archived object
ossutil restore oss://bucket/archived-object

# Restore objects recursively
ossutil restore oss://bucket/prefix -r
```

Note: Restoration time varies by storage tier (minutes for Archive, hours for Cold Archive).

---

## append - Append Upload

### Syntax
```bash
ossutil append localfile oss://bucket/object [flags]
```

### Examples
```bash
# Append content to an appendable object
ossutil append localfile.txt oss://bucket/appendable-object
```

Note: Objects created via append upload are of "Appendable" type.

---

## mkdir - Create Directory

### Syntax
```bash
ossutil mkdir oss://bucket/dirname/
```

### Examples
```bash
# Create a directory
ossutil mkdir oss://bucket/my-folder/
```

Note: Creates a zero-byte object ending with `/` since OSS uses a flat namespace.

---

## cat - Output Object Content

### Syntax
```bash
ossutil cat oss://bucket/object [flags]
```

### Examples
```bash
# Display object content
ossutil cat oss://bucket/config.json

# Anonymous access
ossutil cat oss://bucket/public-object --mode Anonymous
```

---

## hash - Calculate Hash Value

### Syntax
```bash
ossutil hash <file-or-object> [flags]
```

### Examples
```bash
# Calculate hash of local file
ossutil hash localfile.txt --type md5

# Calculate CRC64
ossutil hash localfile.txt --type crc64

# Calculate hash of OSS object
ossutil hash oss://bucket/object
```

---

## revert - Restore Object Version

### Syntax
```bash
ossutil revert oss://bucket[/prefix] [flags]
```

### Examples
```bash
# Revert a deleted object
ossutil revert oss://bucket/deleted-object

# Revert recursively
ossutil revert oss://bucket/prefix -r
```

Note: Requires versioning to be enabled on the bucket.

---

## config - Manage Configuration

### Syntax
```bash
ossutil config [flags]
```

Launches interactive configuration wizard to set up credentials and region.

---

## update - Update ossutil

### Syntax
```bash
ossutil update [flags]
```

Updates ossutil to the latest version.

---

## version - Display Version

### Syntax
```bash
ossutil version
```

---

## probe - Diagnostic Probing

### Syntax
```bash
ossutil probe [flags]
```

Probes network connectivity and configuration.

---

## Filter Options

ossutil supports filtering for batch operations:

| Filter | Description |
|--------|-------------|
| `--include <pattern>` | Include files matching pattern |
| `--exclude <pattern>` | Exclude files matching pattern |
| `--min-size <size>` | Minimum file size |
| `--max-size <size>` | Maximum file size |
| `--min-mtime <time>` | Minimum modification time |
| `--max-mtime <time>` | Maximum modification time |
| `--min-age <duration>` | Minimum age of file |
| `--max-age <duration>` | Maximum age of file |

### Filter Examples

```bash
# Upload only .jpg files
ossutil cp /photos/ oss://bucket/photos/ -r --include "*.jpg"

# Exclude .tmp files
ossutil cp /data/ oss://bucket/data/ -r --exclude "*.tmp"

# Only files larger than 1MB
ossutil cp /data/ oss://bucket/data/ -r --min-size 1M

# Files modified in last 7 days
ossutil cp /data/ oss://bucket/data/ -r --max-age 7d
```
