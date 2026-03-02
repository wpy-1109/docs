# Build a multimodal semantic image retrieval system

You can use the vector storage feature of Object Storage Service (OSS) and the multimodal embedding model from Alibaba Cloud Model Studio to build an intelligent semantic retrieval system for large numbers of images. This system lets you search for images using natural language descriptions and is useful for scenarios such as e-commerce product searches, smart photo albums, and media asset management.

## Solution overview


Building a multimodal semantic image retrieval system includes the following steps:


-

Prepare image data: Prepare the image dataset for retrieval and upload it to a bucket.

-

Vectorize images: Use the Alibaba Cloud Model Studio multimodal embedding model to convert images into high-dimensional vectors.

-

Create a vector index and write data: Create a vector bucket, build a vector index, and write the image vector data to the index.

-

Perform semantic retrieval: Convert text queries into vectors, perform similarity searches in the vector index, and filter the results using metadata.

## Prerequisites

### Obtain access credentials


-

[Activate OSS](https://oss.console.alibabacloud.com/overview) and [obtain an AccessKey ID and AccessKey secret](https://www.alibabacloud.com/help/en/ram/user-guide/create-an-accesskey-pair).

-

[Activate Alibaba Cloud Model Studio](https://modelstudio.console.alibabacloud.com/) and [obtain an API key](https://www.alibabacloud.com/help/en/model-studio/get-api-key).

### Install the SDK


-

You have Python 3.12 or later installed.

-

Run the following commands to install the Alibaba Cloud OSS Python SDK V2 and the Alibaba Cloud Model Studio SDK.


`shell
pip install alibabacloud-oss-v2
pip install dashscope
`


### Configure environment variables


To ensure code security and portability, configure your access credentials as environment variables.


`bash
# Alibaba Cloud Model Studio API key
export DASHSCOPE_API_KEY=<Your_Model_Studio_API_Key>

# OSS access credentials
export oss_test_access_key_id=<Your_AccessKey_ID>
export oss_test_access_key_secret=<Your_AccessKey_Secret>
export oss_test_region=<Your_Region_ID_such_as_cn-hangzhou>
export oss_test_account_id=<Your_Alibaba_Cloud_Account_ID>
`


## 1. Prepare image data


You must upload local images to a bucket because the Alibaba Cloud Model Studio embedding model requires URL access to vectorize them. The following code shows how to upload images in batches from an on-premises folder to a specified bucket.


`python
 -*- coding: utf-8 -*-
"""
Example: Upload images using the file upload manager.

This example shows how to use the OSS SDK's file upload manager for more efficient file uploads.
This is suitable for large files or scenarios that require resumable uploads.
"""

import os
import alibabacloud_oss_v2 as oss
from alibabacloud_oss_v2.models import PutObjectRequest


def create_oss_client():
    """Create an OSS client."""
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')

    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
        access_key_id, access_key_secret
    )
    cfg.region = region
    return oss.Client(cfg)


def upload_with_uploader(client, bucket_name: str, local_path: str, oss_key: str):
    """
    Upload a file using the upload manager.

    Args:
        client: The OSS client.
        bucket_name: The name of the OSS bucket.
        local_path: The path to the local file.
        oss_key: The key of the OSS object.
    """
    # Create an upload manager.
    uploader = client.uploader()

    # Perform the upload.
    result = uploader.upload_file(
        filepath=local_path,
        request=PutObjectRequest(
            bucket=bucket_name,
            key=oss_key
        )
    )
    return result


def main():
    client = create_oss_client()

    bucket_name = "your-bucket-name"
    # Note: The data/photograph/ directory in the GitHub repository at the end of this topic contains test images that you can use directly.
    # You can also modify the local_image_path variable to point to your own image directory.
    local_image_path = "data/photograph/"
    oss_prefix = "photograph/"

    image_files = os.listdir(local_image_path)
    print(f"Number of images to upload: {len(image_files)}")

    for i, image_name in enumerate(image_files, 1):
        local_path = os.path.join(local_image_path, image_name)
        oss_key = f"{oss_prefix}{image_name}"

        try:
            result = upload_with_uploader(client, bucket_name, local_path, oss_key)
            print(f"[{i}/{len(image_files)}] Upload successful: {image_name}, status: {result.status_code}")
        except Exception as e:
            print(f"[{i}/{len(image_files)}] Upload failed for {image_name}: {e}")

    print(f"\nUpload complete!")


if __name__ == "__main__":
    main()
`


## 2. Vectorize images


You can use the Alibaba Cloud Model Studio multimodal embedding model to convert images into 1024-dimensional vectors.


`python
import dashscope
from dashscope import MultiModalEmbeddingItemImage


def embedding_image(image_url: str) -> list[float]:
    """
    Convert an image to a vector.

    Args:
        image_url: The URL of the image. OSS URLs and public URLs are supported.

    Returns:
        A list representing a 1024-dimensional vector.
    """
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[MultiModalEmbeddingItemImage(image=image_url, factor=1.0)]
    )
    return resp.output["embeddings"][0]["embedding"]


def main():
    # Example image URL. Replace it with an accessible image URL. If the image is private, use a signed temporary URL.
    image_url = "http://your-bucket-name.oss-cn-hangzhou.aliyuncs.com/photograph/Zsd0YhBa8LM.jpg"

    print(f"Vectorizing image: {image_url}")

    # Call the Embedding API.
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[MultiModalEmbeddingItemImage(image=image_url, factor=1.0)]
    )

    # Print the full response.
    print("\nFull response:")
    print(resp)

    # Get the vector.
    embedding = resp.output["embeddings"][0]["embedding"]
    print(f"\nVector dimensions: {len(embedding)}")
    print(f"First 10 elements of the vector: {embedding[:10]}")


if __name__ == "__main__":
    main()
`


## 3. Create a vector index and write data

### 3.1 Create a vector bucket


You need to create a vector bucket to serve as a container for all vector data and indexes.


`python
# -*- coding: utf-8 -*-
"""
Example: Create a VectorBucket.

This example shows how to create an OSS VectorBucket.

Prerequisites:
1. alibabacloud-oss-v2 is installed: pip install alibabacloud-oss-v2
2. Environment variables are set. For more information, see the client initialization example.
"""

import os
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors


def main():
    # Get credentials from environment variables.
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')
    account_id = os.environ.get('oss_test_account_id')

    # Initialize the client.
    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
        access_key_id, access_key_secret
    )
    cfg.region = region
    cfg.account_id = account_id
    client = oss_vectors.Client(cfg)

    # VectorBucket name.
    vector_bucket_name = "my-test-2"

    print(f"Creating VectorBucket: {vector_bucket_name}")

    try:
        # Create the VectorBucket.
        result = client.put_vector_bucket(oss_vectors.models.PutVectorBucketRequest(
            bucket=vector_bucket_name,
        ))
        print(f"Creation successful!")
        print(f"  status code: {result.status_code}")
        print(f"  request id: {result.request_id}")
    except Exception as e:
        print(f"Creation failed: {e}")
        print("Note: An error is returned if the bucket already exists.")


if __name__ == "__main__":
    main()
`


### 3.2 Create a vector index


After creating a bucket, create a vector index in it. The index defines the structure of the vectors, such as their dimensions, and the retrieval method, such as the distance metric, providing the foundation for storing and querying vector data.


`python
# -*- coding: utf-8 -*-
"""
Example: Create a vector index.

This example shows how to create a vector index in a VectorBucket.

Prerequisites:
1. alibabacloud-oss-v2 is installed: pip install alibabacloud-oss-v2
2. Environment variables are set.
3. A VectorBucket is created.
"""

import os
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors


def main():
    # Get credentials from environment variables.
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')
    account_id = os.environ.get('oss_test_account_id')

    # Initialize the client.
    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
        access_key_id, access_key_secret
    )
    cfg.region = region
    cfg.account_id = account_id
    client = oss_vectors.Client(cfg)

    # Configure parameters.
    vector_bucket_name = "my-test-2"
    vector_index_name = "test1"
    dimension = 1024  # Vector dimensions output by the Alibaba Cloud Model Studio multimodal model.

    print(f"Creating vector index:")
    print(f"  Bucket: {vector_bucket_name}")
    print(f"  Index: {vector_index_name}")
    print(f"  Dimensions: {dimension}")

    # Create the vector index.
    result = client.put_vector_index(oss_vectors.models.PutVectorIndexRequest(
        bucket=vector_bucket_name,
        index_name=vector_index_name,
        dimension=dimension,
        data_type='float32',           # Vector data type.
        distance_metric='cosine',       # Distance metric: cosine similarity.
        metadata={
            "nonFilterableMetadataKeys": ["key1", "key2"]  # Metadata fields not used for filtering.
        }
    ))
    print(f"\nCreation successful!")
    print(f"  status code: {result.status_code}")
    print(f"  request id: {result.request_id}")

if __name__ == "__main__":
    main()
`


Parameters:








| Parameter | Description |
| --- | --- |
| dimension | The vector dimensions. This must match the output dimensions of the embedding model. |
| data_type | The vector data type. `float32` is supported. |
| distance_metric | The distance metric. `cosine` and `euclidean` are supported. |
| metadata | The metadata configuration. Configure non-filterable metadata fields to store additional information that is not used for search filtering. This information serves as a description for the vector data. |


### 3.3 Write vector data


After the index is ready, you can upload the vector data to the specified vector index for subsequent retrieval.


`python
# -*- coding: utf-8 -*-
"""
Example: Write image vector data in batches.

This example shows how to write vectorized image data to a vector index in batches.

Prerequisites:
1. alibabacloud-oss-v2 is installed: pip install alibabacloud-oss-v2
2. Environment variables are set.
3. A vector index is created.
4. The image vector data file (data/data.json) is ready.
"""

import os
import json
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors


def main():
    # Get credentials from environment variables.
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')
    account_id = os.environ.get('oss_test_account_id')

    # Initialize the client.
    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
        access_key_id, access_key_secret
    )
    cfg.region = region
    cfg.account_id = account_id
    client = oss_vectors.Client(cfg)

    # Configure parameters.
    vector_bucket_name = "my-test-2"
    vector_index_name = "test1"

    # Load the pre-processed image vector data.
    # Note: The data/ directory in the GitHub repository at the end of this topic contains a test file that you can use directly.
    # You can also modify the data_file variable to point to your own image directory.
    data_file = "./data/data.json"
    print(f"Loading image vector data: {data_file}")

    image_data_array = with open(data_file, "r") as f:
        image_data_array = json.load(f)

    print(f"Loaded {len(image_data_array)} image vector data entries")

    # Print a data sample.
    if len(image_data_array) > 0:
        sample = image_data_array[0]
        print(f"\nData sample:")
        print(f"  key: {sample.get('key', 'N/A')}")
        if 'metadata' in sample:
            print(f"  metadata: {sample['metadata']}")
        if 'data' in sample and 'float32' in sample['data']:
            print(f"  Vector dimensions: {len(sample['data']['float32'])}")

    # Write in batches of 500.
    batch_size = 500
    vectors = total_written = 0

    print(f"\nStarting batch write (batch_size={batch_size})...")

    for idx in range(len(image_data_array)):
        vectors.append(image_data_array[idx])

        if len(vectors) == batch_size:
            result = client.put_vectors(oss_vectors.models.PutVectorsRequest(
                bucket=vector_bucket_name,
                index_name=vector_index_name,
                vectors=vectors,
            ))
            total_written += len(vectors)
            print(f"  Wrote {total_written}/{len(image_data_array)} entries, "
                  f"status code: {result.status_code}")
            vectors = # Write the remaining data.
    if len(vectors) > 0:
        result = client.put_vectors(oss_vectors.models.PutVectorsRequest(
            bucket=vector_bucket_name,
            index_name=vector_index_name,
            vectors=vectors,
        ))
        total_written += len(vectors)
        print(f"  Wrote {total_written}/{len(image_data_array)} entries, "
              f"status code: {result.status_code}")

    print(f"\nWrite complete! A total of {total_written} vector data entries were written.")


if __name__ == "__main__":
    main()
`


## 4. Perform semantic retrieval


You can use natural language text as a query to retrieve the most similar images from the vector index.

### 4.1 Basic retrieval


After vectorizing the query text, for example, "dog", you can find the top-K closest image vectors in the index.


`python
# -*- coding: utf-8 -*-
"""
Example: Query vectors.

This example shows how to perform a similarity search using vectors. It supports metadata filtering.

Prerequisites:
1. alibabacloud-oss-v2 and dashscope are installed.
2. Environment variables are set.
3. The Alibaba Cloud Model Studio API key is set: export DASHSCOPE_API_KEY=<Your_API_Key>
4. Vector data is written.
"""

import os
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors
import dashscope
from dashscope import MultiModalEmbeddingItemText


def embedding(text: str) -> list[float]:
    """
    Vectorize text to convert a query text into a vector for text-to-image search.

    Args:
        text: The text to convert.

    Returns:
        A list representing a 1024-dimensional vector.
    """
    return dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[MultiModalEmbeddingItemText(text=text, factor=1.0)]
    ).output["embeddings"][0]["embedding"]


def main():
    # Get credentials from environment variables.
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')
    account_id = os.environ.get('oss_test_account_id')

    # Initialize the client.
    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
        access_key_id, access_key_secret
    )
    cfg.region = region
    cfg.account_id = account_id
    client = oss_vectors.Client(cfg)

    # Configure parameters.
    vector_bucket_name = "my-test-2"
    vector_index_name = "test1"

    # Query text.
    query_text = "dog"

    print(f"Performing vector retrieval:")
    print(f"  Bucket: {vector_bucket_name}")
    print(f"  Index: {vector_index_name}")
    print(f"  Query text: {query_text}")

    # Convert the query text to a vector.
    print(f"\nConverting query text to a vector...")
    query_vector = embedding(query_text)
    print(f"  Vector dimensions: {len(query_vector)}")

    # Perform vector retrieval.
    print(f"\nPerforming vector retrieval...")
    result = client.query_vectors(oss_vectors.models.QueryVectorsRequest(
        bucket=vector_bucket_name,
        index_name=vector_index_name,
        query_vector={
            "float32":query_vector
        },
        top_k=5,                    # Return the 5 most similar results.
        return_distance=True,       # Return the similarity distance.
        return_metadata=True,       # Return the metadata.
    ))

    print(f"\nRetrieval results ({len(result.vectors)} total):")
    for i, vector in enumerate(result.vectors, 1):
        print(f"\n  [{i}] key: {vector.get('key', 'N/A')}")
        if 'distance' in vector:
            print(f"      Distance: {vector['distance']:.6f}")
        if 'metadata' in vector:
            print(f"      Metadata: {vector['metadata']}")

    # Retrieval without filter conditions.
    print(f"\n" + "=" * 50)
    print(f"Performing vector retrieval (no filter conditions)...")
    result = client.query_vectors(oss_vectors.models.QueryVectorsRequest(
        bucket=vector_bucket_name,
        index_name=vector_index_name,
        query_vector={
            "float32": query_vector
        },
        top_k=5,
        return_distance=True,
        return_metadata=True,
    ))

    print(f"\nRetrieval results ({len(result.vectors)} total):")
    for i, vector in enumerate(result.vectors, 1):
        print(f"  [{i}] key: {vector.get('key', 'N/A')}, "
              f"Distance: {vector.get('distance', 'N/A')}")


if __name__ == "__main__":
    main()
`


### 4.2 Retrieve with filter conditions


While performing a vector similarity search, you can accurately filter results based on image metadata, such as `city` and `height`, to narrow the search scope. Vector search supports metadata filtering using operators such as `$in`, `$and`, and `$or`.


`python
# -*- coding: utf-8 -*-
"""
Example: Advanced vector query.

This example shows advanced usage of vector retrieval, including complex filter conditions and multiple query examples.

Prerequisites:
1. alibabacloud-oss-v2 and dashscope are installed.
2. Environment variables are set.
3. The Alibaba Cloud Model Studio API key is set: export DASHSCOPE_API_KEY=<Your_API_Key>
4. Vector data is written.
"""

import os
import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors
import dashscope
from dashscope import MultiModalEmbeddingItemText


def embedding(text: str) -> list[float]:
    """Vectorize text to convert a query text into a vector for text-to-image search."""
    return dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        input=[MultiModalEmbeddingItemText(text=text, factor=1.0)]
    ).output["embeddings"][0]["embedding"]


def create_client():
    """Create an OSS Vector client."""
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')
    account_id = os.environ.get('oss_test_account_id')

    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(
        access_key_id, access_key_secret
    )
    cfg.region = region
    cfg.account_id = account_id
    return oss_vectors.Client(cfg)


def query_with_filter(client, bucket, index, query_text, filter_body, top_k=5):
    """Perform vector retrieval with filter conditions."""
    result = client.query_vectors(oss_vectors.models.QueryVectorsRequest(
        bucket=bucket,
        index_name=index,
        query_vector={"float32": embedding(query_text)},
        filter=filter_body,
        top_k=top_k,
        return_distance=True,
        return_metadata=True,
    ))
    return result.vectors


def main():
    client = create_client()

    vector_bucket_name = "my-test-2"
    vector_index_name = "test1"

    print("=" * 60)
    print("Advanced vector retrieval examples")
    print("=" * 60)

    # Example 1: $in operator - Match multiple cities.
    print("\n[Example 1] Use the $in operator - Query for images in Hangzhou or Shanghai")
    print("-" * 40)
    filter_in = {
        "city": {"$in": ["hangzhou", "shanghai"]}
    }
    results = query_with_filter(client, vector_bucket_name, vector_index_name,
                                "cityscape", filter_in)
    print(f"Query: 'cityscape', Filter: city in ['hangzhou', 'shanghai']")
    print(f"Number of results: {len(results)}")
    for v in results[:3]:
        print(f"  - {v.get('key')}: {v.get('metadata', {}).get('city', 'N/A')}")

    # Example 2: $and operator - Combine multiple conditions.
    print("\n[Example 2] Use the $and operator - Combine multiple filter conditions")
    print("-" * 40)
    filter_and = {
        "$and": [
            {"city": {"$in": ["hangzhou", "shanghai"]}},
            {"height": {"$in": ["1024"]}}
        ]
    }
    results = query_with_filter(client, vector_bucket_name, vector_index_name,
                                "skyscrapers", filter_and)
    print(f"Query: 'skyscrapers', Filter: city in [hangzhou, shanghai] AND height=1024")
    print(f"Number of results: {len(results)}")
    for v in results[:3]:
        meta = v.get('metadata', {})
        print(f"  - {v.get('key')}: city={meta.get('city')}, height={meta.get('height')}")

    # Example 3: Comparison of different query texts.
    print("\n[Example 3] Semantic retrieval effects of different query texts")
    print("-" * 40)
    query_texts = ["dog", "sunset by the sea", "city night view", "food"]

    for qt in query_texts:
        results = query_with_filter(client, vector_bucket_name, vector_index_name,
                                    qt, None, top_k=3)
        print(f"\nQuery: '{qt}'")
        for i, v in enumerate(results, 1):
            print(f"  [{i}] {v.get('key')}, Distance: {v.get('distance', 0):.4f}")


if __name__ == "__main__":
    main()
`


Filter condition description:




















| Operator | Description | Example |
| --- | --- | --- |
| $in | Included in the list. | {"city": {"$in": ["hangzhou", "beijing"]}} |
| $and | Logical AND. | {"$and": [condition1, condition2]} |
| $or | Logical OR. | {"$or": [condition1, condition2]} |


Complex filter example:


`json
{
    "$and": [
        {"city": {"$in": ["hangzhou", "shanghai"]}},
        {
            "$or": [
                {"height": "1024"},
                {"height": "768"}
            ]
        }
    ]
}
`


### 4.3 Build a visual retrieval interface


To visually demonstrate the retrieval results, you can use Gradio to build a simple web interface. This interface provides interactive retrieval with text input, filter conditions, and a display of the resulting images.


-

Install the web UI framework.


`shell
pip install gradio==5.44.1
`


-

Save the following code as `gradio_app.py`.


`python
# -*- coding: utf-8 -*-

import json
import logging
import os

import alibabacloud_oss_v2 as oss
import alibabacloud_oss_v2.vectors as oss_vectors
import dashscope
import gradio as gr
from PIL import Image
from dashscope import MultiModalEmbeddingItemText

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class Util:
    access_key_id = os.environ.get('oss_test_access_key_id')
    access_key_secret = os.environ.get('oss_test_access_key_secret')
    region = os.environ.get('oss_test_region')
    account_id = os.environ.get('oss_test_account_id')

    cfg = oss.config.load_default()
    cfg.credentials_provider = oss.credentials.StaticCredentialsProvider(access_key_id, access_key_secret)
    cfg.region = region
    cfg.account_id = account_id
    client = oss_vectors.Client(cfg)

    vector_bucket_name = "my-test-2"
    vector_index_name = "test1"
    dimension = 1024

    @staticmethod
    def embedding(text) -> list[float]:
        return dashscope.MultiModalEmbedding.call(
            model="multimodal-embedding-v1",
            input=[MultiModalEmbeddingItemText(text=text, factor=1.0)]
        ).output["embeddings"][0]["embedding"]

    @staticmethod
    def query_text(text: str, top_k: int = 5, city: list[str] = None, height: list[str] = None, return_meta: bool = True, return_distance: bool = True) -> list[tuple[Image.Image, str]]:
        logger.info(f"search text:{text}, top_k:{top_k}, city:{city}, height:{height}")

        sub_filter = if city is not None and len(city) > 0:
            sub_filter.append({"city": {"$in": city}})
        if height is not None and len(height) > 0:
            sub_filter.append({"height": {"$in": height}})
        if len(sub_filter) > 0:
            filter_body = {"$and": sub_filter}
        else:
            filter_body = None

        result = Util.client.query_vectors(oss_vectors.models.QueryVectorsRequest(
            bucket=Util.vector_bucket_name,
            index_name=Util.vector_index_name,
            query_vector={
                "float32": Util.embedding(text)
            },
            filter=filter_body,
            top_k=top_k,
            return_distance=return_distance,
            return_metadata=return_meta,
        ))

        gallery_data = current_dir = os.path.dirname(os.path.abspath(__file__))
        # The frontend display depends on local image files. Make sure that image resources are prepared according to the repository structure:
        # - By default, images from the data/photograph/ directory in the repository at the end of this topic are used. The frontend reads and displays these files.
        # - To use your own images, place them in another directory and modify the path below to point to that directory.
        for vector in result.vectors:
            file_path = os.path.join(current_dir, "data/photograph/", vector["key"])
            img = Image.open(file_path)
            gallery_data.append((img, json.dumps(vector)))
        ret = gallery_data
        logger.info(f"search text:{text}, top_k:{top_k}, request_id:{result.request_id}, ret:{ret}")
        return ret

    @staticmethod
    def on_gallery_box_select(evt: gr.SelectData):
        result = ""
        img_data = evt.value["caption"]
        img_data = json.loads(img_data)
        for key in img_data:
            img_data_item = img_data[key]
            if type(img_data_item) is str:
                img_data_item = img_data_item.replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r")
            if type(img_data_item) is dict:
                for sub_key in img_data_item:
                    img_data_item[sub_key] = img_data_item[sub_key].replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r")
                    result += f' - {sub_key}: &nbsp; {img_data_item[sub_key]}\r\n'
                continue
            result += f' - {key}: &nbsp; {img_data_item}\r\n'
        return result


with gr.Blocks(title="OSS Demo") as demo:
    with gr.Tab("OSS QueryVector Image Example") as search_tab:
        with gr.Row():
            query_text_box = gr.Textbox(label='query_text', interactive=True, value="dog")
            top_k_box = gr.Slider(minimum=1, maximum=30, value=10, step=1, label='top_k', interactive=True)
            with gr.Column():
                return_meta_box = gr.Checkbox(label='return_meta', interactive=True, value=True)
                return_distance_box = gr.Checkbox(label='return_distance', interactive=True, value=True)
        with gr.Row():
            city_box = gr.Dropdown(label='city', multiselect=True, choices=["hangzhou", "shanghai", "beijing", "shenzhen", "guangzhou"])
            height_box = gr.Dropdown(label='height', multiselect=True, choices=["1024", "683", "768", "576"])
        with gr.Row():
            query_button = gr.Button(value="query", variant='primary')
        with gr.Row():
            with gr.Column(scale=8):
                gallery_box = gr.Gallery(columns=5, show_label=False, preview=False, allow_preview=False, visible=True, show_download_button=False)
            with gr.Column(scale=2):
                with gr.Row(variant="panel"):
                    md_box = gr.Markdown(visible=True, elem_classes="image_detail")
            gallery_box.select(Util.on_gallery_box_select, , [md_box])
        query_button.click(
            Util.query_text,
            inputs=[
                query_text_box,
                top_k_box,
                city_box,
                height_box,
                return_meta_box,
                return_distance_box
            ],
            outputs=[
                gallery_box,
            ],
            concurrency_limit=1,
        )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
`


-

Start the interface.


`bash
python gradio_app.py
`


After the application starts, you can access `http://localhost:7860` to use the retrieval interface. Retrieval example: If you enter "dog", the interface returns images that contain dogs.








| Feature | Description |
| --- | --- |
| query_text | Enter a natural language description, such as "dog" or "mountain peak". |
| top_k | Set the number of results to return (1-30). |
| city | Filter by city. Multiple selections are supported. |
| height | Filter by image height. Multiple selections are supported. |
| return_meta | Specifies whether to return metadata information. |
| return_distance | Specifies whether to return the similarity distance. |


## References


For the complete project used in this tutorial, see [https://github.com/aliyun/alibabacloud-oss-vector-index-demo](https://github.com/aliyun/alibabacloud-oss-vector-index-demo).

Thank you! We've received your  feedback.