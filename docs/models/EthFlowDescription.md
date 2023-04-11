# openapi_client.model.eth_flow_description.EthFlowDescription

Identifies an Ethernet flow.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Identifies an Ethernet flow. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ethType** | str,  | str,  |  | 
**destMacAddr** | [**MacAddr48**](MacAddr48.md) | [**MacAddr48**](MacAddr48.md) |  | [optional] 
**fDesc** | str,  | str,  | Defines a packet filter of an IP flow. | [optional] 
**fDir** | [**FlowDirection**](FlowDirection.md) | [**FlowDirection**](FlowDirection.md) |  | [optional] 
**sourceMacAddr** | [**MacAddr48**](MacAddr48.md) | [**MacAddr48**](MacAddr48.md) |  | [optional] 
**[vlanTags](#vlanTags)** | list, tuple,  | tuple,  |  | [optional] 
**srcMacAddrEnd** | [**MacAddr48**](MacAddr48.md) | [**MacAddr48**](MacAddr48.md) |  | [optional] 
**destMacAddrEnd** | [**MacAddr48**](MacAddr48.md) | [**MacAddr48**](MacAddr48.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vlanTags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

