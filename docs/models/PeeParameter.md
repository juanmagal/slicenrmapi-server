# openapi_client.model.pee_parameter.PeeParameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**siteIdentification** | str,  | str,  |  | [optional] 
**siteDescription** | str,  | str,  |  | [optional] 
**siteLatitude** | [**Latitude**](Latitude.md) | [**Latitude**](Latitude.md) |  | [optional] 
**siteLongitude** | [**Longitude**](Longitude.md) | [**Longitude**](Longitude.md) |  | [optional] 
**siteAltitude** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**equipmentType** | str,  | str,  |  | [optional] 
**environmentType** | str,  | str,  |  | [optional] 
**powerInterface** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

