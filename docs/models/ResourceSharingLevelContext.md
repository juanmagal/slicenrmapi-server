# openapi_client.model.resource_sharing_level_context.ResourceSharingLevelContext

This data type is the \"ExpectationContext\" data type with specialisations for ResourceSharingLevelContext          

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;ExpectationContext\&quot; data type with specialisations for ResourceSharingLevelContext           | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contextAttribute** | str,  | str,  |  | [optional] must be one of ["ResourceSharingLevel", ] 
**contextCondition** | str,  | str,  |  | [optional] must be one of ["IS_WITHIN_RANGE", ] 
**[contextValueRange](#contextValueRange)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contextValueRange

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharingLevel**](SharingLevel.md) | [**SharingLevel**](SharingLevel.md) | [**SharingLevel**](SharingLevel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

