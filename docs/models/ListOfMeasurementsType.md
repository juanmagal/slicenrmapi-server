# openapi_client.model.list_of_measurements_type.ListOfMeasurementsType

See details in 3GPP TS 32.422 clause 5.10.3 for details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | See details in 3GPP TS 32.422 clause 5.10.3 for details. | 

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
items | str,  | str,  |  | must be one of ["M1", "M2", "M3", "M4", "M5", "M6_DL", "M6_UL", "M7_DL", "M7_UL", ] 

# LTE

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["M1", "M2", "M3", "M4", "M5", "M1_EVENT_TRIGGERED", "M6", "M7", "M8", "M9", ] 

# NR

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M1_EVENT_TRIGGERED", "M8", "M9", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

