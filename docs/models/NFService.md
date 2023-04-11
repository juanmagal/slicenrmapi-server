# openapi_client.model.nf_service.NFService

NF Service is defined in TS 29.510

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NF Service is defined in TS 29.510 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**serviceInstanceId** | str,  | str,  |  | [optional] 
**serviceName** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**schema** | str,  | str,  |  | [optional] 
**fqdn** | str,  | str,  |  | [optional] 
**interPlmnFqdn** | str,  | str,  |  | [optional] 
**[ipEndPoints](#ipEndPoints)** | list, tuple,  | tuple,  |  | [optional] 
**apiPrfix** | str,  | str,  |  | [optional] 
**allowedPlmns** | [**PlmnId**](PlmnId.md) | [**PlmnId**](PlmnId.md) |  | [optional] 
**[allowedNfTypes](#allowedNfTypes)** | list, tuple,  | tuple,  |  | [optional] 
**[allowedNssais](#allowedNssais)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ipEndPoints

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IpEndPoint**](IpEndPoint.md) | [**IpEndPoint**](IpEndPoint.md) | [**IpEndPoint**](IpEndPoint.md) |  | 

# allowedNfTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NFType**](NFType.md) | [**NFType**](NFType.md) | [**NFType**](NFType.md) |  | 

# allowedNssais

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Snssai**](Snssai.md) | [**Snssai**](Snssai.md) | [**Snssai**](Snssai.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

