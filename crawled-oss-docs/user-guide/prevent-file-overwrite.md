# Prevent file overwrites

To prevent files in an OSS bucket from being modified after their initial upload, you can set a prevent-overwrite rule. This rule lets you control which files cannot be overwritten based on their path, type, or user's identity.


-

Initial concurrent uploads: If a file is uploaded concurrently for the first time, which means multiple clients are uploading the same file at the same time, the system allows one of the versions to be written successfully, even if the upload matches a prevent-overwrite rule. This ensures a high success rate for writes in high-concurrency scenarios. However, after the file is successfully created, the rule blocks any subsequent overwrite operations.

-

Internal system behaviors are not blocked: The prevent-overwrite feature applies only to client-initiated operations, such as PutObject and AppendObject. The rule does not block background behaviors initiated by the OSS system, such as lifecycle transformations or cross-region replication (CRR). This ensures that these core features function correctly.

-

VersioningIncompatibility: The prevent-overwrite rule does not take effect when a bucket's versioning state is enabled or suspended.

## How it works


When OSS receives a request to overwrite a file, the system evaluates it against the configured protection rules:


-

Rule matching: The system checks the rules in the order they were created. It verifies whether the requested file path matches the prefix and suffix conditions of a rule and whether the user's identity matches the authorized user setting.

-

Decision execution: The prevent-overwrite operation is triggered only if all filter conditions (prefix and suffix) and the user's identity are met. If triggered, the system returns a `FileAlreadyExists` error.

-

Default behavior: If the request does not match any protection rules, the file overwrite operation is allowed.

## Protect specific file types


You can protect configuration files and log files in a production environment from being accidentally overwritten by specific users.


-

On the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket.

-

In the navigation pane on the left, choose Data Management > File overwrite prohibited.

-

Click New rule added to prohibit overwrite writes and configure the following parameters:


-

Rule ID: Enter an ID or have one generated automatically.

-

File name prefix: Enter the path of the folder to protect, such as `production/configs/`.

-

File name extension: Enter the file name extension, such as `.json`.

-

Authorized User: Specify the RAM users, roles, or other accounts that are restricted by this rule.

-

Click OK to create the rule.

-

Verify that the rule works:


-

Use a restricted account to try to upload a file with the same name to `production/configs/app.json`.

-

Confirm that a `FileAlreadyExists` error is returned.

-

Confirm that other users can upload files normally and that uploads to paths that do not match the prefix and suffix conditions proceed as normal.

## Set a global protection policy


You can establish comprehensive protection for critical business data to prevent accidental operations by any user.


-

On the [Buckets](https://oss.console.alibabacloud.com/bucket) page, click the name of the target bucket.

-

In the navigation pane on the left, choose Data Management > File overwrite prohibited.

-

Click New rule added to prohibit overwrite writes and configure the following parameters:


-

Rule ID: Enter an ID or have one generated automatically.

-

File name prefix: `critical-data/`

-

File name extension: Leave this parameter empty to protect all files in the specified path.

-

Authorized User: All accounts (*)

-

Click OK to create the rule.

-

Verify that the global protection works:


-

Use any account to try to overwrite `critical-data/database.sql`.

-

Confirm that a `FileAlreadyExists` error is returned. This indicates that global protection is active.

-

Confirm that files uploaded to the `public-data/` path can be overwritten normally.

## Matching rules


-

Number of rules: A single bucket supports a maximum of 100 rules.

-

Character length: The maximum length for both the prefix and suffix is 1,023 characters.

-

Prefix and suffix matching: Only exact string matching is supported. Regular expressions and wildcard characters are not supported. An input such as `logs/` is treated as a literal string.

-

Prefix matching: `logs/` matches `logs/app.log` but does not match `dev-logs/app.log`.

-

Suffix matching: `.txt` matches `readme.txt` but does not match `readme.TXT` or `readme.txt.bak`.

-

Authorized user matching: The asterisk (*) wildcard character is supported. For more information, see the Principal configuration described in [Common examples of bucket policies](https://www.alibabacloud.com/help/en/oss/user-guide/common-examples-of-bucket-policy).

-

Condition combination: The prevent-overwrite operation is triggered only if all filter conditions in the rule (prefix, suffix, and authorized user) are met.

-

Rule ID: This parameter is optional. If you leave it empty, a universally unique identifier (UUID) is automatically generated. If you enter an ID, it must be unique within the bucket.

## FAQ

#### After I set Authorized Users to empty, even I, the bucket owner, cannot overwrite files. What should I do?


This is expected behavior. If the Authorized Users field is empty, the rule applies to all users, including the bucket owner and the Alibaba Cloud account. To restore the ability to overwrite files, you can perform one of the following operations:


-

Delete the rule in the console.

-

Modify the rule's prefix or suffix conditions to narrow the scope of protection.

-

Set Authorized Users to specific users to ensure that the overwrite restriction applies only to those users.

#### I set the prefix to `logs/*.txt` to match all .txt files in the logs folder, but it does not work. Why?


OSS prefix and suffix matching does not support wildcard characters. The asterisk (`*`) is treated as a literal character. The system attempts to match a file with the exact name `logs/*.txt`. The correct configuration is as follows:


-

Set the prefix to `logs/`.

-

Set the suffix to `.txt`.


This configuration matches all files in the `logs/` folder that end with `.txt`.

#### What happens if I leave both the prefix and suffix empty?


If you leave both the prefix and suffix empty, the rule applies to the entire bucket. This has the following implications:


-

If Authorized Users is also left empty, all users are prohibited from overwriting any file in the bucket.

-

If Authorized Users specifies certain users, only those users are prohibited from overwriting files in the bucket.

Thank you! We've received your  feedback.