# openapi_client.model.expectation_target.ExpectationTarget

This data type is the \"ExpectationTarget\" data type without specialisations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;ExpectationTarget\&quot; data type without specialisations | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**targetName** | str,  | str,  |  | [optional] 
**targetCondition** | [**Condition**](Condition.md) | [**Condition**](Condition.md) |  | [optional] 
**targetValueRange** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[targetContexts](#targetContexts)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetContexts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TargetContext**](TargetContext.md) | [**TargetContext**](TargetContext.md) | [**TargetContext**](TargetContext.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

