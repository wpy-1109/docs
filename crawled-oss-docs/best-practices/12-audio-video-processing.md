# Audio and Video Processing Best Practices

Source: https://help.aliyun.com/zh/oss/use-cases/audio-and-video-transcoding
Source: https://help.aliyun.com/zh/oss/use-cases/short-videos

## Overview

OSS integrates with Alibaba Cloud media processing services to support various audio/video workflows including transcoding, streaming, and video-on-demand (VOD).

## Architecture Patterns

### Video-on-Demand (VOD) Architecture

```
Upload -> OSS Bucket -> MPS (Media Processing) -> OSS Output Bucket -> CDN -> Users
                                    |
                            Transcoding Jobs
                            (Format conversion,
                             resolution adaptation,
                             watermarking)
```

### Short Video Platform Architecture

```
Mobile App -> STS Direct Upload -> OSS
                                    |
                         Function Compute Trigger
                                    |
                         MPS Transcoding Pipeline
                                    |
                         Multiple Resolutions/Formats
                                    |
                              CDN Distribution
```

## Key Integration Points

### 1. OSS as Media Storage

- **Upload**: Use STS temporary credentials for client-side direct upload
- **Storage**: Choose appropriate storage class based on access patterns
  - Standard: Hot content (recently uploaded, trending)
  - IA: Older content with declining views
  - Archive: Historical content for compliance/archival

### 2. Media Processing Service (MPS) Integration

- Trigger transcoding jobs automatically when files are uploaded to OSS
- Support for multiple output formats: HLS, MP4, FLV, WebM
- Adaptive bitrate streaming for multiple device types
- Audio extraction and processing

### 3. HLS Streaming from OSS

Create HLS (HTTP Live Streaming) streams from video files stored in OSS:

```
# HLS output structure in OSS
video-bucket/
  output/
    playlist.m3u8          # Master playlist
    stream_720p.m3u8       # 720p variant playlist
    stream_480p.m3u8       # 480p variant playlist
    segment_720p_001.ts    # Video segments
    segment_720p_002.ts
    ...
```

### 4. CDN Acceleration for Media Delivery

- Enable Range back-to-origin for video seek support
- Configure appropriate cache TTLs (30+ days for media files)
- Use resource prefetch for planned releases
- Enable Gzip compression for playlists and metadata files

## Transcoding Best Practices

### Output Format Recommendations

| Platform | Recommended Format | Container | Codec |
|---|---|---|---|
| Web (desktop) | MP4 | MP4 | H.264 + AAC |
| Mobile (iOS) | HLS | M3U8+TS | H.264 + AAC |
| Mobile (Android) | HLS or MP4 | M3U8+TS or MP4 | H.264 + AAC |
| Smart TV | HLS | M3U8+TS | H.265 + AAC |

### Multi-Bitrate Output

| Quality | Resolution | Video Bitrate | Audio Bitrate |
|---|---|---|---|
| Low (mobile/3G) | 480p (854x480) | 500 kbps | 64 kbps |
| Medium (mobile/4G) | 720p (1280x720) | 1500 kbps | 128 kbps |
| High (desktop) | 1080p (1920x1080) | 3000 kbps | 192 kbps |
| Ultra (4K) | 2160p (3840x2160) | 8000 kbps | 256 kbps |

### Watermarking

Add watermarks during transcoding:
- Text watermarks: Brand name, timestamp
- Image watermarks: Company logo
- Dynamic watermarks: User-specific identifiers for piracy tracking

## Video Screenshot/Thumbnail Generation

Use OSS video frame capture to generate thumbnails:

```
GET /video.mp4?x-oss-process=video/snapshot,t_1000,f_jpg,w_800,h_600
```

Parameters:
- `t_<ms>`: Time position in milliseconds
- `f_<format>`: Output format (jpg, png)
- `w_<pixels>`: Width
- `h_<pixels>`: Height
- `m_fast`: Fast mode (less accurate but faster)

## Cost Optimization

- Use lifecycle rules to transition older media to IA/Archive storage
- Enable CDN to reduce OSS outbound traffic costs
- Use internal endpoints for transcoding workflows
- Delete intermediate files after processing
- Compress thumbnail images with appropriate quality settings

## Function Compute Integration

Automate media processing with event-driven triggers:

```python
# Function Compute trigger on OSS upload
def handler(event, context):
    evt = json.loads(event)
    bucket = evt['events'][0]['oss']['bucket']['name']
    object_key = evt['events'][0]['oss']['object']['key']

    if object_key.endswith(('.mp4', '.mov', '.avi')):
        # Submit transcoding job
        submit_transcoding_job(bucket, object_key)

    return 'OK'
```
