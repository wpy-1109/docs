# Use the OSS Vectors Embed CLI to write and retrieve vector data

The OSS Vectors Embed command-line interface (CLI) provides an easy way to call Alibaba Cloud Model Studio vector models. You can use the CLI to vectorize source files from OSS or your local machine and write the results to an OSS vector bucket. The CLI also supports multimodal semantic search, which simplifies the development of AI applications, such as retrieval-augmented generation (RAG) knowledge bases, AI assistants, and multimodal semantic search. The core capabilities include the following:


-

Seamless integration: Easily call the Alibaba Cloud Model Studio service to vectorize data.

-

Multiple input sources: Vectorize various data formats, such as local files, OSS objects, third-party file URLs, or text strings.

-

Flexible processing: Process single files or perform batch vectorization on files in a specific path.

-

Deep customization: Flexibly set vector key values and scalar metadata.

-

Multimodal search: Supports semantic similarity search by text, image, or video to empower diverse business scenarios.
The Alibaba Cloud OSS Vectors Embed CLI is currently in preview. Some tool parameters may change.
## Prerequisites


Before you use the CLI, prepare the following access credentials:


-

[Activate the OSS service](https://oss.console.alibabacloud.com/overview) and [obtain an AccessKey ID and an AccessKey secret](https://www.alibabacloud.com/help/en/ram/user-guide/create-an-accesskey-pair).

-

[Activate the Alibaba Cloud Model Studio service](https://modelstudio.console.alibabacloud.com/) and [obtain an API key](https://www.alibabacloud.com/help/en/model-studio/get-api-key).

### Configure access credentials


Configure your access credentials as environment variables. The CLI automatically reads these variables during execution. Therefore, you do not need to provide them in each command.


`bash
# Alibaba Cloud account AccessKey
export OSS_ACCESS_KEY_ID="<your-access-key-id>"
export OSS_ACCESS_KEY_SECRET="<your-access-key-secret>"

# Model Studio API key
export DASHSCOPE_API_KEY="<your-dashscope-api-key>"
`

Security tip: Do not hard-code credentials in scripts. Use environment variables instead.
### Install the OSS Vectors Embed CLI
Python 3.9 or later is required.
#### Method 1: Install using pip (recommended)


`bash
pip install oss-vectors-embed-cli
`


#### Method 2: Install in developer mode


`bash
git clone https://github.com/aliyun/oss-vectors-embed-cli.git
cd oss-vectors-embed-cli
pip install -e .
`


#### Verify the installation


`bash
oss-vectors-embed --version
# Output: oss-vectors-embed, version 0.1.0
`


### Create vector storage resources


Before you write vector data, you must create a vector bucket and configure an index:


-

Create a vector bucket: On the [Vector Bucket](https://oss.console.alibabacloud.com/vector-bucket-list) page, create a vector bucket to store vector data and indexes.

-

Create a vector index: In the vector bucket that you created, create an index and configure vector dimensions that match the vector model.
Important: The dimensions of the vector index must match the output dimensions of the [vector model] you use. For example, if you use the `text-embedding-v4` model (which defaults to 1024 dimensions), set the index dimensions to 1024.
## Write vectors


The `put` command generates vector embeddings from input data and stores them in an OSS vector index. Each file is processed into a separate embedding. Automatic chunking for long documents is not currently supported.

### Write text


Use a [text embedding model], such as `text-embedding-v4`, to process text.

#### Enter text directly


You can enter text directly from the command line to generate a vector:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Artificial intelligence is changing the way we live"
`


The following sample output includes the vector key, bucket information, and metadata:


`json
{
  "key": "3d8935dd-6395-4c9c-a501-df902846ec80",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-CONTENT": "Artificial intelligence is changing the way we live",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
    "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
  }
}
`


Note: The CLI automatically adds source information fields (`OSS-VECTORS-EMBED-SRC-*`) to the metadata to trace the source of the vector.

#### Read a local text file


You can write to a local file to generate vectors:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text "./documents/article.txt"
`


The following is a sample command output:


`json
{
  "key": "415c108e-d653-4d54-a241-d3b70e996666",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-CONTENT": "Artificial intelligence is changing the way we live. From being gently woken up by a smart alarm clock based on our sleep cycle in the morning, to having a voice assistant plan the best route for our commute; from a smart speaker at home playing personalized news summaries, to AI tools at work automatically generating reports, translating documents, and optimizing workflows—AI has quietly integrated into every corner of our daily lives.",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
    "OSS-VECTORS-EMBED-SRC-LOCATION": "./documents/article.txt"
  }
}
`


#### Read an OSS object


You can directly write an object that is stored in OSS. The path format is `oss://bucket-name/object-key`:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --region cn-hangzhou \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text "oss://source-bucket/documents/file.txt"
`


Note: Use the `--region` parameter to specify the region of the source OSS object.


Sample command output:


`json
{
  "key": "7ca24758-0d5b-46fe-ab90-db82be387650",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-CONTENT": "This is a example file.",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
    "OSS-VECTORS-EMBED-SRC-LOCATION": "oss://source-bucket/documents/file.txt"
  }
}
`


### Write images


Use a [multimodal embedding model], such as `qwen2.5-vl-embedding`, to process images and videos. Input sources can be local files, OSS objects, or HTTP/HTTPS URLs.

#### Read a local image


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id qwen2.5-vl-embedding \
  --image "./images/photo.jpg"
`


Sample command output:


`json
{
  "key": "8fc8105b-d54f-464c-bf44-97b088d566ce",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "qwen2.5-vl-embedding",
  "contentType": "image",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-LOCATION": "./images/photo.jpg",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "IMAGE"
  }
}
`


#### Read an OSS object


You can directly write an image object that is stored in OSS. The path format is `oss://bucket-name/object-key`:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --region cn-hangzhou \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id qwen2.5-vl-embedding \
  --image "oss://source-bucket/photo.jpg"
`


Sample command output:


`json
{
  "key": "dbf57dfd-58be-4793-a484-a82eb86e0e08",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "qwen2.5-vl-embedding",
  "contentType": "image",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-LOCATION": "oss://source-bucket/photo.jpg",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "IMAGE"
  }
}
`


#### Read an image URL


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id qwen2.5-vl-embedding \
  --image "https://example.com/photo.jpg"
`


