# Object-level operations

Executes SQL statements to perform operations on an object and obtains the execution results.

Usage notes

You must be granted read permissions on the object.

If an SQL statement is executed correctly, HTTP status code 206 is returned. If an SQL statement is invalid or cannot match existing objects, HTTP status code 400 is returned.

You are charged based on the size of the objects that are scanned when you call the SelectObject operation. For more information, see Data processing fees.

Request syntax

This operation supports the following request syntax for CSV and JSON objects.

Request syntax for CSV objects

 
POST /object?x-oss-process=csv/select HTTP/1.1 
HOST: BucketName.oss-cn-hangzhou.aliyuncs.com 
Date: time GMT
Content-Length: ContentLength
Content-MD5: MD5Value 
Authorization: Signature
<?xml  version="1.0"  encoding="UTF-8"?>
<SelectRequest>    
    <Expression>Base64-encoded SQL statement. Example: c2VsZWN0IGNvdW50KCopIGZyb20gb3Nzb2JqZWN0IHdoZXJlIF80ID4gNDU=</Expression>
    <InputSerialization>
        <CompressionType>None|GZIP</CompressionType>
        <CSV>            
            <FileHeaderInfo>
                NONE|IGNORE|USE
            </FileHeaderInfo>
            <RecordDelimiter>Base64-encoded character</RecordDelimiter>
            <FieldDelimiter>Base64-encoded character</FieldDelimiter>
            <QuoteCharacter>Base64-encoded character</QuoteCharacter>
            <CommentCharacter>Base64-encoded character</CommentCharacter>
            <Range>line-range=start-end|split-range=start-end</Range>
            <AllowQuotedRecordDelimiter>true|false</AllowQuotedRecordDelimiter>
        </CSV>   
        </InputSerialization>
        <OutputSerialization>
             <CSV>
             <RecordDelimiter>Base64-encoded character</RecordDelimiter>
             <FieldDelimiter>Base64-encoded character</FieldDelimiter>

            </CSV>
            <KeepAllColumns>false|true</KeepAllColumns>
            <OutputRawData>false|true</OutputRawData>
            <EnablePayloadCrc>true</EnablePayloadCrc>
            <OutputHeader>false</OutputHeader>
       </OutputSerialization>
     <Options>
        <SkipPartialDataRecord>false</SkipPartialDataRecord>
        <MaxSkippedRecordsAllowed>
        max allowed number of records skipped
        </MaxSkippedRecordsAllowed>
    </Options>
</SelectRequest>

Request syntax for JSON objects

 
POST /object?x-oss-process=json/select HTTP/1.1 
HOST: BucketName.oss-cn-hangzhou.aliyuncs.com 
Date: time GMT
Content-Length: ContentLength
Content-MD5: MD5Value 
Authorization: Signature
<?xml  version="1.0"  encoding="UTF-8"?>
<SelectRequest>    
    <Expression>
        Base64-encoded SQL statement. Example: c2VsZWN0IGNvdW50KCopIGZyb20gb3Nzb2JqZWN0IHdoZXJlIF80ID4gNDU=
    </Expression>
    <InputSerialization>
        <CompressionType>None|GZIP</CompressionType>
        <JSON>
            <Type>DOCUMENT|LINES</Type>
            <Range>
            line-range=start-end|split-range=start-end
            </Range>
            <ParseJsonNumberAsString> true|false
            </ParseJsonNumberAsString>
        </JSON>
    </InputSerialization>
    <OutputSerialization>
        <JSON>
            <RecordDelimiter>
                Base64 of record delimiter
            </RecordDelimiter>
        </JSON>
        <OutputRawData>false|true</OutputRawData>
                 <EnablePayloadCrc>true</EnablePayloadCrc>
    </OutputSerialization>
    <Options>
        <SkipPartialDataRecord>
            false|true
        </SkipPartialDataRecord>
        <MaxSkippedRecordsAllowed>
            max allowed number of records skipped
           </MaxSkippedRecordsAllowed>
        </Options>
</SelectRequest>
Request elements

Element

	

Type

	

Description




SelectRequest

	

Container

	

The container that stores the SelectObject request.

Child nodes: Expression, InputSerialization, and OutputSerialization

Parent nodes: none




Expression

	

String

	

The Base64-encoded SQL statement.

Child nodes: none

Parent nodes: SelectRequest




InputSerialization

	

Container

	

Optional. This element specifies the input serialization parameters.

Child nodes: CompressionType, CSV, and JSON

