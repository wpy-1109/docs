# OSS MCP Server (Alpha)

Use [OSS MCP Server](https://www.npmjs.com/package/alibabacloud-oss-mcp-server) to integrate OSS data management capabilities into your AI applications.


> IMPORTANT:

> NOTE: 


> NOTE: Important 

This is an Alpha version and is subject to major changes.


## Tools


OSS MCP Server provides the following tools:

#### List buckets (ListBuckets)


Supported parameters:


-

`[prefix]`: The prefix that the returned bucket names must contain.

-

`[marker]`: The position from which to start the query. The query returns results in alphabetical order, starting from the entry that follows the marker.

-

`[maxKeys]`: The maximum number of buckets to return. The default value is 100. You can configure the maximum value for this parameter in the OSS MCP Server instance.

-

`[resourceGroupId]`: The ID of the resource group to which the returned buckets belong.

-

`[region]`: The OSS-specific region ID, such as oss-cn-hangzhou. This parameter specifies the endpoint for the request.

#### View bucket information (GetBucketInfo)


Supported parameters:


-

`bucket`: The name of the bucket.

-

`[region]`: The OSS-specific region ID, such as oss-cn-hangzhou. This parameter specifies the endpoint for the request.

#### Get the storage capacity, number of files, and number of multipart parts for a bucket (GetBucketStat)


Supported parameters:


-

`bucket`: The name of the bucket.

-

`[region]`: The OSS-specific region ID, such as oss-cn-hangzhou. This parameter specifies the endpoint for the request.

## Environment requirements


Node.js >= 18.20.5

## STDIO


Communicate with the MCP Server through standard input/output (STDIO).

### Cursor


Edit `~/.cursor/mcp.json`:


`json
{
  "mcpServers": {
    "alibabacloud-oss": {
      "command": "npx",
      "args": ["-y", "alibabacloud-oss-mcp-server@alpha"],
      "env": {
        "OSS_ACCESS_KEY_ID": "your-access-key-id",
        "OSS_ACCESS_KEY_SECRET": "your-access-key-secret"
      }
    }
  }
}
`


Optional environment variables:


-

`OSS_SECURITY_TOKEN`: The security token. This is required if you use temporary identity credentials.

-

`OSS_REGION`: The OSS-specific region ID, such as oss-cn-hangzhou.

-

`OSS_ENDPOINT`: The endpoint.

### Cherry Studio


-

Type: Standard input/output

-

Command: `npx`

-

Parameters: `-y alibabacloud-oss-mcp-server@alpha`

-

Environment variables:


-

`OSS_ACCESS_KEY_ID=your-access-key-id` (Required)

-

`OSS_ACCESS_KEY_SECRET=your-access-key-secret` (Required)

-

`OSS_SECURITY_TOKEN=your-security-token` (Optional. Required if you use temporary identity credentials.)

-

`OSS_REGION=oss-cn-hangzhou` (Optional)

-

`OSS_ENDPOINT=https://oss-cn-hangzhou.aliyuncs.com` (Optional)

## Streamable HTTP


Communicate with the MCP Server over HTTP.

### Server-side deploymentNote on remote access: The OSS MCP Server listens only on localhost. For remote deployments, use a reverse proxy for port forwarding. It is also recommended to configure HTTPS and authentication protection.

Run the following command to start the HTTP service:


`bash
export OSS_ACCESS_KEY_ID="your-access-key-id"
export OSS_ACCESS_KEY_SECRET="your-access-key-secret"

npx -y -p alibabacloud-oss-mcp-server@alpha -p express alibabacloud-oss-mcp-server --transport=streamable-http --port=18081
`


Optional environment variables:


-

`OSS_SECURITY_TOKEN`: The security token. This is required if you use temporary identity credentials.

-

`OSS_REGION`: The OSS-specific region ID, such as oss-cn-hangzhou.

-

`OSS_ENDPOINT`: The endpoint.


Server-side endpoint: `http://localhost:18081/mcp`

### Client configuration


Configure the client to connect to the deployed HTTP server endpoint.

##### Cherry Studio


-

Type: Streamable HTTP

-

URL: `http://localhost:18081/mcp`

##### dify


-

Server-side endpoint URL: `http://localhost:18081/mcp`

## Programmatic use


To integrate the OSS MCP Server directly into your code, create and configure a service instance programmatically.

### Installation


`bash
npm install alibabacloud-oss-mcp-server@alpha
`


### Basic usage


`typescript
import { OSSMcpServer, OSSMcpServerTransport } from 'alibabacloud-oss-mcp-server/server';

const server = new OSSMcpServer({
  accessKeyId: process.env.OSS_ACCESS_KEY_ID,
  accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET,
  securityToken: process.env.OSS_SECURITY_TOKEN,
  region: process.env.OSS_REGION,
  endpoint: process.env.OSS_ENDPOINT,
  transportType: OSSMcpServerTransport.STDIO
});

await server.runServer();
`


### Configuration options


When you create an OSSMcpServer instance, you can pass the following configuration options:


OSS client configuration


-

`accessKeyId`: The AccessKey ID.

-

`accessKeySecret`: The AccessKey secret.

-

`[securityToken]`: The security token.

-

`[refreshCredentials]`: The method to refresh access credentials. If you use temporary identity credentials, set this parameter and the `refreshCredentialsInterval` parameter to prevent the credentials from expiring.

-

`[refreshCredentialsInterval]`: The validity period of the access credential in milliseconds (ms). The default value is 300000 ms, which is 5 minutes.

-

`[lastRefreshCredentialsTime]`: The time when the access credential was last refreshed. The default value is the time when the client instance was initialized.

-

`[region]`: The region ID or the OSS-specific region ID. The default value is oss-cn-hangzhou. This parameter is converted to a region ID for signing.

-

`[endpoint]`: The service endpoint. By default, an internet endpoint is generated based on the `region` parameter. If you set this parameter, the `internal` parameter is ignored. If this parameter includes a protocol, the `secure` parameter is ignored. You must set this parameter if the `region` parameter is set to a region ID or you need to access OSS using another domain name.

-

`[internal]`: Specifies whether to use an internal network endpoint. The default value is false.

-

`[secure]`: Specifies whether to use HTTPS to access OSS. The default value is true.

-

`[cname]`: Specifies whether the `endpoint` parameter is a custom domain name. The default value is false. If this parameter is set to true, you must also set the `endpoint` parameter.

-

`[sldEnable]`: Specifies whether to use a second-level domain to access OSS. The default value is false.

-

`[signVersion]`: The signature version. The default value is ESignVersion.V4, which is signature version 4.

-

`[isRequestPay]`: Specifies whether to use the pay-by-requester mode. The default value is false. If you set this parameter to true, the `x-oss-request-payer` request header is added to requests with its value set to requester.

-

`[userAgent]`: A custom User-Agent. This value is sent as part of the `User-Agent` request header.

-

`[timeout]`: The request timeout period in milliseconds (ms). The default value is 60000 ms, which is 60 seconds.

-

`[disabledMD5]`: Specifies whether to skip calculating the Content-MD5 value. The default value is false.

-

`[proxy]`: The proxy settings for HTTP requests.

-

`[retryMax]`: The maximum number of retries for a failed request. The default value is 0.

-

`[requestErrorShouldRetry]`: The method to determine whether to retry a failed request. By default, all failed requests are retried.

-

`[amendTimeSkewed]`: The time drift to correct in milliseconds (ms). The default value is 0.

-

`[customRequestFunction]`: A custom request method.

-

`[customSign]`: A custom signing method. After you configure this parameter, all requests that require signing, except for POST signatures, are signed using this method.


MCP Server configuration


-

`[transportType]`: The communication type. The default value is standard input/output (stdio).

-

`[port]`: The port on which the HTTP server listens. This is valid only for Streamable HTTP communication. The default value is 18081.

-

`[tools]`: The list of tools to enable. By default, all tools are enabled.

-

`[listToolsMaxKeysMaxValue]`: The maximum value (1-1000) for the `maxKeys` parameter in list-based tools. The default value is 100.

-

`[listToolsDefaultMaxKeys]`: The default value for the `maxKeys` parameter in list-based tools. This defaults to the value of `listToolsMaxKeysMaxValue`.

-

`[httpServer]`: A custom HTTP server instance. This is valid only for Streamable HTTP communication.

-

`[logger]`: A logger instance.

-

`[xmlContentText]`: Specifies whether to return the result as a raw XML string after a tool request succeeds. The default value is false, which means a JSON string is returned.

-

`[toolsRequestSuccessCallback]`: The callback function for successful tool requests.

-

`[toolsRequestErrorCallback]`: The callback function for failed tool requests.

Thank you! We've received your  feedback.