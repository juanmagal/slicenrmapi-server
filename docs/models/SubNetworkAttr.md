# openapi_client.model.sub_network_attr.SubNetworkAttr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dnPrefix** | str,  | str,  |  | [optional] 
**userLabel** | str,  | str,  |  | [optional] 
**userDefinedNetworkType** | str,  | str,  |  | [optional] 
**[setOfMcc](#setOfMcc)** | list, tuple,  | tuple,  |  | [optional] 
**priorityLabel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[supportedPerfMetricGroups](#supportedPerfMetricGroups)** | list, tuple,  | tuple,  |  | [optional] 
**[supportedTraceMetrics](#supportedTraceMetrics)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# setOfMcc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Mcc**](Mcc.md) | [**Mcc**](Mcc.md) | [**Mcc**](Mcc.md) |  | 

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

