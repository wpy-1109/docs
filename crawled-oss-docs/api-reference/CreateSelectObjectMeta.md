# Object-level operations

You can call the CreateSelectObjectMeta operation to obtain information about an object, such as the total number of rows and the number of splits. For a CSV object, you can also obtain the total number of columns in the object when you call this operation. An object consists of multiple data blocks. Each data block corresponds to a split. A split consists of consecutive rows. If the requested information does not exist in the CSV or JSON object, the entire object is scanned to analyze and record the preceding information. The information obtained in the first API operation call is used when the operation is called again. This way, the entire object does not need to be rescanned.

Usage notes

To call the CreateSelectObjectMeta operation, you must have write permissions on the object.

If the operation is successful, HTTP status code 200 is returned. If the object is not a valid CSV or JSON LINES object, or if the specified delimiter does not match existing CSV objects, HTTP status code 400 is returned.

Syntax

This operation supports the following request syntax for CSV and JSON objects.

Request syntax for CSV objects

 
POST  /samplecsv?x-oss-process=csv/meta
<CsvMetaRequest>
    <InputSerialization>
        <CompressionType>None</CompressionType>
        <CSV>
            <RecordDelimiter>Base64-encoded character</RecordDelimiter>
            <FieldDelimiter>Base64-encoded character</FieldDelimiter>
            <QuoteCharacter>Base64-encoded character</QuoteCharacter>
        </CSV>
    </InputSerialization>
    <OverwriteIfExists>false|true</OverwriteIfExists>
</CsvMetaRequest>

Request syntax for JSON objects

 
POST  /samplecsv?x-oss-process=json/meta
<JsonMetaRequest>
    <InputSerialization>
        <CompressionType>None</CompressionType>
        <JSON>
            <Type>LINES</Type>
        </JSON>
    </InputSerialization>
    <OverwriteIfExists>false|true</OverwriteIfExists>
</JsonMetaRequest>
Request elements

Element

	

Type

	

Description




CsvMetaRequest

	

Container

	

The container that stores the CreateSelectObjectMeta request for CSV objects.

Child nodes: InputSerialization

Parent nodes: none




JsonMetaRequest

	

Container

	

The container that stores the CreateSelectObjectMeta request for JSON objects.

Child nodes: InputSerialization

Parent nodes: none




InputSerialization

	

Container

	

Optional. Specifies the input serialization parameters.

Child nodes: CompressionType, CSV, and JSON

Parent nodes: CsvMetaRequest and JsonMetaRequest




OverwriteIfExists

	

bool

	

Optional. Specifies whether to recalculate the SelectMeta and overwrite the existing data. The value false indicates that the result is directly returned if the SelectMeta already exists. Default value: false.

Child nodes: none

Parent nodes: CsvMetaRequest and JsonMetaRequest




CompressionType

	

Enumeration

	

Optional. The compression type of the object. Valid value: None.

Child nodes: none

Parent nodes: InputSerialization




RecordDelimiter

	

String

	

Optional. The Base64-encoded line feed that you want to use to separate rows in the CSV object. Default value: \n. Before the value of this element is encoded, the value must be an ANSI value of up to two characters in length. For example, \n is used to indicate a line feed in Java.

Child nodes: none

Parent nodes: CSV




FieldDelimiter

	

String

	

Optional. The delimiter that you want to use to separate values in the CSV object. The value of this parameter must be Base64-encoded. Default value: ,.

Before the value of this element is encoded, the value must be an ANSI value of one character in length. For example, , is used to indicate a comma in Java.

Child nodes: none

Parent nodes: CSV (input and output)




QuoteCharacter

	

String

	

Optional. The Base64-encoded quote character that you want to use in the CSV object. Default value: \". In a CSV object, line feeds and column delimiters enclosed in quotation marks are processed as normal characters. Before the value of this element is encoded, the value must be an ANSI value of one character in length. For example, \" is used to indicate a quotation mark in Java.

Child nodes: none

Parent nodes: CSV (input)




