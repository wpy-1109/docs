# SelectObject Best Practices: Query CSV and JSON in OSS

Source: https://help.aliyun.com/zh/oss/use-cases/call-selectobject-to-query-csv-and-json-objects-in-a-bucket-by-using-oss-sdk-for-java
Source: https://help.aliyun.com/zh/oss/use-cases/call-selectobject-to-query-csv-and-json-objects-in-a-bucket-by-using-oss-sdk-for-python

## Overview

OSS SelectObject allows you to run SQL-like queries directly on CSV and JSON objects stored in OSS. Instead of downloading entire objects and processing locally, you can push query execution to the server side, significantly reducing data transfer and processing time.

## Supported Formats

- **CSV**: Comma-separated values with configurable delimiters
- **JSON**: Both JSON Lines (one JSON object per line) and standard JSON documents
- **Parquet**: (via integration with Data Lake Analytics)

## SQL Syntax

### Basic Query Structure
```sql
SELECT column_name FROM ossobject WHERE condition
```

### CSV Column Reference
CSV columns are referenced as `_1`, `_2`, `_3`, etc. (1-indexed):
```sql
SELECT _1, _3 FROM ossobject WHERE _2 > 100
```

Or with header row:
```sql
SELECT name, age FROM ossobject WHERE age > 25
```

### JSON Column Reference
JSON fields are referenced using dot notation:
```sql
SELECT s.name, s.age FROM ossobject s WHERE s.age > 25
```

### Supported SQL Operators
- Comparison: `=`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `AND`, `OR`, `NOT`
- Pattern: `LIKE`, `IN`
- Aggregation: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- String: `CAST()`, `TRIM()`, `SUBSTRING()`
- Null check: `IS NULL`, `IS NOT NULL`

## Java SDK Example

```java
import com.aliyun.oss.*;
import com.aliyun.oss.model.*;
import java.io.*;

public class SelectObjectExample {
    public static void main(String[] args) {
        String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
        String bucketName = "example-bucket";
        String objectKey = "data/sales.csv";

        OSS ossClient = new OSSClientBuilder().build(endpoint,
            System.getenv("ACCESS_KEY_ID"),
            System.getenv("ACCESS_KEY_SECRET"));

        try {
            // Create select request
            SelectObjectRequest request = new SelectObjectRequest(bucketName, objectKey);

            // Set SQL expression
            String sql = "SELECT _1, _3, _5 FROM ossobject WHERE _3 > 1000";
            request.setExpression(sql);

            // Configure input format (CSV)
            InputSerialization inputSerialization = new InputSerialization();
            inputSerialization.setCsvInputFormat(new CSVFormat());
            inputSerialization.setCompressionType(CompressionType.NONE);
            request.setInputSerialization(inputSerialization);

            // Configure output format
            OutputSerialization outputSerialization = new OutputSerialization();
            outputSerialization.setCsvOutputFormat(new CSVFormat());
            request.setOutputSerialization(outputSerialization);

            // Execute query
            OSSObject result = ossClient.selectObject(request);

            // Read results
            BufferedReader reader = new BufferedReader(
                new InputStreamReader(result.getObjectContent()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            result.close();
        } finally {
            ossClient.shutdown();
        }
    }
}
```

## Python SDK Example

```python
import oss2
import os

auth = oss2.Auth(
    os.getenv('ACCESS_KEY_ID'),
    os.getenv('ACCESS_KEY_SECRET')
)
bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'example-bucket')

# Query CSV file
sql = "SELECT _1, _3, _5 FROM ossobject WHERE CAST(_3 AS INT) > 1000"

# Configure input/output format
input_format = {
    'CsvInput': {
        'FileHeaderInfo': 'Use',
        'RecordDelimiter': '\n',
        'FieldDelimiter': ','
    }
}
output_format = {
    'CsvOutput': {
        'RecordDelimiter': '\n',
        'FieldDelimiter': ','
    }
}

result = bucket.select_object('data/sales.csv', sql,
    select_params={
        'InputSerialization': input_format,
        'OutputSerialization': output_format
    })

# Read results
content = result.read().decode('utf-8')
print(content)
```

## JSON Query Example

```python
# Query JSON Lines file
sql = "SELECT s.name, s.total FROM ossobject s WHERE s.total > 1000"

input_format = {
    'JsonInput': {
        'Type': 'LINES'  # or 'DOCUMENT' for standard JSON
    }
}
output_format = {
    'JsonOutput': {
        'RecordDelimiter': '\n'
    }
}

result = bucket.select_object('data/orders.json', sql,
    select_params={
        'InputSerialization': input_format,
        'OutputSerialization': output_format
    })
```

## Performance Considerations

### When to Use SelectObject
- **Good for**: Filtering large datasets to retrieve small subsets
- **Good for**: Aggregation queries on large files
- **Not ideal for**: Retrieving most of the data (download is faster)
- **Not ideal for**: Complex joins or multi-file queries (use Data Lake Analytics)

### Optimization Tips
- Use **specific column selection** instead of `SELECT *`
- Apply **WHERE filters** to reduce returned data
- Use **CAST()** for type-specific comparisons
- Consider **splitting large files** into smaller, well-partitioned files
- Use **compressed formats** (GZIP) for large CSV files

### Limitations
- Maximum object size: 256 GB
- Maximum SQL expression length: 256 KB
- Maximum columns: 1,000
- Maximum nested JSON depth: 5 levels
- No support for JOIN operations
- No support for ORDER BY or GROUP BY (in basic SelectObject)
