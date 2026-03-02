# DoMetaQuery

Call the DoMetaQuery operation to query objects that meet specified conditions and list the object information based on a specified field and sorting order. You can also use nested Query elements to perform complex queries and use aggregate operations to collect and analyze statistics on the values of different fields.

Precautions

To query objects that meet specified conditions, you must have the oss:DoMetaQuery permission. For more information, see Grant custom permissions to a RAM user.

Request syntax
Scalar retrievalVector retrieval
 
POST /?metaQuery&comp=query&mode=basic HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue 
<?xml version="1.0" encoding="UTF-8"?>
<MetaQuery>
  <NextToken></NextToken>
  <MaxResults>5</MaxResults>
  <Query>{"Field": "Size","Value": "1048576","Operation": "gt"}</Query>
  <Sort>Size</Sort>
  <Order>asc</Order>
  <Aggregations>
    <Aggregation>
      <Field>Size</Field>
      <Operation>sum</Operation>
    </Aggregation>
    <Aggregation>
      <Field>Size</Field>
      <Operation>max</Operation>
    </Aggregation>
  </Aggregations>
</MetaQuery>
Request headers

All headers in a DescribeRegions request are common request headers. For more information, see Common request headers.

Request elements
Scalar retrievalVector retrieval

Name

	

Type

	

Required

	

Example

	

Description




mode

	

String

	

Yes

	

basic

	

Specifies that the retrieval mode is scalar retrieval.




MetaQuery

	

Container

	

Yes

	

N/A

	

The container for query conditions.

Child nodes: NextToken, MaxResults, Query, Sort, Order, and Aggregations




NextToken

	

String

	

No

	

MTIzNDU2Nzg6aW1tdGVzdDpleGFtcGxlYnVja2V0OmRhdGFzZXQwMDE6b3NzOi8vZXhhbXBsZWJ1Y2tldC9zYW1wbGVvYmplY3QxLmpw****

	

The token used for pagination when the total number of objects is greater than the value of MaxResults.

The list of object information is returned in lexicographical order starting from the object that is specified by NextToken.

When you call this operation for the first time, leave this field empty.

Parent node: MetaQuery




MaxResults

	

Integer

	

No

	

5

	

The maximum number of objects to return. Valid values: 0 to 100.

If you do not set this parameter or set it to 0, the default value is 100.

Parent node: MetaQuery




Query

	

String

	

Yes

	

{"Field": "Size","Value": "1048576","Operation": "gt"}

	

The query condition. It includes the following options:

Operation: The operator. Valid values: eq (equal to), gt (greater than), gte (greater than or equal to), lt (less than), lte (less than or equal to), match (fuzzy query), prefix (prefix query), and (logical AND), or (logical OR), and not (logical NOT).

Field: The field name. For more information about the supported fields and the operators supported by each field, see Appendix: Fields and operators for scalar retrieval.

Value: The field value.

SubQueries: The subquery conditions. The options are the same as those for simple query conditions. You need to set subquery conditions only when Operation is a logical operator (and, or, or not).

For more information about Query examples, see DoMetaQuery.

Parent node: MetaQuery




Sort

	

String

	

No

	

Size

	

Sorts the results by a specified field. For more information about the fields that support sorting, see Appendix: Fields and operators for scalar retrieval.

Parent node: MetaQuery




Order

	

String

	

No

	

asc

	

The sorting order. Valid values:

asc: ascending

desc (default): descending

Parent node: MetaQuery




Aggregations

	

Container

	

No

	

N/A

	

The container for the information about aggregate operations.

Child node: Aggregation

Parent node: MetaQuery




Aggregation

	

Container

	

No

	

N/A

	

The container for the information about a single aggregate operation.

Child nodes: Field and Operation

Parent node: Aggregations




Field

	

String

	

No

	

Size

	

The field name. For more information about the supported fields and the operators supported by each field, see Appendix: Fields and operators for scalar retrieval.

Parent node: Aggregation




Operation

	

String

	

No

	

sum

	

The operator in the aggregate operation. Valid values:

min: minimum value

max: maximum value

average: average value

sum: sum

count: count

distinct: deduplicated count

group: group count

Parent node: Aggregation

Response headers

All headers in the response to a DescribeRegions request are common response headers. For more information, see Common response headers.

Response elements
Scalar retrievalVector retrieval

Name

	

Type

	

Example

	

Description




MetaQuery

	

Container

	

N/A

	

The container for query results.

