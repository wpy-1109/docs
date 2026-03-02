# Authorization process

For security reasons, all Object Storage Service (OSS) resources (buckets and objects) are private by default. This means that only owners and authorized users have access to the resources. OSS allows you to use a variety of access control policies to grant other users specific permissions to access or use your OSS resources. A request is allowed only if all access control policies that apply to the request allow the request.

## Request types


Requests are divided into non-anonymous and anonymous requests.


-

Non-anonymous requests


Non-anonymous requests include signature information in the request headers or request URLs for authentication.

-

Anonymous requests


Anonymous requests do not include signature information in the request headers or request URLs.

## Authorize non-anonymous requests


Authorization description


When OSS receives a non-anonymous request, OSS determines whether to allow or deny the request based on the authentication result, role-based session policies, identity-based policies (RAM policies), bucket policies, object access control lists (ACLs), and bucket ACLs.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1649674471/CAEQMRiBgICElYnknhkiIDUyNmMwZmIxZTNjYzRjNWJiOTgwMzlkZGU0MWExMjEz3963382_20230830144006.372.svg)

The preceding figure shows the possible authorization results:


-

Allow: allows the request based on the applicable policy.

-

Explicit Deny: explicitly denies the request based on the applicable policy.

-

Implicit Deny: implicitly denies the request if OSS detects no applicable policies or no Allow or Deny hits.


Authorization process


OSS performs the following steps to authenticate and authorize a non-anonymous request:


-

OSS checks whether the request passes identity verification.


OSS compares the signature included in the request with the signature calculated by the OSS server.


-

If the signatures are inconsistent, the request is denied.

-

If the signatures are consistent, OSS checks whether the request remains to be checked based on role-based session policies.

-

OSS checks whether the request remains to be checked based on role-based session policies.


If the request remains to be checked based on role-based session policies, OSS checks the request against the session policies.


-

If the result is Explicit Deny or Implicit Deny, OSS denies the request.

-

If the result is Allow, OSS continues to check the request against RAM policies and bucket policies.


If the request requires no evaluation based on role-based session policies, OSS proceeds to check the request based on RAM policies and bucket policies.

-

OSS checks whether the request matches RAM policies and bucket policies.


RAM policies are identity-based access control policies. You can configure RAM policies to manage access to your resources in OSS. In an authorization check based on RAM policies, OSS determines whether to allow or deny the request based on the account that sends the request.


-

If the request is sent by using the AccessKey pair of an Alibaba Cloud account, OSS implicitly denies the request.

-

If the request is sent by using the AccessKey pair of a RAM user or Security Token Service (STS) credentials to access a bucket that does not belong to the Alibaba Cloud account or the owner of the RAM user, OSS implicitly denies the request.

-

OSS calls the authentication operation provided by RAM to authenticate requests. OSS supports authentication based on accounts and the resource groups of buckets. OSS determines whether to allow, explicitly deny, or implicitly deny the request based on the authentication result.


Bucket policies are resource-based authorization policies. The owner of a bucket can configure bucket policies to authorize RAM users or other Alibaba Cloud accounts to perform operations on the bucket or specific resources in the bucket.


-

If no bucket policy is configured for the bucket, OSS implicitly denies the request.

-

If bucket policies are configured for the bucket, OSS checks whether the request matches the bucket policies and then determines whether to allow, explicitly deny, or implicitly deny the request.

-

OSS checks whether the request matches an Explicit Deny based on the preceding check results.


If the request matches an Explicit Deny, OSS denies the request. If the request does not match an Explicit Deny, OSS checks whether the request matches an Allow.


-

OSS checks whether the request matches an Allow based on RAM policies and bucket policies.


If the request matches an Allow, OSS allows the request. If the request does not match an Allow, OSS checks the source of the request.

-

OSS checks the source of the request.


If the request is sent by calling a management API operation, OSS denies the request. If the request is sent by calling a data API operation, OSS checks the object ACL or bucket ACL.


Management API operations include service-related operations such as GetService (ListBuckets), bucket-related operations such as PutBucket and GetBucketLifecycle, and LiveChannel-related operations such as PutLiveChannel and DeleteLiveChannel.


Data API operations include object-related operations, such as PutObject and GetObject.

-

OSS checks the request based on the ACLs of the requested object and bucket.


When OSS checks the request based on the object ACL, OSS checks whether the requester is the bucket owner and whether the request is a read request or a write request. For more information, see [PutBucketAcl](https://www.alibabacloud.com/help/en/oss/developer-reference/putobjectacl#reference-fs3-gfw-wdb).


-

If the result is Allow, OSS allows the request.

-

If the result is Deny, OSS denies the request.


If the ACL of the object is inherited from the bucket, OSS checks the request based on the ACL of the bucket in which the object is stored.


When OSS checks the request based on the bucket ACL, OSS checks whether the requester is the bucket owner. For more information, see [PutBucketAcl](https://www.alibabacloud.com/help/en/oss/developer-reference/putbucketacl#reference-zzr-hk5-tdb).


-

If the result is Allow, OSS allows the request.

-

If the result is Deny, OSS denies the request.

## Authorize anonymous requests


Authorization description


OSS determines whether to allow or deny an anonymous request only based on the bucket policies, object ACL, and bucket ACL. OSS does not perform authorization checks on an anonymous request based on authentication, role-based session policies or RAM policies.
![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/1649674471/CAEQJBiBgMCRgd3G9hgiIDZkZDNkY2IwNDQ4MTRkZTJiMmUzY2M0NzU3MzljZmFi3963382_20230830144006.372.svg)

Authorization process


OSS uses the following steps to perform authorization checks on an anonymous request:


-

OSS evaluates bucket policies.


-

If the result is Deny, OSS denies the request.

-

If the result is Allow, OSS allows the request.

-

If the result is Ignore, OSS continues to check the ACL of the object.

-

OSS checks the request based on the ACLs of the requested object and bucket.


-

If the ACL of the object is private, the result is Deny and OSS denies the request.

-

If the ACL of the object is public-read or public-read-write, the result is Allow and OSS allows the request.

-

If the ACL of the object is inherited from the bucket, OSS checks the request based on the ACL of the bucket in which the object is stored.


-

If the ACL of the bucket is public-read or public-read-write, the result is Allow and OSS allows the request.

-

If the ACL of the bucket is private, the result is Deny and OSS denies the request.

Thank you! We've received your  feedback.