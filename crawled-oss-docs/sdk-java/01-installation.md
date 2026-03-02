# Java SDK Installation

> Source: https://www.alibabacloud.com/help/en/oss/developer-reference/java-installation

## Prerequisites

- Java 1.8 or later
- Maven or Gradle build tool

## SDK Versions

Alibaba Cloud OSS provides two versions of the Java SDK:
- **Java SDK V1** (`aliyun-sdk-oss`) - Stable, widely used
- **Java SDK V2** (`alibabacloud-oss-java-sdk-v2`) - Developer preview with builder patterns, async support

## Maven Installation (V1)

Add the following dependency to your `pom.xml`:

```xml
<dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>aliyun-sdk-oss</artifactId>
    <version>3.18.1</version>
</dependency>
```

For **Java 9+**, you also need JAXB dependencies:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.1</version>
</dependency>
<dependency>
    <groupId>javax.activation</groupId>
    <artifactId>activation</artifactId>
    <version>1.1.1</version>
</dependency>
<dependency>
    <groupId>org.glassfish.jaxb</groupId>
    <artifactId>jaxb-runtime</artifactId>
    <version>2.3.3</version>
</dependency>
```

## Maven Installation (V2 - Preview)

```xml
<dependency>
    <groupId>com.aliyun.oss</groupId>
    <artifactId>alibabacloud-oss-sdk-java-v2</artifactId>
    <version>LATEST</version>
</dependency>
```

## Credentials Dependency

For credential provider chain support:

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>credentials-java</artifactId>
    <version>LATEST</version>
</dependency>
```

## Build from Source

```shell
mvn clean install -DskipTests
```

## Verification

After adding the dependency, verify it compiles:

```java
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;

public class VerifyInstall {
    public static void main(String[] args) {
        System.out.println("OSS SDK installed successfully!");
    }
}
```
