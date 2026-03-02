# ossutil 2.0 Overview

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/ossutil-overview/

ossutil 2.0 simplifies the management of Object Storage Service (OSS) across different operating systems, allowing for fast file uploads, downloads, synchronization, and management. It's perfect for developers, operations engineers, and businesses handling large-scale data migrations and daily operations.

## Download Links

| Operating system | System architecture | Download link | SHA256 checksum |
|---|---|---|---|
| Linux | x86_32 | ossutil-2.2.0-linux-386 | d5647923a96b32d6466258f0c24def271d8309d6914a8d09007fa71b7c9df7c5 |
| Linux | x86_64 | ossutil-2.2.0-linux-amd64 | 9e02837d806cfe976ae6c1fc22557d8e0a394ca6d298b45fb9f48a360d3a67f4 |
| Linux | arm32 | ossutil-2.2.0-linux-arm | 5660734e98c7d0da213aa1daca3656c238e97dd607084b9ea94134ff7c8cbf42 |
| Linux | arm64 | ossutil-2.2.0-linux-arm64 | 4f76dfd71d2af8265fcb9309b530f4671242cf5993a8fd0f0e089de7e9665f72 |
| macOS | x86_64 | ossutil-2.2.0-mac-amd64 | 6b5fd4902683817e6b419db9ee4b1cb825142e4b95ee603f8aa8e373a69e6bfa |
| macOS | arm64 | ossutil-2.2.0-mac-arm64 | dc5b73cde2da84c0e2a13935e63bf419a029fac739cfd6febff9a3ad46af22c3 |
| Windows | x86_32 | ossutil-2.2.0-windows-386 | 40b8950857ad3a37d979dcabcfd740660f8443ed6703962867c2c802586bf4c2 |
| Windows | x86_64 | ossutil-2.2.0-windows-amd64 | c6ea0e1444aa1aea5e846d0153fc8cca8d46ef3f453dd6fa61442f360474885b |
| Windows | amd64 | ossutil-2.2.0-windows-amd64-go1.20 | f5984cfc277cc004e9d310147feba652e30c7e0dd15cd3eb0c2651e2f1d3a1e3 |

## Quick Integration

### Install ossutil

#### Linux

1. Install the unzip tool:

**Alibaba Cloud Linux / CentOS:**
```bash
sudo yum install -y unzip
```

**Ubuntu:**
```bash
sudo apt install -y unzip
```

2. Download the package (Linux x86_64 example):
```bash
curl -o ossutil-2.2.0-linux-amd64.zip https://gosspublic.alicdn.com/ossutil/v2/2.2.0/ossutil-2.2.0-linux-amd64.zip
```

3. Unzip the package:
```bash
unzip ossutil-2.2.0-linux-amd64.zip
```

4. Change to the directory:
```bash
cd ossutil-2.2.0-linux-amd64
```

5. Set permissions:
```bash
chmod 755 ossutil
```

6. Make globally available:
```bash
sudo mv ossutil /usr/local/bin/ && sudo ln -s /usr/local/bin/ossutil /usr/bin/ossutil
```

7. Verify installation:
```bash
ossutil
```

#### Windows

Download the Windows package, extract it, and run `ossutil.exe` from the command prompt or PowerShell.

#### macOS

Download the macOS package, extract it, set permissions with `chmod 755 ossutil`, and move to `/usr/local/bin/`.

### Configure ossutil

Use the configuration wizard:

```bash
ossutil config
```

Follow the prompts:
1. Set the path for the configuration file (default: `/root/.ossutilconfig`)
2. Enter your AccessKey ID
3. Enter your AccessKey Secret
4. Enter the region ID (e.g., `ap-southeast-1`)
5. Optionally enter a custom endpoint

| Parameter | Required | Description |
|---|---|---|
| accessKeyID | Yes | The AccessKey pair for your account |
| accessKeySecret | Yes | The AccessKey secret |
| Region | Yes | The ID of the region where the bucket is located |
| endpoint | No | The endpoint of the region. If not set, the public endpoint corresponding to the Region is used |

