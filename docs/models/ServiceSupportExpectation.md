# openapi_client.model.service_support_expectation.ServiceSupportExpectation

This data type is the \"IntentExpectation\" data type with specialisations to represent MnS consumer's expectations for service deployment    

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;IntentExpectation\&quot; data type with specialisations to represent MnS consumer&#x27;s expectations for service deployment     | 

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
[**ServiceSupportExpectationObject**](ServiceSupportExpectationObject.md) | [**ServiceSupportExpectationObject**](ServiceSupportExpectationObject.md) | [**ServiceSupportExpectationObject**](ServiceSupportExpectationObject.md) |  | 

# expectationTargets

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
[DLThptPerUETarget](DLThptPerUETarget.md) | [**DLThptPerUETarget**](DLThptPerUETarget.md) | [**DLThptPerUETarget**](DLThptPerUETarget.md) |  | 
[ULThptPerUETarget](ULThptPerUETarget.md) | [**ULThptPerUETarget**](ULThptPerUETarget.md) | [**ULThptPerUETarget**](ULThptPerUETarget.md) |  | 
[DLLatencyTarget](DLLatencyTarget.md) | [**DLLatencyTarget**](DLLatencyTarget.md) | [**DLLatencyTarget**](DLLatencyTarget.md) |  | 
[ULLatencyTarget](ULLatencyTarget.md) | [**ULLatencyTarget**](ULLatencyTarget.md) | [**ULLatencyTarget**](ULLatencyTarget.md) |  | 
[MaxNumberofUEsTarget](MaxNumberofUEsTarget.md) | [**MaxNumberofUEsTarget**](MaxNumberofUEsTarget.md) | [**MaxNumberofUEsTarget**](MaxNumberofUEsTarget.md) |  | 
[ActivityFactorTarget](ActivityFactorTarget.md) | [**ActivityFactorTarget**](ActivityFactorTarget.md) | [**ActivityFactorTarget**](ActivityFactorTarget.md) |  | 
[UESpeedTarget](UESpeedTarget.md) | [**UESpeedTarget**](UESpeedTarget.md) | [**UESpeedTarget**](UESpeedTarget.md) |  | 
[ExpectationTarget](ExpectationTarget.md) | [**ExpectationTarget**](ExpectationTarget.md) | [**ExpectationTarget**](ExpectationTarget.md) |  | 

# expectationContexts

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
[ServiceStartTimeContext](ServiceStartTimeContext.md) | [**ServiceStartTimeContext**](ServiceStartTimeContext.md) | [**ServiceStartTimeContext**](ServiceStartTimeContext.md) |  | 
[ServiceEndTimeContext](ServiceEndTimeContext.md) | [**ServiceEndTimeContext**](ServiceEndTimeContext.md) | [**ServiceEndTimeContext**](ServiceEndTimeContext.md) |  | 
[UEMobilityLevelContext](UEMobilityLevelContext.md) | [**UEMobilityLevelContext**](UEMobilityLevelContext.md) | [**UEMobilityLevelContext**](UEMobilityLevelContext.md) |  | 
[ResourceSharingLevelContext](ResourceSharingLevelContext.md) | [**ResourceSharingLevelContext**](ResourceSharingLevelContext.md) | [**ResourceSharingLevelContext**](ResourceSharingLevelContext.md) |  | 
[ExpectationContext](ExpectationContext.md) | [**ExpectationContext**](ExpectationContext.md) | [**ExpectationContext**](ExpectationContext.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

