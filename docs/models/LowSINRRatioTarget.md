# openapi_client.model.low_sinr_ratio_target.LowSINRRatioTarget

This data type is the \"ExpectationTarget\" data type with specialisations for LowSINRatioTarget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;ExpectationTarget\&quot; data type with specialisations for LowSINRatioTarget | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**targetName** | str,  | str,  |  | [optional] must be one of ["LowSINRRatio", ] 
**targetCondition** | str,  | str,  |  | [optional] must be one of ["IS_LESS_THAN", ] 
**targetValueRange** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**targetContexts** | [**LowSINRContext**](LowSINRContext.md) | [**LowSINRContext**](LowSINRContext.md) |  | [optional] 
**targetFulfilmentInfo** | [**FulfilmentInfo**](FulfilmentInfo.md) | [**FulfilmentInfo**](FulfilmentInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

