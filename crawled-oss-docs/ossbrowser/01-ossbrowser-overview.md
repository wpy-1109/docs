# ossbrowser 2.0 (Preview)

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/ossbrowser-2-0-overview/

## Overview

ossbrowser is the official graphical user interface (GUI) management tool provided by Alibaba Cloud for Object Storage Service (OSS). It provides a visual, desktop-based way to manage OSS resources, similar to Windows Explorer for local files.

ossbrowser 2.0 is the latest version (currently in preview) with improved features and UI.

## Download

### Platform-specific Installers

| Platform | Architecture | Installer Type |
|----------|-------------|----------------|
| Windows | x86-64 | NSIS installer (.exe) |
| macOS | Universal | DMG installer (.dmg) |
| Linux | x86-64 | AppImage (.AppImage) |

Download from the official Alibaba Cloud OSS documentation portal.

## Installation

1. Download the appropriate installer for your operating system
2. Run the installer and follow on-screen prompts
3. On first launch, configure your access credentials

## Key Features

| Feature | Description |
|---------|-------------|
| **Bucket Management** | Create, delete, and configure OSS buckets |
| **File Upload/Download** | Drag-and-drop support, batch operations, resumable transfers |
| **File Preview** | Preview images, text files, and other supported formats directly |
| **Access Control** | Supports RAM accounts, STS temporary tokens, and signed URLs |
| **Cross-Region Support** | Access buckets across different Alibaba Cloud regions |
| **Permission Management** | Set ACLs at bucket and object level |
| **Search & Filter** | Quickly locate files within buckets |
| **Logging & Monitoring** | View operation logs |
| **Resumable Transfer** | Resume interrupted uploads and downloads |
| **Directory-Like View** | Browse objects in a folder-style hierarchy |

## Login Methods

| Method | Description |
|--------|-------------|
| **AK Login** | Use AccessKey ID and AccessKey Secret for full account access |
| **STS Token Login** | Use temporary security credentials for scoped, time-limited access |
| **Preset OSS Path** | Restrict access to a specific bucket or directory path |

### AK Login

1. Launch ossbrowser
2. Select "AK Login" mode
3. Enter your AccessKey ID and AccessKey Secret
4. Optionally set a preset OSS path to restrict access scope
5. Select the region/endpoint
6. Click "Login"

### STS Token Login

1. Select "STS Token Login" mode
2. Enter the temporary AccessKey ID, AccessKey Secret, and Security Token
3. Set the preset OSS path
4. Click "Login"

This is ideal for granting limited-time access to sub-users.

## Preview Capabilities

ossbrowser 2.0 supports in-app preview for:

- **Images**: JPEG, PNG, GIF, BMP, WebP, etc.
- **Text files**: TXT, JSON, XML, CSV, etc.
- **Other media types**: Depending on format support

This eliminates the need to download files just to view their contents.

## Usage Guide

### Basic Workflow

1. **Login**: Enter your credentials (AccessKey or STS token)
2. **Navigate**: Browse your buckets and directories via the graphical interface
3. **Upload**: Drag and drop files or use the upload button
4. **Download**: Select files and download individually or in batches
5. **Manage**: Set permissions, generate shareable URLs, copy/move/delete objects
6. **Preview**: Click on supported files to preview without downloading

### Bucket Operations

- **Create Bucket**: Click "Create Bucket", set name, region, storage class, and ACL
- **Delete Bucket**: Right-click bucket, select "Delete" (bucket must be empty)
- **Configure Bucket**: Set CORS, lifecycle rules, logging, etc.

### Object Operations

- **Upload Files**: Drag files into the bucket view or click "Upload"
- **Download Files**: Select files, click "Download" or drag to local folder
- **Delete Files**: Select files, click "Delete"
- **Copy/Move**: Right-click objects to copy or move
- **Generate URL**: Right-click object, select "Generate URL" for sharing
- **Set Properties**: Modify Content-Type, metadata, ACL, storage class

### Batch Operations

- Select multiple files using Ctrl/Cmd+Click or Shift+Click
- Perform batch upload, download, delete, or property changes

## Limitations & Recommendations

- **Not recommended for large-scale data transfer**: For bulk/automated transfers, use ossutil (CLI) or OSS SDK
- **Not a server-side tool**: Desktop client only, not for server deployment
- **Performance**: Suitable for moderate workloads; for high-throughput, use API/SDK
- **File size**: Large file support through resumable transfer, but CLI tools are more reliable for very large files

## Comparison with Other OSS Tools

| Tool | Type | Best For |
|------|------|----------|
| **ossbrowser** | GUI (Desktop) | Visual management, occasional use, file preview |
| **ossutil** | CLI | Automation, scripting, large transfers |
| **OSS Console** | Web (Browser) | Quick config, bucket settings |
| **OSS SDK** | Programming Library | Application integration |
| **ossfs** | FUSE Filesystem | Mount OSS as local filesystem |
| **ossftp** | FTP Server | FTP-based access to OSS |

---

# ossbrowser 1.0

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/ossbrowser-1-0/

## Overview

ossbrowser 1.0 is the older version of the graphical management tool for OSS. While still available, users are encouraged to migrate to ossbrowser 2.0.

## Features

- Bucket management (create, delete, configure)
- Object upload/download with drag-and-drop
- ACL management
- Cross-region access
- STS token and AccessKey login
- Resumable transfer support
- Directory-style navigation
- Operation logging

## Login Configuration

### Using AccessKey Pair

1. Open ossbrowser
2. Enter Endpoint (select region)
3. Enter AccessKey ID
4. Enter AccessKey Secret
5. Optionally set Preset OSS Path
6. Click "Log On"

### Using STS Token

1. Select "STS Token" login mode
2. Enter AccessKey ID, AccessKey Secret, and SecurityToken
3. Set preset path
4. Click "Log On"

## Supported Operations

| Operation | Description |
|-----------|-------------|
| Create Bucket | Create new bucket with region, ACL, storage class |
| Delete Bucket | Delete empty bucket |
| Browse Objects | Navigate bucket contents |
| Upload | Upload files and folders |
| Download | Download files and folders |
| Delete | Delete objects |
| Copy | Copy objects within or across buckets |
| Move | Move objects |
| Rename | Rename objects |
| Preview | Preview supported file types |
| Generate URL | Create shareable signed URLs |
| Set ACL | Change object/bucket permissions |
| Fragment Management | Manage multipart upload fragments |