Child nodes: NextToken, Files, and Aggregations




NextToken

	

String

	

MTIzNDU2Nzg6aW1tdGVzdDpleGFtcGxlYnVja2V0OmRhdGFzZXQwMDE6b3NzOi8vZXhhbXBsZWJ1Y2tldC9zYW1wbGVvYmplY3QxLmpw****

	

The token used for pagination when the total number of objects is greater than the value of MaxResults.

In the next request to list object information, use this value for NextToken to return the remaining results.

This parameter is returned only when not all objects are returned.

Parent node: MetaQuery




Files

	

Container

	

N/A

	

The container for object information.

Child node: File

Parent node: MetaQuery




File

	

Container

	

N/A

	

The container for the information about a single object.

Child nodes: Filename, Size, FileModifiedTime, OSSObjectType, OSSStorageClass, ObjectACL, ETag, OSSTaggingCount, OSSTagging, and OSSCRC64

Parent node: Files




Filename

	

String

	

exampleobject.txt

	

The full path of the object.

Parent node: File




Size

	

Integer

	

120

	

The size of the object in bytes.

Parent node: File




FileModifiedTime

	

String

	

2025-05-19T16:14:38+08:00

	

The last modified time of the object. The format is RFC3339Nano.

Parent node: File




OSSObjectType

	

String

	

Normal

	

The type of the object. Valid values:

Normal: The object is uploaded by calling the PutObject operation or created by calling the CreateDirectory operation.

Appendable: The object is uploaded by calling the AppendObject operation.

Multipart: The object is uploaded by calling the MultipartUpload operation.

Symlink: The symbolic link is created by calling the PutSymlink operation.

Parent node: File




OSSStorageClass

	

String

	

Standard

	

The storage class of the object. Valid values:

Standard: The Standard storage class provides a highly reliable, highly available, and high-performance object storage service that supports frequent data access.

IA: The Infrequent Access storage class is suitable for data that is stored for a long time but infrequently accessed (once or twice a month on average).

Archive: The Archive Storage class is suitable for archived data that requires long-term storage (more than six months is recommended). The data is rarely accessed during its storage lifecycle. It takes 1 minute to restore the data before it can be read.

ColdArchive: The Cold Archive storage class is suitable for data that is stored for a long time and is rarely accessed.

Parent node: File




ObjectACL

	

String

	

default

	

The access control list (ACL) of the object. Valid values:

default: The object inherits the access permissions of the bucket in which it is stored.

private: The object is a private resource. Only the object owner and authorized users have read and write permissions on the object. Other users cannot access the object.

public-read: The object is a public-read resource. Only the object owner and authorized users have read and write permissions on the object. Other users have only read permissions on the object. Use this permission with caution.

public-read-write: The object is a public-read-write resource. All users have read and write permissions on the object. Use this permission with caution.

Parent node: File




ETag

	

String

	

"fba9dede5f27731c9771645a3986****"

	

When an object is created, a corresponding ETag is generated. The ETag is used to identify the content of an object.

For an object created by a PutObject request, the ETag value is the MD5 hash of its content.

For an object created in other ways, the ETag value is a unique value generated based on specific calculation rules, but it is not the MD5 hash of its content.

Note

The ETag value can be used to check whether the object content has changed. We do not recommend that you use the ETag value as the MD5 hash of the object content to verify data integrity.

Parent node: File




OSSTaggingCount

	

Integer

	

2

	

The number of tags of the object.

Parent node: File




OSSTagging

	

Container

	

N/A

	

The container for tag information.

Child node: Tagging

Parent node: File




Tagging

	

Container

	

N/A

	

The container for the information about a single tag.

Child nodes: Key and Value

Parent node: OSSTagging




Key

	

String

	

owner

	

The key of the tag or user-defined metadata.

The key of user-defined metadata must be prefixed with x-oss-meta-.

Parent nodes: Tagging and UserMeta




Value

	

String

	

John

	

The value of the tag or user-defined metadata.

Parent nodes: Tagging and UserMeta




OSSCRC64

	

String

	

4858A48BD1466884

	

The 64-bit CRC value of the object. The 64-bit CRC value is calculated based on the CRC-64/XZ standard.

Parent node: File




Aggregations

	

Container

	

N/A

	

The container for the information about aggregate operations.

Child nodes: Field, Operation, Operation, Value, and Groups

Parent node: MetaQuery




Field

	

String

	

Size

	

The field name.

Parent node: Aggregations




Operation

	

String

	

