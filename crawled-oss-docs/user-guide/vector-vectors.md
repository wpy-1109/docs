# Vectors

Vector data is the core resource of a vector bucket. It consists of three parts:


-

Key (primary key): The unique identifier for a vector.

-

Data (vector data): A high-dimensional numerical array.

-

Metadata: A key-value structure that stores additional properties for a vector, such as category, source, and timestamp. This information is used for post-filtering during queries.


Each vector is stored in a specific vector index and inherits the dimension, data type, and distance measure settings from that index.

## Write vector data


Upload vector data and its metadata to a specified vector index.


-

A single vector index table can store a maximum of 50 million rows of vector data. To increase this quota to 2 billion rows per table, contact [Technical Support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex).

-

The [PutVectors](https://www.alibabacloud.com/help/en/oss/developer-reference/putvectors) API can write up to 500 vectors in a single batch.

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target vector bucket.

-

In the row of the index you created, click View data, and then click Vector data insertion.

-

Configure the vector data. You can add multiple vectors at the same time.


-

Primary Key Value: Set a unique identifier for the vector.

-

Vector data: Enter a numerical array for the vector. The format is a comma-separated list of numbers, such as 0.1, 0.2, 0.3, 0.4, 0.5. The vector dimension must match the dimension of the selected embedding model.

-

Metadata: Add metadata, such as category, title, and timestamp. The total size cannot exceed 40 KB.


-

The supported metadata type is String.

-

A single vector can have a maximum of 10 filterable and non-filterable metadata fields in total.

-

The key for a non-filterable metadata field can be 1 to 63 characters in length.

-

A single filterable metadata field can be up to 2 KB in size.

-

When you perform scalar post-filtering based on filterable metadata, a single filter instruction is subject to the following limits: a maximum length of 64 KB for the filterable metadata, a maximum of 1,024 filterable metadata fields, and a maximum of 8 layers. The filter content can be empty.

-

Click Confirm to insert the data.

## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector put vectors sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--index_name', help='The name of the vector index.', required=True)
parser.add_argument('--account_id', help='The account id.', required=True)

def main():
    args = parser.parse_args()

    # Loading credentials values from the environment variables
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)

    vectors = [
        {
            "data": {"float32":  [0.1] * 128},
            "key": "key1",
            "metadata": {"metadata1": "value1", "metadata2": "value2"}
        },
        {
            "data": {"float32": [0.2] * 128},
            "key": "key2",
            "metadata": {"metadata3": "value3", "metadata4": "value4"}
        }
    ]

    result = vector_client.put_vectors(oss_vectors.models.PutVectorsRequest(
        bucket=args.bucket,
        index_name=args.index_name,
        vectors=vectors,
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
    )

if __name__ == "__main__":
    main()
`


## Go


`
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
)

var (
	region     string
	bucketName string
	accountId  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
}

func main() {
	flag.Parse()
	if len(bucketName) == 0 || len(region) == 0 || len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.PutVectorsRequest{
		Bucket:    oss.Ptr(bucketName),
		IndexName: oss.Ptr("exampleIndex"),

		Vectors: map[string]any{

			{
				"key": "vector1",
				"data": map[string]any{

					"float32": float32{1.2, 2.5, 3},

				},
				"metadata": map[string]any{
					"Key1": "value2",

					"Key2": string{"1", "2", "3"},

				},
			},
		},
	}
	result, err := client.PutVectors(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put vectors %v", err)
	}
	log.Printf("put vectors result:%#v\n", result)
}
`


## ossutil


Add a vector to the index named vector index in the examplebucket vector bucket. Set the vector data to 1, the primary key to vector1, and the metadata to {"Key1": "32"}.


-

Use a JSON configuration file. The following is the content of vectors.json:


`json
[
  {
    "data": {
      "float32": [1]
    },
    "key": "vector1",
    "metadata": {
      "Key1": "32"
    }
  }
]
`


Command example:


`bash
ossutil vectors-api put-vectors --bucket examplebucket --index-name index --vectors file://vectors.json
`


-

Use JSON configuration parameters:


`bash
ossutil vectors-api put-vectors --bucket examplebucket --index-name index --vectors "[{\"data\":{\"float32\":[1]},\"key\":\"vector1\",\"metadata\":{\"Key1\":\"32\"}}]"
`


## API


Call the [PutVectors](https://www.alibabacloud.com/help/en/oss/developer-reference/putvectors) operation to write vector data.

## Perform vector retrieval


You can perform a vector retrieval operation using conditions such as semantic content and metadata to quickly locate target data. This feature provides sub-second retrieval performance with a recall rate of approximately 90%.

## Console


The console supports only single-vector similarity searches. To perform searches in a loop, use an API or SDK.


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target vector bucket.

-

In the row of the index you created, click View data, and then click Vector Data Query.

-

Configure the retrieval parameters:


-

Vector data: Enter the query vector data. Use the same format as when you uploaded the data, such as 0.15, 0.25, 0.35, 0.45, 0.55.

-

Filterable metadata: Filter the results by metadata, such as category or time range.

-

TopK (Number of results): Set the number of most similar results to return. The default range is 1 to 30. You can contact [technical support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex) to request to increase the TopK limit to 100.

-

Return similarity distance: Select whether to return the similarity distance value.

-

Return Metadata: Select whether to return the metadata of the vector.

-

Click OK to perform the query.


The system returns a list of vectors sorted by similarity.

## SDK

## Python


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


## Go


`
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
)

