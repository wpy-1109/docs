# Compliance guide for using OSS SDKs

This guide is provided to help developers protect the personal information of users and prevent infringement upon the personal information rights of end users when using third-party SDKs. Developers who use Object Storage Service (OSS) SDKs can refer to this topic to check whether their configurations meet regulatory compliance requirements.

## 1. Example on how to disclose SDK privacy policies


App operators must clearly inform end users of the following information about OSS SDKs: the SDK name, business features, purpose of processing personal information, types of personal information collected, and link for privacy policies. App operators must formulate a separate privacy policy to inform users that they are using an OSS SDK. For example, app operators can include the following information in the Third-party Sharing List:


SDK name: OSS SDK


Business features: upload or download objects by using corresponding OSS services.


Types of personal information collected: system name, system version number, network connection method, mobile phone model, and build ID.

## 2. SDK initialization and timing for calling API operations


The first time users initialize an app, they must agree to the privacy policy before they can use the SDK. Users can call the corresponding API operations only when they use the features provided by the SDK. To prevent excessive or premature data collection, do not collect device information immediately after users agree to the privacy policy.

## 3. System permissions applied by OSS SDKs


The following table describes the system permissions for Android apps.


| Permission | Required | Purpose | Application timing |
| --- | --- | --- | --- |
| INTERNET | Yes | The permissions to access networks.If an SDK does not have the permissions, specific features are unavailable. | Before calling the API operation for collecting information. |
| WRITE_EXTERNAL_STORAGE | No (We recommend that you grant the permissions to an OSS SDK.) | The permissions to write data into logs and record files for multipart upload and download tasks. | Before calling the API operation for collecting information. |
| READ_EXTERNAL_STORAGE | Yes | The permissions to read data from files during data upload. | Before calling the API operation for collecting information. |


## 4. Appendix


OSS SDK for Android: [Android](https://www.alibabacloud.com/help/en/oss/developer-reference/introduction/)


OSS SDK for iOS: [iOS](https://www.alibabacloud.com/help/en/oss/developer-reference/preface-5/#DAS)


Security and compliance: [Compliance certifications](https://www.alibabacloud.com/help/en/oss/user-guide/compliance-certifications)

Thank you! We've received your  feedback.