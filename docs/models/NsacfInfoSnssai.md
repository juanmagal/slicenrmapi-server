# openapi_client.model.nsacf_info_snssai.NsacfInfoSnssai

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SnssaiInfo** | [**SnssaiInfo**](SnssaiInfo.md) | [**SnssaiInfo**](SnssaiInfo.md) |  | [optional] 
**isSubjectToNsac** | bool,  | BoolClass,  |  | [optional] 
**maxNumberofUEs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**eACMode** | str,  | str,  |  | [optional] must be one of ["INACTIVE", "ACTIVE", ] 
**activeEacThreshhold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**deactiveEacThreshhold** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**numberofUEs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[uEIdList](#uEIdList)** | list, tuple,  | tuple,  |  | [optional] 
**maxNumberofPDUSessions** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# uEIdList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