Sample command output:


`json
{
  "key": "f15cfe75-d4de-497f-b441-3b08243cfa5e",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "qwen2.5-vl-embedding",
  "contentType": "image",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-LOCATION": "https://example.com/photo.jpg",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "IMAGE"
  }
}
`


### Write videos


Use a [multimodal embedding model], such as `qwen2.5-vl-embedding`, to process images and videos. The input source must be an HTTP/HTTPS URL. Directly processing local video files is not supported.

#### Read a video URL


Video processing extracts keyframes from the video and generates a separate vector for each frame. Each vector requires a unique key. Therefore, the `--key` and `--filename-as-key` parameters are not supported. The CLI automatically generates unique sequential keys for each frame.


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id qwen2.5-vl-embedding \
  --video "https://example.com/video.mp4"
`


Sample command output:


`json
{
  "key": "9157d87b-c44b-4c53-aceb-cd4be7fd8bd9",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "qwen2.5-vl-embedding",
  "contentType": "video",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-LOCATION": "https://example.com/video.mp4",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "VIDEO"
  }
}
`


### Add metadata


You can attach custom metadata during the write operation for later use in precise filtered queries.


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Technical document content" \
  --metadata '{"category": "technology", "version": "1.0", "author": "admin"}'
`


User-defined metadata fields are merged and stored with the fields automatically added by the system.


Sample command output:


`json
{
  "key": "c0ed4d9d-5301-49a5-82b7-eaf9d02b04a9",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "embeddingDimensions": 1024,
  "metadata": {
    "category": "technology",
    "version": "1.0",
    "author": "admin",
    "OSS-VECTORS-EMBED-SRC-CONTENT": "Technical document content",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
    "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
  }
}
`


