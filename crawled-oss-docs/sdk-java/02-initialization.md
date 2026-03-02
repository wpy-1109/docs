# Java SDK Initialization

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/java-initialization

## V1 SDK - Creating an OSSClient

### Using AccessKey ID and Secret

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;

String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
String accessKeyId = "<yourAccessKeyId>";
String accessKeySecret = "<yourAccessKeySecret>";

// Create an OSSClient instance
OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);

// ... perform operations ...

// Shut down the client when done
ossClient.shutdown();
```

### Using Environment Variable Credentials Provider

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.common.auth.EnvironmentVariableCredentialsProvider;

// Ensure OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are set
EnvironmentVariableCredentialsProvider credentialsProvider =
    CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();

String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
OSS ossClient = new OSSClientBuilder().build(endpoint, credentialsProvider);
```

### Using STS Temporary Credentials

```java
String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
String accessKeyId = "<yourAccessKeyId>";
String accessKeySecret = "<yourAccessKeySecret>";
String securityToken = "<yourSecurityToken>";

OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret, securityToken);
```

### Using V4 Signature (Recommended)

```java
import com.aliyun.oss.*;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.common.comm.SignVersion;

String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
String region = "cn-hangzhou";
EnvironmentVariableCredentialsProvider credentialsProvider =
    CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();

ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);

OSS ossClient = OSSClientBuilder.create()
    .endpoint(endpoint)
    .credentialsProvider(credentialsProvider)
    .clientConfiguration(clientBuilderConfiguration)
    .region(region)
    .build();
```

## V2 SDK - Creating an OSSClient

### Synchronous Client

```java
import com.aliyun.sdk.service.oss2.OSSClient;
import com.aliyun.sdk.service.oss2.OSSClientBuilder;
import com.aliyun.sdk.service.oss2.credentials.CredentialsProvider;
import com.aliyun.sdk.service.oss2.credentials.EnvironmentVariableCredentialsProvider;

// Configure credentials from environment variables
// OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET
CredentialsProvider provider = new EnvironmentVariableCredentialsProvider();

OSSClientBuilder clientBuilder = OSSClient.newBuilder()
    .credentialsProvider(provider)
    .region("cn-hangzhou");

try (OSSClient client = clientBuilder.build()) {
    // Use client to perform OSS operations
    System.out.println("Client initialized successfully");
} catch (Exception e) {
    System.err.println("Failed to initialize client: " + e.getMessage());
}
```

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `endpoint` | The OSS endpoint for your region | Required |
| `region` | Region identifier (e.g., `cn-hangzhou`) | Required for V4 signature |
| `SignatureVersion` | V1 or V4 signature | V1 (recommend V4) |
| `maxConnections` | Max HTTP connections | 1024 |
| `socketTimeout` | Socket timeout (ms) | 50000 |
| `connectionTimeout` | Connection timeout (ms) | 50000 |
| `maxErrorRetry` | Max retry attempts | 3 |

## Best Practices

| Practice | Detail |
|----------|--------|
| **Always call `ossClient.shutdown()`** | Releases underlying HTTP connections |
| **Use STS or environment credentials** | Avoid hardcoding AccessKey in source code |
| **Handle `OSSException` and `ClientException`** | Proper error handling for network/service errors |
| **Reuse OSSClient** | It's thread-safe; create once and reuse |
