# openapi_client.model.low_dlranue_thpt_context.LowDLRANUEThptContext

This data type is the \"TargetContext\" data type with specialisations for LowDLRANUEThptContext      

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;TargetContext\&quot; data type with specialisations for LowDLRANUEThptContext       | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contextAttribute** | str,  | str,  |  | [optional] must be one of ["LowDLRANUEThptThreshold", ] 
**contextCondition** | str,  | str,  |  | [optional] must be one of ["IS_LESS_THAN", ] 
**contextValueRange** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

