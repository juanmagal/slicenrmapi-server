# openapi_client.model.sub_network_single1.SubNetworkSingle1

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
[SubNetworkNcO](SubNetworkNcO.md) | [**SubNetworkNcO**](SubNetworkNcO.md) | [**SubNetworkNcO**](SubNetworkNcO.md) |  | 
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
[SubNetworkAttr](SubNetworkAttr.md) | [**SubNetworkAttr**](SubNetworkAttr.md) | [**SubNetworkAttr**](SubNetworkAttr.md) |  | 

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SubNetwork** | [**SubNetworkMultiple**](SubNetworkMultiple.md) | [**SubNetworkMultiple**](SubNetworkMultiple.md) |  | [optional] 
**ManagedElement** | [**ManagedElementMultiple**](ManagedElementMultiple.md) | [**ManagedElementMultiple**](ManagedElementMultiple.md) |  | [optional] 
**ExternalAmfFunction** | [**ExternalAmfFunctionMultiple**](ExternalAmfFunctionMultiple.md) | [**ExternalAmfFunctionMultiple**](ExternalAmfFunctionMultiple.md) |  | [optional] 
**ExternalNrfFunction** | [**ExternalNrfFunctionMultiple**](ExternalNrfFunctionMultiple.md) | [**ExternalNrfFunctionMultiple**](ExternalNrfFunctionMultiple.md) |  | [optional] 
**ExternalNssfFunction** | [**ExternalNssfFunctionMultiple**](ExternalNssfFunctionMultiple.md) | [**ExternalNssfFunctionMultiple**](ExternalNssfFunctionMultiple.md) |  | [optional] 
**AmfSet** | [**AmfSetMultiple**](AmfSetMultiple.md) | [**AmfSetMultiple**](AmfSetMultiple.md) |  | [optional] 
**AmfRegion** | [**AmfRegionMultiple**](AmfRegionMultiple.md) | [**AmfRegionMultiple**](AmfRegionMultiple.md) |  | [optional] 
**Configurable5QISet** | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) |  | [optional] 
**Dynamic5QISet** | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) |  | [optional] 
**EcmConnectionInfo** | [**EcmConnectionInfoMultiple**](EcmConnectionInfoMultiple.md) | [**EcmConnectionInfoMultiple**](EcmConnectionInfoMultiple.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