## Retrieve vectors


The `query` command performs a similarity search. It first vectorizes the query content (text or image) and then finds the most semantically similar vectors in the vector index.
Important: The vector model used for the query must be the same as the model used for the indexed data.
### Text similarity search


You can query for semantically similar vectors based on text. The `--top-k` parameter controls the number of results to return.


Run the following command to search the `my-index` index for vectors that are most semantically similar to "What is artificial intelligence".


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  query \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "What is artificial intelligence" \
  --top-k 10
`


The following sample query output includes the vector key and metadata:


`bash
{
  "results": [
    {
      "Key": "3d8935dd-6395-4c9c-a501-df902846ec80",
      "metadata": {
        "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
        "OSS-VECTORS-EMBED-SRC-CONTENT": "Artificial intelligence is changing the way we live",
        "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
      }
    },
    ...
  ],
  "summary": {
    "queryType": "text",
    "model": "text-embedding-v4",
    "index": "my-index",
    "resultsFound": 10,
    "queryDimensions": 1024
  }
}
`


Note: By default, the similarity distance is not returned. To retrieve it, add the `--return-distance` parameter.

### Metadata-filtered search


You can use the `--filter` parameter to filter results based on metadata. This narrows the search scope and provides more precise results.

#### Simple filtering


You can query for vectors where the `category` is `technology`:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  query \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Technical documentation" \
  --filter '{"category": {"$eq": "technology"}}' \
  --top-k 20 \
  --return-metadata
`


Note: The `--return-metadata` parameter returns the complete metadata in the results. This includes both user-defined fields and fields automatically added by the CLI.


Sample query output:


`bash
{
  "results": [
    {
      "Key": "fd91808c-8d7c-480e-a72b-2bfa7d313a80",
      "metadata": {
        "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
        "author": "admin",
        "category": "technology",
        "OSS-VECTORS-EMBED-SRC-CONTENT": "Technical document content",
        "version": "1.0",
        "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
      }
    },
    ...
  ],
  "summary": {
    "queryType": "text",
    "model": "text-embedding-v4",
    "index": "test1",
    "resultsFound": 4,
    "queryDimensions": 1024
  }
}
`


#### Combined filtering


You can combine multiple filter conditions for a query based on the [filter syntax].


AND query: Matches all conditions.


`bash
# AND: Both conditions must match
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  query \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "API Reference" \
  --filter '{"$and": [{"category": "documentation"}, {"version": "3.0"}]}' \
  --top-k 5

`


Sample query output:


`bash
{
  "results": [
  {
      "Key": "fd91808c-8d7c-480e-a72b-2bfa7d313a80",
      "metadata": {
        "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
        "author": "admin",
        "category": "technology",
        "OSS-VECTORS-EMBED-SRC-CONTENT": "API Reference",
        "version": "1.0",
        "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
      }
    },
    {
    ...
  ],
  "summary": {
    "queryType": "text",
    "model": "text-embedding-v4",
    "index": "my-index",
    "resultsFound": 5,
    "queryDimensions": 1024
  }
}
`


OR query: Matches any of the conditions.


`bash
# OR: Matches any condition
oss-vectors-embed \
  --account-id 1234567890123456 \
  --vectors-region cn-hangzhou \
  query \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Getting Started Guide" \
  --filter '{"$or": [{"category": "tutorial"}, {"category": "quickstart"}]}' \
  --top-k 5
`


Sample query output:


`bash
{
  "results": [
  {
      "Key": "fd91808c-8d7c-480e-a72b-2bfa7d313a80",
      "metadata": {
        "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
        "author": "admin",
        "category": "technology",
        "OSS-VECTORS-EMBED-SRC-CONTENT": "Getting Started Guide",
        "version": "1.0",
        "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
      }
    },
    {
    ...
  ],
  "summary": {
    "queryType": "text",
    "model": "text-embedding-v4",
    "index": "my-index",
    "resultsFound": 5,
    "queryDimensions": 1024
  }
}
`


### Multimodal search


