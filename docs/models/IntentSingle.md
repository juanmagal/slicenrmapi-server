# openapi_client.model.intent_single.IntentSingle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Top](Top.md) | [**Top**](Top.md) | [**Top**](Top.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**userLabel** | str,  | str,  |  | [optional] 
**[intentExpectations](#intentExpectations)** | list, tuple,  | tuple,  |  | [optional] 
**[intentContexts](#intentContexts)** | list, tuple,  | tuple,  |  | [optional] 
**intentFulfilmentInfo** | [**FulfilmentInfo**](FulfilmentInfo.md) | [**FulfilmentInfo**](FulfilmentInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# intentExpectations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[IntentExpectation](IntentExpectation.md) | [**IntentExpectation**](IntentExpectation.md) | [**IntentExpectation**](IntentExpectation.md) |  | 
[RadioNetworkExpectation](RadioNetworkExpectation.md) | [**RadioNetworkExpectation**](RadioNetworkExpectation.md) | [**RadioNetworkExpectation**](RadioNetworkExpectation.md) |  | 
[ServiceSupportExpectation](ServiceSupportExpectation.md) | [**ServiceSupportExpectation**](ServiceSupportExpectation.md) | [**ServiceSupportExpectation**](ServiceSupportExpectation.md) |  | 

# intentContexts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IntentContext**](IntentContext.md) | [**IntentContext**](IntentContext.md) | [**IntentContext**](IntentContext.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

