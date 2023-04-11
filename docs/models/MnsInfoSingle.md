# openapi_client.model.mns_info_single.MnsInfoSingle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mnsLabel** | str,  | str,  |  | [optional] 
**mnsType** | str,  | str,  |  | [optional] must be one of ["ProvMnS", "FaultSupervisionMnS", "StreamingDataReportingMnS", "FileDataReportingMnS", ] 
**mnsVersion** | str,  | str,  |  | [optional] 
**mnsAddress** | str,  | str,  |  | [optional] 
**[mnsScope](#mnsScope)** | list, tuple,  | tuple,  | List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mnsScope

List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the managed object instances that can be accessed using the MnS. If a complete SubNetwork can be accessed using the MnS, this attribute may contain the DN of the SubNetwork instead of the DNs of the individual managed entities within the SubNetwork. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

