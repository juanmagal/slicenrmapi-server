# openapi_client.model.pcf_function_single.PcfFunctionSingle

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
[ManagedFunctionNcO](ManagedFunctionNcO.md) | [**ManagedFunctionNcO**](ManagedFunctionNcO.md) | [**ManagedFunctionNcO**](ManagedFunctionNcO.md) |  | 
[all_of_3](#all_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attributes](#attributes)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ManagedFunctionAttr](ManagedFunctionAttr.md) | [**ManagedFunctionAttr**](ManagedFunctionAttr.md) | [**ManagedFunctionAttr**](ManagedFunctionAttr.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**plmnIdList** | [**PlmnIdList**](PlmnIdList.md) | [**PlmnIdList**](PlmnIdList.md) |  | [optional] 
**sBIFqdn** | str,  | str,  |  | [optional] 
**snssaiList** | [**SnssaiList**](SnssaiList.md) | [**SnssaiList**](SnssaiList.md) |  | [optional] 
**managedNFProfile** | [**ManagedNFProfile**](ManagedNFProfile.md) | [**ManagedNFProfile**](ManagedNFProfile.md) |  | [optional] 
**commModelList** | [**CommModelList**](CommModelList.md) | [**CommModelList**](CommModelList.md) |  | [optional] 
**configurable5QISetRef** | str,  | str,  |  | [optional] 
**dynamic5QISetRef** | str,  | str,  |  | [optional] 
**supportedBMOList** | [**SupportedBMOList**](SupportedBMOList.md) | [**SupportedBMOList**](SupportedBMOList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**EP_N5** | [**EPN5Multiple**](EPN5Multiple.md) | [**EPN5Multiple**](EPN5Multiple.md) |  | [optional] 
**EP_N7** | [**EPN7Multiple**](EPN7Multiple.md) | [**EPN7Multiple**](EPN7Multiple.md) |  | [optional] 
**EP_N15** | [**EPN15Multiple**](EPN15Multiple.md) | [**EPN15Multiple**](EPN15Multiple.md) |  | [optional] 
**EP_N16** | [**EPN16Multiple**](EPN16Multiple.md) | [**EPN16Multiple**](EPN16Multiple.md) |  | [optional] 
**EP_Rx** | [**EPRxMultiple**](EPRxMultiple.md) | [**EPRxMultiple**](EPRxMultiple.md) |  | [optional] 
**PredefinedPccRuleSet** | [**PredefinedPccRuleSetSingle**](PredefinedPccRuleSetSingle.md) | [**PredefinedPccRuleSetSingle**](PredefinedPccRuleSetSingle.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

