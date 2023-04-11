# openapi_client.model.node_filter.NodeFilter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**areaOfInterest** | [**AreaOfInterest**](AreaOfInterest.md) | [**AreaOfInterest**](AreaOfInterest.md) |  | [optional] 
**networkDomain** | str,  | str,  |  | [optional] must be one of ["CN", "RAN", ] 
**cpUpType** | str,  | str,  |  | [optional] must be one of ["CP", "UP", ] 
**sst** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

