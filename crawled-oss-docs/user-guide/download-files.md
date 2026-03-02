# Download objects

You can download objects stored in OSS using a variety of methods, each tailored to different download needs.


OSS offers the following methods for downloading objects:


-

[Simple download](https://www.alibabacloud.com/help/en/oss/user-guide/simple-download-1): The GetObject operation is used to download objects via a single HTTP request. This approach is suitable for small objects or scenarios where high download speed is not required.

-

[Resumable download](https://www.alibabacloud.com/help/en/oss/user-guide/oss-resumable-download): This method is suitable for downloading large objects, especially in environments with unstable network connectivity. Resumable download splits a large object into smaller parts and downloads them concurrently. If the download is interrupted, the process resumes from the position that is recorded in the checkpoint file. This approach is suitable for scenarios with frequent network fluctuations.

-

[Download files using a signed URL](https://www.alibabacloud.com/help/en/oss/user-guide/how-to-obtain-the-url-of-a-single-object-or-the-urls-of-multiple-objects): You can use presigned URLs to grant temporary access to third parties for viewing or downloading objects without revealing your AccessKey pair. This method is appropriate for temporary authorization and facilitates secure sharing of objects.

-

[Conditional download](https://www.alibabacloud.com/help/en/oss/user-guide/conditional-download): You can conditionally download an object based on criteria such as its last modified timestamp or ETag. This prevents re-downloading unmodified content, reducing network traffic and resource consumption. This approach is applicable to use cases involving frequent object updates, where avoiding repeated downloads of unchanged content is desired.

Thank you! We've received your  feedback.