# openapi_client.model.logging_interval_type.LoggingIntervalType

See details in 3GPP TS 32.422 clause 5.10.8.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | See details in 3GPP TS 32.422 clause 5.10.8. | 

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
items | str,  | str,  |  | must be one of ["1.28s", "2.56s", "5.12s", "10.24s", "20.48s", "30.72s", "40.96s", "61.44s", ] 

# LTE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["1.28s", "2.56s", "5.12s", "10.24s", "20.48s", "30.72s", "40.96s", "61.44s", ] 

# NR

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["0.32s", "0.64s", "1.28s", "2.56s", "5.12s", "10.24s", "20.48s", "30.72s", "40.96s", "61.44s", "INFINITY", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