Multimodal search supports both text and image queries on the same vector collection. This enables scenarios such as text-to-image search (finding images similar to a text description) or search by image (finding images that match a given image).


`bash
oss-vectors-embed \
  --account-id 1234567890123456 \
  --vectors-region cn-hangzhou \
  query \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id qwen2.5-vl-embedding \
  --image "./query-images/similar-product.jpg" \
  --top-k 10
`


Sample query output:


`bash
{
  "results": [
    {
      "Key": "11dcf66b-708a-4707-8bd4-8656bead19da",
      "metadata": {
        "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "IMAGE",
        "OSS-VECTORS-EMBED-SRC-LOCATION": "similar-product.png"
      }
    },
    {
    ...
  ],
  "summary": {
    "queryType": "image",
    "model": "qwen2.5-vl-embedding",
    "index": "my-index",
    "resultsFound": 10,
    "queryDimensions": 1024
  }
}
`


### Table output format


You can use the `--output table` parameter to convert the default JSON output to a table format. This format is easier for manual reading, interactive exploration, and debugging.


`bash
oss-vectors-embed \
--account-id <your-account-id> \
--vectors-region cn-hangzhou \
query \
--vector-bucket-name my-vector-bucket \
--index-name my-index \
--model-id text-embedding-v4 \
--text "./queries/user-question.txt" \
--top-k 3 \
--output table
`


Sample table output:


`line
                                 Query Results
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Rank ┃ Vector Key             ┃ Distance ┃ Metadata               ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1    │ doc:auth-setup         │ N/A      │ {"category": "docs"}   │
│ 2    │ doc:security-config    │ N/A      │ {"category": "docs"}   │
│ 3    │ doc:api-reference      │ N/A      │ {"category": "docs"}   │
└──────┴────────────────────────┴──────────┴────────────────────────┘
Query Summary:
  Model: text-embedding-v4
  Results Found: 3
  Query Dimensions: 1024
`


Note: The Distance column shows N/A because the command did not specify to return the distance value. To display the distance, add the `--return-distance` parameter to the command.

## Batch processing


The CLI supports batch processing for all files in a directory using wildcard characters. In batch mode, the CLI automatically sends parallel requests to improve processing efficiency.

### Batch process local files


You can process all text files in a local directory:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text "./documents/*.txt" \
  --filename-as-key
`


The following sample output shows that unlike single-file processing, batch processing returns a summary of the operation:


`json
{
  "type": "streaming_batch",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "totalFiles": 5,
  "processedFiles": 5,
  "failedFiles": 0,
  "totalVectors": 5,
  "vectorKeys": [
    "doc1.txt",
    "doc2.txt",
    "doc3.txt",
    "doc4.txt",
    "doc5.txt"
  ]
}
`


During processing, progress indicators are displayed, such as `Processing chunk 1...` and `STORED BATCH: 5 vectors`.

### Batch process OSS files


You can use wildcard characters to batch process all files under a specific prefix in an OSS bucket.


`bash
oss-vectors-embed \
  --account-id 1234567890123456 \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text "oss://bucket/path/*"
`


Sample output:


`json
{
  "type": "streaming_batch",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "totalFiles": 2,
  "processedFiles": 2,
  "failedFiles": 0,
  "totalVectors": 2,
  "vectorKeys": [
    "1001dfcb-1e78-450b-8526-a9c92fa308c6",
    "b6aa1da0-adc7-489e-83e2-e39ff2e1fb9d"
  ]
}
`


### Control concurrency


The `--max-workers` parameter controls the number of concurrent requests. The default value is 4. Increasing this value can improve throughput but consumes more API quota.


`bash
oss-vectors-embed \
  --account-id 1234567890123456 \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text "./documents/*.txt" \
  --max-workers 8
`


Sample output:


`json
{
  "type": "streaming_batch",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "totalFiles": 8,
  "processedFiles": 8,
  "failedFiles": 0,
  "totalVectors": 8,
  "vectorKeys": [
    "doc1.txt",
    "doc2.txt",
    "doc3.txt",
    "doc4.txt",
    "doc5.txt",
    "doc6.txt",
    "doc7.txt",
    "doc8.txt"
  ]
}
`


## Customize vector keys

### Use a custom key


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Document content" \
  --key "doc-001"
`