var (
	region     string
	bucketName string
	accountId  string
	indexName  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
	flag.StringVar(&indexName, "index", "", "The name of vector index.")
}

func main() {
	flag.Parse()
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accounId required")
	}

	if len(indexName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, index required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.QueryVectorsRequest{
		Bucket:    oss.Ptr(bucketName),
		IndexName: oss.Ptr(indexName),
		Filter: map[string]any{
			"$and": map[string]any{
				{
					"type": map[string]any{
						"$in": string{"comedy", "documentary"},
					},
				},
			},
		},
		QueryVector: map[string]any{
			"float32": float32{float32(32)},
		},
		ReturnMetadata: oss.Ptr(true),
		ReturnDistance: oss.Ptr(true),
		TopK:           oss.Ptr(10),
	}
	result, err := client.QueryVectors(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to query vectors %v", err)
	}
	log.Printf("query vectors result:%#v\n", result)
}
`


## ossutil


In the index named vector index in the examplebucket vector bucket, retrieve the top 10 vectors of the type comedy or documentary that are most similar to the query vector.


`bash
ossutil vectors-api query-vectors --bucket examplebucket --index-name index --filter "{\"$and\":[{\"type\":{\"$in\":[\"comedy\",\"documentary\"]}}]}" --query-vector "{\"float32\":[32]}" --top-k 10
`


## API


Call the [QueryVectors](https://www.alibabacloud.com/help/en/oss/developer-reference/queryvectors) operation to perform a vector similarity search.

## Get vector data

## Console


On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target vector bucket. On the Index List page, click an index name to navigate to the vector data page and view the vector information.

## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector get vectors sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--index_name', help='The name of the vector index.', required=True)
parser.add_argument('--account_id', help='The account id.', required=True)

def main():
    args = parser.parse_args()

    # Loading credentials values from the environment variables
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)

    keys = ['key1', 'key2']

    result = vector_client.get_vectors(oss_vectors.models.GetVectorsRequest(
        bucket=args.bucket,
        index_name=args.index_name,
        keys=keys,
        return_data=True,
        return_metadata=True
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
          )

    if result.vectors:
        for vector in result.vectors:
            print(f'vector id: {vector}')


if __name__ == "__main__":
    main()
`


## Go


`
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
)

var (
	region     string
	bucketName string
	accountId  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
}

func main() {
	flag.Parse()
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accounId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.GetVectorsRequest{
		Bucket:         oss.Ptr(bucketName),
		IndexName:      oss.Ptr("index"),
		Keys:           string{"key1", "key2", "key3"},
		ReturnData:     oss.Ptr(true),
		ReturnMetadata: oss.Ptr(false),
	}
	result, err := client.GetVectors(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to get vectors %v", err)
	}
	log.Printf("get vectors result:%#v\n", result)
}
`


## ossutil


Retrieve the properties for vectors with the primary keys key and key1 in the index named index in the examplebucket vector bucket.


`bash
ossutil vectors-api get-vectors --bucket examplebucket --index-name index --keys key,key1
`


## API


