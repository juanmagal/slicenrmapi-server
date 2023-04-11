# openapi_client.model.managed_element_attr.ManagedElementAttr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dnPrefix** | str,  | str,  |  | [optional] 
**[managedElementTypeList](#managedElementTypeList)** | list, tuple,  | tuple,  |  | [optional] 
**userLabel** | str,  | str,  |  | [optional] 
**locationName** | str,  | str,  |  | [optional] 
**managedBy** | [**DnList**](DnList.md) | [**DnList**](DnList.md) |  | [optional] 
**vendorName** | str,  | str,  |  | [optional] 
**userDefinedState** | str,  | str,  |  | [optional] 
**swVersion** | str,  | str,  |  | [optional] 
**priorityLabel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[supportedPerfMetricGroups](#supportedPerfMetricGroups)** | list, tuple,  | tuple,  |  | [optional] 
**[supportedTraceMetrics](#supportedTraceMetrics)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# managedElementTypeList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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

