# Vector index

A vector index stores and manages vector data in a vector bucket. Each index defines the vector dimensions, distance measure, and metadata structure, which provides the foundation for vector search.

## Create a vector index


A single vector bucket can contain up to 100 vector indexes. The call frequency for the [PutVectorIndex](https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorindex) API operation is limited to 5 calls per second.

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click a vector bucket.

-

On the Index List page, click Create Index Table.

-

Configure the index parameters:


-

Index Table Name: The name must be 1 to 63 characters in length, contain only letters and digits, and start with a letter. The name must be unique within the vector bucket.

-

Vector Data Type: The default is float32 (floating-point).

-

Vector Dimensions: 1 to 4096. All vectors added to this index must have the same number of dimensions.

-

Distance Measure: Select a distance calculation method.


-

Euclidean Distance: The straight-line distance between two points in space. Suitable for measuring numerical differences.

-

Cosine Distance: Measures the difference in direction between two vectors. Suitable for calculating high-dimensional semantic similarity for text, images, and more.

-

Metadata Configuration: Configure metadata fields that are not used for filtering. These fields store additional information that is not used for search filtering and serves as a description of the vector data. The metadata configuration has the following limits:


-

1 to 10 metadata fields.

-

The name of each metadata primary key can be 1 to 63 bytes in length.

-

Click OK to create the index.

## ossutil


For the bucket `examplebucket`, you can create an index named `index` with 512 vector dimensions, the float32 data type, and the Euclidean distance measure.


`bash
ossutil vectors-api put-vector-index --bucket examplebucket --index-name index --data-type float32 --dimension 512 --distance-metric euclidean
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector put vector index sample")
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

    result = vector_client.put_vector_index(oss_vectors.models.PutVectorIndexRequest(
        bucket=args.bucket,
        index_name=args.index_name,
        dimension=512,
        data_type='float32',
        distance_metric='euclidean',
        metadata={"nonFilterableMetadataKeys": ["key1", "key2"]}
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
		log.Fatalf("invalid parameters, accountId required")
	}

	if len(indexName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, index required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.PutVectorIndexRequest{
		Bucket:         oss.Ptr(bucketName),
		DataType:       oss.Ptr("float32"),
		Dimension:      oss.Ptr(128),
		DistanceMetric: oss.Ptr("cosine"),
		IndexName:      oss.Ptr(indexName),
		Metadata: map[string]any{
			"nonFilterableMetadataKeys": string{"foo", "bar"},
		},
	}
	result, err := client.PutVectorIndex(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to put vector index %v", err)
	}
	log.Printf("put vector index result: %#v\n", result)
}
`


## API


Call the [PutVectorIndex](https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorindex) operation to create a vector index.

## Get vector index information

## Console


On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click a vector bucket. On the Index List page, you can view the vector index information.

## ossutil


Retrieve the properties of the vector index named `index` in the vector bucket `examplebucket`.


`bash
ossutil vectors-api get-vector-index --bucket examplebucket --index-name index
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector get vector index sample")
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

    result = vector_client.get_vector_index(oss_vectors.models.GetVectorIndexRequest(
        bucket=args.bucket,
        index_name=args.index_name,
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
          )

    if result.index:
        print(f'index name: {result.index}')

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
	indexName  string
	accountId  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&indexName, "index", "", "The name of the vector index.")
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

	if len(indexName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, index required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accountId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.GetVectorIndexRequest{
		Bucket:    oss.Ptr(bucketName),
		IndexName: oss.Ptr(indexName),
	}
	result, err := client.GetVectorIndex(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to get vector index %v", err)
	}
	log.Printf("get vector index result: %#v\n", result)
}
`


## API


Call the [GetVectorIndex](https://www.alibabacloud.com/help/en/oss/developer-reference/getvectorindex) operation to retrieve vector index information.

## List vector index information


The [ListVectorIndexes](https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorindexes) API operation returns a maximum of 500 indexes per call. Use paging to retrieve the next batch of indexes. The concurrency limit is 16.

## Console


On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click a vector bucket. The Index List page opens and lists all indexes in the bucket.

## ossutil


List all vector indexes in the vector bucket named examplebucket.


`bash
ossutil vectors-api list-vector-indexes --bucket examplebucket
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="list vector indexes sample")

parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--account_id', help='The account id.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)

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

    # Create the Paginator for the ListVectorIndex operation
    paginator = client.list_vector_indexes_paginator()

    # Iterate through the vector index pages
    for page in paginator.iter_page(oss_vectors.models.ListVectorIndexesRequest(
        bucket=args.bucket
        )
    ):
        for o in page.indexes:
            print(f'Index: {o.get("indexName")}, {o.get("dataType")}, {o.get("dimension")}, {o.get("status")}')

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
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(bucketName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, bucket required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accountId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.ListVectorIndexesRequest{
		Bucket: oss.Ptr(bucketName),
	}
	p := client.NewListVectorIndexesPaginator(request)

	var i int
	log.Println("Vector Indexes:")
	for p.HasNext() {
		i++

		page, err := p.NextPage(context.TODO())
		if err != nil {
			log.Fatalf("failed to get page %v, %v", i, err)
		}

		// Log the objects found
		for _, index := range page.Indexes {
			log.Printf("index: %v, %v, %v, %v\n", oss.ToString(index.IndexName), oss.ToTime(index.CreateTime), oss.ToString(index.DataType), oss.ToString(index.Status))
		}
	}
}
`


## API


Call the [ListVectorIndexes](https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorindexes) operation to list all vector indexes in a vector bucket.

## Delete a vector index


When you delete an index, all vector data in that index is also deleted. This operation is irreversible. Proceed with caution and ensure that you have backed up important data.

## Console


On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click a vector bucket. On the Index List page, select the index that you want to delete, and then complete the deletion.

## ossutil


Delete the vector index named `index` from the vector bucket `examplebucket`.


`bash
ossutil vectors-api delete-vector-index --bucket examplebucket --index-name index
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector delete vector index sample")
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

    result = vector_client.delete_vector_index(oss_vectors.models.DeleteVectorIndexRequest(
        bucket=args.bucket,
        index_name=args.index_name,
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
	indexName  string
	accountId  string
)

func init() {
	flag.StringVar(&region, "region", "", "The region in which the vector bucket is located.")
	flag.StringVar(&bucketName, "bucket", "", "The name of the vector bucket.")
	flag.StringVar(&indexName, "index", "", "The name of the vector index.")
	flag.StringVar(&accountId, "account-id", "", "The ID of the vector account.")
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

	if len(indexName) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, index required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accountId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.DeleteVectorIndexRequest{
		Bucket:    oss.Ptr(bucketName),
		IndexName: oss.Ptr(indexName),
	}
	result, err := client.DeleteVectorIndex(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to delete vector index %v", err)
	}

	log.Printf("delete vector index result:%#v\n", result)
}
`


## API


Call the [DeleteVectorIndex](https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectorindex) operation to delete a vector index.


Thank you! We've received your  feedback.