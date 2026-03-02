# Data consistency validation

OSS supports three validation methods: ETag, MD5, and CRC-64.











> NOTE:

> NOTE: 


> NOTE: 


> NOTE:

> NOTE: 


> NOTE: 

-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/can-i-use-etag-values-as-oss-md5-hashes-to-check-data-consistency)


> NOTE:

> NOTE: 


> NOTE: 


(https://www.alibabacloud.com/help/en/oss/user-guide/check-data-transmission-integrity-by-using-crc-64)


| Verification method | Application scenario | Description |
| --- | --- | --- |
| ETag | Check whether object content is changed. | An ETag is created upon object creation and identifies the content of the object. If an object is created using a PutObject request, the ETag of the object is the MD5 hash of the object content. If an object is created using other methods, the ETag is a unique value generated based on a specific algorithm. Note The ETag of an object can be used to check whether the object content changes. We recommend that you use the MD5 hash of an object rather than the ETag of the object to verify data integrity. |
| MD5 | Check data integrity. | To use MD5 for data integrity verification in an object upload, you calculate the MD5 hash of the object and provide the MD5 hash in the upload request using the Content-MD5 header. When OSS receives the object, OSS calculates the MD5 hash and compares the calculated MD5 hash with the Content-MD5 header value that you provided. The object can be uploaded only when the two MD5 hash values match. This way, data consistency is ensured. Note MD5 verification is supported for PutObject, GetObject, AppendObject, PostObject, Multipart upload, and UploadPart. The Content-MD5 header in a CompleteMultipartUpload request checks the integrity of the request body of CompleteMultipartUpload and cannot be used to check the integrity of the object. For more information about how to check data integrity using MD5, see Can I use ETag values as OSS MD5 hashes to check data consistency? |
| CRC-64 | Check data integrity. | You can use CRC-64 to check data integrity between the local data and the data uploaded to OSS. OSS returns a CRC-64 value of an object uploaded using any of the methods provided. The client compares the CRC-64 value with the CRC-64 value calculated on the local machine to verify data integrity. Note In a CompleteMultipartUpload request, if all parts have CRC-64 values, OSS returns the CRC-64 value of the object for data integrity verification. For more information about how to check data integrity using CRC-64, see Check data integrity using CRC-64. |


Thank you! We've received your  feedback.