> **Important:** Starting March 20, 2025, new OSS users must use a custom domain name (CNAME) to perform data API operations on OSS buckets in Chinese mainland regions.

### Run Commands (Quick Examples)

**Create a bucket:**
```bash
ossutil mb oss://examplebucket
```

**Upload a file:**
```bash
echo 'Hello, OSS!' > uploadFile.txt
ossutil cp uploadFile.txt oss://examplebucket
```

**Download a file:**
```bash
ossutil cp oss://examplebucket/uploadFile.txt localfolder/
```

**List files:**
```bash
ossutil ls oss://examplebucket
```

**Delete a file:**
```bash
ossutil rm oss://examplebucket/uploadFile.txt
```

**Delete a bucket:**
```bash
ossutil rb oss://examplebucket
```

## Configuration Guide

### Configuration Precedence

Command-line options > Environment variables > Configuration file (~/.ossutilconfig)

> **Note:** Starting from version 2.2.0, you can use the `--ignore-env-var` command-line option to ignore environment variables prefixed with `OSS_`.

### Configuration File

Default path: `~/.ossutilconfig`. Uses INI format with sections and key-value pairs.

```ini
[default]
accessKeyID = "your-access-key-id"
accessKeySecret = "your-access-key-secret"
region = ap-southeast-1
```

#### Configuration File Format Rules

- Section names and keys are not case-sensitive
- Keys support multiple formats: camelCase, kebab-case, snake_case, all lowercase
- Lines starting with `#` are comments

#### Supported Section Types

| Section name | Description |
|---|---|
| `[default]` | Default settings (used when `--profile` not set) |
| `[profile name]` | Named profile referenced via `--profile name` |
| `[buckets name]` | Endpoint configuration for specific buckets |

### Access Credential Parameters

| Parameter | Alias | Description |
|---|---|---|
| mode | / | Authentication mode: AK, StsToken, RamRoleArn, EcsRamRole, Anonymous |
| access-key-id | accessKeyId, access_key_id | AccessKey ID |
| access-key-secret | accessKeySecret, access_key_secret | AccessKey Secret |
| sts-token | stsToken, sts_token | STS token |
| role-arn | roleArn, role_arn | ARN of the RAM role |
| role-session-name | roleSessionName, role_session_name | Session name |
| ecs-role-name | ecsRoleName, ecs_role_name | ECS role name |
| credential-process | credentialProcess, credential_process | External command |
| credential-uri | credentialUri, credential_uri | URI for credentials |
| oidc-provider-arn | oidcProviderArn, oidc_provider_arn | OIDC provider ARN |
| oidc-token-file-path | oidcTokenFilePath, oidc_token_file_path | OIDC token file path |
| credential-process-timeout | credentialProcessTimeout | Timeout for external credentials (default: 15s, max: 600s) |

### Global Parameters

| Parameter | Description | Default |
|---|---|---|
| region | Region ID (required) | - |
| loglevel | Log level: off, info, debug | off |
| read-timeout | Read/write timeout (seconds) | 20 |
| connect-timeout | Connection timeout (seconds) | 10 |
| retry-times | Retry count on error | 10 |
| skip-verify-cert | Skip certificate verification | false |
| sign-version | Signature version: v1, v4 | v4 |
| output-format | Output format: raw, json, xml, yaml | raw |
| addressing-style | Request address format: virtual, path, cname | virtual |
| language | Display language | - |
| endpoint | Public endpoint (optional) | - |

### Environment Variables

| Environment variable | Corresponding parameter |
|---|---|
| OSS_ACCESS_KEY_ID | access-key-id |
| OSS_ACCESS_KEY_SECRET | access-key-secret |
| OSS_SESSION_TOKEN | sts-token |
| OSS_ROLE_ARN | ram-role-arn |
| OSS_ROLE_SESSION_NAME | role-session-name |
| OSS_REGION | region |
| OSS_ENDPOINT | endpoint |
| OSSUTIL_CONFIG_FILE | config-file |
| OSSUTIL_PROFILE | profile |

