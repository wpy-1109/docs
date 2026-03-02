# Query objects

You can call the SelectObject operation to execute SQL statements on an object and obtain the execution results.

## Background information


You can directly process data in Object Storage Service (OSS) when you run Hadoop 3.0 or use services such as Spark, Hive, and Presto on E-MapReduce (EMR). Alibaba Cloud services, such as MaxCompute and Data Lake Analytics (DLA), are also supported in OSS.


The GetObject operation that is provided by OSS requires a big data platform to download OSS objects to your local computer for analysis and filtering. As a result, large amounts of bandwidth and client resources are wasted in many query scenarios.


The SelectObject operation is used to address this issue. The SelectObject operation allows OSS to preliminarily filter data by using conditions and projections that are provided by the big data platform. As a result, only useful data is returned to the big data platform. This way, the client can consume fewer bandwidth resources and process smaller amounts of data to minimize CPU utilization and memory usage. This makes OSS-based data warehousing and data analytics more suitable for your business requirements.

## Billing rules


You are charged based on the size of the objects that are scanned when you call the SelectObject operation. For more information, see [Data processing fees](https://www.alibabacloud.com/help/en/oss/data-processing-fees#concept-2558464).

## Supported object types


This section describes the object types that are supported by the SelectObject operation.


-

CSV objects (and CSV-like objects such as TSV objects) that conform to RFC 4180. You can specify custom row and column delimiters and quote characters in CSV objects.

-

UTF-8 encoded JSON objects. The SelectObject operation supports JSON objects in the DOCUMENT and LINES formats.


-

A JSON DOCUMENT object contains a single object.

-

A JSON LINES object consists of lines of objects that are separated by line feeds. However, the entire object is not a valid JSON object. SelectObject supports common delimiters, such as \n and \r\n. You do not need to specify the delimiters.

-

Standard and Infrequent Access (IA) objects. Archive, Cold Archive, and Deep Cold Archive objects must be restored before the SelectObject operation is called on the objects.

-

Objects that are fully managed and encrypted by OSS or encrypted by using customer master keys (CMKs) that are managed by Key Management Service (KMS).

## Supported SQL syntax


-

SQL statement: SELECT FROM WHERE

-

Data types: string, int(64bit), double(64bit), decimal(128bit), timestamp, and bool.

-

Operators: logical operators (AND, OR, and NOT), arithmetic operators (+, -, *, /, and %), comparison operators (>, =, <, >=, <=, and !=), and string operators (LIKE and ||).


> NOTE:

> NOTE: 


> NOTE: Important 

LIKE-based fuzzy matches are case-sensitive.


## Supported data types


By default, CSV data in OSS is of the String type. You can use the CAST function to convert the data type.


The following sample SQL statement is used to convert the data in the first and second columns into data of the Integer type: `Select * from OSSOBject where cast (_1 as int) > cast(_2 as int)`.


The SelectObject operation allows you to implicitly convert the data type by using a WHERE clause. For example, the following SQL statement converts the data in the first and second columns into data of the Integer type:


`Select _1 from ossobject where _1 + _2 > 100`


If you do not use the CAST function, the type of data in a JSON object remains unchanged. A standard JSON object can support various data types, including Null, Bool, Int64, Double, and String.

## Sample SQL statements


SQL statement examples are provided for CSV and JSON objects.


-

CSV








| Scenario | SQL statement |
| --- | --- |
| Return the first 10 rows. | select * from ossobject limit 10 |
| Return integers in the first and third columns. The integer values in the first column are greater than the integer values in the third column. | select _1, _3 from ossobject where cast(_1 as int) > cast(_3 as int) |
| Return the number of records in which the data in the first column starts with X. A Chinese character that is specified after LIKE must be UTF-8 encoded. | select count(*) from ossobject where _1 like 'X%' |
| Return all records in which the time value in the second column is later than 2018-08-09 11:30:25 and the value in the third column is greater than 200. | select * from ossobject where _2 > cast('2018-08-09 11:30:25' as timestamp) and _3 > 200 |
| Return the average value, sum, maximum value, and minimum value of the floating-point numbers in the second column. | select AVG(cast(_6 as double)), SUM(cast(_6 as double)), MAX(cast(_6 as double)), MIN(cast(_6 as double)) from ossobject |
| Return all records in which the strings that are concatenated by the data in the first and third columns start with Tom and end with Anderson. | select * from ossobject where (_1 || _3) like 'Tom%Anderson' |
| Return all records in which the value in the first column is divisible by 3. | select * from ossobject where (_1 % 3) = 0 |
| Return all records in which the value in the first column is between 1995 and 2012. | select * from ossobject where _1 between 1995 and 2012 |
| Return all records in which the value in the fifth column is N, M, G, or L. | select * from ossobject where _5 in ('N', 'M', 'G', 'L') |
| Return all records in which the product of the values in the second and third columns is greater than the sum of 100 and the value in the fifth column. | select * from ossobject where _2 * _3 > _5 + 100 |


-

JSON


Sample JSON object:


`plaintext
{
  "contacts":[
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    },
    {
      "type": "mobile",
      "number": "123 456-7890"
    }
  ],
  "children": ,
  "spouse": null
}, …… # Other similar nodes are omitted.
]}
`


The following table describes the sample SQL statements for JSON objects.








> NOTE:

> NOTE: 


> NOTE: 


| Scenario | SQL statement |
| --- | --- |
| Return all records in which the value of age is 27. | select * from ossobject.contacts[*] s where s.age = 27 |
| Return all home phone numbers. | select s.number from ossobject.contacts[*].phoneNumbers[*] s where s.type = "home" |
| Return all records in which the value of spouse is null. | select * from ossobject s where s.spouse is null |
| Return all records in which the value of children is 0. | select * from ossobject s where s.children[0] is null Note The preceding statement is used to specify an empty array because no other methods are available. |


## Scenarios


In most cases, SelectObject is used for multipart query, query of JSON objects, and analysis of log objects.


-

Query large objects by using multipart query


The multipart query feature that is provided by the SelectObject operation is similar to the byte-based multipart download feature that is provided by the GetObject operation. Data is split into parts by row or by split.


-

By row: This method is used in most cases. However, unbalanced loads may occur when sparse data is split.

-

By split: A split includes multiple rows. Each split has approximately the same size.


> NOTE:

> NOTE: 


> NOTE: Note 

Dividing data by split is more efficient.


If columns in a CSV object do not include line feeds, you can divide the object into parts based on bytes. This method is simple because you do not need to create Meta for the object. If you want to query a JSON object or a CSV object in which columns include line feeds, perform the following steps:


-

Call the CreateSelectObjectMeta operation to obtain the total number of splits for the object. To reduce the scanning time, we recommend that you asynchronously call the SelectObject operation before you query the object.

-

Select the appropriate concurrency level (n) based on the resources on the client. Divide the total number of splits by the concurrency level (n) to obtain the number of splits in each query.

-

Configure the parameters in the request body to perform multipart query. For example, you can set split-range to 1-20.

-

Combine the results.

-

Query JSON objects


When you query a JSON object, narrow down the JSON path range in the FROM clause.


Sample JSON object:


`plaintext
{
  "contacts":[
{
  "firstName": "John",
  "lastName": "Smith",
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    },
    {
      "type": "mobile",
      "number": "123 456-7890"
    }
  ]
}
]}
`


To query all street addresses whose postal codes start with 10021, execute the following SQL statement: `select s.address.streetAddress from ossobject.contacts[*] s where s.address.postalCode like '10021%'` or `select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'`.


The SQL statement with the JSON path outperforms because the statement is more accurate when you execute `select s.streetAddress from ossobject.contacts[*].address s where s.postalCode like '10021%'`.

-

Process high-precision floating-point numbers in JSON objects


If you want to calculate high-precision floating-point numbers in a JSON object, we recommend that you set the ParseJsonNumberAsString parameter to true and use the CAST function to convert the parsed data to the Decimal type. For example, if the value of attribute a is 123456789.123456789, you can execute the `select s.a from ossobject s where cast(s.a as decimal) > 123456789.12345` statement to maintain the accuracy of attribute a.

## Procedure

### Use the OSS console


> NOTE:

> NOTE: 


> NOTE: Important 

You can select and obtain up to 40 MB of data from an object up to 128 MB in size in the OSS console.


-

Log on to the [OSS console](https://oss.console.alibabacloud.com/).

-

In the left-side navigation pane, click Buckets. On the Buckets page, find and click the desired bucket.

-

In the left-side navigation tree, choose Object Management > Objects.

-

On the right side of the target object, choose ![more ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/en-US/2197678661/p508856.jpg) > Select Content in the Actions column.

-

In the Select Content panel, configure the parameters. The following table describes the parameters.








| Parameter | Description |
| --- | --- |
| Object Type | Valid values: CSV and JSON. |
| Delimiter | This parameter is available only when Object Type is set to CSV. Valid values: , and Custom. |
| Title Row | This parameter is available only when Object Type is set to CSV. Specify whether the first row of the object contains column titles. |
| JSON Display Mode | This parameter is available only when Object Type is set to JSON. Valid values: JSON_LINES and JSON_DOCUMENT. |
| Compression Format | Select whether to compress the object. Only GZIP compression is supported. |


-

Click Preview. to preview the selected data.


> NOTE:

> NOTE: 


> NOTE: Important 

When you preview the selected data of a Standard object, you are charged data scanning fees incurred by the SelectObject operation. When you preview the selected data of an IA, Archive, Cold Archive, or Deep Cold Archive object, you are charged data scanning fees and data retrieval fees incurred by the SelectObject operation. For more information, see [Data processing fees](https://www.alibabacloud.com/help/en/oss/data-processing-fees#concept-2558464).


-

Click Next. Enter and execute an SQL statement.


For example, a CSV object named People contains the following columns: Name, Company, and Age.


-

To query people who are over 50 years old and whose names start with Lora, execute the following SQL statement. In the statement, _1, _2, and _3 specify column indexes. _1 specifies the index of the first column. _2 specifies the index of the second column. _3 specifies the index of the third column.


`plaintext
select * from ossobject where _1 like 'Lora*' and _3 > 50
`


-

To query the number of rows in the object, maximum age, and minimum age, execute the following SQL statement:


`plaintext
select count(*), max(cast(_3 as int)), min(cast(_3 as int)) from oss_object
`


-

View the execution results.


You can also click Download to download the selected content to your local computer.

### Use OSS SDKs


You can use only OSS SDK for Java and OSS SDK for Python to query objects.
Java

`java
import com.aliyun.oss.model.*;
import com.aliyun.oss.OSS;
import com.aliyun.oss.common.auth.*;
import com.aliyun.oss.OSSClientBuilder;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.InputStreamReader;

/
 * Examples of create select object metadata and select object.
 /
public class SelectObjectSample {
    // Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
    private static String endpoint = "https://oss-cn-hangzhou.aliyuncs.com";
    // Specify the name of the bucket. Example: examplebucket.
    private static String bucketName = "examplebucket";

    public static void main(Stringargs) throws Exception {

      	// Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
        EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider();
        // Specify the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the region to cn-hangzhou.
        String region = "cn-hangzhou";

        // Create an OSSClient instance.
        ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration();
        clientBuilderConfiguration.setSignatureVersion(SignVersion.V4);
        OSS ossClient = OSSClientBuilder.create()
        .endpoint(endpoint)
        .credentialsProvider(credentialsProvider)
        .clientConfiguration(clientBuilderConfiguration)
        .region(region)
        .build();
        // Specify the full path of the object that you want to query, and then query the data of the object by using SELECT statements. Do not include the bucket name in the full path.
        // Specify the full path of the CSV object.
        selectCsvSample("test.csv", ossClient);
        // Specify the full path of the JSON object.
        selectJsonSample("test.json", ossClient);
        ossClient.shutdown();
    }

    private static void selectCsvSample(String key, OSS ossClient) throws Exception {
        // Specify the content of the object that you want to upload.
        String content = "name,school,company,age\r\n" +
                "Lora Francis,School A,Staples Inc,27\r\n" +
                "Eleanor Little,School B,\"Conectiv, Inc\",43\r\n" +
                "Rosie Hughes,School C,Western Gas Resources Inc,44\r\n" +
                "Lawrence Ross,School D,MetLife Inc.,24";

        ossClient.putObject(bucketName, key, new ByteArrayInputStream(content.getBytes()));

        SelectObjectMetadata selectObjectMetadata = ossClient.createSelectObjectMetadata(
                new CreateSelectObjectMetadataRequest(bucketName, key)
                        .withInputSerialization(
                                new InputSerialization().withCsvInputFormat(
                                        // Specify the delimiter that is used to separate different records in the content. Example: \r\n.
                                        new CSVFormat().withHeaderInfo(CSVFormat.Header.Use).withRecordDelimiter("\r\n"))));
        System.out.println(selectObjectMetadata.getCsvObjectMetadata().getTotalLines());
        System.out.println(selectObjectMetadata.getCsvObjectMetadata().getSplits());

        SelectObjectRequest selectObjectRequest =
                new SelectObjectRequest(bucketName, key)
                        .withInputSerialization(
                                new InputSerialization().withCsvInputFormat(
                                        new CSVFormat().withHeaderInfo(CSVFormat.Header.Use).withRecordDelimiter("\r\n")))
                        .withOutputSerialization(new OutputSerialization().withCsvOutputFormat(new CSVFormat()));
        // Use a SELECT statement to query all records whose values are greater than 40 in the 4th column.
        selectObjectRequest.setExpression("select * from ossobject where _4 > 40");
        OSSObject ossObject = ossClient.selectObject(selectObjectRequest);

        // Read the content of the object.
        BufferedReader reader = new BufferedReader(new InputStreamReader(ossObject.getObjectContent()));
        while (true) {
            String line = reader.readLine();
            if (line == null) {
                break;
            }
            System.out.println(line);
        }
        reader.close();

        ossClient.deleteObject(bucketName, key);
    }

    private static void selectJsonSample(String key, OSS ossClient) throws Exception {
        // Specify the content of the object that you want to upload.
        final String content = "{\n" +
                "\t\"name\": \"Lora Francis\",\n" +
                "\t\"age\": 27,\n" +
                "\t\"company\": \"Staples Inc\"\n" +
                "}\n" +
                "{\n" +
                "\t\"name\": \"Eleanor Little\",\n" +
                "\t\"age\": 43,\n" +
                "\t\"company\": \"Conectiv, Inc\"\n" +
                "}\n" +
                "{\n" +
                "\t\"name\": \"Rosie Hughes\",\n" +
                "\t\"age\": 44,\n" +
                "\t\"company\": \"Western Gas Resources Inc\"\n" +
                "}\n" +
                "{\n" +
                "\t\"name\": \"Lawrence Ross\",\n" +
                "\t\"age\": 24,\n" +
                "\t\"company\": \"MetLife Inc.\"\n" +
                "}";

        ossClient.putObject(bucketName, key, new ByteArrayInputStream(content.getBytes()));

        SelectObjectRequest selectObjectRequest =
                new SelectObjectRequest(bucketName, key)
                        .withInputSerialization(new InputSerialization()
                                .withCompressionType(CompressionType.NONE)
                                .withJsonInputFormat(new JsonFormat().withJsonType(JsonType.LINES)))
                        .withOutputSerialization(new OutputSerialization()
                                .withCrcEnabled(true)
                                .withJsonOutputFormat(new JsonFormat()))
                        .withExpression("select * from ossobject as s where s.age > 40"); // Use the SELECT statement to query data in the object.

        OSSObject ossObject = ossClient.selectObject(selectObjectRequest);

        // Read the content of the object.
        BufferedReader reader = new BufferedReader(new InputStreamReader(ossObject.getObjectContent()));
        while (true) {
            String line = reader.readLine();
            if (line == null) {
                break;
            }
            System.out.println(line);
        }
        reader.close();

        ossClient.deleteObject(bucketName, key);
    }
}
`

Python

`python
import oss2
from oss2.credentials import EnvironmentVariableCredentialsProvider

def select_call_back(consumed_bytes, total_bytes =  None):
        print('Consumed Bytes:' + str(consumed_bytes) + '\n')

# Obtain access credentials from environment variables. Before you run the sample code, make sure that the OSS_ACCESS_KEY_ID and OSS_ACCESS_KEY_SECRET environment variables are configured.
auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider())

# Specify the endpoint of the region in which the bucket is located. For example, if the bucket is located in the China (Hangzhou) region, set the endpoint to https://oss-cn-hangzhou.aliyuncs.com.
endpoint = "https://oss-cn-hangzhou.aliyuncs.com"

# Specify the ID of the region that maps to the endpoint. Example: cn-hangzhou. This parameter is required if you use the signature algorithm V4.
region = "cn-hangzhou"

# Specify the name of your bucket.
bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region)

key ='python_select.csv'
content ='Tom Hanks,USA,45\r\n'*1024
filename ='python_select.csv'

# Upload a CSV file.
bucket.put_object(key, content)
# Configure the parameters for the SelectObject operation.
csv_meta_params = {'RecordDelimiter': '\r\n'}
select_csv_params = {'CsvHeaderInfo': 'None',
                    'RecordDelimiter': '\r\n',
                    'LineRange': (500, 1000)}

csv_header = bucket.create_select_object_meta(key, csv_meta_params)
print(csv_header.rows)
print(csv_header.splits)
result = bucket.select_object(key, "select * from ossobject where _3 > 44", select_call_back, select_csv_params)
select_content = result.read()
print(select_content)

result = bucket.select_object_to_file(key, filename,
      "select * from ossobject where _3 > 44", select_call_back, select_csv_params)
bucket.delete_object(key)

###JSON DOCUMENT
key =  'python_select.json'
content =  "{\"contacts\":[{\"key1\":1,\"key2\":\"hello world1\"},{\"key1\":2,\"key2\":\"hello world2\"}]}"
filename =  'python_select.json'
# Upload a JSON DOCUMENT object.
bucket.put_object(key, content)
select_json_params = {'Json_Type': 'DOCUMENT'}
result = bucket.select_object(key, "select s.key2 from ossobject.contacts[*] s where s.key1 = 1", None, select_json_params)
select_content = result.read()
print(select_content)

result = bucket.select_object_to_file(key, filename,
      "select s.key2 from ossobject.contacts[*] s where s.key1 = 1", None, select_json_params)
bucket.delete_object(key)

###JSON LINES
key =  'python_select_lines.json'
content =  "{\"key1\":1,\"key2\":\"hello world1\"}\n{\"key1\":2,\"key2\":\"hello world2\"}"
filename =  'python_select.json'
# Upload a JSON LINES object.
bucket.put_object(key, content)
select_json_params = {'Json_Type': 'LINES'}
json_header = bucket.create_select_object_meta(key,select_json_params)
print(json_header.rows)
print(json_header.splits)

result = bucket.select_object(key, "select s.key2 from ossobject s where s.key1 = 1", None, select_json_params)
select_content =  result.read()
print(select_content)
result = bucket.select_object_to_file(key, filename,
           "select s.key2 from ossobject s where s.key1 = 1", None, select_json_params)
bucket.delete_object(key)
`


### Use the OSS API


If your business requires a high level of customization, you can directly call RESTful APIs. To directly call an API, you must include the signature calculation in your code. For more information, see [SelectObject](https://www.alibabacloud.com/help/en/oss/developer-reference/selectobject#reference-lz1-r1x-b2b).


Thank you! We've received your  feedback.