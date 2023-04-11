# openapi_client.model.file_download_job_process_monitor.FileDownloadJobProcessMonitor

This data type is the \"ProcessMonitor\" data type with specialisations for usage in the \"FileDownloadJob\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;ProcessMonitor\&quot; data type with specialisations for usage in the \&quot;FileDownloadJob\&quot;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**jobId** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["NOT_STARTED", "RUNNING", "FINSHED", "FAILED", "CANCELLING", "CANCELLED", ] 
**progressPercentage** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**progressStateInfo** | str,  | str,  |  | [optional] 
**[resultStateInfo](#resultStateInfo)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**startTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**endTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**timer** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# resultStateInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | str,  | str,  |  | must be one of [None, "UNKNOWN", "NO_STORAGE", "LOW_MEMROY", "NO_CONNECTION_TO_REMOTE_SERVER", "FILE_NOT_AVAILABLE", "DNS_CANNOT_BE_RESOLVED", "TIMER_EXPIRED", "OTHER", ] 
[one_of_1](#one_of_1) | str,  | str,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of [None, "UNKNOWN", "NO_STORAGE", "LOW_MEMROY", "NO_CONNECTION_TO_REMOTE_SERVER", "FILE_NOT_AVAILABLE", "DNS_CANNOT_BE_RESOLVED", "TIMER_EXPIRED", "OTHER", ] 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