Parent nodes: SelectRequest




OutputSerialization

	

Container

	

Optional. This element specifies the output serialization parameters.

Child nodes: CSV, JSON, and OutputRawData

Parent nodes: SelectRequest




CSV(InputSerialization)

	

Container

	

Optional. This element specifies the input serialization parameters when the CSV object is queried.

Child nodes: FileHeaderInfo, RecordDelimiter, FieldDelimiter, QuoteCharacter, CommentCharacter, and Range

Parent nodes: InputSerialization




CSV(OutputSerialization)

	

Container

	

Optional. This element specifies the output serialization parameters when the CSV object is queried.

Child nodes: RecordDelimiter and FieldDelimiter

Parent nodes: OutputSerialization




JSON(InputSerialization)

	

Container

	

Optional. This element specifies the input serialization parameters when the JSON object is queried.

Child nodes: Type, Range, and ParseJsonNumberAsString




JSON(OutputSerialization)

	

Container

	

Optional. This element specifies the output serialization parameters when the JSON object is queried.

Child nodes: RecordDelimiter




Type

	

Enumeration

	

The type of the input JSON object. Valid values: DOCUMENT and LINES.




OutputRawData

	

Boolean

	

Optional. This element specifies whether to export raw data. Default value: false.

Child nodes: none

Parent nodes: OutputSerialization

Note

If you specify OutputRawData in the request, Object Storage Service (OSS) returns data based on the request element.

If you do not specify OutputRawData in the request, OSS automatically selects a format and returns data in the selected format in the response.

If you set OutputRawData to true and it takes a long time for the sent SQL statement to return data, the HTTP request may time out.




CompressionType

	

Enumeration

	

The compression type of the object. Valid value: None and GZIP.

Child nodes: none

Parent nodes: InputSerialization




FileHeaderInfo

	

Enumeration

	

Optional. This element specifies the header information about the CSV object.

Valid values:

Use: The CSV object contains header information. You can use the column names in the CSV object as the column names in the SelectObject operation.

Ignore: The CSV object contains header information. The column names in the CSV object cannot be used as the column names in the SelectObject operation.

None: The CSV object does not contain header information. This is the default value.

Child nodes: none

Parent nodes: CSV (input)




RecordDelimiter

	

String

	

Optional. This element specifies a Base64-encoded line feed. Default value: \n. Before the value of this element is encoded, the value must be an ANSI value of up to two characters in length. For example, \n is used to indicate a line feed in Java.

Child nodes: none

Parent nodes: CSV (input and output) and JSON (output)




FieldDelimiter

	

String

	

Optional. This element specifies the delimiter that you want to use to separate columns in the CSV object. The value of this element must be Base64-encoded. Default value: ,. Before the value of this element is encoded, the value must be an ANSI value of one character in length. For example, , is used to indicate a comma in Java.

Child nodes: none

Parent nodes: CSV (input and output)




QuoteCharacter

	

String

	

Optional. This element specifies a Base64-encoded quote character that you want to use in the CSV object. Default value: \". In a CSV object, line feeds and column delimiters enclosed in quotation marks are processed as normal characters. Before the value of this element is encoded, the value must be an ANSI value of one character in length. For example, \" is used to indicate a quote character in Java.

Child nodes: none

Parent nodes: CSV (input)




CommentCharacter

	

String

	

The comment character that you want to use in the CSV object. The value of this element must be Base64-encoded. This element is empty by default.




Range

	

String

	

Optional. This element specifies the query range. The following query methods are supported:

Note

SelectMeta must be created for objects that are queried based on Range.

Query by row: line-range=start-end. For example, line-range=10-20 indicates that data from row 10 to row 20 is scanned.

Query by split: split-range=start-end. For example, split-range=10-20 indicates that data from split 10 to split 20 is scanned.

The start and end parameters are inclusive. The two preceding parameters use the same format as that of the range parameter in range get.

This parameter can be used only if the object is in the CSV format or if the JSON type is LINES.

Child nodes: none

Parent nodes: CSV (input) and JSON (output)




KeepAllColumns

	

bool

	

Optional. This element specifies whether all columns in the CSV object are included in the response. Default value: false. Only columns included in the SELECT clause contain values. The columns in the response are sorted in ascending order of the column numbers. Example:

select _5, _1 from ossobject.

If you set KeepAllColumns to true and six columns are included in the CSV object, the following result is returned for the preceding SELECT clause:

Value of 1st column,,,,Value of 5th column,\n

Child nodes: none

