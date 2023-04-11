# openapi_client.model.managed_function_attr.ManagedFunctionAttr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**userLabel** | str,  | str,  |  | [optional] 
**[vnfParametersList](#vnfParametersList)** | list, tuple,  | tuple,  |  | [optional] 
**[peeParametersList](#peeParametersList)** | list, tuple,  | tuple,  |  | [optional] 
**priorityLabel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[supportedPerfMetricGroups](#supportedPerfMetricGroups)** | list, tuple,  | tuple,  |  | [optional] 
**[supportedTraceMetrics](#supportedTraceMetrics)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vnfParametersList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VnfParameter**](VnfParameter.md) | [**VnfParameter**](VnfParameter.md) | [**VnfParameter**](VnfParameter.md) |  | 

# peeParametersList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeeParameter**](PeeParameter.md) | [**PeeParameter**](PeeParameter.md) | [**PeeParameter**](PeeParameter.md) |  | 

# supportedPerfMetricGroups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SupportedPerfMetricGroup**](SupportedPerfMetricGroup.md) | [**SupportedPerfMetricGroup**](SupportedPerfMetricGroup.md) | [**SupportedPerfMetricGroup**](SupportedPerfMetricGroup.md) |  | 

# supportedTraceMetrics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