Call the [GetVectors](https://www.alibabacloud.com/help/en/oss/developer-reference/getvectors) operation to retrieve specified vector data.

## List vector data

## Console


On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target vector bucket. On the Index List page, click an index name to view the list of vectors it contains.

## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="list vectors sample")

parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--account_id', help='The account id.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--index_name', help='The name of the vector index.', required=True)

def main():

    args = parser.parse_args()

    # Loading credentials values from the environment variables
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    client = oss_vectors.Client(cfg)

    # Create the Paginator for the ListVectors operation
    paginator = client.list_vectors_paginator()

    # Create request with bucket and index name
    request = oss_vectors.models.ListVectorsRequest(
        bucket=args.bucket,
        index_name=args.index_name
    )

    # Iterate through the vectors pages
    for page in paginator.iter_page(request):
        for o in page.vectors:
            print(f'Vector: {o}')

if __name__ == "__main__":
    main()
`


## Go


`
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
)

var (
	region     string
	bucketName string
	accountId  string
	indexName  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
	flag.StringVar(&indexName, "index", "", "The name of vector index.")
}

func main() {
	flag.Parse()
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accounId required")
	}

	if len(indexName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, index required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.ListVectorsRequest{
		Bucket:         oss.Ptr(bucketName),
		IndexName:      oss.Ptr(indexName),
		ReturnMetadata: oss.Ptr(true),
		ReturnData:     oss.Ptr(false),
	}

	p := client.NewListVectorsPaginator(request)

	var i int
	log.Println("Vectors:")
	for p.HasNext() {
		i++

		page, err := p.NextPage(context.TODO())
		if err != nil {
			log.Fatalf("failed to get page %v, %v", i, err)
		}

		for _, v := range page.Vectors {
			log.Printf("vector:%v\n", v)
		}
	}
}
`


## ossutil


List all vectors in the index named index in the examplebucket vector bucket.


`bash
ossutil vectors-api list-vectors --bucket examplebucket --index-name index
`


## API


Call the [ListVectors](https://www.alibabacloud.com/help/en/oss/developer-reference/listvectors) operation to list all vector data in a vector index.

## Delete vector data


You can delete vector data in batches. This operation is irreversible. Proceed with caution and ensure that you have backed up important data.

## Console


On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the target vector bucket. Navigate to the Index List page and click an index name to open the vector data page. Select the vector data to delete and complete the operation.

## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector delete vectors sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--index_name', help='The name of the vector index.', required=True)
parser.add_argument('--account_id', help='The account id.', required=True)

def main():
    args = parser.parse_args()

    # Loading credentials values from the environment variables
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Using the SDK's default configuration
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id
    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)

    keys = ['key1', 'key2', 'key3']

    result = vector_client.delete_vectors(oss_vectors.models.DeleteVectorsRequest(
        bucket=args.bucket,
        index_name=args.index_name,
        keys=keys,
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
    )

if __name__ == "__main__":
    main()
`


## Go


`
package main

import (
	"context"
	"flag"
	"log"

	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials"
	"github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/vectors"
)

var (
	region     string
	bucketName string
	accountId  string
)

func init() {
	// Define command-line parameters.
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&accountId, "account-id", "", "The id of vector account.")
}

func main() {
	// Parse command-line parameters.
	flag.Parse()

	// Verify required parameters.
	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket name required")
	}

	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accountId required")
	}

	// Create a configuration, and set the credential provider, region, and account ID.
	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).
		WithAccountId(accountId)

	// Create a vector storage client.
	client := vectors.NewVectorsClient(cfg)

	// Construct a request to delete vector data.
	request := &vectors.DeleteVectorsRequest{
		Bucket:    oss.Ptr(bucketName),
		IndexName: oss.Ptr("index"),
		Keys: string{

			"key1", "key2",                          // List of vector keys to delete.
		},
	}

	// Execute the operation to delete vector data.
	result, err := client.DeleteVectors(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to delete vectors %v", err)
	}

	// Output the operation result.
	log.Printf("delete vectors result:%#v\n", result)
}
`


## ossutil


Delete the vectors with the primary keys key and key1 from the index named index in the examplebucket vector bucket.


`bash
ossutil vectors-api delete-vectors --bucket examplebucket --index-name index --keys key,key1
`


## API


Call the [DeleteVectors](https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectors) operation to delete vector data.

Thank you! We've received your  feedback.