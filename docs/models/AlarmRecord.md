# openapi_client.model.alarm_record.AlarmRecord

The alarmId is not a property of an alarm record. It is used as key in the map of alarm records instead.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The alarmId is not a property of an alarm record. It is used as key in the map of alarm records instead. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**objectInstance** | str,  | str,  |  | [optional] 
**notificationId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**alarmRaisedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**alarmChangedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**alarmClearedTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**alarmType** | [**AlarmType**](AlarmType.md) | [**AlarmType**](AlarmType.md) |  | [optional] 
**probableCause** | [**ProbableCause**](ProbableCause.md) | [**ProbableCause**](ProbableCause.md) |  | [optional] 
**specificProblem** | [**SpecificProblem**](SpecificProblem.md) | [**SpecificProblem**](SpecificProblem.md) |  | [optional] 
**perceivedSeverity** | [**PerceivedSeverity**](PerceivedSeverity.md) | [**PerceivedSeverity**](PerceivedSeverity.md) |  | [optional] 
**backedUpStatus** | bool,  | BoolClass,  |  | [optional] 
**backUpObject** | str,  | str,  |  | [optional] 
**trendIndication** | [**TrendIndication**](TrendIndication.md) | [**TrendIndication**](TrendIndication.md) |  | [optional] 
**thresholdinfo** | [**ThresholdInfo1**](ThresholdInfo1.md) | [**ThresholdInfo1**](ThresholdInfo1.md) |  | [optional] 
**correlatedNotifications** | [**CorrelatedNotifications**](CorrelatedNotifications.md) | [**CorrelatedNotifications**](CorrelatedNotifications.md) |  | [optional] 
**stateChangeDefinition** | [**AttributeValueChangeSet**](AttributeValueChangeSet.md) | [**AttributeValueChangeSet**](AttributeValueChangeSet.md) |  | [optional] 
**monitoredAttributes** | [**AttributeNameValuePairSet**](AttributeNameValuePairSet.md) | [**AttributeNameValuePairSet**](AttributeNameValuePairSet.md) |  | [optional] 
**proposedRepairActions** | str,  | str,  |  | [optional] 
**additionalText** | str,  | str,  |  | [optional] 
**additionalInformation** | [**AttributeNameValuePairSet**](AttributeNameValuePairSet.md) | [**AttributeNameValuePairSet**](AttributeNameValuePairSet.md) |  | [optional] 
**rootCauseIndicator** | bool,  | BoolClass,  |  | [optional] 
**ackTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**ackUserId** | str,  | str,  |  | [optional] 
**ackSystemId** | str,  | str,  |  | [optional] 
**ackState** | [**AckState**](AckState.md) | [**AckState**](AckState.md) |  | [optional] 
**clearUserId** | str,  | str,  |  | [optional] 
**clearSystemId** | str,  | str,  |  | [optional] 
**serviceUser** | str,  | str,  |  | [optional] 
**serviceProvider** | str,  | str,  |  | [optional] 
**securityAlarmDetector** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

