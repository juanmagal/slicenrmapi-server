# openapi_client.model.radio_network_expectation_object.RadioNetworkExpectationObject

This data type is the \"ExpectationObject\" data type with specialisations for RadioNetworkExpectation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This data type is the \&quot;ExpectationObject\&quot; data type with specialisations for RadioNetworkExpectation | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**objectType** | str,  | str,  |  | [optional] must be one of ["RAN_SubNetwork", ] 
**objectInstance** | str,  | str,  |  | [optional] 
**[objectContexts](#objectContexts)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# objectContexts

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
[CoverageAreaPolygonContext](CoverageAreaPolygonContext.md) | [**CoverageAreaPolygonContext**](CoverageAreaPolygonContext.md) | [**CoverageAreaPolygonContext**](CoverageAreaPolygonContext.md) |  | 
[CoverageTACContext](CoverageTACContext.md) | [**CoverageTACContext**](CoverageTACContext.md) | [**CoverageTACContext**](CoverageTACContext.md) |  | 
[PLMNContext](PLMNContext.md) | [**PLMNContext**](PLMNContext.md) | [**PLMNContext**](PLMNContext.md) |  | 
[NRFqBandContext](NRFqBandContext.md) | [**NRFqBandContext**](NRFqBandContext.md) | [**NRFqBandContext**](NRFqBandContext.md) |  | 
[RATContext](RATContext.md) | [**RATContext**](RATContext.md) | [**RATContext**](RATContext.md) |  | 
[ObjectContext](ObjectContext.md) | [**ObjectContext**](ObjectContext.md) | [**ObjectContext**](ObjectContext.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

