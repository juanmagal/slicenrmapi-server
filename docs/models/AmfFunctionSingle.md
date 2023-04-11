# openapi_client.model.amf_function_single.AmfFunctionSingle

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
**amfIdentifier** | [**AmfIdentifier**](AmfIdentifier.md) | [**AmfIdentifier**](AmfIdentifier.md) |  | [optional] 
**sBIFqdn** | str,  | str,  |  | [optional] 
**interPlmnFQDN** | str,  | str,  |  | [optional] 
**taiList** | [**TaiList**](TaiList.md) | [**TaiList**](TaiList.md) |  | [optional] 
**[taiRangeList](#taiRangeList)** | list, tuple,  | tuple,  |  | [optional] 
**weightFactor** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cNSIIdList** | [**CNSIIdList**](CNSIIdList.md) | [**CNSIIdList**](CNSIIdList.md) |  | [optional] 
**[gUAMIdList](#gUAMIdList)** | list, tuple,  | tuple,  |  | [optional] 
**[backupInfoAmfFailure](#backupInfoAmfFailure)** | list, tuple,  | tuple,  |  | [optional] 
**[backupInfoAmfRemoval](#backupInfoAmfRemoval)** | list, tuple,  | tuple,  |  | [optional] 
**amfSetRef** | str,  | str,  |  | [optional] 
**managedNFProfile** | [**ManagedNFProfile**](ManagedNFProfile.md) | [**ManagedNFProfile**](ManagedNFProfile.md) |  | [optional] 
**commModelList** | [**CommModelList**](CommModelList.md) | [**CommModelList**](CommModelList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# taiRangeList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TaiRange**](TaiRange.md) | [**TaiRange**](TaiRange.md) | [**TaiRange**](TaiRange.md) |  | 

# gUAMIdList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GUAMInfo**](GUAMInfo.md) | [**GUAMInfo**](GUAMInfo.md) | [**GUAMInfo**](GUAMInfo.md) |  | 

# backupInfoAmfFailure

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GUAMInfo**](GUAMInfo.md) | [**GUAMInfo**](GUAMInfo.md) | [**GUAMInfo**](GUAMInfo.md) |  | 

# backupInfoAmfRemoval

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GUAMInfo**](GUAMInfo.md) | [**GUAMInfo**](GUAMInfo.md) | [**GUAMInfo**](GUAMInfo.md) |  | 

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**EP_N2** | [**EPN2Multiple**](EPN2Multiple.md) | [**EPN2Multiple**](EPN2Multiple.md) |  | [optional] 
**EP_N8** | [**EPN8Multiple**](EPN8Multiple.md) | [**EPN8Multiple**](EPN8Multiple.md) |  | [optional] 
**EP_N11** | [**EPN11Multiple**](EPN11Multiple.md) | [**EPN11Multiple**](EPN11Multiple.md) |  | [optional] 
**EP_N12** | [**EPN12Multiple**](EPN12Multiple.md) | [**EPN12Multiple**](EPN12Multiple.md) |  | [optional] 
**EP_N14** | [**EPN14Multiple**](EPN14Multiple.md) | [**EPN14Multiple**](EPN14Multiple.md) |  | [optional] 
**EP_N15** | [**EPN15Multiple**](EPN15Multiple.md) | [**EPN15Multiple**](EPN15Multiple.md) |  | [optional] 
**EP_N17** | [**EPN17Multiple**](EPN17Multiple.md) | [**EPN17Multiple**](EPN17Multiple.md) |  | [optional] 
**EP_N20** | [**EPN20Multiple**](EPN20Multiple.md) | [**EPN20Multiple**](EPN20Multiple.md) |  | [optional] 
**EP_N22** | [**EPN22Multiple**](EPN22Multiple.md) | [**EPN22Multiple**](EPN22Multiple.md) |  | [optional] 
**EP_N26** | [**EPN26Multiple**](EPN26Multiple.md) | [**EPN26Multiple**](EPN26Multiple.md) |  | [optional] 
**EP_NLS** | [**EPNLSMultiple**](EPNLSMultiple.md) | [**EPNLSMultiple**](EPNLSMultiple.md) |  | [optional] 
**EP_NLG** | [**EPNLGMultiple**](EPNLGMultiple.md) | [**EPNLGMultiple**](EPNLGMultiple.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