#### Linux Example:
```bash
echo "export OSS_ACCESS_KEY_ID='your-access-key-id'" >> ~/.bashrc
echo "export OSS_ACCESS_KEY_SECRET='your-access-key-secret'" >> ~/.bashrc
source ~/.bashrc
```

### Access Credential Configuration Methods

#### Use the AccessKey pair of a RAM user

```ini
[default]
accessKeyID = yourAccessKeyID
accessKeySecret = yourAccessKeySecret
region=ap-southeast-1
```

#### Use an STS token

```ini
[default]
accessKeyID = yourSTSAccessKeyID
accessKeySecret = yourSTSAccessKeySecret
stsToken = yourSecurityToken
region=ap-southeast-1
```

#### Use a RAMRoleARN

```ini
[default]
accessKeyID = yourAccessKeyID
accessKeySecret = yourAccessKeySecret
mode = RamRoleArn
roleArn = acs:ram::137918634953****:role/Alice
roleSessionName = session_name_example
region=ap-southeast-1
```

#### Use an EcsRamRole

```ini
[default]
mode = EcsRamRole
ecsRoleName = EcsRamRoleOss
region=ap-southeast-1
```

#### Use an OIDCRoleARN

```ini
[default]
mode = oidcRoleArn
OIDCProviderArn=acs:ram::113511544585****:oidc-provider/TestOidcProvider
OIDCTokenFilePath=OIDCTokenFilePath
roleArn=acs:ram::113511544585****:role/testoidc
roleSessionName=TestOidcAssumedRoleSession
region=ap-southeast-1
```

#### Obtain credentials from an external process

```ini
[default]
mode = Process
credentialProcess = user-cmd
region=ap-southeast-1
```

External command return format (long-term credentials):
```json
{
  "AccessKeyId": "ak",
  "AccessKeySecret": "sk"
}
```

External command return format (temporary credentials):
```json
{
  "AccessKeyId": "ak",
  "AccessKeySecret": "sk",
  "SecurityToken": "token",
  "Expiration": "2024-01-01T00:00:00Z"
}
```

#### Anonymous access

```bash
ossutil cat oss://bucket/public-object --mode Anonymous
```

## Command Reference

### Command Structure

```
ossutil command [argument] [flags]
ossutil command subcommand [argument] [flags]
ossutil topic
```

### High-Level Commands

| Command | Description |
|---|---|
| mb | Creates a bucket |
| rb | Deletes a bucket |
| du | Gets storage size of a bucket or prefix |
| stat | Displays bucket or object description |
| mkdir | Creates a directory object (name ends with /) |
| append | Appends content to appendable object |
| cat | Outputs object content to stdout |
| ls | Lists buckets or objects |
| cp | Uploads, downloads, or copies objects |
| rm | Deletes objects in a bucket |
| set-props | Sets object properties |
| presign | Generates a signed URL |
| restore | Restores frozen object to readable state |
| revert | Restores object to a specified version |
| sync | Synchronizes files/objects from source to destination |
| hash | Calculates hash value of file or object |

### API-Level Commands

| Command | Description |
|---|---|
| put-bucket-acl | Sets/modifies bucket access permissions |
| get-bucket-acl | Gets access permissions |
| put-bucket-cors | Sets CORS rules |
| get-bucket-cors | Gets CORS rules |
| delete-bucket-cors | Deletes CORS rules |

> Run `ossutil api -h` to view all API-level commands.

### Helper Commands

| Command | Description |
|---|---|
| help | Gets help information |
| config | Creates/manages configuration file |
| update | Updates version |
| version | Displays version information |
| probe | Probes commands |

## Command Option Types

