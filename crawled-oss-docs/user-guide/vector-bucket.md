# Vector bucket

A vector bucket is a container for storing vector indexes and vector data. It is the fundamental storage unit used to build and manage large-scale vector retrieval services.


> NOTE:

> NOTE: 


> NOTE: Note 

Vector buckets are in invitational preview. You can go to the [Vector Bucket console](https://oss.console.alibabacloud.com/vector-bucket-list) to request access. This feature is available in the China (Shenzhen), China (Beijing), China (Hangzhou), China (Shanghai), China (Ulanqab), and Singapore regions.


## Create a vector bucket


A single Alibaba Cloud account can create a maximum of 10 vector buckets in a single region. To increase this quota, contact [Technical Support](https://smartservice.console.alibabacloud.com/#/ticket/createIndex).

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click Create Vector Bucket.

-

Configure the bucket information:


-

Vector Bucket Name: The name must be unique for an Alibaba Cloud account within the same region. The name must be 3 to 32 characters long. It can contain only lowercase letters, digits, and hyphens (-). The name cannot start or end with a hyphen.

-

Region: Select the region for the bucket. You cannot change the region after the bucket is created. To reduce access latency, select the region closest to your business.

-

Redundancy Type: The default is zone-redundant storage, which ensures high reliability. You do not need to change this setting.

-

Endpoint: The system automatically generates an endpoint. It provides separate endpoints for Internet and internal network access. These endpoints are separate from standard OSS buckets.

-

Click OK to complete the setup.

## ossutil


Create a vector bucket named examplebucket.


`bash
ossutil vectors-api put-vector-bucket --bucket examplebucket
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector put bucket sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
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

    result = vector_client.put_vector_bucket(oss_vectors.models.PutVectorBucketRequest(
        bucket=args.bucket,
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
	flag.StringVar(&accountId, "account-id", "", "The ID of the vector account.")
	flag.StringVar(&indexName, "index", "", "The name of the vector index.")
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
		log.Fatalf("failed to put vector index%v", err)
	}
	log.Printf("put vector index result:%#v\n", result)
}
`


## API


Call the [PutVectorBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/putvectorbucket) operation to create a vector bucket.

## Get vector bucket information

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, click the name of the target bucket.

-

On the Overview page, view the following information:


-

Basic Information: Includes the bucket name, region, and creation time.

-

Endpoints: Endpoints for Internet and internal network access.

## ossutil


View information about the vector bucket named examplebucket.


`bash
ossutil vectors-api get-vector-bucket --bucket examplebucket
`


## SDK

## Python


`python
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector get bucket sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
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

    result = vector_client.get_vector_bucket(oss_vectors.models.GetVectorBucketRequest(
        bucket=args.bucket,
    ))

    print(f'status code: {result.status_code},'
          f' request id: {result.request_id},'
          f' bucket: {result.bucket_info},'
          )


if __name__ == "__main__":
    main()
`


## Go


`go
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

	request := &vectors.GetVectorBucketRequest{
		Bucket: oss.Ptr(bucketName),
	}
	result, err := client.GetVectorBucket(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to get vector bucket %v", err)
	}
	log.Printf("get vector bucket result:%#v\n", result)
}
`


## API


Call the [GetVectorBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/getvectorbucket) operation to retrieve information about a vector bucket.

## List vector buckets

## Console


Go to the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page to view all vector buckets in your account.

## ossutil


List all vector buckets in your account.


`bash
ossutil vectors-api list-vector-buckets
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="list vector buckets sample")

parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
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

    client = oss_vectors.Client(cfg)

    # Create the Paginator for the ListVectorBuckets operation
    paginator = client.list_vector_buckets_paginator()

    # Iterate through the vector bucket pages
    for page in paginator.iter_page(oss_vectors.models.ListVectorBucketsRequest(
        )
    ):
        for o in page.buckets:
            print(f'Bucket: {o.name}, {o.location}')

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
	region    string
	accountId string
)

func init() {
	flag.StringVar(&region, "region", "", "The region where the vector bucket is located.")
	flag.StringVar(&accountId, "account-id", "", "The ID of the vector account.")
}

func main() {
	flag.Parse()
	if len(region) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, region required")
	}

	if len(accountId) == 0 {
		flag.PrintDefaults()
		log.Fatalf("invalid parameters, accountId required")
	}

	cfg := oss.LoadDefaultConfig().
		WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()).
		WithRegion(region).WithAccountId(accountId)

	client := vectors.NewVectorsClient(cfg)

	request := &vectors.ListVectorBucketsRequest{}

	p := client.NewListVectorBucketsPaginator(request)

	var i int
	log.Println("Vector Buckets:")
	for p.HasNext() {
		i++

		page, err := p.NextPage(context.TODO())
		if err != nil {
			log.Fatalf("failed to get page %v, %v", i, err)
		}

		// Log the objects found
		for _, b := range page.Buckets {
			log.Printf("Bucket:%v, %v, %v\n", oss.ToString(b.Name), oss.ToString(b.ResourceGroupId), oss.ToString(b.Location))
		}
	}
}
`


## API


Call the [ListVectorBuckets](https://www.alibabacloud.com/help/en/oss/developer-reference/listvectorbuckets) operation to list all vector buckets in your account.

## Delete a vector bucket


Before you delete a vector bucket, you must first delete all the vector indexes and vector data it contains. This operation cannot be undone. Proceed with caution and ensure that you have backed up important data.

## Console


-

On the [Vector Buckets](https://oss.console.alibabacloud.com/vector-bucket-list) page, find and click the name of the vector bucket that you want to delete.

-

In the navigation pane on the left, click Delete Bucket.

-

Follow the on-screen instructions to confirm the operation and clean up the resources in the bucket.

-

After the cleanup is complete, click Delete Immediately.

## ossutil


Delete the vector bucket named examplebucket.


`bash
ossutil vectors-api delete-vector-bucket --bucket examplebucket
`


## SDK

## Python


`
import argparse
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors

parser = argparse.ArgumentParser(description="vector delete bucket sample")
parser.add_argument('--region', help='The region in which the bucket is located.', required=True)
parser.add_argument('--bucket', help='The name of the bucket.', required=True)
parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS')
parser.add_argument('--account_id', help='The account id.', required=True)

def main():
    args = parser.parse_args()

    # Load credential values from environment variables.
    credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider()

    # Use the SDK's default configuration.
    cfg = oss.config.load_default()
    cfg.credentials_provider = credentials_provider
    cfg.region = args.region
    cfg.account_id = args.account_id

    if args.endpoint is not None:
        cfg.endpoint = args.endpoint

    vector_client = oss_vectors.Client(cfg)

    result = vector_client.delete_vector_bucket(oss_vectors.models.DeleteVectorBucketRequest(
        bucket=args.bucket,
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

	request := &vectors.DeleteVectorBucketRequest{
		Bucket: oss.Ptr(bucketName),
	}
	result, err := client.DeleteVectorBucket(context.TODO(), request)
	if err != nil {
		log.Fatalf("failed to delete vector bucket %v", err)
	}
	log.Printf("delete vector bucket result:%#v\n", result)
}
`


## API


Call the [DeleteVectorBucket](https://www.alibabacloud.com/help/en/oss/developer-reference/deletevectorbucket) operation to delete a vector bucket.


Thank you! We've received your  feedback.