Sample output:


`json
{
 "key": "doc-001",
 "bucket": "my-test-2",
 "index": "test1",
 "model": "text-embedding-v4",
 "contentType": "text",
 "embeddingDimensions": 1024,
 "metadata": {
   "OSS-VECTORS-EMBED-SRC-CONTENT": "Document content",
   "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
   "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
 }
}
`


### Use the filename as the key


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text "article.txt" \
  --filename-as-key
`


Sample output:


`json
{
  "key": "article.txt",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-CONTENT": "Artificial intelligence is changing the way we live. From being gently woken up by a smart alarm clock based on our sleep cycle in the morning, to having a voice assistant plan the best route for our commute; from a smart speaker at home playing personalized news summaries, to AI tools at work automatically generating reports, translating documents, and optimizing workflows—AI has quietly integrated into every corner of our daily lives.",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
    "OSS-VECTORS-EMBED-SRC-LOCATION": "article.txt"
  }
}
`


### Add a key prefix


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Document content" \
  --key "doc-001" \
  --key-prefix "project-a/"
`


Sample output:


`json
{
  "key": "project-a/doc-001",
  "bucket": "my-vector-bucket",
  "index": "my-index",
  "model": "text-embedding-v4",
  "contentType": "text",
  "embeddingDimensions": 1024,
  "metadata": {
    "OSS-VECTORS-EMBED-SRC-CONTENT": "Document content",
    "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
    "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
  }
}
`


## Customize model parameters


The `--dashscope-inference-params` parameter lets you fine-tune the behavior of the vector model to meet the needs of different business scenarios.

### Write using custom model parameters


When vectorizing data, you can specify parameters such as the output type and dimension:


`bash
oss-vectors-embed \
  --account-id <your-account-id> \
  --vectors-region cn-hangzhou \
  put \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id text-embedding-v4 \
  --text-value "Technical document content" \
  --dashscope-inference-params '{"output_type": "dense", "dimension": "1024"}'
`


Sample output:


`json
{
 "key": "73359c62-55a7-458a-a171-003755f3338e",
 "bucket": "my-vector-bucket",
 "index": "my-index",
 "model": "text-embedding-v4",
 "contentType": "text",
 "embeddingDimensions": 1024,
 "metadata": {
   "OSS-VECTORS-EMBED-SRC-CONTENT": "Document content",
   "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
   "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
 }
}
`


### Retrieve using custom model parameters


When retrieving vectors, you can control behaviors such as the text truncation policy:


`bash
oss-vectors-embed \
  --account-id 1234567890123456 \
  --vectors-region cn-hangzhou \
  query \
  --vector-bucket-name my-vector-bucket \
  --index-name my-index \
  --model-id qwen2.5-vl-embedding \
  --text-value "Technical documentation" \
  --dashscope-inference-params '{"truncate": "END"}' \
  --top-k 10
  --return-distance
`


Sample output:


`json
{
  "results": [
    {
      "Key": "3d8935dd-6395-4c9c-a501-df902846ec80",
      "metadata": {
        "OSS-VECTORS-EMBED-SRC-CONTENT-TYPE": "TEXT",
        "OSS-VECTORS-EMBED-SRC-CONTENT": "Technical documentation",
        "OSS-VECTORS-EMBED-SRC-LOCATION": "direct_text_input"
      }
    },
    ...
  ],
  "summary": {
    "queryType": "text",
    "model": "text-embedding-v4",
    "index": "my-index",
    "resultsFound": 10,
    "queryDimensions": 1024
  }
}
`


## Supported vector models

### Text embedding models











| Model ID | Default dimensions | Optional dimensions |
| --- | --- | --- |
| text-embedding-v4 | 1024 | 2048/1536/768/512/256/128/64 |
| text-embedding-v3 | 1024 | 768/512/256/128/64 |
| text-embedding-v2 | 1536 | - |
| text-embedding-v1 | 1536 | - |