Parent nodes: OutputSerialization (CSV)




EnablePayloadCrc

	

bool

	

The CRC-32 value for verification of each frame. The client can calculate the CRC-32 value of each payload and compare it with the included CRC-32 value to verify data integrity.

Child nodes: none

Parent nodes: OutputSerialization




Options

	

Container

	

Other optional parameters.

Child nodes: SkipPartialDataRecord and MaxSkippedRecordsAllowed

Parent nodes: SelectRequest




OutputHeader

	

bool

	

Specifies whether the header information about the CSV object is included in the beginning of the response.

Default value: false.

Child nodes: none

Parent nodes: OutputSerialization




SkipPartialDataRecord

	

bool

	

Specifies whether to ignore rows in which data is missing. If this parameter is set to false, OSS processes the row data as null without reporting errors. If this parameter is set to true, rows that do not contain data are skipped. If the number of skipped rows has exceeded the maximum number of rows that can be skipped, OSS reports an error and stops processing the data.

Default value: false.

Child nodes: none

Parent nodes: Options




MaxSkippedRecordsAllowed

	

Int

	

The maximum number of rows that can be skipped. If a row does not match the type specified in the SQL statement, or if one or more columns in a row are missing and the value of SkipPartialDataRecord is true, the rows are skipped. If the number of skipped rows has exceeded the value of this parameter, OSS reports an error and stops processing the data.

Note

If a row in a CSV object is not correctly formatted, OSS stops processing the data and reports an error because this format error may result in incorrect parsing of the CSV object. For example, a column in the row includes continual odd numbered quote characters. This parameter can be used to modify the tolerance for irregular data but cannot be configured for invalid CSV objects.

Default value: 0.

Child nodes: none

Parent nodes: Options




ParseJsonNumberAsString

	

bool

	

Specifies whether to parse integer and floating-point numbers in the JSON object into strings. The precision of floating-point numbers in a JSON object decreases when the numbers are parsed. If you want to retain the raw data, we recommend that you set this parameter to true. To use the parsed numbers in calculations, you can use the CAST function in SQL to convert the parsed data into the required type such as INT, DOUBLE, or DECIMAL.

Default value: false.

Child nodes: none

Parent nodes: JSON




AllowQuotedRecordDelimiter

	

bool

	

Specifies whether the CSV object can contain line feeds in quotation marks (").

For example, if the value of a column is "abc\ndef" and \n is a line feed, set this parameter to true. If this parameter is set to false, you can call the SelectObject operation to specify a range in the request header to perform more efficient multipart queries.

Default value: true.

Child nodes: none

Parent nodes: InputSerialization

Response body

If the HTTP status code included in the response is 4xx, the request failed to pass the SQL syntax check or the request contains errors. In this case, the format of the body of the returned error message is the same as that of the error message returned for a GetObject request.

If the HTTP status code included in the response is 5xx, internal server errors occur. In this case, the format of the body of the returned error message is the same as that of the error message returned for a GetObject request.

HTTP status code 206 is returned if the operation is successful.

If the value of header x-oss-select-output-raw is true, the object data except for frame-based data is returned. The client can obtain the data in the same manner as the GetObject operation.

If the value of x-oss-select-output-raw is false, the result is returned as frames.

The frames are returned in the Version|Frame-Type | Payload Length | Header Checksum | Payload | Payload Checksum<1 byte><--3 bytes--><---4 bytes----><-------4 bytes--><variable><----4bytes----------> format.

Note

The value of Checksum in frames is CRC-32. All integers in a frame are big-endian. Currently, the value of Version is 1.

Frame Type

The following table describes three frame types supported by SelectObject.

Frame type

	

Value

	

Payload format

	

Description




Data Frame

	

8388609

	

offset | data<-8 bytes><---variable->

	

The data returned for the SelectObject request. The value of the offset parameter is an 8-bit integer that indicates the current scanning location (the offset from the file header). This parameter is used to report the progress of the operation.




Continuous Frame

	

8388612

	

offset<----8 bytes-->

	

The frame used to report the progress of an operation and maintain an HTTP connection. If no data is returned for a query request within 5 seconds, a continuous frame is returned.




End Frame

	

8388613

	

offset | total scanned bytes | http status code | error message<--8bytes-><--8bytes---------><----4 bytes--------><-variable------>

	

An end frame is used to return the final state of an operation, including the scanned bytes and the possible error messages.

The offset parameter indicates the final location offset after scanning is complete.

The total scanned bytes parameter indicates the size o