# openapi_client.model.time_domain_para.TimeDomainPara

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dlULSwitchingPeriod1** | str,  | str,  |  | [optional] must be one of ["MS0P5", "MS0P625", "MS1", "MS1P25", "MS2", "MS2P5", "MS3", "MS4", "MS5", "MS10", "MS20", ] 
**symbolOffsetOfReferencePoint1** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**dlULSwitchingPeriod2** | str,  | str,  |  | [optional] must be one of ["MS0P5", "MS0P625", "MS1", "MS1P25", "MS2", "MS2P5", "MS3", "MS4", "MS5", "MS10", "MS20", ] 
**symbolOffsetOfReferencePoint2** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**totalnrofSetIdofRS1** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**totalnrofSetIdofRS2** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**nrofConsecutiveRIMRS1** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**nrofConsecutiveRIMRS2** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[consecutiveRIMRS1List](#consecutiveRIMRS1List)** | list, tuple,  | tuple,  |  | [optional] 
**[consecutiveRIMRS2List](#consecutiveRIMRS2List)** | list, tuple,  | tuple,  |  | [optional] 
**enablenearfarIndicationRS1** | str,  | str,  |  | [optional] must be one of ["ENABLE", "DISABLE", ] 
**enablenearfarIndicationRS2** | str,  | str,  |  | [optional] must be one of ["ENABLE", "DISABLE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# consecutiveRIMRS1List

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# consecutiveRIMRS2List

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

