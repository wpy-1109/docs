# PutBucketRTC

Enables or disables the Replication Time Control (RTC) feature for existing cross-region replication (CRR) rules.

Request syntax
 
PUT /?rtc HTTP/1.1
Host: BucketName.oss-cn-hangzhou.aliyuncs.com
Date: GMT Date
Content-Length: ContentLength
Content-Type: application/xml
Authorization: SignatureValue

<?xml version="1.0" encoding="UTF-8"?>
<ReplicationRule>
    <RTC>
        <Status>enabled or disabled</Status>
    </RTC>
    <ID>rule id</ID>
</ReplicationRule>
Request headers

All headers in a PutBucketRTC request are common request headers. For more information, see Common request headers.

Request parameters

Parameter

	

Type

	

Required

	

Example

	

Description




ReplicationRule

	

Container

	

Yes

	

N/A

	

The container that stores the RTC configurations.

Parent nodes: none

Child nodes: RTC and RuleID




RTC

	

Container

	

Yes

	

N/A

	

The container that stores the status of the RTC feature.

Parent nodes: ReplicationRule

Child nodes: Status




Status

	

String

	

Yes

	

enabled

	

The status of the RTC feature.

Default value: disabled. Valid values:

enabled: The RTC feature is enabled.

Important

When the RTC feature is enabled, if historical data replication is in progress or the replication rule does not take effect, the status of the RTC feature is enabling. If historical data replication is complete or historical data replication is not selected, and the replication rule takes effect, the status of the RTC feature is enabled.

disabled: The RTC feature is disabled.

Parent nodes: RTC

Child nodes: none




ID

	

String

	

Yes

	

test_replication_rule_1

	

The ID of the CRR rule for which you want to configure the status of the RTC feature. You can call the DeleteBucketReplication operation to obtain the ID of the CRR rule.

Parent nodes: ReplicationRule

Child nodes: Status

Response headers

All headers in the response to a PutBucketRTC request are common response headers. For more information, see Common response headers.

Examples

Sample requests

 
PUT /?rtc HTTP/1.1
Host: oss-example.oss-cn-hangzhou.aliyuncs.com
Date: Thu, 21 Jul 2022 15:39:18 GMT
Content-Length: 46
Content-Type: application/xml
Authorization: OSS qn6q**************:77Dv****************


<?xml version="1.0" encoding="UTF-8"?>
<ReplicationRule>
    <RTC>
        <Status>enabled</Status>
    </RTC>
    <ID>test_replication_rule_1</ID>
</ReplicationRule>

Sample responses

 
HTTP/1.1 200 OK
x-oss-request-id: 534B371674E88A4D8906****
Date: Thu, 21 Jul 2022 15:39:18 GMT
Content-Length: 0
Connection: close
Server: AliyunOSS
OSS SDKs

You can use OSS SDKs for the following programming languages to call the PutBucketRTC operation:

Java

Python

Go V2

ossutil

For information about the ossutil command that corresponds to the PutBucketRTC operation, see put-bucket-rtc.

Error codes

Error code

	

HTTP status code

	

Description




ReplicationLocationNotSupportRtc

	

400 BadRequest

	

The RTC feature is unavailable in this region. For more information about the regions in which the RTC feature is available, see Overview.




BucketReplicationInClosingStatus

	

400 BadRequest

	

If the CRR rule is disabled, you cannot enable or disable the RTC feature.




BucketReplicationNotSupportRtc

	

400 BadRequest

	

The current CRR rule does not support the RTC feature. Contact technical support to troubleshoot and resolve the issues.