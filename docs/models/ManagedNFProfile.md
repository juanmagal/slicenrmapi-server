# openapi_client.model.managed_nf_profile.ManagedNFProfile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nfInstanceID** | str,  | str,  |  | [optional] 
**nfType** | [**NFType**](NFType.md) | [**NFType**](NFType.md) |  | [optional] 
**heartbeatTimer** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**authzInfo** | str,  | str,  |  | [optional] 
**hostAddr** | [**HostAddr**](HostAddr.md) | [**HostAddr**](HostAddr.md) |  | [optional] 
**[allowedPLMNs](#allowedPLMNs)** | list, tuple,  | tuple,  |  | [optional] 
**[allowedSNPNs](#allowedSNPNs)** | list, tuple,  | tuple,  |  | [optional] 
**[allowedNfTypes](#allowedNfTypes)** | list, tuple,  | tuple,  |  | [optional] 
**[allowedNfDomains](#allowedNfDomains)** | list, tuple,  | tuple,  |  | [optional] 
**[allowedNSSAIs](#allowedNSSAIs)** | list, tuple,  | tuple,  |  | [optional] 
**locality** | str,  | str,  |  | [optional] 
**nFInfo** | [**NFInfo**](NFInfo.md) | [**NFInfo**](NFInfo.md) |  | [optional] 
**capacity** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[nfSetIdList](#nfSetIdList)** | list, tuple,  | tuple,  |  | [optional] 
**[servingScope](#servingScope)** | list, tuple,  | tuple,  |  | [optional] 
**[nfSetRecoveryTimeList](#nfSetRecoveryTimeList)** | list, tuple,  | tuple,  |  | [optional] 
**[scpDomains](#scpDomains)** | list, tuple,  | tuple,  |  | [optional] 
**vendorId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# allowedPLMNs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PlmnId**](PlmnId.md) | [**PlmnId**](PlmnId.md) | [**PlmnId**](PlmnId.md) |  | 

# allowedSNPNs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SnpnInfo**](SnpnInfo.md) | [**SnpnInfo**](SnpnInfo.md) | [**SnpnInfo**](SnpnInfo.md) |  | 

# allowedNfTypes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NFType**](NFType.md) | [**NFType**](NFType.md) | [**NFType**](NFType.md) |  | 

# allowedNfDomains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# allowedNSSAIs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Snssai**](Snssai.md) | [**Snssai**](Snssai.md) | [**Snssai**](Snssai.md) |  | 

# nfSetIdList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# servingScope

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# nfSetRecoveryTimeList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# scpDomains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