CSV

	

Container

	

The format of the input CSV object.

Child nodes: RecordDelimiter, FieldDelimiter, and QuoteCharacter

Parent nodes: InputSerialization




JSON

	

Container

	

The format of the input JSON object.

Child nodes: Type

Parent nodes: InputSerialization




Type

	

Enumeration

	

The type of the JSON object.

Valid value: LINES.

Response headers

Similar to SelectObject, the results of CreateSelectObjectMeta are also returned as frames.

Frame type

	

Value

	

Payload format

	

Description




Meta End Frame (CSV)

	

8388614

	

offset | total scanned bytes | status| splits count | rows count | columns count | error message

<-8 bytes><------8 bytes------><--4bytes><--4 bytes--><--8 bytes><--4 bytes---><variable size>

	

The frame used to report the final state of a CreateSelectObjectMeta operation.

offset: an 8-bit integer that indicates the offset when scanning is complete.

total scanned bytes: an 8-bit integer that indicates the size of the scanned data.

status: a 4-bit integer that indicates the final state of the operation.

splits_count: a 4-bit integer that indicates the total number of splits.

rows_count: an 8-bit integer that indicates the total number of rows.

cols_count: a 4-bit integer that indicates the total number of columns.

error_message: the detailed error message that is returned. If no errors occur, the value of this parameter is null.




Meta End Frame (JSON)

	

8388615

	

offset | total scanned bytes | status| splits count | rows count | error message

<-8 bytes><------8 bytes------><--4bytes><--4 bytes--><--8 bytes><variable size>

	

The frame used to report the final state of a CreateSelectObjectMeta operation.

offset: an 8-bit integer that indicates the offset when scanning is complete.

total scanned bytes: an 8-bit integer that indicates the size of the scanned data.

status: a 4-bit integer that indicates the final state of the operation.

splits_count: a 4-bit integer that indicates the total number of splits.

rows_count: an 8-bit integer that indicates the total number of rows.

error_message: the detailed error message that is returned. If no errors occur, the value of this parameter is null.

Sample requests

The following sample requests are used to call SelectObject for CSV and JSON objects:

Sample requests for CSV objects

 
POST /oss-select/bigcsv_normal.csv?x-oss-process=csv%2Fmeta HTTP/1.1
Date: Fri, 25 May 2018 23:06:41 GMT
Content-Type:
Authorization: OSS qn6q**************:77Dv****************
User-Agent: aliyun-sdk-dotnet/2.8.0.0(windows 16.7/16.7.0.0/x86;4.0.30319.42000)
Content-Length: 309
Expect: 100-continue
Connection: keep-alive
Host: Host
<?xml version="1.0"?>
<CsvMetaRequest>
    <InputSerialization>
        <CSV>
            <RecordDelimiter>Cg==</RecordDelimiter>
            <FieldDelimiter>LA==</FieldDelimiter>
            <QuoteCharacter>Ig==</QuoteCharacter>
        </CSV>
    </InputSerialization>
    <OverwriteIfExisting>false</OverwriteIfExisting>
</CsvMetaRequest>

Sample requests for JSON objects

 
POST /oss-select/sample.json?x-oss-process=json%2Fmeta HTTP/1.1
Date: Fri, 25 May 2018 23:06:41 GMT
Content-Type:
Authorization: OSS qn6q**************:77Dv****************
User-Agent: aliyun-sdk-dotnet/2.8.0.0(windows 16.7/16.7.0.0/x86;4.0.30319.42000)
Content-Length: 309
Expect: 100-continue
Connection: keep-alive
Host: Host
<?xml version="1.0"?>
<JsonMetaRequest>
    <InputSerialization>
        <JSON>
            <Type>LINES</Type>
        </JSON>
    </InputSerialization>
    <OverwriteIfExisting>false</OverwriteIfExisting>
</JsonMetaRequest>
ossutil

For more information about the ossutil command that corresponds to the CreateSelectObjectMeta operation, see create-select-object-meta.