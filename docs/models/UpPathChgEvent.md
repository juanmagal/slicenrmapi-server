# openapi_client.model.up_path_chg_event.UpPathChgEvent

Contains the UP path change event subscription from the AF.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Contains the UP path change event subscription from the AF. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dnaiChgType** | [**DnaiChangeType**](DnaiChangeType.md) | [**DnaiChangeType**](DnaiChangeType.md) |  | 
**notifCorreId** | str,  | str,  | It is used to set the value of Notification Correlation ID in the notification sent by the SMF. | 
**notificationUri** | str,  | str,  | String providing an URI formatted according to RFC 3986. | 
**afAckInd** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

