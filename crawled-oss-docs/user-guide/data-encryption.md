# what is OSS data encryption

Object Storage Service (OSS) provides server-side and client-side encryption. OSS also supports encrypted data transmission over HTTPS using SSL/TLS. These features protect your data in the cloud from potential security risks.

## Server-side encryption


OSS supports server-side encryption for data that you upload. When you upload data, OSS encrypts it before saving the encrypted data. When you download the data, OSS automatically decrypts it and returns the original data. The HTTP response header also indicates that the data was encrypted on the server.


OSS provides data-at-rest protection using server-side encryption. This method is suitable for scenarios that require high security or compliance for file storage, such as storing deep learning sample files or online collaborative documents. OSS provides the following two server-side encryption methods for different scenarios:


-

Use KMS-managed keys for encryption and decryption (SSE-KMS)


When you upload an object, you can use the default customer master key (CMK) managed by Key Management Service (KMS) or a specified CMK ID for encryption. This method is suitable for encrypting and decrypting large amounts of data. It is a low-cost encryption method because the data does not need to be sent over the network to the KMS server for encryption and decryption.


KMS is a secure and easy-to-use management service provided by Alibaba Cloud. You do not need to invest heavily in protecting the confidentiality, integrity, and availability of your keys. With KMS, you can use keys securely and conveniently, and focus on developing your encryption and decryption features. You can view and manage your KMS keys in the KMS console.


KMS uses the AES-256 encryption algorithm and envelope encryption to prevent unauthorized data access. KMS generates data encryption keys and uses your CMK to encrypt them. You can generate a CMK using the default KMS key managed by OSS or using the Bring-Your-Own-Key (BYOK) feature. The key material for BYOK can be provided by Alibaba Cloud or imported by you.


The following figure illustrates how SSE-KMS server-side encryption works.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/9135874671/CAEQMhiBgIC5g5mypBkiIGVlMDQ1YWUxMTUwNjRjMzJhNmFiOGU3MWRkYmQ4N2I43963382_20230830144006.372.svg)
-

Use OSS-managed encryption (SSE-OSS)


Server-side encryption that is fully managed by OSS (SSE-OSS) is an object attribute. SSE-OSS uses the industry-standard 256-bit Advanced Encryption Standard (AES-256) algorithm to encrypt each object. Each object is encrypted with a unique key. For added protection, a master key is used to encrypt these unique data keys. This method is suitable for the batch encryption and decryption of data.


With this encryption method, OSS is responsible for generating and managing data encryption keys. You can set the default server-side encryption method for a bucket to AES-256. You can also include the `X-OSS-server-side-encryption` header in your request and set its value to `AES256` when you upload an object or modify its metadata. This enables server-side encryption for the object.


For more information, see [Server-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/server-side-encryption-8#concept-lqm-fkd-5db).

## Client-side encryption


Client-side encryption is the process of encrypting objects locally before you upload them to Object Storage Service (OSS). When you use client-side encryption, you are responsible for the integrity and correctness of the master key. When you copy or migrate encrypted data, you are also responsible for the integrity and correctness of the encryption metadata.


When you use client-side encryption, a random data encryption key is generated for each object. This plaintext data key is used to symmetrically encrypt the object data. The master key is then used to encrypt the random data encryption key. The encrypted data key is saved as part of the object's metadata on the server. To decrypt the object, you must first use the master key to decrypt the encrypted data key. Then, you can use the resulting plaintext data key to decrypt the object data. The master key is used only for local calculations on the client. It is not transmitted over the network or stored on the server. This process ensures the security of the master key.


The following two methods are supported for managing master keys:


-

Use KMS-managed customer master keys


When you use a KMS-managed customer master key for client-side data encryption, you do not need to provide an encryption key to the OSS encryption client. You only need to specify the KMS customer master key ID (CMK ID) when you upload an object. The following figure illustrates this process.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0235874671/CAEQORiBgICErfLmqhkiIGM3NjhiYmU2MTBjNDQ5MjdiZTlhZmUyZjJiZjg1NGM03963382_20230830144006.372.svg)
-

Use customer-managed keys


When you use customer-managed keys, you must generate and store the encryption keys yourself. When the local client encrypts an object, you must provide an encryption key, which can be a symmetric or asymmetric key, to the local encryption client. The following figure illustrates the encryption process.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/0235874671/CAEQORiBgIDs0_TmqhkiIGRiZmEzYjA0ZDA1NDQ2OGJhNjA0YTM2NmI3NWIwMmMz3963382_20230830144006.372.svg)

For more information, see [Client-side encryption](https://www.alibabacloud.com/help/en/oss/user-guide/client-side-encryption#concept-2323737).

## Encrypted transmission over HTTPS using SSL/TLS


OSS supports access over HTTP or HTTPS. You can [set the TLS version](https://www.alibabacloud.com/help/en/oss/user-guide/set-tls-version) based on your business needs to improve data transmission security. Transport Layer Security (TLS) is a protocol that provides confidentiality and data integrity between two communicating applications. This protocol helps protect your data from security risks in the cloud.

Thank you! We've received your  feedback.