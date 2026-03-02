# Quick start for vector buckets

Vector buckets let you store, index, and retrieve high-dimensional vector data in OSS. This guide walks you through four steps: create a vector bucket, create a vector index, upload vector data, and run a retrieval query.

## Prerequisites


Before you begin, make sure you have:


-

An activated OSS account. If not, [activate Object Storage Service (OSS)](https://oss.console.alibabacloud.com/overview)

-

Invitational preview access for Vector Bucket. Go to the [Vector Bucket console](https://oss.console.alibabacloud.com/vector-bucket-list) to request access
Vector Bucket is in the invitational preview stage. Check the [Vector Bucket console](https://oss.console.alibabacloud.com/vector-bucket-list) for the list of supported regions.
## Step 1: Create a vector bucket


A vector bucket stores all your vector data and indexes.


-

On the [Vector Buckets](https://www.alibabacloud.com/help/en/oss/user-guide/vector-bucket) page, click Create a Vector Bucket.

-

Configure the following settings:


| Parameter | Description |
| --- | --- |
| Vector Bucket Name | A globally unique name. Must be 3 to 32 characters long, contain only lowercase letters, numbers, and hyphens (-), and must not start or end with a hyphen. |
| Region | The region for the bucket, such as China (Shenzhen). |


-

Click OK, then click Confirm in the confirmation dialog.

## Step 2: Create a vector index


A vector index defines how vectors are stored and searched, including the number of dimensions and the distance metric. All vectors uploaded to an index must share the same dimensions.


-

On the [Vector Buckets](https://www.alibabacloud.com/help/en/oss/user-guide/vector-bucket) page, click the name of the vector bucket that you created.

-

On the Vector Indexes page, click Create Index Table.

-

Configure the index parameters:


| Parameter | Description |
| --- | --- |
| Index Table Name | A unique name within the bucket. Must be 1 to 63 characters long, consist of letters and numbers, and start with a letter. |
| Vector Data Type | The data type for vector values. Default: float32 (32-bit floating-point). |
| Vector dimension | The number of dimensions per vector. Must be an integer from 1 to 4096. Example: 128. |
| Distance metric function | The method used to measure similarity between vectors. See the following table. |


Distance metric options

| Metric | Description | Best for |
| --- | --- | --- |
| Euclidean distance | Measures the straight-line distance between two points in space. | Numerical difference comparisons |
| Cosine Distance | Measures the directional difference between two vectors, ignoring magnitude. | High-dimensional semantic similarity (text, images) |


-

Click OK.

## Step 3: Upload vector data


After you create an index, upload vector data to make it searchable.


-

In the index list, find the index you created and click View data on the right.

-

Click Vector data insertion.

-

Configure the vector entries. You can add multiple entries at once:


| Field | Description |
| --- | --- |
| Primary Key Value | A unique identifier for the vector. |
| Vector data | A comma-separated array of numbers. The number of values must match the Vector dimension set in Step 2. |
| Metadata | Optional key-value pairs (such as category, title, or timestamp) that you can use as filter conditions during retrieval. |


-

Click Confirm to insert the data.

## Step 4: Retrieve vectors


After you upload data, call the API from your application using an SDK to retrieve vectors.


The following Python example queries the top 10 vectors most similar to a target vector, filtering out entries where the `type` field is "comedy" or "documentary".


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector query vectors sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--index_name', help='The name of the vector index.', required=True)
parser.add_argument('--account_id', help='The account id.', required=True)

def main():
    args = parser.parse_args()

    # Loading credentials values from the environment variables.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)

    query_filter = {
        "$and": [{
            "type": {
                "$nin": ["comedy", "documentary"]
            }
        }]
    }

    query_vector = {"float32": [0.1] * 128}

    result = vector_client.query_vectors(oss_vectors.models.QueryVectorsRequest(
        bucket=args.bucket,
        index_name=args.index_name,
        filter=query_filter,
        query_vector=query_vector,
        return_distance=True,
        return_metadata=True,
        top_k=10
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
          )

    if result.vectors:
        for vector in result.vectors:
            print(f'vector: {vector}')


if __name__ == "__main__":
    main()
`


Required parameters

| Parameter | Description |
| --- | --- |
| --region | The region where the vector bucket is located. |
| --bucket | The name of the vector bucket. |
| --index_name | The name of the vector index. |
| --account_id | Your Alibaba Cloud account ID. |
| --endpoint | (Optional) A custom endpoint for OSS access. |


Key points


-

Credentials: Loaded from environment variables through `EnvironmentVariableCredentialsProvider`. Set `OSS_ACCESS_KEY_ID` and `OSS_ACCESS_KEY_SECRET` before running the script.

-

Filter syntax: Uses `$and` and `$nin` operators to exclude specific metadata values. Metadata fields set during upload (Step 3) are available for filtering.

-

Query vector: Must have the same number of dimensions as the index (128 in this example).

-

`top_k`: Controls how many nearest results to return (10 in this example).

## Next steps


Manage vector buckets through the console, the OSS SDK, ossutil, or API calls. For complete configuration and advanced usage, see:


-

[Vector Buckets](https://www.alibabacloud.com/help/en/oss/user-guide/vector-bucket)

-

[Vector Indexes](https://www.alibabacloud.com/help/en/oss/user-guide/vector-index)

-

[Vectors](https://www.alibabacloud.com/help/en/oss/user-guide/vector-vectors)

-

[Access control and logs](https://www.alibabacloud.com/help/en/oss/user-guide/access-control-and-logging)

Thank you! We've received your  feedback.