# openapi_client.model.managed_element_single1.ManagedElementSingle1

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
[ManagedElementNcO](ManagedElementNcO.md) | [**ManagedElementNcO**](ManagedElementNcO.md) | [**ManagedElementNcO**](ManagedElementNcO.md) |  | 
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
[ManagedElementAttr](ManagedElementAttr.md) | [**ManagedElementAttr**](ManagedElementAttr.md) | [**ManagedElementAttr**](ManagedElementAttr.md) |  | 

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AmfFunction** | [**AmfFunctionMultiple**](AmfFunctionMultiple.md) | [**AmfFunctionMultiple**](AmfFunctionMultiple.md) |  | [optional] 
**SmfFunction** | [**SmfFunctionMultiple**](SmfFunctionMultiple.md) | [**SmfFunctionMultiple**](SmfFunctionMultiple.md) |  | [optional] 
**UpfFunction** | [**UpfFunctionMultiple**](UpfFunctionMultiple.md) | [**UpfFunctionMultiple**](UpfFunctionMultiple.md) |  | [optional] 
**N3iwfFunction** | [**N3iwfFunctionMultiple**](N3iwfFunctionMultiple.md) | [**N3iwfFunctionMultiple**](N3iwfFunctionMultiple.md) |  | [optional] 
**PcfFunction** | [**PcfFunctionMultiple**](PcfFunctionMultiple.md) | [**PcfFunctionMultiple**](PcfFunctionMultiple.md) |  | [optional] 
**AusfFunction** | [**AusfFunctionMultiple**](AusfFunctionMultiple.md) | [**AusfFunctionMultiple**](AusfFunctionMultiple.md) |  | [optional] 
**UdmFunction** | [**UdmFunctionMultiple**](UdmFunctionMultiple.md) | [**UdmFunctionMultiple**](UdmFunctionMultiple.md) |  | [optional] 
**UdrFunction** | [**UdrFunctionMultiple**](UdrFunctionMultiple.md) | [**UdrFunctionMultiple**](UdrFunctionMultiple.md) |  | [optional] 
**UdsfFunction** | [**UdsfFunctionMultiple**](UdsfFunctionMultiple.md) | [**UdsfFunctionMultiple**](UdsfFunctionMultiple.md) |  | [optional] 
**NrfFunction** | [**NrfFunctionMultiple**](NrfFunctionMultiple.md) | [**NrfFunctionMultiple**](NrfFunctionMultiple.md) |  | [optional] 
**NssfFunction** | [**NssfFunctionMultiple**](NssfFunctionMultiple.md) | [**NssfFunctionMultiple**](NssfFunctionMultiple.md) |  | [optional] 
**SmsfFunction** | [**SmsfFunctionMultiple**](SmsfFunctionMultiple.md) | [**SmsfFunctionMultiple**](SmsfFunctionMultiple.md) |  | [optional] 
**LmfFunction** | [**LmfFunctionMultiple**](LmfFunctionMultiple.md) | [**LmfFunctionMultiple**](LmfFunctionMultiple.md) |  | [optional] 
**NgeirFunction** | [**NgeirFunctionMultiple**](NgeirFunctionMultiple.md) | [**NgeirFunctionMultiple**](NgeirFunctionMultiple.md) |  | [optional] 
**SeppFunction** | [**SeppFunctionMultiple**](SeppFunctionMultiple.md) | [**SeppFunctionMultiple**](SeppFunctionMultiple.md) |  | [optional] 
**NwdafFunction** | [**NwdafFunctionMultiple**](NwdafFunctionMultiple.md) | [**NwdafFunctionMultiple**](NwdafFunctionMultiple.md) |  | [optional] 
**ScpFunction** | [**ScpFunctionMultiple**](ScpFunctionMultiple.md) | [**ScpFunctionMultiple**](ScpFunctionMultiple.md) |  | [optional] 
**NefFunction** | [**NefFunctionMultiple**](NefFunctionMultiple.md) | [**NefFunctionMultiple**](NefFunctionMultiple.md) |  | [optional] 
**Configurable5QISet** | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) |  | [optional] 
**Dynamic5QISet** | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) |  | [optional] 
**EcmConnectionInfo** | [**EcmConnectionInfoMultiple**](EcmConnectionInfoMultiple.md) | [**EcmConnectionInfoMultiple**](EcmConnectionInfoMultiple.md) |  | [optional] 
**EASDFFunction** | [**EASDFFunctionMultiple**](EASDFFunctionMultiple.md) | [**EASDFFunctionMultiple**](EASDFFunctionMultiple.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

