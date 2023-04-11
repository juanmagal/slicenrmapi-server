# openapi_client.model.five_qi_characteristics_single.FiveQICharacteristicsSingle

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

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fiveQIValue** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**resourceType** | str,  | str,  |  | [optional] must be one of ["GBR", "NonGBR", ] 
**priorityLevel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**packetDelayBudget** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**packetErrorRate** | [**PacketErrorRate**](PacketErrorRate.md) | [**PacketErrorRate**](PacketErrorRate.md) |  | [optional] 
**averagingWindow** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**maximumDataBurstVolume** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

