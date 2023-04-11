# openapi_client.model.smf_function_single.SmfFunctionSingle

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
**pLMNInfoList** | [**PlmnInfoList**](PlmnInfoList.md) | [**PlmnInfoList**](PlmnInfoList.md) |  | [optional] 
**nRTACList** | [**TACList**](TACList.md) | [**TACList**](TACList.md) |  | [optional] 
**sBIFqdn** | str,  | str,  |  | [optional] 
**[sNssaiSmfInfoList](#sNssaiSmfInfoList)** | list, tuple,  | tuple,  |  | [optional] 
**taiList** | [**TaiList**](TaiList.md) | [**TaiList**](TaiList.md) |  | [optional] 
**[taiRangeList](#taiRangeList)** | list, tuple,  | tuple,  |  | [optional] 
**pwgFqdn** | str,  | str,  |  | [optional] 
**[pgwAddrList](#pgwAddrList)** | list, tuple,  | tuple,  |  | [optional] 
**accessType** | [**AccessType**](AccessType.md) | [**AccessType**](AccessType.md) |  | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cNSIIdList** | [**CNSIIdList**](CNSIIdList.md) | [**CNSIIdList**](CNSIIdList.md) |  | [optional] 
**vsmfSupportInd** | bool,  | BoolClass,  |  | [optional] 
**[pwgFqdnList](#pwgFqdnList)** | list, tuple,  | tuple,  |  | [optional] 
**managedNFProfile** | [**ManagedNFProfile**](ManagedNFProfile.md) | [**ManagedNFProfile**](ManagedNFProfile.md) |  | [optional] 
**commModelList** | [**CommModelList**](CommModelList.md) | [**CommModelList**](CommModelList.md) |  | [optional] 
**configurable5QISetRef** | str,  | str,  |  | [optional] 
**dynamic5QISetRef** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sNssaiSmfInfoList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SNssaiSmfInfoItem**](SNssaiSmfInfoItem.md) | [**SNssaiSmfInfoItem**](SNssaiSmfInfoItem.md) | [**SNssaiSmfInfoItem**](SNssaiSmfInfoItem.md) |  | 

# taiRangeList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TaiRange**](TaiRange.md) | [**TaiRange**](TaiRange.md) | [**TaiRange**](TaiRange.md) |  | 

# pgwAddrList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IpAddr1**](IpAddr1.md) | [**IpAddr1**](IpAddr1.md) | [**IpAddr1**](IpAddr1.md) |  | 

# pwgFqdnList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**EP_N4** | [**EPN4Multiple**](EPN4Multiple.md) | [**EPN4Multiple**](EPN4Multiple.md) |  | [optional] 
**EP_N7** | [**EPN7Multiple**](EPN7Multiple.md) | [**EPN7Multiple**](EPN7Multiple.md) |  | [optional] 
**EP_N10** | [**EPN10Multiple**](EPN10Multiple.md) | [**EPN10Multiple**](EPN10Multiple.md) |  | [optional] 
**EP_N11** | [**EPN11Multiple**](EPN11Multiple.md) | [**EPN11Multiple**](EPN11Multiple.md) |  | [optional] 
**EP_N16** | [**EPN16Multiple**](EPN16Multiple.md) | [**EPN16Multiple**](EPN16Multiple.md) |  | [optional] 
**EP_S5C** | [**EPS5CMultiple**](EPS5CMultiple.md) | [**EPS5CMultiple**](EPS5CMultiple.md) |  | [optional] 
**FiveQiDscpMappingSet** | [**FiveQiDscpMappingSetSingle**](FiveQiDscpMappingSetSingle.md) | [**FiveQiDscpMappingSetSingle**](FiveQiDscpMappingSetSingle.md) |  | [optional] 
**GtpUPathQoSMonitoringControl** | [**GtpUPathQoSMonitoringControlSingle**](GtpUPathQoSMonitoringControlSingle.md) | [**GtpUPathQoSMonitoringControlSingle**](GtpUPathQoSMonitoringControlSingle.md) |  | [optional] 
**QFQoSMonitoringControl** | [**QFQoSMonitoringControlSingle**](QFQoSMonitoringControlSingle.md) | [**QFQoSMonitoringControlSingle**](QFQoSMonitoringControlSingle.md) |  | [optional] 
**PredefinedPccRuleSet** | [**PredefinedPccRuleSetSingle**](PredefinedPccRuleSetSingle.md) | [**PredefinedPccRuleSetSingle**](PredefinedPccRuleSetSingle.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

