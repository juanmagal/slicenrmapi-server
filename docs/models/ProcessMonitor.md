# openapi_client.model.process_monitor.ProcessMonitor

This data type is the \"ProcessMonitor\" data type without specialisations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;ProcessMonitor\&quot; data type without specialisations. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**jobId** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["NOT_STARTED", "RUNNING", "FINSHED", "FAILED", "PARTIALLY_FAILED", "CANCELLING", "CANCELLED", ] 
**progressPercentage** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**progressStateInfo** | str,  | str,  |  | [optional] 
**resultStateInfo** | str,  | str,  |  | [optional] 
**startTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**endTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**timer** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

