# openapi_client.model.nf_profile.NFProfile

NF profile stored in NRF, defined in TS 29.510

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NF profile stored in NRF, defined in TS 29.510 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nFInstanceId** | str,  | str,  | uuid of NF instance | [optional] 
**nFType** | [**NFType**](NFType.md) | [**NFType**](NFType.md) |  | [optional] 
**nFStatus** | [**NFStatus**](NFStatus.md) | [**NFStatus**](NFStatus.md) |  | [optional] 
**plmn** | [**PlmnId**](PlmnId.md) | [**PlmnId**](PlmnId.md) |  | [optional] 
**sNssais** | [**Snssai**](Snssai.md) | [**Snssai**](Snssai.md) |  | [optional] 
**fqdn** | str,  | str,  |  | [optional] 
**interPlmnFqdn** | str,  | str,  |  | [optional] 
**[nfServices](#nfServices)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nfServices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NFService**](NFService.md) | [**NFService**](NFService.md) | [**NFService**](NFService.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