| Option type | Format | Description | Example |
|---|---|---|---|
| String | --option string | String parameters | --acl private |
| Boolean | --option | Enables/disables option | --dry-run |
| Integer | --option Int | Unsigned integer | --read-timeout 10 |
| Timestamp | --option Time | ISO 8601 format | --max-mtime 2006-01-02T15:04:05 |
| Byte unit suffix | --option SizeSuffix | Default bytes; K, M, G, T, P, E suffixes | --min-size 1K |
| Time unit suffix | --option Duration | Default seconds; ms, s, m, h, d, w, M, y | --min-age 1.5d |
| String list | --option strings | Comma-separated or multiple options | --metadata user=jack,email=test |
| String array | --option stringArray | Multiple options, single values | --include *.jpg --include *.txt |

## Loading Data from Files

- `file://` prefix loads from a file path
- `-` loads from standard input

Example:
```bash
ossutil api put-bucket-cors --bucket examplebucket --cors-configuration file://cors-configuration.json
```

```bash
cat cors-configuration.json | ossutil api put-bucket-cors --bucket examplebucket --cors-configuration -
```

## Output Control

### Output Format

Use `--output-format` parameter:

| Format | Description |
|---|---|
| raw | Original format from server |
| json | JSON string format |
| yaml | YAML string format |
| xml | XML string format |

### Filter Output

Use `--output-query` with JMESPath syntax:
```bash
ossutil api get-bucket-cors --bucket bucketexample --output-query CORSRule.AllowedMethod --output-format json
```

### Human-Readable Display

Use `--human-readable` option:
```bash
ossutil stat oss://bucketexample --human-readable
```

## Command Return Codes

| Return code | Description |
|---|---|
| 0 | Command successful |
| 1 | Parameter error |
| 2 | Server returned error (non-2xx) |
| 3 | Non-server error (SDK error) |
| 4 | Partial failure in batch operation |
| 5 | Interrupted by Ctrl+C |

Check return code: `echo $?` (Linux/macOS) or `echo %ERRORLEVEL%` (Windows)

## Global Command-Line Options

| Parameter | Type | Description |
|---|---|---|
| -i, --access-key-id | string | AccessKey ID |
| -k, --access-key-secret | string | AccessKey Secret |
| --addressing-style | string | Request address format: virtual, path, cname |
| -c, --config-file | string | Configuration file path (default: ~/.ossutilconfig) |
| --connect-timeout | int | Connection timeout (seconds, default: 10) |
| -n, --dry-run | - | Dry run mode |
| -e, --endpoint | string | Public endpoint |
| -h, --help | - | Help information |
| --language | string | Display language |
| --loglevel | string | Log level: off, info, debug |
| --mode | string | Auth mode: AK, StsToken, EcsRamRole, Anonymous |
| --output-format | string | Output format (default: raw) |
| --output-query | string | JMESPath query |
| --profile | string | Profile in configuration file |
| -q, --quiet | - | Quiet mode |
| --read-timeout | int | Read/write timeout (seconds, default: 20) |
| --region | string | Region ID |
| --retry-times | int | Retry count (default: 10) |
| --sign-version | string | Signature version: v1, v4 (default) |
| --skip-verify-cert | - | Skip certificate verification |
| -t, --sts-token | string | STS token |
| --proxy | string | Proxy server (direct URL or "env") |
| --log-file | string | Log output file ("-" for stdout) |
| --cloudbox-id | string | CloudBox ID (since v2.1.0) |
| --ignore-env-var | - | Ignore OSS_ env vars (since v2.2.0) |
| --bind-address | string | Local IP for outbound connections (since v2.2.0) |
| --account-id | string | Account ID for vector buckets (since v2.2.0) |

## Common Command-Line Options

| Command scope | Supported options |
|---|---|
| All high-level commands | --encoding-type, --request-payer |
| Batch operations | --start-after/--end-with, filter options, --limited-num, --recursive/-r, --dirs/-d, --force/-f, --list-objects |
| Destination filtering | --update, --size-only, --checksum, --ignore-existing |
| Single object operations | --version-id |
| List mode | --list-format, --list-manifest-from |

## FAQ

### Error: "region must be set in sign version 4"

**Cause:** Region ID was not configured.

**Solution:** Make sure you configure AccessKey ID, AccessKey secret, and region ID. The region ID is required because the signature has been upgraded to V4.
