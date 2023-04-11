# openapi_client.model.condition_data.ConditionData

Contains conditions of applicability for a rule.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Contains conditions of applicability for a rule. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**condId** | str,  | str,  | Uniquely identifies the condition data within a PDU session. | 
**activationTime** | [**DateTimeRm**](DateTimeRm.md) | [**DateTimeRm**](DateTimeRm.md) |  | [optional] 
**deactivationTime** | [**DateTimeRm**](DateTimeRm.md) | [**DateTimeRm**](DateTimeRm.md) |  | [optional] 
**accessType** | [**AccessType**](AccessType.md) | [**AccessType**](AccessType.md) |  | [optional] 
**ratType** | [**RatType**](RatType.md) | [**RatType**](RatType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

