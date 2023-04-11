# openapi_client.model.intent_expectation.IntentExpectation

This data type is the \"IntentExpectation\" data type without specialisations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;IntentExpectation\&quot; data type without specialisations | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**expectationId** | str,  | str,  |  | [optional] 
**expectationVerb** | [**ExpectationVerb**](ExpectationVerb.md) | [**ExpectationVerb**](ExpectationVerb.md) |  | [optional] 
**[expectationObjects](#expectationObjects)** | list, tuple,  | tuple,  |  | [optional] 
**[expectationTargets](#expectationTargets)** | list, tuple,  | tuple,  |  | [optional] 
**[expectationContexts](#expectationContexts)** | list, tuple,  | tuple,  |  | [optional] 
**expectationfulfilmentInfo** | [**FulfilmentInfo**](FulfilmentInfo.md) | [**FulfilmentInfo**](FulfilmentInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# expectationObjects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExpectationObject**](ExpectationObject.md) | [**ExpectationObject**](ExpectationObject.md) | [**ExpectationObject**](ExpectationObject.md) |  | 

# expectationTargets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExpectationTarget**](ExpectationTarget.md) | [**ExpectationTarget**](ExpectationTarget.md) | [**ExpectationTarget**](ExpectationTarget.md) |  | 

# expectationContexts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExpectationContext**](ExpectationContext.md) | [**ExpectationContext**](ExpectationContext.md) | [**ExpectationContext**](ExpectationContext.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