sum

	

The aggregate operator.

Parent node: Aggregations




Value

	

Floating-point number

	

200

	

The result value of the aggregate operation.

Parent node: Aggregations




Groups

	

Container

	

N/A

	

The list of results of grouping and aggregation.

Child nodes: Value and Count

Parent node: Aggregations




Value

	

String

	

100

	

The value of the grouping and aggregation.

Parent node: Groups




Count

	

Integer

	

5

	

The total number of grouping and aggregation results.

Parent node: Groups

Examples
Request examples
Scalar retrievalVector retrieval
 
POST /?metaQuery&comp=query&mode=basic HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Authorization: SignatureValue 
<?xml version="1.0" encoding="UTF-8"?>
<MetaQuery>
  <NextToken></NextToken>
  <MaxResults>5</MaxResults>
  <Query>{"Field": "Size","Value": "1048576","Operation": "gt"}</Query>
  <Sort>Size</Sort>
  <Order>asc</Order>
  <Aggregations>
    <Aggregation>
      <Field>Size</Field>
      <Operation>sum</Operation>
    </Aggregation>
    <Aggregation>
      <Field>Size</Field>
      <Operation>max</Operation>
    </Aggregation>
  </Aggregations>
</MetaQuery>
Response examples
Scalar retrievalVector retrieval
 
HTTP/1.1 200 OK
x-oss-request-id: 5C1B138A109F4E405B2D****
Date: Mon, 26 Jul 2021 13:08:38 GMT
Content-Length: 118
Content-Type: application/xml
Connection: keep-alive
Server: AliyunOSS
<?xml version="1.0" encoding="UTF-8"?>
<MetaQuery>
  <NextToken>MTIzNDU2Nzg6aW1tdGVzdDpleGFtcGxlYnVja2V0OmRhdGFzZXQwMDE6b3NzOi8vZXhhbXBsZWJ1Y2tldC9zYW1wbGVvYmplY3QxLmpw****</NextToken>
  <Files>
    <File>
      <Filename>exampleobject.txt</Filename>
      <Size>120</Size>
      <FileModifiedTime>2025-05-19T16:14:38+08:00</FileModifiedTime>
      <OSSObjectType>Normal</OSSObjectType>
      <OSSStorageClass>Standard</OSSStorageClass>
      <ObjectACL>default</ObjectACL>
      <ETag>"fba9dede5f27731c9771645a3986****"</ETag>
      <OSSCRC64>4858A48BD1466884</OSSCRC64>
      <OSSTaggingCount>2</OSSTaggingCount>
      <OSSTagging>
        <Tagging>
          <Key>owner</Key>
          <Value>John</Value>
        </Tagging>
        <Tagging>
          <Key>type</Key>
          <Value>document</Value>
        </Tagging>
      </OSSTagging>
    </File>
  </Files>
</MetaQuery>
Query examples

You can nest Query elements to build complex query conditions and precisely query for the content you need.

To search for an object named exampleobject.txt that is smaller than 1000 bytes, configure the Query element as follows:

 

{
  "SubQueries":[
    {
      "Field":"Filename",
      "Value": "exampleobject.txt",
      "Operation":"eq"
    },         
    {
      "Field":"Size",
      "Value":"1000",
      "Operation":"lt"
    }
  ],
  "Operation":"and"
}
            

To search for objects that have the exampledir/ prefix, contain the type=document or owner=John tag, and are larger than 10 MB, configure the Query element as follows:

 

{
  "SubQueries": [
    {
      "Field": "Filename",
      "Value": "exampledir/",
      "Operation": "prefix"
    },
    {
      "Field": "Size",
      "Value": "1048576",
      "Operation": "gt"
    },
    {
      "SubQueries": [
        {
          "Field": "OSSTagging.type",
          "Value": "document",
          "Operation": "eq"
        },
        {
          "Field": "OSSTagging.owner",
          "Value": "John",
          "Operation": "eq"
        }
      ],
      "Operation": "or"
    }
  ],
  "Operation": "and"
}
        
            

In addition to these search conditions, you can use aggregate operations to perform statistical analysis on different data. For example, you can calculate the total size, count, average value, or maximum or minimum value of all objects that meet the search criteria, or collect statistics on the size distribution of all images that meet the search criteria.

SDK

The following SDKs are available for this operation:

Java

Python V2

Go V2

PHP V2

ossutil command-line tool

The DoMetaQuery operation corresponds to the do-meta-query command in ossutil.