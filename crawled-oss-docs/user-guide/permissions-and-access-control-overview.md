# Introduction to access control policies and scenarios

By default, Object Storage Service (OSS) resources, such as buckets and objects, are private to ensure data security. Only the resource owner or authorized users can access these resources. To allow third-party users to access your OSS resources, you can use various access control policies to grant specific permissions. OSS provides the following permission and access control features for objects stored in buckets:











(https://www.alibabacloud.com/help/en/oss/ram-policy-overview/#concept-y5r-5rm-2gb)


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-policy/)


-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/oss-bucket-acl#concept-fnt-4z1-5db)


(https://www.alibabacloud.com/help/en/oss/user-guide/object-acl#concept-blw-yqm-2gb)


(https://www.alibabacloud.com/help/en/oss/user-guide/block-public-access)


-


-


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/access-point/)


-


-


(https://www.alibabacloud.com/help/en/oss/user-guide/hotlink-protection)


(https://www.alibabacloud.com/help/en/oss/user-guide/cors-settings)


| Type | Description | Scenarios |
| --- | --- | --- |
| RAM Policy | Resource Access Management (RAM) is an access control service provided by Alibaba Cloud. A RAM policy is a user-based authorization policy. You can use RAM policies to centrally manage your users, such as employees, systems, or applications, and control their permissions to access your resources. For example, you can grant users read-only permissions for a specific bucket. | Grant OSS permissions to RAM users, user groups, or RAM roles within your Alibaba Cloud account. |
| Bucket Policy | A bucket policy is a resource-based authorization policy. Bucket policies are simpler to use than RAM policies, and you can configure them in the console through a graphical interface. Bucket owners can grant access directly without needing RAM permissions. Bucket policies support granting access permissions to RAM users from other accounts and to anonymous users with specific IP address restrictions. | Grant OSS permissions to RAM users or RAM roles within your account.Grant OSS permissions to RAM users or RAM roles from other accounts.Grant OSS permissions to anonymous users. |
| Bucket ACL | You can set an access control list (ACL) when you create a bucket. You can also modify the ACL at any time after the bucket is created. Only the bucket owner can perform this operation. Bucket ACLs include public-read-write, public-read, and private. | Set the same access permissions for all objects in a bucket. |
| Object ACL | In addition to bucket-level ACLs, OSS also provides object-level ACLs. You can set an ACL when you upload an object or modify the ACL at any time after the object is uploaded. Object ACLs include default (inherits from the bucket), public-read-write, public-read, and private. | Set access permissions for one or more individual objects. For example, you may have set the access permissions for all objects in a bucket or for objects that match a specific prefix to private using a RAM policy or bucket policy. To make a specific object accessible to all anonymous users on the Internet, you can use an object ACL and set the ACL to public-read. |
| Block Public Access | OSS supports public access through bucket policies and ACLs. Public access means that OSS resources can be accessed without requiring specific permissions or identity verification. Public access increases the risk of data breaches and high outbound traffic costs that result from malicious access. To avoid these risks, OSS lets you enable Block Public Access. When Block Public Access is enabled, existing public access permissions are ignored, and you cannot create new public access permissions. This feature closes public access channels and helps ensure data security. | Enabling Block Public Access at the global OSS level.Enabling Block Public Access for a single bucket.Enabling Block Public Access for a single access point.Enabling Block Public Access for a single object FC access point. |
| Access point | You can create multiple access points for a bucket and configure different access control permissions and network control policies for each access point. Using different access points for different business scenarios simplifies access management for large, shared datasets. | A customer manages dozens of app clients, and each client requires different access permissions to data in different folders within the same bucket.A customer stores all company data in a single bucket and needs to ensure that dozens or even hundreds of internal teams can access only specific folders or files. |
| Hotlink protection | Hotlink protection prevents unauthorized websites from directly linking to your OSS resources by verifying the source information of HTTP requests, such as the Referer and User-Agent headers. This helps prevent bandwidth theft and resource hotlinking. You can configure hotlink protection using whitelists, blacklists, or regular expressions. | Allow only specified domain names or applications to access a bucket or object to prevent third-party websites from hotlinking resources such as images and files. This feature is suitable for scenarios that require high bandwidth and resource protection, such as audio and video playback, image hosting, and software downloads. |
| Cross-origin resource sharing settings | Cross-origin resource sharing (CORS) lets you configure cross-domain access rules for your buckets. This allows web page scripts to securely access OSS resources from different origins. You can configure parameters such as allowed origins, methods, and headers. | This feature is used when frontend pages, such as web applications, H5 pages, or miniapps, or third-party services need to make cross-origin requests to access OSS resources from a different domain (origin). Typical scenarios include direct file uploads from the frontend and cross-domain loading for web-based audio and video playback. |


If a bucket has multiple access control policies, such as RAM policies, ACLs, and bucket policies, see [OSS authentication details](https://www.alibabacloud.com/help/en/oss/user-guide/authentication) for information about the authentication flow.

Thank you! We've received your  feedback.