### Multimodal embedding models











| Model ID | Dimensions | Supported input types |
| --- | --- | --- |
| qwen2.5-vl-embedding | 2048/1024/768/512 | Text, image, video, multiple images |
| tongyi-embedding-vision-plus | 1152 | Text, image, video, multiple images |
| tongyi-embedding-vision-flash | 768 | Text, image, video, multiple images |
| multimodal-embedding-v1 | 1024 | Text, image, video |


Model selection recommendations:


-

For text-only scenarios, use text-embedding-v4.

-

For mixed text and image scenarios, use qwen2.5-vl-embedding.

-

For high-speed processing, use tongyi-embedding-vision-flash.

## Parameter descriptions

### Global parameters


























| Parameter | Required | Description |
| --- | --- | --- |
| --account-id | Yes | Your Alibaba Cloud account ID. |
| --vectors-region | Yes | The region where the vector bucket is located, for example, cn-hangzhou. |
| --vectors-endpoint | No | The endpoint of the vector bucket. |
| --debug | No | Enables debug mode. |


### put command parameters




















| Parameter | Required | Description |
| --- | --- | --- |
| --vector-bucket-name | Yes | The name of the vector bucket. |
| --index-name | Yes | The name of the vector index. |
| --model-id | Yes | The ID of the DashScope model used to generate vectors. |
| --text-value | No | The text content to process. You must specify one of --text-value, --text, --image, or --video. |
| --text | No | The path to the text file or OSS object to process. |
| --image | No | The path to the image file, OSS object, or URL to process. |
| --video | No | The URL of the video to process. |
| --key | No | Specifies a custom unique key for the vector. |
| --key-prefix | No | Adds a prefix to the automatically generated or specified key. |
| --filename-as-key | No | Uses the name of the input file as the vector key. |
| --dashscope-inference-params | No | Model-specific parameters passed to DashScope in JSON format, for example, '{"dimension": "1024"}'. |
| --metadata | No | Metadata specified in a JSON string. |
| --max-workers | No | The maximum number of concurrent requests for batch processing. Default: 4. |
| --batch-size | No | The number of vectors included in a single request during a batch write. Value range: 1 to 500. Default: 500. |
| --output | No | Specifies the output format. Valid values are json (default) and table. |
| --region | No | When the input source is an OSS object, specifies the region where the object is located. |


### query command parameters




















| Parameter | Required | Description |
| --- | --- | --- |
| --vector-bucket-name | Yes | The name of the vector bucket. |
| --index-name | Yes | The name of the vector index. |
| --model-id | Yes | The ID of the DashScope model used to generate vectors. |
| --text-value | No | The text content to query. |
| --text | No | The path to the file that contains the query text. |
| --image | No | The path to the image to query. |
| --video | No | The URL of the video to query. |
| --top-k | No | The number of most similar results to return. Default: 5. |
| --filter | No | Filter conditions specified in a JSON string. |
| --return-distance | No | Includes the similarity distance value in the results. |
| --return-metadata | No | Includes metadata in the results. Enabled by default. |
| --dashscope-inference-params | No | Model-specific parameters passed to DashScope in JSON format, for example, '{"truncate": "END"}'. |
| --output | No | Specifies the output format. Valid values are json (default) and table. |


### Filter syntax









































| Operator | Description | Example |
| --- | --- | --- |
| $eq | Equals | {"category": {"$eq": "docs"}} |
| $ne | Not equals | {"status": {"$ne": "deleted"}} |
| $in/$nin | In/Not in a list | {"tag": {"$in": ["a", "b"]}} |
| $and | Logical AND | {"$and": [{"a": 1}, {"b": 2}]} |
| $or | Logical OR | {"$or": [{"a": 1}, {"a": 2}]} |


## References


For more information about the OSS Vectors Embed CLI, see the [GitHub repository](https://github.com/aliyun/oss-vectors-embed-cli).


Thank you! We've received your  feedback.