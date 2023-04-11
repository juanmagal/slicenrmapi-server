# openapi_client.model.report_interval_type.ReportIntervalType

See details in 3GPP TS 32.422 clause 5.10.5.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | See details in 3GPP TS 32.422 clause 5.10.5. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[UMTS](#UMTS)** | list, tuple,  | tuple,  |  | [optional] 
**[LTE](#LTE)** | list, tuple,  | tuple,  |  | [optional] 
**[NR](#NR)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# UMTS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["250ms", "500ms", "1000ms", "2000ms", "3000ms", "4000ms", "6000ms", "8000ms", "12000ms", "16000ms", "20000ms", "24000ms", "28000ms", "32000ms", "64000ms", ] 

# LTE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["120ms", "240ms", "480ms", "640ms", "1024ms", "2048ms", "5120ms", "10240ms", "60000ms", "360000ms", "720000ms", "1800000ms", "3600000ms", ] 

# NR

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["120ms", "240ms", "480ms", "640ms", "1024ms", "2048ms", "5120ms", "10240ms", "20480ms", "40960ms", "60000ms", "360000ms", "720000ms", "1800000ms", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

